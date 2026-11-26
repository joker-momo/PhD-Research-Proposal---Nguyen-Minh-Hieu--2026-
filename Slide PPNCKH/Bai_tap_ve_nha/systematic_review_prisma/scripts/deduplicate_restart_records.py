#!/usr/bin/env python3
"""Deduplicate locked records while retaining their source-row identities."""

import argparse
import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


def title_key(title):
    return " ".join(re.findall(r"[^\W_]+", unicodedata.normalize("NFKC", title).casefold()))


def doi_key(doi):
    value = unquote(doi).strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)


def proceedings_match(row, candidate):
    return (
        row["source"] == candidate["source"] == "ACM"
        and row["record_type"] == candidate["record_type"] == "PROCEEDING"
        and row["year"] == candidate["year"]
        and bool(row["year"])
    )


def representative_score(row):
    return tuple(bool(row[field]) for field in (
        "abstract", "doi", "authors", "venue", "abstract_snippet", "url",
    ))


def deduplicate(rows):
    by_title = defaultdict(list)
    titles_by_doi = defaultdict(set)
    for row in rows:
        key = title_key(row["title"])
        if not key:
            raise ValueError(f"no usable title: {row['record_id']}")
        by_title[key].append(row)
        if row["doi"]:
            titles_by_doi[doi_key(row["doi"])].add(key)
    if len({row["record_id"] for row in rows}) != len(rows):
        raise ValueError("duplicate provenance ID")
    conflicted_dois = {doi for doi, titles in titles_by_doi.items() if len(titles) > 1}
    queue, mapping, unresolved, year_conflicts = [], [], [], []
    for normalized_title, title_group in by_title.items():
        known = {doi_key(row["doi"]) for row in title_group if row["doi"]}
        if known & conflicted_dois or len(known) > 1:
            unresolved.append({
                "reason": "conflicting_doi_or_title",
                "record_ids": [row["record_id"] for row in title_group],
                "doi_keys": sorted(known),
            })
            clusters = [[row] for row in title_group]
        else:
            doi_rows = [row for row in title_group if row["doi"]]
            no_doi_rows = [row for row in title_group if not row["doi"]]
            if doi_rows:
                linked = [row for row in no_doi_rows if any(proceedings_match(row, other) for other in doi_rows)]
                remaining = [row for row in no_doi_rows if row not in linked]
                clusters = [doi_rows + linked] + [[row] for row in remaining]
            else:
                clusters = [[row] for row in title_group]
            if len(clusters) > 1:
                unresolved.append({
                    "reason": "title_only_insufficient",
                    "record_ids": [row["record_id"] for row in title_group],
                    "doi_keys": sorted(known),
                })
        for cluster in clusters:
            best = max(cluster, key=representative_score)
            group_id = f"R{len(queue)+1:04d}"
            queue.append({"screening_id": group_id, "member_count": len(cluster), **best})
            years = sorted({row["year"] for row in cluster if row["year"]})
            if len(years) > 1:
                year_conflicts.append({
                    "screening_id": group_id, "years": years,
                    "record_ids": [row["record_id"] for row in cluster],
                })
            for row in cluster:
                reason = "representative"
                if row is not best:
                    reason = "matching_doi_and_title" if row["doi"] else "exact_title_year_acm_proceeding"
                mapping.append({
                    "screening_id": group_id,
                    "record_id": row["record_id"],
                    "link_reason": reason,
                    "doi_key": doi_key(row["doi"]),
                    "title_key": normalized_title,
                })
    return queue, mapping, unresolved, year_conflicts


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    with args.input.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    queue, mapping, unresolved, year_conflicts = deduplicate(rows)
    write_csv(args.output_dir / "unique_record_queue.csv", queue)
    write_csv(args.output_dir / "dedup_map.csv", mapping)
    detail = {
        "input_records": len(rows),
        "removed_duplicate_rows": len(rows) - len(queue),
        "screening_records": len(queue),
        "unresolved_identity_groups": unresolved,
        "metadata_year_conflicts": year_conflicts,
    }
    (args.output_dir / "dedup_issues.json").write_text(json.dumps(detail, indent=2) + "\n")
    print(f"{len(rows)} input rows = {len(queue)} screening records + {len(rows)-len(queue)} duplicates")


if __name__ == "__main__":
    main()
