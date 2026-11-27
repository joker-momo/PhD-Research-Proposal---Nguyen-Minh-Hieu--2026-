#!/usr/bin/env python3
"""Build or verify the checkout-recoverable HK261 report evidence catalog."""

import argparse
from collections import Counter
import csv
from functools import cache
from hashlib import sha256
import io
import json
from pathlib import Path
import subprocess

from build_index import PROJECT, RESTART


FIELDS = (
    "id", "doi", "evidence_type", "status", "source", "version", "repo_path", "sha256",
    "physical_pages", "locator",
)
OUTPUT = PROJECT / "prisma_evidence/evidence_by_id.csv"
SUPPLEMENT = RESTART / "supplemental_screening"


def read_csv(path, key):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    result = {row[key]: row for row in rows}
    if len(result) != len(rows) or "" in result:
        raise ValueError(f"Missing or duplicate identifier in {path}")
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


@cache
def digest(path):
    with path.open("rb") as stream:
        return sha256_file(stream)


def sha256_file(stream):
    value = sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b""):
        value.update(block)
    return value.hexdigest()


def verify_pdf(path, count, parser):
    with parser.open(path) as document:
        if not document.is_pdf or not count or len(document) != count:
            raise ValueError(f"PDF signature or page count mismatch in {path}")
        readable = sum(bool(page.get_text().strip() or page.get_images()) for page in document)
        if not readable:
            raise ValueError(f"No readable text or page image in {path}")


