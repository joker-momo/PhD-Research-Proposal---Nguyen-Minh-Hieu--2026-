"""Refresh or verify the portable HK261 figure and table evidence folder."""
import argparse
import hashlib
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
        "human_adjudication_log.csv", "audit_adjudication.py", "audit_summary.json", "adjudication_audit_table.tex",
        "sn-jnl.cls", "sn-vancouver-num.bst", "technical_coding.psv", "prisma_flow.pdf",
        "technical_appraisal.tex", "technical_appraisal_bars.tex",
        "technical_appraisal_figure.tex", "technical_architecture.tex",
        "technical_architecture_figure.tex", "technical_evaluation.tex",
        "technical_macros.tex", "technical_overview_figure.tex", "technical_taxonomy_figure.tex",
    )),
    *(RESTART / name for name in (
        "prisma/flow_template.tex", "prisma/prisma_counts.json", "prisma/prisma_flow.tex",
        "synthesis/active_study_characteristics.csv",
        "synthesis/active_appraisal_summary.csv", "synthesis/active_outcome_evidence.csv",
        "synthesis/active_rq_p08_erratum_R0092.json", "synthesis/active_synthesis_input_index.csv",
        "extraction/p08_source_inventory.json",
        "extraction/rq5_uniform/manifest.json", "extraction/rq5_uniform/rule.md",
        "extraction/rq5_uniform/outcomes.csv", "extraction/rq5_uniform/report_coverage.csv",
        "synthesis/desk_reject_evidence_map.csv",
        "appraisal/active_appraisal_table.csv", "appraisal/active_appraisal_rationale_matrix.csv",
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
        if source == RESTART / "prisma/reconcile.py":
            target = "../" + name
        elif source in FILES:
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
    print(f"PASS: {len(FILES)} archived files and 16 indexed figures, tables and equations.")


if __name__ == "__main__":
    main()
