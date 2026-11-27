# SN Computer Science coursework manuscript

`main.tex` is the editable source, `references.bib` is the bibliography, and
`main.pdf` is the compiled HK261 review. The build uses the Springer Nature
`sn-jnl.cls` and `sn-vancouver-num.bst` files from the December 2024 template.

Build from this directory with the approved command:

```sh
tectonic --keep-logs --keep-intermediates main.tex
```

The review includes 46 reports representing 46 studies. The
[PRISMA ledger](../../restart_2026_11_26/prisma/prisma_counts.json) records 87
full-text exclusions, three reports awaiting classification and one unretrieved
report. The [PRISMA 2020 checklist](../../restart_2026_11_26/prisma/active_prisma_checklist.md)
tracks reporting and its limits.

- S1. [Search strategies](supplement_search_strategies.md)
- S2. [Excluded full-text reports and decision locators](supplement_fulltext_exclusions.csv)
- S3. [Study characteristics](../../restart_2026_11_26/synthesis/active_study_characteristics.csv),
  [46-study revision evidence map](../../restart_2026_11_26/synthesis/desk_reject_evidence_map.csv),
  [revision evidence and eligibility checks](../../restart_2026_11_26/synthesis/desk_reject_revision_review.md),
  [report-level appraisal](../../restart_2026_11_26/appraisal/active_appraisal_table.csv),
  [uniform RQ5 extraction rule](../../restart_2026_11_26/extraction/rq5_uniform/rule.md),
  [46-report outcome coverage](../../restart_2026_11_26/extraction/rq5_uniform/report_coverage.csv),
  [page-level outcome ledger](../../restart_2026_11_26/extraction/rq5_uniform/outcomes.csv),
  [RQ5 claim sources](../../restart_2026_11_26/extraction/rq5_uniform/claim_source.csv),
  [RQ5 source verification](../../restart_2026_11_26/extraction/rq5_uniform/review.md),
  [baseline claim sources](../../restart_2026_11_26/synthesis/active_claim_source_matrix.csv) and
  [R0092 source erratum](../../restart_2026_11_26/synthesis/active_rq_p08_erratum_R0092.json).

The [integrity audit](../../restart_2026_11_26/integrity/active_final_integrity_audit.md) and [limitations](../../restart_2026_11_26/integrity/active_limitations.md) describe the baseline coursework handoff at commit `7a6675d`. The revision evidence records the checks for this branch. Author details and declarations await confirmation. Journal submission is outside the current HK261 scope.
