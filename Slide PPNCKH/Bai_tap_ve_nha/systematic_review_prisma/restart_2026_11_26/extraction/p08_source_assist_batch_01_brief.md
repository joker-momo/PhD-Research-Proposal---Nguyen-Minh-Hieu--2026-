# TASK

Verify original PDF evidence for exactly 27 still-pending P08 field keys in HK261 Batch 01.

# REQUIRED WORK

1. Read only the authorized original PDFs listed below using the attached canonical project folder. For each PDF, start by locating an exact short contiguous excerpt on a body page. If you cannot read the PDF or find the excerpt, report which ID and why. Do not infer details from abstracts.
2. Check each listed assertion against the full text, table or figure and its setup. Physical pages start at 1. For absence claims, give the physical pages and sections actually inspected. Use local PyMuPDF, then MinerU for unresolved layout, then Marker if MinerU remains unclear, only if those tools are available. Report unavailable tools and use the original PDF.
3. Distinguish exact values and approximate values, units, comparator, denominator, workload and conditions. If a clause overgeneralizes the source, return PARTIAL and identify exactly which clause. Treat proposed statements as claims to check.
4. Use one parent Task. You may divide work internally if that capability is available. No key may be assigned twice. Report actual worker assignments or that no workers were used. Return one consolidated result.

PDFs:

- `R0044` → `restart_2026_11_26/fulltext_retrieval/pdf/R0044.pdf`
- `R0048` → `restart_2026_11_26/fulltext_retrieval/pdf/R0048.pdf`

Exactly these keys and assertions:

- `R0044` `uav_architecture_role_and_topology:1` | physical p. 6 | 4 UAVs at fixed altitude H=100 m (circular flight at 10 m/s, radius R=200 m) act as MEC servers for mobile devices (MDs) with 1 BS at (200,200) m as fallback cloud server.
- `R0044` `inference_model_task_and_dataset:1` | physical p. 7 | Evaluated on AlexNet (default), TinyYOLOv2, NiN, and VGG16; feature extraction (conv/pool) offloaded, FC layers run on MD; dataset not named.
- `R0044` `partition_and_assignment:1` | physical p. 3 | Input/feature maps partitioned row-wise along height using Arbitrary Input Range (AIR) backtracking across conv/pool layers into N_m independent subtasks offloaded to UAVs.
- `R0044` `decision_variables_objectives_constraints_and_solver:1` | physical p. 6 | LaCPOO combines subgradient projection and CPOO; transmission powers are updated using KKT conditions.
- `R0044` `compute_and_radio:1` | physical p. 6 | MD compute 1 GHz, UAV compute 4-8 GHz (8 DP FLOPS/cycle), MD max tx power 2 mW, G2U bandwidth b0=10 MHz, G2B bB=15 MHz, noise -100 dBm, fading mean 2 / var 0.4, reliability threshold 0.9.
- `R0044` `mobility_channel_intermittency_failure_and_recovery:1` | physical p. 3 | For failed return data under unreliable connections, the mobile device sends the whole task to the base station for reprocessing using maximum device transmission power.
- `R0044` `evaluation_platform_simulator_hardware_and_traces:1` | physical p. 6 | The simulation distributes mobile devices across a square area and employs four clockwise-moving UAV edge servers at a fixed altitude with the base station at the centre.
- `R0044` `baselines_and_workloads:1` | physical p. 7 | The comparison includes local execution, RPOM and Edgent-P.
- `R0044` `sensitivity_and_variability:1` | physical p. 7 | In the bandwidth sweep all compared algorithms reduce average inference delay as bandwidth increases.
- `R0044` `code_and_data:1` | physical p. 8 |  | Verify whether the field is reported and document sections inspected.
- `R0044` `funding_and_conflicts:1` | physical p. 8 |  | Verify whether the field is reported and document sections inspected.
- `R0044` `funding_and_conflicts:2` | physical p. 8 |  | Verify whether the field is reported and document sections inspected.
- `R0044` `reported_limitations:1` | physical p. 8 |  | Verify whether the field is reported and document sections inspected.
- `R0048` `uav_architecture_role_and_topology:1` | physical p. 10 | Scalable UCAA supporting 5-200 UAVs hovering at 200 m over 500m x 500m area: centralized BS mode (JDTSO) for <=20 UAVs and distributed Dec-POMDP mode (MAPDP) for >20 UAVs.
- `R0048` `inference_model_task_and_dataset:1` | physical p. 9 | Real-time video analytics (vehicle/person attribute recognition) using background subtractor ROI extraction (every 10 frames) + YOLOv3-tiny classifiers arranged as a branching DAG.
- `R0048` `partition_and_assignment:1` | physical p. 7 | Classifier-level DAG partitioning (enumerated partition points C) with offloading U_v,i^v' to neighboring UAVs.
- `R0048` `decision_variables_objectives_constraints_and_solver:1` | physical p. 2 | Centralized JDTSO uses genetic-algorithm positioning and dynamic programming with DAG partitioning for scheduling. Distributed MAPDP combines MAPPO and DAG partitioning.
- `R0048` `compute_and_radio:1` | physical p. 9 | 2 UAV hardware types: RPi 3B+ with Intel Movidius NCS1 (0.25 s latency, 6 W) and NCS2 (0.2 s, 5.6 W); UAV-UAV 2 GHz LoS (P_v=30 dBm), UAV-BS 28 GHz mmWave, total bandwidth 20 MHz, noise -174 dBm, hovering power 60 W.
- `R0048` `mobility_channel_intermittency_failure_and_recovery:1` | physical p. 12 | UAVs hover at 200 m with minimum separation d_min=10 m and LoS attenuation 5 dB; trajectory planning, turning/climb constraints, and failures deferred to future work.
- `R0048` `evaluation_platform_simulator_hardware_and_traces:1` | physical p. 9 | Implemented in Python 3.8.19, PyTorch 2.3.0, OpenCV 3.2.0, CVXPY on Intel Core i7-13700KF CPU + 2x RTX 4090 24 GB GPUs using measured RPi 3B++NCS1/NCS2 latency/power.
- `R0048` `baselines_and_workloads:1` | physical p. 10 | The comparison uses C-PPO, C-DQN, MADDPG, Random and IND-UAV.
- `R0048` `outcomes_latency_energy_communication_accuracy_reliability_and_scalability:1` | physical p. 12 | JDTSO achieves lowest latency/energy and highest throughput for <=20 UAVs (times out >20); MAPDP outperforms all baselines for 40-200 UAVs (Fig. 3-8); Table III reports 60-UAV metrics (0.511-0.515 s, 596.1-778.7 J, 116.6-117.4 IPS).
- `R0048` `sensitivity_and_variability:1` | physical p. 12 | Evaluated learning rates (0.05, 0.005, 0.0005, Fig. 9-11), UAV scales (5-200 with box plots Fig. 4, 6, 8), and energy efficiency phi_v (0.6, 0.7, 0.8 in Table III).
- `R0048` `code_and_data:1` | physical p. 12 |  | Verify whether the field is reported and document sections inspected.
- `R0048` `funding_and_conflicts:1` | physical p. 1 | Supported by NSFC Grant 62472332 and Hubei Provincial International S&T Cooperation Project 2024EHA031.
- `R0048` `funding_and_conflicts:2` | physical p. 1 |  | Verify whether the field is reported and document sections inspected.
- `R0048` `reported_limitations:1` | physical p. 12 | Authors note future work must add trajectory planning, kinematic constraints (turning radius, climb rate), and inter-UAV interference.

