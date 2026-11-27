"""Check the HK261 manuscript evidence crosswalk and saved file identities."""
import argparse
import csv
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
RESTART = PROJECT / "restart_2026_11_26"
INDEX = HERE / "supplement_evidence_index.md"
SNAPSHOT = HERE / "evidence_sha256.txt"


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_index():
    index = INDEX.read_text()
    manuscript = (HERE / "main.tex").read_text()
    start = 1
    for left, right in re.findall(r"^\| (\d+)–(\d+) \|", index, re.M):
        require(int(left) == start and int(right) >= start, f"Invalid crosswalk at LaTeX line {start}")
        start = int(right) + 1
    require(start == len(manuscript.splitlines()) + 1, "Crosswalk does not cover the full LaTeX source")

    paths = {INDEX, Path(__file__).resolve(), HERE / "main.pdf",
             HERE / "sn-jnl.cls", HERE / "sn-vancouver-num.bst"}
    for link in re.findall(r"\]\(([^)]+)\)", index):
        if "://" in link:
            continue
        path = (HERE / link.split("#", 1)[0]).resolve()
        require(path.is_relative_to(PROJECT) and path.is_file(), f"Missing local evidence: {link}")
        paths.add(path)

    tex = "\n".join(path.read_text() for path in sorted(paths) if path.suffix == ".tex")
    labels = set(re.findall(r"\\label\{((?:fig|tab|eq):[^}]+)\}", tex))
    indexed = set(re.findall(r"`((?:fig|tab|eq):[^ `]+)`", index))
    require(labels == indexed and len(labels) == 13, f"Figure/table/equation coverage mismatch: {labels ^ indexed}")
    require((HERE / "prisma_flow.pdf").read_bytes() ==
            (RESTART / "prisma/prisma_flow.pdf").read_bytes(), "Embedded PRISMA PDF differs from accepted PDF")
    paths.add(RESTART / "prisma/prisma_flow.pdf")
    return paths, len(labels)


def check_outcome_rows():
    manuscript = (HERE / "main.tex").read_text()
    table = manuscript.split(r"\label{tab:outcomes}", 1)[1].split(r"\end{longtable}", 1)[0]
    report_ids = re.findall(r"^\\cite\{(R\d{4})\} &", table, re.M)
    ledger = rows(RESTART / "synthesis/active_outcome_evidence.csv")
    keys = {(row["report_id"], row["key"]) for row in ledger}
    map_text = INDEX.read_text().split("## Table 4 row map", 1)[1].split("## Manuscript prose crosswalk", 1)[0]
    mapped = re.findall(r"^\| (R\d{4}) [^|]+\|([^|]+)\|", map_text, re.M)
    require(report_ids == [report for report, _ in mapped] and len(mapped) == 9, "Table 4 row index differs")
    for report, cell in mapped:
        evidence = re.findall(r"`(quantity:\d+)`", cell)
        require(evidence and all((report, key) in keys for key in evidence),
                f"{report}: Table 4 evidence key missing from accepted ledger")
    return len(mapped)


def check_originals():
    included = rows(RESTART / "synthesis/active_synthesis_input_index.csv")
    ids = {row["report_id"] for row in included}
    require(len(ids) == len(included) == 46, "Expected 46 distinct included reports")
    sources = [(row["report_id"], row["original_pdf"], row["original_pdf_sha256"]) for row in included]
    pending = {"R0081", "R0082", "R0132"}
    retrieval = RESTART / "fulltext_retrieval"
    pending_paths = {
        row["screening_id"]: (retrieval.relative_to(PROJECT) / row["local_path"], row["sha256"])
        for row in rows(retrieval / "retrieval_log.csv")
        if row["screening_id"] in pending and row["status"] == "RETRIEVED_PDF"
    }
    supplemental = RESTART / "supplemental_screening" / "screening_decisions.csv"
    pending_paths.update({row["id"]: (row["pdf"], row["sha256"]) for row in rows(supplemental)
                          if row["id"] in pending and row["decision"] == "AWAITING_CLASSIFICATION"})
    require(pending_paths.keys() == pending, "Missing PDF identity for a pending report")
    sources.extend((report_id, *pending_paths[report_id]) for report_id in sorted(pending))
    for report_id, relative, expected in sources:
        path = PROJECT / relative
        require(path.is_file(), f"{report_id}: original PDF missing at {relative}")
        require(sha256(path) == expected, f"{report_id}: original PDF checksum differs")
    return len(sources)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true", help="Record a snapshot after reviewing evidence changes")
    args = parser.parse_args()
    try:
        paths, label_count = check_index()
        original_count = check_originals()
        contrast_count = check_outcome_rows()
        snapshot = "".join(f"{sha256(path)}  {path.relative_to(PROJECT)}\n" for path in sorted(paths))
        if args.record:
            SNAPSHOT.write_text(snapshot)
        else:
            require(SNAPSHOT.is_file() and SNAPSHOT.read_text() == snapshot,
                    "Evidence snapshot differs. Review changed sources and the crosswalk before recording.")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Evidence check failed: {error}\n")
    print(f"PASS: {label_count} figures/tables/equations, {len(paths)} saved files, "
          f"{contrast_count} outcome rows, {original_count} original PDF checksums and complete LaTeX crosswalk.")


if __name__ == "__main__":
    main()
