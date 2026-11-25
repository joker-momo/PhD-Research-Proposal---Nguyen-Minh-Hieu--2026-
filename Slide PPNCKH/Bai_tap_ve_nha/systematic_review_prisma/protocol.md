# Review Protocol

**Protocol version:** 0.1  
**Protocol date:** 2026-11-24  
**Status:** Fixed before pilot retrieval; amendments must be dated and justified below.  
**Review type:** Systematic review with narrative and evidence-map synthesis, reported using PRISMA 2020.  
**Registration:** Local time-stamped protocol for the HK261 coursework. No external registration has yet been made.

## 1. Working title

Collaborative DNN Inference in UAV-Enabled Edge Computing: A Systematic Review of Partitioning, Placement, and Resource Allocation

## 2. Rationale

UAV-enabled edge systems combine mobile sensing, constrained onboard computation, and time-varying wireless links. Existing studies distribute or partition DNN inference across UAVs, terrestrial edge nodes, or cloud servers, but they use different architectures, optimization variables, evaluation assumptions, and outcome definitions. A systematic synthesis is needed to determine what has actually been evaluated, which design choices are supported by evidence, and which claims remain dependent on idealized simulations.

## 3. Objective and review questions

The objective is to systematically identify and synthesize primary studies of collaborative DNN inference in UAV-enabled edge computing.

- **RQ1:** Which UAV–edge architectures, inference tasks, DNN models, and collaboration patterns have been studied?
- **RQ2:** How do studies jointly or separately optimize model partitioning, task or node assignment, compute allocation, bandwidth, transmit power, trajectory, or deployment?
- **RQ3:** Which datasets, simulators, hardware platforms, network models, baselines, and metrics are used to evaluate the proposed methods?
- **RQ4:** How do studies model mobility, time-varying links, intermittent connectivity, UAV failure, and recovery?
- **RQ5:** What evidence supports improvements in latency, energy, communication load, accuracy, reliability, and scalability, and what methodological or reproducibility gaps remain?

## 4. Eligibility framework

### 4.1 Inclusion criteria

Reports must satisfy all applicable criteria.

1. Primary research presenting or evaluating a method, model, algorithm, architecture, or system.
2. At least one UAV participates as a sensing, computing, relay, or orchestration node in an edge, fog, cloud, or multi-UAV computing architecture.
3. The computational workload includes DNN inference, collaborative inference, split computing, model partitioning, distributed inference, or a joint optimization problem in which DNN inference placement or partitioning is explicit.
4. The report provides an evaluative method or analyzable evidence, such as experiments, emulation, simulation, trace-driven evaluation, prototype results, or a mathematical performance study.
5. Published from 2021-01-01 through the final search date.
6. Written in English.
7. Full peer-reviewed journal and conference papers are eligible. Preprints may be included only when they provide unique recent evidence and are labelled as non-peer-reviewed.

### 4.2 Exclusion criteria

1. Federated learning or distributed training without an inference-stage contribution.
2. Generic computation offloading in which the task is indivisible and DNN inference, model placement, or model partitioning is not explicit.
3. Single-UAV onboard perception with no collaborative edge, fog, cloud, or multi-node inference component.
4. UAV communication, routing, caching, or relay studies without an inference workload.
5. Editorials, tutorials, posters, abstracts without a full report, theses, patents, book chapters, review papers, and secondary studies. Relevant reviews may be retained only for backward and forward citation searching.
6. Duplicate reports. The most complete version will supply the primary evidence, while related reports will remain linked in the study-to-report map.
7. Full text cannot be retrieved after documented attempts.

## 5. Information sources

The planned core sources are IEEE Xplore, ACM Digital Library, Scopus, and Web of Science Core Collection because the topic spans electrical engineering, networking, edge computing, and computer systems. OpenAlex and Semantic Scholar will be used for pilot discovery, deduplication support, and citation chaining. Crossref will verify DOI metadata. arXiv will identify relevant preprints. Google Scholar, publisher pages, and reference lists will be supplementary discovery sources and will not be represented as exhaustive database searches.

If subscription access prevents a planned core search, the missing source and coverage limitation will be reported. Search results from different platforms will be exported and retained unchanged before normalization.

## 6. Search concepts

Three concept blocks will be combined.

