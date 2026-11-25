# Protocol Amendment 001

**Date:** 2026-11-24  
**Applies to:** Protocol version 0.1  
**Timing:** After pilot calibration and before any formal database search or final eligibility decision.

## Change

The review scope is narrowed from all UAV-enabled edge-computing systems to distributed DNN inference in UAV swarms and multi-UAV systems.

The effective working title becomes:

> **Distributed DNN Inference in UAV Swarms: A Systematic Review of Partitioning, Orchestration, and Resilience**

The following eligibility condition replaces inclusion criteria 2 and 3 in protocol version 0.1:

1. The evaluated architecture contains at least two UAVs, a UAV swarm, a multi-UAV system, or a FANET.
2. The workload includes DNN, CNN, VLM, or LLM inference whose execution, features, layers, requests, or resources are distributed, partitioned, assigned, migrated, fused, or jointly orchestrated across the swarm or across a multi-UAV–edge/cloud hierarchy.

The following exclusion condition is added:

> Exclude single-UAV-assisted systems in which the UAV serves only ground devices or a terrestrial edge server and no multi-UAV or swarm inference architecture is evaluated.

RQ1 is refined to ask which swarm inference topologies, collaboration patterns, DNN families, and tasks have been evaluated. RQ4 remains focused on mobility, time-varying links, intermittent connectivity, UAV failure, and recovery.

The final search must include at least one swarm-specific term in addition to the inference concept:

```text
("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
 OR "aerial network" OR FANET)
AND
("distributed inference" OR "collaborative inference" OR "cooperative inference"
 OR "split inference" OR "split computing" OR "DNN partitioning"
 OR "model partitioning" OR "layer placement")
```

## Reason

The broader pilot produced 52 provisionally relevant records from a single query and combined two materially different systems: multi-UAV distributed inference and a single UAV acting as an aerial edge server for ground devices. The narrowed scope aligns with the user’s UAV-swarm research direction, supports a coherent synthesis, and is more compatible with the HK261 requirement to study approximately 20 closely related papers.

## Effect on completed work

No formal search, final screening decision, extraction, or synthesis had been completed. The 81-record pilot will be re-screened under the amended scope and retained as calibration evidence. The original protocol remains unchanged for auditability.

