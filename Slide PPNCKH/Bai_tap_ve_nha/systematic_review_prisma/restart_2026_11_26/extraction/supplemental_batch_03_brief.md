# TASK
Extract the 13 P08 source fields for each of seven supplemental HK261 reports in batch 03.

# REQUIRED WORK
1. Open only the seven authorized local PDFs and P08 from restart_2026_11_26/protocol_restart.md. For each access row use an exact Methods, Experimental Setup, Results or equivalent quote on physical page 2 or later. Zero title, header, footer or abstract access quotes. Use the parent only with no workers. Use PyMuPDF if available, Poppler fallback, and native original-page view where needed. Report tool and access limitations. For difficult layouts use MinerU locally before Marker if available and confirm against the original.
2. Extract all 13 key groups per ID. State tested vs proposed conditions. Choose one short exact four-to-nine-word phrase within one printed line, and cite its 1-based physical page and section. Attach a second short phrase only to support an otherwise ungrounded second claim. Give examples with concrete components, without long lists or speculation.
3. Distinguish profiled simulations from hardware validation, experimental outcomes from design objectives, and source-reported limitations from review inferences. Use the pinned PDF for each ID. Report only the evidence established by that version. R0113 has DOI_NOT_FOUND; R0292 differs slightly in title wording on the source PDF. Keep manifest IDs pinned. Avoid suspect quantitative spans, exact values only visible in unlabelled figures, and whole-survey generalizations. No numerical outcomes, p-values or unverified URLs in the provider response. In code_data, if release is explicit, give the exact plain-text route printed by the authors, or a precise locator when the route cannot be verified.
4. If a field is absent, include the inspected page/section and specify the gap. If you cannot verify it, flag it explicitly by ID and key. Use body pages for substantive claims. No operational targeting or attack details.

Report manifest, with fixed title/DOI and exact path:
- R0113 | A Neuromorphic Spiking Neural Network-Based Continual Learning Framework for Energy-Efficient Edge Intelligence in Autonomous UAV Swarm Navigation | DOI_NOT_FOUND | restart_2026_11_26/fulltext_retrieval/pdf/R0113.pdf
- R0118 | NetMoE: Joint Trajectory Planning and Distributed Mixture-of-Experts Inference for UAV Swarms | 10.1109/jiot.2026.3755315 | restart_2026_11_26/fulltext_retrieval/pdf/R0118.pdf
- R0125 | UAV Extreme Edge Computing for Real Time AI Inference: A Distributed Processing Approach | 10.1109/sm69703.2026.11614110 | restart_2026_11_26/fulltext_retrieval/pdf/R0125.pdf
- R0137 | MARL-based Reliability-aware Video Analytics in Multi-UAV-Assisted MEC Systems | 10.1109/tcsvt.2026.3745821 | restart_2026_11_26/fulltext_retrieval/pdf/R0137.pdf
- R0145 | LLM-based UAV Path Planning for Autonomous and Adaptive Industry Systems | 10.1145/3774655 | restart_2026_11_26/fulltext_retrieval/pdf/R0145.pdf
- R0223 | Outdoor Multi-UAV Collaborative Task Planning System Based on Multi-Agent and Improved PPO Algorithm | 10.1145/3760269.3760299 | restart_2026_11_26/fulltext_retrieval/pdf/R0223.pdf
- R0292 | Continuous Marine Monitoring via Autonomous UAV Handoff | 10.1145/3711875.3737661 | restart_2026_11_26/fulltext_retrieval/pdf/R0292.pdf

# REQUIRED OUTPUT
Raw compact JSONL. Use one row per key, no Markdown fences or commentary. Example:
{"id":"RTEST","key":"evaluation","s":"OBSERVED","f":"Software simulation with specified source profiles.","l":[[4,"IV.A Simulation Setup","four to nine exact words"]],"g":null}
Keys: access, architecture, workload, partition_assignment, optimization, compute_radio, mobility_continuity, evaluation, baselines, outcomes, variability, code_data, funding_conflicts, limitations. Use READ or NOT_ACCESSIBLE for access; use OBSERVED, PARTIAL, NOT_REPORTED or NOT_YET_ASSESSED for the other 13. Every l item is [physical page, section or named table/figure, exact quote]. Put null as quote only to document inspected absence. A PARTIAL field also needs at least one positive body quote. Use g for missing facets or access. Keep f at or below 25 words. Quotes must not cross columns, pages or printed lines. Avoid ellipses, ligatures, internal quotes, formula symbols and publisher sidebars. Report tools, unresolved ID/key and reason, and that no workers were used in one summary object with id SUMMARY, report_count, key_count, no_workers_used, tools_used and unresolved. Final standalone marker P08_SUPPLEMENT_BATCH_03_COMPLETE.

# ACCEPTANCE CRITERIA
1. Exactly 7 report IDs and 98 unique keys (7 access plus 91 field keys) or a specific documented shortfall. Zero unexpected keys, invalid state or duplicate. Source identities are supplied in this brief and project manifest.
2. Every adopted claim has a physically matching original body quote with a precise page and section, or the checked absence is documented. Zero unsupported facts or quantitative outcomes.
3. Every access row cites a body section on physical page 2 or later. One valid summary and final marker. No worker delegation, hidden shortfall, file mutation or original PDF upload. Codex independently verifies all accepted source uses.

# BOUNDARIES
Only named originals and P08 protocol. No access to other folders, web, shell commands, uploads, edits, re-screening, appraisal, manuscript prose or prior corpus. Keep all work in one read-only Task.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
