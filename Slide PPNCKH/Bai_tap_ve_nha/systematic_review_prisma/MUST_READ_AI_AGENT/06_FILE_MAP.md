# Canonical File Map

All paths are relative to `systematic_review_prisma/` unless absolute.

## Read first for current truth

| Purpose | Canonical path |
|---|---|
| Single current-state source | `current_state.json` |
| Validate/render current state | `../../../../.codex/hooks/project_state.py validate\|show` |
| Context/token budget evidence | `CONTEXT_BUDGET.md` |
| Official assignment | `../../HK261 - Bài tập lớn-Tiểu luận.pdf` from the project directory; equivalently `../../../HK261 - Bài tập lớn-Tiểu luận.pdf` from this folder |
| Current project overview | `../README.md` |
| Fixed protocol | `../protocol.md` |
| Scope amendment | `../protocol_amendment_001.md` |
| 2021+ amendment | `../protocol_amendment_002.md` |
| Stage/status plan | `../project_plan.md` |
| Current completion audit | `../completion_audit_2026-11-25.md` |
| Submission blockers | `../submission_readiness_2026-11-25.md` |
| A2A policy | `../corpus_expansion/a2a_routing_policy_2026-11-25.md` |
| Current research queue | `current_state.json` field `next_task`; `../corpus_expansion/current_tasks.md` is a compatibility pointer |
| Automation/code decision history | `../automation/decision_log.jsonl` |
| Reusable code catalog | `../automation/artifact_catalog.json` |
| Automation registry instructions | `../automation/README.md` |

## Active research artifacts

| Purpose | Canonical path |
|---|---|
| Platform queries | `../final_query_translations.md` |
| Formal-search status | `../formal_search_log_v0.2.csv` |
| Record screening | `../screening_log.csv` |
| Study/report linkage | `../study_report_map.csv` |
| Current 27-report dataset | `../interim_27report/` |
| Expansion plan | `../corpus_expansion_30_35_plan_2026-11-25.md` |
| Full-text priority queue | `../corpus_expansion/doi_fulltext_priority_queue.md` |
| PRISMA checklist | `../prisma_2020_checklist_working.md` |

## Active manuscript

| Purpose | Canonical path |
|---|---|
| LaTeX source | `../manuscript/sn_computer_science/main.tex` |
| Bibliography | `../manuscript/sn_computer_science/references.bib` |
| Compiled review PDF | `../manuscript/sn_computer_science/main.pdf` |
| Approved venue/build profile | `../manuscript/sn_computer_science/build_profile.json` |
| Template notes | `../manuscript/sn_computer_science/README.md` |
| Release artifacts | `../output/` |
| Submission evidence | `../submission_evidence/` |

## Historical or non-canonical by default

- `history/CURRENT_HANDOFF.pre-state-v1.2026-11-26.md` and
  `../corpus_expansion/history/current_tasks.pre-state-v1.2026-11-26.md` preserve
  the verbose pre-migration state; do not load them as current truth.
- `../manuscript/ieee_access/` — absent from canonical `main`; retained under
  `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/root_project_live_before_promotion/manuscript/ieee_access/`.
- `../output/docx/` — absent from canonical `main`; retained under
  `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/root_project_live_before_promotion/output/docx/`.
- older `interim_*` directories except `interim_27report/`
- superseded venue decisions and earlier release manifests
- raw provider JSON, failed/quota-only tasks, unaccepted ledgers, and candidate
  output without a Codex PASS gate
- LaTeX auxiliary files (`.aux`, `.log`, `.fls`, `.blg`) as scientific evidence

Historical artifacts remain for audit. Do not delete, promote, or use them as
current truth without a documented decision.

## Path discipline

- Keep all coursework artifacts inside this project directory.
- Preserve immutable raw exports under `sources/raw/`.
- Put normalized derivatives under `sources/normalized/` and record provenance.
- Do not overwrite an accepted dated release; create a new dated release and
  manifest.
- Update this map and `current_state.json` whenever a canonical path changes.
