"""Build or check the S2 full-text decision register from accepted inputs."""

import argparse
import csv
import io
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
RESTART = PROJECT / "restart_2026_11_26"
SCREEN = "restart_2026_11_26/fulltext_screening/fulltext_screening.csv"
SUPPLEMENTAL = "restart_2026_11_26/supplemental_screening/screening_decisions.csv"
QUEUE = "restart_2026_11_26/unique_record_queue.csv"
STUDIES = "restart_2026_11_26/synthesis/final_46/study_characteristics.csv"
RECHECK = "restart_2026_11_26/supplemental_screening/prior_awaiting_recheck.json"
LOG = "manuscript/sn_computer_science/human_adjudication_log.csv"
EXCLUSIONS = "manuscript/sn_computer_science/supplement_fulltext_exclusions.csv"
OUT = HERE / "supplement_s2_eligibility.csv"


def read_csv(path, key):
    with (PROJECT / path).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result = {row[key]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError(f"Duplicate {key} in {path}")
    return result


def build():
    counts = json.loads((RESTART / "prisma/prisma_counts.json").read_text())
    ids = counts["report_ids_by_fulltext_decision"]
    included, excluded = set(ids["INCLUDE"]), set(ids["EXCLUDE"])
    log = read_csv(LOG, "Record_ID")
    studies = read_csv(STUDIES, "report_id")
    titles = read_csv(QUEUE, "screening_id")
    screening = read_csv(SCREEN, "screening_id")
    supplemental = read_csv(SUPPLEMENTAL, "id")
    exclusions = read_csv(EXCLUSIONS, "screening_id")
    rechecks = {row["id"]: row for row in json.loads((PROJECT / RECHECK).read_text())["records"]}
    codes = {rid: code for code, records in counts["fulltext_exclusions_by_primary_reason"].items()
             for rid in records}
    if (len(included), len(excluded), len(log)) != (46, 90, 136) or (
        included & excluded or included | excluded != log.keys()
        or ids["AWAITING_CLASSIFICATION"] or studies.keys() != included or codes.keys() != excluded
    ):
        raise ValueError("S2, S3 and PRISMA report IDs do not reconcile")

    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(("report_id", "title", "final_disposition", "primary_exclusion_code",
                     "decision_basis", "source_locators", "source_record",
                     "original_pdf", "original_pdf_sha256",
                     "documented_item_level_author_decision_date"))
    for rid, row in sorted(log.items()):
        disposition = "INCLUDE" if rid in included else "EXCLUDE"
        code = codes.get(rid, "")
        if row["Final_Human_Decision"]:
            if (row["Final_Human_Decision"], row["Primary_Reason_Code"]) != (disposition, code):
                raise ValueError(f"{rid}: author entry differs from the reconciled decision")
            reason, locator = row["Adjudication_Notes"], row["PDF_Page_Evidence"]
            source = f"{LOG} / Record_ID={rid}"
        elif disposition == "EXCLUDE":
            ex = exclusions[rid]
            if ex["primary_reason_code"] != code:
                raise ValueError(f"{rid}: exclusion code differs from the accepted ledger")
            reason, locator = ex["decision_reason"], ex["decision_locators"]
            source = ex["decision_evidence"]
        else:
            study = studies[rid]
            reason = " ".join(study[field] for field in (
                "uav_architecture_role_and_topology", "partition_and_assignment",
                "evaluation_platform_simulator_hardware_and_traces",
            ))
            source = f'{STUDIES} / report_id={rid}; {study["accepted_extraction_source"]}'
            if rid in screening:
                locator = screening[rid]["decision_locators"]
                source += f"; {SCREEN} / screening_id={rid}"
            else:
                screening_row = supplemental[rid]
                locator = screening_row["principal_locators"]
                source += f'; {screening_row["decision_evidence"]}#id={rid}'
            if rid in rechecks:
                publisher = rechecks[rid]["publisher_evidence"]
                reason += f' E5: {publisher["field"]}, {publisher["display_value"]}.'
                source += f'; {RECHECK} / id={rid}; {publisher["source"]}'
        if not all((reason.strip(), locator.strip(), source, row["PDF_SHA256"],
                    (PROJECT / row["Source_PDF"]).is_file())):
            raise ValueError(f"{rid}: missing decision rationale or evidence")
        writer.writerow((rid, titles[rid]["title"], disposition, code, reason, locator, source,
                         row["Source_PDF"], row["PDF_SHA256"], row["Adjudicated_Date"]))

    if Counter(row["Final_Human_Decision"] for row in log.values()) != {
        "INCLUDE": 7, "EXCLUDE": 3, "": 126
    }:
        raise ValueError("The documented item-level author decision count changed")
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = build()
    if args.check:
        if OUT.read_text(encoding="utf-8") != content:
            raise SystemExit(f"{OUT.name} differs from accepted inputs")
    else:
        OUT.write_text(content, encoding="utf-8")
    print("S2: 136 unique reports, 46 included, 90 excluded, 0 awaiting.")


if __name__ == "__main__":
    main()
