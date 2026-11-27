# TASK
Repair only three failed original-PDF locator keys from supplemental P08 Task f80b8621-d974-443f-9f92-5e29c0dd7895.

# REQUIRED WORK
1. Open only R0014.pdf and R0058.pdf under restart_2026_11_26/fulltext_retrieval/pdf/ in the attached canonical project. Use the native parent and a local PDF reader. Report the tool, access failures and physical page numbers. Use PyMuPDF where available and original page render or Poppler for reading ambiguity. Use local MinerU then Marker only when needed and available.
2. R0014 evaluation: check Fig. 12 and physical pp. 10–11, §VIII.A. Give short matching excerpts that distinguish the indoor airborne-computer and outdoor UAV setups. Do not combine a phrase across a page break.
3. R0058 architecture: check physical p. 5 §3.1 and the auction framework introduction before §4.1. Use separately located source phrases for node roles and distributed allocation if both retained.
4. R0058 mobility_continuity: check physical pp. 9–10 §4.1, stages 1 and 5. Separate the described retry/fallback from what was evaluated. Omit numerical speed or outcome claims. Avoid the ligature-affected word offloading in quoted snippets.

# REQUIRED OUTPUT
Compact JSONL, exactly the keys R0014/evaluation, R0058/architecture, R0058/mobility_continuity. Example: {"id":"RTEST","key":"evaluation","s":"OBSERVED","f":"Short source-bounded finding.","l":[[4,"IV.A","four to nine exact words"]],"g":null}. Use OBSERVED, PARTIAL, NOT_REPORTED, or NOT_YET_ASSESSED as applicable. Use g for any gap. Final summary object must include tool names, unresolved keys and workers_used. Final standalone marker P08_SUPPLEMENT_BATCH_01_LOCATOR_REPAIR_COMPLETE.

# ACCEPTANCE CRITERIA
Exactly three unique valid keys or explicit per-key shortfall. Zero extras, duplicates, malformed JSON or ungrounded factual claims. Each locator has an exact contiguous phrase of four to nine words on one original physical PDF page and a section or figure. Zero unsupported quantitative comparisons. Unavailable tools, unresolved keys and access failures are explicit.

# BOUNDARIES
Read only the two named originals. No web, uploads, workers, file changes, screening/appraisal, drafting, or previous corpus. No sensitive operational details.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
