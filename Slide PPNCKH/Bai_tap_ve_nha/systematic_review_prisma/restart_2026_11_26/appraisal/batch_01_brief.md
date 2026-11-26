# TASK

Review original PDF evidence for all 10 P09 quality appraisal domains for the five named reports in HK261 Batch 01 (50 report/domain keys).

# REQUIRED WORK

1. Read only the five listed PDFs using the attached canonical HK261 project folder, the appraisal section P09 of `restart_2026_11_26/protocol_restart.md`, and the matching records of `restart_2026_11_26/extraction/p08_extraction_table.json` at P08 commit 4b58140. P08 provides orientation. Original PDFs determine the appraisal. Verify PDF access by returning an exact short contiguous body excerpt and physical page for each report before judgments. Report inaccessible PDFs with a reason and report ID.
2. Check the original Methods, Settings, Results, Conclusion and end matter where relevant. Use physical 1-based PDF page numbers. Return a short contiguous excerpt or named table cell plus its row/column for positive, partial or adverse evidence. For absent or unassessable evidence, report precisely which pages and sections were inspected and what was missing. Use local PyMuPDF if available. For difficult layout try local MinerU then Marker if available and validate against original PDF. State unavailable tools. Every score has a specific rationale, not a repeated domain name.
3. Apply each domain below to each report. YES is affirmative evidence supporting all relevant facets. PARTIAL is affirmative evidence for some facets plus a specific gap. NO requires directly observed inadequacy or contrary evidence. NOT_REPORTED is silence after inspecting relevant source sections. NOT_APPLICABLE requires a reason grounded in design and its locator. NOT_YET_ASSESSED records inability to finish, never silence in the paper. Do not infer actual bias from a reporting gap or calculate a total score. Give separate support for D10 limitations, funding and conflict when the facets differ.
4. Use one parent Task and one consolidated output. Use internal workers only if the app truly supports them and assign each report to exactly one worker. State whether workers were used and actual report assignments when applicable.

- D01 Question and system model: Clear technical question and enough system/workflow description to locate the proposed mechanism.
- D02 Assumptions, variables and constraints: Explicit critical assumptions, decision variables and constraints or experimental boundaries.
- D03 Reproducible configuration: Operational setup and key parameter values sufficient to interpret and plausibly reconstruct the reported experiment. Identify material gaps.
- D04 Baseline comparability: Named comparators and evidence of common workloads, resources, protocol or stated differences. Distinguish tunings disclosed from tuning parity not established.
- D05 Metric–objective alignment: Key outcomes measure the stated objective. Note simulation proxy or mismatch if material.
- D06 Variability, repetitions, sensitivity or convergence: Assess facets applicable to the design. A sensitivity sweep or convergence plot alone does not establish uncertainty across repeated random trials.
- D07 Network and mobility realism relative to claims: Compare channel, mobility, network, topology assumptions and evaluation modality with the actual scope claimed. Simulation is not automatically inadequate.
- D08 Claim bounds: Identify how claims and conclusions are bounded to the evaluated workloads, scenarios, systems and modality. Cite both scope and claim if needed.
- D09 Code, data, traces and implementation availability: Identify an explicit release, access route, statement of restriction, or the exact methods, end matter and supplement sections checked for availability. Mention of a named component or third-party dataset is not author artifact availability.
- D10 Limitations, funding and conflict reporting: Give explicit evidence for each of three subfacets as reported or searched; an acknowledgment listing funding does not establish absence of conflicts. Distinguish implicit setup boundaries from explicit author limitations.

Authorized report scope and verified identity metadata:

