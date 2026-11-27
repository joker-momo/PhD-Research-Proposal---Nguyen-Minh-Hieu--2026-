# Supplemental P08, batch 03 — R0125 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0125.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 3, III.D Experimental Configuration.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | An orchestrator divides video frames among parallel inference workers and recombines their detections. Worker roles are implemented as workstation processes standing in for UAV devices. | pp. 2–3, §§II and III.D |
| Workload | YOLO11m exported to ONNX evaluates urban surveillance video. The video content and resolution are described; the original video source is not identified in the inspected setup. | p. 3, §§III.B and III.D |
| Partition assignment | The system divides input frames spatially with controlled overlap, performs worker-local inference and merges globally mapped detections. | p. 2, §§II.B–D |
| Optimization | The implementation assigns worker threads and frame regions and evaluates adaptive thread reallocation and heterogeneous allocation. The system is evaluated as a parallel implementation on a workstation. | pp. 2–4, §§II, III.D and IV.D–E |
| Compute radio | The implementation documents an AMD workstation and HTTP/JPEG data transfer. The evaluation lacks measured airborne wireless links; the authors identify sensitivity to the link bandwidth. | pp. 3 and 5, §§III.C–D and IV.G |
| Mobility continuity | The paper describes replacement of stateless workers and tests changing thread allocations on a workstation. It does not demonstrate interference, flight motion or real link-disconnection recovery. | pp. 3–5, §§III.C, IV.E and IV.G |
| Evaluation | Inference measurements use workstation processes with varying computational allocations to emulate UAV workers. The platform and video workload are stated in §III.D. | p. 3, §III.D |
| Baselines | Evaluation reports single-worker baselines, parallel worker counts, ideal throughput scaling and comparisons among different resource allocations. | pp. 3–4, §§IV.A–E and Figs. 1–3 |
| Outcomes | Measured workstation outcomes include frame latency, throughput, detection quality and communication overhead; the evidence is specific to the emulated resource setup. | pp. 3–5, §§IV.B–G |
| Variability | The authors show per-frame latency distribution, scaling and heterogeneity sweeps. The inspected setup/results do not establish independent run counts or outcome confidence intervals. | pp. 3–5, §§III.D and IV |
| Code data | The report identifies implementation components and describes workload footage. A release for study source code, raw video or traces is not stated in the inspected sections. | pp. 2–5, §§III–V and end matter |
| Funding conflicts | The Acknowledgment names Canadian natural sciences and engineering research council support. No competing-interest statement is identified in inspected end matter. | p. 5, Acknowledgment and end matter |
| Limitations | The authors state that transfer latency depends on inter-node bandwidth and would increase under constrained wireless conditions, limiting how workstation timing generalizes. | p. 5, §IV.G |
