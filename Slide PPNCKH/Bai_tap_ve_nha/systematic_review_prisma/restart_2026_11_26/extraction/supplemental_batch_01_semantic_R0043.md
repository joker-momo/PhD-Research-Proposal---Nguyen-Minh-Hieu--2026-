# Supplemental P08, batch 01 — R0043 source review

Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0043.pdf`. The manifest SHA-256 matched. Physical pages are 1-based. PyMuPDF and original renderings of pp. 5–6 were used. Review status is a candidate for the batch composite.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | User UAVs originate data and server-equipped UAVs process DNN subtasks in an aerial network. The server nodes can queue those subtasks and store models. | p. 2, §II.A–B; p. 3, Fig. 2 |
| Workload | The simulated workload uses SeaShip images and four benchmark models, NiN, VGG16, AlexNet and ResNet18. Task arrivals are Poisson. The source establishes a visual workload with six ship types. Avoid an unqualified claim that an evaluated detector reports detection accuracy. | p. 5, §IV.A and Table I |
| Partition and assignment | The approach divides fused convolutional blocks into sub-blocks with overlapping spatial inputs. The scheme assigns the subtasks to matched server UAVs. | pp. 3–4, Fig. 2 and §III.A–B |
| Optimization | The formulation seeks to minimize total inference time. It bounds the number of servers per task and imposes a minimum transmission rate. Fine-grained partition and genetic-algorithm coalition matching are separate subproblems. Avoid substituting the coalition-fitness expression for the overall objective. | p. 3, §II.C Eq. (6); pp. 4–5, §III.A–B, Algorithm 1 and Eq. (11) |
| Compute and radio | Table I reports 30 user nodes and six server nodes. The stated simulation parameters are 20 MHz system bandwidth, 10 dBm user transmit power and 60 GFLOPS computing power per modeled server node. The network model states fixed bandwidth and includes Rayleigh fading. | pp. 2–3, §II.A–C; p. 5, Table I and §IV.A |
| Mobility and continuity | Bandwidth is held fixed in the network model. The inspected model and simulation do not establish movement trajectories, outages, migration or recovery tests. | p. 2, §II.A; pp. 5–6, §IV and Fig. 3 |
| Evaluation | The paper reports simulations with common node power assumptions and a task-count sweep for the four benchmark models. Fig. 3 plots through 3,000 tasks. No physical flight experiment is described in the evaluation. | p. 5, §IV.A–B and Table I; p. 6, Fig. 3 |
| Baselines | Random fusion retains DIA-O, Random offload retains DIA-FP and Greedy sends a whole task to the nearest server without partitioning. | p. 5, §IV.A |
| Outcomes | DIA shows the lowest simulated total inference time on all four plotted model panels for the reported task-count sweep. Preserve the matched qualitative comparison. The abstract's range does not identify the exact model, task-count and comparator denominator needed for a verified numerical comparison. | pp. 5–6, §IV.B and Fig. 3 |
| Variability | Fig. 3 shows a task-count sweep without visible error bars. Independent repetitions and dispersion are unreported in the inspected setup and result text. | pp. 5–6, §IV and Fig. 3 |
| Code and data | The SeaShip dataset is identified through reference 11. The inspected implementation, evaluation and end matter give no author implementation release statement. | pp. 4–6, §III, §IV.A and reference 11 |
| Funding and conflicts | The acknowledgment names two funding sources. The inspected first page and end matter do not document a competing-interest statement. | pp. 1 and 6, first page and Acknowledgment |
| Reported limitations | The authors defer a partitioning scheme to avoid accuracy loss and handling heterogeneous compute and energy supplies. The evaluated configuration assumes homogeneous server compute. | p. 5, §IV.A; p. 6, §V |
