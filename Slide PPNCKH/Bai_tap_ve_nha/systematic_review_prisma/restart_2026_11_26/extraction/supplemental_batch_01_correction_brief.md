# TASK
Repair only the 47 enumerated original-PDF extraction keys in supplemental P08 batch 01 from native Task 15cbc890-5eb8-41d6-ad0a-52686af3dd74.

# REQUIRED WORK
1. Open only the seven allowed originals in `restart_2026_11_26/fulltext_retrieval/pdf/` from the attached HK261 project. In the parent Task, confirm R0058 has direct body-page access with one exact phrase from §6.1. Use physical 1-based PDF pages, not printed journal numbers. Use the available local PDF tool. If the original is unavailable, specify the failed ID, path, tool and reason.
2. For each listed key give the smallest defensible qualitative finding and one exact 4–9 word continuous phrase on the cited original page. Use a second phrase only if needed for a distinct facet. Avoid mathematical symbols, ligatures, punctuation, internal quotation marks, ellipses, rewritten sentences, displayed equations and cross-column joins in the excerpt. Inspect the actual source. Prefer limitations explicitly stated by authors, and record a concrete gap separately. For NOT_REPORTED include inspected body or end-matter location and null excerpt. Do not invent anything to fill the schema.
3. R0014 distinguishes the airborne-computer testbed from the UAV evaluations, and the source conditions of any fault test. R0036 distinguishes the simulation fed by ground-view video and variability of random comparator only from full-system variance. R0038 distinguishes deliberate hardware disconnection, pause and checkpoint restore from mobility or field testing, and qualitative stage outcomes from internally inconsistent aggregates. R0043 reports simulated performance and names visual workloads. R0058 avoid guessing default server count from inconsistent prose. R0064 distinguish fixed seeds from independent reruns and cover the variability that is actually reported. R0075 distinguish model profiling from wireless evaluation and main results from specific sensitivity experiments.
4. Aim for at most 22 words of finding text per field. No optional quantitative comparison rows. Report actual tool and access limitations with the unresolved keys; no workers.

Allowed exact keys:
- R0014: compute_radio, evaluation, mobility_continuity, optimization, outcomes
- R0036: architecture, code_data, compute_radio, limitations, mobility_continuity, outcomes, variability, workload
- R0038: baselines, limitations, mobility_continuity, outcomes, variability
- R0043: compute_radio, evaluation, optimization, outcomes, partition_assignment, workload
- R0058: access, architecture, baselines, code_data, compute_radio, mobility_continuity, optimization, outcomes, partition_assignment, variability
- R0064: architecture, compute_radio, mobility_continuity, optimization, outcomes, variability, workload
- R0075: architecture, optimization, outcomes, partition_assignment, variability, workload

# REQUIRED OUTPUT
Compact raw JSONL (no Markdown fences), one object per named key, all double quotes escaped if present. Exact schema example:
{"id":"RTEST","key":"evaluation","s":"OBSERVED","f":"Software simulations were run. The original page documents the setup.","l":[[4,"IV.A Simulation Setup","short exact source phrase"]],"g":null}
Access row example (only R0058): {"id":"R0058","key":"access","s":"READ","f":"Original body page directly opened.","l":[[19,"6.1. Simulation settings","short exact source phrase"]],"g":null}
Use OBSERVED, PARTIAL, NOT_REPORTED, NOT_YET_ASSESSED for field status. For access READ or NOT_ACCESSIBLE. l gives physical page, section, and quote or null for inspected absence; g is the gap for PARTIAL, NOT_REPORTED, NOT_YET_ASSESSED or NOT_ACCESSIBLE. Path is determined by ID in the specified directory. Finish with one summary object containing keys_returned (integer), unresolved (array of ID/key/reason), tools and workers_used, then standalone P08_SUPPLEMENT_BATCH_01_CORRECTION_COMPLETE.

# ACCEPTANCE CRITERIA
- Exactly 47 unique valid keys, comprising 46 field keys and one access key, or explicit ID-key shortfalls. No additional report, duplicate, unparseable line or unsupported number.
- Every locator has the original physical page, exact named section and exact matching phrase, or documents examined absence. Wrong page, skipped access or unsupported scope fails.
- No hidden gaps and no changes to input files. Original evidence is read only. Codex checks all returned fields before acceptance.

# BOUNDARIES
Use only original PDFs named here. Exclude abstract-only and metadata-only evidence for substantive findings. No manuscript, re-screening, appraisal, web search, uploads, file edits, operational or exploit details, or previous corpus.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
