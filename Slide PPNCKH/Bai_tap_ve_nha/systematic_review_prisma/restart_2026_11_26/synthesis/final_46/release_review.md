# HK261 final 46-study comparison release

The task branch holds the [new 29-page PDF](../../../manuscript/sn_computer_science/main.pdf) and the [previous 29-page PDF](../../../manuscript/sn_computer_science/comparison_previous_46.pdf). The previous file is byte-for-byte the manuscript PDF from commit `92edf84`. The LaTeX source is [main.tex](../../../manuscript/sn_computer_science/main.tex). No new author decisions were entered during the synthesis or build.

| Gate | Verified result |
| --- | --- |
| PRISMA and study IDs | 136 assessed = 46 included + 90 excluded + 0 awaiting. One of 137 sought reports was unretrieved. Relative to the previous 46-study PDF, R0082 (S047) replaced R0113. R0292 (S046) remained included. |
| Outcome ledger and appraisal | 105 rows: 51 matched, 47 descriptive, 4 held and 3 cross-references. 98 retained entries, 36 contributing reports, 23 reports with matched outcomes, 10 plot-only, 0 with unresolved printed outcomes at report level. 460 engineering judgments. D01 is 45 Yes and 1 Partial. |
| Human adjudication | 8 final decisions, 128 assessed reports without documented author confirmation, 4/8 changed among author-processed and 4/8 among final decisions. Zero reviewer pairs. Agreement and kappa are undefined. |
| Evidence links | 164 claim entries over 90 prose lines, source links for 46 rows in the technical tables, nine numerical contrast rows and 49 original PDF checksums. The source index covers all 5 figures, 8 tables and 3 equations. |
| Original R0082 and related evaluation | [Source review](r0082_review.md) records physical arXiv v1 locators, plot-only outcomes, engineering appraisal and comparisons against R0019. R0082 contributes no inferred numerical values. Its IEEE publisher pages were unavailable. R0019 and R0082 differ in technical method and reported experiments; reuse of underlying inputs or runs remains unresolved. |
| Build and reproduction | Eight adjudication/reconciliation unit tests passed. LaTeX compilation completed with no undefined citations/references. PDFKit verified PRISMA at p. 6, outcomes at pp. 20–21, appraisal at pp. 21–22 and S2 audit at p. 24. Figure, table and equation pages were rendered and inspected. An isolated build using the [portable evidence package](../../../manuscript/sn_computer_science/minh_chung_hinh_bang/README.md) regenerated the figures, tables and S2 outputs and matched all 29 canonical page renders (1440 × 1800 thumbnail bounds, TIFF SHA-256). |

The changed PDF renders compared with the previous draft are physical pp. 1, 4–13, 15–18, 20–22 and 24–29. Many changes reflect the new citation order. The audit table retains IDs of author-confirmed exclusions as part of the decision record.

[Supplement S3](../../../manuscript/sn_computer_science/supplement_s3.md) provides data and derivations. [Supplement S4](../../../manuscript/sn_computer_science/supplement_evidence_index.md) indexes each figure, table, equation, and prose claim. The original study PDFs stay in the project and are identified by path and SHA-256. The portable package rebuilds from the checksummed frozen inputs; the worktree commands rerun validation from the upstream project ledgers.
