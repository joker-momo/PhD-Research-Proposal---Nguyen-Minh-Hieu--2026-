# TASK
Correct three specific rejected Batch 02 outcomes components only, linked to the original e891c230-d182-4bfa-8068-1cba64226569 and correction 06 432bbd73-3594-440b-a7a2-104f1804e2a3.

# REQUIRED WORK
1. Parent opens the three authorized attached PDFs using the Task folder. Paths relative to the attached project are restart_2026_11_26/fulltext_retrieval/pdf/{R0074,R0121,R0062}.pdf. Resolve paths from the selected project mount, not an unmounted worker's working directory. If relative lookup fails, resolve it under the authorized attached host directory named below if the parent has that ability. No locations outside this project. Verify one exact short body quote, physical page and section per PDF or report a specific access error. Parent handles this assignment unless workers demonstrably share access; no worker overlap.
2. T01, R0074 physical page 17, section 4.2: repair only the quote covering the successful distributed 70B comparators. Use a short contiguous fragment wholly on p17. Avoid words beginning the sentence on p16. Support the named successful comparators and omit numerical latency claims. Keep unrelated field evidence unchanged.
3. T02, R0121 physical page 6, Section 6: repair only the typed precision of the approximate per-hop speedup. Keep the approximation in the value itself, with the original workload and conditions, and a short source quote on that physical page containing the approximation. Do not repeat other K03 rows.
4. T03, R0062 physical page 6, Effect of UAV Unavailability: repair only the inherited outcomes field sentence about stage 2 precision. The existing separate approved frame-rate keys remain untouched. Supply an exact contiguous fragment with the approximate stage 2 value and its unit, clearly scoped to one unavailable UAV. If retaining a distinct stage 3 recovery finding from the inherited sentence, give it a separate short exact page-6 anchor and do not quantify it unless the section explicitly provides a numerical measurement for stage 3. No application details.

# REQUIRED OUTPUT
One P08_DELEGATION followed by JSON {subagent_status,reason,assignments:[{worker,report_ids}]} with enum USED_CONFIRMED, UNAVAILABLE, UNCONFIRMED. One P08_ACCESS followed by compact JSON {reports:[{report_id,pdf_path,status,page,section,excerpt,reason}]} with OBSERVED or NOT_ACCESSIBLE. Between standalone P08_FIX_BEGIN and P08_FIX_END lines put exactly three compact records with this shape (example only, no invented evidence):
{"key":"T00","report_id":"R0000","status":"OBSERVED","assertions":[{"finding":"one finding","page":6,"locator":"actual section","excerpt":"exact contiguous excerpt","quantitative":null}],"reason":""}
Allowed status OBSERVED, UNVERIFIED, NOT_ACCESSIBLE. For OBSERVED NUMBER use quantitative with exactly {value,units,baseline,denominator,workload,conditions}, all strings. Include approximation in value as printed. An unresolved record has empty assertions and specific reason. End with P08_SUMMARY JSON {returned_keys,unresolved_keys}, then P08_COMPLETE.

# ACCEPTANCE CRITERIA
A1: Three unique keys T01/T02/T03, three exact IDs in scope, zero additions or duplicates.
A2: Three body access anchors and 100% assertion anchors independently verifiable. One physical source page per exact continuous excerpt.
A3: T01 contains no mis-scoped outcome or abstract-only source; T02 and T03 preserve the original approximations in the typed values and bound the conditions independently. Zero added claims.
A4: Three parseable objects, correct enum/types and reconciled summary; unknowns explicit.
A5: One parent, 0 overlaps, 0 previously passing components rewritten.

# BOUNDARIES
Read-only attached project and named PDFs only. No web search, file changes, manuscript prose, guesses, figures estimated as exact, or reporting other components. Record the precise access problem if any.

Authorized attached host directory if visible to the Task parent: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma
