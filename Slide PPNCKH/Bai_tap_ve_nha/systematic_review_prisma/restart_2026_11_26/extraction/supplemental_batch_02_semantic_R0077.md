# Supplemental P08, batch 02 — R0077 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0077.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, 1. Introduction.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Swarm nodes exchange local capacity metrics with one-hop neighbors; repeated exchanges propagate workload information beyond one hop. There is no global scheduler in the proposed method. | pp. 3–5, §§1 and 3 |
| Workload | The simulator processes a modeled layered inference graph with two intermediate exits. The evaluation identifies an application example, with no named input dataset or specified neural-network implementation. | pp. 4 and 8, §3 and Table 2 |
| Partition assignment | A node can forward raw inputs or already computed intermediate state to a neighbor, choosing a layer exit depth with respect to load. The method bounds redundant reconsideration. | pp. 2 and 5–8, Fig. 2 and §4 |
| Optimization | The algorithm combines a diffused compute-capacity indicator, a threshold on offloading, and a congestion-aware early exit. Sensitivity to the threshold is evaluated separately. | pp. 5–8, §4 and Fig. 3 |
| Compute radio | Compute capacity is parameterized across heterogeneous UAVs. The two-ray channel and transmission rate are modeled. Table 2 gives simulator settings rather than hardware validation. | pp. 5 and 8, §3 and Table 2 |
| Mobility continuity | Circular UAV trajectories and mostly line-of-sight connections drive modeled neighbor changes. Constraint and queue behavior mitigates redistribution loops. Physical node failure and recovery are not evaluated in the inspected simulation. | pp. 6 and 8, §§4 and 5 |
| Evaluation | The evaluation is software simulation with stochastic arrivals, mobility and heterogeneous nodes. It describes repeated independent runs, with no physical UAV test in the evaluation. | p. 8, §5 and Table 2 |
| Baselines | Comparisons include random and acyclic-random offloading, a least-busy greedy scheme and local-only inference. The proposed distributed method is the fifth case. | p. 8, §5 |
| Outcomes | The evaluation reports latency, outstanding work, transfer time, energy per task and fairness under scenario sweeps. Interpret early-exit results in the context of the model’s assumed exit accuracies. | pp. 8–12, §5, Table 2, performance figures and §6 |
| Variability | Section 5 reports 95% intervals derived from 50 independent runs and varies threshold, worker count and task intensity, among other inputs. | pp. 8–11, §5, Table 2 and sensitivity figures |
| Code data | No simulator/code release or application dataset is specified in the inspected simulation, conclusion and acknowledgment. | pp. 8 and 11–12, §5, §6 and Acknowledgment |
| Funding conflicts | The Acknowledgment names ITU and PRIN 2022 support. The inspected first page and end matter do not contain a competing-interest declaration. | pp. 1 and 12, first page and Acknowledgment |
| Limitations | The authors call for advanced mobility models and real-flight data and identify field-operation needs in runtime monitoring, parameter tuning and early-exit accuracy policy. | pp. 11–12, §6 |
