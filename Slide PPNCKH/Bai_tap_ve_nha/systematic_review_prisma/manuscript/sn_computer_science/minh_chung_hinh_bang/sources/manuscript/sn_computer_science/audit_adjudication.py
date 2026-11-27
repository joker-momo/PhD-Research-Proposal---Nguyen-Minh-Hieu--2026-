"""Report documented S2 adjudication and verified PRISMA counts."""

import argparse
import csv
import io
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from build_editorial_evidence import review_log

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
PRISMA = PROJECT / "restart_2026_11_26/prisma"
DECISIONS = ("INCLUDE", "EXCLUDE", "AWAITING_CLASSIFICATION")
REASONS = {f"E{number}" for number in range(1, 8)}


def load_rows(source, baseline, assessed_ids):
    reader = csv.DictReader(io.StringIO(source, newline=""), strict=True)
    expected = csv.DictReader(io.StringIO(baseline, newline=""), strict=True)
    if reader.fieldnames != expected.fieldnames:
        raise ValueError("S2 header does not match the adjudication schema")
    original = {row["Record_ID"]: row for row in expected}
    baseline_fields = reader.fieldnames[:6]
    rows = {}
    for row in reader:
        if None in row or None in row.values():
            raise ValueError(f"S2 line {reader.line_num}: incorrect number of columns")
        row = {key: value.strip() for key, value in row.items()}
        report_id = row["Record_ID"]
        if report_id in rows or report_id not in assessed_ids:
            raise ValueError(f"S2 line {reader.line_num}: duplicate or unexpected ID {report_id!r}")
        if any(row[key] != original[report_id][key] for key in baseline_fields):
            raise ValueError(f"{report_id}: S2 baseline decision or PDF evidence changed")

        for reviewer in ("Reviewer1", "Reviewer2"):
            decision = row[f"{reviewer}_Decision"]
            if decision and (decision not in DECISIONS or not row[f"{reviewer}_ID"]
                             or not row[f"{reviewer}_Date"] or not row["PDF_Page_Evidence"]):
                raise ValueError(f"{report_id}: invalid {reviewer} decision or missing provenance")
        if (row["Reviewer1_Decision"] and row["Reviewer2_Decision"]
                and row["Reviewer1_ID"].casefold() == row["Reviewer2_ID"].casefold()):
            raise ValueError(f"{report_id}: paired decisions must have distinct reviewer IDs")

        final = row["Final_Human_Decision"]
        reason = row["Primary_Reason_Code"]
        if (final == "EXCLUDE" and reason not in REASONS) or (final != "EXCLUDE" and reason):
            raise ValueError(f"{report_id}: invalid primary exclusion reason")
        expected_flag = ""
        if final:
            if final not in DECISIONS[:2] or not row["PDF_Page_Evidence"] or not row["Adjudicated_Date"]:
                raise ValueError(f"{report_id}: invalid final decision or missing provenance")
            expected_flag = "YES" if row["AI_Decision"] != final else "NO"
        if row["Changed_From_AI"].upper() != expected_flag:
            raise ValueError(f"{report_id}: Changed_From_AI does not match the documented decisions")
        rows[report_id] = row

    if set(rows) != set(assessed_ids):
        raise ValueError("S2 does not cover the assessed PRISMA report IDs")
    return rows


def paired_agreement(pairs):
    n = len(pairs)
    matrix = {left: dict.fromkeys(DECISIONS, 0) for left in DECISIONS}
    for left, right in pairs:
        matrix[left][right] += 1
    result = {"paired_reports": n, "matched": None, "percent_agreement": None,
              "expected_agreement": None, "cohens_kappa": None, "confidence_interval_95": None,
              "matrix": matrix}
    if not n:
        return result | {"status": "NO_PAIRED_DECISIONS"}
    matched = sum(matrix[label][label] for label in DECISIONS)
    expected = sum(sum(matrix[label].values()) * sum(row[label] for row in matrix.values())
                   for label in DECISIONS)
    result.update(matched=matched, percent_agreement=100 * matched / n,
                  expected_agreement=expected / n**2)
    if expected == n**2:
        return result | {"status": "KAPPA_UNDEFINED"}
    return result | {"status": "DESCRIPTIVE_PAIRED_SUBSET",
                     "cohens_kappa": (n * matched - expected) / (n**2 - expected)}


