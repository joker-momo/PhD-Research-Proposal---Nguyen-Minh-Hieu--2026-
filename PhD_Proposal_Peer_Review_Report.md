# Peer Review Report (Simulated 5-Reviewer Panel)

## Manuscript Information
- **Title**: Adaptive Joint Computation–Communication Optimization in UAV Swarms (working title, from header: *Adaptive Joint Computation-Communication in UAV Swarms*)
- **Author**: Nguyễn Minh Hiếu
- **Document type**: PhD Research Proposal (pre-execution; no results yet)
- **Review mode**: `academic-paper-reviewer` — full mode (5-perspective panel), adapted for a *proposal* rather than a completed manuscript — "Methodology" is scored as *planned rigor*, "Evidence" as *the strength of the case for the approach*, not executed findings.
- **Review date**: 2026-07-07

---

## Reviewer Panel Configuration

| Role | Configured identity | Focus |
|---|---|---|
| EIC | Editor, IEEE-style systems/networking venue (e.g. *IEEE Transactions on Mobile Computing* / *IEEE Communications Magazine* tier) | Fit, positioning, overall viability as a 3-year PhD program |
| R1 – Methodology | Combinatorial optimization + edge-computing systems reviewer | Problem formulation, bounded-$K$ model, complexity claims, evaluation design |
| R2 – Domain | FANET / UAV networking reviewer | Literature coverage, technical correctness of communication claims, domain positioning |
| R3 – Perspective | Cross-disciplinary reviewer (robotics + mobile networks + broader impact) | Generalizability, real-world deployability, dual-use/ethical framing |
| Devil's Advocate | Adversarial stress-tester | Strongest counter-arguments against the novelty and evidentiary claims |

---

## R-EIC: Editor-in-Chief Review

**Recommendation**: Minor Revision (proposal is soundly positioned; needs sharper specification before it can anchor 3 years of committed work)
**Confidence**: 4/5

**Summary**: The proposal targets a real and well-documented mismatch — small UAVs' SWaP limits vs. the compute demands of modern DNNs — and stakes out a specific, checkable niche: joint bounded-$K$ partitioning + assignment optimization with communication cost embedded in the objective, plus online re-optimization for FANET volatility. The RQ → Gap → Contribution → Objective chain (Research Objectives section) is unusually clean for a proposal at this stage, and the comparative literature table gives the novelty claim a falsifiable basis rather than a rhetorical one. The main open question is not "is this worth doing" but "is it specified precisely enough yet" — several load-bearing terms ($K$, the FANET link model, the online-adaptation method family) are named but not yet pinned down, which is fine for Objectives 1–3 to resolve in Year 1, but the reader currently cannot tell if the plan is right-sized for 36 months or unify committed to too many mechanisms (bounded-$K$ theory *and* a communication-cost model *and* an online controller *and* three publications). Fit for a systems/networking venue is good; fit for a controls/optimization-theory venue would need Objective 1's analytical contribution stated more concretely.

**Strengths**:
- **S1 — Falsifiable gap claim.** The Table 1 comparison (Literature Review §6) lets a reader verify "no row has ✓ in all four columns" independently — this is much stronger than a prose-only gap claim.
- **S2 — Clean RQ traceability.** Every contribution and concrete objective in Research Objectives cites back to a specific RQ and gap number; this discipline will make the eventual thesis easy to defend.
- **S3 — Appropriately matched validation environment.** NS-3 + ROS + Gazebo co-simulation (Objective 4, Methodology Phase 3) is the field-standard combination for network+robotics claims, not an over- or under-built choice.

