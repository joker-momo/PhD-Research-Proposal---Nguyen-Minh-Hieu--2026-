# HK261 supplemental full-text screening closeout

Completed at `2026-11-27T12:19:25+07:00`. The screening decisions apply P03 and the P06 exclusion precedence at report level. Codex checked each accepted source locator after the Gemini.app first pass. The retained decisions have received AI-assisted screening and verification. Author adjudication remains pending.

| Batch | Reports | Include | Exclude | Awaiting classification | Evidence commit |
| --- | ---: | ---: | ---: | ---: | --- |
| [Batch 05](batch_05_review.md) | 13 | 4 | 9 | 0 | `ab63f84` |
| [Batch 06](batch_06_review.md) | 13 | 0 | 13 | 0 | `b063f3f` |
| [Batch 07](batch_07_review.md) | 13 | 1 | 12 | 0 | `e64133c` |
| [Batch 08](batch_08_review.md) | 13 | 0 | 13 | 0 | `42c74c7` |
| Batches 05–08 | 52 | 5 | 47 | 0 | |
| Supplemental retrieval total | 92 | 16 | 74 | 2 | |

Batch 05 was recovered by reading the saved task UUID in its [bridge receipt](batch_05_bridge_receipt.json). It was dispatched once. The 92 supplemental records consist of 91 batch decisions and the existing R0070 exclusion carried forward under the same DOI and counted once.

Primary supplemental exclusion reasons were E1 = 8, E2 = 26, E3 = 35, E4 = 1, E7 = 4. Supplemental reports awaiting classification are `R0082` (E7), `R0132` (E2|E3). The per-report ledger uses paths relative to the HK261 review directory and links each row to the accepted criterion notes and page or section evidence.

The earlier set of 44 consisted of 25 included, 13 excluded and six awaiting classification. The [six rechecks](prior_awaiting_recheck.json) support inclusion of `R0075`, `R0092`, `R0110`, `R0118`, `R0137`. R0081 still awaits confirmation of the applicable MobiSys 2022 demonstration-track peer review (E7). R0116 remains the sole report without a retrieved PDF.

The [decision ledger](screening_decisions.csv) contains 92 distinct IDs, normalized DOIs and SHA-256 values. All 92 paths resolve and byte hashes and page counts match the [evidence catalog](../../prisma_evidence/evidence_by_id.csv). The closeout check independently matched 300 retained physical-page excerpts across the 52 reports. The catalog covers 136 original PDFs.

Gemini.app cleanup was verified for batch 07. Cleanup was unverified for batch 05, batch 06, batch 08. Local receipts retain the research results.
