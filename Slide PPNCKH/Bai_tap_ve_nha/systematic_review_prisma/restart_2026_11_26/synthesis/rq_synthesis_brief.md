# TASK

Build a structured synthesis for RQ1–RQ5 from the 25 study units in the locked HK261 restart.

# REQUIRED WORK

1. Read the attached project directly. Use only `restart_2026_11_26/protocol_restart.md` P02 and P10, `prisma/prisma_counts.json`, `study_linkage/report_study_map.csv`, `extraction/p08_extraction_table.json`, `extraction/p08_quantitative_claim_source_matrix.csv`, `appraisal/appraisal_table.csv` and `appraisal/rationale_source_matrix.csv` under the restart directory. The accepted P08 entries and P09 rationales already identify original PDF file/page/section. Use their retained keys, plus original PDF as needed. If also opening a PDF, prefer local PyMuPDF where available and local MinerU then Marker only for complex layouts. Report tools actually available and used. No PDF uploads. Use the parent task to retain project access and reconcile one response.
2. Return exactly two distinct substantive conclusions per RQ and a concise evidence limitation per RQ. Each conclusion must be precise enough to independently verify from 1–3 retained field keys associated with original PDF page and section, or a complete, reproducible classification with report IDs. At least one conclusion per RQ must map to P08. For RQ3/RQ5 include P09 with domain and actual source-located judgment. Avoid broad “none found” or “dominant” claims unless based on every eligible report and documented coding.
3. For RQ1 distinguish collaboration topology from model partition granularity. For RQ2 distinguish decisions made by the optimization algorithm from fixed experimental settings. For RQ3 identify type of evidence and comparator setup. For RQ4 distinguish changing links/mobility assumptions from tested mobility, and communication interruption from UAV loss/recovery. For RQ5 use at least one accepted individual-study numerical row, with the original value, units, baseline, denominator (as recorded), workload, conditions, physical page and locator verbatim from the P08 quantitative matrix. Do not pool effects or generalize across incompatible configurations.
4. For any frequency, supply distinct report IDs for the numerator, exact denominator and eligible set definition. Prefer source-bound examples when exhaustive evidence classification is ambiguous. Keep unresolved statuses explicit and do not equate missing reporting with observed absence.

# REQUIRED OUTPUT

Compact JSONL: ten conclusion objects, two each for RQ1 through RQ5, and one summary object. Example with illustrative values only:
{"rq":"RQ1","claim_id":"RQ1-A","finding":"Scoped finding suitable for checking","citations":[{"report_id":"RTEST","source":"P08","key":"partition_and_assignment:1","physical_page":3,"section":"II.B"}],"frequency":null,"quantitative":null}
Use claim IDs RQ1-A, RQ1-B up through RQ5-B. The citation source enum is P08, P09, P08_QUANT. For P09 key use actual domain code. Citation physical page is 1-based and section is exactly stated in the locked derivative. Frequency if used: {"n":2,"N":25,"numerator_ids":["RTEST","RTEST2"],"denominator":"eligible set definition"}. Quantitative if used: {"report_id":"RTEST","key":"quantity:1","value":"value as printed","units":"as recorded","baseline":"as recorded","denominator":"as recorded","workload":"as recorded","conditions":"as recorded","page":6,"locator":"exact section or table"}. Summary: {"summary":true,"limitations":{"RQ1":"...","RQ2":"...","RQ3":"...","RQ4":"...","RQ5":"..."},"tools":[],"workers_used":false,"unresolved":[]}. An unresolved item supplies affected key and reason. End with `HK261_RESTART_14_SYNTHESIS_COMPLETE` alone.

# ACCEPTANCE CRITERIA

10/10 distinct conclusion keys and 5/5 separately named limitations or explicit documented shortfalls. 100% conclusions cite approved report IDs and actual evidence keys plus locator. At least one P08 claim per RQ and at least one P09 judgment supporting each of RQ3 and RQ5. At least one accepted RQ5 value preserving all measurement conditions. Zero unsupported numeric claims, malformed locators or duplicate keys. All frequencies include numerator IDs and denominator, or no frequency is asserted. Zero pooled or cross-study performance effects from incompatible experiments. No invented status when uncertain.

# BOUNDARIES

Return findings for independent verification, not manuscript prose. No filesystem edits, external searches, old corpus, disclosure of unrelated files, new appraisal, values withheld in P08, or inclusion of pending/unretrieved records. No new model runs, meta-analysis, submissions, or author inferences.
