# HK261 Desk Reject revision evidence

Baseline is `7a6675d`. This is an internal revision of the HK261 coursework review. PDF locators below refer to physical pages, counted from 1. The accepted screening ledger and PRISMA denominator remain the basis of this revision. The seven checks below are Codex verifications. Independent human screening and author adjudication remain undocumented.

## Eligibility checks

| ID | Working disposition | Source check and limit |
| --- | --- | --- |
| R0292 | Retain | pp. 3–5, §§4–5 and Fig. 5 describe transfer of active visual tracking state to a receiving UAV for continuation. The evaluated setting is recorded footage and hardware-in-the-loop. This is inference-state transfer, with no demonstrated outdoor two-UAV handoff. |
| R0145 | Retain | pp. 14–17, §§6.1–6.2 compare small, large and hybrid language-model inference in grid scenarios. The edge and cloud are execution roles in the experimental setup. This supports E3 at the request level. |
| R0223 | Retain with E3 boundary flag | pp. 3 and 5, §§3 and 4.2 and Fig. 3 describe onboard Grounding DINO and perception feedback consumed by a shared LLM during joint replanning. This supports the existing decision under the protocol's feature/interface interpretation. Table 2 measures task-level behaviour and does not isolate distributed model execution. This report is sensitive to a stricter model-execution definition. |
| R0113 | Retain with evaluation-setting flag | pp. 7–8 describe graph-based exchange and fusion of representations. pp. 9–13 report simulation and describe hardware-in-the-loop without mapping every reported result to either modality. The [publisher article record](https://ajaccm.com/journal/index.php/ajaccm/article/view/771) matches the PDF title, authors and printed pages 448–464. The [journal policy](https://ajaccm.com/journal/index.php/ajaccm/policies) describes peer review and the published PDF identifies the journal as peer reviewed. The publisher's DOI field gives only `10.64751/`, with no article suffix. Retain `DOI_NOT_FOUND`. These sources establish publication and the stated review policy; article-level review records and independent venue quality assessments were not available. |
| R0081 | Awaiting classification, E7 | pp. 1–2, §§2–3 describe the collaborative detector and a frame-rate comparison. The [official acceptance list](https://www.sigmobile.org/mobisys/2022/accepted-demos.html) confirms the demo track. The [call](https://www.sigmobile.org/mobisys/2022/demos.html) describes selection for audience interest and an extended abstract. The evidence does not establish substantive peer review for this track. |
| R0082 | Awaiting classification, E7 | p. 1 of the local PDF is marked arXiv:2305.15858v1. The [arXiv record](https://arxiv.org/abs/2305.15858) links the IEEE DOI. The conference report identifier alone does not verify that the retained preprint contains the accepted report's method and results. Preserve the distinction until the conference-report text is verified. |
| R0132 | Awaiting classification, E2/E3 | The retained journal-formatted PDF, p. 10 §§8.1–8.2 and p. 20 Table 12, describes simulation and hardware-in-the-loop validation. The scope question remains whether the reported evaluation establishes both a multi-UAV inference workload and the distribution of that workload. Do not treat a repository DOI as evidence of peer review. |

R0116 remains unretrieved. The PRISMA accounting remains 693 identified, 228 duplicates, 465 screened, 328 excluded before retrieval, 137 sought, 136 assessed, 87 full-text exclusions, 3 awaiting classification and 46 included reports representing 46 studies.

Two examples in the [accepted pair evidence](../study_linkage/active_pair_evidence.csv) explain why shared authorship alone did not trigger a merge. R0003 evaluates switching between model sizes for a single stream (PDF pp. 4–5), while R0059 evaluates contention and switching across several concurrent CNN streams (PDF pp. 6–9). R0015 evaluates parallel within-layer assignment (PDF pp. 3 and 5–6) and R0010 evaluates sequential pipeline allocations across a task flow (PDF pp. 2–5).

## Corpus-wide evidence map

[The evidence map](desk_reject_evidence_map.csv) has one row per study. Classification uses the accepted extraction and the evaluated unit, not the publication title. Where the same system combines multiple mechanisms, priority goes to a specialized model block, an explicitly partitioned spatial or within-layer unit, a transferred/fused representation or task state, a sequential stage, or a whole request/stream, in that order for the mechanism in use. The R0063 category refers to the inference interface in the accepted extraction and makes no operational claim about its application.

Evaluation codes describe the documented system-level exercise rather than the computer used to run the evaluator. Standalone processing profiles do not qualify as physical multi-UAV evaluation. Reports with both a software evaluation and a reported physical multi-UAV deployment receive the physical code, even when the timing or failure measurements are software-based. Bench, host emulation and hardware-in-the-loop are grouped, with mixed or unclear attribution carried in the evidence column.

The map links the prior 67 numerical rows to the 25 contributing reports and accounts for the other 21 reports with an explicit coverage status. Empty cells in the prior outcome evidence cannot establish that a report lacked outcomes. For the full outcome inventory, apply one documented post-protocol rule to all 46 reports. Record outcomes by report, experiment and operating point with the exact printed value and unit, metric definition, baseline or absence of a named comparator, measured or simulated conditions, and physical PDF page with table, figure or section. Mark plot-only values and unresolved conditions explicitly. Keep unpaired measures separate from paired comparisons and flag cases that are unsuitable for an aggregate estimate. The historical numbers remain selective and cannot support a coverage estimate for outcomes reported by the primary studies.


## First revision checkpoint

| Check | Status | Evidence |
| --- | --- | --- |
| Corpus and PRISMA | PASS | The evidence map and RQ1 cite the same 46 included study keys. PRISMA arithmetic reconciles, four reconciliation tests pass, and the three pending IDs and R0116 retain their dispositions. |
| Reporting | PASS | The 27 active checklist rows have working evidence links, and PDF page locators are within the 16-page output. The taxonomy and validation counts agree with the map. |
| Build and references | PASS | Tectonic exits successfully with no overfull boxes or undefined references. All 16 pages were rendered and visually checked. The 50 bibliography entries resolve in the PDF, and all 49 DOI link targets match the recorded DOI. |
| Workspace test suite | OPEN | Of 85 hook tests, 84 pass. The context-budget check fails on the inherited 15,000-byte limit. The baseline state file alone already occupies 35,124 bytes. |
| Uniform numeric extraction | OPEN | The 67 retained results represent 25 reports. Uniform re-extraction and verification across all 46 PDFs remain outstanding. |
| Search and retrieval | OPEN | Access to Web of Science Core Collection, systematic citation chaining, and full text for R0116 are unresolved. |
| Human adjudication and declarations | OPEN | Independent human decisions, including for the three pending reports and the E3 boundary case, and verified authorship and submission declarations remain outstanding. |
