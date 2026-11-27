# Supplemental P08, batch 03 — R0292 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0292.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 3, 4 COOPERATIVE CONTINUOUS TRACKING.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | The design coordinates two UAV tracking roles and transfers tracking information so a receiving UAV can continue monitoring. | pp. 3–4, system setup and §4.1 |
| Workload | The tracker comparison uses a custom set of aerial marine footage, with changing views, partial occlusion and background noise. | pp. 3–4, dataset description and §5.1 |
| Partition assignment | Handoff exchanges tracking state at task level. Matching and onboard tracking are separate from neural-layer partition. | pp. 4–5, §4.1 and §5 |
| Optimization | The study describes tracker selection, feature matching, template padding and onboard implementation optimization. It tests configuration alternatives rather than an offloading optimizer. | pp. 3–6, method, §5 and Table 3 |
| Compute radio | The design names onboard Jetson and ROS/flight-stack integration and Wi-Fi transfer. Power and compute measures refer to the reported HIL operation. | pp. 3–6, setup, §4.1, Fig. 5 and discussion |
| Mobility continuity | The design addresses planned handoff of monitoring. Validation tests tracking and feature matching, and explicitly identifies the onboard system test as hardware-in-the-loop. | pp. 4–6, §4.1, §5 and §6 |
| Evaluation | The study compares trackers on recorded footage and reports hardware-in-the-loop operation including tracking, matching, coordination and navigation logic. | pp. 4–6, §5.1, Fig. 5 and §6 |
| Baselines | Tracker alternatives are compared on marine footage. The handoff experiment varies template padding to assess matching separately. | pp. 4–5, §5.1 and Tables 2–3 |
| Outcomes | Results cover tracking accuracy, matching coverage and persistence, and onboard rate, power and compute behavior. Footage and HIL results support different claims. | pp. 4–6, §5 and Tables 2–3 |
| Variability | The evaluation varies tracker and matching settings. It does not specify independent mission repetitions or uncertainty for the handoff outcomes. | pp. 4–6, §5 and Tables 2–3 |
| Code data | The authors describe a custom footage dataset and named trackers. The inspected text does not identify a release for study data, coordination code or HIL configuration. | pp. 3–6, Methods, §5 and §6 |
| Funding conflicts | No study funding or competing-interest declaration is identified in the inspected first page and end matter. | pp. 1 and 6, first page, conclusion and References |
| Limitations | The authors note differing viewpoints and incomplete bounding-box alignment in the matching results. There is no dedicated limitations discussion in the conclusion. | pp. 5–6, §5 and §6 |
