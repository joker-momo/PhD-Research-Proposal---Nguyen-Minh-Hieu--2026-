"""Project the final HK261 corpus from locked source inputs and one evidence delta."""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from fractions import Fraction
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
AUTHOR_LEDGER = RESTART / "integrity/source_review_887/r1_r2_reconciliation/author_decisions.csv"
AUTHOR_RELEASE = HERE / "author_decision_application.json"


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


def author_decisions():
    with AUTHOR_LEDGER.open(newline="", encoding="utf-8-sig") as stream:
        decisions = list(csv.DictReader(stream))
    release = json.loads(AUTHOR_RELEASE.read_text())
    entries = release["decisions"]
    keys = [(row["ma_bai"], row["khoa"], row["loai"]) for row in decisions]
    if (keys != [tuple(entry["key"]) for entry in entries] or len(set(keys)) != 12 or
            hashlib.sha256(AUTHOR_LEDGER.read_bytes()).hexdigest() != release["ledger_sha256"]):
        raise ValueError("Author decision application differs from the signed-off 12-item ledger")
    for row in decisions:
        with (PROJECT / row["pdf_goc"]).open("rb") as stream:
            if hashlib.file_digest(stream, "sha256").hexdigest() != row["pdf_goc_sha256"]:
                raise ValueError(f'{row["ma_bai"]}: author-decision PDF differs from confirmed source')
    return list(zip(decisions, entries))


