"""Project the final HK261 corpus from locked source inputs and one evidence delta."""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNTHESIS = HERE.parent
RESTART = SYNTHESIS.parent
PROJECT = RESTART.parent
RQ5 = RESTART / "extraction/rq5_uniform"
APPRAISAL = RESTART / "appraisal"
ADDED = "R0082"
REMOVED = "R0113"
STATUSES = ("YES", "PARTIAL", "NOT_REPORTED", "NO", "NOT_APPLICABLE", "NOT_YET_ASSESSED")


def rows(path):
    with path.open(newline="", encoding="utf-8") as stream:
        table = csv.DictReader(stream)
        return table.fieldnames, list(table)


def serialize(fields, data):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(data)
    return stream.getvalue()


def sorted_rows(data):
    return sorted(data, key=lambda row: row["report_id"])


def render():
    ledger = json.loads((RESTART / "prisma/prisma_counts.json").read_text())
    decided = ledger["report_ids_by_fulltext_decision"]
    eligible = set(decided["INCLUDE"])
    study_ids = {
        report_id: study_id for study_id, members in ledger["study_ids_to_report_ids"].items()
        for report_id in members
    }
    delta = json.loads((HERE / "r0082_evidence.json").read_text())
    evidence = delta["reports"][0]
    identity = delta["identity"]
    source = identity["original_pdf"]
    digest = identity["original_pdf_sha256"]
    study_id = study_ids[ADDED]
    if evidence["report_id"] != ADDED or REMOVED not in decided["EXCLUDE"]:
        raise ValueError("Unexpected corpus correction")
    with (PROJECT / source).open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != digest:
            raise ValueError("R0082 source PDF checksum changed")
    def relative(path):
        return path.relative_to(PROJECT).as_posix()

    evidence_path = relative(HERE / "r0082_evidence.json")
    appraisal_path = relative(HERE / "appraisal_table.csv")
    rationale_path = relative(HERE / "appraisal_rationale.csv")
    versioned_review = relative(HERE / "r0082_review.md")
    result = {}

    def project_table(original, filename, extra):
        fields, baseline = rows(original)
        if {row["report_id"] for row in baseline} != (eligible - {ADDED}) | {REMOVED}:
            raise ValueError(f"Unexpected starting corpus in {original.name}")
        final = sorted_rows([row for row in baseline if row["report_id"] in eligible] +
                            [dict(row, report_id=ADDED, study_id=study_id) for row in extra])
        if filename != "appraisal_rationale.csv" and len(final) != len(eligible):
            raise ValueError(f"Duplicate or missing report row in {filename}")
        if {row["report_id"]: row["study_id"] for row in final} != study_ids:
            raise ValueError(f"Study identity mismatch in {filename}")
        result[filename] = serialize(fields, final)
        return final

    project_table(SYNTHESIS / "active_synthesis_input_index.csv", "synthesis_input_index.csv", [{
        "original_pdf": source, "original_pdf_sha256": digest, "extraction_source": evidence_path,
        "quantitative_source": relative(HERE / "report_coverage.csv"),
        "extraction_source_review": versioned_review, "appraisal_source": appraisal_path,
        "appraisal_locator_source": rationale_path,
    }])
    project_table(SYNTHESIS / "active_study_characteristics.csv", "study_characteristics.csv", [dict(
        delta["characteristics"], pdf_path=source, accepted_extraction_source=evidence_path)])
    if [item["domain"] for item in delta["appraisal"]] != [f"D{i:02}" for i in range(1, 11)]:
        raise ValueError("Expected one ordered R0082 judgment per appraisal domain")
    appraisal = project_table(APPRAISAL / "active_appraisal_table.csv", "appraisal_table.csv", [
        {item["domain"]: item["judgment"] for item in delta["appraisal"]}
    ])
    project_table(APPRAISAL / "active_appraisal_rationale_matrix.csv", "appraisal_rationale.csv", [
        dict(item, pdf_path=source, pdf_sha256=digest, batch="FINAL46_R0082",
             provider_uuid=delta["provider_uuid"]) for item in delta["appraisal"]
    ])
    coverage = project_table(RQ5 / "report_coverage.csv", "report_coverage.csv", [
        dict(delta["coverage"], source_pdf=source, pdf_sha256=digest)
    ])
    mechanism = project_table(SYNTHESIS / "desk_reject_evidence_map.csv", "mechanisms.csv", [
        dict(delta["mechanism"], source_pdf=source, accepted_extraction_source=evidence_path)
    ])
    summary = []
    for domain in (f"D{i:02}" for i in range(1, 11)):
        for status in STATUSES:
            member_ids = [row["report_id"] for row in appraisal if row[domain] == status]
            summary.append(dict(domain=domain, judgment=status, numerator=len(member_ids),
                                denominator=len(eligible), included_report_ids=" ".join(member_ids),
                                source=appraisal_path))
    if sum(row["numerator"] for row in summary) != len(eligible) * 10:
        raise ValueError("An appraisal judgment is missing or outside the rubric")
    result["appraisal_summary.csv"] = serialize(list(summary[0]), summary)
    fields, original_outcomes = rows(RQ5 / "outcomes.csv")
    outcomes = [row for row in original_outcomes if row["report_id"] in eligible]
    if delta["coverage"]["exact_outcome_status"] != "PLOT_ONLY":
        raise ValueError("R0082 numerical outcomes require a new verified outcome branch")
    result["outcomes.csv"] = serialize(fields, outcomes)
    fields, contrasts = rows(SYNTHESIS / "active_outcome_evidence.csv")
    result["contrast_evidence.csv"] = serialize(fields, [row for row in contrasts if row["report_id"] in eligible])
    fields, claims = rows(SYNTHESIS / "active_claim_source_matrix.csv")
    claims = [row for row in claims if row["report_id"] in eligible]
    for claim, key in (("RQ1-R0082", "partition_assignment"), ("RQ2-R0082", "optimization"),
                       ("RQ3-R0082", "evaluation"), ("RQ4-R0082", "mobility_continuity")):
        field = evidence["fields"][key]
        claims.append(dict(claim_id=claim, report_id=ADDED, study_id=study_id, source_path=source,
                           sha256=digest, physical_page=field["page"], section=field["locator"],
                           anchor=field["quote"], accepted_artifact=evidence_path,
                           accepted_key=key, judgment=field["status"]))
    result["claim_source_matrix.csv"] = serialize(fields, claims)
    sources = sorted_rows([dict(report_id=row["report_id"], study_id=row["study_id"],
                                path=row["source_pdf"], sha256=row["pdf_sha256"]) for row in coverage])
    result["outcome_manifest.json"] = json.dumps({"inputs": sources, "fixed_pending": ledger["awaiting_classification_codes"],
                                                 "fixed_unretrieved": ledger["report_ids_by_retrieval_decision"]["NOT_RETRIEVED"]},
                                                indent=2) + "\n"
    counts = Counter(row["comparison_status"] for row in outcomes)
    covered = Counter(row["exact_outcome_status"] for row in coverage)
    cells = Counter((row["mechanism"], row["evaluation_setting"]) for row in mechanism)
    metrics = dict(studies=len(eligible), outcome_ledger_rows=len(outcomes), outcome_rows=dict(counts),
                   coverage=dict(covered),
                   matched_reports=len({row["report_id"] for row in outcomes if row["comparison_status"] == "matched"}),
                   layers_total=sum(num for (code, _), num in cells.items() if code == "layer_or_stage"),
                   layers_software=cells["layer_or_stage", "software_or_trace"],
                   layers_physical=cells["layer_or_stage", "reported_physical_multi_uav"],
                   appraisal={domain: {row["judgment"]: row["numerator"] for row in summary if row["domain"] == domain}
                              for domain in (f"D{i:02}" for i in range(1, 11))})
    claim_fields, rq5_claims = rows(RQ5 / "claim_source.csv")
    for row in rq5_claims:
        key = row["claim_id"]
        if key == "RQ5-U01":
            row["source_file_or_outcome_key"] = "outcome_manifest.json; report_coverage.csv"
        if key == "RQ5-U02":
            row["claim"] = (f'{covered["VERIFIED_EXACT"]} verified numerical, {covered["PLOT_ONLY"]} plot-only, '
                            f'{covered["PRINTED_UNRESOLVED"]} printed unresolved')
        if key == "RQ5-U04":
            row.update(claim="Mechanism coverage and entry counts in Table 5",
                       source_file_or_outcome_key="report_coverage.csv; mechanisms.csv; outcomes.csv")
        if key == "RQ5-U09":
            row["source_file_or_outcome_key"] = "appraisal_table.csv; appraisal_summary.csv"
    rq5_claims.append(dict(claim_id="RQ5-U10", claim="R0082 contributes plot-only outcomes",
                           source_file_or_outcome_key="R0082 in report_coverage.csv; r0082_evidence.json",
                           derivation_or_locator="arXiv v1 physical pp. 5–6, §IV, Figs. 2–5; zero inferred values"))
    result["rq5_claim_sources.csv"] = serialize(claim_fields, rq5_claims)
    result["recomputed_counts.json"] = json.dumps(metrics, indent=2, sort_keys=True) + "\n"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for filename, content in render().items():
        path = HERE / filename
        if args.check:
            if path.read_text() != content:
                parser.exit(1, f"Stale final corpus input: {filename}\n")
        else:
            path.write_text(content)
    print("PASS: final synthesis data match the approved study and report IDs.")


if __name__ == "__main__":
    main()
