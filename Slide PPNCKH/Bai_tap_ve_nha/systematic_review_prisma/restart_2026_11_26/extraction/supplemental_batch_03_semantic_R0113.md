# Supplemental P08, batch 03 — R0113 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0113.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 9, IMPLEMENTATION AND RESULTS.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | The framework combines onboard event-driven processing, continual adaptation and a graph of UAV peers that share processed representations for local cooperative decisions. | pp. 5–8, Methodology |
| Workload | The sensing workload uses event-camera spike streams and a spiking neural network for navigation decisions. The paper evaluates sequential learning tasks in varied scenario types. | pp. 5–6 and 9–11, Methodology, Implementation and Results, Table 2 |
| Partition assignment | The design exchanges compact semantic or graph representations among neighbors; it does not present collaborative execution by splitting contiguous neural layers. | pp. 7–8 and 12, Methodology and Scalability Analysis |
| Optimization | The paper describes continual learning with replay and weight consolidation, graph-based coordination and a reinforcement-learning objective for navigation. | pp. 6–9, Methodology and Implementation and Results |
| Compute radio | The study describes low-power edge compute and names software components and simulators. The reporting does not fully specify the onboard compute and radio configuration of each comparative result. | pp. 5–9, Methodology and Implementation and Results |
| Mobility continuity | Environmental and communication changes are considered in the design and scenario descriptions. Fully specified link interruption and recovery measurement conditions are not provided for the reported comparisons. | pp. 8–10 and 12, Methodology and Implementation and Results |
| Evaluation | The authors report simulated swarm experiments and describe hardware-in-the-loop activity on embedded platforms. The text does not identify how every tabulated outcome maps to the two evaluation modes. | pp. 9–13, Implementation and Results, Tables 1–4 |
| Baselines | Table 1 presents CNN, vision-transformer and conventional SNN alternatives. Table 4 compares components of the proposed stack in an ablation. | pp. 10 and 13, Tables 1 and 4 |
| Outcomes | The tables report navigation, continual retention, scalability and component outcomes. This review retains qualitative categories because correspondence between reported measures, implementation modality and matched conditions is incomplete. | pp. 10–13, Tables 1–4 |
| Variability | The report varies scenario, learning task, swarm scale and ablative configuration. The inspected Methods and comparative results do not state independent repeated-run counts or uncertainty intervals. | pp. 9–13, Implementation and Results |
| Code data | No exact study code or data release is identified in the implementation sections, conclusion and end matter. Named third-party frameworks do not establish release of this study. | pp. 9 and 14–17, Implementation and Results, Conclusion and References |
| Funding conflicts | The inspected first page, conclusion and end matter contain no explicit study funding or competing-interest statement. | pp. 1 and 14–17, first page and end matter |
| Limitations | The authors identify further dynamic edge and multimodal extensions. A dedicated discussion tracing limitations of the reported evaluations is not given in the inspected conclusion. | pp. 14–16, Conclusion and future research paragraph |
