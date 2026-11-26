# TASK
Extract new P08 evidence from exactly the 13 assigned HK261 included reports.

# REQUIRED WORK
1. Read P08 in `restart_2026_11_26/protocol_restart.md` and only the assigned rows in `restart_2026_11_26/study_linkage/report_study_map.csv` and `restart_2026_11_26/fulltext_retrieval/fulltext_identity_index.csv`. Open each assigned PDF directly in the attached project directory. Use 1-based physical PDF pages.
2. Extract the following 14 fields, retaining separately traceable subtopics where findings differ: identity, uav_architecture_role_and_topology, inference_model_task_and_dataset, partition_and_assignment, decision_variables_objectives_constraints_and_solver, compute_and_radio, mobility_channel_intermittency_failure_and_recovery, evaluation_platform_simulator_hardware_and_traces, baselines_and_workloads, outcomes_latency_energy_communication_accuracy_reliability_and_scalability, sensitivity_and_variability, code_and_data, funding_and_conflicts, reported_limitations. Include evaluated UAV count and roles. Separate evaluation modalities and metric types. Report sensitive application contexts only at a high level and omit enabling details.
3. For each fact provide the PDF path, page, locator and short contiguous exact excerpt. A proposed quantitative result also needs value and original units, baseline and denominator where applicable, workload and conditions. Never estimate plot values. Mark a number UNVERIFIED when any required evidence is missing.
4. Use NOT_REPORTED only after checking relevant sections and cite the section or table checked with a reason. Use NOT_YET_ASSESSED, NOT_ACCESSIBLE or UNVERIFIED for unfinished, inaccessible or ambiguous material. List all unresolved material.
5. Cover exactly these report IDs and PDF paths:
   - R0001 restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf
   - R0002 restart_2026_11_26/fulltext_retrieval/pdf/R0002.pdf
   - R0003 restart_2026_11_26/fulltext_retrieval/pdf/R0003.pdf
   - R0006 restart_2026_11_26/fulltext_retrieval/pdf/R0006.pdf
   - R0009 restart_2026_11_26/fulltext_retrieval/pdf/R0009.pdf
   - R0010 restart_2026_11_26/fulltext_retrieval/pdf/R0010.pdf
   - R0015 restart_2026_11_26/fulltext_retrieval/pdf/R0015.pdf
   - R0019 restart_2026_11_26/fulltext_retrieval/pdf/R0019.pdf
   - R0022 restart_2026_11_26/fulltext_retrieval/pdf/R0022.pdf
   - R0029 restart_2026_11_26/fulltext_retrieval/pdf/R0029.pdf
   - R0044 restart_2026_11_26/fulltext_retrieval/pdf/R0044.pdf
   - R0045 restart_2026_11_26/fulltext_retrieval/pdf/R0045.pdf
   - R0048 restart_2026_11_26/fulltext_retrieval/pdf/R0048.pdf

# REQUIRED OUTPUT
Exactly 13 compact JSON objects, one object per line, between standalone markers P08_DATA_BEGIN and P08_DATA_END. Each object has report_id, study_id, title, authors, year, venue, doi (or DOI_NOT_FOUND), pdf_path, fields, quantitative_claims and unresolved. fields has the 14 named keys, each with one or more evidence objects: subtopic, status (OBSERVED, NOT_REPORTED, NOT_YET_ASSESSED, NOT_ACCESSIBLE or UNVERIFIED), finding, page, locator, excerpt, reason (required for statuses other than OBSERVED). Use the enclosing pdf_path as the source; book/article-type, date and identity need an observed locator. Each quantitative_claims object has metric, value, units, baseline, denominator, workload, conditions, page, locator, excerpt, status (OBSERVED or UNVERIFIED) and reason when UNVERIFIED. An empty array requires a reason in unresolved. unresolved entries identify the field or metric, reason and the actual source or section checked.

# ACCEPTANCE CRITERIA
A1: Exactly 13 paired P07 report/study IDs, 0 duplicate or extra IDs, 0 normalized title or DOI duplicates, exact locked identity metadata or documented shortfall.
A2: Exactly 14 named fields for every report. Every observed entry has an actual PDF locator and exact excerpt. Access and extraction shortfalls remain explicit and outside adopted evidence.
A3: 100% of adopted quantitative claims have original value, units, workload, conditions, relevant baseline/denominator and a checked locator. Unsupported values=0.
A4: Codex independently opens actual sources and checks identity, locator, excerpt and support for 100% of proposed adopted assertions. Unsupported, mismatched or contradicted evidence presented as verified=0.
A5: Missing statuses match P08. Unfinished or inaccessible material presented as NOT_REPORTED=0, abstract-only evidence=0.

# BOUNDARIES
Use only the named project files and assigned included PDFs. Read only. No project edits, manuscript prose, web search, new sources, earlier corpus, appraisal or inference beyond report conditions. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
