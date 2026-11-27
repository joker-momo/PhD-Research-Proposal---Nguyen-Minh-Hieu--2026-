# Supplemental P08, batch 02 — R0110 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0110.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, I. INTRODUCTION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | An ad hoc swarm uses a leader to coordinate transformer inference among UAV workers with redundant shards. | pp. 3–4, §§I and III.A |
| Workload | The simulator supports two FP16 Llama-2 sizes. Main displayed results use the 70B workload. The setup does not identify an empirical task or prompt dataset. | p. 9, §V.A |
| Partition assignment | The method deploys redundant feed-forward shards offline and activates worker replicas selectively online. Leader-side state and worker-side aggregation have different roles. | pp. 4 and 7–9, §III.A and §IV |
| Optimization | The optimization uses an offline placement phase and an online solver coordinating selective execution and communication under resource and reliability constraints. | pp. 6–9, §§III.E and IV |
| Compute radio | The simulator uses parameterized compute and 3GPP-informed channel assumptions. Table III separates propagation parameters and study-specific operating settings. | pp. 9–10, §V.A and Table III |
| Mobility continuity | Worker redundancy, leader re-election and checkpoint recovery are described. Stress tests vary simulated network and mobility conditions. The paper leaves real-hardware recovery latency unmeasured. | pp. 9 and 13–14, §IV.E, §V.F and §VI |
| Evaluation | A discrete-event simulator tests fixed and stress conditions, with independent seeds and a shared timeout. The article explicitly leaves the physical prototype and on-device solver timing for future work. | pp. 9–10 and 14–15, §§IV.E, V.A and VI |
| Baselines | The evaluation uses parallelism, partition/deployment, random and alternative scheduling baselines, with separate component ablations. Shared conditions and baseline adaptations are documented. | pp. 9–12, §V.A–D |
| Outcomes | The reported outcomes include completion, energy and latency. In the default 70B simulated comparison, latency is conditioned on success; reliability and latency therefore require separate interpretation. | pp. 9 and 11–13, §V.A, §V.C–D and Figs. 7 and 9 |
| Variability | The study gives independent-seed counts for default and stress settings and tests model parameters, mobility and channel scenarios separately. | pp. 9–10 and 12–14, §V.A, Table III and §V.D–F |
| Code data | The simulator design and model family are named. No study-specific repository, trace release or input dataset is identified in the inspected evaluation and end matter. | pp. 9–10 and 14–15, §V.A, §§VI–VII and end matter |
| Funding conflicts | The footnote discloses government and university support. The inspected first page and final sections do not give a competing-interest statement. | pp. 1 and 14–15, funding footnote and end matter |
| Limitations | The paper describes the redundancy–memory and deployment cost trade-off, interference-related limits and lack of validation of leader operation on real UAVs. | pp. 9 and 14, §IV.E and §VI |
