"""Check a bounded Springer draft against explicit counts; not a submission gate."""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript/sn_computer_science"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--expected-pages", type=int, default=14)
parser.add_argument("--expected-studies", type=int, default=18)
parser.add_argument("--expected-citations", type=int, default=27)
parser.add_argument("--dataset", default="interim_20report")
args = parser.parse_args()
if min(args.expected_pages, args.expected_studies, args.expected_citations) < 1:
    parser.error("Expected counts must be positive")
dataset = ROOT / args.dataset
tex = (SOURCE / "main.tex").read_text()
bib = (SOURCE / "references.bib").read_text()
log = (SOURCE / "main.log").read_text()
blg = (SOURCE / "main.blg").read_text()
reader = PdfReader(SOURCE / "main.pdf")
rows = list(csv.DictReader((dataset / "data_extraction_eligible.csv").open()))
expected = {row["study_id"] for row in rows}
table = tex.split("\\begin{longtable}", 1)[1].split("\\end{longtable}", 1)[0]
table_ids = re.findall(r"^([SC]\d{2})~", table, re.MULTILINE)
cited = {key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", tex)
         for key in group.split(",")}
entries = dict(re.findall(r"@\w+\{([^,]+),(.*?)(?=\n@|\Z)", bib, re.S))
abstract = tex.split("\\abstract{", 1)[1].split("\\keywords", 1)[0]
abstract = re.sub(r"\\textbf\{[^}]*\}", "", abstract)
word_count = len(re.findall(r"\b\w+(?:[-–]\w+)*\b", abstract))
page_texts = [page.extract_text() for page in reader.pages]
checks = {
    "expected_dataset_records": len(rows) == args.expected_studies and len(expected) == args.expected_studies,
    "expected_unique_matching_table_rows": len(table_ids) == args.expected_studies and set(table_ids) == expected,
    "expected_resolved_unique_citations": len(cited) == args.expected_citations and cited == entries.keys(),
    "all_cited_entries_have_doi": all(re.search(r"\bdoi\s*=\s*\{10\.", entries[k]) for k in cited),
    "no_bibliography_warnings": "Warning--" not in blg,
    "no_undefined_or_overfull": not re.search(r"undefined|Overfull|Emergency stop|Fatal error", log, re.I),
    "structured_abstract_150_to_250": 150 <= word_count <= 250 and all(
        label in tex for label in ("Purpose:", "Methods:", "Results:", "Conclusion:")),
    "six_keywords": len(tex.split("\\keywords{", 1)[1].split("}", 1)[0].split(",")) == 6,
    "interim_and_not_submitted_disclosed": "Not submitted" in tex and "interim" in tex.lower(),
    "expected_nonempty_pages": len(page_texts) == args.expected_pages and all(len(t.strip()) > 80 for t in page_texts),
    "pdf_newer_than_all_build_inputs": all(
        (SOURCE / "main.pdf").stat().st_mtime_ns >= (SOURCE / name).stat().st_mtime_ns
        for name in ("main.tex", "references.bib", "sn-jnl.cls", "sn-vancouver-num.bst")),
    "single_main_source": "\\input{" not in tex and "\\include{" not in tex,
}
files = [SOURCE / name for name in ("main.tex", "main.pdf", "references.bib", "sn-jnl.cls", "sn-vancouver-num.bst")]
result = {
    "scope": "Interim build/structure checks only; no final completeness claim",
    "checks": {name: "PASS" if passed else "FAIL" for name, passed in checks.items()},
    "observations": {"included_studies": len(rows), "table_rows": len(table_ids),
                     "unique_citations": len(cited), "abstract_words_excluding_labels": word_count,
                     "pages": len(page_texts), "underfull_vbox_warnings": log.count("Underfull \\vbox")},
    "sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
    "not_proven_by_this_check": ["source-level research validity", "46-record alignment acceptance",
        "30–35-study expanded corpus", "final database PRISMA reconciliation",
        "author metadata and approval", "journal submission", "visual page inspection"],
}
target = dataset / "sncs_build_audit.json"
target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(result, indent=2, ensure_ascii=False))
raise SystemExit(0 if all(checks.values()) else 1)
