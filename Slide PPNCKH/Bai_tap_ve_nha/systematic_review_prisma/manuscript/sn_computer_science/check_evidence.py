"""Check the HK261 manuscript evidence crosswalk and saved file identities."""
import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from functools import cache
from pathlib import Path

from build_editorial_evidence import review_log, outcome_tables

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
RESTART = PROJECT / "restart_2026_11_26"
FINAL = RESTART / "synthesis/final_46"
INDEX = HERE / "supplement_evidence_index.md"
SNAPSHOT = HERE / "evidence_sha256.txt"
CLAIM_AUDIT = HERE / "s4_claim_audit.md"
STUDY_ROW_MAP = HERE / "s4_study_row_sources.csv"

FIELD_GROUPS = {
    "t2_topology": ("uav_architecture_role_and_topology", "architecture"),
    "t2_workload": ("inference_model_task_and_dataset", "baselines_and_workloads", "workload", "baselines"),
    "t2_partition": ("partition_and_assignment", "partition_assignment"),
    "t2_decisions_objective_solver": ("decision_variables_objectives_constraints_and_solver", "optimization", "compute_and_radio", "compute_radio"),
    "t3_platform_modality": ("evaluation_platform_simulator_hardware_and_traces", "evaluation"),
    "t3_network_event_response": ("mobility_channel_intermittency_failure_and_recovery", "mobility_continuity", "compute_and_radio", "compute_radio"),
}


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
    require(labels == indexed and len(labels) == 16, f"Figure/table/equation coverage mismatch: {labels ^ indexed}")
    require((HERE / "prisma_flow.pdf").read_bytes() ==
            (RESTART / "prisma/prisma_flow.pdf").read_bytes(), "Embedded PRISMA PDF differs from accepted PDF")
    paths.add(RESTART / "prisma/prisma_flow.pdf")
    return paths, len(labels)


def check_outcome_rows():
    manuscript = (HERE / "main.tex").read_text()
    table = manuscript.split(r"\label{tab:outcomes}", 1)[1].split(r"\end{longtable}", 1)[0]
    report_ids = re.findall(r"^\\cite\{(R\d{4})\} &", table, re.M)
    ledger = rows(FINAL / "contrast_evidence.csv")
    keys = {(row["report_id"], row["key"]) for row in ledger}
    map_text = INDEX.read_text().split("## Numerical contrast row map", 1)[1].split("## Manuscript prose crosswalk", 1)[0]
    mapped = re.findall(r"^\| (R\d{4}) [^|]+\|([^|]+)\|", map_text, re.M)
    require(report_ids == [report for report, _ in mapped] and len(mapped) == 9, "Numerical contrast index differs")
    for report, cell in mapped:
        evidence = re.findall(r"`(quantity:\d+)`", cell)
        require(evidence and all((report, key) in keys for key in evidence),
                f"{report}: Numerical contrast evidence key missing from accepted ledger")
    return len(mapped)


def check_claim_audit():
    entries = re.findall(
        r"^\| (L(\d+)\.\d+) \| \[(\d+)\]\(main\.tex#L(\d+)\) \| "
        r"(SOURCE|RECORD|DERIVED|PROPOSAL|NARROWED|OPEN) \| [^|]+ \| [^|]+ \|$",
        CLAIM_AUDIT.read_text(), re.M,
    )
    require(len({entry[0] for entry in entries}) == len(entries), "Duplicate claim IDs")
    require(all(int(line) == int(text) == int(anchor) for _, line, text, anchor, _ in entries),
            "Claim line and link differ")
    main_lines = (HERE / "main.tex").read_text().splitlines()
    prose = set()
    in_equation = False
    for number, line in enumerate(main_lines, 1):
        if line.startswith(r"\begin{equation}"):
            in_equation = True
        if not in_equation and re.match(r"(?:[A-Z][^&]*$|where |\\abstract\{|\\item)", line):
            prose.add(number)
        if line.startswith(r"\end{equation}"):
            in_equation = False
    audited = {int(entry[1]) for entry in entries}
    require(prose == audited, f"Claim audit prose coverage differs: {sorted(prose ^ audited)}")
    return len(entries), len(audited)


@cache
def extraction_fields(path):
    return {report["report_id"]: report["fields"]
            for report in json.loads(path.read_text())["reports"]}


def field_locators(fields, keys):
    entries = []
    for key in keys:
        if key not in fields:
            continue
        observations = fields[key]
        for item in observations if isinstance(observations, list) else [observations]:
            locator = item.get("original_locator")
            if not locator:
                page = item.get("page")
                location = item.get("locator") or "section or table unspecified"
                locator = f"p. {page}, {location}" if page else f"page unavailable, {location}"
            additional = sorted({f"p. {source['physical_page']}, {source['locator']}"
                                 for source in item.get("sources", [])
                                 if source.get("physical_page") and source.get("locator")})
            if additional:
                locator += " [additional: " + "; ".join(additional) + "]"
            entries.append(f"{item.get('key', key)} [{item['status']}] {locator}")
    require(entries, f"No retained observation for {keys}")
    return "; ".join(entries)


