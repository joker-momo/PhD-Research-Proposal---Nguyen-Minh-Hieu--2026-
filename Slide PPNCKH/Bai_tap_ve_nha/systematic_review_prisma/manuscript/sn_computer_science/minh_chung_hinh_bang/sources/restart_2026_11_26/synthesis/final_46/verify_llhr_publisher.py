"""Cross-check the frozen R0082 locators against a local IEEE proceedings PDF."""
import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOI = "10.1109/WCNC55385.2023.10118908"
IEEE_SHA256 = "7a9a00413539e420d7cf412c2cb71e522311744151dc3a4008c08f2b1415a5ad"


def normalize(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"\s+", " ", text).strip()


def source_pages(path, digest):
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError(f"Unexpected source PDF hash: {path}")
    data = subprocess.check_output(["swift", str(HERE / "pdfkit_pages.swift"), str(path)])
    pages = [normalize(page) for page in json.loads(data)]
    if len(pages) != 6:
        raise ValueError(f"Expected six physical pages: {path}")
    return pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("publisher_pdf", type=Path)
    args = parser.parse_args()
    evidence = json.loads((HERE / "r0082_evidence.json").read_text())
    identity = evidence["identity"]
    preprint = source_pages(HERE.parents[2] / identity["original_pdf"], identity["original_pdf_sha256"])
    ieee = source_pages(args.publisher_pdf, IEEE_SHA256)
    if DOI.lower() not in ieee[0] or "ieee" not in ieee[0]:
        raise ValueError("IEEE publication identity missing from page 1")
    checks = []
    for key, row in evidence["reports"][0]["fields"].items():
        checks.append((key, row["page"], row["locator"], row["quote"]))
    for row in evidence["appraisal"]:
        checks.append((row["domain"], row["physical_page"], row["section"], row["quote"]))
    for page, figs in ((5, (2, 3)), (6, (4, 5))):
        for fig in figs:
            checks.append((f"figure_{fig}", page, "§IV", f"Fig. {fig}."))
    result = []
    for key, page, locator, excerpt in checks:
        if not all(normalize(excerpt) in pages[page - 1] for pages in (preprint, ieee)):
            raise ValueError(f"Anchor mismatch: {key}, physical page {page}")
        result.append({"key": key, "physical_page_in_both_copies": page,
                       "locator": locator, "status": "PASS"})
    receipt = dict(report_id="R0082", doi=DOI, ieee_pdf_sha256=IEEE_SHA256,
                   preprint_pdf_sha256=identity["original_pdf_sha256"], physical_pages=6,
                   source="Author-supplied local IEEE WCNC proceedings PDF",
                   text_parser="Apple PDFKit", checks=result)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