def build_report(rows, ledger, deferrals, endorsement):
    counts = ledger["counts"]
    if endorsement["working_counts"] != {
        "include": counts["included_reports"],
        "exclude": counts["reports_excluded"],
        "awaiting": counts["reports_awaiting_classification"],
    }:
        raise ValueError("The S2 author endorsement does not match the PRISMA dispositions")
    pending = ledger["awaiting_classification_codes"]
    for report_id, reason in deferrals.items():
        row = rows.get(report_id)
        if (not row or pending.get(report_id) != reason or row["Final_Human_Decision"]
                or not row["PDF_Page_Evidence"] or not row["Adjudication_Notes"]):
            raise ValueError(f"{report_id}: author-confirmed deferral lacks matching S2 or PRISMA evidence")

    pairs = [(row["Reviewer1_Decision"], row["Reviewer2_Decision"])
             for row in rows.values() if row["Reviewer1_Decision"] and row["Reviewer2_Decision"]]
    final = {report_id: row for report_id, row in rows.items() if row["Final_Human_Decision"]}
    transitions = defaultdict(list)
    for report_id, row in sorted(final.items()):
        if row["Changed_From_AI"].upper() == "YES":
            transition = f'{row["AI_Decision"]} -> {row["Final_Human_Decision"]}'
            transitions[transition].append(report_id)
    processed_reports = len(final) + len(deferrals)
    changed_reports = sum(map(len, transitions.values()))
    return {
        "s2": {
            "reports_in_log": len(rows),
            "author_processed_reports": processed_reports,
            "reports_without_separate_final_author_entry": len(rows) - len(final),
            "corpus_author_endorsement": {
                "date": endorsement["author_endorsement_date"],
                "register": endorsement["path"],
                "included_reports": counts["included_reports"],
                "excluded_reports": counts["reports_excluded"],
            },
            "final_human_decisions": {
                key: {"decision": row["Final_Human_Decision"], "reason": row["Primary_Reason_Code"]}
                for key, row in sorted(final.items())
            },
            "author_confirmed_deferrals": deferrals,
            "reviewer1_decisions": sum(bool(row["Reviewer1_Decision"]) for row in rows.values()),
            "reviewer2_decisions": sum(bool(row["Reviewer2_Decision"]) for row in rows.values()),
        },
        "paired_human_agreement": paired_agreement(pairs),
        "ai_to_final_human_decisions": {
            "compared_reports": len(final),
            "changed_reports": changed_reports,
            "changed_among_author_processed": {"changed": changed_reports, "total": processed_reports},
            "transitions": dict(transitions),
            "scope": "Compared reports have documented final decisions. Author-processed reports include final "
                     "decisions and confirmed deferrals. Both counts describe the documented subset.",
        },
        "prisma": {"counts": ledger["counts"], "awaiting_classification_codes": pending,
                   "arithmetic_differences": ledger["arithmetic_differences"]},
    }


