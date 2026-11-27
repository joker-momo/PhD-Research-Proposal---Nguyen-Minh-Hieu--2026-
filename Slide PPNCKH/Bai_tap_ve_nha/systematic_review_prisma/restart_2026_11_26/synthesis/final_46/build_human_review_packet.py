"""Build blank independent screening and source-verification forms for HK261."""
import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
MANUSCRIPT = PROJECT / "manuscript/sn_computer_science"
PACKET = HERE / "human_review_packet"
SEED = "hk261-full-136-review-v2"


def read(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def rank(purpose, report):
    return hashlib.sha256(f"{SEED}:{purpose}:{report}".encode()).hexdigest()


def require_blank_forms():
    fixed_fields = {"packet_id", "check_type", "check_key", "suggested_physical_page", "suggested_section"}
    for reviewer in ("R1", "R2"):
        for name in ("screening.csv", "source_verification.csv"):
            path = PACKET / reviewer / name
            if path.is_file() and any(
                value for row in read(path) for key, value in row.items() if key not in fixed_fields
            ):
                raise ValueError(f"Preserve the in-progress form: {path}")


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)


def build():
    source = {row["Record_ID"]: row for row in read(MANUSCRIPT / "human_adjudication_log.csv")}
    included = {row["report_id"] for row in read(HERE / "synthesis_input_index.csv")}
    ledger = json.loads((HERE.parents[1] / "prisma/prisma_counts.json").read_text())
    strata = ledger["fulltext_exclusions_by_primary_reason"]
    excluded = [report for reports in strata.values() for report in reports]
    if (len(included), len(excluded), len(set(excluded))) != (46, 90, 90) or (
        included & set(excluded) or included | set(excluded) != source.keys()
    ):
        raise ValueError("Review frame differs from the reconciled 136 assessed reports")
    stratum_by_id = {report: reason for reason, reports in strata.items() for report in reports}
    sorted_ids = sorted(source, key=lambda key: rank("alias", key))
    aliases = {report: f"HKF-{i:03}" for i, report in enumerate(sorted_ids, 1)}

    require_blank_forms()
    coordinator = PACKET / "coordinator"
    coordinator.mkdir(parents=True, exist_ok=True)
    write(coordinator / "exclusion_coverage.csv", ("primary_exclusion_code", "frame", "in_packet"),
          [(reason, len(reports), len(reports)) for reason, reports in sorted(strata.items())])
    write(coordinator / "key.csv", ("packet_id", "record_id", "frozen_disposition",
                                   "primary_exclusion_code", "source_pdf", "sha256"),
          [(aliases[report], report, "INCLUDE" if report in included else "EXCLUDE",
            stratum_by_id.get(report, ""), source[report]["Source_PDF"], source[report]["PDF_SHA256"])
           for report in sorted_ids])

    checks = []
    source_fields = ("t2_topology", "t2_workload", "t2_partition", "t2_decisions_objective_solver",
                     "t3_platform_modality", "t3_network_event_response")
    for row in read(MANUSCRIPT / "s4_study_row_sources.csv"):
        for key in source_fields:
            checks.append((aliases[row["report_id"]], "technical", key, "", row[key]))
    for row in read(HERE / "outcomes.csv"):
        checks.append((aliases[row["report_id"]], "outcome", row["outcome_id"].rsplit("-", 1)[-1],
                       row["pdf_page"], row["locator"]))
    for row in read(HERE / "report_coverage.csv"):
        checks.append((aliases[row["report_id"]], "report_coverage", "coverage", "",
                       "Results and supplements"))
    locators = {}
    for row in read(HERE / "appraisal_rationale.csv"):
        key = (aliases[row["report_id"]], row["domain"])
        locators.setdefault(key, set()).add(f'p. {row["physical_page"]}, {row["section"]}')
    checks.extend((alias, "appraisal", domain, "", " | ".join(sorted(pages)))
                  for (alias, domain), pages in locators.items())
    if len(locators) != 460 or {row[0] for row in checks} != {aliases[key] for key in included} or (
        len({row[:3] for row in checks}) != len(checks)
    ):
        raise ValueError("Missing included audits or duplicate source-verification key")

    for reviewer in ("R1", "R2"):
        folder = PACKET / reviewer
        folder.mkdir(exist_ok=True)
        write(folder / "screening.csv", ("packet_id", "decision", "primary_reason", "physical_pdf_page",
                                        "section", "rationale", "reviewer_id", "date"),
              [(aliases[key], "", "", "", "", "", "", "")
               for key in sorted(sorted_ids, key=lambda key: rank(reviewer, key))])
        write(folder / "source_verification.csv", ("packet_id", "check_type", "check_key",
              "suggested_physical_page", "suggested_section", "verified_value_or_judgment",
              "unit", "workload_conditions_and_denominator", "original_page_and_locator",
              "reason_or_verbatim_anchor", "reviewer_id", "date"),
              [(*row, "", "", "", "", "", "", "") for row in sorted(checks)])
    return source, sorted_ids, aliases, len(checks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--materialize-pdfs", type=Path, metavar="LOCAL_DIRECTORY",
                        help="Copy and hash-check the originals using masked filenames")
    args = parser.parse_args()
    source, selected, aliases, n = build()
    if args.materialize_pdfs:
        args.materialize_pdfs.mkdir(parents=True, exist_ok=True)
        for key in selected:
            path = PROJECT / source[key]["Source_PDF"]
            if hashlib.sha256(path.read_bytes()).hexdigest() != source[key]["PDF_SHA256"]:
                raise ValueError(f"Original PDF hash mismatch: {key}")
            shutil.copyfile(path, args.materialize_pdfs / f"{aliases[key]}.pdf")
    print(f"PASS: {len(selected)} masked screening records per reviewer; {n} blank extraction checks.")


if __name__ == "__main__":
    main()
