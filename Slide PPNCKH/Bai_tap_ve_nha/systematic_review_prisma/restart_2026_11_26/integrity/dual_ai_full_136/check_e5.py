#!/usr/bin/env python3
"""Check HK261 E5 dates by DOI against Crossref and saved publisher evidence."""

import argparse
import calendar
import csv
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
RESTART = HERE.parents[1]
ROUND_EVIDENCE = RESTART / "retrieval_round_01/round_01_evidence.json"
PUBLISHER_LOOKUP = HERE / "e5_date_check/publisher_lookup.json"
DATE_FIELDS = ("published", "issued", "published-print")


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def publisher_dates(round_evidence):
    dates = {}
    for index, item in enumerate(round_evidence["awaiting_recheck"]):
        locator = f"retrieval_round_01/round_01_evidence.json#/awaiting_recheck/{index}/publisher_evidence"
        dates[item["id"]] = (item.get("publisher_evidence", {}), locator)
    for key, item in read_json(PUBLISHER_LOOKUP).items():
        if key in dates:
            raise ValueError(f"Multiple publisher entries for {key}")
        dates[key] = (item, f"integrity/dual_ai_full_136/e5_date_check/publisher_lookup.json#/{key}")
    return dates


def targets():
    dois = {}
    ledger_files = (
        RESTART / "fulltext_screening/fulltext_screening.csv",
        RESTART / "supplemental_screening/screening_decisions.csv",
    )
    for path in ledger_files:
        for row in read_csv(path):
            key = row.get("screening_id") or row["id"]
            doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", row["doi"].strip(), flags=re.I).lower()
            if doi:
                dois.setdefault(key, set()).add(doi)
    for row in sorted(read_csv(HERE / "review_136.csv"), key=lambda item: item["record_id"]):
        reviewers = [
            name for name in ("codex", "gemini")
            if row[f"{name}_decision"] == "AWAITING_CLASSIFICATION"
            and row[f"{name}_criterion"] == "E5"
        ]
        if reviewers:
            key = row["record_id"]
            yield key, row["packet_id"], reviewers, sorted(dois.get(key, []))


def interval(parts):
    if not isinstance(parts, list) or not 1 <= len(parts) <= 3 or any(type(p) is not int for p in parts):
        raise ValueError(f"Invalid date-parts {parts!r}")
    if len(parts) == 3:
        return (date(*parts),) * 2
    if len(parts) == 2:
        year, month = parts
        return date(year, month, 1), date(year, month, calendar.monthrange(year, month)[1])
    return date(parts[0], 1, 1), date(parts[0], 12, 31)


def date_status(bounds, lower, upper):
    first, last = bounds
    if lower <= first <= last <= upper:
        return "IN_WINDOW"
    if last < lower or first > upper:
        return "OUTSIDE_WINDOW"
    return "UNCERTAIN"


def classify(work, lower, upper):
    dates = {}
    is_proceedings = work.get("type") == "proceedings-article"
    fields = (*DATE_FIELDS, "published-online") if is_proceedings else ("published-online", *DATE_FIELDS)
    for field in fields:
        if field not in work:
            continue
        parts = work[field].get("date-parts", [])
        if len(parts) != 1:
            continue
        first, last = interval(parts[0])
        dates[field] = ([first.isoformat(), last.isoformat()], date_status((first, last), lower, upper))
    if not dates:
        return "", "", "", "UNRESOLVED", "No usable publication date in Crossref."
    field = next(iter(dates))
    (first, last), status = dates[field]
    if status == "UNCERTAIN":
        return field, first, last, "UNRESOLVED", "Date precision overlaps an E5 boundary."
    if field != "published-online" and len(
        {value[1] for value in dates.values()} - {"UNCERTAIN"}
    ) > 1:
        return field, first, last, "UNRESOLVED", "Publication fields disagree across the E5 boundary."
    if status == "OUTSIDE_WINDOW" and not is_proceedings and field != "published-online":
        return field, first, last, "UNRESOLVED", "Check the journal's first online publication date."
    return field, first, last, status, "Crossref publisher-deposit evidence. Verify the assessed edition."


