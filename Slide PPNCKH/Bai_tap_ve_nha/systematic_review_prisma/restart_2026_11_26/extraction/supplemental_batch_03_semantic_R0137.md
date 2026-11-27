# Supplemental P08, batch 03 — R0137 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0137.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 10, VI.A Experimental Setup.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | UAVs analyze video locally or collaborate with edge computing resources. The reliability-aware method coordinates choices among UAVs and the edge. | pp. 4–6, §III and system figure |
| Workload | Evaluation uses urban traffic video and object-detection CNN configurations at multiple resolutions. Request patterns are derived separately from an external usage distribution. | p. 10, §VI.A and Tables II–IV |
| Partition assignment | Per-task decisions select local or remote execution and model/input configurations. This is task-level allocation, with no consecutive-layer split. | pp. 5–7, §§III.C–D and IV |
| Optimization | A multi-agent learner jointly addresses inference configuration and offloading and incorporates computation or transmission failures in the reliability model. | pp. 5–9, §§III.B, IV and V |
| Compute radio | Physical UAV and edge hardware are profiled. The training model uses probabilistic path loss and communication effects. Profile measurements and modeled links have different provenance. | pp. 10–11, §VI.A and Tables II–IV |
| Mobility continuity | Evaluation accounts for compute and link reliability using modeled disturbances. The source distinguishes profiling and physical policy deployment from a simulated link; it does not establish an airborne outage experiment. | pp. 5 and 10–12, §III.B and §VI |
| Evaluation | The authors describe actual inference profile measurements and physical multi-UAV policy deployment, as well as offline training and modeled evaluation conditions. Modality depends on the reported result. | pp. 10–11, §VI.A and Tables II–IV |
| Baselines | Comparisons include MARL-based analytics, single-node optimization and alternative policies. Ablations serve distinct comparisons. | pp. 11–12, §§VI.B–C |
| Outcomes | The paper reports analytics accuracy and reliability-related outcomes. Measured model profiles in Tables II–IV are distinct from modeled system-level comparisons. | pp. 10–12, Tables II–IV and §§VI.B–C |
| Variability | Training episodes, operating-factor changes and ablations are reported. Independent repeats and run-level uncertainty are not established by the inspected evaluation. | pp. 10–12, §VI |
| Code data | The article cites video material and a request-pattern proxy. A study code or experiment trace release is not identified in the inspected text. | pp. 10 and 13, §VI.A and References |
| Funding conflicts | The study discloses grant support. The inspected first page and end matter lack a competing-interest declaration. | pp. 1 and 13, first page and end matter |
| Limitations | The authors identify incomplete modeling of scheduling jitter and battery voltage, and defer dedicated fault-injection validation. | pp. 10–13, §VI.A–B and §VII |
