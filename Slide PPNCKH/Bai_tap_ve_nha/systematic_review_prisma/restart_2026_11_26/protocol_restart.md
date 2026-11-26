# Restart protocol — HK261 systematic review

Version: restart-1.1-draft
Recorded at: 2026-11-26T18:21:14+07:00
Status: DRAFT_FOR_CONSISTENCY_REVIEW; not yet a completed search or eligibility assessment.
Authority: approved_plan.md, steps 02–16. This protocol is recorded after the existing source searches and before the new screening; it is not a prospectively registered protocol for the earlier searches. No external registration is claimed.

## P01 — Objective and unit

Review distributed/collaborative DNN inference in UAV swarms and multi-UAV edge systems. Describe architectures, partitioning, orchestration, evaluation and resilience with source-bounded evidence. ResNet-18, ROS 2, PX4, Gazebo and NS-3 are possible extraction values, not mandatory eligibility criteria. Do not preferentially include a paper because it supports the author's planned implementation or is published in the target journal.

A record is a bibliographic search entry; a report is a document; a study is an underlying investigation that may have several reports. Unique studies are unknown until report-family reconciliation. No fixed number of included reports or studies is set.

## P02 — Review questions

- RQ1: Which multi-UAV architectures, inference tasks, DNN families, collaboration topologies and partition granularities have been evaluated?
- RQ2: Which partitioning, assignment, placement, compute/radio-resource, trajectory and deployment decisions are optimized, with what objectives, constraints and methods?
- RQ3: Which datasets, simulators, hardware, network models, baselines and metrics support the evaluations, and under which conditions?
- RQ4: How are mobility, changing links, intermittent connectivity, UAV failure and recovery represented and evaluated?
- RQ5: What source-located evidence supports latency, energy, communication, accuracy, reliability and scalability claims; what limitations and reproducibility gaps constrain the conclusions?

RQ1 maps to E2/E3 and architecture/workload fields; RQ2 to E3/E4 and decision/optimization fields; RQ3 to E4 and evaluation fields; RQ4 to resilience/network fields; RQ5 to outcome/condition/appraisal fields. Failure recovery and model partitioning need not both be present for eligibility.

## P03 — Eligibility (all E1–E7 must be established for INCLUDE)

- E1 Primary contribution: a method/model/algorithm/architecture/system is described with substantive research content. Reviews, tutorials, editorials, patents, theses and book chapters are excluded from primary synthesis.
- E2 Multi-UAV setting: the evaluated setting explicitly contains at least two UAVs or identifies a swarm/multi-UAV/FANET architecture. A passing mention of multi-UAV future work does not establish this. If the evaluated number/setting cannot be established, mark unclear/awaiting classification rather than infer it.
- E3 Collaborative inference: DNN/CNN/VLM/LLM inference workload has execution, features, layers, requests or inference resources distributed, partitioned, assigned, migrated, fused or jointly orchestrated across the multi-UAV system or its edge/cloud hierarchy. Explicit DNN inference placement/assignment can qualify without layer splitting. A DNN used only as an optimizer, generic indivisible offloading without explicit inference, standalone perception without collaboration, and training/federated-learning-only work do not qualify.
- E4 Evaluation: the report provides experiments, prototype/emulation, simulation, trace-driven evaluation or mathematical performance analysis of the proposed inference method. Merely proposing a concept without analyzable method/evaluation is insufficient.
- E5 Date: publication from 2021-01-01 through the actual final accepted search date. The current source runs were recorded on 2026-11-26; the final cutoff is finalized at step04 if step03 requires reruns. Record date type and source. For a journal report use the publisher's first-publication/online-publication date for that version when available, retaining issue date separately; for proceedings/preprints retain the corresponding authoritative report-version date. DOI string or copyright year alone is not authoritative. Contradictory dates at a boundary remain awaiting classification pending source verification; do not guess. Do not import old date adjudications. Treat imprecise dates as intervals: a known year wholly within the eligible window can establish date eligibility; a cutoff-year date without verifiable month/day cannot establish eligibility if its possible interval crosses the cutoff. Keep such cases AWAITING_CLASSIFICATION pending authoritative date verification. Record the date of the assessed report version, not an assumed date from another version.
- E6 Language: full report in English. An English title/abstract alone does not prove full-text language. Missing language metadata is not an automatic exclusion.
- E7 Report type/completeness: only peer-reviewed journal/conference research reports with full text, substantive method and evaluation results are eligible. Preprints, theses, patents, book chapters and abstracts-only items cannot enter the primary corpus. Record peer-review/type evidence from the publisher/proceedings, not merely a database label or guessed venue. A short conference report is not excluded by page count alone: it must establish (a) a defined inference method/system with inputs, decisions or procedure and (b) reported evaluation results with identifiable conditions and metrics. A demo/poster/work-in-progress label does not prove full-paper or peer-review status; if these required facts cannot be established, keep awaiting classification rather than assume eligibility. Link versions at step10; a preprint may supply identity/version linkage but not primary synthesis evidence.

