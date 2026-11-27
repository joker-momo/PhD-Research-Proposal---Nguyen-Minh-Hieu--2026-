# Supplemental P08, batch 02 — R0090 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0090.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 1, I. INTRODUCTION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | A layered flying-edge system uses coordinated UAVs with onboard inference, ground sensor connections and optional cloud synchronization. | pp. 2–3, §II and Figs. 2–3 |
| Workload | The paper describes crop-pest detection, vegetation and soil monitoring, and yield prediction. It reports lightweight CNN edge benchmarking, but does not identify specific input datasets for those benchmarks. | pp. 4–5, §§IV and V.J |
| Partition assignment | Onboard inference tasks are assigned or reassigned across drones. The cited design is task-level allocation with local inference; no layer-level split is described in the relevant sections. | pp. 2–3, §§II.B and III.B |
| Optimization | Coverage coordination and energy-aware task allocation support the design, alongside a redundancy and consensus policy. A reproducible mathematical allocation objective is not given in the inspected architecture sections. | pp. 2–3, §§II–III |
| Compute radio | The field-prototype description identifies camera/sensor connections, Raspberry Pi and Coral devices, LoRaWAN-connected IoT sensors and ROS coordination. Hardware descriptions are distinct from unreported radio parameters. | pp. 3–4, §§II.D and V.E |
| Mobility continuity | The design describes self-healing connectivity and redundant reassignment. Dropout and packet-loss results are reported, with no explicit link assigning the individual dropout comparison to the hardware field prototype. | pp. 3 and 5–6, §§II.D, III.B, V.F and V.K |
| Evaluation | The authors describe simulation with NS-3, ROS, Gazebo and MATLAB UAV Toolbox and a separate author-reported DJI/Raspberry Pi/Coral field prototype. | p. 4, §V.E |
| Baselines | The paper identifies two comparator classes: conventional centrally tasked UAVs and cloud-based monitoring. Detailed reproduction of comparator hardware and network parity is not established by that summary. | p. 5, Results and Discussion opening |
| Outcomes | Reported measures include decision and inference latency, energy and completion under load or dropout. Simulated and emulated conditions are explicitly named for some measures; modality is not assigned figure-by-figure. | pp. 5–6, §§V.F–L, Figs. 5–8 |
| Variability | The paper varies coordinated swarm load and dropout conditions. The text and comparison figures inspected do not establish independent repeat counts or uncertainty intervals. | pp. 5–6, §§V.H and V.K, Figs. 5 and 8 |
| Code data | The simulation tools and prototype components are named, but no study code, data or artifact release is given at the inspected locations. | pp. 4 and 6, §V.E, conclusion and References |
| Funding conflicts | The inspected first page and end sections lack study funding and competing-interest statements. | pp. 1 and 6, first page, conclusion and end matter |
| Limitations | The discussion and conclusion describe intended benefits without an explicit limitations or threats-to-validity statement. | p. 6, §§V.L and VI |
