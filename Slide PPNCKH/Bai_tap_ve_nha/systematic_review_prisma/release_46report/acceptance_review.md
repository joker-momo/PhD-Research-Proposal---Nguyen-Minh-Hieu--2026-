# Acceptance review: bounded 46-report manuscript

Updated at: 2026-11-26T11:08:27+07:00

This review accepts the delivery scope only. It does not certify an exhaustive systematic search, finalized study families, uniform extraction/appraisal or submission readiness. Previously accepted Gemini evidence was reused; no new A2A task was dispatched.

| Criterion | Verdict | Measured evidence |
|---|---|---|
| all_46_reports_accounted | PASS | 46 unique report IDs in accounting ledger |
| decision_arithmetic | PASS | 46 = 36 working INCLUDE + 2 EXCLUDE + 8 UNCERTAIN; difference 0 |
| 36_extraction_rows_and_table_rows_match | PASS | 36 CSV rows = 36 Table 1 IDs = current working included set |
| every_extraction_row_has_locator | PASS | 36/36 rows carry accepted-result and full-text locators |
| 12_delta_records_24_exact_page_quotes | PASS | 12 delta records, 24/24 quotes match named PDF pages |
| 92_original_evidence_hashes_match | PASS | 46 PDF and 46 text hashes equal original intake checksums |
| retained_appraisal_216 | PASS | 24 x 9 = 216; yes 100, partial 110, no 6 |
| appraisal_missingness_explicit | PASS | 24 domain-9 values WITHHELD; 12 report rows NOT_ASSESSED |
| 53_citations_resolved_exact_bib_set | PASS | 53 cited keys equal 53 bibliography entries; unresolved 0 |
| 53_dois_unique | PASS | 53 distinct normalized DOI values |
| no_missing_bibliographic_identity | PASS | 53/53 title, authors, year, venue and DOI populated from retained evidence |
| no_undefined_citations_or_overfull_boxes | PASS | Final LaTeX log: undefined 0, overfull 0, fatal 0 |
| no_manuscript_placeholder_markers | PASS | TBD/TODO/XXX/PLACEHOLDER and fake affiliation markers 0 |
| 27_checklist_items | PASS | Items 1-27, status plus locator plus limitation; subitems explicitly mapped |
| abstract_word_range | PASS | 194 words excluding structured labels |
| 22_nonempty_pdf_pages | PASS | 22/22 pages contain extractable content |
| source_newer_than_historical_pdf | PASS | Compiled PDF newer than final TeX and bibliography |
| author_identities_not_imputed | PASS | No unconfirmed author/affiliation block; review-copy status disclosed |
| no_new_performance_effects | PASS | 0 newly adopted performance magnitudes from delta records |
| unknown_study_count_retained | PASS | Unique-study count null; report unit used throughout |
| all_36_extraction_cells_explicit | PASS | 36/36 rows have values or explicit NOT_EXTRACTED/withheld limitations |
| 46_report_dois_unique | PASS | 46 accounted reports, zero normalized DOI duplicates |
| no_unapproved_submission_changes | PASS | No submission evidence, author form, search brief or email artifact changed |

| Visual review | PASS | 22/22 pages inspected; final changed pages 15-22 re-inspected, pages 1-14 pixel-identical |

## Retained limitations

- Twelve added reports have minimum extraction, not completed detailed outcome extraction or appraisal.
- Domain 9 is withheld; 216 accepted judgments do not represent all 36 reports.
- Database identification counts and unique-study count remain unknown; eight reports await classification.
- Three nonfatal BibTeX warnings concern omitted conference page ranges (C22/C23/C24); no metadata was guessed.
- The manuscript is an interim review copy with unconfirmed authorship/declarations and no submission.
- A zero-fabrication policy is enforced by using accepted evidence and retaining unknowns; this audit is not an independent re-review of every source claim.
