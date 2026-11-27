# Supplemental P08, batch 01 — R0075 source review

Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0075.pdf`. The manifest SHA-256 matched. Physical pages are 1-based. PyMuPDF page text and the original layout text were used.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Assistant UAVs compute branches of a multi-exit student model and transmit selected intermediate features. A master forms the final prediction from its own representation and the received features. | pp. 4–5, §III.A–C |
| Workload | CIFAR-10 and CIFAR-100 image classification with Wide Residual Network teachers and lighter multi-exit students. The experiment uses classification benchmarks in place of aerial imagery. | pp. 8–9, §IV.A and Table I; p. 13, §IV.E |
| Partition and assignment | The offline alignment method assigns ranked teacher feature channels to student branches using device-capacity allocation and deterministic overlap. The master can select different exit depths for different assistants. | pp. 4–5, §III.C; pp. 6–8, §III.D and Algorithm 1 |
| Optimization | The sequential LinUCB exit router uses confidence and modeled computation, communication and synchronization costs, learns on the validation split and is frozen during testing. | pp. 6–8, §III.D and Algorithm 1; pp. 9–10, Tables II–III |
| Compute and radio | Local sequential execution is profiled on a Jetson TX2. The network experiment uses modeled Rician fading and sets or sweeps feature-stream rates. | pp. 8–9, §IV.A and Table I; p. 11, §IV.C |
| Mobility and continuity | Time-varying link rates, bandwidth sweeps and assistant waiting are represented. The reported setup does not establish live mobility, a node-failure test or restart performance. | pp. 8–9, §IV.A; p. 11, §IV.C; p. 13, §IV.E |
| Evaluation | Hardware profiles feed a simulation with saved channel traces and separate validation/test roles. It is a profiled simulation of routing, with no full distributed on-device deployment reported. | pp. 8–10, §IV.A–B and Tables I–III; p. 13, §IV.E |
| Baselines | Random, epsilon-greedy and similarity-based exit, AdaEE, COBEE, Full Final Exit, and Offline Oracle final-agreement are compared. The oracle knows future information and is a reference bound. | pp. 9–10, §IV.B and Table III |
| Outcomes | Under Table III conditions CIDER reduces routing-controlled computation and communication latency relative to Full Final Exit and reports lower accuracy than that comparator. The trade-off varies by comparator and dataset. The measured boundary excludes multiple sensing-to-output stages and overheads. | p. 10, Table III and §IV.B; p. 13, §IV.E |
| Variability | The analysis includes swarm-size, rate, and other sensitivity tests. Table III gives point results. The confidence-target ablation separately gives dispersion; do not use it as uncertainty for the main comparison. | pp. 10–13, Table III, §IV.C–D and Table XIV |
| Code and data | CIFAR-10 and CIFAR-100 are externally sourced benchmarks. The inspected methods, setup and end sections do not identify an author artifact release. | pp. 4–9, §§III and IV.A; pp. 13–15, §IV.E and end sections |
| Funding and conflicts | First-page footnote discloses project funding. The inspected first page and end sections do not state a competing-interest declaration. | p. 1, footnotes; pp. 13–15, §IV.E and end sections |
| Reported limitations | The paper defines a limited routing latency boundary and calls for aerial imagery, full-device evaluation and measurement of excluded components. It also identifies scaling, straggler and open-link feature protection concerns. | pp. 13–14, §IV.E |