This E7 policy was selected directly by the user during step02 and recorded in step02_user_decision.md. It supersedes the historical protocol's optional preprint inclusion; it does not change the four-source discovery set or the order of the approved plan.

## P04 — Source scope and search audit

IEEE Xplore, Scopus and ACM Digital Library provide the core source files; OpenAlex is supplementary discovery with distinct coverage. Web of Science Core Collection is not searched because access is unavailable and the user removed it from this run; its result count is null, not zero. Do not rename OpenAlex as WoS.

Step03 audits the exact executed queries, fields, filters, dates, coverage and syntax using supplied run evidence. Step04 selects versions and locks filenames/hashes/counts. Preserve the actual timestamp basis, including export-file modification time where that was the recorded basis. A query string is not proof that a search ran. Reruns, if necessary within approved scope, are separately versioned and logged.

Only these four sources define this restart's discovery input. The earlier protocol's old seed calibration/citation-chaining/pilot inputs do not automatically add records here. Adding discovery sources or changing scope requires user approval; metadata verification or lawful retrieval of an already-found record is not a new discovery source. Do not claim citation chaining was performed.

ACM's recorded month-end date filter extends beyond 2026-11-26; enforce the accepted exact cutoff downstream. Broad publication-type/language exports likewise require eligibility screening. Missing metadata and source limitations remain visible.

## P05 — Record management (steps05–06)

Raw files are immutable. Each row receives a stable raw ID with source/query/file/SHA256/row locator. Normalize DOI/title/author/year fields while retaining original values. Missing values remain explicit; provenance-supported enrichment is logged separately. Every raw row must be accounted for.

Deduplicate exact normalized DOI matches subject to conflict checks; use normalized title/year/author evidence for no-DOI candidates. Conflicting identifiers and fuzzy-title pairs require evidence review, not automatic merge. Preserve the complete source list, duplicate mapping and unresolved pairs. Distinct reports/versions are linked rather than erased as if they were the same file.

No labels, extraction, appraisal or selection pool from the old46 workflow enter the restart. Existing PDFs may be reused only after their record is independently identified in the new workflow and document identity/version is verified.

## P06 — Selection and retrieval (steps07–09)

At title/abstract stage assign RETRIEVE_FULL_TEXT, EXCLUDE or UNCLEAR using only available record evidence. Exclude only when a criterion clearly fails; missing abstract, author, DOI, venue or language metadata is not itself evidence of ineligibility. UNCLEAR moves forward for full-text clarification. Do not infer methods/results from an abstract.

Log full-text retrieval attempts, date, route, version and DOI/title identity. Use lawful accessible copies or user-provided documents. A sought report that cannot be retrieved is NOT_RETRIEVED, separate from an assessed full-text exclusion. An abstract-only publication type is different from failure to retrieve an otherwise full report.

For a retrieved report, apply E1–E7 and preserve exact page/section/quote locators. Decisions are INCLUDE, EXCLUDE or AWAITING_CLASSIFICATION. For EXCLUDE store one primary reason and any secondary flags. When several clearly fail, use this reporting priority: date (E5), language (E6), secondary/non-primary (E1), incomplete/ineligible report type (E7), no evaluated multi-UAV (E2), no collaborative inference (E3), no evaluative evidence (E4). This priority organizes reasons; it must not prevent checking contradictory evidence. Unresolved facts are not treated as confirmed failures or inclusions.

Gemini.app performs an AI-assisted first pass; Codex checks acceptance and supporting sources and requests targeted corrections. These are two AI roles, not two independent human reviewers. No human screening or author adjudication is claimed unless actually recorded. Unresolved substantive decisions are referred to the author; other independent work can continue. If the author has not reviewed the final decisions, report this limitation explicitly and do not claim author approval or submission readiness.