**Weaknesses**:
- **W1 — $K$ is never bounded.** "Research Methodology" states $K$ "is restricted to a small value" but no range, rule, or relationship to UAV count/DNN depth is given anywhere in the document. *Severity: Major.* Suggestion: state even a placeholder rule (e.g., "$K \le$ number of available UAVs, and $K \le 8$ based on [prior work's] tractability limit") so Objective 1 has a concrete target.
- **W2 — Publication cadence risk.** Three first-author papers are scheduled at Months 12, 24, 30 (Research Plan and Timeline), each immediately followed by the next phase, with no slack for the 3–9 month review-and-revise cycle typical of IEEE Trans-level venues. *Severity: Major.* Suggestion: either target workshop/magazine venues for faster turnaround on Papers 1–2, or add explicit buffer/parallelism in the Gantt-style plan.
- **W3 — Risk section is generic.** "Risk Considerations" (end of Methodology) names three risks in one sentence each with no decision criteria (e.g., what happens if Phase 1's combinatorial problem turns out to have no useful approximation). *Severity: Minor.* Suggestion: convert to a short risk table with trigger condition → fallback plan, one row per Objective.

---

## R1: Methodology Review (Combinatorial Optimization / Edge Systems)

**Recommendation**: Major Revision (on the *planned* rigor — the direction is sound but under-specified for execution)
**Confidence**: 5/5

**Summary**: The core formulation $\min_x L(x) + \lambda E(x)$ over a bounded-$K$ partition family is a reasonable and standard way to make DNN-partitioning-for-UAVs tractable, and the acknowledgment that the problem is combinatorial and exponential in partition points × UAV nodes (Methodology, "Computational Complexity") is honest rather than hand-waved. However, the proposal stops at "restricted to a small value to balance analytical tractability against communication overhead" without stating *how* $K$ will be chosen, what complexity class the bounded-$K$ problem falls into (the text implies NP-hardness by analogy but never states or cites a hardness result), or what approximation guarantee (if any) is targeted. The preliminary Pareto analysis (Fig. 1) is described as coming from "a simplified simulation under homogeneous UAV capabilities and static links" — this is a reasonable illustrative device, but the trade-off it shows (finer partitioning → more communication, coarser → more per-node compute) is close to definitional for any distributed-execution system and does not, by itself, demonstrate that *joint* optimization beats *sequential* optimization; a sequential-but-iterated baseline is never run for comparison. The evaluation plan (Objective 4) names the co-simulation stack but not the baselines the joint method will be benchmarked against, even though the Literature Review itself cites directly comparable systems (Neurosurgeon, CoEdge, DADS, Zhao/Dai et al.'s joint formulation) that would make natural baselines.

**Strengths**:
- **S1**: Explicit acknowledgment of combinatorial hardness rather than glossing over it (Methodology, "Computational Complexity" paragraph).
- **S2**: The three-phase decomposition (partitioning/assignment → communication cost → online re-optimization) mirrors how the coupling is actually introduced into the objective, so the phases are not artificially separated from the problem structure.
- **S3**: Telemetry state design for online adaptation (link quality, packet loss, residual energy, CPU load, graph execution status) is concrete and appropriately scoped.

**Weaknesses**:
- **W1**: No stated complexity class or hardness citation for the bounded-$K$ problem. **Problem**: "the joint problem is combinatorial, with complexity growing exponentially" is asserted, not derived or cited. **Why it matters**: Objective 1's "structured analysis of this interdependence and the role of $K$" cannot be scoped without knowing whether the target is an exact algorithm for small $K$, an approximation with provable ratio, or a heuristic with only empirical validation. **Suggestion**: state the target complexity result (e.g., "we conjecture/aim to show NP-hardness via reduction from X, then pursue a $(1+\epsilon)$-approximation for fixed $K$") even provisionally. **Severity**: Major.
- **W2**: No named baseline for the "joint > sequential" claim. **Problem**: Objective 4 evaluates the full architecture but does not mention comparing against a sequential partition-then-schedule baseline, despite this being the central claim of Contribution 1. **Why it matters**: without this comparison, the thesis's headline claim (joint beats decoupled) is asserted by literature citation, not demonstrated by the proposal's own evaluation. **Suggestion**: add a named baseline condition (e.g., "greedy partition followed by shortest-path assignment") to the Phase 4 evaluation plan. **Severity**: Critical for the thesis's central claim, though acceptable to defer the *design* of this baseline to Year 1 — flagged here so it is not forgotten by Phase 4.
- **W3**: SWaP constraints are named but never quantified. **Problem**: "compute, memory, energy" constraints appear in the feasible-set definition but no reference UAV class (payload, battery capacity, onboard compute e.g. Jetson-class vs. Raspberry-Pi-class) is given anywhere. **Why it matters**: the co-simulation in Objective 4 needs concrete numbers to be reproducible and for the "SWaP-constrained" framing to be checkable. **Suggestion**: name at least one reference platform in Objective 1 or the Methodology. **Severity**: Minor at proposal stage, Major once Phase 2 begins.

---

## R2: Domain Review (FANET / UAV Networking)

**Recommendation**: Minor Revision
**Confidence**: 4/5

**Summary**: Literature coverage is strong for a proposal — 42 references, 81% from the last five years, spanning the three relevant strands (collaborative inference/split computing, FANET routing, swarm resilience) with a synthesis table that is genuinely useful rather than decorative. The FANET-specific claims (mobility, intermittent links, bandwidth variability driving delay/energy — Literature Review §4) are consistent with the cited routing literature (Lansky et al., Hosseinzadeh et al., Rahmani et al.). Domain positioning is accurate: it correctly identifies that FANET research and split-inference research "proceed largely in parallel" (Gap 2) rather than overstating the gap. Two domain-level concerns: several supporting citations use truncated author lists ("and others"), which slightly undercuts the ability of a domain reader to verify who actually did the work being leaned on; and four references in the bibliography (`eshratifar2019jointdnn`, `lin2024dnnpartition`, `seid2021multiagent`, `zhang2024cnn`) are never cited in the running text, which for a domain reviewer raises the question of whether relevant related work (JointDNN, multi-UAV DRL offloading) was deliberately left out of the Literature Review's narrative or just left unlinked.

**Strengths**:
- **S1**: Accurate, non-overstated gap framing — Gap 2 in particular correctly describes parallel-but-disconnected literatures rather than claiming FANET research "ignores" inference entirely.
- **S2**: Good source currency (81% within 5 years); appropriately retains one older foundational reference (Neely 2010, Lyapunov optimization) as a theory anchor rather than for empirical currency.
- **S3**: The FANET communication-cost framing (tensor size × link quality → delay/energy, Methodology Phase 2) correctly treats communication cost as *endogenous* to the partitioning decision rather than as an external parameter, which is the actual technical crux of Gap 1.

**Weaknesses**:
- **W1**: Truncated author lists in 9 bibliography entries (e.g. `khan2022uavedge`, `chen2023edgeuav`, `wang2024ress` use "and others"). **Why it matters**: makes independent verification of these sources harder for a reader and reads as less rigorous sourcing. **Suggestion**: complete the author lists. **Severity**: Minor.
- **W2**: Four uncited bibliography entries, including `eshratifar2019jointdnn` (JointDNN) and `seid2021multiagent` (multi-UAV DRL offloading), both of which look domain-relevant to Objective 1/RQ1. **Why it matters**: if these were read and excluded deliberately, the Literature Review should say why (e.g., "JointDNN targets mobile-cloud, not swarm-internal, partitioning"); if they were simply left over from an earlier draft, they should be cited or removed. **Suggestion**: either weave them into Literature Review §3 or delete from the .bib. **Severity**: Minor.
- **W3**: No discussion of FANET-specific MAC/physical-layer assumptions (e.g., 802.11-family vs. LTE/5G-for-UAV, interference model). **Why it matters**: the communication-cost model in Objective 2 will need to commit to a link/PHY model eventually, and the proposal gives no hint of which. **Suggestion**: at least name the intended link-layer assumption. **Severity**: Minor.

---

## R3: Cross-Disciplinary / Perspective Review

**Recommendation**: Minor Revision
**Confidence**: 3/5 (perspective/impact framing is partially outside strict optimization-theory expertise)

**Summary**: The practical motivation (disaster response, search-and-rescue, environmental monitoring — Background and Motivation) is well chosen and gives the work a clear application pull beyond pure algorithm design. The three-layer architecture (computation / network / control) is a transferable framing that could generalize past UAVs to other mobile-edge-swarm settings (e.g., ground robot fleets, maritime drones), though the proposal does not explicitly claim or explore this transferability. One notable omission for a proposal centered on UAV swarms in "disaster response" and "contested environments" (Abstract) is any explicit ethics/dual-use statement — UAV swarm coordination research has known dual-use sensitivity, and Methodology's "Risk Considerations" paragraph mentions ethics in one clause ("intended for civilian and research-oriented use cases") without elaboration.

**Strengths**:
- **S1**: Strong, concrete application framing (disaster response, SAR, infrastructure inspection) that motivates the SWaP constraint non-abstractly.
- **S2**: The three-layer (computation/network/control) architecture is a reusable conceptual contribution independent of the UAV-specific results.
- **S3**: Explicit acknowledgment of the sim-to-real gap as a limitation (Methodology, Risk Considerations) rather than presenting simulation results as a stand-in for field validation.

**Weaknesses**:
- **W1**: Dual-use/ethics framing is a single clause, not a treatment. **Problem**: "contested environments" appears in the Abstract, and the application domain (autonomous UAV swarm coordination) is one where thesis committees and funders increasingly expect an explicit ethics/dual-use paragraph. **Why it matters**: for a topic this close to military/surveillance-adjacent applications, a one-clause disclaimer may not satisfy an ethics review or a skeptical committee member. **Suggestion**: expand to a short paragraph naming the civilian-use boundary and what safeguards (if any) the research design assumes. **Severity**: Minor-to-Major depending on the institution's requirements.
- **W2**: No discussion of generalization beyond UAVs. **Problem**: the three-layer architecture is UAV-specific in every objective and evaluation, even though its structure (compute/network/control separation) plausibly generalizes. **Why it matters**: broadening the significance claim, even briefly, would strengthen Expected Outcomes without added scope. **Suggestion**: one sentence in Expected Outcomes noting the architecture's applicability beyond aerial swarms. **Severity**: Minor.

---

## Devil's Advocate Report

**Strongest Counter-Argument** (≈250 words):
The proposal's novelty claim rests on a *conjunction* argument: no single prior work scores ✓ on all four of {joint optimization, coupling, online adaptation, UAV/FANET}. This is a valid and checkable claim (the comparison table lets a reader verify it), but it is a *combination* novelty, not a *mechanism* novelty — every individual ingredient (bounded-partition joint optimization: Hu et al. 2019 DADS scores ✓ on joint optimization already; online adaptation under failures: Pan et al. 2025, Kim et al. 2025 score ✓ already; communication-aware coupling: Shao & Zhang 2022, Li et al. 2023 score ✓ already) already exists somewhere in the cited literature. The thesis is therefore a bet that *assembling* these three known techniques into one coupled objective, specifically for FANET-connected UAV swarms, constitutes a sufficient PhD-level contribution. That bet may well pay off, but the proposal does not yet argue *why* the assembly is technically hard rather than merely effortful — i.e., what new difficulty emerges specifically from combining bounded-$K$ partitioning with FANET-specific communication volatility and online re-optimization, that does not appear when each is studied alone. Without that argument, a skeptical reader can ask: "what breaks if I just bolt DADS's partitioning onto Pan et al.'s self-healing controller?" The proposal would be considerably stronger if it identified one concrete technical obstruction that only appears at the intersection (e.g., "re-optimizing the assignment after a node failure requires re-deriving tensor sizes for a *different* partition boundary, which existing self-healing controllers do not model because they assume fixed task placement, not placement coupled to a partition choice").

**Issue List**:

| # | Issue | Category | Location | Severity |
|---|---|---|---|---|
| 1 | Novelty is argued by conjunction-of-gaps rather than by a named technical obstruction unique to the intersection | Foundation strength | Literature Review §7, Research Objectives | Major |
| 2 | Preliminary Pareto trade-off (Fig. 1) is close to a structural tautology of any partition-vs-communication system; it is not clearly distinguished from "evidence that joint optimization is necessary" | Evidence strength | Methodology, "Preliminary Analysis" | Major |
| 3 | No stated hardness/complexity result for the bounded-$K$ problem, despite Objective 1 promising "structured analysis... including identification of tractable substructures" | Specification gap | Methodology, "Computational Complexity"; Research Objectives, Objective 1 | Major |
| 4 | Online-adaptation method family left open ("control-theoretic and learning-based methods... under a unified structural framework") with no stated preference or hypothesis | Specification gap | Methodology, Phase 3 | Minor |
| 5 | No baseline comparison named for the central "joint beats sequential" claim | Evidence strength | Research Methodology / Expected Outcomes | Major (see R1-W2) |
| 6 | Ethics/dual-use treatment is one clause for a swarm-coordination topic explicitly framed around "contested environments" | Framing completeness | Abstract; Methodology Risk Considerations | Minor-to-Major (institution-dependent) |

**Ignored Alternative Explanations/Paths**: The proposal does not discuss why a *learned* end-to-end policy (e.g., a single graph neural network that jointly predicts partition + assignment + adapts online, trained via RL) would not subsume all three phases without an explicit combinatorial formulation — this is a live alternative research direction in the cited literature (Park et al. 2025 MARL) and deserves at least a sentence of why the analytical/combinatorial route was chosen over an end-to-end learned one.

**Missing Stakeholder Perspectives**: Disaster-response end users (first responders) and swarm operators are named as motivation but not consulted or referenced as a source of requirements (e.g., real acceptable-latency thresholds, real failure-rate statistics for field UAVs) — the SWaP and latency constraints appear to come entirely from the technical literature, not from an operational-requirements source.

**Observations (Non-Defects)**: The three-paper, three-year structure mapped cleanly onto RQ1a/RQ1b/RQ2 is a genuinely well-organized plan, independent of the specification concerns above.

---

## Editorial Decision

### Dimension Scores (aggregated across R1–R3, EIC narrative-weighted)

| Dimension | Score (0–100) | Descriptor |
|---|---|---|
| Originality (20%) | 72 | Adequate–Strong (integrative novelty; conjunction-of-gaps argument, per Devil's Advocate) |
| Methodological Rigor (25%) | 64 | Adequate (sound direction, under-specified $K$/complexity/baseline) |
| Evidence Sufficiency (25%) | 69 | Adequate (strong lit base; preliminary result evidentially weak) |
| Argument Coherence (15%) | 83 | Strong (RQ→Gap→Contribution→Objective traceability is a real strength) |
| Writing Quality (15%) | 80 | Strong (clear, professional; minor repetitive phrasing) |
| *Literature Integration (R2, optional)* | 78 | Strong coverage; minor completeness gaps (uncited refs, truncated author lists) |
| *Significance & Impact (R3, optional)* | 74 | Clear applied motivation; broader-transfer and ethics framing underdeveloped |
| **Weighted Average** | **72.1** | **→ Minor Revision** |

*(Weighting: Originality 0.20 + Methodology 0.25 + Evidence 0.25 + Coherence 0.15 + Writing 0.15, per `quality_rubrics.md`.)*

### Panel Recommendations
EIC: Minor Revision · R1: Major Revision · R2: Minor Revision · R3: Minor Revision · Devil's Advocate: no CRITICAL finding (highest-severity findings are Major; see Issue List).

### Decision: **Minor Revision** (read, for a proposal, as: *proceed — but resolve the items below before treating this as the locked scope for Year 1*)

No Devil's Advocate finding meets the CRITICAL bar (Foundation Collapse / Logic Chain Break / Data-Conclusion Mismatch / Stronger Counter-Narrative with equal-or-better fit) — the strongest challenge (conjunction-novelty) is a *strength-of-contribution* concern, not a demonstrable falsity, so it is scored Major. R1's Major Revision recommendation is driven by specification gaps that are normal for a proposal but should not survive into the Objective 1 deliverable.

### Consensus Issues (raised by 2+ reviewers)
1. **$K$ and complexity class left unspecified** (EIC-W1, R1-W1, DA-3).
2. **No named baseline for the joint-vs-sequential claim** (R1-W2, DA-5).
3. **Ethics/dual-use treatment underdeveloped for the stated application domain** (R3-W1, DA-6).

### Disagreements
R1 rates methodology Major Revision (specification-focused, technical lens) while EIC/R2/R3 rate Minor Revision (structure-and-positioning lens); this is not a true conflict — R1's concerns are about depth-of-specification appropriate to flag now so they are resolved in Objective 1, not evidence that the overall proposal direction is unsound.

---

## Revision Roadmap (prioritized; directly usable as input to `academic-paper` revision mode)

| Priority | Item | Source | Action |
|---|---|---|---|
| 1 | State a concrete rule or provisional range for $K$, and name the target complexity result (hardness citation or conjecture) | EIC-W1, R1-W1, DA-3 | Add 2–3 sentences to Methodology / Objective 1 |
| 2 | Name at least one baseline (e.g., sequential partition-then-assign) for the Phase 4 evaluation | R1-W2, DA-5 | Add to Objective 4 / Expected Outcomes |
| 3 | Articulate the specific technical obstruction that only appears at the coupling+FANET+online-adaptation intersection (not just "no one has combined these") | DA-1 | Add 1 paragraph to Literature Review §7 or Research Objectives intro |
| 4 | Expand the ethics/dual-use clause into a short paragraph | R3-W1, DA-6 | Methodology, Risk Considerations |
| 5 | Reconcile publication timeline with realistic review cycles, or explicitly name target venue tiers with faster turnaround | EIC-W2 | Research Plan and Timeline |
| 6 | Convert the Risk Considerations bullets into trigger→fallback pairs per objective | EIC-W3 | Methodology |
| 7 | Resolve the 4 uncited bibliography entries (cite or remove) and complete "and others" author lists | R2-W1, R2-W2 | references.bib — can be done via `/ars-citation-check` auto-corrections already identified |
| 8 | Name a reference UAV platform for SWaP constraints | R1-W3 | Objective 1 / Methodology |
| 9 (optional) | Add one sentence on architecture transferability beyond UAV swarms | R3-W2 | Expected Outcomes |

**Acknowledged Limitation** (per IRON RULE — max 2 revision loops, unresolved items may be logged rather than fully resolved pre-defense): items 5, 6, and 9 are stylistic/planning refinements and can reasonably be deferred to the full thesis proposal defense rather than blocking immediate next steps.
