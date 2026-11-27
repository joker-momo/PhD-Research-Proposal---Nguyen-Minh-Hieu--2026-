# Supplemental P08, batch 02 — R0106 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0106.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, I. INTRODUCTION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | A multi-UAV system coordinates compute among airborne nodes and distributes inference within the airborne group. | pp. 3–4, §III and Fig. 1 |
| Workload | The evaluation uses a layered neural network and software workload profiles. No underlying input dataset is identified in the inspected setup. | p. 10, §V and Table II |
| Partition assignment | The architecture allocates sequential portions of a split neural workload across participating UAVs. | p. 4, §III.A and Fig. 2 |
| Optimization | The study evaluates a learning-based coordination method with centralized training and decentralized execution. | pp. 7–9, §IV |
| Compute radio | The system defines compute and radio models and specifies simulator configurations, distinct from measured airborne deployment. | pp. 4–6 and 10, §III, §V and Table II |
| Mobility continuity | The software evaluation varies node participation and inspects the ability to continue inference after node losses. Hardware recovery is not demonstrated. | pp. 10–13, §V |
| Evaluation | The authors report Python/PyTorch numerical simulation with a GPU for the study configuration. The evaluation is not a live or hardware testbed study. | p. 10, §V and Table II |
| Baselines | The evaluation compares alternative partition policies, learning methods, and component variants. | p. 10, §V |
| Outcomes | The simulation reports task completion and inference-quality measures under alternative conditions. The findings are limited to the described software experiments. | pp. 11–13, §§V.B–D |
| Variability | The evaluation varies study conditions and reports convergence. The inspected results do not state independent trial counts, seeds or outcome uncertainty. | pp. 10–13, §V |
| Code data | No study-specific software, traces or input dataset availability statement is identified in the inspected simulation setup, discussion and end matter. | pp. 10 and 13–15, §§V–VII and end matter |
| Funding conflicts | The funding footnote identifies national and regional grant support. No competing-interest statement is given in the inspected first page and end matter. | pp. 1 and 14–15, funding footnote and end matter |
| Limitations | The discussion reports constraints on transferring a trained policy beyond its configured size. The conclusion identifies topics left to future work, including energy and privacy. | pp. 13–14, §§VI–VII |
