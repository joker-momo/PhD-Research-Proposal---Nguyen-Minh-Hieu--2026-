# Supplemental P08, batch 01 — R0036 source review

Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0036.pdf`. The manifest SHA-256 matched. Physical pages are 1-based. PyMuPDF page text and the original page-layout text were used. Review status is a candidate for the batch composite.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | Each UAV preprocesses its video, and an edge controller selects streams and their configurations for edge-side inference. | pp. 4–5, §III |
| Workload | The study runs YOLOv5 object detection on video frames from the ground-view ETH pedestrian dataset. The source video is divided into ten-second chunks, with candidate spatial and temporal sampling settings. | p. 10, §VI and Fig. 4 |
| Partition and assignment | The assigned unit is a configured video stream or chunk. UAVs sample and resize frames before upload. The edge performs detection on offloaded frames. | p. 4, §III; p. 10, §VI |
| Optimization | Joint stream selection, resolution and frame-rate choices maximize effective weighted surveillance coverage subject to accuracy, delay, bandwidth and edge compute constraints. The method combines a learned accuracy profiler and greedy local search. | pp. 5–6, §§III–IV; pp. 9–10, §V.C and Theorem 2 |
| Compute and radio | The evaluation uses modeled shared bandwidth and edge processing capacity in frames per second. Physical radio and processor implementation for the scenario are unreported. | p. 5, §III; pp. 10–12, §VI and Table II |
| Mobility and continuity | Videos capture target/camera motion, while the multi-UAV scenarios assign surveillance positions and vary system conditions. The inspected experiments establish no evaluated UAV trajectory, handover or failure-recovery mechanism. | pp. 10–12, §VI and Figs. 5–8 |
| Evaluation | Simulations use car-mounted stereo footage as a controlled input and synthesize UAV positions and coverage. They distinguish a single-UAV runtime scenario from multi-UAV coverage tests. | pp. 10–12, §VI and Figs. 4–8 |
| Baselines | Fixed Configuration, Capacity Based Adaptation, All-to-upload, Random-to-upload and an exhaustive-search reference are identified. The latter is an upper-bound reference. | pp. 10 and 12, §VI and Fig. 8 |
| Outcomes | The report compares effective coverage and discusses how changing target dynamics affects detection accuracy and resource conditions. Coverage patterns depend on link bandwidth and compute capacity. It presents a bounded comparison to Random-to-upload for a particular bandwidth setting. | pp. 11–13, §VI and Figs. 6–8 |
| Variability | The authors average 20 Random-to-upload trials per parameter setting and run several scenario sweeps. This supports comparator repeat coverage, with uncertainty or repetitions for SAC2 unreported in the compared settings. | pp. 11–12, §VI, §VI text for Fig. 8 and Figs. 6–8 |
| Code and data | The paper identifies the external ETH dataset. The inspected evaluation, conclusion and accompanying end sections provide no author source-code or custom-data release statement. | p. 10, §VI and dataset reference 40; pp. 13–15, conclusion and end sections |
| Funding and conflicts | Funding sources appear in first-page footnotes. The inspected first page and end sections do not state a competing-interest declaration. | p. 1, footnotes; pp. 13–15, conclusion and end sections |
| Reported limitations | The authors identify further work on spatiotemporal correlations and aerial scene dynamics. The use of ground-view video is an explicit setup choice and limits direct inference about aerial imagery. | p. 10, §VI; p. 13, §VII |