def make_study_row_map(included):
    appraisal_path = FINAL / "appraisal_rationale.csv"
    judgments = {row["report_id"]: row for row in rows(appraisal_path) if row["domain"] == "D09"}
    require(judgments.keys() == {row["report_id"] for row in included}, "D09 study IDs differ")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(("report_id", "study_id", "original_pdf", "original_pdf_sha256",
                     "accepted_extraction", *FIELD_GROUPS, "t3_d09", "t3_d09_locator",
                     "t3_d09_rationale"))
    sources = {appraisal_path}
    for row in included:
        report_id = row["report_id"]
        extraction_path = PROJECT / row["extraction_source"]
        sources.add(extraction_path)
        fields = extraction_fields(extraction_path)[report_id]
        judgment = judgments[report_id]
        page = judgment["physical_page"]
        section = judgment["section"] or "section unspecified"
        writer.writerow((
            report_id, row["study_id"], row["original_pdf"], row["original_pdf_sha256"],
            row["extraction_source"], *(field_locators(fields, keys) for keys in FIELD_GROUPS.values()),
            judgment["judgment"], f"p. {page}, {section}" if page else f"page unavailable, {section}",
            judgment["rationale"],
        ))
    return output.getvalue(), sources


def check_originals():
    included = rows(FINAL / "synthesis_input_index.csv")
    ids = {row["report_id"] for row in included}
    require(len(ids) == len(included) == 46, "Expected 46 distinct included reports")
    sources = [(row["report_id"], row["original_pdf"], row["original_pdf_sha256"]) for row in included]
    ledger = json.loads((RESTART / "prisma/prisma_counts.json").read_text())
    require(ids == set(ledger["report_ids_by_fulltext_decision"]["INCLUDE"]), "Study rows differ from the PRISMA inclusion set")
    s2_priority_originals = {"R0081", "R0113", "R0132"}
    retrieval = RESTART / "fulltext_retrieval"
    pending_paths = {
        row["screening_id"]: (retrieval.relative_to(PROJECT) / row["local_path"], row["sha256"])
        for row in rows(retrieval / "retrieval_log.csv")
        if row["screening_id"] in s2_priority_originals and row["status"] == "RETRIEVED_PDF"
    }
    supplemental = RESTART / "supplemental_screening" / "screening_decisions.csv"
    pending_paths.update({row["id"]: (row["pdf"], row["sha256"]) for row in rows(supplemental)
                          if row["id"] in s2_priority_originals})
    require(pending_paths.keys() == s2_priority_originals, "Missing PDF identity for a priority S2 exclusion")
    sources.extend((report_id, *pending_paths[report_id]) for report_id in sorted(s2_priority_originals))
    for report_id, relative, expected in sources:
        path = PROJECT / relative
        require(path.is_file(), f"{report_id}: original PDF missing at {relative}")
        require(sha256(path) == expected, f"{report_id}: original PDF checksum differs")
    return len(sources), included


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true", help="Record a snapshot after reviewing evidence changes")
    args = parser.parse_args()
    try:
        paths, label_count = check_index()
        original_count, included = check_originals()
        contrast_count = check_outcome_rows()
        for filename, expected in outcome_tables().items():
            require((HERE / filename).read_text() == expected, f"Stale generated table: {filename}")
        subprocess.run([sys.executable, "-B", str(HERE / "audit_adjudication.py"), "--check"],
                       check=True, stdout=subprocess.DEVNULL)
        subprocess.run([sys.executable, "-B", str(FINAL / "reconcile_inputs.py"), "--check"],
                       check=True, stdout=subprocess.DEVNULL)
        baseline = list(csv.reader(io.StringIO(review_log())))
        with (HERE / "human_adjudication_log.csv").open(newline="") as stream:
            adjudication = list(csv.reader(stream))
        require(adjudication[0] == baseline[0] and
                [row[:6] for row in adjudication[1:]] == [row[:6] for row in baseline[1:]],
                "Human review log must preserve the 136 original evidence rows")
        claim_count, prose_lines = check_claim_audit()
        row_map, sources = make_study_row_map(included)
        if args.record:
            STUDY_ROW_MAP.write_text(row_map)
        else:
            require(STUDY_ROW_MAP.read_text() == row_map, "Study row map differs from accepted source locators")
        paths.update(sources | {CLAIM_AUDIT, STUDY_ROW_MAP})
        snapshot = "".join(f"{sha256(path)}  {path.relative_to(PROJECT)}\n" for path in sorted(paths))
        if args.record:
            SNAPSHOT.write_text(snapshot)
        else:
            require(SNAPSHOT.is_file() and SNAPSHOT.read_text() == snapshot,
                    "Evidence snapshot differs. Review changed sources and the crosswalk before recording.")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Evidence check failed: {error}\n")
    print(f"PASS: {claim_count} audit entries across {prose_lines} prose lines, "
          f"{len(included)} study rows, {label_count} figures/tables/equations, {len(paths)} saved files, "
          f"{contrast_count} outcome rows and {original_count} original PDF checksums.")


if __name__ == "__main__":
    main()
