#!/usr/bin/env python3
"""Deduplicate locked records while retaining their source-row identities."""

import argparse
import csv
import json
import re
import tempfile
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


def deduplicate(rows, previous=()):
    if not rows:
        raise ValueError("no input records")
    assigned = {}
    representatives = {}
    for row in previous:
        record_id, group_id = row["record_id"], row["screening_id"]
        if not record_id or record_id in assigned or not re.fullmatch(r"R[0-9]{4,}", group_id):
            raise ValueError(f"invalid previous assignment: {record_id}: {group_id}")
        assigned[record_id] = group_id
        if row["link_reason"] == "representative":
            if group_id in representatives:
                raise ValueError(f"duplicate previous representative: {group_id}")
            representatives[group_id] = record_id
    if set(assigned.values()) != representatives.keys():
        raise ValueError("missing previous representative")
    raw_ids = {row["record_id"] for row in rows}
    if len(raw_ids) != len(rows):
        raise ValueError("duplicate provenance ID")
    if missing := assigned.keys() - raw_ids:
        raise ValueError(f"previous records missing from input: {', '.join(sorted(missing))}")
    next_id = max((int(group_id[1:]) for group_id in assigned.values()), default=0) + 1
    used_groups = set()
    if assigned:
        order = {record_id: offset for offset, record_id in enumerate(assigned)}
        rows = sorted(rows, key=lambda row: (order.get(row["record_id"], len(order)), row["record_id"]))

    by_title = defaultdict(list)
    titles_by_doi = defaultdict(set)
    for row in rows:
        key = title_key(row["title"])
        if not key:
            raise ValueError(f"no usable title: {row['record_id']}")
        by_title[key].append(row)
        if row["doi"]:
            titles_by_doi[doi_key(row["doi"])].add(key)
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
            prior_groups = {assigned[row["record_id"]] for row in cluster if row["record_id"] in assigned}
            if len(prior_groups) > 1:
                raise ValueError(f"proposed merge of assigned groups: {', '.join(sorted(prior_groups))}")
            if prior_groups:
                group_id = prior_groups.pop()
                best = next((row for row in cluster if row["record_id"] == representatives[group_id]), None)
                if group_id in used_groups or best is None:
                    raise ValueError(f"proposed split of assigned group: {group_id}")
            else:
                group_id = f"R{next_id:04d}"
                next_id += 1
                best = max(cluster, key=representative_score)
            used_groups.add(group_id)
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
    if assigned:
        def group_order(row):
            return int(row["screening_id"][1:])

        queue.sort(key=group_order)
        mapping.sort(key=lambda row: (group_order(row), order.get(row["record_id"], len(order))))
        year_conflicts.sort(key=group_order)
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
    parser.add_argument("--prior-map", type=Path,
                        help="Existing dedup_map.csv, defaults to the output or input directory map")
    args = parser.parse_args()
    with args.input.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    map_path = args.output_dir / "dedup_map.csv"
    prior_path = args.prior_map or (map_path if map_path.is_file() else args.input.with_name("dedup_map.csv"))
    previous = []
    try:
        if args.prior_map or prior_path.is_file():
            with prior_path.open(encoding="utf-8", newline="") as handle:
                previous = list(csv.DictReader(handle))
            if not previous:
                raise ValueError(f"previous map is empty: {prior_path}")
        elif (args.output_dir / "unique_record_queue.csv").exists():
            raise ValueError("existing queue requires its previous dedup map")
        queue, mapping, unresolved, year_conflicts = deduplicate(rows, previous)
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))
    detail = {
        "input_records": len(rows),
        "removed_duplicate_rows": len(rows) - len(queue),
        "screening_records": len(queue),
        "unresolved_identity_groups": unresolved,
        "metadata_year_conflicts": year_conflicts,
    }
    with tempfile.TemporaryDirectory(dir=args.output_dir, prefix=".dedup-") as temporary:
        draft = Path(temporary)
        write_csv(draft / "unique_record_queue.csv", queue)
        write_csv(draft / "dedup_map.csv", mapping)
        (draft / "dedup_issues.json").write_text(json.dumps(detail, indent=2) + "\n", encoding="utf-8")
        # Preserve the newly assigned IDs first so an interrupted run can be replayed.
        for name in ("dedup_map.csv", "unique_record_queue.csv", "dedup_issues.json"):
            (draft / name).replace(args.output_dir / name)
    print(f"{len(rows)} input rows = {len(queue)} screening records + {len(rows)-len(queue)} duplicates")


if __name__ == "__main__":
    main()
