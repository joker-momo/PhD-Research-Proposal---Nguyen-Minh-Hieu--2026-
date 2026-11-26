#!/usr/bin/env python3
"""Run auditable OpenAlex searches for the HK261 PRISMA review.

This tool creates OpenAlex evidence only. It must not be used to claim that a
Web of Science Core Collection search was executed.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path


CSV_FIELDS = [
    "record_id",
    "source",
    "query_variant",
    "openalex_id",
    "doi",
    "title",
    "authors",
    "publication_year",
    "publication_date",
    "type",
    "language",
    "venue",
    "landing_page_url",
    "locations_count",
    "is_retracted",
]
RFC3339_SECONDS = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
)


def validate_config(config):
    required = {
        "schema_version",
        "source",
        "source_role",
        "base_url",
        "query_set_version",
        "from_date",
        "to_date",
        "language",
        "per_page",
        "select",
        "variants",
    }
    missing = sorted(required - set(config))
    if missing:
        raise ValueError("missing config fields: " + ", ".join(missing))
    if config["source"] != "OpenAlex":
        raise ValueError("source must be OpenAlex")
    if not str(config["base_url"]).startswith("https://api.openalex.org/"):
        raise ValueError("base_url must use the official OpenAlex HTTPS API")
    if not 1 <= int(config["per_page"]) <= 200:
        raise ValueError("per_page must be between 1 and 200")
    datetime.strptime(config["from_date"], "%Y-%m-%d")
    datetime.strptime(config["to_date"], "%Y-%m-%d")
    if config["from_date"] > config["to_date"]:
        raise ValueError("from_date must not be after to_date")
    variants = config["variants"]
    if not isinstance(variants, list) or not variants:
        raise ValueError("variants must be a non-empty list")
    identifiers = [variant.get("id") for variant in variants]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("duplicate variant id")
    for variant in variants:
        for field in ("id", "search_parameter", "query"):
            if not variant.get(field):
                raise ValueError("variant missing " + field)
        parameter = variant["search_parameter"]
        if parameter not in {
            "search.title_and_abstract",
            "search.title_and_abstract.exact",
        }:
            raise ValueError("unsupported search_parameter: " + parameter)
        if ("*" in variant["query"] or "?" in variant["query"]) and not parameter.endswith(
            ".exact"
        ):
            raise ValueError("wildcard queries require an exact search parameter")


def validate_observed_at(value, now=None):
    if not isinstance(value, str) or not RFC3339_SECONDS.fullmatch(value):
        raise ValueError("observed_at must include RFC3339 seconds and a known timezone")
    if value.endswith("-00:00"):
        raise ValueError("observed_at timezone must be known, not -00:00")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("observed_at must include a known timezone")
    current = now or datetime.now().astimezone()
    if parsed > current:
        raise ValueError("observed_at must not be in the future")
    return value


def _collapse_space(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _normal_doi(value):
    doi = _collapse_space(value).lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix) :]
    return doi


def _normal_title(value):
    return re.sub(r"[^a-z0-9]+", " ", _collapse_space(value).lower()).strip()


def normalize_work(record, variant_id):
    openalex_id = _collapse_space(record.get("id")).rsplit("/", 1)[-1]
    authors = []
    for authorship in record.get("authorships") or []:
        name = _collapse_space((authorship.get("author") or {}).get("display_name"))
        if name:
            authors.append(name)
    location = record.get("primary_location") or {}
    source = location.get("source") or {}
    title = _collapse_space(record.get("title") or record.get("display_name"))
    doi = _normal_doi(record.get("doi"))
    landing_page_url = _collapse_space(location.get("landing_page_url"))
    return {
        "record_id": "OPENALEX:" + openalex_id,
        "source": "OpenAlex",
        "query_variant": variant_id,
        "openalex_id": openalex_id,
        "doi": doi,
        "title": title,
        "authors": "; ".join(authors),
        "publication_year": record.get("publication_year") or "",
        "publication_date": record.get("publication_date") or "",
        "type": record.get("type") or "",
        "language": record.get("language") or "",
        "venue": _collapse_space(source.get("display_name")),
        "landing_page_url": landing_page_url,
        "locations_count": record.get("locations_count") or 0,
        "is_retracted": bool(record.get("is_retracted")),
    }


def duplicate_report(rows):
    def repeated(values):
        counts = Counter(value for value in values if value)
        return sum(count - 1 for count in counts.values() if count > 1)

    return {
        "openalex_id_duplicates": repeated(row["openalex_id"] for row in rows),
        "doi_duplicates": repeated(row["doi"] for row in rows),
        "title_duplicates": repeated(_normal_title(row["title"]) for row in rows),
    }


def _filter_string(config):
    return ",".join(
        [
            "from_publication_date:" + config["from_date"],
            "to_publication_date:" + config["to_date"],
            "language:" + config["language"],
        ]
    )


def _request_url(url, params):
    return url + "?" + urllib.parse.urlencode(params)


def collect_variant(config, variant, fetch):
    filters = _filter_string(config)
    cursor = "*"
    seen_cursors = set()
    records = []
    request_urls = []
    page_count = 0
    reported_total = None
    interpreted_query = None
    while cursor:
        if cursor in seen_cursors:
            raise RuntimeError("cursor repeated before pagination completed")
        seen_cursors.add(cursor)
        params = {
            variant["search_parameter"]: variant["query"],
            "filter": filters,
            "per-page": int(config["per_page"]),
            "cursor": cursor,
            "select": ",".join(config["select"]),
        }
        request_urls.append(_request_url(config["base_url"], params))
        page = fetch(config["base_url"], params)
        if not isinstance(page, dict) or "meta" not in page or "results" not in page:
            raise RuntimeError("OpenAlex response lacks meta/results")
        meta = page["meta"] or {}
        current_total = meta.get("count")
        if not isinstance(current_total, int) or current_total < 0:
            raise RuntimeError("OpenAlex response lacks a valid total count")
        if reported_total is None:
            reported_total = current_total
        elif reported_total != current_total:
            raise RuntimeError("OpenAlex total changed during pagination")
        x_query = meta.get("x_query")
        current_interpreted = x_query.get("oql") if isinstance(x_query, dict) else x_query
        if interpreted_query is None:
            interpreted_query = current_interpreted
        records.extend(page.get("results") or [])
        page_count += 1
        cursor = meta.get("next_cursor")
    if len(records) != reported_total:
        raise RuntimeError(
            "count mismatch: API reported {0}, collected {1}".format(reported_total, len(records))
        )
    identifiers = [record.get("id") for record in records]
    if len(identifiers) != len(set(identifiers)):
        raise RuntimeError("OpenAlex returned duplicate work IDs during pagination")
    return {
        "variant": variant["id"],
        "query": variant["query"],
        "search_parameter": variant["search_parameter"],
        "filters": filters,
        "api_reported_total": reported_total,
        "page_count": page_count,
        "interpreted_query": interpreted_query,
        "records": records,
        "request_urls": request_urls,
    }


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def write_bundle(config, result, output_dir, observed_at):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    date = observed_at[:10]
    stem = "openalex_{0}_{1}".format(result["variant"], date)
    raw_path = output_dir / (stem + "_raw.json")
    csv_path = output_dir / (stem + "_normalized.csv")
    manifest_path = output_dir / (stem + "_manifest.json")
    checksum_path = output_dir / (stem + "_checksums.sha256")
    existing = [
        path.name for path in (raw_path, csv_path, manifest_path, checksum_path) if path.exists()
    ]
    if existing:
        raise FileExistsError("refusing to overwrite evidence: " + ", ".join(existing))
    rows = [normalize_work(record, result["variant"]) for record in result["records"]]

    raw_payload = {
        "schema_version": 1,
        "source": "OpenAlex",
        "source_role": config["source_role"],
        "query_set_version": config["query_set_version"],
        "observed_at": observed_at,
        "query_variant": result["variant"],
        "search_parameter": result["search_parameter"],
        "exact_query": result["query"],
        "interpreted_query": result["interpreted_query"],
        "filters": result["filters"],
        "api_reported_total": result["api_reported_total"],
        "page_count": result["page_count"],
        "request_urls": result["request_urls"],
        "records": result["records"],
    }
    _atomic_write(
        raw_path,
        (json.dumps(raw_payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    )
    temporary_csv = csv_path.with_name(csv_path.name + ".tmp")
    with temporary_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary_csv.replace(csv_path)

    manifest = {
        "schema_version": 1,
        "source": "OpenAlex",
        "source_role": config["source_role"],
        "query_set_version": config["query_set_version"],
        "observed_at": observed_at,
        "query_variant": result["variant"],
        "search_parameter": result["search_parameter"],
        "exact_query": result["query"],
        "interpreted_query": result["interpreted_query"],
        "filters": result["filters"],
        "api_reported_total": result["api_reported_total"],
        "exported_total": len(rows),
        "page_count": result["page_count"],
        "duplicate_counts": duplicate_report(rows),
        "raw_file": raw_path.name,
        "normalized_file": csv_path.name,
        "manifest_file": manifest_path.name,
        "checksum_file": checksum_path.name,
        "sha256": {
            raw_path.name: sha256_file(raw_path),
            csv_path.name: sha256_file(csv_path),
        },
        "limitations": [
            "OpenAlex is not Web of Science Core Collection and has different coverage.",
            "Publication type is exported broadly and must be enforced during screening.",
            "Search results are supplementary/compensatory evidence until a protocol amendment adopts them.",
        ],
    }
    _atomic_write(
        manifest_path,
        (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    )
    checksum_lines = [
        "{0}  {1}".format(sha256_file(path), path.name)
        for path in (raw_path, csv_path, manifest_path)
    ]
    _atomic_write(checksum_path, ("\n".join(checksum_lines) + "\n").encode("utf-8"))
    return manifest


def make_fetcher(api_key=None, timeout=60, retries=4):
    headers = {
        "Accept": "application/json",
        "User-Agent": "HK261-PRISMA-OpenAlex-Search/1.0",
    }
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    def fetch(url, params):
        request = urllib.request.Request(_request_url(url, params), headers=headers)
        for attempt in range(retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as error:
                retryable = error.code == 429 or 500 <= error.code < 600
                if not retryable or attempt == retries:
                    body = error.read().decode("utf-8", errors="replace")
                    raise RuntimeError(
                        "OpenAlex HTTP {0}: {1}".format(error.code, body[:500])
                    ) from error
                retry_after = error.headers.get("Retry-After")
                delay = int(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt
                time.sleep(min(delay, 30))
            except urllib.error.URLError as error:
                if attempt == retries:
                    raise RuntimeError("OpenAlex network error: " + str(error)) from error
                time.sleep(min(2 ** attempt, 30))
        raise RuntimeError("OpenAlex request exhausted retries")

    return fetch


def _timestamp_now():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_config(path):
    with Path(path).open(encoding="utf-8") as handle:
        config = json.load(handle)
    validate_config(config)
    return config


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--variant", action="append", help="Run only the named variant")
    parser.add_argument("--observed-at", help="RFC3339 timestamp; defaults to current local time")
    parser.add_argument("--api-key-env", default="OPENALEX_API_KEY")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    selected = args.variant or [variant["id"] for variant in config["variants"]]
    known = {variant["id"]: variant for variant in config["variants"]}
    unknown = sorted(set(selected) - set(known))
    if unknown:
        parser.error("unknown variants: " + ", ".join(unknown))
    observed_at = args.observed_at or _timestamp_now()
    try:
        validate_observed_at(observed_at)
    except ValueError as error:
        parser.error(str(error))

    summary_path = args.output_dir / ("openalex_run_summary_" + observed_at[:10] + ".json")
    if summary_path.exists():
        parser.error("refusing to overwrite evidence: " + str(summary_path))

    fetch = make_fetcher(os.environ.get(args.api_key_env))
    manifests = []
    for variant_id in selected:
        result = collect_variant(config, known[variant_id], fetch)
        manifests.append(write_bundle(config, result, args.output_dir, observed_at))
        print(
            "{0}: reported={1} exported={2} pages={3}".format(
                variant_id,
                manifests[-1]["api_reported_total"],
                manifests[-1]["exported_total"],
                manifests[-1]["page_count"],
            )
        )

    summary = {
        "schema_version": 1,
        "source": "OpenAlex",
        "query_set_version": config["query_set_version"],
        "observed_at": observed_at,
        "config_file": str(args.config),
        "config_sha256": sha256_file(args.config),
        "variant_count": len(manifests),
        "reported_total_sum_not_deduplicated": sum(
            manifest["api_reported_total"] for manifest in manifests
        ),
        "manifests": [manifest["manifest_file"] for manifest in manifests],
        "integrity_boundary": "OpenAlex evidence only; not a Web of Science Core Collection run.",
    }
    _atomic_write(
        summary_path,
        (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    )
    print("summary: " + str(summary_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
