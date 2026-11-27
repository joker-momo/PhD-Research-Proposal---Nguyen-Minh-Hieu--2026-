# S3. Study characteristics, appraisal, outcomes and S2 audit

| Need | Evidence |
| --- | --- |
| Find one of the 46 studies | [Study characteristics](../../restart_2026_11_26/synthesis/active_study_characteristics.csv), [source identity and SHA-256](../../restart_2026_11_26/synthesis/active_synthesis_input_index.csv), and [sources for individual technical-table cells](s4_study_row_sources.csv). |
| Check one engineering judgment | [460 judgments with rationales and original locators](../../restart_2026_11_26/appraisal/active_appraisal_rationale_matrix.csv). |
| Reconstruct the uniform RQ5 reread | [Pre-extraction rule](../../restart_2026_11_26/extraction/rq5_uniform/rule.md), [frozen PDF manifest](../../restart_2026_11_26/extraction/rq5_uniform/manifest.json), [report coverage](../../restart_2026_11_26/extraction/rq5_uniform/report_coverage.csv), and [outcome ledger](../../restart_2026_11_26/extraction/rq5_uniform/outcomes.csv). |
| Check the quantitative prose and the two summary tables | [RQ5 claim sources](../../restart_2026_11_26/extraction/rq5_uniform/claim_source.csv), [mechanism and evaluation coding with original locators](../../restart_2026_11_26/synthesis/desk_reject_evidence_map.csv), and [table generator](build_editorial_evidence.py). |
| Check the nine illustrated comparisons | [S4 row map](supplement_evidence_index.md#numerical-contrast-row-map) and [source-verified R0092 correction](../../restart_2026_11_26/synthesis/active_rq_p08_erratum_R0092.json). |
| Reproduce the S2 audit in Table 8 | [S2 log](human_adjudication_log.csv), [audit output](audit_summary.json), [generated LaTeX](adjudication_audit_table.tex), and [S4 derivations](supplement_evidence_index.md#s2-audit-derivations). |

The numerical inventory, coverage and coding were imported from the sibling
manuscript's verified release at Git commit `5910b6b`. The [source release
review](../../restart_2026_11_26/extraction/rq5_uniform/review.md) records the
inspection method, tabular and plot locators, and issues requiring original-page
inspection. The integration verified that all 46 report/study pairs, original
paths and PDF hashes agree with the technical survey. The 108 ledger rows
comprise 51 matched, 47 descriptive, seven held and three cross-references.
Only matched and descriptive rows contribute to the total of 98. The 36
studies contributing numbers include the 23 with matched results. Nine have
plot-only evidence under the rule and one has printed values lacking
interpretable measurement context. Physical PDF pages are counted from one.
The extraction samples explicit outcomes by domain and does not estimate
reporting completeness or supply a pooled effect.

The 21 supplemental included reports are identified by
`supplemental_batch_` in the accepted input index's `extraction_source`.
Joining by report ID to report coverage yields 18 with retained quantitative
evidence (52 entries), two plot-only (R0043, R0077) and one with printed
results whose conditions are unresolved (R0113). The study count and outcomes
refer to the current PRISMA selection of 46 included studies.

## S2 audit of author decisions

Of the 136 assessed reports, 133 lack documented author confirmation
(136 − 2 final decisions − 1 confirmed deferral). The author processed three
reports. R0081 (E7) and R0132 (E3) moved from awaiting classification to
exclusion, and R0082 remains awaiting E7 verification. Changes therefore
account for **2/3 author-processed reports** and **2/2 reports with final
decisions**. These fractions describe the recorded subset. The S2 log has
zero paired independent human decisions, so observed agreement and Cohen's
kappa are undefined. The verified PRISMA totals are 46 included,
89 excluded and one awaiting classification. See [S2](supplement_s2_adjudication.md)
for the case-level decisions and original-page locators.