## P07 — Reports and study families (step10)

Retain report IDs even when several reports describe one study. A merge requires evidence from both reports, such as explicit version linkage, shared experiment/cohort/dataset design with an established relationship or author statement. Common authors/title topics alone are insufficient. Unresolved families remain separate reports with uncertain independence; do not invent a final unique-study count.

## P08 — New extraction (step11)

Extract afresh from accepted full texts: identity/type/date; UAV number/role/topology; inference task/model/dataset; partition granularity and assignment; decision variables/objectives/constraints/solution method; compute and radio configuration; mobility/channel/intermittency/failure/recovery; evaluation platform, simulator/hardware/traces, baselines and workloads; latency/energy/communication/accuracy/reliability/scalability; sensitivity/variability; code/data; funding/conflicts; author-reported limitations.

For every quantitative claim retain report ID, page/table/figure, short exact support, value, units, baseline, workload and conditions. If full-text inspection establishes a field is absent, use NOT_REPORTED with an inspection locator; if extraction is not done, use NOT_YET_ASSESSED. These are not interchangeable. Figures may be described qualitatively without inventing exact plotted values. No numerical synthesis uses an unverified value.

## P09 — Appraisal (step12)

Use a domain-based systems/simulation appraisal, not an unvalidated clinical score. Domains: (1) question/system model; (2) assumptions/variables/constraints; (3) reproducible configuration; (4) baseline comparability; (5) metric-objective alignment; (6) variability/repetitions/sensitivity/convergence where applicable; (7) network/mobility realism relative to claims; (8) claim bounds; (9) code/data/traces/implementation availability; (10) limitations and funding/conflict reporting.

Judgments: YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE, NOT_YET_ASSESSED. Each has rationale and full-text locator; NOT_APPLICABLE requires a reason. NO requires observed contrary/inadequate evidence, not silence alone. Separate reporting absence from evidence of actual bias. Do not exclude by summed score; use domains to qualify synthesis. Do not describe this bespoke appraisal as a validated risk-of-bias instrument.

## P10 — Reconciliation and synthesis (steps13–14)

Reconcile raw-source records, duplicates, screened records, sought/retrieved reports, primary full-text reasons, awaiting classification, included reports and study families using their proper units. Keep a complete ID ledger; unexplained arithmetic difference must be zero. Produce the PRISMA flow and 27-item checklist with actual locations/status/limitations rather than treating every item as achieved.

Structured narrative synthesis and evidence maps answer RQ1–RQ5. Group comparable architecture/workload/evaluation conditions; every claim maps to accepted evidence. Report numerator and denominator for frequencies. No cross-study percentage or pooled advantage is inferred from incompatible baselines/conditions. There is no authorized new meta-analysis in this restart plan; any such scope expansion requires approval. Non-peer-reviewed preprints are not primary evidence under E7; version-linkage records must not contribute synthesis results. Lack of identified evidence is not proof no such research exists.

## P11 — Writing, integrity and dissemination (steps15–16)

Codex writes in Springer Nature LaTeX for SN Computer Science: Methods, Results, Discussion, Introduction, then Title/Abstract/Conclusion. Bibliography, tables, figures and all counts derive only from accepted restart evidence. Recheck DOI identity, corrections/retractions, numerical provenance and unresolved citations; build and inspect every PDF page. Disclose actual source coverage, date restrictions, AI involvement and human-review limits. Do not fabricate review findings under an expected-results label.

The course's eventual submission/evidence requirement is distinct from current authorization: no submission/email in this run. Author order/consent, HCMUT email, affiliations/IDs, contributions, funding/conflicts/data/AI declarations and exam date need factual confirmation; never invent them. Missing metadata can limit submission readiness without changing scientific eligibility.

## P12 — Audit and change control

Keep the approved16-step plan unchanged as baseline, with progress, source evidence, provider IDs, raw results and criterion-by-criterion PASS/FAIL. Codex accepts evidence only after mandatory output criteria pass; a clean transport state is not acceptance. Changes within a draft are logged, and any change to approved scope/sequence requires user approval before execution. Record timestamps with timezone and commit each phase before moving to the next. This document does not retroactively validate the old manuscript or old46 decisions.