def fetch(target):
    key, packet, reviewers, dois = target
    result = dict(record_id=key, packet_id=packet, flagged_by=reviewers, input_dois=dois,
                  retrieved_at=datetime.now().astimezone().isoformat(timespec="seconds"))
    if len(dois) != 1 or not re.fullmatch(r"10\.\d{4,9}/\S+", dois[0]):
        return result | {"error": "Missing, invalid or conflicting DOI in the input ledgers."}
    doi = dois[0]
    url = "https://api.crossref.org/works/" + quote(doi, safe="/")
    result.update(doi=doi, source_url=url, publisher_url="https://doi.org/" + quote(doi, safe="/"))
    try:
        request = Request(url, headers={"User-Agent": "HK261-E5-Audit/1.0", "Accept": "application/json"})
        try:
            with urlopen(request, timeout=15) as response:
                result["response"] = json.load(response)
        except HTTPError as exc:
            if exc.code != 429:
                raise
            retry_after = exc.headers.get("Retry-After", "")
            delay = int(retry_after) if retry_after.isdigit() else 3
            if delay > 15:
                raise
            time.sleep(delay)
            with urlopen(request, timeout=15) as response:
                result["response"] = json.load(response)
    except (OSError, ValueError) as exc:
        result["error"] = str(exc)
    return result


def summarize(item, lower, upper, publisher=None):
    row = {field: item.get(field, "") for field in ("record_id", "packet_id", "doi", "publisher_url", "source_url")}
    row["flagged_by"] = ", ".join(item["flagged_by"])
    work = item.get("response", {}).get("message", {})
    error = item.get("error")
    if not error and work.get("DOI", "").lower() != item["doi"]:
        error = "Crossref response DOI does not match the requested DOI."
    row["title"] = (work.get("title") or [""])[0] if not error else ""
    row["type"] = work.get("type", "") if not error else ""
    row["crossref_api_url"] = row["source_url"]
    row["date_source"] = "Crossref"
    row["evidence_locator"] = "message"
    try:
        evidence = ("", "", "", "UNRESOLVED", error) if error else classify(work, lower, upper)
        if publisher:
            record, locator = publisher
            if (
                row["doi"]
                and record.get("field") == "Date of Publication"
                and record.get("publisher_version_label") == "Early Access"
                and record.get("matching_doi", "").lower() == row["doi"]
                and re.fullmatch(r"https://(?:ieeexplore|xplorestaging)\.ieee\.org/document/\d+/?", record.get("source", ""))
            ):
                publication = date.fromisoformat(record["date_iso"])
                status = date_status((publication, publication), lower, upper)
                online = work.get("published-online", {}).get("date-parts", []) if not error else []
                first, last = interval(online[0]) if len(online) == 1 else (publication, publication)
                if len(online) > 1 or not first <= publication <= last:
                    status = "UNRESOLVED"
                    note = "The IEEE date disagrees with the Crossref online date."
                else:
                    note = "DOI-matched IEEE Xplore Early Access publication date."
                row.update(source_url=record["source"], date_source="IEEE Xplore", evidence_locator=locator)
                evidence = (record["field"], publication.isoformat(), publication.isoformat(), status, note)
    except ValueError as exc:
        evidence = ("", "", "", "UNRESOLVED", str(exc))
    row.update(zip(("date_field", "date_start", "date_end", "e5_result", "note"), evidence))
    if row["date_source"] == "Crossref" and row["date_field"]:
        row["evidence_locator"] = f"message.{row['date_field']}.date-parts"
    return row


def main():
    round_evidence = read_json(ROUND_EVIDENCE)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=date.fromisoformat, default=date(2021, 1, 1))
    parser.add_argument("--cutoff", type=date.fromisoformat, default=date.fromisoformat(round_evidence["cutoff"]))
    parser.add_argument("--output", type=Path, default=HERE / "e5_date_check")
    parser.add_argument("--replay", action="store_true", help="Regenerate CSV from the saved JSON without network access.")
    args = parser.parse_args()
    if args.start > args.cutoff:
        parser.error("--start must be on or before --cutoff")
    args.output.mkdir(parents=True, exist_ok=True)
    archive = args.output / "crossref_receipts.json"
    if args.replay:
        evidence = read_json(archive)
        expected = [(key, packet, reviewers, dois) for key, packet, reviewers, dois in targets()]
        saved = [
            (item["record_id"], item["packet_id"], item["flagged_by"], item["input_dois"])
            for item in evidence
        ]
        if saved != expected:
            parser.error("Saved receipts do not match the current E5 inventory")
    else:
        with ThreadPoolExecutor(max_workers=2) as pool:
            evidence = list(pool.map(fetch, targets()))
        archive.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not evidence:
        parser.error("No E5 records found")
    publishers = publisher_dates(round_evidence)
    rows = [summarize(item, args.start, args.cutoff, publishers.get(item["record_id"])) for item in evidence]
    for row in rows:
        row.update(window_start=args.start.isoformat(), window_cutoff=args.cutoff.isoformat())
    with (args.output / "results.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row["record_id"], row["e5_result"], row["date_field"], row["date_start"], row["date_end"], row["note"])


if __name__ == "__main__":
    main()
