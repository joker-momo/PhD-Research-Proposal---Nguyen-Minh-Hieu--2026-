# S4. Evidence and reproduction record for the IEEE manuscript

Page references are one-based physical pages of the [IEEE journal PDF](main.pdf). LaTeX labels and links refer to the IEEE sources. Shared input ledgers retain their original report IDs and PDF locators. Figure labels and tables use the same Times Roman family as the IEEE body text.

| Evidence | Source |
| --- | --- |
| Search and eligibility | [S1](../sn_computer_science/supplement_search_strategies.md), [S2](../sn_computer_science/supplement_s2_adjudication.md), [IEEE PRISMA checklist](prisma_2020_checklist.md) and [frozen counts](../../restart_2026_11_26/prisma/prisma_counts.json). |
| Per-study source locators | [46-study table row map](../sn_computer_science/s4_study_row_sources.csv), [report identity and checksums](../../restart_2026_11_26/synthesis/final_46/synthesis_input_index.csv) and [study characteristics](../../restart_2026_11_26/synthesis/final_46/study_characteristics.csv). |
| Appraisal and numerical synthesis | [S3](../sn_computer_science/supplement_s3.md), [appraisal rationale](../../restart_2026_11_26/synthesis/final_46/appraisal_rationale.csv), [outcomes](../../restart_2026_11_26/synthesis/final_46/outcomes.csv) and [claim source matrix](../../restart_2026_11_26/synthesis/final_46/claim_source_matrix.csv). |
| Rebuild the IEEE PDF | [Build instructions](README.md). |

Publisher PDFs are identified by report ID and physical locator. Access to the original reports is subject to their distribution terms.

## Figures, tables, and equations