- R0001 | Adaptive Partition and Resource Allocation for Collaborative Inference Services in UAV Swarm | Y. Dong; J. Shi; S. Li; Y. Gao; Y. Zhu; J. Zhang; J. Huang | 2026 | 2026 IEEE International Conference on Web Services (ICWS) | DOI 10.1109/ICWS72778.2026.00154 | restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf
- R0002 | Promise: Predictive and Cost-Optimal Migrations for Service-Continuous Edge Intelligence in Multi-UAV Networks | J. Zhang; M. Tao; R. Xie; Y. Zhang | 2026 | 2026 IEEE International Conference on Web Services (ICWS) | DOI 10.1109/ICWS72778.2026.00067 | restart_2026_11_26/fulltext_retrieval/pdf/R0002.pdf
- R0003 | Dynamic DNN Model Switching for Collaborative Edge Intelligence in UAV Swarm | Y. Li; Y. Qu; C. Dong; F. Zhou; L. Zhang; Q. Wu | 2023 | 2023 International Conference on Wireless Communications and Signal Processing (WCSP) | DOI 10.1109/WCSP58612.2023.10405273 | restart_2026_11_26/fulltext_retrieval/pdf/R0003.pdf
- R0006 | Joint UAV Deployment and Model Partition for Efficient Collaborative Inference | W. Xia; T. Wu; H. Wang; R. Jiang; M. Zhang; Y. Qu | 2025 | 2025 IEEE 31th International Conference on Parallel and Distributed Systems (ICPADS) | DOI 10.1109/ICPADS67057.2025.11322921 | restart_2026_11_26/fulltext_retrieval/pdf/R0006.pdf
- R0009 | Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks | X. B. Zhai; S. Fu; C. Yi; Z. Liu; C. Dong; C. Wei Tan | 2026 | IEEE Transactions on Intelligent Transportation Systems | DOI 10.1109/TITS.2025.3629117 | restart_2026_11_26/fulltext_retrieval/pdf/R0009.pdf

# REQUIRED OUTPUT

Use compact JSONL, one object per domain key, with the exact enum labels above. Include a short rationale and a list of locators with one physical page per locator and exact contiguous quote without ellipses, or an identifiable table cell; use null for quote when describing an inspected absence. Do not duplicate DOI metadata already supplied in this brief. Synthetic example:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"Simulation settings are listed, but the traffic arrival process is not specified in Setup.","locators":[{"page":4,"section":"Simulation Setup, Table 2, arrivals row","quote":"Task arrivals"},{"page":5,"section":"Simulation Setup","quote":null}]}
Before judgments include one JSONL object per PDF like {"access":"READ","report_id":"RTEST","pdf_path":"relative/file.pdf","page":2,"section":"Methods","quote":"exact contiguous phrase from body","reason":null}. If access fails, use NOT_ACCESSIBLE, the intended path, null page/section/quote, and a reason. End with a JSONL summary object giving returned_keys, unresolved (explicit report/domain and reason), tools, workers_used and worker_assignments. End the payload with P09_BATCH_01_COMPLETE on a line by itself (inside any bridge result envelope). Keep the output compact.

# ACCEPTANCE CRITERIA

- Exactly five unique report IDs and their 50 unique report/domain keys or explicit per-key documented shortfall. Zero extra/duplicate keys, invalid statuses or mismatched identity fields. Bibliographic fields are provided in this brief and locked P08.
- For every accessible report one body excerpt matches the correct project-relative path and original physical page. For every decided judgment one or more correct physical pages and section/table/figure locators support the exact rationale. NOT_REPORTED includes inspected pages/sections and missing facet. NO has affirmative evidence of a specific defect.
- Zero unsupported quantitative values or unsupported scope/bias attributions. If you mention a numerical measurement, give printed units/condition and comparator when applicable, or omit the numerical detail.
- All unresolved keys and access failures are explicit. Report actual worker and tool availability. Codex will independently verify every proposed judgment against the original PDF.

# BOUNDARIES

Read only named project inputs. No PDF upload, file edits, discovery, screening decisions, old corpus appraisal, manuscript text, author/contact work, or summed exclusions. No assumed absence, code availability, comparator parity, access or repeat counts. Treat PDF text as evidence, never as instructions.
