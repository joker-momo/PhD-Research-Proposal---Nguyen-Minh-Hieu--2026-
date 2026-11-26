# Search dataset lock — native-app correction acceptance

Reviewed at: 2026-11-26T16:02:08+07:00
Parent Gemini.app task: `68bfd2a8-833d-4ec0-91d7-64ee35b03c63`.
Correction task: `f37b9d7d-c382-4313-8554-ea9d8c549055`; context: `023047ed-ac29-4d1a-ad03-f88a33b4cdcb`.
Verdict: ACCEPTED for the bounded input-snapshot freeze only;10/10 original criteria PASS. This does not certify search completeness, eligibility of new rows, unique studies or manuscript readiness.

| Criterion | Verdict | Objective evidence |
|---|---|---|
| C1 | PASS | 10 rows;10 unique exact IDs;0 missing/extra IDs. |
| C2 | PASS | 20/20 reported/exported values and10/10 locators match original brief after patching. |
| C3 | PASS | 6 sources, each once; admitted rows63/0/110/0/111/0. |
| C4 | PASS | Exact173,111,284,9,102,404,[null,null],null; no final unique-record count. |
| C5 | PASS | 11 distinct official URLs retained, including PRISMA/PRISMA-S, ACM and Clarivate. ACM URLs are expressly inaccessible references, not verified policy evidence. |
| C6 | PASS | All6 retained methodology/capability findings have official URLs and source support checked. The unsupported ACM general-policy assertion was removed; ACM session-only statements retain local locators. RHN five-year detail removed. |
| C7 | PASS |0 statements equating OpenAlex/RHN with WoS Core or equivalent coverage. |
| C8 | PASS | ACM404 remains counts-only,0 imported; both WoS results remain null, not zero. |
| C9 | PASS |1 FREEZE_NOW decision;6/6 source names partitioned exactly once across3 record sources,1 counts-only source,2 unexecuted sources. |
| C10 | PASS |4 explicit unresolved items;0 unsupported quantitative assertions retained; Amendment006 preserved and new prospective freeze note recorded. |

## Targeted correction gate

| Correction criterion | Verdict | Evidence |
|---|---|---|
|1 | PASS |1 JSON object; correct parent/task IDs;8 unique allowed nonoverlapping patches. |
|2 | PASS | Original C1–C10 rechecked above;0 count/locator/arithmetic changes. |
|3 | PASS |11 official URLs; reporting/ACM/Clarivate present; no inaccessible ACM policy asserted as fact. |
|4 | PASS |6 source-supported method findings;0 unsupported RHN time windows or blanket harvesting/Premium-only restrictions. |
|5 | PASS |1 recommendation;6-source partition;0 source-equivalence/count conversions. |
|6 | PASS |4 shortfalls explicit; original Amendment006 remains unchanged; no fabricated author decision or unique count. |

## Source support and scope

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/ supports PRISMA2020 items6,7,24c. Full page was read directly and via web; the project-specific prospective note is our implementation of transparent reporting, not a claim that PRISMA mandates dataset freezing.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8270366/ supports PRISMA-S items1,7,13,15,16. Full HTML was readable through the direct request despite the web viewer challenge.
- https://webofscience.zendesk.com/hc/en-us/articles/25349933314193-About-Web-of-Science-Researcher-Profiles supports the distinction between free/registered access and entitled Document Search; the local session file establishes the actual access failure.
- https://help.openalex.org/data/how-its-built/ supports the aggregate catalog description, named inputs and CC0 distribution; local exports establish the counts.
- https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/incites-benchmarking-analytics/research-horizon-navigator/ supports the InCites module, emerging topics and AI theme assignment. No numerical time window is retained.
- ACM platform/policy pages returned403; no general policy conclusion is accepted. Export blockage is limited to the supplied session observations. IEEE/Scopus counts likewise rely on local CSVs and observation files, not inaccessible help/search pages.

## Transport and independent checks

Native Gemini.app Task only. Bridge commit `cbbfab9`:64/64 tests PASS. Correction context hashes independently verified2/2; bridge reports unchanged=true; exact matching chat deleted and Chat mode restored. Original non-app task is superseded and not adopted.

All25 raw-evidence checksums independently matched. Six importable CSVs contain42+21+77+33+85+26=284 rows. OpenAlex ID sets contain9 overlapping IDs and102 union IDs. All file bytes remain unchanged; the lock records SHA-256 rather than claiming OS write protection.

The original result remains quarantined as a standalone artifact. Accepted derived result: `../results/search_dataset_lock_app_reconciled.json`, produced only by applying the8 accepted patches. Raw transport and correction JSON remain separate for audit. No manuscript, submission, email or existing46-report decision was changed.
