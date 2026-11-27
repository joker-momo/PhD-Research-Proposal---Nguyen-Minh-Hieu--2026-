# Supplemental P08, batch 02 — R0080 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0080.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, I. INTRODUCTION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Multiple aerial edge nodes independently extract features and collaborate with one ground/cloud server via a modeled radio access network. | pp. 2–3, §II.A and Fig. 1 |
| Workload | CIFAR-10 test images are augmented to synthesize non-identical data across UAVs. ResNet-18/34 act as edge backbones and ResNet-101/152 act as cloud backbones. | p. 5, §IV.A |
| Partition assignment | Cloud processing of uploaded features estimates confidence, then a per-UAV threshold selects cases requiring an additional quantized raw upload. | pp. 2–3, §II.A and Fig. 1 |
| Optimization | The study uses per-UAV thresholds and raw-data quantization for accuracy maximization within a shared bandwidth limit, with alternating optimization. | pp. 2–5, §§II.B–III and Algorithm 1 |
| Compute radio | The setup names a cloud GPU and models per-UAV spectral efficiency and bandwidth. The 100 Mbps value applies to the Table I comparison. No flight radio or onboard hardware characterization is given there. | pp. 2 and 5–6, §§II.A and IV.A–B |
| Mobility continuity | No UAV trajectory, outage or recovery evaluation is reported in the configuration or results. Spectral efficiency differences do not establish mobility validation. | pp. 2 and 5–6, §§II.A and IV |
| Evaluation | The edge–cloud experiment is simulated using synthesized data distributions. The cloud processing hardware is identified; there is no demonstrated flight test in this experiment. | p. 5, §IV.A |
| Baselines | Raw-Only sends raw data, Feat-Only sends extracted features, and GSUP uses shared confidence/quantization settings. Table I compares them with the proposed policy. | p. 5, §IV.A and Table I |
| Outcomes | The proposed policy reports higher top-1 accuracy across Table I model pairs and lower simulated end-to-end latency than Raw-Only. Its point-estimate latency is higher than GSUP and Feat-Only. | pp. 5–6, Table I and §IV.B |
| Variability | The paper reports three independent seeds per setting and 95% Student-t confidence intervals. Fig. 2 is a single-UAV bandwidth and confidence-threshold sweep; Fig. 3 varies UAV count. | pp. 5–6, §IV.A–B and Figs. 2–3 |
| Code data | The underlying CIFAR-10 data are named and cited. No study-specific source code, generated input splits or simulation artifacts are identified in the inspected setup and end matter. | pp. 5–6, §IV.A, conclusion and References |
| Funding conflicts | The acknowledgment names multiple funding programs. The first page and end matter inspected do not contain a competing-interest declaration. | pp. 1 and 6, first page and Acknowledgement |
| Limitations | The results describe a latency cost for deeper cloud backbones and a smaller accuracy gain where upstream information is limited. The conclusion does not provide a dedicated limitations discussion. | p. 6, §IV.B and conclusion |
