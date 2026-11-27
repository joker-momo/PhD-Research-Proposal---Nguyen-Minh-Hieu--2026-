# Supplemental P08, batch 01 — R0058 source review

Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0058.pdf`. The manifest SHA-256 matched. Physical pages are 1-based. PyMuPDF, Poppler layout text and original renderings of pp. 5, 9 and 10 were used.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Autonomous UAVs generate inference tasks and ground edge servers execute eligible offloaded tasks. A distributed auction coordinates UAV bids and server resource offers. | pp. 5–6, §3.1 and Fig. 1; p. 9, §4 |
| Workload | Simulated ResNet-18 image classification tasks use random draws from CIFAR-10 test images, with task input, output and computation sizes specified in the simulator configuration. | p. 19, §6.1 |
| Partition and assignment | The task-to-server decision is binary with at most one server per task. Local or deferred operation is described as a fallback. No split by model layer appears in the evaluated assignment variable. | pp. 5–6, §3.1; pp. 9–10, §4.1; p. 11, §4.2 |
| Optimization | The formulation considers latency and accuracy with connection and compute constraints. Buyers and sellers separately evaluate bids and service costs, and the auction objective maximizes aggregate utility subject to feasibility. | pp. 8–9, §3; pp. 11–12, §4.2; pp. 14–16, §§4.4–5 |
| Compute and radio | The simulator uses modeled sub-6 GHz links with prescribed bandwidth and compute budgets. The source’s stated default server count falls outside its stated range. Preserve that conflict and avoid assigning a default for reported plots. | p. 19, §6.1; pp. 20–22, §§6.2–6.3 |
| Mobility and continuity | The design estimates remaining connection time and describes retry, buffering or simplified local operation. A system-level task-success test varies simulated UAV speed and does not isolate retry or fallback. | pp. 9–10, §4.1; pp. 21–22, §6.3 and Fig. 4 |
| Evaluation | Discrete-time simulator with modeled ground servers, moving UAVs and an image-classification workload. The paper reports no hardware or live-flight trial in §6. | pp. 19–22, §6.1–6.4 |
| Baselines | Compares local-only, MWBS, LADPO and OATS schemes. Section 6 identifies the comparators by scheduling approach. | pp. 19–20, §6.1 |
| Outcomes | Reports latency, accuracy and task success under separate sweeps over server frequency, system scale and UAV speed. In the matched 1,500 MHz scenario, the text supplies direct latency and accuracy comparisons with MWBS. Keep results within those simulation conditions. | pp. 20–22, §§6.2–6.3 and Figs. 2–4 |
| Variability | Task-success distributions in Fig. 4 and experimental sweeps are available. The latency and accuracy plots provide no precision interval. Convergence criteria and plotted distributions do not establish independent-repeat counts. | pp. 19–22, §§6.1–6.3 and Figs. 2–4 |
| Code and data | Tasks use the external CIFAR-10 test set. The inspected setup, conclusion and end matter do not give an implementation or simulation-script release. | pp. 19 and 23–25, §6.1, conclusion and end matter |
| Funding and conflicts | No funding declaration or competing-interest statement appears in the inspected front and end matter. The ORCID listing is separate from a declaration. | pp. 1–2 and 23–25, front matter, conclusion and end sections |
| Reported limitations | The conclusion states results under simulated conditions. No dedicated author limitations or field-validation result is supplied in the inspected conclusion. The inconsistent server default is a review observation. | pp. 19 and 23, §6.1 and §7 |
