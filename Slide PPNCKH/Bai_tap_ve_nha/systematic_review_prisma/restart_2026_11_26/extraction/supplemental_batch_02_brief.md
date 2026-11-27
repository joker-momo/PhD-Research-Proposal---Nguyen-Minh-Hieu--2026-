# TASK
Extract the 13 P08 source fields for each of seven supplemental HK261 reports in batch 02.

# REQUIRED WORK
1. Open only the seven authorized local PDFs and P08 from restart_2026_11_26/protocol_restart.md. Check original body access for every ID with an exact physical page quote. Use the parent only with no workers. Use PyMuPDF if available, Poppler fallback, and native original-page view where needed. Report tool and access limitations. For difficult layouts use MinerU locally before Marker if available and confirm against the original.
2. Extract all 13 key groups per ID. State tested vs proposed conditions. Choose one short exact four-to-nine-word phrase within one printed line, and cite its 1-based physical page and section. Attach a second short phrase only to support an otherwise ungrounded second claim. Give examples with concrete components, without long lists or speculation.
3. Distinguish profiled simulations from hardware validation, experimental outcomes from design objectives, and source-reported limitations from review inferences. For R0077, read the manifest-pinned author accepted version for the journal DOI supplied below. Avoid suspect quantitative spans, exact values only visible in unlabelled figures, and whole-survey generalizations. No optional numerical outcome comparisons in the provider response.
4. If a field is absent, include the inspected page/section and specify the gap. If you cannot verify it, flag it explicitly by ID and key. Use body pages for substantive claims. No operational targeting or attack details.

Report manifest, with fixed title/DOI and exact path:
- R0077 | Distributed split computing using diffusive metrics for UAV swarms | DOI 10.1016/j.sysarc.2026.103804 | restart_2026_11_26/fulltext_retrieval/pdf/R0077.pdf
- R0080 | Edge-Cloud Collaborative Model Inference for Aerial Networks with Distributionally Diverse Data | DOI 10.1109/VTC2025-Fall65116.2025.11310097 | restart_2026_11_26/fulltext_retrieval/pdf/R0080.pdf
- R0090 | Aeroagrinet: Swarm-Enabled Flying Edge Framework for Real-Time Agricultural Intelligence | DOI 10.1109/ICoEIT63558.2025.11457712 | restart_2026_11_26/fulltext_retrieval/pdf/R0090.pdf
- R0092 | A DRL-Assisted Decentralized Framework for UAV Swarm Collaborative Inference | DOI 10.1109/JIOT.2026.3740035 | restart_2026_11_26/fulltext_retrieval/pdf/R0092.pdf
- R0106 | Robust Group Target Awareness Inference in Multi-UAV-Enabled ISCC Networks Based on Split Deep Reinforcement Learning | DOI 10.1109/TWC.2025.3573654 | restart_2026_11_26/fulltext_retrieval/pdf/R0106.pdf
- R0107 | Joint Semantic Compression and Resource Allocation for Multi-UAV Networks: A Knowledge-Guided Reinforcement Learning Approach | DOI 10.1109/TVT.2026.3733130 | restart_2026_11_26/fulltext_retrieval/pdf/R0107.pdf
- R0110 | RDI-LLM: A Resilient Distributed Inference Framework for LLMs in Resource-Constrained UAV Swarms | DOI 10.1109/tvt.2026.3755123 | restart_2026_11_26/fulltext_retrieval/pdf/R0110.pdf

# REQUIRED OUTPUT
Raw compact JSONL. Use one row per key, no Markdown fences or commentary. Example:
{"id":"RTEST","key":"evaluation","s":"OBSERVED","f":"Software simulation with specified source profiles.","l":[[4,"IV.A Simulation Setup","four to nine exact words"]],"g":null}
Keys: access, architecture, workload, partition_assignment, optimization, compute_radio, mobility_continuity, evaluation, baselines, outcomes, variability, code_data, funding_conflicts, limitations. Use READ or NOT_ACCESSIBLE for access; use OBSERVED, PARTIAL, NOT_REPORTED or NOT_YET_ASSESSED for the other 13. Every l item is [physical page, section or named table/figure, exact quote]. Put null as quote only to document inspected absence. Use g for missing facets or access. Keep f at or below 25 words. Quotes must not cross columns, pages or printed lines. Avoid ellipses, ligatures, internal quotes, formula symbols and publisher sidebars. Report tools, unresolved ID/key and reason, and that no workers were used in one summary object. Final standalone marker P08_SUPPLEMENT_BATCH_02_COMPLETE.

# ACCEPTANCE CRITERIA
1. Exactly 7 report IDs and 98 unique keys (7 access plus 91 field keys) or a specific documented shortfall. Zero unexpected keys, invalid state or duplicate. Source identities are supplied in this brief and project manifest.
2. Every adopted claim has a physically matching original body quote with a precise page and section, or the checked absence is documented. Zero unsupported facts or quantitative outcomes.
3. One valid summary and final marker. No worker delegation, hidden shortfall, file mutation or original PDF upload. Codex independently verifies all accepted source uses.

# BOUNDARIES
Only named originals and P08 protocol. No access to other folders, web, shell commands, uploads, edits, re-screening, appraisal, manuscript prose or prior corpus. Keep all work in one read-only Task.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
