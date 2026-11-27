# TASK
Repair five specific P09 keys in two original PDFs following correction Task 15ee76c5-479f-4f66-945b-a7fe6d1b99bf.

# REQUIRED WORK
1. Use only P09 of restart_2026_11_26/protocol_restart.md and the two named originals. Parent only. Use local PyMuPDF or Poppler if available and local MinerU before Marker for difficult layout if available. Check actual physical pages, report tools and access issues.
2. Verify the following pointers against the originals and return exactly these keys once. Keep each rationale at or below 25 words and short exact one-line quotes (four to nine words). Finish with no unresolved keys unless evidence is unavailable.
- R0058/D03: Use physical p.19 §6.1, exact plain body phrase integrates ground edge servers with aerial UAV nodes. Review the original layout of the printed server range and default. The default lies outside the range as printed. Do not alter either value.
- R0058/D07: Use physical p.19 §6.1 and p.21 §6.3. For p.21 use the exact clean words illustrates the distribution of task success rates. Contrast model assumptions with claimed scope without relying on the ligature in different.
- R0058/D09: Use precisely inference tasks are based on the CIFAR-10 on p.19 §6.1 if documenting the external input, with separate inspected-absence locator for the study artifacts in setup and conclusion/end matter.
- R0064/D05: Use physical p.8 §5.1 and p.12 §6 for the accuracy function and absence of empirical video verification. On physical p.9 §5.2.2 exact words are Fig. 7 shows the average inference delay. No numeric results needed.
- R0064/D09: Use NOT_REPORTED for author code when only a no-data-used statement is present, consistent with baseline R0083 and R0095. Locate p.12 Data availability as context and a null-quote Methods/end matter locator for the missing implementation route. Exact quote: No data was used for the research.

Authorized report metadata and files:
- R0058 | Efficient AI Inference Offloading for UAVs via Distributed Auctions in Dynamic Edge Environments | 10.1142/S0218126626440020 | Yi Yang; Hao Liu; Peng Wang; Xiuping Li; Wen Sun | 2025 | Journal of Circuits, Systems and Computers | restart_2026_11_26/fulltext_retrieval/pdf/R0058.pdf
- R0064 | Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach | 10.1016/j.comnet.2025.111540 | Xiaokun Fan; Yali Chen; Min Liu; Yuchen Zhu; Zhongcheng Li | 2025 | Computer Networks | restart_2026_11_26/fulltext_retrieval/pdf/R0064.pdf

# REQUIRED OUTPUT
JSONL, exact schema: {"id":"RTEST","key":"D05","s":"PARTIAL","f":"Delay measures the modeled objective.","l":[[4,"Evaluation","four exact source words"],[5,"Limitations",null]],"g":"End-to-end sensing is not measured."}
Valid states YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE, NOT_YET_ASSESSED. For substantive anchors use precise pages, section names and exact excerpts. Use null quote for inspected absence and g for the specific gap. One summary with id SUMMARY, report_count 2, key_count 5, no_workers_used true, tools_used and unresolved. Finish with P09_SUPPLEMENT_BATCH_01_LOCATORS_COMPLETE on a standalone line.

# ACCEPTANCE CRITERIA
Five unique listed keys across two matching report identities and one summary plus end marker. No duplicates, extra records, invalid JSON or unsupported facts. Every decided row matches the original physical page and section. Do not invent missing values. No quantitative outcomes.

# BOUNDARIES
Parent read-only. No web, shell, workers, uploads, new sources, manuscript text or project changes.

Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
