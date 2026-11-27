# Supplemental P08, batch 03 — R0223 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0223.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 4, 4 Experience.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | A shared language model decomposes tasks across simulated UAV agents. Perception feedback informs the common task graph. | pp. 2–4, method and Figs. 1–3 |
| Workload | The evaluation includes multi-agent planning and perception-plus-planning scenarios in Microsoft AirSim. | pp. 3–5, method and §4 |
| Partition assignment | A controller decomposes and updates shared tasks, using feedback from the agents. This is task-level sequencing and assignment rather than layer partition. | pp. 2–4, method and Fig. 3 |
| Optimization | The paper presents a multi-agent policy variant and task-graph rules. It compares the planning component separately from scenario demonstrations. | pp. 2–5, method and §4 |
| Compute radio | The study names workstation and software components. No physical compute or radio measurements across UAV devices are reported in the experimental setup. | p. 4, §4 Experience |
| Mobility continuity | Simulated scenes vary obstacles and coordination. The inspected results do not describe a measured airborne outage or recovery test. | pp. 4–5, §4 and Fig. 4 |
| Evaluation | The authors identify workstation software experiments using Microsoft AirSim and comparisons implemented in MATLAB. Scene descriptions do not establish field flight. | pp. 4–5, §4 Experience and Fig. 4 |
| Baselines | Table 1 contrasts planning policies under agent and obstacle settings. Table 2 instead contrasts coordination architectures. Neither measures standalone neural inference latency. | pp. 5 and 7, §4 and Tables 1–2 |
| Outcomes | The evaluation reports path length, planning-step time and success, plus separate plan-response time, task completion time and success for coordination experiments. | pp. 4–5 and 7, §4 and Tables 1–2 |
| Variability | Scenarios and group size vary. The coordination tasks were each run at least 30 times as reported. Independent seeding and uncertainty intervals are not specified. | pp. 4–5 and 7, §4 and Tables 1–2 |
| Code data | AirSim scenes and software tools are named. No study implementation or task-prompt release is identified. The authors explicitly note the prompts are omitted. | pp. 4–5, §4 and Conclusion |
| Funding conflicts | No study funding or competing-interest declaration is identified in the inspected first page and end sections. | pp. 1 and 5–6, first page and end matter |
| Limitations | The authors note omitted scenario prompts and identify future work in the conclusion. | p. 5, Conclusion |
