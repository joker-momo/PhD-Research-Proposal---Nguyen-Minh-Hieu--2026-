"""Build the editorial evidence tables and seed the human review log."""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

from build_technical_survey import DIMENSIONS

HERE = Path(__file__).resolve().parent
RESTART = HERE.parent.parent / "restart_2026_11_26"
RQ5 = RESTART / "synthesis/final_46"
MECHANISMS = DIMENSIONS["unit"]
SETTINGS = DIMENSIONS["evaluation"]
STATUSES = ("VERIFIED_EXACT", "PLOT_ONLY", "PRINTED_UNRESOLVED")


def read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def keyed(records, key):
    index = {record[key]: record for record in records}
    if len(index) != len(records):
        raise ValueError(f"Duplicate IDs in {key}")
    return index


def outcome_tables(verify_pdfs=False):
    coding = keyed(read(RQ5 / "mechanisms.csv"), "report_id")
    coverage = keyed(read(RQ5 / "report_coverage.csv"), "report_id")
    outcomes = keyed(read(RQ5 / "outcomes.csv"), "outcome_id")
    manifest = keyed(json.loads((RQ5 / "outcome_manifest.json").read_text())["inputs"], "report_id")
    study_rows = keyed(read(RQ5 / "synthesis_input_index.csv"), "report_id")
    if not coding.keys() == coverage.keys() == manifest.keys() == study_rows.keys() or len(coding) != 46:
        raise ValueError("Outcome data must match all 46 included reports")
    retained = Counter()
    states = Counter()
    matched_reports = set()
    for row in outcomes.values():
        report = row["report_id"]
        source = manifest[report]
        if (row["source_pdf"], row["pdf_sha256"], row["study_id"]) != (
            source["path"], source["sha256"], source["study_id"]
        ):
            raise ValueError(f"{report}: outcome provenance differs from the frozen manifest")
        if not 1 <= int(row["pdf_page"]) <= int(coverage[report]["physical_pdf_pages"]) or not row["locator"]:
            raise ValueError(f"{report}: invalid original-page locator")
        status = row["comparison_status"]
        states[status] += 1
        if status in {"matched", "descriptive"}:
            retained[report] += 1
        if status == "matched":
            matched_reports.add(report)
    census = Counter()
    modality = Counter()
    entries = Counter()
    for report, row in coding.items():
        source = manifest[report]
        accepted = study_rows[report]
        assessment = coverage[report]
        if (source["path"], source["sha256"], source["study_id"]) != (
            accepted["original_pdf"], accepted["original_pdf_sha256"], accepted["study_id"]
        ) or (assessment["source_pdf"], assessment["pdf_sha256"], assessment["study_id"]) != (
            source["path"], source["sha256"], source["study_id"]
        ):
            raise ValueError(f"{report}: report coverage has a different source identity")
        if verify_pdfs:
            with (RESTART.parent / source["path"]).open("rb") as stream:
                if hashlib.file_digest(stream, "sha256").hexdigest() != source["sha256"]:
                    raise ValueError(f"{report}: original PDF hash mismatch")
        mechanism = row["mechanism"]
        setting = row["evaluation_setting"]
        status = assessment["exact_outcome_status"]
        if mechanism not in MECHANISMS or setting not in SETTINGS or status not in STATUSES:
            raise ValueError(f"{report}: unknown inventory code")
        if retained[report] != int(assessment["retained_numeric_rows"]) or bool(retained[report]) != (
            status == "VERIFIED_EXACT"
        ):
            raise ValueError(f"{report}: retained outcomes disagree with report coverage")
        census[mechanism, status] += 1
        modality[mechanism, setting] += 1
        entries[mechanism] += retained[report]
    summary = json.loads((RQ5 / "recomputed_counts.json").read_text())
    if (len(outcomes), dict(states), len(matched_reports), sum(map(bool, retained.values()))) != (
        summary["outcome_ledger_rows"], summary["outcome_rows"], summary["matched_reports"],
        summary["coverage"]["VERIFIED_EXACT"]
    ):
        raise ValueError("Retained outcome census differs from the verified source release")
    settings_rows = [
        (name, *counts, sum(counts))
        for key, name in MECHANISMS.items()
        for counts in [tuple(modality[key, setting] for setting in SETTINGS)]
    ]
    coverage_rows = [
        (name, sum(counts), *counts, entries[key])
        for key, name in MECHANISMS.items()
        for counts in [tuple(census[key, status] for status in STATUSES)]
    ]
    return {
        "editorial_mechanism_setting.tex": table(
            "settings", "Primary inference mechanism by primary evaluation modality.",
            r"Partition or dispatch unit & Analyt. & Sim. & Trace & Bench & Outdoor & Total",
            settings_rows,
            "Sim. denotes software evaluation. Trace denotes trace- or profile-backed evaluation. "
            "Bench includes component measurement, host emulation, and hardware-in-the-loop. "
            "Outdoor requires a multi-UAV inference evaluation.",
        ),
        "editorial_outcome_coverage.tex": table(
            "coverage", "Coverage of retained numerical outcomes by primary inference mechanism.",
            r"Partition or dispatch unit & Studies & Verified & Plot only & Unresolved & Entries",
            coverage_rows,
            "The first four numeric columns count studies. Entries counts matched or descriptive "
            "results. The extraction rule retains explicit results with interpretable conditions.",
        ),
    }


