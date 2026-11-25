# Batch 04 brief gate

Date: 25 November 2026

Brief: `screening_46/briefs/batch_04.md`

Brief commit before this gate: `195ea79d1b2883abf2e443e1adfb2270ccad9b7e`

Brief SHA-256: `353289f61b8625248e48accfe2c29020e3f097cb8a2e0abf30e9f34000826ca2`

This gate validates the research contract and supplied-file inputs only. It does
not contain screening decisions and does not accept provider output.

| Criterion | Verdict | Objective evidence |
|---|---|---|
| Five mandatory brief headings | PASS | `TASK`, `REQUIRED WORK`, `REQUIRED OUTPUT`, `ACCEPTANCE CRITERIA`, and `BOUNDARIES` each occur exactly once |
| Exact record set | PASS | 6/6 unique IDs in order: S19, S20, C01, C02, C03, C04; silent shortfall count 0 |
| Supplied evidence resolves | PASS | 18/18 source/PDF/text absolute locators exist |
| Frozen identity inputs agree | PASS | 6/6 DOI, page-count, and PDF SHA-256 values equal the frozen manifest; 6/6 PDF hashes equal the checksum ledger |
| Output schema is measurable | PASS | One JSON object; exact batch and record fields; six named gates; allowed statuses/decisions; project mutation count required to equal 0 |
| Mandatory research checks | PASS | DOI or `DOI_NOT_FOUND`, source version, page/quote locators, zero normalized DOI/title duplicates, zero unsupported quantitative claims, and explicit unresolved arrays are required |
| Ownership and integrity boundary | PASS | Read-only supplied evidence; no project edits, downloads, credentials, final prose, Git, or external messages; missing evidence must remain uncertain |
| Prior Batch 04 transport/result/review artifact | PASS | 0 matching artifact before creation of this gate; no task has been dispatched |

Gate verdict: **PASS — brief is valid and committed before dispatch.**

Dispatch remains temporarily blocked because `scripts/run_screening_batches.py`
still checks repository-wide status. That driver must adopt the same three owned
scopes as the accepted baseline-aware hook in a separate tested commit. The
brief must remain byte-identical while that prerequisite is repaired.
