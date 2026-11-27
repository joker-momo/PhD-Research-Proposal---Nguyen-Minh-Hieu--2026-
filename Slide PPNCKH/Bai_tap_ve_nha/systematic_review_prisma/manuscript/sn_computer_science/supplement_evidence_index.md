# S4. Evidence and reproduction record

This appendix indexes the HK261 combined technical survey. Locations in
the prose table refer to lines in [main.tex](main.tex). Where a source is a
paper, a page is the physical PDF page counted from one. The source records
below retain the version, file path, checksum, and available locators. Start
with the manuscript location, then use its report ID or evidence key to find
the original. Repository paths in the ledgers are relative to the HK261
project directory.

## Evidence files

| Evidence | Where to look |
| --- | --- |
| Protocol, dates, sources, coverage and limits | [Restart protocol](../../restart_2026_11_26/protocol_restart.md), [search dataset manifest](../../restart_2026_11_26/search_dataset_manifest.json), [search log](../../restart_2026_11_26/search_log.md), [S1 search strings and changes](supplement_search_strategies.md). |
| Counts, exclusions, and retrieval | [Reconciled counts](../../restart_2026_11_26/prisma/prisma_counts.json), [reconciliation review](../../restart_2026_11_26/prisma/active_reconciliation_review.md), [PRISMA checklist](../../restart_2026_11_26/prisma/active_prisma_checklist.md), [retrieval log](../../restart_2026_11_26/fulltext_retrieval/retrieval_log.csv), [S2 exclusions and locators](supplement_fulltext_exclusions.csv), [initial pending reports](../../restart_2026_11_26/fulltext_screening/awaiting_classification.csv), [supplemental decisions](../../restart_2026_11_26/supplemental_screening/screening_decisions.csv), [report–study map](../../restart_2026_11_26/study_linkage/active_report_study_map.csv), [candidate linkage pairs](../../restart_2026_11_26/study_linkage/active_pair_evidence.csv). |
| Report identity and original PDF | [Included input index](../../restart_2026_11_26/synthesis/final_46/synthesis_input_index.csv) has the study and report IDs, original local PDF, SHA-256, and accepted evidence paths. [Citation metadata](references.bib) records DOI or publisher identifier. |
| Architecture, model, optimization, evaluation, and continuity | [R0082 accepted fields](../../restart_2026_11_26/synthesis/final_46/r0082_evidence.json), [historical extraction](../../restart_2026_11_26/extraction/p08_extraction_table.json), [historical source-locator inventory](../../restart_2026_11_26/extraction/p08_source_inventory.json), [study characteristics](../../restart_2026_11_26/synthesis/final_46/study_characteristics.csv), [RQ claim–source matrix](../../restart_2026_11_26/synthesis/active_claim_source_matrix.csv), [claim synthesis](../../restart_2026_11_26/synthesis/active_rq_claims.json), [technical coding ledger](technical_coding.psv). For an expanded claim or primary coding decision, use the cited report ID to look up the matching extraction field and original locator. |
| Numerical statements and outcomes | [Retained outcome ledger](../../restart_2026_11_26/synthesis/final_46/contrast_evidence.csv), [quantitative source matrix](../../restart_2026_11_26/extraction/p08_quantitative_claim_source_matrix.csv), [R0092 correction](../../restart_2026_11_26/synthesis/active_rq_p08_erratum_R0092.json), and the numerical contrast row map below. |
| Human adjudication and scope | [S2 audit and priority cases](supplement_s2_adjudication.md), [136-report log](human_adjudication_log.csv). S2 records eight final author decisions, including R0082 and R0292 included and R0113 excluded under E3. Independent human review fields remain blank. |
| Uniform RQ5 reread | [S3 and evidence provenance](supplement_s3.md), [RQ5 claim sources](../../restart_2026_11_26/synthesis/final_46/rq5_claim_sources.csv), [general claim–source matrix](../../restart_2026_11_26/synthesis/final_46/claim_source_matrix.csv), and [input index](../../restart_2026_11_26/synthesis/final_46/synthesis_input_index.csv). |
| Reference validation | [DOI and landing checks](editorial_doi_audit.csv). Landing responses and independent registry identity checks have separate columns. |
| Appraisal | [Data and rationales](../../restart_2026_11_26/synthesis/final_46/appraisal_rationale.csv) keyed by report and D01–D10, [full ratings](../../restart_2026_11_26/synthesis/final_46/appraisal_table.csv), [summary](../../restart_2026_11_26/synthesis/final_46/appraisal_summary.csv). |
| Comparison release | [Editorial integration and verification](editorial_verification.md), [public source lookup review](editorial_source_lookup_review.md), and [targeted correction brief](editorial_source_lookup_correction.md). |
| Editorial revision and human review | [Editorial response](../../restart_2026_11_26/synthesis/final_46/editorial_response.md), [blinded forms and sampling method](../../restart_2026_11_26/synthesis/final_46/human_review_packet/README.md), [publisher verification code](../../restart_2026_11_26/synthesis/final_46/verify_llhr_publisher.py), and [scope scenarios](../../restart_2026_11_26/synthesis/final_46/scope_sensitivity.json). |
| Verification and unresolved items | [Final release review](../../restart_2026_11_26/synthesis/final_46/release_review.md), [R0082 source and R0019 linkage review](../../restart_2026_11_26/synthesis/final_46/r0082_review.md), [historical technical survey review](technical_survey_review.md), [historical integrity audit](../../restart_2026_11_26/integrity/active_final_integrity_audit.md), [historical limitations](../../restart_2026_11_26/integrity/active_limitations.md). |