def apply_rows(data, report_id, updates, **key_fields):
    selected = [row for row in data if row["report_id"] == report_id and
                all(row.get(key) == value for key, value in key_fields.items())]
    if not selected or (len(selected) != 1 and "domain" not in key_fields):
        raise ValueError(f"{report_id}: expected a unique target, or appraisal source rows, for {key_fields}")
    for row in selected:
        if not updates.keys() <= row.keys():
            raise ValueError(f"{report_id}: unexpected update fields {updates.keys() - row.keys()}")
        row.update(updates)


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
    author_entries = author_decisions()

    def project_table(original, filename, extra, coding=None):
        fields, baseline = rows(original)
        if {row["report_id"] for row in baseline} != (eligible - {ADDED}) | {REMOVED}:
            raise ValueError(f"Unexpected starting corpus in {original.name}")
        final = sorted_rows([row for row in baseline if row["report_id"] in eligible] +
                            [dict(row, report_id=ADDED, study_id=study_id) for row in extra])
        if filename != "appraisal_rationale.csv" and len(final) != len(eligible):
            raise ValueError(f"Duplicate or missing report row in {filename}")
        if {row["report_id"]: row["study_id"] for row in final} != study_ids:
            raise ValueError(f"Study identity mismatch in {filename}")
        if coding is not None:
            for row in final:
                code = coding[row["report_id"]]
                row.update(mechanism=code["unit"], evaluation_setting=code["evaluation"])
        result[filename] = serialize(fields, final)
        return final

    project_table(SYNTHESIS / "active_synthesis_input_index.csv", "synthesis_input_index.csv", [{
        "original_pdf": source, "original_pdf_sha256": digest, "extraction_source": evidence_path,
        "quantitative_source": relative(HERE / "report_coverage.csv"),
        "extraction_source_review": versioned_review, "appraisal_source": appraisal_path,
        "appraisal_locator_source": rationale_path,
    }])
    characteristics = project_table(SYNTHESIS / "active_study_characteristics.csv", "study_characteristics.csv", [dict(
        delta["characteristics"], pdf_path=source, accepted_extraction_source=evidence_path)])
    if [item["domain"] for item in delta["appraisal"]] != [f"D{i:02}" for i in range(1, 11)]:
        raise ValueError("Expected one ordered R0082 judgment per appraisal domain")
    appraisal = project_table(APPRAISAL / "active_appraisal_table.csv", "appraisal_table.csv", [
        {item["domain"]: item["judgment"] for item in delta["appraisal"]}
    ])
    rationales = project_table(APPRAISAL / "active_appraisal_rationale_matrix.csv", "appraisal_rationale.csv", [
        dict(item, pdf_path=source, pdf_sha256=digest, batch="FINAL46_R0082",
             provider_uuid=delta["provider_uuid"]) for item in delta["appraisal"]
    ])
    coverage = project_table(RQ5 / "report_coverage.csv", "report_coverage.csv", [
        dict(delta["coverage"], source_pdf=source, pdf_sha256=digest)
    ])
    coding_path = PROJECT / "manuscript/sn_computer_science/technical_coding.psv"
    with coding_path.open(newline="", encoding="utf-8") as stream:
        codes = list(csv.DictReader(stream, delimiter="|"))
    coding = {row["id"]: row for row in codes}
    if len(codes) != len(coding) or coding.keys() != eligible:
        raise ValueError("Primary coding differs from the final eligible set")
    mechanism = project_table(SYNTHESIS / "desk_reject_evidence_map.csv", "mechanisms.csv", [
        dict(delta["mechanism"], source_pdf=source, accepted_extraction_source=evidence_path)
    ], coding=coding)
    fields, original_outcomes = rows(RQ5 / "outcomes.csv")
    outcomes = [row for row in original_outcomes if row["report_id"] in eligible]
    if delta["coverage"]["exact_outcome_status"] != "PLOT_ONLY":
        raise ValueError("R0082 numerical outcomes require a new verified outcome branch")
    tables = {"study_characteristics.csv": characteristics, "appraisal_table.csv": appraisal,
              "appraisal_rationale.csv": rationales, "report_coverage.csv": coverage,
              "mechanisms.csv": mechanism, "outcomes.csv": outcomes}
    for decision, entry in author_entries:
        report_id, key, kind = entry["key"]
        if report_id not in eligible:
            raise ValueError(f"{report_id}: confirmed decision outside the frozen corpus")
        if kind == "appraisal":
            apply_rows(appraisal, report_id, {key: decision["quyet_dinh"]})
            apply_rows(rationales, report_id, {"judgment": decision["quyet_dinh"],
                                              "rationale": entry["applied"]}, domain=key)
        if kind == "outcome":
            patch = dict(entry["outcome_fields"])
            if "exact_seconds" in entry:
                decimal_values = [format(float(Fraction(value)), ".2f") for value in entry["exact_seconds"]]
                if patch.get("reported_value") != " / ".join(decimal_values):
                    raise ValueError(f"{report_id}-{key}: TTFT conversion is inconsistent")
            apply_rows(outcomes, report_id, patch, outcome_id=f"{report_id}-{key}")
        for filename, updates in entry.get("report_fields", {}).items():
            apply_rows(tables[filename], report_id, updates)
    cross_references = {row["outcome_id"]: row for row in outcomes
                        if row["report_id"] == "R0125"}
    q01, q02 = (cross_references[f"R0125-{key}"] for key in ("Q01", "Q02"))
    if (q01["comparison_status"] != "cross_reference" or q02["comparison_status"] != "descriptive" or
            q01["reported_value"] != q02["reported_value"].split(" / ")[0]):
        raise ValueError("R0125 two-worker measurement must be counted exactly once in Q02")
    retained = Counter(row["report_id"] for row in outcomes
                       if row["comparison_status"] in {"matched", "descriptive"})
    held = Counter(row["report_id"] for row in outcomes if row["comparison_status"] == "held")
    for row in coverage:
        report_id = row["report_id"]
        row.update(retained_numeric_rows=str(retained[report_id]), unresolved_printed_rows=str(held[report_id]))
    for row in mechanism:
        report_id = row["report_id"]
        row.update(retained_outcome_rows=str(retained[report_id]),
                   outcome_inventory_status=("RETAINED" if retained[report_id] else "NO_RETAINED_OUTCOME"))
    for filename, data in tables.items():
        result[filename] = serialize(list(data[0]), data)
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
    claims.extend(dict(claim_id=f"AUTHOR-PRIORITY-{row['thu_tu'].zfill(2)}", report_id=row["ma_bai"],
                       study_id=study_ids[row["ma_bai"]], source_path=row["pdf_goc"],
                       sha256=row["pdf_goc_sha256"], physical_page=row["trang_pdf"], section=row["muc"],
                       anchor=entry["applied"], accepted_artifact=relative(AUTHOR_LEDGER),
                       accepted_key=row["khoa"], judgment=entry["status"])
                  for row, entry in author_entries)
    result["claim_source_matrix.csv"] = serialize(fields, claims)
    sources = sorted_rows([dict(report_id=row["report_id"], study_id=row["study_id"],
                                path=row["source_pdf"], sha256=row["pdf_sha256"]) for row in coverage])
    result["outcome_manifest.json"] = json.dumps({"inputs": sources, "fixed_pending": ledger["awaiting_classification_codes"],
                                                 "fixed_unretrieved": ledger["report_ids_by_retrieval_decision"]["NOT_RETRIEVED"]},
                                                indent=2) + "\n"
    counts = Counter(row["comparison_status"] for row in outcomes)
    covered = Counter(row["exact_outcome_status"] for row in coverage)
    def describe(omitted):
        selected = eligible - set(omitted)
        records = [row for row in outcomes if row["report_id"] in selected
                   and row["comparison_status"] in {"matched", "descriptive"}]
        return dict(studies=len(selected), entries=len(records),
                    matched_entries=sum(row["comparison_status"] == "matched" for row in records),
                    studies_with_entries=len({row["report_id"] for row in records}),
                    coverage=dict(Counter(row["exact_outcome_status"] for row in coverage
                                          if row["report_id"] in selected)),
                    partition=dict(Counter(coding[key]["unit"] for key in selected)),
                    modality=dict(Counter(coding[key]["evaluation"] for key in selected)))
    alternatives = ((), ("R0145",), ("R0223",), ("R0145", "R0223"))
    result["scope_sensitivity.json"] = json.dumps(
        {"basis": "Descriptive recalculation after the 12 author decisions, with frozen eligibility.",
         "scenarios": [dict(omitted=keys, **describe(keys)) for keys in alternatives]},
        indent=2, sort_keys=True) + "\n"
    cells = Counter((row["mechanism"], row["evaluation_setting"]) for row in mechanism)
    metrics = dict(studies=len(eligible), outcome_ledger_rows=len(outcomes), outcome_rows=dict(counts),
                   coverage=dict(covered),
                   matched_reports=len({row["report_id"] for row in outcomes if row["comparison_status"] == "matched"}),
                   layers_total=sum(num for (code, _), num in cells.items() if code == "layer"),
                   layers_software=cells["layer", "sim"] + cells["layer", "trace"],
                   layers_outdoor=cells["layer", "flight"],
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
        if key == "RQ5-U03":
            row["claim"] = (f'{counts["matched"] + counts["descriptive"]} retained rows: '
                            f'{counts["matched"]} matched and {counts["descriptive"]} descriptive. '
                            f'Matched rows from {metrics["matched_reports"]} studies.')
        if key == "RQ5-U04":
            row.update(claim="Mechanism coverage and entry counts in Table 5",
                       source_file_or_outcome_key="report_coverage.csv; mechanisms.csv; outcomes.csv")
        if key == "RQ5-U09":
            row["source_file_or_outcome_key"] = "appraisal_table.csv; appraisal_summary.csv"
    rq5_claims.append(dict(claim_id="RQ5-U10", claim="R0082 contributes plot-only outcomes",
                           source_file_or_outcome_key="R0082 in report_coverage.csv; r0082_evidence.json",
                           derivation_or_locator="IEEE WCNC and arXiv v1 physical pp. 5–6, §IV, Figs. 2–5; zero inferred values"))
    rq5_claims.extend(dict(claim_id=f"RQ5-AUTHOR-{row['thu_tu'].zfill(2)}", claim=entry["applied"],
                           source_file_or_outcome_key=f"{row['ma_bai']}-{row['khoa']}",
                           derivation_or_locator=f"PDF p. {row['trang_pdf']}, {row['muc']}. {entry['open']}".strip())
                      for row, entry in author_entries if row["loai"] == "outcome")
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
