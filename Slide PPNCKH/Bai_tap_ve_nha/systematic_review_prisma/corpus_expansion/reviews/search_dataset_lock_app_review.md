# Native Gemini.app search dataset lock review

Reviewed at: 2026-11-26T15:55:36+07:00
Task: `68bfd2a8-833d-4ec0-91d7-64ee35b03c63`; context: `b18ad5c5-6b10-4938-85f9-3cac38faac37`.
Status: REJECTED_C6_C10; 8/10 criteria PASS. Recommendation is quarantined, not adopted.

| Criterion | Verdict | Evidence |
|---|---|---|
| C1 | PASS | 10/10 query rows; exact ID set; zero duplicates. |
| C2 | PASS | 20/20 counts and 10/10 locators equal committed brief. |
| C3 | PASS | 6/6 sources, each once. |
| C4 | PASS | All eight arithmetic fields match; unique cross-platform count remains null. |
| C5 | PASS | 12 distinct official-domain URLs supplied, including original PRISMA/PRISMA-S, ACM and Clarivate; no nonofficial links. This checks source class, not semantic support (C6). |
| C6 | FAIL | ACM general policy/capability assertions could not be verified from two cited pages (403); RHN source page does not contain the asserted five-year window. |
| C7 | PASS | Zero claims that OpenAlex/RHN equals a WoS Core search or equivalent coverage. |
| C8 | PASS | ACM imported rows=0; WoS reported counts=[null,null]; no violations. |
| C9 | PASS | Exactly one FREEZE_NOW recommendation; six sources partitioned once across 3/1/2 lists. |
| C10 | FAIL | Unsupported five-year RHN detail and overly categorical Premium-only implication remain; unverified capabilities are not listed as unresolved. Amendment006 already exists prospectively, so rewriting it must not be implied. |

## Transport and local verification

Native Gemini.app Task completed; context unchanged=true, file_count=1; matching chat deleted and Chat mode restored. Bridge fix `cbbfab9` passed64/64 tests; 30 label cases exercise the actual JS/Swift predicates, including the observed false positive. No CLI research result is used.

Raw evidence ledger25/25 hashes PASS. IEEE63 rows, Scopus110 rows, OpenAlex111 rows with9 shared IDs and102 union IDs. Arithmetic284 is pre-deduplication only.

## Source verification

PRISMA2020 explanation at https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/ supports items6,7,24c. PRISMA-S https://pmc.ncbi.nlm.nih.gov/articles/PMC8270366/ supports items1,7,13,15,16 (full HTML fetched via urllib; web viewer challenged). Clarivate researcher-profile help supports the non-subscriber Document Search restriction (web viewer); OpenAlex how-it-is-built supports its distinct aggregate catalog and CC0 distribution (web viewer). Clarivate RHN product page (HTTP200) supports emerging-topic/InCites functionality but not the specific five-year window. ACM pages, IEEE search endpoint and Scopus help failed direct retrieval; do not pretend HTTP status proves factual support. Exact CSV counts derive from local evidence, not those endpoints.

A linked correction may remove nonessential unsupported claims and explicitly retain access shortfalls. A generic unavailable URL is not itself evidence that a claim is false. No dataset freeze is adopted pending correction.
