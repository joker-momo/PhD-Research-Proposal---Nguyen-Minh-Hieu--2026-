#!/usr/bin/env python3
"""Map every locked search CSV record to a common schema without deduplication."""

import argparse
import csv
import hashlib
import json
from pathlib import Path

SOURCE_COLUMNS = {
    "IEEE": {
        "title": "Document Title", "authors": "Authors", "year": "Publication Year",
        "venue": "Publication Title", "doi": "DOI", "record_type": "Document Identifier",
        "publication_date": "Online Date", "url": "PDF Link", "abstract": "Abstract",
    },
    "SCOPUS": {
        "title": "Title", "authors": "Author full names", "year": "Year",
        "venue": "Source title", "doi": "DOI", "record_type": "Document Type",
        "language": "Language of Original Document", "source_id": "EID",
        "url": "Link", "abstract": "Abstract",
    },
    "ACM": {
        "title": "title", "authors": "authors", "year": "year", "venue": "venue",
        "doi": "doi", "record_type": "record_type", "publication_date": "display_date",
        "url": "url", "abstract_snippet": "abstract_snippet", "source_page_url": "source_page_url",
    },
    "OPENALEX": {
        "title": "title", "authors": "authors", "year": "publication_year", "venue": "venue",
        "doi": "doi", "record_type": "type", "publication_date": "publication_date",
        "language": "language", "source_id": "openalex_id", "url": "landing_page_url",
    },
}
PROVENANCE_FIELDS = (
    "record_id", "source", "search_variant", "query_version", "source_file",
    "source_record_number", "source_page", "source_rank",
)
DATA_FIELDS = (
    "title", "authors", "year", "venue", "doi", "record_type", "publication_date",
    "language", "source_id", "url", "abstract", "abstract_snippet", "source_page_url",
)
AUDITED_FIELDS = ("title", "authors", "year", "venue", "doi", "record_type", "language", "abstract")


def source_value(value):
    value = value.strip()
    if value.casefold() in {"doi_not_found", "not_found", "n/a", "null", "venue_not_found", "url_not_found"}:
        return ""
    return value


def normalize(project, manifest):
    rows = []
    runs = {(run["source"], run["variant"]): run for run in manifest["selected_runs"]}
    files = manifest["canonical_raw_inputs"]
    for source_file in files:
        source = source_file["source"]
        relative_path = source_file["path"]
        csv_path = project / relative_path
        if hashlib.sha256(csv_path.read_bytes()).hexdigest() != source_file["sha256"]:
            raise ValueError(f"locked input checksum mismatch: {relative_path}")
        source_runs = [
            run for (run_source, _), run in runs.items()
            if run_source == source and run["selected_file"] == relative_path
        ]
        columns = SOURCE_COLUMNS[source]
        with csv_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if set(columns.values()) - set(reader.fieldnames or ()):
                raise ValueError(f"locked input columns changed: {relative_path}")
            file_rows = list(reader)
        if len(file_rows) != source_file["rows"]:
            raise ValueError(f"locked input count mismatch: {relative_path}")
        for ordinal, record in enumerate(file_rows, start=1):
            if source == "ACM":
                run = runs[(source, record["query_variant"])]
                if run["selected_file"] != relative_path:
                    raise ValueError("ACM result position does not resolve to its locked run")
            else:
                run, = source_runs
            values = {field: "" for field in DATA_FIELDS}
            for field, column in columns.items():
                values[field] = source_value(record[column])
            rows.append({
                "record_id": f"{source_file['query_id']}:{ordinal:04d}",
                "source": source,
                "search_variant": run["variant"],
                "query_version": run["query_version"],
                "source_file": relative_path,
                "source_record_number": ordinal,
                "source_page": record.get("page", ""),
                "source_rank": record.get("rank", ""),
                **values,
            })
    if len(rows) != manifest["rows_before_normalization_and_dedup"] or len({row["record_id"] for row in rows}) != len(rows):
        raise ValueError("locked input rows do not reconcile to unique provenance IDs")
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--issues", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.dataset.read_text())
    rows = normalize(args.project, manifest)
    no_value = {
        field: [row["record_id"] for row in rows if not row[field]] for field in AUDITED_FIELDS
    }
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PROVENANCE_FIELDS + DATA_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    issues = {
        "dataset_id": manifest["dataset_id"],
        "rows_accounted_for": len(rows),
        "empty_cell_semantics": "NOT_AVAILABLE_IN_LOCKED_EXPORT; no factual inference",
        "abstract_snippets_are_separate_from_full_abstracts": True,
        "metadata_gaps": {field: {"count": len(ids), "record_ids": ids} for field, ids in no_value.items()},
    }
    args.issues.write_text(json.dumps(issues, indent=2) + "\n", encoding="utf-8")
    print(f"{len(rows)} source rows with unique provenance IDs")


if __name__ == "__main__":
    main()
