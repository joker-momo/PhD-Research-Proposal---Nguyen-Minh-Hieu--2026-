# Supplemental P08, batch 02 — R0092 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0092.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, I. INTRODUCTION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | The simulated swarm is decentralized, with two UAVs collaborating per inference. The task pipeline is distinct from swarm population; Table IV gives the default and Table X varies it. | pp. 5–6, 10–11 and 15, §III.E and Tables IV and X |
| Workload | The workload uses image minibatches and profiled model configurations, including four networks in Table V and an additional transfer-analysis model. Named source image data are not reported in the setup. | pp. 5, 10, 13 and 14–15, §III.D, §V.A and Table V |
| Partition assignment | Each task can pair its source with a selected neighbor and split a DNN at a candidate layer. The mini-batch pipeline overlaps communication and processing, with a local option. | pp. 5–8, §§III.D–E and IV |
| Optimization | The model uses a Pareto shortlist and DQN to jointly select the partner and partition under variable neighborhood availability and deadline/energy trade-offs. | pp. 6–9, §§III.G and IV |
| Compute radio | The hardware-grounded model represents heterogeneous Jetson-class compute and Wi-Fi 802.11ac airborne links. These radio and compute settings are simulator parameters. | pp. 3–5 and 10, §§III.B–C and V.A |
| Mobility continuity | The simulator models changing neighbors and link interruptions. The design includes assignment or local fallback handling. This is software evaluation rather than field-validated recovery. | pp. 3–4 and 11–12, §III.A, §III.C and §V.E–G |
| Evaluation | A custom Gymnasium simulator and a PyTorch/Stable-Baselines3 learner evaluate a set of common-seed episodes. Named hardware characteristics inform simulated compute profiles. | pp. 10–11, §V.A–C and Table IV |
| Baselines | Collaborative heuristics are tested on a shared two-UAV pipeline, and Local is a separate noncollaborative comparator. Table V distinguishes original EPCTA from its same-substrate adaptation. | pp. 10–11 and 13, §V.B and Table V |
| Outcomes | Under VGG-16 and VGG-19, the proposed method reports higher deadline satisfaction than the strongest same-substrate comparator. Local remains competitive on lighter workloads. Latency in Table V is end-to-end P50. | pp. 11–13, §V.D, §V.G and Table V |
| Variability | Training is assessed over three seeds and main evaluation over 30 independent episodes. The evaluation reports uncertainty, paired significance tests and sensitivity and ablation results. | pp. 10–13, §§V.A–G, Fig. 4 and Table V |
| Code data | The reproducibility paragraph reports source code, environment, baselines and entry points at github.com/cupofcup/DDCI and gives training/test seed settings. | p. 15, §V.J, Reproducibility |
| Funding conflicts | The first page declares funding. The inspected first page and end matter do not contain a competing-interest statement. | pp. 1 and 15–16, funding footnote and end matter |
| Limitations | The article explicitly excludes propulsion power and detailed MAC effects and calls for extending energy modeling to battery balancing. A fully matched DRL backbone study is deferred. | pp. 5–6, 11 and 15, §§III.F–G, V.B and VI |
