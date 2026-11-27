"""Reconcile the HK261 restart and regenerate its PRISMA count and flow files."""
import argparse
from collections import Counter
import csv
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def index(rows, key, label):
    keyed = {}
    for row in rows:
        value = row[key]
        require(value and value not in keyed, f"{label}: missing/duplicate {key}: {value}")
        keyed[value] = row
    return keyed


def eq(left, right, label):
    require(left == right, f"{label}: mismatch")


def split(rows, field, allowed=None):
    groups = {}
    for key, row in sorted(rows.items()):
        value = row[field]
        require(value and (allowed is None or value in allowed), f"{key}: bad {field} {value}")
        groups.setdefault(value, []).append(key)
    return dict(sorted(groups.items()))


def audit_baseline(project):
    restart = project / "restart_2026_11_26"
    hashes = {}

    def open_path(relative):
        path = restart / relative
        hashes[relative] = sha256(path.read_bytes()).hexdigest()
        return path

    def read_json(relative):
        return json.loads(open_path(relative).read_text())

    def read_csv(relative, field):
        with open_path(relative).open(newline="", encoding="utf-8-sig") as handle:
            return index(csv.DictReader(handle), field, relative)

    source = read_json("search_dataset_manifest.json")
    eq(source["legacy_46_records_imported"], 0, "prior-corpus import count")
    eq(source["wos"], {"status": "not_searched_access_unavailable", "count": None}, "WoS")
    records = read_csv("records_normalized.csv", "record_id")
    source_files = split(records, "source_file")
    eq(set(source_files), {item["path"] for item in source["canonical_raw_inputs"]}, "raw sources")
    raw = {}
    for item in source["canonical_raw_inputs"]:
        path = item["path"]
        digest = sha256((project / path).read_bytes()).hexdigest()
        eq(digest, item["sha256"], path)
        ids = sorted(source_files[path], key=lambda key: int(records[key]["source_record_number"]))
        eq([int(records[key]["source_record_number"]) for key in ids],
           list(range(1, item["rows"] + 1)), f"{path}: physical export row coverage")
        require(all(records[key]["source"] == item["source"] for key in ids), f"{path}: source mismatch")
        raw[path] = {"source": item["source"], "query_id": item["query_id"],
                     "sha256": digest, "record_ids_in_data_row_order": ids}
    by_source = split(records, "source")
    eq({key: len(ids) for key, ids in by_source.items()}, source["rows_by_source"], "source counts")
    eq(len(records), source["rows_before_normalization_and_dedup"], "raw total")
    runs = index(source["selected_runs"], "evidence_locator", "selected search runs")
    for path, run in runs.items():
        eq(sha256((project / path).read_bytes()).hexdigest(), run["evidence_sha256"], f"{path}: run hash")
    eq(sum(run["selected_rows"] for run in runs.values()), len(records), "rows from selected search runs")

    dedup = read_csv("dedup_map.csv", "record_id")
    queue = read_csv("unique_record_queue.csv", "screening_id")
    eq(set(dedup), set(records), "dedup input IDs")
    members = split(dedup, "screening_id")
    eq(set(members), set(queue), "dedup representative groups")
    reps = split(dedup, "link_reason", {"representative", "matching_doi_and_title",
                                        "exact_title_year_acm_proceeding"})
    representative_records = set(reps["representative"])
    eq(representative_records, {row["record_id"] for row in queue.values()}, "representatives")
    for key, row in queue.items():
        eq(row["member_count"], str(len(members[key])), f"{key}: member count")
        eq(set(members[key]) & representative_records, {row["record_id"]}, f"{key}: representative")

    title = read_csv("title_abstract_screening.csv", "screening_id")
    eq(set(title), set(queue), "title/abstract screen IDs")
    title_groups = split(title, "decision", {"RETRIEVE_FULL_TEXT", "EXCLUDE", "UNCLEAR"})
    for key, row in title.items():
        eq(dedup[row["evidence_record_id"]]["screening_id"], key, f"{key}: screening evidence")
    title_exclusions = split({k: title[k] for k in title_groups["EXCLUDE"]}, "primary_E_code")

    retrieval = read_csv("fulltext_retrieval/retrieval_log.csv", "screening_id")
    eq(set(retrieval), set(title_groups["RETRIEVE_FULL_TEXT"] + title_groups["UNCLEAR"]), "sought report IDs")
    for key, row in retrieval.items():
        eq(row["decision"], title[key]["decision"], f"{key}: retrieval handoff")
    retrieval_groups = split(retrieval, "status", {"RETRIEVED_PDF", "NOT_RETRIEVED"})
    missing = read_csv("fulltext_retrieval/missing_pdf.csv", "screening_id")
    eq(set(missing), set(retrieval_groups["NOT_RETRIEVED"]), "missing PDF IDs")
    for key, row in missing.items():
        eq(row["reason_if_no_pdf"], retrieval[key]["reason_if_no_pdf"], f"{key}: missing reason")
    identity = read_csv("fulltext_retrieval/fulltext_identity_index.csv", "screening_id")
    screen = read_csv("fulltext_screening/fulltext_screening.csv", "screening_id")
    eq(set(identity), set(screen), "assessed report IDs vs identity index")
    eq(set(screen), set(retrieval_groups["RETRIEVED_PDF"]), "retrieved vs assessed report IDs")
    for key, row in screen.items():
        eq(row["sha256"], identity[key]["sha256"], f"{key}: PDF hash")
        eq(row["sha256"], retrieval[key]["sha256"], f"{key}: retrieval hash")
        canonical_pdf = restart / "fulltext_retrieval" / identity[key]["local_path"]
        eq(row["pdf_path"], canonical_pdf.relative_to(project).as_posix(), f"{key}: PDF path")
    screen_groups = split(screen, "decision", {"INCLUDE", "EXCLUDE", "AWAITING_CLASSIFICATION"})
    excluded = read_csv("fulltext_screening/exclusions.csv", "screening_id")
    eq(excluded, {k: screen[k] for k in screen_groups["EXCLUDE"]}, "full-text exclusions")
    excluded_by_reason = split(excluded, "primary_reason_code", {f"E{i}" for i in range(1, 8)})
    unresolved = {key: screen[key]["unresolved_codes"] for key in screen_groups["AWAITING_CLASSIFICATION"]}
    require(all(unresolved.values()), "full-text pending reports require unresolved codes")

    linkage = read_json("study_linkage/manifest.json")
    eq(linkage["screen_sha256"], hashes["fulltext_screening/fulltext_screening.csv"], "linkage input hash")
    study_map = read_csv("study_linkage/report_study_map.csv", "report_id")
    eq(set(study_map), set(screen_groups["INCLUDE"]), "included report-to-study mapping")
    eq(set(linkage["included_ids"]), set(study_map), "linkage manifest report IDs")
    pairs = read_csv("study_linkage/pair_evidence.csv", "pair_id")
    pair_keys = set()
    for row in pairs.values():
        pair = frozenset((row["report_a"], row["report_b"]))
        require(len(pair) == 2 and pair <= study_map.keys() and pair not in pair_keys, "invalid linkage pair")
        eq(row["decision"], "DISTINCT", "linkage pair decision")
        pair_keys.add(pair)
    require({frozenset(pair) for pair in linkage["priority_pairs"]} <= pair_keys,
            "all priority linkage pairs must have been assessed")
    eq(linkage["all_pairs"], len(study_map) * (len(study_map) - 1) // 2, "candidate universe")
    eq(read_csv("study_linkage/unresolved_families.csv", "pair_id"), {}, "unresolved linkage families")
    studies = split(study_map, "study_id")
    require(all(len(ids) == 1 for ids in studies.values()), "new merges require reconciliation logic")

    p08 = read_json("extraction/p08_extraction_lock.json")
    p09 = read_json("appraisal/p09_appraisal_lock.json")
    eq(p08["status"], "LOCKED_P08_PASS", "P08 gate")
    eq(p09["gate"], "PASS", "P09 gate")
    for lock in (p08["artifacts"], p09["artifact_sha256"]):
        for path, digest in lock.items():
            eq(sha256((project / path).read_bytes()).hexdigest(), digest, f"{path}: lock hash")
    extraction = index(read_json("extraction/p08_extraction_table.json")["reports"], "report_id", "P08")
    eq(set(extraction), set(study_map), "P08 report IDs")
    for key, row in extraction.items():
        eq(row["pdf_sha256"], screen[key]["sha256"], f"{key}: P08 PDF hash")
    appraisal = read_csv("appraisal/appraisal_table.csv", "report_id")
    eq(set(appraisal), set(study_map), "P09 report IDs")
    eq(p08["reports"], len(study_map), "P08 locked total")
    eq(p09["reports"], len(study_map), "P09 locked total")
    eq(p09["judgments"], len(study_map) * p09["domains_per_report"], "P09 locked judgment total")
    eq(p09["pending_judgments"], 0, "P09 pending")

    counts = {
        "raw_records": len(records), "duplicate_records_removed": len(records) - len(queue),
        "records_screened": len(title), "records_excluded": len(title_groups["EXCLUDE"]),
        "reports_sought": len(retrieval), "reports_not_retrieved": len(missing),
        "reports_assessed": len(screen), "reports_excluded": len(excluded),
        "reports_awaiting_classification": len(unresolved), "included_reports": len(study_map),
        "included_studies": len(studies),
    }
    differences = {
        "identified_minus_duplicates_and_screened": counts["raw_records"] - counts["duplicate_records_removed"] - counts["records_screened"],
        "screened_minus_excluded_and_sought": len(title) - counts["records_excluded"] - len(retrieval),
        "sought_minus_unretrieved_and_assessed": len(retrieval) - len(missing) - len(screen),
        "assessed_minus_excluded_pending_and_included": len(screen) - len(excluded) - len(unresolved) - len(study_map),
    }
    require(not any(differences.values()), f"unexplained differences: {differences}")
    return {
        "dataset_id": source["dataset_id"], "wos": source["wos"], "counts": counts,
        "arithmetic_differences": differences, "raw_file_index": raw, "record_ids_by_source": by_source,
        "dedup_groups": members, "raw_ids_by_dedup_reason": reps,
        "screening_ids_by_title_abstract_decision": title_groups,
        "title_abstract_exclusions_by_reason": title_exclusions,
        "report_ids_by_retrieval_decision": retrieval_groups,
        "retrieval_counts_by_title_decision": {
            key: dict(Counter(retrieval[i]["status"] for i in ids))
            for key, ids in title_groups.items() if key != "EXCLUDE"
        },
        "not_retrieved_by_reason": split(missing, "reason_if_no_pdf"),
        "report_ids_by_fulltext_decision": screen_groups, "fulltext_exclusions_by_primary_reason": excluded_by_reason,
        "awaiting_classification_codes": unresolved, "study_ids_to_report_ids": studies,
        "tested_version_pairs": {key: [row["report_a"], row["report_b"], row["decision"]] for key, row in pairs.items()},
        "input_sha256_relative_to_restart": hashes,
    }


def audit_supplemental(project, baseline):
    restart = project / "restart_2026_11_26"
    supplemental = restart / "supplemental_screening"
    linkage = restart / "study_linkage"
    inputs = []
    linkage_map = linkage / "active_report_study_map.csv"

    def read_json(path):
        inputs.append(path)
        return json.loads(path.read_text())

    for phase, lock_path, status in (
        ("P08", restart / "extraction/active_p08_extraction_lock.json", "LOCKED_ACTIVE_P08_PASS"),
        ("P09", restart / "appraisal/active_p09_appraisal_lock.json", "LOCKED_ACTIVE_P09_PASS"),
    ):
        lock = read_json(lock_path)
        eq(lock["status"], status, f"{phase} active gate")
        eq(lock["study_linkage"]["path"], linkage_map.relative_to(project).as_posix(), f"{phase} linkage path")
        eq(sha256(linkage_map.read_bytes()).hexdigest(), lock["study_linkage"]["sha256"], f"{phase} linkage SHA-256")
        if phase == "P08":
            eq(lock["outstanding_reports"], [], "P08 outstanding reports")
            active_p08 = lock
        else:
            eq(lock["pending_judgments"], 0, "P09 pending judgments")
            eq(sha256((project / lock["active_p08"]["path"]).read_bytes()).hexdigest(),
               lock["active_p08"]["sha256"], "P09 consumed P08 SHA-256")
            for relative, digest in lock["artifact_sha256"].items():
                eq(sha256((project / relative).read_bytes()).hexdigest(), digest, f"P09 {relative} SHA-256")
            active_p09 = lock


    def read_csv(path, key):
        inputs.append(path)
        with path.open(newline="", encoding="utf-8-sig") as source:
            return index(csv.DictReader(source), key, path.name)

    original = read_csv(restart / "fulltext_screening/fulltext_screening.csv", "screening_id")
    addition = read_csv(supplemental / "screening_decisions.csv", "id")
    missing = read_csv(restart / "fulltext_retrieval/missing_pdf.csv", "screening_id")
    retrieval_meta = read_json(supplemental / "manifest.json")
    eq(retrieval_meta["not_retrieved"], ["R0116"], "supplemental screening unretrieved IDs")
    intake = read_csv(supplemental / "supplemental_intake.csv", "id")
    eq(set(intake), set(addition), "intake and screened supplement IDs")
    eq(set(original) & set(addition), set(), "baseline/supplemental overlap")
    eq(set(missing) - set(addition), {"R0116"}, "unretrieved report")
    eq(set(addition) - set(missing), set(), "supplemental not part of original shortfall")

    recheck_path = supplemental / "prior_awaiting_recheck.json"
    recheck = index(read_json(recheck_path)["records"], "id", recheck_path.name)
    eq(set(recheck), set(baseline["awaiting_classification_codes"]), "baseline recheck coverage")
    partition = {
        key: {"status": row["decision"], "reason": row["primary_reason_code"],
              "pending": row["unresolved_codes"], "pdf": row["pdf_path"], "sha256": row["sha256"]}
        for key, row in original.items()
    }
    for key, row in recheck.items():
        eq((row["pdf"], row["sha256"]), (partition[key]["pdf"], partition[key]["sha256"]), f"{key}: recheck identity")
        partition[key]["status"] = row["decision_supported_by_round_01"]
        partition[key]["pending"] = "|".join(row["criterion_to_resolve"])

    normalized_ids = set()
    decision_files = set()
    for key, row in addition.items():
        eq((row["doi"], row["sha256"], row["physical_pages"]),
           (intake[key]["doi"], intake[key]["sha256"], intake[key]["physical_pages"]),
           f"{key}: intake and screening identity")
        doi = row["doi"].casefold()
        if doi:
            require(doi not in normalized_ids, f"{key}: duplicate supplemental DOI")
            normalized_ids.add(doi)
        decision_path = project / row["decision_evidence"]
        require(decision_path.is_file() and row["principal_locators"], f"{key}: missing decision evidence")
        decision_files.add(decision_path)
        partition[key] = {
            "status": row["decision"], "reason": row["primary_reason"],
            "pending": row["unresolved_criteria"], "pdf": row["pdf"], "sha256": row["sha256"],
        }

    inputs.extend(sorted(decision_files))
    catalog_path = project / "prisma_evidence/evidence_by_id.csv"
    inputs.append(catalog_path)
    with catalog_path.open(newline="", encoding="utf-8-sig") as handle:
        pdfs = index(
            (row for row in csv.DictReader(handle) if row["evidence_type"] in {"BASELINE_PDF", "SUPPLEMENTAL_PDF"}),
            "id", "original PDF catalog",
        )
    eq(set(partition), set(pdfs), "PDF catalog coverage")
    repository_prefix = project.relative_to(project.parents[2])
    for key, row in partition.items():
        catalog_relative = Path(pdfs[key]["repo_path"]).relative_to(repository_prefix).as_posix()
        eq((row["pdf"], row["sha256"]), (catalog_relative, pdfs[key]["sha256"]), f"{key}: catalog identity")
        eq(sha256((project / row["pdf"]).read_bytes()).hexdigest(), row["sha256"], f"{key}: original PDF checksum")

    groups = split(partition, "status", {"INCLUDE", "EXCLUDE", "AWAITING_CLASSIFICATION"})
    reasons = split({key: partition[key] for key in groups["EXCLUDE"]}, "reason", {f"E{i}" for i in range(1, 8)})
    pending = {key: partition[key]["pending"] for key in groups["AWAITING_CLASSIFICATION"]}
    eq(pending, {"R0081": "E7", "R0082": "E7", "R0132": "E2|E3"}, "pending statuses")
    study_map = read_csv(linkage_map, "report_id")
    eq(set(study_map), set(groups["INCLUDE"]), "active study-linkage coverage")
    studies = split(study_map, "study_id")
    eq((active_p08["reports_verified"], active_p08["studies_verified"]),
       (len(study_map), len(studies)), "P08 active totals")
    eq((active_p09["reports"], active_p09["studies"]),
       (len(study_map), len(studies)), "P09 active totals")
    eq(active_p09["judgments"], len(study_map) * active_p09["domains_per_report"], "P09 decision count")
    appraisal = read_csv(restart / "appraisal/active_appraisal_table.csv", "report_id")
    eq(set(appraisal), set(study_map), "P09 exact included report IDs")
    for key, row in appraisal.items():
        eq(row["study_id"], study_map[key]["study_id"], f"{key}: P09 study ID")

    pairs = read_csv(linkage / "active_pair_evidence.csv", "pair_id")
    merged_pairs = set()
    for row in pairs.values():
        a, b = row["report_a"], row["report_b"]
        require(a < b and a in study_map and b in study_map, "invalid study-linkage pair")
        eq(row["pair_id"], f"{a}/{b}", "pair key")
        require(row["decision"] in {"DISTINCT", "SAME_STUDY"}, "unresolved linkage family")
        eq(study_map[a]["study_id"] == study_map[b]["study_id"], row["decision"] == "SAME_STUDY",
           f"{a}/{b}: linkage and study group disagree")
        if row["decision"] == "SAME_STUDY":
            merged_pairs.add(frozenset((a, b)))
    for members in studies.values():
        connected = {members[0]}
        for _ in members:
            for edge in merged_pairs:
                if edge & connected:
                    connected |= edge
        eq(connected, set(members), "study merge lacks connected evidence")
        for report in members:
            eq(study_map[report]["group_member_reports"], "|".join(members), f"{report}: study membership")

    retrieval_groups = {"NOT_RETRIEVED": ["R0116"], "RETRIEVED_PDF": sorted(partition)}
    sought = set().union(*map(set, baseline["report_ids_by_retrieval_decision"].values()))
    eq(set(partition) | {"R0116"}, sought, "sought/assessed set identity")
    by_title_decision = baseline["screening_ids_by_title_abstract_decision"]
    by_initial = {
        status: dict(Counter("RETRIEVED_PDF" if key in partition else "NOT_RETRIEVED" for key in ids))
        for status, ids in by_title_decision.items() if status != "EXCLUDE"
    }
    counts = baseline["counts"] | {
        "reports_not_retrieved": 1,
        "reports_assessed": len(partition),
        "reports_excluded": len(groups["EXCLUDE"]),
        "reports_awaiting_classification": len(pending),
        "included_reports": len(study_map),
        "included_studies": len(studies),
    }
    differences = baseline["arithmetic_differences"] | {
        "sought_minus_unretrieved_and_assessed": len(sought) - 1 - len(partition),
        "assessed_minus_excluded_pending_and_included": len(partition) - counts["reports_excluded"] - len(pending) - len(study_map),
    }
    require(not any(differences.values()), "unexplained PRISMA count differences")
    return baseline | {
        "counts": counts,
        "supplemental_retrieval": {"original_missing": len(missing), "recovered": len(addition),
                                   "unretrieved": len(missing) - len(addition)},

        "arithmetic_differences": differences,
        "report_ids_by_retrieval_decision": retrieval_groups,
        "retrieval_counts_by_title_decision": by_initial,
        "not_retrieved_by_reason": {"NO_VERIFIED_PDF_FROM_CHECKED_ROUTES": ["R0116"]},
        "report_ids_by_fulltext_decision": groups,
        "fulltext_exclusions_by_primary_reason": reasons,
        "awaiting_classification_codes": pending,
        "study_ids_to_report_ids": studies,
        "tested_version_pairs": {key: [row["report_a"], row["report_b"], row["decision"]] for key, row in pairs.items()},
        "supplemental_input_sha256_relative_to_project": {
            path.relative_to(project).as_posix(): sha256(path.read_bytes()).hexdigest() for path in inputs
        },
    }


def audit(project):
    return audit_supplemental(project, audit_baseline(project))

def main():
    project = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = audit(project)
    output = Path(__file__).with_name("prisma_counts.json")
    expected = json.dumps(result, indent=2, sort_keys=True) + "\n"
    reasons = {
        "E1": "Secondary or non-primary report",
        "E2": "No evaluated multi-UAV system",
        "E3": "No collaborative inference",
        "E4": "No evaluative evidence",
        "E5": "Outside the publication window",
        "E6": "Language ineligible",
        "E7": "Incomplete or ineligible report type",
    }
    reason_text = r"\\ ".join(
        f"{reasons[code]}: {len(ids)}" for code, ids in result["fulltext_exclusions_by_primary_reason"].items()
    )
    variables = result["counts"] | {key: len(ids) for key, ids in result["record_ids_by_source"].items()}
    flow_template = output.with_name("flow_template.tex")
    flow = flow_template.read_text()
    for key, value in (variables | {"reasons": reason_text}).items():
        flow = flow.replace(f"@{key}@", str(value))
    require("@" not in flow, "unexpanded flow template variables")
    flow_file = output.with_name("prisma_flow.tex")
    if args.check:
        eq(output.read_text(), expected, "derived PRISMA count artifact")
        eq(flow_file.read_text(), flow, "derived PRISMA flow source")
    else:
        output.write_text(expected)
        flow_file.write_text(flow)
    print(json.dumps(result["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
