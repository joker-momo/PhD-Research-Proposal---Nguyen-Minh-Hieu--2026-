# Supplemental P08, batch 03 — R0118 source review

`restart_2026_11_26/fulltext_retrieval/pdf/R0118.pdf` matched the manifest SHA-256. All page numbers are physical and 1-based. Codex read the original with PyMuPDF, cross-checked Poppler output where needed and rendered critical source pages.

Body access: p. 9, VI. PERFORMANCE EVALUATION.

| Required field | Source-bounded interpretation | Original physical locator |
|---|---|---|
| Architecture | An airborne swarm hosts distributed expert components. A hierarchical design coordinates software control and expert assignment. The study also evaluates a decentralized control alternative. | pp. 3–4 and 6–9, §§III and V |
| Workload | The study models a mixture-of-experts inference workload with task and expert compatibility. The nominal simulator abstracts inference into inputs. The measured-gate subexperiment uses a CIFAR-100 classifier instantiation; this is not an airborne deployment. | pp. 4–5, 9–11 and 17, §§III.C–D, VI.A–B, measured-gate experiment and VII |
| Partition assignment | Different UAV nodes host different expert components, and inference is assigned to suitable experts. An evaluation contrasts the expert assignment unit with layer-wise inference. | pp. 4, 6–8 and 12, §§III.C, V.B–D and Table V |
| Optimization | The method combines control and expert assignment under latency and communication constraints. A learned decision component is compared with alternative decision rules. | pp. 5–9, §§IV–V |
| Compute radio | The study parameterizes node compute and models wireless communication, interference and deployment resource accounting. The modeled assumptions are not physical radio or compute measurements. | pp. 3–5 and 11–12, §§III.B–D and VI.C |
| Mobility continuity | Software evaluations vary network and mobility conditions, including disrupted connectivity. Some alternative conditions are sensitivity tests under the trained design rather than airborne recovery tests. | pp. 9 and 13–17, §§VI and VII |
| Evaluation | The study uses a software evaluation with multiple seeds and episodes. Physical validation is deferred by the authors. | pp. 9–10 and 17, §VI.A–B and §VII |
| Baselines | The evaluation compares layer-wise execution, candidate routing and control rules, and ablated configurations. Conditions are separately fixed for different comparison tables. | pp. 9 and 11–15, §VI.B–F and comparison tables |
| Outcomes | Completion, latency and resource use are reported in simulation. Interpret results by comparison table and operating condition; the review does not extend them to real flight. | pp. 9–16, §VI and Tables III–XII |
| Variability | The paper reports three-seed evaluation and many episodes, uncertainty intervals, component ablations and sensitivity to modeled conditions. | pp. 9–17, §VI, Tables V–XII and §VII |
| Code data | The authors provide the code and simulation environment route github.com/traumasv/NetMoE-IoTJ in a source footnote. Review verification establishes the printed route. | p. 9, §VI.A footnote |
| Funding conflicts | The Acknowledgment discloses grant support. The inspected first page and end matter do not give a separate competing-interest statement. | pp. 1 and 17–18, first page and Acknowledgment |
| Limitations | The authors bound the evidence to simulation, discrete motion, abstracted expert accuracy and future real-testbed validation. | p. 17, §VII, Limitations and future work |
