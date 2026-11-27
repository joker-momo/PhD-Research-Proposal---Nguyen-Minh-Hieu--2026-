# Supplemental P08, batch 01 — R0064 source review

Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0064.pdf`. The manifest SHA-256 matched. Physical pages are 1-based. PyMuPDF page text and the original layout text were used.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Multiple camera-equipped UAVs survey points of interest. UAVs carry compressed DNNs, while ground edge servers provide uncompressed inference. | pp. 3–4, §3 and Fig. 2 |
| Workload | The analytic workload models temporally correlated multi-frame recognition, with an accuracy function of sampled frame count and a compressed-model penalty. The setup uses 1080 × 1080 frames and allowed frame counts from 5 to 20 with gaps above 13. It reports no real-video experiment. | pp. 5–6, §§3.3–3.4; p. 8, §5.1; p. 12, §6 |
| Partition and assignment | Each UAV executes the whole sampled task locally or sends it to one ground edge server. The formulation preserves temporal correlation across sampled frames. | p. 5, §3.3 and Eq. (19); p. 12, §6 |
| Optimization | MAPPO-HA trains a cooperative policy for 3D motion, frame sampling and binary offloading to minimize delay subject to sensing, accuracy and energy constraints. Its actor separates continuous and discrete action dimensions. | pp. 6–8, §§3.5, 4.1–4.2 |
| Compute and radio | The default simulated configuration uses probabilistic LoS/NLoS links, a 2 MHz bandwidth and distinct onboard and edge compute budgets. A bandwidth sweep varies that value. | pp. 4–5, §3; p. 9, Table 2 and §5.2.2 |
| Mobility and continuity | The model varies 3D trajectories and uses a minimum UAV separation. The discussion explicitly omits congestion-related loss and changing locations of mobile points of interest. The evaluated framework does not verify service recovery after node dropout. | p. 4, §3.1.1; pp. 9–11, Table 2 and §5.2; p. 12, §6 |
| Evaluation | The analytical workload and channel run as simulations on an Ubuntu server. Baseline runs use a scenario with three UAVs, two fixed servers and fifty points of interest. Separate tests vary swarm size. | pp. 8–9, §5.1; p. 11, §5.2.5 |
| Baselines | MAPPO-DA, MADQN, static-frame sampling, fixed flight trajectories, edge-only computing and local-only computing. Distinguish external algorithm designs from framework ablations. | p. 9, §5.1 |
| Outcomes | The study compares modeled inference delay and accuracy and reports reward, sensing counts and fairness in particular experiments. The proposed approach shows lower simulated delay in the compared bandwidth sweep. This result uses the modeled accuracy function. | pp. 9–11, §§5.2.1–5.2.7 |
| Variability | The bandwidth comparison reports 50 test episodes and 95% confidence intervals. NumPy and Torch seeds are fixed in the setup. The stated confidence intervals describe the reported tests, not between-seed training variance. | p. 9, §§5.1, 5.2.1–5.2.2; p. 10, Fig. 7 |
| Code and data | The article states that no data were used. The inspected simulation section and end matter do not identify a released implementation. | pp. 8–9, §5.1; p. 12, Data availability |
| Funding and conflicts | The authors identify funding and report no known competing financial interests or personal relationships of the stated kind. | p. 12, Acknowledgments and Declaration of competing interest |
| Reported limitations | The discussion identifies limits of binary offloading, the absence of real video or high-fidelity physics, unmodeled packet losses and mobile points of interest, and the need to retrain when the environment changes. | pp. 11–12, §6 |
