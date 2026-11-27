"""Refresh or verify the portable HK261 figure and table evidence folder."""
import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANUSCRIPT = HERE.parent
PROJECT = MANUSCRIPT.parents[1]
RESTART = Path("restart_2026_11_26")
MANUSCRIPT_PATH = MANUSCRIPT.relative_to(PROJECT)
FILES = [
    *(MANUSCRIPT_PATH / name for name in (
        "build_technical_survey.py", "build_editorial_evidence.py", "main.tex",
        "editorial_mechanism_setting.tex", "editorial_outcome_coverage.tex", "main.pdf", "references.bib",
        "supplement_fulltext_exclusions.csv", "human_adjudication_log.csv", "audit_adjudication.py", "audit_summary.json", "adjudication_audit_table.tex",
        "supplement_s2_eligibility.csv", "supplement_s2_adjudication.md",
        "sn-jnl.cls", "sn-vancouver-num.bst", "technical_coding.psv", "prisma_flow.pdf",
        "technical_appraisal.tex", "technical_appraisal_bars.tex",
        "technical_appraisal_figure.tex", "technical_architecture.tex",
        "technical_architecture_figure.tex", "technical_evaluation.tex",
        "s4_study_row_sources.csv", "supplement_s3.md", "s4_claim_audit.md", "supplement_evidence_index.md",
        "technical_macros.tex", "technical_overview_figure.tex", "technical_taxonomy_figure.tex",
    )),
    *(RESTART / name for name in (
        "prisma/reconcile.py", "fulltext_screening/fulltext_screening.csv",
        "supplemental_screening/screening_decisions.csv", "synthesis/active_synthesis_input_index.csv",
        "prisma/flow_template.tex", "prisma/prisma_counts.json", "prisma/prisma_flow.tex",
        "prisma/active_prisma_checklist.md",
        "synthesis/final_46/study_characteristics.csv",
        "synthesis/final_46/appraisal_summary.csv", "synthesis/final_46/contrast_evidence.csv",
        "synthesis/active_rq_p08_erratum_R0092.json", "synthesis/final_46/synthesis_input_index.csv",
        "extraction/p08_source_inventory.json",
        "synthesis/final_46/outcome_manifest.json", "extraction/rq5_uniform/rule.md",
        "synthesis/final_46/outcomes.csv", "synthesis/final_46/report_coverage.csv",
        "synthesis/final_46/mechanisms.csv", "synthesis/final_46/recomputed_counts.json",
        "synthesis/final_46/claim_source_matrix.csv", "synthesis/final_46/rq5_claim_sources.csv", "synthesis/final_46/r0082_evidence.json",
        "synthesis/final_46/r0082_review.md", "synthesis/final_46/reconcile_inputs.py",
        "synthesis/final_46/author_decision_application.json",
        "integrity/source_review_887/r1_r2_reconciliation/author_decisions.csv",
        "synthesis/final_46/scope_sensitivity.json", "synthesis/final_46/r0082_publisher_crosscheck.json",
        "synthesis/final_46/verify_llhr_publisher.py", "synthesis/final_46/pdfkit_pages.swift",
        "synthesis/final_46/r0082_primary_review.md", "synthesis/final_46/gemini_primary_receipt.json",
        "synthesis/final_46/r0082_correction_review.md", "synthesis/final_46/gemini_correction_receipt.json",
        "synthesis/final_46/r0082_locator_review.md", "synthesis/final_46/gemini_locator_receipt.json",
        "synthesis/final_46/gemini_locator_acceptance.json",
        "synthesis/final_46/appraisal_table.csv", "synthesis/final_46/appraisal_rationale.csv",
    )),
]


def build_index():
    s4 = (MANUSCRIPT / "supplement_evidence_index.md").read_text()
    start = s4.index("## Figures, tables, and equations")
    stop = s4.index("## Manuscript prose crosswalk")
    excerpt = s4[start:stop].rstrip()
    labels = re.findall(r"\| (?:Figure|Table|Eq\.) \d+ `((?:fig|tab|eq):[^`]+)`", excerpt)
    expected = sorted(["fig"] * 5 + ["tab"] * 8 + ["eq"] * 3)
    if len(set(labels)) != len(expected) or sorted(label.split(":")[0] for label in labels) != expected:
        raise ValueError("Expected five figures, eight tables and three equations in S4")

    def relink(match):
        link = match[1]
        if "://" in link:
            return match[0]
        name, delimiter, anchor = link.partition("#")
        source = (MANUSCRIPT / name).resolve().relative_to(PROJECT)
        if source in FILES:
            target = (Path("sources") / source).as_posix()
        else:
            raise ValueError(f"Unpacked source in item index: {source}")
        return f"]({target}{delimiter}{anchor})"

    body = re.sub(r"\]\(([^)]+)\)", relink, excerpt)
    intro = (
        "# Figure, table and equation evidence\n\n"
        "Generated from Supplement S4. PDF pages refer to the archived comparison draft.\n"
        "For commands and input files by item, see [README.md](README.md).\n\n"
    )
    return (intro + body + "\n").encode()


def snapshot():
    items = {Path("sources") / path: (PROJECT / path).read_bytes() for path in FILES}
    state = json.loads((PROJECT / "MUST_READ_AI_AGENT/current_state.json").read_text())
    deferrals = state["evidence"]["alternative_technical_survey"]["editorial_integration"][
        "author_confirmed_deferrals"]
    deferrals_path = Path("sources") / MANUSCRIPT_PATH / "s2_author_confirmed_deferrals.json"
    items[deferrals_path] = (json.dumps(deferrals, indent=2, sort_keys=True) + "\n").encode()
    endorsement = state["evidence"]["s2_final_eligibility_register"]
    endorsement_path = Path("sources") / MANUSCRIPT_PATH / "s2_corpus_author_endorsement.json"
    items[endorsement_path] = (json.dumps(endorsement, indent=2, sort_keys=True) + "\n").encode()
    items[Path("ITEM_INDEX.md")] = build_index()
    manifest = "".join(f"{hashlib.sha256(data).hexdigest()}  {path.as_posix()}\n"
                       for path, data in sorted(items.items()))
    items[Path("SHA256SUMS")] = manifest.encode()
    return items


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Copy current sources into this evidence folder")
    args = parser.parse_args()

    try:
        files = snapshot()
        for relative, data in files.items():
            path = HERE / relative
            if args.refresh:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            elif not path.is_file() or path.read_bytes() != data:
                raise ValueError(f"Snapshot differs from the canonical source: {relative}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Package check failed: {error}\n")
    print(f"PASS: {len(files) - 2} archived files and 16 indexed figures, tables and equations.")


if __name__ == "__main__":
    main()
