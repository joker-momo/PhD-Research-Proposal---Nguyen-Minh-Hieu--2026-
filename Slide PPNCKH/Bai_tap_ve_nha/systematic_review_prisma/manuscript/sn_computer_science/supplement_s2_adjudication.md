# S2. Full-text eligibility and human adjudication

The [136-report review log](human_adjudication_log.csv) carries the existing
AI-assisted decision, initial evidence, the original PDF path and SHA-256.
It separates the initial assessment, author notes and final adjudication.
The original decisions reconcile to 46 inclusions, 87 exclusions and three
awaiting classification. R0116 was not retrieved and therefore has no
full-text review row. The [exclusions ledger](supplement_fulltext_exclusions.csv)
preserves the 87 baseline exclusions and their primary reasons. The author
confirmed two additional exclusions, R0081 (E7) and R0132 (E3), on
27 November 2026. The
[active PRISMA ledger](../../restart_2026_11_26/prisma/prisma_counts.json)
combines both sources: 46 inclusions, 89 exclusions and one awaiting
classification (R0082). The author confirmed on 27 November 2026
that R0082 remains pending under E7. S2 records two final exclusions and one
confirmed deferral.
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
| R0082, LLHR | The [conference DOI](https://doi.org/10.1109/WCNC55385.2023.10118908) identifies the publication. The retained file is [arXiv:2305.15858v1](https://arxiv.org/abs/2305.15858), as shown on p. 1. The arXiv page links the conference DOI. This verifies the bibliographic linkage. Its §§I and IV (pp. 2 and 5) support a scope candidate. The IEEE version of record was unavailable in the current public-access check. | **Author confirmed AWAITING_CLASSIFICATION (E7), 27 November 2026.** Reassess when an authorized IEEE proceedings copy is available for comparison. The preprint stays outside the primary synthesis while E7 is pending. |
| R0132 | Original p. 10, §§8.1–8.2, and pp. 17–20, including Table 12, describe system-level simulation, HIL replay and component metrics. They do not tie a specific evaluated multi-UAV workload to shared neural inference across those UAVs. The [DataCite deposit record](https://api.datacite.org/dois/10.5281/zenodo.20445205) links a separate version DOI ending 20445206 and journal ISSN 3051-3820. This establishes publication metadata, while E7 remains to be confirmed. | **Author confirmed EXCLUDE (E3), 27 November 2026.** Figures 12–13 place Transformer fusion at the edge and show the UAV in a sensing role. Table 12 reports HIL and component benchmarks. These do not establish an evaluated neural workload executed collaboratively within the multi-UAV system. E3 is the sole primary exclusion code. |
| R0223, Wang and Deng | Original pp. 2–4 §§2–3 describes task-graph and perception feedback. Pp. 5–7 §4 and Table 2 measure scenario response and coordination. Those measures do not isolate assignment, transfer or fusion of a neural inference workload. | Proposed exclusion under E3 if author review confirms that coordinated planning is the evaluated unit. |
| R0113, Hemasri and Reddy | Original p. 1 identifies the venue, and pp. 9–13 describe simulation and HIL without consistently locating which setting produced the printed outcomes. The [ISSN record](https://portal.issn.org/resource/ISSN/3069-0102) confirms 3069-0102. The [publisher's About page](https://ajaccm.com/journal/index.php/ajaccm/about) states that the journal uses peer review, lists discovery services and gives a journal-level identifier. The [article landing page](https://ajaccm.com/journal/index.php/ajaccm/article/view/771) confirms the title and both authors, but its citation DOI contains only the prefix. An article-level DOI or authoritative Scopus/WoS coverage was not verified. | Recheck E3 and E7 using the exact article and issue, and separate venue eligibility from unusable outcome context. The locked protocol does not require Scopus/WoS coverage or an article DOI. A new index requirement would require a documented amendment and consistent rescreening of all reports. |
| R0145, Xiao et al. | Original pp. 4–6 and 11–14 describe edge/cloud model roles, and p. 15 Fig. 4 plus p. 16 identify stand-alone model times. The reported component timings do not establish matched orchestration performance for the multi-UAV request workload. | Retain as whole-request orchestration only if the author confirms an evaluated cross-node assignment of identifiable neural calls or state distinct from trajectory generation alone. Otherwise propose E3. |
| R0292, Kim et al. | Original pp. 3–6, §§4–5, describe transfer of tracker state across UAV roles and evaluate tracking continuity with recorded video and hardware in the loop. | Proposed retention under E3 as evaluated stateful inference handoff, with its HIL setting stated. |
| R0001, Dong et al. | Original p. 2 §II.A specifies the partition model and p. 3 §III shows comparative simulated results. The [IEEE conference policies](https://services.conferences.computer.org/2026/info-for-authors/) distinguish work-in-progress and research tracks and describe manuscript review. | Proposed retention as a substantive reviewed short research report, applying the same criteria as to longer papers. |
| R0121 and R0125 | Transport analysis at R0121 pp. 4–8 §§3–4 relies on a reference payload, and the detector in R0125 pp. 2–3 §§II–IV was measured on workstations. | Check whether the explicit multi-UAV inference workload and evaluation claims jointly satisfy E2–E4. Preserve analytical and workstation boundaries if retained. |

The [46-row evidence map](../../restart_2026_11_26/synthesis/desk_reject_evidence_map.csv)
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
