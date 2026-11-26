# TASK

Correct exactly three P09 Batch 03 judgments from Gemini.app task 75bd8baa-78fd-40b3-8d2a-bfe7fe53bfb3 (context c419c8a0-fa1a-4461-918d-4e5085313fa0).

# REQUIRED WORK

1. Use the native parent Task directly, without workers. Inspect R0048.pdf, R0054.pdf and R0059.pdf in the attached project's `restart_2026_11_26/fulltext_retrieval/pdf/` and P09 in `restart_2026_11_26/protocol_restart.md`. Original PDF access was previously verified. Report new access or parser limits. Prefer in-app original PDF viewing or local PyMuPDF, then local MinerU and Marker only if layout requires them and they are available. Never upload the PDFs.
2. R0048/D05: repair the original p.10 §VII.A.4 locator. Use a short exact phrase without a typographic apostrophe, for example “inference latency as the primary metric”. Relate objective to latency and documented energy/throughput outcomes; cite the objective's original anchor when making that link.
3. R0054/D04: check original p.4 §IV Protocol and p.5 Fig. 3(c) caption. Specifically distinguish “Each scheme is trained” with “identical hyperparameters and evaluated on the same” for matched holdout from the narrower paired OOD comparison. Do not claim that the six matched-holdout schemes all participate in the paired OOD comparison.
4. R0059/D07: in original p.8 §5.1, avoid spanning the one-/tenth line wrap. Use “tenth of the clock cycles per number of cores.” or a short body phrase about the stable link/traces to support the conclusion. Qualify realism by the actual trace-driven simulation and stable link/coordination assumptions, without claiming a flight test.
5. Keep rationales within 30 words and each quotation within one original visible line. Report missing items and do not add numerical outcome magnitudes.

# REQUIRED OUTPUT

Exactly one compact JSONL object per fixed key or documented shortfall:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"One bounded reporting gap.","locators":[{"page":4,"section":"Methods","quote":"exact short phrase from original body"},{"page":5,"section":"Setup","quote":null}]}
Use YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE, or NOT_YET_ASSESSED. Physical pages start from one. End with a summary object containing returned_keys, unresolved, tools and workers_used=false. Then output P09_B03_CORRECTION_COMPLETE on its own line. Report identities are fixed in Batch 03 and locked P08.

# ACCEPTANCE CRITERIA

- Three unique in-scope keys with no missing key except one explicitly named and explained, no extra keys, and no duplicate entries or malformed JSONL.
- All decided claims carry verifiable original PDF page/section support. Zero mismatched verbatim excerpts, unsupported numerical results and repeated previously checked keys.
- No workers, no file changes and all unresolved evidence/tool limits explicit.

# BOUNDARIES

No altered corpus, no new search, no edits and no work outside these three fixed keys.

Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