def table(label, caption, heading, records, note):
    totals = tuple(sum(column) for column in zip(*(row[1:] for row in records)))
    body = "\n".join(" & ".join(map(str, row)) + r" \\" for row in [*records, ("Total", *totals)])
    return "\n".join((
        r"\begin{table}[tbp]",
        rf"\caption{{{caption}}}\label{{tab:{label}}}",
        r"\centering\small\setlength{\tabcolsep}{4pt}",
        r"\begin{tabular}{@{}p{.31\linewidth}" + "r" * len(totals) + "@{}}",
        r"\toprule", heading + r" \\", r"\midrule", body,
        r"\bottomrule", r"\end{tabular}",
        rf"\par\smallskip\raggedright {note}",
        r"\end{table}", "",
    ))


def review_log():
    initial_path = RESTART / "fulltext_screening/fulltext_screening.csv"
    supplemental_path = RESTART / "supplemental_screening/screening_decisions.csv"
    initial = [(r["screening_id"], r["decision"], r["primary_reason_code"], r["pdf_path"],
                r["sha256"], r["decision_locators"]) for r in read(initial_path)]
    supplemental = [(r["id"], r["decision"], r["primary_reason"], r["pdf"],
                     r["sha256"], r["principal_locators"]) for r in read(supplemental_path)]
    included = keyed(read(RESTART / "synthesis/active_synthesis_input_index.csv"), "report_id")
    excluded = keyed(read(HERE / "supplement_fulltext_exclusions.csv"), "screening_id")
    if included.keys() & excluded.keys():
        raise ValueError("A report appears in both final baseline decision lists")
    baseline = []
    for report, _, reason, path, digest, locator in sorted(initial + supplemental):
        if report in included:
            decision = "INCLUDE"
            locator = "See accepted extraction: " + included[report]["extraction_source"]
            reason = ""
        elif report in excluded:
            decision = "EXCLUDE"
            reason = excluded[report]["primary_reason_code"]
            locator = excluded[report]["decision_locators"]
        else:
            decision = "AWAITING_CLASSIFICATION"
        baseline.append((report, decision, reason, path, digest, locator))
    if (len({r[0] for r in baseline}), len(baseline), Counter(r[1] for r in baseline)) != (
        136, 136, {"INCLUDE": 46, "EXCLUDE": 87, "AWAITING_CLASSIFICATION": 3}
    ):
        raise ValueError("Expected 136 baseline decisions with 46 included, 87 excluded and 3 pending")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(("Record_ID", "AI_Decision", "AI_Primary_Reason_Code", "Source_PDF", "PDF_SHA256",
                     "AI_PDF_Locator", "Reviewer1_Decision", "Reviewer2_Decision", "Final_Human_Decision",
                     "Changed_From_AI", "Primary_Reason_Code", "PDF_Page_Evidence", "Adjudication_Notes",
                     "Reviewer1_ID", "Reviewer1_Date", "Reviewer1_Notes", "Reviewer2_ID",
                     "Reviewer2_Date", "Reviewer2_Notes", "Adjudicated_Date"))
    writer.writerows((*r, *[""] * 14) for r in baseline)
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("tables", "check", "seed-review-log"))
    parser.add_argument("--verify-pdfs", action="store_true")
    args = parser.parse_args()
    if args.action == "seed-review-log":
        content = review_log()
        with (HERE / "human_adjudication_log.csv").open("x", encoding="utf-8") as stream:
            stream.write(content)
        return
    for filename, content in outcome_tables(args.verify_pdfs).items():
        path = HERE / filename
        if args.action == "tables":
            path.write_text(content, encoding="utf-8")
        elif path.read_text(encoding="utf-8") != content:
            raise ValueError(f"Generated table differs from {path.name}")


if __name__ == "__main__":
    main()