def build_catalog(repo, parser):
    queue_path = RESTART / "unique_record_queue.csv"
    title_screen_path = RESTART / "title_abstract_screening.csv"
    retrieval_path = RESTART / "fulltext_retrieval/retrieval_log.csv"
    identity_path = RESTART / "fulltext_retrieval/fulltext_identity_index.csv"
    screen_path = RESTART / "fulltext_screening/fulltext_screening.csv"
    intake_path = SUPPLEMENT / "supplemental_intake.csv"
    intake_manifest_path = SUPPLEMENT / "manifest.json"
    queue = read_csv(queue_path, "screening_id")
    title_screen = read_csv(title_screen_path, "screening_id")
    retrieval = read_csv(retrieval_path, "screening_id")
    identity = read_csv(identity_path, "screening_id")
    screen = read_csv(screen_path, "screening_id")
    intake = read_csv(intake_path, "id")
    intake_manifest = read_json(intake_manifest_path)
    missing = set(intake_manifest["not_retrieved"])
    if (
        len(intake) != intake_manifest["supplemental_files_by_id"]
        or set(identity) != set(screen)
        or set(identity) & set(intake)
        or (set(identity) | set(intake)) & missing
        or set(retrieval) != (set(identity) | set(intake) | missing)
    ):
        raise ValueError("Sought report IDs do not reconcile to the three intake groups")

    rows = []
    pdf_paths = set()
    pdf_hashes = set()

    def add(record_id, kind, status, path, *, source="", version="", locator="", pdf=None):
        record = queue[record_id]
        doi = record["doi"] or "DOI_NOT_FOUND"
        if pdf:
            doi = pdf.get("verified_doi") or pdf.get("doi") or doi
        if not path.resolve().is_relative_to(PROJECT.resolve()) or not path.is_file():
            raise ValueError(f"Broken or out-of-scope evidence path: {path}")
        sha = digest(path)
        pages = ""
        if pdf:
            pages = int(pdf.get("physical_pages") or pdf["page_count"])
            if sha != pdf["sha256"] or path in pdf_paths or sha in pdf_hashes:
                raise ValueError(f"Duplicate or checksum mismatch: {record_id}")
            verify_pdf(path, pages, parser)
            pdf_paths.add(path)
            pdf_hashes.add(sha)
        rows.append(dict(zip(FIELDS, (
            record_id, doi, kind, status, source, version, path.relative_to(repo).as_posix(),
            sha, pages, locator,
        ), strict=True)))

    for record_id, report in sorted(retrieval.items()):
        queue_row = queue[record_id]
        add(record_id, "REPORT_METADATA", "LOCKED_SEARCH_SET", queue_path,
            source=queue_row["source_file"], locator=f"screening_id={record_id}")
        add(record_id, "TITLE_ABSTRACT_SCREEN", title_screen[record_id]["decision"],
            title_screen_path, locator=f"screening_id={record_id}")
        add(record_id, "BASELINE_RETRIEVAL_RECORD", report["status"], retrieval_path,
            source=report.get("source_url") or report.get("landing_url", ""),
            locator=f"screening_id={record_id}")
        if record_id in identity:
            pdf = identity[record_id]
            add(record_id, "BASELINE_PDF", pdf["status"],
                identity_path.parent / pdf["local_path"], source=pdf["source_url"],
                version=pdf["version"], pdf=pdf,
                locator=pdf["identity_check"])
            decision = screen[record_id]
            add(record_id, "BASELINE_FULLTEXT_SCREEN", decision["decision"], screen_path,
                locator=decision["decision_locators"])
        elif record_id in intake:
            pdf = intake[record_id]
            origin = f'{pdf["source_collection"]}/{pdf["source_file"]}'
            identity_link = report.get("identity_url") or report.get("landing_url", "")
            if identity_link:
                origin += f" | bibliographic identity: {identity_link}"
            locator = f'DOI physical PDF pages {pdf["doi_pages"] or "unverified"}'
            locator += f' | exact title pages {pdf["exact_title_pages"] or "unverified"}'
            add(record_id, "SUPPLEMENTAL_PDF", pdf["status"],
                identity_path.parent / f"pdf/{record_id}.pdf", source=origin,
                version=pdf.get("version") or "PENDING_VERSION_ADJUDICATION",
                locator=locator, pdf=pdf)
        else:
            source = intake_manifest.get("intake_revision", {}).get("not_retrieved_evidence", {})
            add(record_id, "SUPPLEMENTAL_RETRIEVAL_RECORD", "NOT_RETRIEVED", intake_manifest_path,
                source=source.get("url", report.get("landing_url", "")),
                locator=source.get("disposition", "not_retrieved"))

    round_path = RESTART / "retrieval_round_01/round_01_evidence.json"
    round_evidence = read_json(round_path)
    for entry in round_evidence["retrieval"]:
        add(entry["id"], "RETRIEVAL_ROUND_01", entry["status"], round_path,
            source=" | ".join(entry.get("sources", [])), locator=f'retrieval[id={entry["id"]}]')
        if eligibility := entry.get("eligibility"):
            primary = eligibility["primary_reason"]
            add(entry["id"], "ROUND_01_FULLTEXT_SCREEN", eligibility["decision"], round_path,
                source=" | ".join(entry.get("sources", [])),
                locator=f'{primary}: {eligibility["criteria"][primary][1]}')
    awaiting_path = SUPPLEMENT / "prior_awaiting_recheck.json"
    for entry in read_json(awaiting_path)["records"]:
        locators = ", ".join(
            f'{key}: physical PDF p{value["page"]} {value["section"]}'
            for key, value in entry["prior_verified_locators"].items()
        )
        add(entry["id"], "PRIOR_AWAITING_RECHECK", entry["decision_supported_by_round_01"],
            awaiting_path, source=" | ".join(entry["sources"]), locator=locators)

    screened = set()
    for accepted_path in sorted(SUPPLEMENT.glob("batch_*_accepted.json")):
        for entry in read_json(accepted_path):
            record_id = entry["id"]
            if record_id in screened or record_id not in intake:
                raise ValueError(f"Duplicate or invalid new screened report: {record_id}")
            screened.add(record_id)
            locators = " | ".join(
                f"{criterion}: " + (f"physical PDF p{page} " if page else "") + section
                for criterion, source, page, section, _ in entry["evidence"]
                if source == "PDF"
            )
            if not locators:
                raise ValueError(f"Missing approved original-PDF evidence: {record_id}")
            add(record_id, "SUPPLEMENTAL_FULLTEXT_SCREEN", entry["decision"],
                accepted_path, locator=locators)

    extraction = RESTART / "extraction/p08_extraction_table.json"
    appraisal = RESTART / "appraisal/appraisal_table.csv"
    linkage = RESTART / "study_linkage/report_study_map.csv"
    accepted_baseline = {key for key, record in screen.items() if record["decision"] == "INCLUDE"}
    for kind, path, ids in (
        ("BASELINE_STUDY_LINKAGE", linkage, read_csv(linkage, "report_id").keys()),
        ("BASELINE_EXTRACTION", extraction, [row["report_id"] for row in read_json(extraction)["reports"]]),
        ("BASELINE_APPRAISAL", appraisal, read_csv(appraisal, "report_id").keys()),
    ):
        if len(ids) != len(accepted_baseline) or set(ids) != accepted_baseline:
            raise ValueError(f"Baseline included report coverage changed: {path}")
        for record_id in sorted(ids):
            add(record_id, kind, "BASELINE_ACCEPTED", path,
                locator=("reports" if path.suffix == ".json" else "row") + f"[report_id={record_id}]")

    if len(pdf_paths) != len(identity) + len(intake):
        raise ValueError("The canonical PDF count is inconsistent")
    return sorted(rows, key=lambda row: (row["id"], row["evidence_type"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare the saved catalog to the checkout")
    args = parser.parse_args()
    try:
        import pymupdf
    except ImportError:
        parser.error("PyMuPDF is required to verify the original PDFs")
    repo = Path(subprocess.check_output(
        ["git", "-C", str(PROJECT), "rev-parse", "--show-toplevel"], text=True,
    ).strip())
    rows = build_catalog(repo, pymupdf)
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    expected = output.getvalue()
    if args.check:
        if OUTPUT.read_text(encoding="utf-8") != expected:
            parser.error(f"Stale catalog: {OUTPUT}")
        paths = sorted({row["repo_path"] for row in rows})
        tracked = subprocess.check_output(
            ["git", "-C", str(repo), "ls-files", "-z", "--", *paths], text=True,
        ).split("\0")
        if missing := set(paths) - set(tracked):
            parser.error(f"Evidence paths absent from Git: {sorted(missing)}")
    else:
        OUTPUT.write_text(expected, encoding="utf-8")
    print(json.dumps({
        "report_ids": len({row["id"] for row in rows}),
        "entries": len(rows),
        "counts": dict(Counter(row["evidence_type"] for row in rows)),
        "physical_pages": sum(int(row["physical_pages"] or 0) for row in rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
