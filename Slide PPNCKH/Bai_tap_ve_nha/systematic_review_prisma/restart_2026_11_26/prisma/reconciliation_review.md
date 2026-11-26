# Step 13 — PRISMA 2020 reconciliation of the HK261 restart

The data unit changes after title/abstract screening. The [count artifact](prisma_counts.json) anchors each transition to exact raw record IDs, screening or report IDs, or study IDs. Its normalized raw-row locations are 1-based data rows, excluding CSV headers. Inputs are the restart's locked search dataset, decisions and appraisal artifacts. No old 46-report dataset was imported.

| Transition | Equation | Evidence |
|---|---|---|
| Raw records to title/abstract screening | 693 = 228 duplicates + 465 screened | `raw_file_index`, `raw_ids_by_dedup_reason`, `dedup_groups` |
| Screened records to sought reports | 465 = 328 title/abstract exclusions + 137 sought | `screening_ids_by_title_abstract_decision`, `report_ids_by_retrieval_decision` |
| Sought reports to full-text assessment | 137 = 93 not retrieved + 44 assessed | `report_ids_by_retrieval_decision` |
| Full-text assessment to included reports | 44 = 13 excluded + 6 awaiting classification + 25 included | `report_ids_by_fulltext_decision` |
| Included reports to study units | 25 reports map to 25 study IDs | `study_ids_to_report_ids`, `tested_version_pairs` |

### Retrieval decisions versus initial screening

| Initial title/abstract decision | Reports sought | PDF retrieved | Report not retrieved |
|---|---:|---:|---:|
| Retrieve full text | 44 | 30 | 14 |
| Unclear, forwarded for clarification | 93 | 14 | 79 |
| Total | 137 | 44 | 93 |

The 93 unclear records and 93 nonretrieved reports are different sets. The [missing-PDF log](../fulltext_retrieval/missing_pdf.csv) preserves the original access reason, route and links for every nonretrieved report. Those reports do not receive an eligibility exclusion. The 13 full-text exclusions have one primary reason each, from E1 (4), E2 (3), E3 (4), E6 (1) and E7 (1). See the [exclusion ledger](../fulltext_screening/exclusions.csv).

Six assessed reports remain awaiting classification. R0075, R0092, R0110, R0118 and R0137 have unresolved date eligibility (E5). R0081 has unresolved publication-type eligibility (E7). They contribute to the assessment count only. Among included reports, step 10 found no established merge among the 13 version-linkage candidates. The 25-study count reflects that documented linkage audit, subject to its detection coverage.

### Limits to carry into the manuscript

- Four executed sources retain seven input files and eight selected runs. ACM combines two manually captured result lists and applied a month-level ceiling. OpenAlex is supplementary. Web of Science was not searched because access was unavailable, and its count remains null. The [locked search log](../search_log.md) preserves actual timestamp bases, executed query variants and filters.
- Selection, extraction and appraisal were AI-assisted and checked by Codex. There is no record of two independent human reviewers or an author adjudication of the final corpus.
- Report the 93 access shortfalls and the six unresolved decisions as possible sources of incomplete coverage. Appraisal uses a bespoke engineering-domain instrument and supplies no formal certainty grade.

### Deterministic acceptance checks

| Criterion | Verdict | Evidence |
|---|---|---|
| Exact ID preservation through every stage | PASS | 693 raw IDs linked to source rows and all 465 representative IDs accounted for, then 137 sought and 44 assessed report IDs partitioned without gaps. |
| Zero unexplained arithmetic difference | PASS | 4/4 stage equations close and key sets are identical at handoffs. |
| Separate exclusion, awaiting and study-family units | PASS | 13 primary exclusions, 6 awaiting IDs, 93 nonretrieved reports and 25 report-to-study links. |
| P08 and P09 align to the included set | PASS | P08/P09 gate labels and 14 locked file hashes verified. Both map to the same 25 reports. P09 has 250 judgments and 0 pending. |
| Flow and checklist | PASS | [Flow PDF](prisma_flow.pdf) built and inspected, 1/1 pages. [Checklist](prisma_checklist.md) contains 27/27 numbered items with status, locator and limitations, with final manuscript locations deferred to drafting. |
| Restart-only scope | PASS | Seven raw input file hashes checked. Old corpus import rows = 0. WoS status remains unsearched with null count. |

The independent [Gemini.app composite review](audit_review.md) passed after correcting five column locators. The provider result did not change the reconciled counts.
