# TASK
Correct the p. 5 geometry excerpt repeated in R0082 EVALUATION and FAMILY, following task f6696609-30c3-41a0-8d7e-808373512953.

# REQUIRED WORK
1. Reopen only restart_2026_11_26/fulltext_retrieval/pdf/R0082.pdf, physical page 5, §IV. Check the simulation geometry paragraph of the named PDF.
2. Return that paragraph's exact area dimensions with the Unicode multiplication sign × if quoting it. An alternative short contiguous exact excerpt beginning after the area dimensions and covering the cell count and dimensions is acceptable. Return two keys, EVALUATION and FAMILY. Their anchors can be identical. No other research is required.

# REQUIRED OUTPUT
Two JSONL objects with key (EVALUATION or FAMILY), record_id, path, physical_page, section, excerpt, status (VERIFIED, UNVERIFIED or NOT_ACCESSIBLE), and reason if not verified. Final footer with complete, unresolved_keys and workers_used.

# ACCEPTANCE CRITERIA
One source PDF, two distinct keys and zero extra evidence keys. Both locators must match physical p. 5 and contain a short exact contiguous excerpt, or report the inability explicitly. Zero inferred numbers or study-independence conclusions.

# BOUNDARIES
Read-only. The named original PDF is the only source. No new searches, uploads, substitution, drafting or editing. Return only the focused locator repair.
Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