## Claim audit and missing evidence

- [Claim-level audit](s4_claim_audit.md) records the source, physical page or section,
  review record, or derivation for each prose claim group. `NARROWED` marks
  claims rewritten to follow the available evidence. `OPEN` marks unresolved
  source coverage, methods, or author confirmations.
- [Study row source map](s4_study_row_sources.csv) locates the original,
  accepted extraction fields and D09 appraisal behind each of the 46 rows of
  the architecture and evaluation tables. Filter by report ID. Each field retains its extraction status,
  including `PARTIAL` and `NOT_REPORTED`. Page or section unavailability is explicit.
- The artifact folder [reproduction guide](minh_chung_hinh_bang/README.md)
  links the frozen inputs and commands for every figure, table and equation.

### Revisions with consequences for interpretation

| Issue | Verified support and manuscript change |
| --- | --- |
| R0001 family (architecture table and Figure 2) | Physical pp. 1–3, §II and §III.A describe convolutional and fully connected layer types and use real-world auxiliary data, without specifying a concrete evaluated DNN family. Code as a generic layered DNN proxy. |
| R0058 workload (architecture table and Figure 2) | Physical p. 19, §6.1 identifies ResNet-18 and CIFAR-10. Code as a concrete CNN workload. Physical pp. 9–10 and 21–22 describe fallback and a speed sensitivity experiment. Individual recovery phases remain open. |
| R0075 modality (evaluation table and Figure 2) | Physical pp. 8–10, §§IV.A–B distinguish Jetson TX2 profiling from modeled links and record a routing boundary in Table III. Code as profile-backed, with communication modeled. |
| R0019 continuity (evaluation table) | Physical p. 15, Fig. 19 varies active UAV count from 3 to 4 to 2 in simulation. Layer allocation is evaluated, while measured handoff time remains open. |
| R0014 event setting (main.tex L225, L242) | Physical p. 10 reports five UAVs outdoors. Physical p. 13 §VIII.C and Table IV report deliberate head disconnection and rescheduling latency. The table measures the scheduler stage. The event's relation to the outdoor run remains open. |
| R0090 dropout evidence (evaluation table) | Physical p. 4 §V.E reports implementation, and physical pp. 3, 5–6 §§II.D, III.B, V.F and V.K describe dropout response and loss. The test modality of the dropout outcome remains open. |
| R0082 setup (evaluation table) | IEEE WCNC and arXiv v1 physical pp. 5–6, §IV and Figs. 2–5 describe simulation and curve-only results. The two-version [cross-check](../../restart_2026_11_26/synthesis/final_46/r0082_publisher_crosscheck.json) records 20 matching anchors or captions. |
| R0118 and R0125 comparability (main.tex L229, L281) | R0118 physical p. 12, Table V supports the common planner. R0125 physical p. 3, Table I and §IV.B support four nominal threads per worker on a workstation. The allocations are 16 versus 4; matched aggregate compute was not established. |
| R0062 fault outcome (main.tex L258) | Physical p. 6, Effect of UAV Unavailability, reports about 2 versus 3 fps. The exact failure-to-resumption time and deadline count remain open. |
| Search and human verification (main.tex L87, L105–107, L342–350) | One unretrieved report, independent duplicate human verification and author declarations remain open in the retained workflow. |

