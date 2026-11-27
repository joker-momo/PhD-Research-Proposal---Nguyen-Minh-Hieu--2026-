"""Check source locators in HK261 without changing review or extraction decisions."""
import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESTART = HERE.parents[1]
PROJECT = RESTART.parent
SYNTHESIS = RESTART / "synthesis/final_46"


def csv_rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def normalize(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def anchor_on_page(pages, page, excerpt):
    return (isinstance(page, int) and not isinstance(page, bool) and 1 <= page <= len(pages)
            and bool(normalize(excerpt)) and normalize(excerpt) in normalize(pages[page - 1]))


def spans(text, label=""):
    matches = re.findall(label + r"(\d+)(?:\s*[–—-]\s*(\d+))?", text)
    return [(int(a), int(b or a)) for a, b in matches]


def audit_extraction(key, pages):
    rows = []
    source_rows = {row["record_id"]: row for row in key}
    source_key = {report: row["packet_id"] for report, row in source_rows.items()}
    selections = {row["packet_id"] for row in key if row["frozen_disposition"] == "INCLUDE"}

    def add(report, kind, item, locator, state, note):
        source = source_rows[report]
        rows.append(dict(record_id=report, packet_id=source["packet_id"], kind=kind, item=item,
                         source_pdf=source["source_pdf"], source_pdf_sha256=source["sha256"],
                         locator=locator, automated_check=state, note=note))

    def page_limit(report):
        return len(pages[source_key[report]])

    source_map = PROJECT / "manuscript/sn_computer_science/s4_study_row_sources.csv"
    technical = ("t2_topology", "t2_workload", "t2_partition", "t2_decisions_objective_solver",
                 "t3_platform_modality", "t3_network_event_response")
    for row in csv_rows(source_map):
        report = row["report_id"]
        for field in technical:
            physical_only = re.sub(r"\(printed[^)]*\)", "", row[field], flags=re.I)
            references = spans(physical_only, r"(?i)\bp(?:p|age)?\.?\s+")
            present = bool(references) and all(1 <= start <= stop <= page_limit(report)
                                               for start, stop in references)
            add(report, "technical", field, row[field],
                "PAGE_RANGE_VALID" if present else "CHECK_LOCATOR",
                "Locator check only. Read the source field before accepting extraction.")

    visual = {row["item"]: row for row in csv_rows(HERE / "visual_outcome_review.csv")}
    visually_required = set()
    for row in csv_rows(SYNTHESIS / "outcomes.csv"):
        report = row["report_id"]
        page = int(row["pdf_page"])
        locator = f"p. {page}, {row['locator']}"
        status = row["comparison_status"]
        matched = anchor_on_page(pages[source_key[report]], page, row["source_excerpt_or_transcription"])
        status_note = f"Existing ledger status: {status}. Check the original metric, units, comparator and conditions."
        if not (1 <= page <= page_limit(report)):
            check = "CHECK_LOCATOR"
        elif row["verification_method"] == "rendered original PDF":
            visually_required.add(row["outcome_id"])
            record = visual.get(row["outcome_id"])
            check = "RENDERED_SOURCE_MATCH" if record and record["result"] == "MATCH" else "VISUAL_REVIEW_REQUIRED"
            if record:
                status_note += " " + record["scope_note"]
        elif matched:
            check = "TEXT_ANCHOR_MATCH"
        else:
            check = "CHECK_TEXT_OR_RENDERED_PAGE"
        add(report, "outcome", row["outcome_id"], locator, check, status_note)

    if visually_required != visual.keys():
        raise ValueError("Visual-review manifest differs from the nine rendered-source outcome keys")

    for row in csv_rows(SYNTHESIS / "report_coverage.csv"):
        report = row["report_id"]
        locations = spans(row["outcome_pages_checked"])
        check = bool(locations) and all(1 <= start <= stop <= page_limit(report) for start, stop in locations)
        add(report, "coverage", "coverage", row["outcome_pages_checked"],
            "PAGE_RANGE_VALID" if check else "CHECK_LOCATOR",
            f"Existing coverage: {row['exact_outcome_status']}. Review figures and results for completeness.")

    rationales = defaultdict(list)
    for row in csv_rows(SYNTHESIS / "appraisal_rationale.csv"):
        rationales[row["report_id"], row["domain"]].append(row)
    for (report, domain), candidates in rationales.items():
        count = sum(anchor_on_page(pages[source_key[report]], int(row["physical_page"]), row["quote"])
                    for row in candidates if row["physical_page"].isdigit())
        if count == len(candidates):
            check = "TEXT_ANCHOR_MATCH"
        elif count:
            check = "PARTIAL_ANCHOR_MATCH"
        else:
            check = "CHECK_TEXT_OR_RENDERED_PAGE"
        locator = " | ".join(dict.fromkeys(f"p. {row['physical_page']}, {row['section']}" for row in candidates))
        add(report, "appraisal", domain, locator, check,
            f"{count}/{len(candidates)} stored quotes matched selectable text. Appraisal judgment still needs review.")
    if len(rows) != 887 or set(row["packet_id"] for row in rows) != selections:
        raise ValueError("Extraction audit does not cover 887 rows across all 46 included reports")
    return sorted(rows, key=lambda row: (row["record_id"], row["kind"], row["item"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pages", type=Path, help="PDFKit physical-page JSON arrays, one per masked PDF")
    args = parser.parse_args()
    key = csv_rows(SYNTHESIS / "human_review_packet/coordinator/key.csv")
    pages = {row["packet_id"]: json.loads((args.pages / (row["packet_id"] + ".json")).read_text()) for row in key}
    rows = audit_extraction(key, pages)
    write_csv(HERE / "extraction_locator_audit.csv", rows)
    print(json.dumps(Counter(row["automated_check"] for row in rows), sort_keys=True))


if __name__ == "__main__":
    main()
