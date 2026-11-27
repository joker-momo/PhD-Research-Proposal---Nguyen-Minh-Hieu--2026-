# Supplemental P08, batch 03 — R0145 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0145.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 14, 6.1 Experiment settings.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Small models serve edge roles and a larger model serves the cloud role. The architecture can revisit selected local inference cases. | pp. 4–6 and 12–14, system model and §§5–6 |
| Workload | Fine-tuned language models process generated multi-UAV decision tasks. The evaluation uses separate training and test samples. | pp. 14–16, §§6.1–6.2 |
| Partition assignment | Work is distributed between edge and cloud models at task level. Replay can revise prior inferences. | pp. 4–6 and 11–14, system model and §5 |
| Optimization | The study describes generated fine-tuning samples, model selection and a scene memory/replay component for simulated edge–cloud coordination and model evaluation. | pp. 6–14, §§4–6.1 |
| Compute radio | A lab server and software versions are given, alongside modeled system and communication conditions. Device-side roles are represented in software. | pp. 4–6 and 14, system model and §6.1 |
| Mobility continuity | Motion and decisions are simulated. Replay addresses inference errors; no actual network outage recovery validation is identified. | pp. 11–19, §§5 and 6 |
| Evaluation | Experiments use a lab server and generated gridded simulation settings. Local and cloud labels are experimental roles. | pp. 14–15, §6.1 |
| Baselines | Comparisons distinguish language models, edge-only or cloud-only and coordinated inference, and heuristic and DRL task-planning baselines. | pp. 15–18, §§6.1–6.3 |
| Outcomes | The software results report task completion, processing time and system cost. Each comparison applies to its own workload and baseline group. | pp. 15–20, §§6.2–6.4 and §7 |
| Variability | Scenario variants and comparative conditions are reported. Outcome uncertainty intervals and independent seed replication are not specified for the inspected comparisons. | pp. 14–20, §6 |
| Code data | The authors describe internal data generation and software dependencies. No release of the study dataset or implementation is identified in the inspected text. | pp. 14–15 and 20, §6.1, §7 and end matter |
| Funding conflicts | A first-page footnote declares grants. The inspected first page and final pre-reference text lack a competing-interest statement. | pp. 1 and 20, first-page note and §7 |
| Limitations | The discussion and conclusion identify inference resource costs and the need for improved resilience and broader collaboration. | pp. 18–20, §§6.3–7 |
