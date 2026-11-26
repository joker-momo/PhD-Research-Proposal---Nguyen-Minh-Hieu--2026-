# AVSTC Seed Grant — Section 5: Project Proposal

**Project Title:**
Resilient Collaborative Edge Inference in UAV Swarms: A Joint Computation–Communication Optimiser and Open Co-Simulation Testbed for Disaster-Response Connectivity

**Preferred start and end dates (6 months):** 01/11/2026 – 30/04/2027

---

## Background and Motivation

UAV swarms are becoming essential instruments for disaster response, search-and-rescue and infrastructure inspection — mission profiles of direct national relevance to Vietnam, where annual storms and flooding routinely disable ground communication infrastructure. Delivering onboard AI perception in these settings faces a structural mismatch: modern deep neural networks (DNNs) exceed the Size, Weight and Power (SWaP) budget of any single small UAV, while offloading to cloud or edge servers presupposes the very connectivity that has failed. Collaborative Edge Inference (CEI) resolves this by partitioning a DNN across the swarm, so that the collective executes what no individual can.

The difficulty is that partition boundaries determine intermediate tensor sizes, which in turn govern transmission delay and RF energy over a volatile Flying Ad-Hoc Network (FANET). Computation and communication costs are therefore coupled and cannot be optimised independently. A second gap is more consequential: when a UAV fails mid-inference, existing systems possess no recovery semantics and implicitly restart the request from the first layer, discarding work already completed correctly.

## Objectives

This six-month project delivers the foundational layer of that agenda:

**O1.** Formulate and solve the joint optimisation of bounded-K DNN partitioning and UAV assignment, minimising end-to-end latency and total energy under coupled SWaP and FANET constraints, and characterise the regimes in which increasing K ceases to pay for its communication overhead.

**O2.** Design and implement *reactive mid-inference recovery*: upon node failure, re-derive partition boundaries over the surviving topology and resume from the last delivered intermediate activation rather than restarting.

**O3.** Build and openly release a network–robotics co-simulation testbed enabling reproducible evaluation of collaborative inference over aerial networks.

## Research Program and Activities

**Months 1–2 — Formulation and testbed foundation.** Formalise the joint problem as minimisation of L(x) + λE(x) over partitioning and assignment variables, with the feasible set defined by per-node compute, memory and energy limits, FANET link constraints and sequential execution order. Profile representative detection models (YOLO-class, ResNet-class) to obtain per-layer compute cost and activation size on a Jetson-class reference platform. Stand up the co-simulation environment integrating NS-3 (FANET) with ROS/Gazebo (mobility) and PyTorch (inference).

**Months 3–4 — Optimiser and regime analysis.** Implement exact solution for small K and tractable approximations for larger instances; the closely related joint partitioning–offloading problem is known to be NP-hard, motivating the bounded-K restriction. Characterise the latency–energy Pareto frontier as a function of K, link quality and swarm size, identifying the operating regimes where communication overhead dominates. Benchmark the joint optimiser against a sequential partition-then-assign baseline representing decoupled practice.

**Months 5–6 — Reactive recovery and evaluation.** Implement the recovery mechanism: telemetry-triggered failure detection, boundary re-derivation for the unfinished sub-model, tensor rerouting over the surviving topology, and resumption from retained activations. Evaluate under stress scenarios (node dropout, link disruption, varying mobility) against three named baselines: sequential optimisation, static joint optimisation without re-derivation, and full restart. Report end-to-end latency, total energy, recomputation overhead and service continuity. Prepare one conference paper and a public code release.

## Anticipated Outcomes

1. **A validated joint optimisation formulation** for bounded-K collaborative inference with communication cost endogenous to the partitioning decision, together with analytical characterisation of the role of K.
2. **A working reactive recovery mechanism** demonstrating measurable reduction in recomputation after mid-inference node failure relative to the restart behaviour implicit in current systems.
3. **An open co-simulation testbed** (NS-3 + ROS/Gazebo + PyTorch) released publicly, with reproducible scenario configurations — a reusable asset for AVSTC partners and the wider community.
4. **One peer-reviewed conference paper** co-authored with the Australian collaborator, submitted within the grant period.
5. **A technical report and demonstration** presented to industry partners, positioning the work for follow-on funding.

## Potential Impact

**Scientific.** The project supplies the missing recovery semantics for distributed inference on volatile networks. Checkpoint-and-resume is standard in datacentre training but has never been brought to inference pipelines on aerial networks, where the resume point is an activation distributed across moving nodes and re-planning is itself an optimisation problem.

**Practical and national.** Vietnam faces recurring natural disasters in which ground communication infrastructure fails precisely when aerial situational awareness matters most. A swarm that sustains AI perception without any external infrastructure — and survives the loss of individual aircraft — directly serves that need. The three-layer formulation also transfers to ground robot fleets and maritime platforms.

**Collaboration and industry.** The work sits at the intersection of AVSTC priority areas: AI, robotics and next-generation connectivity. It establishes a concrete joint artefact — shared code, shared data, a shared paper — between HCMUT and the Australian partner institution, providing the foundation for larger follow-on proposals under AVSTC Phase II. The testbed and resilience metrics are directly relevant to industry partners in aerial networking and counter-UAS.

**Risk management.** Two risks are anticipated with pre-committed fallbacks. If co-simulation integration slips beyond Month 2, evaluation proceeds network-only in NS-3 with trace-driven compute delays, so the optimiser work is never blocked. If no useful approximation emerges for larger K, the scope narrows to exact solution at small K plus systematic empirical characterisation of the trade-off surface — still delivering Outcomes 1–3.

---

## ⚠️ CẦN ĐIỀN / SỬA TRƯỚC KHI NỘP
- Tên cộng tác viên Úc + tổ chức (thay "the Australian collaborator")
- Ngày bắt đầu/kết thúc: hiện để 01/11/2026 – 30/04/2027, chỉnh nếu thầy muốn khác
- Nếu có tên hội nghị mục tiêu cụ thể → thêm vào Outcome 4
- Nếu ban tổ chức yêu cầu tiếng Anh Anh/Mỹ nhất quán: hiện dùng Anh-Anh (optimise, characterise)
