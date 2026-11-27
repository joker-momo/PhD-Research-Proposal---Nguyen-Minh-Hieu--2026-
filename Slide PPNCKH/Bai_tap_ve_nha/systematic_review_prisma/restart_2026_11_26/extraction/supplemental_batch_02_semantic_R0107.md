# Supplemental P08, batch 02 — R0107 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0107.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, I. INTRODUCTION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Multiple UAV semantic experts process observations from different views. A coordinating UAV fuses representations and sends a task-oriented description over a modeled downlink. | pp. 3–5, §§III.A–C and Fig. 1 |
| Workload | The study tests COCO-based visual question answering, identifies multiple edge expert backbones, and uses a task-specific semantic representation and codec. | pp. 6–7 and 9–10, §IV and §VI.A |
| Partition assignment | Inference uses distributed per-UAV representation extraction and task-guided collaborative fusion, with selectable semantic symbol granularity. | pp. 4 and 6–7, §III.B and §IV |
| Optimization | A two-stage learner jointly adjusts the UAV contribution weights and representation granularity toward task quality under a communication constraint. | pp. 7–9, §V |
| Compute radio | The setup gives a Jetson-class onboard compute profile, modeled channels and a workstation for the PyTorch implementation. The compatibility profile is distinct from on-device flight validation. | pp. 5 and 9–10, §III.C, §VI.A and Table II |
| Mobility continuity | The channel varies in the simulation. No explicit UAV trajectory, loss-based reassignment or recovery evaluation is reported in the inspected methods and results. | pp. 5 and 9–12, §III.C and §VI |
| Evaluation | Simulation on an RTX workstation evaluates collaborative VQA under modeled communication settings. Table II characterizes candidate experts relative to onboard resources. | pp. 9–10, §VI.A and Table II |
| Baselines | The evaluation compares policy learning against PPO and other control variants, then evaluates fusion against expert alternatives and the task-specific best single expert. | pp. 10–12, §§VI.B–E |
| Outcomes | The study reports learning, task quality, granularity control and per-task accuracy. Comparisons against a single expert and controller ablations answer different questions. | pp. 10–12, §§VI.B–F and Figs. 5–9 |
| Variability | The study varies SNR, semantic granularity, task type and training parameters. The inspected evaluation does not establish independent repeat counts or run-level outcome intervals. | pp. 9–12, §§VI.A–F |
| Code data | A COCO-based VQA dataset is named. There is no release route for study code, generated input configurations or simulation scripts in the inspected sections. | pp. 9–12, §§VI.A and VII |
| Funding conflicts | The first page and final pre-reference text do not state study funding or competing interests. | pp. 1 and 12, first page and §VII |
| Limitations | The authors identify inter-UAV exchange overhead, synchronization under heterogeneous delays and onboard real-time implementation as open deployment issues. | p. 12, §VII |