# REQUIRED OUTPUT

Return compact JSONL, one object per key. Allowed status: SUPPORTED, PARTIAL, CONTRADICTED, UNVERIFIED, NOT_ACCESSIBLE. Use null where inapplicable. Schema example (synthetic values):
{"report_id":"RXXXX","evidence_key":"results:1","status":"SUPPORTED","pdf_relative_path":"folder/file.pdf","physical_pages":[4,5],"section_or_table_or_figure":"§IV, Table II row A","excerpt_or_cell":"short contiguous excerpt","value_as_printed":"3","units":"ms","baseline":"A","workload":"model B","conditions":"scenario C","rationale":"Both sections were inspected. Table II row A reports the result."}
Add the returned count, unresolved keys and reasons, PDF access probe results, worker status with assignments if used, and final marker P08_B01_SOURCE_ASSIST_COMPLETE.

# ACCEPTANCE CRITERIA

- 27/27 exact keys or explicit shortfall. Zero duplicates or out-of-scope keys.
- Every SUPPORTED key has a valid original PDF path and physical page, section or figure or table, and an exact contiguous excerpt or identifiable cell. For an explicit absence call, record sections and pages inspected.
- Zero accepted quantities missing their original value, units, comparator, workload or measurement conditions. Unknown conditions are not assumed.
- Every unresolved key and reason is listed. Zero unsupported or invented evidence.

# BOUNDARIES

Read only the listed PDFs. Do not edit any files, upload PDFs, change study decisions, or draft manuscript text. Do not review keys already accepted or adjudicated. Treat the summary lines as hypotheses. When facts or access cannot be verified, report the shortfall.