def render_latex(report):
    s2 = report["s2"]
    paired = report["paired_human_agreement"]
    comparison = report["ai_to_final_human_decisions"]
    processed = comparison["changed_among_author_processed"]
    prisma = report["prisma"]["counts"]
    endorsement = s2["corpus_author_endorsement"]
    agreement = paired["percent_agreement"]
    pending = ", ".join(f"{key} ({reason})"
                        for key, reason in report["prisma"]["awaiting_classification_codes"].items())
    final = ", ".join(f"{key} ({row['reason']})" for key, row in s2["final_human_decisions"].items()
                      if row["decision"] == "EXCLUDE")
    included = endorsement["included_reports"]
    excluded = endorsement["excluded_reports"]
    final_count = len(s2["final_human_decisions"])
    exclusion_count = sum(row["decision"] == "EXCLUDE" for row in s2["final_human_decisions"].values())
    deferral_count = len(s2["author_confirmed_deferrals"])
    final_change = (f"{comparison['changed_reports']} / {comparison['compared_reports']}"
                    if comparison["compared_reports"] else "N/A")
    agreement_label = "N/A" if agreement is None else rf"{agreement:.1f}\%"
    rows = [
        ("Full-text reports in the S2 register", s2["reports_in_log"]),
        ("Final PRISMA disposition (included / excluded / awaiting)",
         f"{prisma['included_reports']} / {prisma['reports_excluded']} / {prisma['reports_awaiting_classification']}"),
        ("Decisions endorsed by the lead reviewer (include / exclude)",
         f"{included + excluded} ({included} / {excluded})"),
        ("Separate adjudication entries (include / exclude / defer)",
         f"{final_count + deferral_count} ({final_count - exclusion_count} / {exclusion_count} / {deferral_count})"),
        ("Exclusions with separate entries", final or "None"),
        ("Reports without a separate final entry", s2["reports_without_separate_final_author_entry"]),
        ("Status changes from preliminary dispositions (separate final entries)", final_change),
        ("Independent human decisions recorded (R1 / R2)", f"{s2['reviewer1_decisions']} / {s2['reviewer2_decisions']}"),
        ("Paired independent human decisions", paired["paired_reports"]),
        ("Observed agreement on independent pairs", agreement_label),
        ("PRISMA awaiting classification", pending or "None"),
    ]
    if deferral_count:
        rows.insert(7, ("Status changes among separate entries including deferrals",
                        f"{processed['changed']} / {processed['total']}" if processed["total"] else "N/A"))
    return "\n".join([
        r"\begin{table}[htbp]", r"\centering",
        r"\caption{Documented S2 adjudication and current PRISMA dispositions.}",
        r"\label{tab:adjudication_audit}", r"\begin{tabular}{@{}p{0.61\linewidth}p{0.33\linewidth}@{}}", r"\hline",
        r"\textbf{Measure} & \textbf{Value} \\", r"\hline",
        *(f"{label} & {value} " + r"\\" for label, value in rows),
        r"\hline", r"\end{tabular}", r"\end{table}", "",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify both saved outputs without writing")
    parser.add_argument("--frozen-prisma", action="store_true",
                        help="Use the checksummed PRISMA ledger in the portable evidence package")
    args = parser.parse_args()
    try:
        if not args.frozen_prisma:
            subprocess.run([sys.executable, "-B", str(PRISMA / "reconcile.py"), "--check"],
                           check=True, stdout=subprocess.DEVNULL)
        ledger = json.loads((PRISMA / "prisma_counts.json").read_text())
        if args.frozen_prisma:
            deferrals = json.loads((HERE / "s2_author_confirmed_deferrals.json").read_text())
            endorsement = json.loads((HERE / "s2_corpus_author_endorsement.json").read_text())
        else:
            state = json.loads((PROJECT / "MUST_READ_AI_AGENT/current_state.json").read_text())
            deferrals = state["evidence"]["alternative_technical_survey"]["editorial_integration"][
                "author_confirmed_deferrals"]
            endorsement = state["evidence"]["s2_final_eligibility_register"]
        assessed_ids = ledger["report_ids_by_retrieval_decision"]["RETRIEVED_PDF"]
        source = (HERE / "human_adjudication_log.csv").read_text(encoding="utf-8-sig")
        report = build_report(load_rows(source, review_log(), set(assessed_ids)), ledger, deferrals, endorsement)
        outputs = {
            "audit_summary.json": json.dumps(report, indent=2, sort_keys=True) + "\n",
            "adjudication_audit_table.tex": render_latex(report),
        }
        for filename, content in outputs.items():
            path = HERE / filename
            if args.check:
                if path.read_text() != content:
                    raise ValueError(f"{filename}: saved audit output differs")
            else:
                path.write_text(content)
    except (OSError, ValueError, KeyError, csv.Error, subprocess.CalledProcessError) as error:
        parser.exit(1, f"S2 audit failed: {error}\n")
    print("PASS: documented S2 adjudication and PRISMA counts verified.")


if __name__ == "__main__":
    main()
