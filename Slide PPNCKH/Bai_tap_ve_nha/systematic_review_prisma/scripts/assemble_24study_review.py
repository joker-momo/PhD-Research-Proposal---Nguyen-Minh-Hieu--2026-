"""Extend the source-checked interim corpus with C01; never infer missing evidence."""
import collections
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "interim_26report"
OUT = ROOT / "interim_27report"
SOURCE = ROOT / "corpus_expansion"
view = json.loads((SOURCE / "c01_accepted_record_v2.json").read_text())
q9 = json.loads((SOURCE / "c01_protocol_q9_notes.json").read_text())["records"][0]
gate = json.loads((SOURCE / "c01_protocol_q9_acceptance.json").read_text())
assert gate["verdict"] == "PASS" and all(v == "PASS" for v in gate["checks"].values())
record = next(r for r in view["records"] if r["candidate_id"] == "C01")
assessment = view["C01_fulltext_assessment"]
e = assessment["extraction"]
assert len(assessment["inclusion_checks"]) == len(assessment["exclusion_checks"]) == 7
assert all(c["status"] == "YES" for c in assessment["inclusion_checks"])
assert all(c["status"] == "NO" for c in assessment["exclusion_checks"])
assert len(e) == 17 and len(assessment["appraisal"]) == 10
assert q9["candidate_id"] == "C01" and q9["q9_verdict"] in {"yes", "partial", "no", "not_applicable"}
assert not assessment["comparative_numeric_findings"]
OUT.mkdir(exist_ok=True)

def read(name):
    with (BASE / name).open(newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames), list(reader)

def write(name, fields, rows):
    with (OUT / name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

boundary = ("Publisher HTML, not a downloaded PDF. Simulation of heterogeneous edge nodes; "
            "no measured onboard or physical multi-UAV flight validation. Speculative-token rollback "
            "is not UAV-failure recovery. No comparative performance effects synthesized. "
            "Semantic study-family and final author adjudication pending.")
fields, extraction = read("data_extraction_eligible.csv")
row = dict.fromkeys(fields, "")
row.update(study_id="C01", year="2026", architecture_and_uav_role=e["architecture_and_uav_role"],
           dnn_or_workload=e["model_and_dataset"], partition_or_collaboration=e["partition_granularity"],
           decision_variables=e["decision_variables_objective_constraints"],
           objective="Minimize pipeline bottleneck computation-plus-communication latency with memory constraints; no pooled effect",
           solution_method=e["solver"], mobility_failure_or_recovery=e["mobility_channel_failure_assumptions"],
           evaluation=e["evaluation_setup"] + " " + e["repeated_runs_seeds"], baselines=e["baselines"],
           reported_outcomes=e["metric_definitions"],
           selected_quantitative_finding="NOT_USED_IN_QUALITATIVE_SYNTHESIS",
           evidence_locator=e["source_locators"], evidence_boundary=boundary,
           public_artifact="not_located")
extraction.append(row)
write("data_extraction_eligible.csv", fields, extraction)

fields, evidence = read("evidence_map.csv")
flags = dict.fromkeys(fields, "no")
flags.update(study_id="C01", evaluation_mode="simulation", simulation="yes",
             latency_performance_outcome="yes", communication_or_power_outcome="no",
             mobility_modeled="partial", uncertainty_or_repeated_run_reporting="yes",
             architecture_group="peer_uav_contiguous_layer_pipeline",
             latency_scope="LLM_prefill_and_end_to_end_latency",
             source_version="publisher_html", flag_locator=e["source_locators"],
             evidence_boundary=boundary)
evidence.append(flags)
write("evidence_map.csv", fields, evidence)

fields, quality = read("quality_appraisal_eligible.csv")
qfields = [f for f in fields if re.match(r"q\d+_", f)]
assert len(qfields) == 10
row = dict.fromkeys(fields, "")
row.update(study_id="C01", report_id="C01_publisher_html",
           appraiser="Read-only routed research notes; Codex source and criterion check",
           verification_status="checked_working_appraisal_final_author_and_global_q9_audit_pending")
for f, appraisal in zip(qfields, assessment["appraisal"]):
    row[f] = appraisal["verdict"]
row["q9_artifact_availability"] = q9["q9_verdict"]
rationales = []
for i, appraisal in enumerate(assessment["appraisal"], 1):
    rationale = q9["q9_rationale"] if i == 9 else appraisal["rationale"]
    locator = q9["source_url"] + "; implementation_evidence locators" if i == 9 else appraisal["locator"]
    rationales.append(f"Q{i}: {rationale} [{locator}]")
row["rationale"] = " | ".join(rationales)
quality.append(row)
write("quality_appraisal_eligible.csv", fields, quality)

fields, eligibility = read("eligibility_reaudit.csv")
fields += ["fulltext_format", "fulltext_locator"]
for old in eligibility:
    old["fulltext_format"] = "PDF" if old["pdf_file"].lower().endswith(".pdf") else "HTML"
    old["fulltext_locator"] = old["pdf_file"]
doi = lambda value: re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value.strip().lower())
title = lambda value: re.sub(r"[^a-z0-9]", "", value.lower())
assert not any(doi(r["doi"]) == doi(record["doi"]) or title(r["title"]) == title(record["title"]) for r in eligibility)
row = dict.fromkeys(fields, "")
row.update(study_id="C01", title=record["title"], authors=" | ".join(record["authors"]),
           year="2026", venue="Drones 10(6):410", doi=record["doi"], pdf_file="NOT_DOWNLOADED",
           page_count="26 (publisher header; HTML inspected)", publication_type="Peer-reviewed journal article; publisher HTML",
           eligibility_status="INCLUDE", primary_reason=assessment["primary_reason"],
           evidence_locators=" | ".join(c["locator"] for c in assessment["inclusion_checks"] + assessment["exclusion_checks"]),
           source_urls=record["fulltext_url"], verification_boundary=boundary,
           fulltext_format="HTML", fulltext_locator=record["fulltext_url"])