1. **UAV:** “unmanned aerial vehicle”, UAV, drone, aerial robot, flying ad hoc network, FANET.
2. **Inference:** deep neural network, DNN, deep learning inference, edge intelligence, collaborative inference, cooperative inference, distributed inference, split inference, split computing.
3. **Partition and orchestration:** model partitioning, DNN partitioning, layer partitioning, computation offloading, task assignment, resource allocation, bandwidth allocation, model placement, service placement.

The inference block is mandatory. The third block will be used in a complementary query rather than as a universal requirement so that architecture papers using different terminology are not lost.

## 7. Search and record management

Each platform-specific query will be piloted against known relevant seed papers before the final search. For every run, the exact query, search date, platform, filters, reported total, exported total, file name, and failure or cap will be recorded. Raw exports will be immutable. Records will be normalized and deduplicated first by DOI, then by normalized title, year, and first author. Preprints and published versions will be linked rather than silently discarded.

Backward and forward citation searching will be applied to included studies and directly relevant review articles. Supplementary records will undergo the same eligibility assessment as database records.

## 8. Study selection

Screening will proceed in two stages.

1. Title and abstract screening against the fixed eligibility criteria.
2. Full-text assessment with one primary exclusion reason assigned to every excluded report.

The AI-assisted first pass will be checked by Nguyễn Minh Hiếu for final full-text eligibility. This is not represented as two independent human reviewers. Any unresolved judgment will remain marked `uncertain` until adjudicated. The manuscript will disclose the actual screening arrangement as a limitation.

## 9. Data extraction

The extraction form will capture bibliographic identity, architecture, UAV role, inference topology, DNN and dataset, partition granularity, optimization variables, objective and constraints, solution method, mobility and channel model, failure handling, simulator or hardware, baselines, metrics, quantitative findings, sensitivity analyses, code or data availability, funding, conflicts, and author-reported limitations.

Only information verified in the full report will be treated as extracted evidence. Abstract-only observations will be labelled explicitly.

## 10. Quality appraisal

Because the expected evidence consists mainly of systems, simulation, optimization, and prototype studies, clinical risk-of-bias tools are not applicable. Each included study will be judged `yes`, `partial`, `no`, or `not applicable` across these domains:

1. Research question and system model are clearly defined.
2. Assumptions, variables, and constraints are explicit.
3. Experimental or simulation configuration is reproducible.
4. Baselines are relevant and implemented comparably.
5. Metrics match the stated objective.
6. Results include variability, repeated runs, sensitivity analysis, or convergence evidence where applicable.
7. Network mobility and channel assumptions are justified for the claimed setting.
8. Claims are bounded by the evaluated conditions.
9. Code, data, traces, or sufficient implementation details are available.
10. Limitations and conflicts or funding are reported.

Quality judgments will inform interpretation and sensitivity analysis. Studies will not be excluded solely by a summed quality score.

## 11. Synthesis

Because heterogeneous models, network assumptions, objectives, and metrics are expected, the default synthesis is structured narrative synthesis and an evidence map. Results will be grouped by architecture and decision type, then compared across evaluation realism, outcomes, and quality domains. Meta-analysis will be attempted only if a sufficiently homogeneous subset reports compatible outcomes and variance information. Otherwise, no pooled effect estimate will be produced.

## 12. Reporting and integrity

The review will follow PRISMA 2020. Records, reports, and studies will be counted separately. The PRISMA flow will be generated only from reconciled logs. Every citation will be checked against its source and DOI metadata. Quantitative claims will be copied from verified reports with their conditions and units. No projected or fabricated review result will appear in the Results section.

AI assistance will be disclosed according to the target journal policy. Authors retain responsibility for searches, eligibility decisions, extraction, interpretation, and submission.

## 13. Protocol amendments

| Date | Section | Change | Reason | Effect on completed work |
|---|---|---|---|---|
| 2026-11-24 | Scope and eligibility | Amendment 001 requires an explicit multi-UAV or UAV-swarm inference architecture. | Align the review with the defined UAV-swarm research direction. | Pilot records are retained for audit and re-screened under the narrower scope. |
| 2026-11-24 | Publication-date eligibility | Amendment 002 changes the lower publication-date bound from 2015-01-01 to 2021-01-01. | User-specified recency requirement: include research from 2021 onward only. | Formal database filters, screening, Methods, and synthesis use 2021 through the final search date; earlier pilot records remain in the audit trail but are ineligible. |