| Item | Source, inputs and reproduction rule |
| --- | --- |
| Figure 1 `fig:flow` (PDF p. 4) | [PRISMA reconciler](../../restart_2026_11_26/prisma/reconcile.py) takes the locked records and decisions plus [the S2 author adjudication log](../sn_computer_science/human_adjudication_log.csv), fills [the TikZ template](../../restart_2026_11_26/prisma/flow_template.tex) and writes [counts](../../restart_2026_11_26/prisma/prisma_counts.json) and [standalone source](../../restart_2026_11_26/prisma/prisma_flow.tex). The [IEEE layout source](prisma_flow_ieee.tex) preserves the reconciled text, counts and arrows. From the IEEE source directory, run `pdflatex -jobname=prisma_flow prisma_flow_ieee.tex` to rebuild the embedded [figure PDF](prisma_flow.pdf). Arithmetic is raw − duplicates = screened, screened − title/abstract exclusions = sought, sought − unretrieved = assessed, assessed = full-text exclusions + pending + included reports. |
| Figure 2 `fig:macro` (PDF p. 5) | [TikZ](technical_overview_figure.tex) uses [generated counts](technical_macros.tex). The [generator](../sn_computer_science/build_technical_survey.py) counts each report once per panel, using the citation year and BibTeX venue type in panel A and the family, optimizer, and evaluation columns of [primary coding](../sn_computer_science/technical_coding.psv) in the remaining panels. Unscaled TikZ segment height in panel A is 0.16 cm × count, with conference at the bottom and journal stacked above. Horizontal bar length in panels B–D is 0.115 cm × count. Panel A shows count ticks and marks 2026 with an asterisk linked to the 26 November 2026 search cutoff. Panels B–D start at a visible zero baseline and share the same count scale. The enclosing LaTeX resize applies one scale to the figure. Each panel counts 46 studies, as stated in the PDF caption. |
| Figure 3 `fig:topologies` (PDF p. 5) | [TikZ](technical_architecture_figure.tex) illustrates the three analyst-defined topology categories from the coding ledger and Table III. Representative mappings are peer transport R0010/R0121, a head–worker hierarchy R0014/R0118, and tiered processing R0001/R0080. Panel B uses one UAV head for task dispatch and result merging. The PDF caption defines solid arrows as data flow, including tasks sent to workers and results returned to the head. Panel C illustrates the route that uses the cloud. Arrows represent logical relationships. They carry no measured distance, time, or scale. |
| Figure 4 `fig:taxonomy` (PDF p. 7) | [TikZ](technical_taxonomy_figure.tex) uses [generated counts](technical_macros.tex) for topology, unit, optimizer and continuity, derived by [the generator](../sn_computer_science/build_technical_survey.py) from [primary coding](../sn_computer_science/technical_coding.psv). The four panels show the dimensions in a two-by-two grid. Each row counts distinct report IDs assigned to that label. Each dimension totals 46. R0019 changes from `proactive` to `analytic`, moving one from planned reassignment (4 → 3) to modeled reliability or stress (4 → 5). See the [S3 continuity correction](../sn_computer_science/supplement_s3.md#continuity-correction-for-r0019). |
| Figure 5 `fig:appraisalbar` (PDF p. 15) | [TikZ](technical_appraisal_figure.tex) draws [generated bar inputs](technical_appraisal_bars.tex) from the accepted summary. Segment width in percentage points is 100 × status count / 46. The endpoints are cumulative percentages for Yes, Partial, and Not reported, followed by 100% for any No votes. Hatching identifies Not reported. The Artifact availability bar labels its Not reported count directly from the same input. The corresponding Table VII percentage is 100 × Yes count / 46 rounded to one decimal. |
| Table I `tab:related` (PDF p. 1) | [LaTeX](main.tex#L38) and [bibliography](references.bib). Row-level sources are listed below. |
| Table III `tab:architecture` (PDF pp. 8–9) | [Generated LaTeX](technical_architecture.tex) uses the 46-study characteristics and coding ledgers. The report citation joins each cell back to architecture, model and partition fields in the accepted extraction and locator inventory. |
| Table IV `tab:evaluation` (PDF pp. 11–12) | [Generated LaTeX](technical_evaluation.tex) uses the same 46 IDs and joins evaluation settings, connectivity, mobility, faults and continuity cells to the original report through the extraction and locator inventory. |
| Table VI `tab:outcomes` (PDF p. 14) | [LaTeX](main.tex#L269) transcribes checked values in their reported units and conditions. The row map below identifies the accepted ledger record and the original page/table. |
| Table II `tab:settings` (PDF p. 6) | [Generated LaTeX](editorial_mechanism_setting.tex) and [generator](../sn_computer_science/build_editorial_evidence.py) count report IDs grouped by primary mechanism and strongest evaluation setting in the [coded input](../../restart_2026_11_26/synthesis/final_46/mechanisms.csv). Each report contributes to exactly one cell. The two grouping fields are projected from the [primary coding ledger](../sn_computer_science/technical_coding.psv). Source descriptions are retained in the coded input. |
| Table V `tab:coverage` (PDF p. 14) | [Generated LaTeX](editorial_outcome_coverage.tex) and [generator](../sn_computer_science/build_editorial_evidence.py) join the [primary coding](../../restart_2026_11_26/synthesis/final_46/mechanisms.csv) and [report coverage](../../restart_2026_11_26/synthesis/final_46/report_coverage.csv) by report ID. Study counts group by status and entries sum matched and descriptive rows in the [outcome ledger](../../restart_2026_11_26/synthesis/final_46/outcomes.csv). [Rule and gap definitions](../../restart_2026_11_26/extraction/rq5_uniform/rule.md). |
| Table VII `tab:appraisal` (PDF p. 14) | [Generated rows](technical_appraisal.tex) use the accepted summary. Domain counts and percentages share the same source as Figure 5. Use the rationale matrix for individual ratings or missing reporting evidence. |
| Table VIII `tab:adjudication_audit` (PDF p. 15) | The [IEEE table](adjudication_audit_table.tex) summarizes the [frozen audit JSON](../sn_computer_science/audit_summary.json). The audit derives its counts from the [S2 audit script](../sn_computer_science/audit_adjudication.py), the [136-row S2 log](../sn_computer_science/human_adjudication_log.csv), and the [PRISMA ledger](../../restart_2026_11_26/prisma/prisma_counts.json). The lead reviewer made the final eligibility decisions for all 136 assessed reports. The author's confirmation covers the full [final eligibility register](../sn_computer_science/supplement_s2_eligibility.csv). Count separate final decisions and confirmed deferrals for the documented subset. The change numerator counts final decisions that differ from the AI-assisted initial classification. With zero confirmed deferrals, the two audit fractions equal 4/10, so the PDF shows one status-change row. The JSON retains both calculations. |
| Eq. 1 `eq:objective` (PDF p. 6) | [LaTeX](main.tex#L181). This review's synthesized objective defines a feasible decision tuple and weights latency, energy, quality and recovery cost across scenarios. The negative quality sign suits minimization. Weights carry unit conversions and recovery cost must have a distinct boundary from end-to-end delay unless deliberate weighting is explained. See R0001/R0006/R0058/R0080 and RQ2 for examples of subproblems. The review did not fit weights or compute a pooled objective. |
| Eq. 2 `eq:link` (PDF p. 6) | [LaTeX](main.tex#L190). The serialization duration follows from bits divided by effective bits per second. Queueing and protocol time are additive for the stated non-overlapping accounting boundary. R0121 and R0092 provide context for link accounting, with exact assumptions in their extraction. This equation is a schematic decomposition. |
| Eq. 3 `eq:recovery` (PDF p. 13) | [LaTeX](main.tex#L326). Let t0 be event onset, t1 detection, t2 the valid plan, t3 transfer complete and t4 the first correct resumed output. The sum of consecutive differences telescopes to t4 − t0. With overlapping phases, record wall time and individual intervals. R0038/R0062/R0014 are motivating examples. This is a proposed measurement definition. No recovery values were computed with it. |

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
| Ning et al. | [Author institution record](https://researchportal.hkust.edu.hk/en/publications/mobile-edge-computing-and-machine-learning-in-the-internet-of-unm/), Abstract and publication metadata. Describes the topic. [ACM metadata deposited with Crossref](https://api.crossref.org/works/10.1145/3604933) lists online publication in 2023 and the 2024 issue cited as reference [13]. |
| Cao et al. | [IEEE publisher record](https://xplorestaging.ieee.org/document/10516683), Abstract and Sections III–V. Covers networking, collaboration and cooperative task assignment. |
| Wang et al. | [IEEE publisher record](https://xplorestaging.ieee.org/document/10508191/metrics), Abstract and Section I. Covers training, inference and updating with partitioning among enabling techniques. |
| Hao et al. | [Publisher-deposited abstract](https://api.crossref.org/works/10.1145/3786145), JSON field `message.abstract`. Gives mathematical modeling, optimization, granularity and toolchains. [Publication history](https://crossmark.crossref.org/dialog?cm_version=v2.0&doi=10.1145%2F3786145&domain=dl.acm.org) records the 2026 issue. |
| This review | Sections II–V, accepted protocol, PRISMA counts, and coded primary studies. |

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
| R0125 four four-thread workers vs one four-thread worker | `quantity:1` | p. 3, Table I (four threads) and Section IV.B. |

## IEEE manuscript claims with bounded evidence

| IEEE location | Source and evidence boundary |
| --- | --- |
| §II-C, p. 2 (R0082/R0019 linkage) | [Source review](../../restart_2026_11_26/synthesis/final_46/r0082_review.md). R0019 §IV, physical p. 14 (printed 8198), Figs. 16–17. Shared-run provenance remains unresolved. |
| Reference 22, p. 16 (R0082, LLHR) | [IEEE conference paper](https://doi.org/10.1109/WCNC55385.2023.10118908), WCNC 2023, pp. 1–6. The [IEEE bibliography](references.bib) abbreviates the proceedings title. The DOI and cited version are unchanged. |
| §IV-B, p. 6 (R0223/R0145) | R0223 §3.2 and Fig. 3 describe the roles and data flow. §4.2 and Table 2 (physical p. 7) compare planning-system response time and task success across orchestration configurations. R0145 §§3.1 and 6.2, Figs. 2 and 7–10, describe local or cloud assignment and compare use policies. Use the report IDs in the [S2 register](../sn_computer_science/supplement_s2_eligibility.csv) and [S3 sensitivity](../sn_computer_science/supplement_s3.md#unified-coding-and-scope-sensitivity). |
| §IV-D, p. 7 (layer-cut and hover co-design, [28]) | [Coding ledger](../sn_computer_science/technical_coding.psv) classifies R0006 as hybrid. The mathematical paragraph refers to the hover-position subproblem. |
| §V-B, p. 10, Fig. 4, p. 7, and Table IV, pp. 11–12 (R0019) | Original physical p. 15 (printed 8199), Fig. 19. PPO reward reconverges after modeled active-set changes. Transfer in progress and time to the first correct resumed inference output are unreported. [S3 continuity rationale](../sn_computer_science/supplement_s3.md#continuity-correction-for-r0019). |
| §V-C, pp. 10, 13–14 (RQ5) | [RQ5 source map](../../restart_2026_11_26/synthesis/final_46/rq5_claim_sources.csv) and the contrast map above. The 97 entries, 51 matched entries and nine illustrative contrasts describe different selections. |
| §II-C and §VI-D, pp. 2–3 and 15 | See the screening workflow below and [S2 reviewer roles](../sn_computer_science/supplement_s2_adjudication.md#author-statement-on-reviewer-responsibilities). Table VIII records zero paired independent human decisions. The two AI-assisted evidence forms record source checks for the included studies. Independent duplicate extraction remains undocumented. See the acknowledgment on p. 16 for the AI-use disclosure. |

## Screening workflow provenance

| Round | Roles recorded in the logs | Decision ledger and project log locator |
| --- | --- | --- |
| Title and abstract | Gemini proposed one disposition per unique record across seven batches (465 records). Codex checked record coverage, criteria, and source excerpts before batch acceptance. | [465-record ledger](../../restart_2026_11_26/title_abstract_screening.csv). Project log `restart_2026_11_26/step07_screening_summary.md` indexes the seven batch acceptance records. |
| Full text, initial batches | Gemini proposed dispositions for the initial 44 reports. Codex checked report evidence, eligibility criteria, and dispositions before batch acceptance. | [44-report ledger](../../restart_2026_11_26/fulltext_screening/fulltext_screening.csv). Project log `restart_2026_11_26/fulltext_screening/step09_screening_summary.md`. |
| Full text, supplemental batches | The supplemental ledger contains 91 batch dispositions and one previously verified exclusion (R0070). Gemini proposed batch dispositions and Codex checked source locators and criterion application. | [92-report ledger](../../restart_2026_11_26/supplemental_screening/screening_decisions.csv). Project log `restart_2026_11_26/supplemental_screening/screening_closeout.md`. |

The ledgers above record intermediate screening. The [S2 final register](../sn_computer_science/supplement_s2_eligibility.csv) records the 136 final full-text decisions made by the lead reviewer. The author confirmed the full set and documented ten decisions separately. The [S2 author statement](../sn_computer_science/supplement_s2_adjudication.md#author-statement-on-reviewer-responsibilities) gives the documented human roles. Item-level human assignments and independence could not be reconstructed.

## S2 audit derivations

| Table VIII result | Input and calculation |
| --- | --- |
| 136 assessed reports | Count unique `report_id` values in the S2 CSV and match the PRISMA retrieved ID set. |
| Author endorsed 46 included and 90 excluded | [S2 endorsement](../sn_computer_science/supplement_s2_adjudication.md#final-decisions-and-author-endorsement) and [final eligibility register](../sn_computer_science/supplement_s2_eligibility.csv). |
| Ten separate final decisions, zero deferrals | S2 rows have seven inclusions (R0001, R0082, R0121, R0125, R0145, R0223, R0292) and three exclusions (R0081, R0113, R0132). Case details are in [S2](../sn_computer_science/supplement_s2_adjudication.md). |
| 126 without a separate final author entry | 136 assessed − 10 separately documented final decisions = 126. The full set has the author's endorsement. |
| 4/10 processed and 4/10 final changed | R0081 and R0132 awaiting→exclude, R0113 include→exclude, R0082 awaiting→include. Four changed statuses divided by ten separately documented reports, all of which have a final decision. |
| 0 / 0 reviewer decisions, 0 pairs, N/A observed agreement | Both reviewer decision columns have zero nonempty entries. The audit requires two independent decisions on the same report; the observed-agreement denominator is zero. |
| 46 included, 90 excluded, 0 awaiting | Read the verified PRISMA counts and pending map from the ledger. 46 + 90 + 0 = 136. |
