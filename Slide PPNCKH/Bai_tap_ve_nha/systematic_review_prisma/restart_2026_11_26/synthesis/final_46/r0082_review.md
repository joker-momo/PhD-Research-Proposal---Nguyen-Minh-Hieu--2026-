# R0082 source, results and related-report review

## Retained version

The author confirmed R0082 for inclusion as the IEEE WCNC proceedings paper, DOI `10.1109/WCNC55385.2023.10118908`. [Crossref deposited metadata](https://api.crossref.org/works/10.1109/WCNC55385.2023.10118908) corroborates the title, authors, year and venue. The [arXiv v1 identifier](https://arxiv.org/abs/2305.15858v1) is on physical page 1 of the retained six-page original. Its registration records the WCNC DOI. The PDF under `restart_2026_11_26/fulltext_retrieval/pdf/R0082.pdf` is arXiv v1. Its SHA-256, version, field anchors and appraisal judgments are in [r0082_evidence.json](r0082_evidence.json). IEEE publisher-page equivalence beyond the author's confirmation remains unverified.

## Coding and numerical coverage

| Decision | Original locator |
| --- | --- |
| Intra-swarm peer transport | arXiv v1 physical p. 2, §II/Fig. 1, and p. 4, §III.C. Inference stays within the swarm. The optimization uses coordinator notation, so the coding describes the inference data path. |
| CNN layer assignment using mathematical optimization | Physical pp. 3–5, §III, Eqs. 6–14. Power, position and layer assignment are separate subproblems. The assignment constraint distributes each layer to one available UAV. |
| Software simulation, no tested failure response | Physical pp. 5–6, §IV. Raspberry Pi B+ capabilities parameterize simulated devices. LoS and transmission-rate bounds are described at pp. 3–4. Capacity-based delegation is described at pp. 2 and 4; no injected failure, outage or recovery metric is stated. |
| Plot-only, zero retained exact outcomes | Physical pp. 5–6, §IV, Figs. 2–5. The plots present latency and minimum radio transmit power by simulated operating conditions. These values were not estimated from the curves. The configuration values in §IV are setup inputs. |
| 10 appraisal readings | Original locations, observed text and qualifications stated per domain in [accepted evidence](r0082_evidence.json) and [rationale matrix](appraisal_rationale.csv). D01 is affirmative, D09 is not reported, and the other eight judgments are partial. |

PDFKit supplied selectable text and original-page renderings. Six accepted field anchors and ten appraisal anchors matched after normalizing extraction whitespace and soft line breaks. The rendered original results pages were checked for figure captions, axes, units and value labels. Figures 2–3 and Figure 5 use different latency units. No figure-derived values enter calculations.

## R0082 compared with R0019

The [LLHR arXiv record](https://arxiv.org/abs/2305.15858v1) flags text overlap with [arXiv:2212.11201](https://arxiv.org/abs/2212.11201), which links to R0019 (DOI `10.1109/JIOT.2022.3231341`). The SHA-256 of each original is retained in [r0082_evidence.json](r0082_evidence.json). The R0019 locations below refer to the original local IEEE PDF.

| Comparison | R0082 arXiv v1 | R0019 IEEE |
| --- | --- | --- |
| Shared experimental design features | Physical pp. 5–6, §IV: surveillance requests, LeNet, AlexNet, Raspberry Pi family simulation profiles, static-path and random-movement baselines. | Physical pp. 11 and 14, simulation parameters and Fig. 16: same named surveillance CNN families and profiles; static greedy and random selection comparators. |
| Distinct reported design and evaluations | Physical pp. 3–5, §III: separate mathematical subproblems for radio power, placement and layer assignment. Physical pp. 5–6, §IV: a 480 m × 480 m grid, bandwidth and power sweeps, and an LLHR latency-versus-load comparison in Fig. 5. | Physical pp. 9–11: PPO training and a 100 m × 100 m grid, VGG16 in addition to LeNet/AlexNet, constraint-respecting accuracy and service QoS. Physical p. 14, Figs. 16–17: RL, suboptimal and OULD comparators in addition to heuristic/random traces, and PPO versus actor–critic. Fig. 16 (printed p. 8198) and R0082 Fig. 5 differ in included methods and plotted scales. |
| Disposition | The distinguishable methods and evaluation configurations support retaining two technical evaluations. The relationship does not establish independent replications, and the source files do not document whether any simulation runs or underlying inputs were reused. No R0082 numeric effect was combined with R0019. | |

The [primary provider review](r0082_primary_review.md) records rejected unverified details. The release uses the original-page evidence and the accepted fields above.
