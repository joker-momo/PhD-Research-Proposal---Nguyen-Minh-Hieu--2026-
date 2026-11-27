# Figure, table and equation evidence

Generated from Supplement S4. PDF pages refer to the archived comparison draft.
For commands and input files by item, see [README.md](README.md).

## Figures, tables, and equations

| Item | Source, inputs and reproduction rule |
| --- | --- |
| Figure 1 `fig:flow` (PDF p. 6) | [PRISMA reconciler](sources/restart_2026_11_26/prisma/reconcile.py) takes the locked records and decisions plus [the S2 author adjudication log](sources/manuscript/sn_computer_science/human_adjudication_log.csv), fills [the TikZ template](sources/restart_2026_11_26/prisma/flow_template.tex) and writes [counts](sources/restart_2026_11_26/prisma/prisma_counts.json) and [standalone source](sources/restart_2026_11_26/prisma/prisma_flow.tex). Compile the latter to rebuild the embedded [figure PDF](sources/manuscript/sn_computer_science/prisma_flow.pdf). Arithmetic is raw − duplicates = screened, screened − title/abstract exclusions = sought, sought − unretrieved = assessed, assessed = full-text exclusions + pending + included reports. |
| Figure 2 `fig:macro` (PDF p. 8) | [TikZ](sources/manuscript/sn_computer_science/technical_overview_figure.tex) uses [generated counts](sources/manuscript/sn_computer_science/technical_macros.tex). The [generator](sources/manuscript/sn_computer_science/build_technical_survey.py) counts each report once per panel, using the citation year and BibTeX venue type in panel A and the family, optimizer, and evaluation columns of [primary coding](sources/manuscript/sn_computer_science/technical_coding.psv) in the remaining panels. Unscaled TikZ segment height in panel A is 0.16 cm × count, with conference at the bottom and journal stacked above. Horizontal bar length in panels B–D is 0.115 cm × count. The enclosing LaTeX resize applies one scale to the figure. Each panel totals 46. |
| Figure 3 `fig:topologies` (PDF p. 9) | [TikZ](sources/manuscript/sn_computer_science/technical_architecture_figure.tex) illustrates the three analyst-defined topology categories from the coding ledger and Table 3. Representative mappings are peer transport R0010/R0121, a head–worker hierarchy R0014/R0118, and tiered processing R0001/R0080. Arrows represent logical relationships. They carry no measured distance, time, or scale. |
| Figure 4 `fig:taxonomy` (PDF p. 10) | [TikZ](sources/manuscript/sn_computer_science/technical_taxonomy_figure.tex) uses [generated counts](sources/manuscript/sn_computer_science/technical_macros.tex) for topology, unit, optimizer and resilience. A leaf count is the number of distinct reports assigned its label. Each dimension has its own denominator of 46. |
| Figure 5 `fig:appraisalbar` (PDF p. 22) | [TikZ](sources/manuscript/sn_computer_science/technical_appraisal_figure.tex) draws [generated bar inputs](sources/manuscript/sn_computer_science/technical_appraisal_bars.tex) from the accepted summary. Segment width in percentage points is 100 × status count / 46. The endpoints are cumulative percentages for Yes, Partial, and Not reported, followed by 100% for any No votes. The corresponding Table 7 percentage is 100 × Yes count / 46 rounded to one decimal. |
| Table 1 `tab:related` (PDF p. 2) | [LaTeX](sources/manuscript/sn_computer_science/main.tex#L33) and [bibliography](sources/manuscript/sn_computer_science/references.bib). Row-level sources are listed below. |
| Table 3 `tab:architecture` (PDF p. 11) | [Generated LaTeX](sources/manuscript/sn_computer_science/technical_architecture.tex) uses the 46-study characteristics and coding ledgers. The report citation joins each cell back to architecture, model and partition fields in the accepted extraction and locator inventory. |
| Table 4 `tab:evaluation` (PDF p. 17) | [Generated LaTeX](sources/manuscript/sn_computer_science/technical_evaluation.tex) uses the same 46 IDs and joins evaluation settings, connectivity, mobility, faults and continuity cells to the original report through the extraction and locator inventory. |
| Table 6 `tab:outcomes` (PDF p. 21) | [LaTeX](sources/manuscript/sn_computer_science/main.tex#L260) transcribes checked values in their reported units and conditions. The row map below identifies the accepted ledger record and the original page/table. |
| Table 2 `tab:settings` (PDF p. 7) | [Generated LaTeX](sources/manuscript/sn_computer_science/editorial_mechanism_setting.tex) and [generator](sources/manuscript/sn_computer_science/build_editorial_evidence.py) count report IDs grouped by primary mechanism and strongest evaluation setting in the [coded input](sources/restart_2026_11_26/synthesis/final_46/mechanisms.csv). Each report contributes to exactly one cell. The two grouping fields are projected from the [primary coding ledger](sources/manuscript/sn_computer_science/technical_coding.psv). Source descriptions are retained in the coded input. |
| Table 5 `tab:coverage` (PDF p. 21) | [Generated LaTeX](sources/manuscript/sn_computer_science/editorial_outcome_coverage.tex) and [generator](sources/manuscript/sn_computer_science/build_editorial_evidence.py) join the [primary coding](sources/restart_2026_11_26/synthesis/final_46/mechanisms.csv) and [report coverage](sources/restart_2026_11_26/synthesis/final_46/report_coverage.csv) by report ID. Study counts group by status and entries sum matched and descriptive rows in the [outcome ledger](sources/restart_2026_11_26/synthesis/final_46/outcomes.csv). [Rule and gap definitions](sources/restart_2026_11_26/extraction/rq5_uniform/rule.md). |
| Table 7 `tab:appraisal` (PDF p. 22) | [Generated rows](sources/manuscript/sn_computer_science/technical_appraisal.tex) use the accepted summary. Domain counts and percentages share the same source as Figure 5. Use the rationale matrix for individual ratings or missing reporting evidence. |
| Table 8 `tab:adjudication_audit` (PDF p. 25) | [Generated LaTeX](sources/manuscript/sn_computer_science/adjudication_audit_table.tex) and [JSON](sources/manuscript/sn_computer_science/audit_summary.json) come from the [S2 audit script](sources/manuscript/sn_computer_science/audit_adjudication.py), the [136-row S2 log](sources/manuscript/sn_computer_science/human_adjudication_log.csv), and the [PRISMA ledger](sources/restart_2026_11_26/prisma/prisma_counts.json). Count final decisions and confirmed deferrals together for author coverage. The change numerator counts only final decisions that differ from the frozen AI disposition. |
| Eq. 1 `eq:objective` (PDF p. 10) | [LaTeX](sources/manuscript/sn_computer_science/main.tex#L169). This review's synthesized objective defines a feasible decision tuple and weights latency, energy, quality and recovery cost across scenarios. The negative quality sign suits minimization. Weights carry unit conversions and recovery cost must have a distinct boundary from end-to-end delay unless deliberate weighting is explained. See R0001/R0006/R0058/R0080 and RQ2 for examples of subproblems. The review did not fit weights or compute a pooled objective. |
| Eq. 2 `eq:link` (PDF p. 10) | [LaTeX](sources/manuscript/sn_computer_science/main.tex#L179). The serialization duration follows from bits divided by effective bits per second. Queueing and protocol time are additive for the stated non-overlapping accounting boundary. R0121 and R0092 provide context for link accounting, with exact assumptions in their extraction. This equation is a schematic decomposition. |
| Eq. 3 `eq:recovery` (PDF p. 23) | [LaTeX](sources/manuscript/sn_computer_science/main.tex#L319). Let t0 be event onset, t1 detection, t2 the valid plan, t3 transfer complete and t4 the first correct resumed output. The sum of consecutive differences telescopes to t4 − t0. With overlapping phases, record wall time and individual intervals. R0038/R0062/R0014 are motivating examples. This is a proposed measurement definition. No recovery values were computed with it. |

### Finding an individual cell in the architecture and evaluation tables

In the included input index, take the row's report ID to the matching
record in the accepted extraction. The keys below describe the baseline
extraction under `fields`. Supplemental records use compact keys such as
`architecture`, `workload`, `evaluation`, and `mobility_continuity`. Both
schemas are resolved in the S4 row map above.

| Cells | Extraction keys and analyst input |
| --- | --- |
| architecture table topology | `uav_architecture_role_and_topology` and `topology` in primary coding. |
| architecture table workload | `inference_model_task_and_dataset` and `baselines_and_workloads`. |
| architecture table partition / dispatch | `partition_and_assignment` and `unit` in primary coding. |
| architecture table decisions, objective and solver | `decision_variables_objectives_constraints_and_solver`, supplemented by `partition_and_assignment` and `compute_and_radio`. |
| evaluation table modality and platform | `evaluation_platform_simulator_hardware_and_traces` and `evaluation` in primary coding. |
| evaluation table channel, mobility, disruption, action and evidence class | `mobility_channel_intermittency_failure_and_recovery`, supplemented by `compute_and_radio` and `evaluation_platform_simulator_hardware_and_traces`. `resilience` in primary coding supplies the analyst's evidence class. |

## Related-survey matrix source locators

| Row | Source location and recorded basis |
| --- | --- |
| McEnroe et al. | [University of Oulu author record](https://oulurepo.oulu.fi/handle/10024/32545), Abstract. Names edge AI, UAV functions and civilian applications. [Published DOI](https://doi.org/10.1109/JIOT.2022.3176400). |
| Ren et al. | [Springer publisher record](https://link.springer.com/article/10.1007/s11633-022-1391-7), Abstract. Defines collaborative DNN inference across cloud, edge and end devices and a four-paradigm organization. |
| Xia et al. | [Author preprint](https://arxiv.org/abs/2210.06679), Abstract. Describes resource-management taxonomy, collaborations and wireless communication models. [Published DOI](https://doi.org/10.1145/3626566) and [issue catalog](https://findit.library.nd.edu/EdsRecord/edb%2C173383387?sid=2265930) distinguish the 2024 issue from earlier versions. |
| Ning et al. | [Author institution record](https://researchportal.hkust.edu.hk/en/publications/mobile-edge-computing-and-machine-learning-in-the-internet-of-unm/), Abstract and publication metadata. Records the topic and 2023 issue year. [Published DOI](https://doi.org/10.1145/3604933). |
| Cao et al. | [IEEE publisher record](https://xplorestaging.ieee.org/document/10516683), Abstract and Sections III–V. Covers networking, collaboration and cooperative task assignment. |
| Wang et al. | [IEEE publisher record](https://xplorestaging.ieee.org/document/10508191/metrics), Abstract and Section I. Covers training, inference and updating with partitioning among enabling techniques. |
| Hao et al. | [Publisher-deposited abstract](https://api.crossref.org/works/10.1145/3786145), JSON field `message.abstract`. Gives mathematical modeling, optimization, granularity and toolchains. [Publication history](https://crossmark.crossref.org/dialog?cm_version=v2.0&doi=10.1145%2F3786145&domain=dl.acm.org) records the 2026 issue. |
| This review | Sections 2–5, accepted protocol, PRISMA counts, and coded primary studies. |

Matrix codes apply to the cited scope passages. Unestablished coverage is
marked with a question mark. A check denotes explicit, substantive coverage
and a triangle denotes adjacent or limited documented coverage. The positive
and partial marks are traced by row below. S = systematic search, selection
and synthesis, U = multi-UAV architectures, P = inference partitioning and
assignment, J = joint mobility/radio decisions, L = LLM/MoE, F = failure and
recovery of inference, and A = engineering appraisal.

| Survey | Basis for marked coverage |
| --- | --- |
| McEnroe | U is adjacent. The abstract describes edge AI for UAV functions and applications. |
| Ren | P is direct. The publisher abstract centers on collaborative inference and partition-oriented execution paradigms. F is direct in §5.2.3 and Table 5 of the [author full text](https://arxiv.org/html/2207.07812v1), which classify failure-resilient distributed inference. |
| Xia | U and J are adjacent. The abstract describes UAV roles and device collaboration, resource management and wireless models. The author text organizes communication models and resource allocation, providing context for the joint decision axis. |
| Ning | U and J are adjacent. The abstract is about the Internet of UAVs and covers resource allocation and trajectory design as related topics. |
| Cao | U is direct. The survey centers on swarm networking and collaboration. J is adjacent given §III–V coverage of network constraints and task assignment. |
| Wang | P is direct. The abstract and §I describe model partitioning among enabling methods for inference across computing tiers. |
| Hao | P is direct. The [ACM article](https://doi.org/10.1145/3786145), Abstract and §3, center on DNN partitioning and its solution space. |
| This review | S follows the archived protocol and PRISMA flow. U and P follow eligibility and the two detailed study tables. J is limited to documented co-design examples (R0006 p. 4, R0118 pp. 5–8); L is limited to selected settings (R0074, R0110 and R0118). F and A are direct across the continuity coding and ten-domain engineering appraisal. |

## Numerical contrast row map

The report ID plus extraction key identifies a row of the outcome ledger.
Inspect the original locator for the comparator, condition and uncertainty.

| Displayed contrast | Accepted key | Original physical location |
| --- | --- | --- |
| R0080 top-1 accuracy | `quantity:1` | p. 5, Table I, ResNet-18/101, 100 Mb/s, Ours and GSUP, accuracy. |
| R0080 end-to-end latency | `quantity:2` | p. 5, same block, latency. |
| R0092 deadline success | `quantity:1` and R0092 erratum | p. 13, Table V, VGG-16, DDCI and Comm-Min, deadline satisfaction with SD. |
| R0075 computation and communication | `quantity:1` | p. 10, Table III, CIDER and Full Final Exit, combined column. |
| R0074 Orion vs Cloud-Edge-Opt | `quantity:1` | p. 16, Section 4.2 and Fig. 4, Llama-2 7B prefill. |
| R0074 Orion vs Edge-Solo | `quantity:1` | p. 16, same setting, second comparator. |
| R0014 20 vs four devices | `quantity:1` | p. 11, §VIII.B, first-to-100th task timing definition and high-resolution input; p. 12, Table III, ResNet152, ASAP columns for 20 and four nodes. |
| R0062 three vs four UAVs | `quantity:2`, `quantity:1` | p. 6, Effect of UAV Unavailability, first paragraph. |
| R0125 four vs one worker | `quantity:1` | p. 3, Table I (four threads) and Section IV.B. |
