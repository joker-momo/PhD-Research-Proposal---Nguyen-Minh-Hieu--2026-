# Protocol Amendment 003 — Report Completeness

**Date:** 2026-11-26
**Recorded at:** 2026-11-26T13:03:38+07:00
**Applies to:** Protocol version 0.1 after Amendments 001 and 002
**Timing:** Before final core-database searches and before final human full-text adjudication.

## Change

This amendment clarifies how the existing requirement for a full primary-research report applies to short conference publications.

Page count alone is not an inclusion or exclusion criterion. A short conference paper is eligible only when its accessible report contains enough substantive primary-research information to apply the frozen extraction and appraisal framework. At minimum, the report must identify:

1. the research question, proposed method, architecture, model or algorithm;
2. the evaluated system/model and material assumptions;
3. an evaluation method such as experiment, simulation, emulation, trace-driven evaluation, prototype or mathematical performance study; and
4. results or analyzable evidence that can support at least one review question.

Demo abstracts, poster abstracts, extended abstracts and work-in-progress notices that do not provide this substantive method-and-results content remain excluded under protocol Section 4.2. A venue label such as `short paper` does not automatically exclude a report, and a nominal page count does not automatically make it a full report.

The final selection ledger must record publication type, the substantive-content determination and a page/section locator supporting that determination. When the available report is too limited to decide, the status remains `uncertain` until E-05 human adjudication.

## Reason

The existing protocol includes full peer-reviewed conference papers and excludes posters or abstracts without a full report, but it does not define how to treat short papers consistently. The working corpus contains a two-page demo record (S03) and a three-page conference record (S19). Their different working decisions cannot be justified by page count alone.

## Effect on completed work

- No record, report or study count changes when this amendment is recorded.
- S03 and S19 must be re-audited under the same content/type rule in E-04.
- Every newly retrieved delta report must use the same rule in E-03.
- Existing full-text decisions other than affected short/demo/WIP cases are inherited through D-03 and are not mechanically re-screened.
- The ACM query instruction `Do not include Short-Paper` is not silently changed here. S-01 must verify the official content-type behavior and flag whether that filter would exclude substantively eligible full reports. Any query/filter change after a formal run requires a dated amendment and rerun of the affected search.

## Integrity boundary

This clarification does not convert abstracts into full-text evidence, does not authorize eligibility decisions without readable reports and does not permit abstract-only material to support detailed extraction, appraisal or quantitative synthesis.
