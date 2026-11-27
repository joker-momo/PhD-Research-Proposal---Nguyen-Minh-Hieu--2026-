# S3. Study characteristics, appraisal, outcomes and S2 audit

| Need | Evidence |
| --- | --- |
| Find one of the 46 studies | [Study characteristics](../../restart_2026_11_26/synthesis/final_46/study_characteristics.csv), [source identity and SHA-256](../../restart_2026_11_26/synthesis/final_46/synthesis_input_index.csv), and [sources for individual technical-table cells](s4_study_row_sources.csv). |
| Check the R0082 source and relation to R0019 | [Source review](../../restart_2026_11_26/synthesis/final_46/r0082_review.md), [accepted field and appraisal evidence](../../restart_2026_11_26/synthesis/final_46/r0082_evidence.json), and [reconciliation script](../../restart_2026_11_26/synthesis/final_46/reconcile_inputs.py). |
| Check one engineering judgment | [460 judgments with rationales and original locators](../../restart_2026_11_26/synthesis/final_46/appraisal_rationale.csv). |
| Reconstruct the uniform RQ5 reread | [Pre-extraction rule](../../restart_2026_11_26/extraction/rq5_uniform/rule.md), [frozen PDF manifest](../../restart_2026_11_26/synthesis/final_46/outcome_manifest.json), [report coverage](../../restart_2026_11_26/synthesis/final_46/report_coverage.csv), and [outcome ledger](../../restart_2026_11_26/synthesis/final_46/outcomes.csv). |
| Check the quantitative prose and the two summary tables | [RQ5 claim sources](../../restart_2026_11_26/synthesis/final_46/rq5_claim_sources.csv), [mechanism and evaluation coding with original locators](../../restart_2026_11_26/synthesis/final_46/mechanisms.csv), and [table generator](build_editorial_evidence.py). |
| Check the nine illustrated comparisons | [S4 row map](supplement_evidence_index.md#numerical-contrast-row-map) and [source-verified R0092 correction](../../restart_2026_11_26/synthesis/active_rq_p08_erratum_R0092.json). |
| Reproduce the S2 audit in Table 8 | [S2 log](human_adjudication_log.csv), [audit output](audit_summary.json), [generated LaTeX](adjudication_audit_table.tex), and [S4 derivations](supplement_evidence_index.md#s2-audit-derivations). |

The [historical reread review](../../restart_2026_11_26/extraction/rq5_uniform/review.md) documents the source method. The final release filters the previous corpus by the approved PRISMA IDs, removes R0113 and adds the independently checked R0082 fields. R0292 remains included. The 105 numerical-ledger rows contain 51 matched, 47 descriptive, four held and three cross-references. The 98 retained entries come from 36 studies, including 23 with matched entries. Ten studies, including R0082, report results only as curves under the extraction rule. The final corpus has zero studies with printed outcomes held at report level for unresolved context. Individual held rows remain listed. The inventory samples explicit outcomes and supplies no pooled effect.

R0082's bibliography identifies the IEEE proceedings publication. The archived extraction uses physical pages counted from one in the retained arXiv v1 PDF. All six field anchors, all ten appraisal anchors and all four result figure captions were cross-checked at the same physical pages in the author-supplied IEEE proceedings PDF. The [cross-check](../../restart_2026_11_26/synthesis/final_46/r0082_publisher_crosscheck.json) records the file fingerprints and results. Source review records overlap with R0019 and the distinct technical evaluations. Shared run provenance remains unresolved. The figure-only R0082 results contribute zero exact outcome entries.

## S2 audit of author decisions

Of 136 assessed reports, **128** lack documented author confirmation (136 − 8). Eight reports were author-processed, all with final decisions. Four changed status relative to the frozen AI ledger, so the two change fractions are **4/8**. The S2 log has zero paired independent human decisions. Observed agreement and Cohen's kappa are undefined. PRISMA reconciles 46 included, 90 excluded and zero awaiting classification. [S2](supplement_s2_adjudication.md) and [S4 derivations](supplement_evidence_index.md#s2-audit-derivations) record the case-level evidence and calculation.

## Unified coding and scope sensitivity

[Primary technical coding](technical_coding.psv) gives one unit and one modality per included report. The [reconciliation script](../../restart_2026_11_26/synthesis/final_46/reconcile_inputs.py) projects these two columns into [mechanisms.csv](../../restart_2026_11_26/synthesis/final_46/mechanisms.csv). Existing mechanism and evaluation evidence notes in that file preserve the source descriptions. Tables 2 and 5 aggregate these same codes; Table 4 and Figures 2 and 4 use the primary ledger directly.

| Scenario | Reports | Dispatch studies | Studies with retained entries | Retained entries | Matched entries |
| --- | ---: | ---: | ---: | ---: | ---: |
| Final corpus | 46 | 9 | 36 | 98 | 51 |
| Omit R0145 | 45 | 8 | 35 | 96 | 51 |
| Omit R0223 | 45 | 8 | 35 | 96 | 51 |
| Omit both | 44 | 7 | 34 | 94 | 51 |

[Computed scenarios](../../restart_2026_11_26/synthesis/final_46/scope_sensitivity.json) reuse the frozen extraction. Each omission removes one software-simulation dispatch study and two descriptive entries. The official corpus and PRISMA disposition remain as adjudicated. No pooled effect was calculated.
