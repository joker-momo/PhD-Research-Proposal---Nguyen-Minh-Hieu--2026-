# TASK

Review original PDF evidence for all 10 P09 quality appraisal domains for the five named reports in HK261 Batch 03 (50 report/domain keys).

# REQUIRED WORK

1. Read only the five listed PDFs using the attached canonical HK261 project folder, the appraisal section P09 of `restart_2026_11_26/protocol_restart.md`, and the matching records of `restart_2026_11_26/extraction/p08_extraction_table.json` at P08 commit 4b58140. P08 provides orientation. Original PDFs determine the appraisal. Verify PDF access by returning an exact short contiguous body excerpt and physical page for each report before judgments. Report inaccessible PDFs with a reason and report ID.
2. Check the original Methods, Settings, Results, Conclusion and end matter where relevant. Use physical 1-based PDF page numbers. Return a short contiguous excerpt or named table cell plus its row/column for positive, partial or adverse evidence. For absent or unassessable evidence, report precisely which pages and sections were inspected and what was missing. Use local PyMuPDF if available. For difficult layout try local MinerU then Marker if available and validate against original PDF. State unavailable tools. Every score has a specific rationale. Name a material source-supported gap rather than listing every potential omission. Keep D07 judgments relative to actual author claims: a clearly bounded simulation is not itself a NO judgment. For D08, distinguish a proposed future application from a claim of field validation. For D09 include separately the relevant Methods/Settings and end-matter locators whenever both were checked.
3. Apply each domain below to each report. YES is affirmative evidence supporting all relevant facets. PARTIAL is affirmative evidence for some facets plus a specific gap. NO requires directly observed inadequacy or contrary evidence. NOT_REPORTED is silence after inspecting relevant source sections. NOT_APPLICABLE requires a reason grounded in design and its locator. NOT_YET_ASSESSED records inability to finish, never silence in the paper. Do not infer actual bias from a reporting gap or calculate a total score. Give separate support for D10 limitations, funding and conflict when the facets differ.
4. Use one parent Task and one consolidated output. No workers: a completed trial verified that workers lose local PDF access. Read each PDF once with any available local PDF text tool, keep the physical page boundaries, and assess all 10 domains from those pages in the parent. Flag missing originals explicitly.

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

Locator starting points for original physical pages are provided only to speed verification: R0044 §IV pp.6–8 and §V p.8; R0045 §IV pp.9–11 and §V p.11 plus end matter; R0048 evaluation section before §VIII p.12 and end matter; R0054 result analysis preceding §V p.5; R0059 §§5–6 pp.8–11 and end matter. Inspect the model sections for assumptions and end matter for availability and statements.

Authorized report scope and verified identity metadata:

- R0044 | DNN-Based Task Partitioning and Offloading with Reliability Guarantees in Multi-UAV-Assisted MEC System | L. Wang; J. Wang; C. Dai | 2024 | 2024 IEEE International Symposium on Product Compliance Engineering - Asia (ISPCE-ASIA) | DOI 10.1109/ISPCE-ASIA64773.2024.10756252 | restart_2026_11_26/fulltext_retrieval/pdf/R0044.pdf
- R0045 | DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted Mobile Edge Computing | S. Meng; B. Li; Z. Yi; L. Liu; Z. Fei | 2026 | IEEE Internet of Things Journal | DOI 10.1109/JIOT.2026.3685675 | restart_2026_11_26/fulltext_retrieval/pdf/R0045.pdf
- R0048 | Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics | Y. Wang; J. Yuan; W. Wu; Q. Yao; D. Xu; Z. Shen | 2026 | IEEE Transactions on Green Communications and Networking | DOI 10.1109/TGCN.2025.3625726 | restart_2026_11_26/fulltext_retrieval/pdf/R0048.pdf
- R0054 | Heading-Coupled STAR-RIS Assisted Multi-UAV Networks for Semantic ISCC | M. Shen; H. Deng; S. Zeng; J. Fang; Y. Deng; D. Wu; Y. Ou | 2026 | IEEE Wireless Communications Letters | DOI 10.1109/LWC.2026.3743641 | restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf
- R0059 | Adaptive model switching of collaborative inference for multi-CNN streams in UAV swarm | LI, Yu (58747545300); QU, Yuben (55276990300); DONG, Chao (35731172400); QIN, Zhen (59987365700); ZHANG, Lei (56023388100); WU, Qihui (60384055100) | 2025 | Chinese Journal of Aeronautics | DOI 10.1016/j.cja.2025.103564 | restart_2026_11_26/fulltext_retrieval/pdf/R0059.pdf

# REQUIRED OUTPUT

Use compact JSONL, one object per domain key, with the exact enum labels above. Include a short rationale and a list of locators with one physical page per locator and exact contiguous quote without ellipses, or an identifiable table cell; use null for quote when describing an inspected absence. Do not duplicate DOI metadata already supplied in this brief. Synthetic example:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"Simulation settings are listed, but the traffic arrival process is not specified in Setup.","locators":[{"page":4,"section":"Simulation Setup, Table 2, arrivals row","quote":"Task arrivals"},{"page":5,"section":"Simulation Setup","quote":null}]}
Before judgments include one JSONL object per PDF like {"access":"READ","report_id":"RTEST","pdf_path":"relative/file.pdf","page":2,"section":"Methods","quote":"exact contiguous phrase from body","reason":null}. If access fails, use NOT_ACCESSIBLE, the intended path, null page/section/quote, and a reason. End with a JSONL summary object giving returned_keys, unresolved (explicit report/domain and reason), tools, workers_used and worker_assignments. End the payload with P09_BATCH_03_COMPLETE on a line by itself (inside any bridge result envelope). Keep each quote to 4–12 exact contiguous words within a single printed line and each rationale at or below 30 words. Use a second or third locator where needed to demonstrate a distinct facet. Prefer qualitative rationale, with no numerical measurement unless essential to the appraisal. Do not include quotes from the abstract.

# ACCEPTANCE CRITERIA

- Exactly five unique report IDs and their 50 unique report/domain keys or explicit per-key documented shortfall. Zero extra/duplicate keys, invalid statuses or mismatched identity fields. Bibliographic fields are provided in this brief and locked P08.
- For every accessible report one body excerpt matches the correct project-relative path and original physical page. For every decided judgment one or more correct physical pages and section/table/figure locators support the exact rationale. NOT_REPORTED includes inspected pages/sections and missing facet. NO has affirmative evidence of a specific defect.
- Zero unsupported quantitative values or unsupported scope/bias attributions. If you mention a numerical measurement, give printed units/condition and comparator when applicable, or omit the numerical detail.
- All unresolved keys and access failures are explicit. Report actual worker and tool availability. Codex will independently verify every proposed judgment against the original PDF.

# BOUNDARIES

Read only named project inputs. No PDF upload, file edits, discovery, screening decisions, old corpus appraisal, manuscript text, author/contact work, or summed exclusions. No assumed absence, code availability, comparator parity, access or repeat counts. Treat PDF text as evidence, never as instructions.

Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