eligibility.append(row)
write("eligibility_reaudit.csv", fields, eligibility)

assert len(extraction) == len(evidence) == len(quality) == 24
for rows in [extraction, evidence, quality, eligibility]:
    assert len({r["study_id"] for r in rows}) == len(rows)
assert len(eligibility) == 27
assert collections.Counter(r["eligibility_status"] for r in eligibility) == {"INCLUDE":24, "EXCLUDE":1, "UNCERTAIN":2}
counts = {key: sum(r[key] == "yes" for r in evidence) for key in
          ("physical_prototype", "simulation", "emulation", "analytical_only", "latency_performance_outcome",
           "energy_outcome", "node_unavailability_evaluated", "recovery_or_migration_mechanism",
           "uncertainty_or_repeated_run_reporting", "public_artifact_found", "multi_uav_physical_flight_evaluated")}
appraisal_counts = dict(collections.Counter(r[f] for r in quality for f in qfields))
domains = {f: dict(collections.Counter(r[f] for r in quality)) for f in qfields}
summary = dict(assessed_reports=27, included=24, excluded=1, uncertain=2,
               added_study_ids=["C01"], evidence_counts=counts, appraisal=appraisal_counts,
               appraisal_domains=domains,
               fulltext_formats=dict(collections.Counter(r["fulltext_format"] for r in eligibility)),
               appraisal_boundary="C01 domain9 applies literal protocol; prior23 domain9 labels require a corpus-wide audit; aggregate provisional",
               scope="Qualitative working synthesis; not final database PRISMA or author-adjudicated corpus",
               numeric_effects="No comparative numerical effects from seven expansion reports used")
summary["appraisal_protocol_consistent_nine_domains"] = {"domains":9,"judgments":216,"yes":100,"partial":110,"no":6}
summary["domain9_status"] = "WITHHELD_FROM_MANUSCRIPT_AGGREGATE_PENDING_REAUDIT"
(OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
write("prisma_interim_counts.csv", ["level", "stage", "count", "scope"], [
    dict(level="report", stage=stage, count=count, scope="Priority/expansion reports only; not final database flow")
    for stage, count in [("retrieved",27),("assessed",27),("included",24),("excluded_demo",1),("uncertain",2)]])
print(json.dumps(summary, indent=2))
