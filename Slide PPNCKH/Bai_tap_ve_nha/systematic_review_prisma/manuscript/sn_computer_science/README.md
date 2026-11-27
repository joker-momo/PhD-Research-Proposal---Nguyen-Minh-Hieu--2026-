# HK261 systematic technical survey

`main.tex` is the editable source, `references.bib` is the bibliography, and
`main.pdf` is the compiled HK261 review. The build uses the Springer Nature
`sn-jnl.cls` and `sn-vancouver-num.bst` files from the December 2024 template.

Build the comparison draft from this directory:

```sh
python3 build_technical_survey.py
tectonic --keep-logs --keep-intermediates main.tex
python3 build_technical_survey.py --check
python3 check_evidence.py
```

The generator derives both technical tables, the appraisal rows, and the figure
counts from the accepted corpus, the appraisal summary, and [the primary coding
ledger](technical_coding.psv). Its check fails if a generated input is stale or
an included study is missing from either study table or the analytical text.

[Supplement S4](supplement_evidence_index.md) maps the text and 13 numbered
figures, tables, and equations to their sources. It gives the calculation,
input data and generation code for each chart, commands to rebuild the PRISMA
diagram and manuscript, and original-page locators for the quantitative
comparisons. The [snapshot](evidence_sha256.txt) fixes the file versions used
for the crosswalk. Each new or changed factual claim, number, figure, table,
and equation needs a source locator or a checkable derivation. Keep unresolved
claims in the evidence record until they can be supported. Update the crosswalk,
regenerate affected outputs, and run the checks before recording a new snapshot. `--record` records the reviewed
files. It does not adjudicate a claim.

The comparison PDF uses the Springer Nature class and bibliography style with
a 216 mm text height and compact reference spacing to fit the full-corpus
tables into the requested single-column length. For this branch, see
[the initial technical survey review](technical_survey_review.md) and [the current evidence record](supplement_evidence_index.md). The original
13-page coursework checkpoint remains available at commit `7a6675d`.

The review includes 46 reports representing 46 studies. The
[PRISMA ledger](../../restart_2026_11_26/prisma/prisma_counts.json) records 87
full-text exclusions, three reports awaiting classification and one unretrieved
report. The [PRISMA 2020 checklist](../../restart_2026_11_26/prisma/active_prisma_checklist.md)
tracks reporting and its limits.

- S1. [Search strategies](supplement_search_strategies.md)
- S2. [Excluded full-text reports and decision locators](supplement_fulltext_exclusions.csv)
- S3. [Study characteristics](../../restart_2026_11_26/synthesis/active_study_characteristics.csv),
  [report-level appraisal](../../restart_2026_11_26/appraisal/active_appraisal_table.csv),
  [outcome evidence](../../restart_2026_11_26/synthesis/active_outcome_evidence.csv),
  [claim sources](../../restart_2026_11_26/synthesis/active_claim_source_matrix.csv) and
  [R0092 source erratum](../../restart_2026_11_26/synthesis/active_rq_p08_erratum_R0092.json).

The baseline [final integrity audit](../../restart_2026_11_26/integrity/active_final_integrity_audit.md) and [limitations](../../restart_2026_11_26/integrity/active_limitations.md) accompany the coursework handoff. Author details and declarations await confirmation. Journal submission is outside the current HK261 scope.