## Figures, tables, and equations

| Item | Source, inputs and reproduction rule |
| --- | --- |
| Figure 1 `fig:flow` (PDF p. 6) | [PRISMA reconciler](../../restart_2026_11_26/prisma/reconcile.py) takes the locked records and decisions plus [the S2 author adjudication log](human_adjudication_log.csv), fills [the TikZ template](../../restart_2026_11_26/prisma/flow_template.tex) and writes [counts](../../restart_2026_11_26/prisma/prisma_counts.json) and [standalone source](../../restart_2026_11_26/prisma/prisma_flow.tex). Compile the latter to rebuild the embedded [figure PDF](prisma_flow.pdf). Arithmetic is raw − duplicates = screened, screened − title/abstract exclusions = sought, sought − unretrieved = assessed, assessed = full-text exclusions + pending + included reports. |
| Figure 2 `fig:macro` (PDF p. 8) | [TikZ](technical_overview_figure.tex) uses [generated counts](technical_macros.tex). The [generator](build_technical_survey.py) counts each report once per panel, using the citation year and BibTeX venue type in panel A and the family, optimizer, and evaluation columns of [primary coding](technical_coding.psv) in the remaining panels. Unscaled TikZ segment height in panel A is 0.16 cm × count, with conference at the bottom and journal stacked above. Horizontal bar length in panels B–D is 0.115 cm × count. The enclosing LaTeX resize applies one scale to the figure. Each panel totals 46. |
| Figure 3 `fig:topologies` (PDF p. 9) | [TikZ](technical_architecture_figure.tex) illustrates the three analyst-defined topology categories from the coding ledger and Table 3. Representative mappings are peer transport R0010/R0121, a head–worker hierarchy R0014/R0118, and tiered processing R0001/R0080. Arrows represent logical relationships. They carry no measured distance, time, or scale. |
| Figure 4 `fig:taxonomy` (PDF p. 10) | [TikZ](technical_taxonomy_figure.tex) uses [generated counts](technical_macros.tex) for topology, unit, optimizer and resilience. A leaf count is the number of distinct reports assigned its label. Each dimension has its own denominator of 46. |
| Figure 5 `fig:appraisalbar` (PDF p. 22) | [TikZ](technical_appraisal_figure.tex) draws [generated bar inputs](technical_appraisal_bars.tex) from the accepted summary. Segment width in percentage points is 100 × status count / 46. The endpoints are cumulative percentages for Yes, Partial, and Not reported, followed by 100% for any No votes. The corresponding Table 7 percentage is 100 × Yes count / 46 rounded to one decimal. |
| Table 1 `tab:related` (PDF p. 2) | [LaTeX](main.tex#L33) and [bibliography](references.bib). Row-level sources are listed below. |
| Table 3 `tab:architecture` (PDF p. 11) | [Generated LaTeX](technical_architecture.tex) uses the 46-study characteristics and coding ledgers. The report citation joins each cell back to architecture, model and partition fields in the accepted extraction and locator inventory. |
| Table 4 `tab:evaluation` (PDF p. 17) | [Generated LaTeX](technical_evaluation.tex) uses the same 46 IDs and joins evaluation settings, connectivity, mobility, faults and continuity cells to the original report through the extraction and locator inventory. |
| Table 6 `tab:outcomes` (PDF p. 21) | [LaTeX](main.tex#L260) transcribes checked values in their reported units and conditions. The row map below identifies the accepted ledger record and the original page/table. |
| Table 2 `tab:settings` (PDF p. 7) | [Generated LaTeX](editorial_mechanism_setting.tex) and [generator](build_editorial_evidence.py) count report IDs grouped by primary mechanism and strongest evaluation setting in the [coded input](../../restart_2026_11_26/synthesis/final_46/mechanisms.csv). Each report contributes to exactly one cell. The two grouping fields are projected from the [primary coding ledger](technical_coding.psv). Source descriptions are retained in the coded input. |
| Table 5 `tab:coverage` (PDF p. 21) | [Generated LaTeX](editorial_outcome_coverage.tex) and [generator](build_editorial_evidence.py) join the [primary coding](../../restart_2026_11_26/synthesis/final_46/mechanisms.csv) and [report coverage](../../restart_2026_11_26/synthesis/final_46/report_coverage.csv) by report ID. Study counts group by status and entries sum matched and descriptive rows in the [outcome ledger](../../restart_2026_11_26/synthesis/final_46/outcomes.csv). [Rule and gap definitions](../../restart_2026_11_26/extraction/rq5_uniform/rule.md). |
| Table 7 `tab:appraisal` (PDF p. 22) | [Generated rows](technical_appraisal.tex) use the accepted summary. Domain counts and percentages share the same source as Figure 5. Use the rationale matrix for individual ratings or missing reporting evidence. |
| Table 8 `tab:adjudication_audit` (PDF p. 25) | [Generated LaTeX](adjudication_audit_table.tex) and [JSON](audit_summary.json) come from the [S2 audit script](audit_adjudication.py), the [136-row S2 log](human_adjudication_log.csv), and the [PRISMA ledger](../../restart_2026_11_26/prisma/prisma_counts.json). Count final decisions and confirmed deferrals together for author coverage. The change numerator counts only final decisions that differ from the frozen AI disposition. |
| Eq. 1 `eq:objective` (PDF p. 10) | [LaTeX](main.tex#L169). This review's synthesized objective defines a feasible decision tuple and weights latency, energy, quality and recovery cost across scenarios. The negative quality sign suits minimization. Weights carry unit conversions and recovery cost must have a distinct boundary from end-to-end delay unless deliberate weighting is explained. See R0001/R0006/R0058/R0080 and RQ2 for examples of subproblems. The review did not fit weights or compute a pooled objective. |
| Eq. 2 `eq:link` (PDF p. 10) | [LaTeX](main.tex#L179). The serialization duration follows from bits divided by effective bits per second. Queueing and protocol time are additive for the stated non-overlapping accounting boundary. R0121 and R0092 provide context for link accounting, with exact assumptions in their extraction. This equation is a schematic decomposition. |
| Eq. 3 `eq:recovery` (PDF p. 23) | [LaTeX](main.tex#L319). Let t0 be event onset, t1 detection, t2 the valid plan, t3 transfer complete and t4 the first correct resumed output. The sum of consecutive differences telescopes to t4 − t0. With overlapping phases, record wall time and individual intervals. R0038/R0062/R0014 are motivating examples. This is a proposed measurement definition. No recovery values were computed with it. |

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

## Manuscript prose crosswalk

Direct findings use citations and retrieved evidence. Analyst synthesis joins
these findings or explains a trade-off. A proposal records the motivation and
assumptions for future work without reporting a newly measured result.

| LaTeX lines | What to retrieve and how to interpret it |
| --- | --- |
| 1–19 | Title, abstract and keywords. Check scope and dates against the protocol, counts against Figure 1 and appraisal table, and interpretations against Sections 4–6 and contrasts table. |
| 20–27 | Inference placement and continuity use the cited report IDs in the extraction and claim matrix. Civil use cases use McEnroe's abstract. Tracking versus batch timing is an illustrative contrast, with R0292 as corpus context. |
| 28–51 | Contextual positioning and related-survey matrix. See the eight row locators above. The scope statement for this review follows from its protocol and outputs. |
| 52–68 | Review questions and contributions. Use the protocol, Sections 2–6, both technical tables, ten-domain ratings and indexed figures. |
| 69–76 | Eligibility and protocol timing. Use the restart protocol, acceptance and S1. PRISMA standard is the cited [reporting guideline](https://doi.org/10.1136/bmj.n71). Registration status concerns the documented project record. |
| 77–81 | Sources, exact cutoff and selection of exports. See the search manifest, search log, recorded timestamps and S1. |
| 82–88 | Screening, retrieval, linkage and reviewer roles. See reconciliation, retrieval log, candidate linkage pairs, report–study map, the PRISMA checklist and limitations. Retrieval percentage = 100 × 136 / 137, rounded to one decimal. |
| 89–93 | Extracted fields, uniform numerical inventory, and ten-domain engineering appraisal. Use the accepted extraction, outcome ledger and appraisal rationales. S3 report coverage has one row per included report. The RQ5 ledger retains 98 entries when filtered to matched or descriptive. |
| 94–102 | Additional coding and synthesis rules. See primary coding, table generator and contrasts table row map. Selective display, absence of pooling and appraisal boundaries describe the review methods. |
| 103–114 | Counts and classification. See Figure 1 and its inputs, S2, the missing item R0116 in the retrieval log, and the final author inclusion R0082. See Table 8 and the S2 audit derivations for 128 and both 4/8 fractions. |
| 115–128 | Corpus/year and evaluation framing. See Figure 2 and evaluation table. Examples of model and workload categories come from coding columns and extracted test settings. |
| 129–145 | Topologies and Figure 3. Use the three topology bins and the cited examples in the report extraction. Interpret overhead and coordination statements as consequences of the depicted dependencies. |
| 146–167 | Partition/dispatch taxonomy and Figure 4. R0145 physical p. 6 and pp. 17–18 and R0223 physical pp. 3–5 and 7 establish request-level eligibility. [Derived sensitivity counts](../../restart_2026_11_26/synthesis/final_46/scope_sensitivity.json) omit each report and then both from the descriptive calculations. Connect the five unit bins to architecture table rows and extraction. Representative checks include R0014 for halo/spatial work, R0075 for exits, R0110 for redundancy, R0080 for representation, R0118 for experts, and R0292 for tracker state. |
| 168–189 | Definitions, common optimization model and link equation. See Eq. 1–2 above, the RQ2 claim matrix, and report locators for R0006/R0058/R0080. |
| 190–209 | Five solver classes and overhead interpretation. Use the optimizer bins, architecture table and the RQ2 evidence. Conditions on online cost are criteria for reading a study, with evaluation boundary drawn from evaluation table. |
| 210–230 | Evaluation modalities, channel assumptions and resource comparison. Use the evaluation bins, evaluation table and RQ3. Key checks are R0121 transport, R0038 bench recovery, R0125 thread count, R0292 handoff, R0014 indoor/outdoor boundary and R0118 planner/comparator design. |
| 231–250 | Disruption and response classes. See resilience coding, evaluation table and RQ4. Distinguish modeled, planned and observed action using each report's extracted event fields and originals. |
| 251–283 | Quantitative comparisons and bounded interpretation. See the nine original contrast locators and outcome conditions. Comparative prose follows the displayed differences and stated measurement boundaries. |
| 284–307 | Appraisal and reporting implications. See appraisal table/Figure 5, appraisal summary and D03, D04, D07 and D09 source rationales. |
| 308–313 | Model regimes and state. Check R0074, R0110 and R0118 and the corresponding architecture table–4 entries. Changes in bottlenecks and memory costs are synthesis conditional on the execution design. |
| 314–327 | Benchmark proposal and Eq. 3. The motivations are workload differences and comparator gaps (the architecture, evaluation, contrasts and appraisal tables), controlled versus planned continuity (evaluation table), and consistent arrival denominators (R0092/contrasts table). The proposal specifies comparators, accounting and timestamp requirements. |
| 328–340 | Open research questions motivated by appraisal D03/D04/D07/D09 and the evaluation/continuity gaps in the architecture, evaluation, contrasts and appraisal tables. Thermal profiling and authenticated provenance are proposed tests. |
| 341–345 | Validity limits. See S2 audit and Table 8 for the absence of paired decisions, and project limitations, accepted reconciliation, extraction scope, PRISMA checklist, and the source class of the related-survey matrix sample for the other limitations. |
| 346–356 | Conclusion, declarations, supplements and bibliography. Map RQ1–RQ5 to Sections 4–5 and the RQ claim matrix. Benchmark implications refer to Section 6. Author confirmations remain open. |

## S2 audit derivations

| Table 8 result | Input and calculation |
| --- | --- |
| 136 assessed reports | Count unique `Record_ID` values in the S2 CSV and match the PRISMA retrieved ID set. |
| Eight final decisions, zero deferrals | S2 rows have five inclusions (R0001, R0082, R0145, R0223, R0292) and three exclusions (R0081, R0113, R0132). Case details are in [S2](supplement_s2_adjudication.md). |
| 128 without author confirmation | 136 − 8 final author decisions = 128. |
| 4/8 processed and 4/8 final changed | R0081 and R0132 awaiting→exclude, R0113 include→exclude, R0082 awaiting→include. Four changed statuses divided by eight author-processed reports, all of which have a final decision. |
| 0 / 0 reviewer decisions, 0 pairs, N/A observed agreement and kappa | Both reviewer decision columns have zero nonempty entries. The audit requires two independent decisions on the same report; the observed-agreement denominator is zero and both metrics are null in JSON. |
| 46 included, 90 excluded, 0 awaiting | Read the verified PRISMA counts and pending map from the ledger. 46 + 90 + 0 = 136. |

## Rebuild and check

From this directory, with Python 3.11 or newer and Tectonic available:

```sh
python3 ../../restart_2026_11_26/prisma/reconcile.py --check
python3 ../../restart_2026_11_26/synthesis/final_46/reconcile_inputs.py --check
python3 build_technical_survey.py --check
python3 audit_adjudication.py --check
python3 check_evidence.py
```

To regenerate the embedded flow independently, write into a temporary
directory, for example:

```sh
flow_build_dir="$(mktemp -d)"
(
  cd ../../restart_2026_11_26/prisma
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$flow_build_dir" prisma_flow.tex
)
```

For the full paper, regenerate the technical and editorial inputs with
`python3 build_technical_survey.py` and `python3 build_editorial_evidence.py tables`.
Run `python3 audit_adjudication.py` in the worktree to regenerate Table 8
and the JSON from S2, the frozen baseline, canonical deferrals and PRISMA.
Then compile with
`tectonic --only-cached --keep-logs --keep-intermediates main.tex`.
The verified toolchain used pdfTeX 1.40.27 (TeX Live 2025) for the standalone
flow, Tectonic 0.16.9 for the manuscript, and Python 3.14.5 for the data. Omit
`--only-cached` for an initial Tectonic build if its TeX bundle is unavailable
locally. Binary PDFs can carry different metadata. Compare extracted page content or
rendered pages when verifying a reproduction. Update the evidence crosswalk and confirm sources before recording
a new local file snapshot with `python3 check_evidence.py --record`.

## Boundaries

The 46 included originals are retained with checksums. Use the retrieval log
and its access/version fields when copying or reobtaining an original. Its
access conditions also apply to any future shared package. One report was unretrieved. PRISMA has zero reports awaiting classification. Independent duplicate human screening, human extraction verification, and author declarations remain open. The taxonomy, common optimization model and benchmark
are the review's synthesis and proposals. Their evidence documents how
they were derived, with empirical findings attributed to the original studies.
