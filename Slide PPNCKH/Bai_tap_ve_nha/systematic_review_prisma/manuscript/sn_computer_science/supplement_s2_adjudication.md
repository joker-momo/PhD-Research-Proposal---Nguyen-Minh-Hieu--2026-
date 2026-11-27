# S2. Full-text eligibility and human adjudication

The [136-report review log](human_adjudication_log.csv) carries the existing
AI-assisted decision, initial evidence, the original PDF path and SHA-256.
It separates the initial assessment, author notes and final adjudication.
The original decisions reconcile to 46 inclusions, 87 exclusions and three
awaiting classification. R0116 was not retrieved and therefore has no
full-text review row. The [exclusions ledger](supplement_fulltext_exclusions.csv)
preserves the 87 baseline exclusions and their primary reasons. The author
confirmed three additional exclusions, R0081 (E7), R0113 (E3) and R0132 (E3), on
27 November 2026. The
[active PRISMA ledger](../../restart_2026_11_26/prisma/prisma_counts.json)
combines the screening and author decisions. The current eligibility set
contains 44 included, 90 excluded and two awaiting classification.
The author confirmed deferrals for R0082 (E7) and R0292 (E7).
S2 records six final decisions (three inclusions and three exclusions) and
two confirmed deferrals. Eight of 136 reports have author confirmation.
The prior 46-study comparison PDF, extraction, appraisal and synthesis
are an earlier snapshot pending reconciliation to the current set.
Independent duplicate human screening remains undocumented.

The [audit report](audit_summary.json) and [LaTeX summary](adjudication_audit_table.tex)
report the current S2 coverage and reconciled PRISMA counts. Run
`python3 -B audit_adjudication.py` from this directory to regenerate both.
Add `--check` to verify the saved outputs. The count of changed decisions uses
only documented final decisions. Agreement statistics require paired reviewer
entries. Confidence intervals require a documented sampling design.

## Priority records for the author

PDF pages are physical, one-based. Look up the local original and checksum
by report ID in the review log. Use the frozen eligibility requirements
and record the original page and criterion behind each decision.

| Report | Source and finding | Author disposition or proposed check |
| --- | --- | --- |
| R0081, Sun et al., IDEA | Original pp. 1–2, §§1–3 describes model splitting and prototype results. The [MobiSys accepted demos](https://www.sigmobile.org/mobisys/2022/accepted-demos.html) list the report. The [Call for Demos](https://www.sigmobile.org/mobisys/2022/demos.html) specifies a demo extended abstract and selection for audience interest. | **Author confirmed EXCLUDE (E7), 27 November 2026.** The official ACM demo category and its extended-abstract format establish the publication type. |
| R0082, LLHR | The [conference DOI](https://doi.org/10.1109/WCNC55385.2023.10118908) identifies the publication. The retained file is [arXiv:2305.15858v1](https://arxiv.org/abs/2305.15858), as shown on p. 1. The arXiv page links the conference DOI. This verifies the bibliographic linkage. Its §§I and IV (pp. 2 and 5) support a scope candidate. The IEEE version of record was unavailable in the current public-access check. | **Author reaffirmed AWAITING_CLASSIFICATION (E7), 27 November 2026,** after the [targeted source recheck](../../restart_2026_11_26/integrity/pending_three_followup/review.md). Reassess when an authorized IEEE proceedings copy is available for comparison. The preprint stays outside the primary synthesis while E7 is pending. |
| R0132 | Original p. 10, §§8.1–8.2, and pp. 17–20, including Table 12, describe system-level simulation, HIL replay and component metrics. They do not tie a specific evaluated multi-UAV workload to shared neural inference across those UAVs. The [DataCite deposit record](https://api.datacite.org/dois/10.5281/zenodo.20445205) links a separate version DOI ending 20445206 and journal ISSN 3051-3820. This establishes publication metadata, while E7 remains to be confirmed. | **Author confirmed EXCLUDE (E3), 27 November 2026.** Figures 12–13 place Transformer fusion at the edge and show the UAV in a sensing role. Table 12 reports HIL and component benchmarks. These do not establish an evaluated neural workload executed collaboratively within the multi-UAV system. E3 is the sole primary exclusion code. |
| R0223, Wang and Deng | Physical pp. 3–5 and 7, §§3.2 and 4.2, Figs. 3 and 7, Table 2. | **Author confirmed INCLUDE.** The system-level experiment evaluates configurations of server and UAV neural model orchestration. |
| R0113, Hemasri and Reddy | [Original PDF](../../restart_2026_11_26/fulltext_retrieval/pdf/R0113.pdf), physical pp. 7–9 and 12–13 (printed pp. 454–456 and 459–460), including the methodology flow chart and Table 4. | **Author confirmed EXCLUDE (E3), 27 November 2026.** The paper describes inter-UAV embedding exchange and reports an ablation with graph coordination. The cited sections do not establish which inference operation uses a received embedding in the evaluated configuration. E3 is the sole primary exclusion code. |
| R0145, Xiao et al. | Physical pp. 6 and 17–18, §§3.1 and 6.2, Figs. 2 and 7–10. | **Author confirmed INCLUDE.** Whole LLM requests are assigned locally or to cloud according to connectivity. The study evaluates three assignment schemes. |
| R0292, Kim et al. | Physical pp. 3–5, §§4–5.2, Fig. 3 and Table 3, and the DroNet workshop documentation. | **Author confirmed AWAITING_CLASSIFICATION (E7).** The handoff and HIL evidence were verified. The track or report still requires authoritative peer-review evidence. |
| R0001, Dong et al. | Physical pp. 2–3, §§II.A–B and III.A, Figs. 2–3, and the official ICWS WIP programme and author policy. | **Author confirmed INCLUDE.** Evaluated DNN partitioning and a substantive peer-reviewed WIP report. |
| R0121 and R0125 | Transport analysis at R0121 pp. 4–8 §§3–4 relies on a reference payload, and the detector in R0125 pp. 2–3 §§II–IV was measured on workstations. | Check whether the explicit multi-UAV inference workload and evaluation claims jointly satisfy E2–E4. Preserve analytical and workstation boundaries if retained. |

The [five-record author review report](../../restart_2026_11_26/integrity/borderline_author_review/report.md)
contains the original sources and the evidence used for these decisions.

The historical [46-row evidence map](../../restart_2026_11_26/synthesis/desk_reject_evidence_map.csv)
locates the evaluated assignment and evaluation for every included report.
It is a triage aid for the full author audit.

## How to complete and summarize the review

For each reviewed record, enter the categorical decision, date, reviewer
identifier and exact supporting original PDF location. Reviewers record
their independent decisions before consulting the prior decision or each
other. A reviewer may work from a copy with the prior decision and notes
hidden. Preserve both initial decisions when recording a consensus outcome.
Use one primary frozen eligibility code for exclusion. Add source-version
and access details if a proceedings copy could not be retrieved. For data
verification, use the S3 outcome IDs, technical-table field keys and D01–D10
appraisal keys to record source-page checks and corrections.

After sign-off, report coverage for each reviewer and for the paired subset.
For paired, independent categorical decisions, observed agreement is the
number of matching decisions divided by the number of paired records.
Expected agreement is the sum across categories of the product of the two
reviewers' marginal fractions. Cohen's kappa is (observed − expected) /
(1 − expected), undefined if expected agreement is 1. State the paired
sample and how it was selected. A separate comparison with the baseline can
count changed decisions using final human decisions as the denominator.
A single reviewer cannot yield inter-human agreement. Leave statistics
unreported until the necessary observations exist, then reconcile PRISMA,
appraisal, coding, and outcome denominators from the signed decisions.
