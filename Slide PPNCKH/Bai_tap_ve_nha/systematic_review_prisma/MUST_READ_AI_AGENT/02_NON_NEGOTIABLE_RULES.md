# Non-Negotiable Rules

## Scientific integrity

- Fabricated citations, DOI values, data, counts, findings, experiments, search
  runs, manuscript IDs, receipts, and author approvals: **zero tolerance**.
- A transport status of `completed` is not evidence acceptance.
- Never present projected/expected results as observed results.
- Never report final PRISMA counts until record, report, and study arithmetic is
  reconciled with zero unexplained difference.
- Never generalize from a simulator, analytical model, component prototype, or
  single-drone check to a physical UAV swarm without an explicit limitation.
- Never convert missing evidence into a negative finding. Use `not reported`,
  `uncertain`, `DOI_NOT_FOUND`, or an explicit unresolved item.

## Sources and citations

- Every citation must identify a real source and be checked against the original
  report plus DOI/publisher-deposited metadata.
- Detailed study evidence must come from readable full text. Abstract-only
  observations must be labelled abstract-only and cannot support detailed
  quantitative synthesis or quality appraisal.
- Every quantitative claim needs a report locator, conditions, units, and the
  applicable population/system boundary.
- Duplicate DOI/title records after normalization must equal zero.
- Raw A2A output, discovery lists, candidate ledgers, and unreviewed extraction
  are quarantined until Codex's criterion gate accepts them.

## Manuscript and format

- Edit `../manuscript/sn_computer_science/main.tex` and
  `../manuscript/sn_computer_science/references.bib` as the active manuscript.
- Compile PDF from LaTeX. Do not use a Word file as the source of truth.
- `manuscript/ieee_access/`, root-level older tables, and earlier interim release
  directories are historical unless a current canonical document explicitly
  promotes them.
- Do not leave placeholders, fake author metadata, guessed affiliations,
  unverified funding text, or provisional declarations in a submission package.

## Authorship and submission

- Do not guess author order, contribution, consent, email, ORCID, affiliation,
  funding, conflicts, AI disclosure, examination date, or deadline.
- HCMUT/VNU-HCM affiliation and verified `@hcmut.edu.vn` correspondence must be
  consistent across manuscript and portal.
- Never submit, send email, forward evidence, or communicate externally without
  the user's explicit instruction for that external action and all required
  metadata/approval gates.
- Never submit the same manuscript to multiple venues simultaneously.

## Agent ownership

- Codex: all prose, LaTeX and project edits, review decisions, user-facing text,
  author/submission documents, and Git mutations.
- Gemini or Codex fallback: research, discovery, factual verification,
  extraction, comparison, classification, and structured synthesis only.
- Claude and Grok: read-only unless the user explicitly transfers authority.
- No research agent may accept its own findings or silently repair missing
  evidence.

## Security and Git

- Never include credentials, private messages, tokens, personal secrets, or
  unrelated private project material in an A2A brief or committed artifact.
- Preserve every pre-existing user change. Never use destructive cleanup or
  broad staging.
- Use a dedicated branch/worktree for each agent mutation; stage explicit paths,
  verify, merge fast-forward, delete the branch/worktree, and leave zero new
  uncommitted agent changes.
- The parent repository may already contain unrelated dirty/untracked user work.
  Capture the baseline and ensure the agent adds no new residue; do not claim the
  whole repository was clean when it was not.
- Do not initialize a nested repository or bulk-add the currently untracked
  research tree without explicit user approval.

## Automation-first / code mode

- Before acting on every task, record one of `REUSE_EXISTING`, `WRITE_SCRIPT`,
  or `MANUAL` with a one-sentence reason.
- Prefer, in order: a verified existing script/tool/API/CLI; a small tested and
  reusable script for deterministic or repeated work; manual execution only
  when automation is unsafe, unavailable, judgment-heavy, or more expensive
  than the one-off work.
- Even for a manual task, automate safe deterministic substeps when this reduces
  repetition and error risk.
- Do not overengineer. New automation must have explicit inputs/outputs,
  structured failure behavior, no embedded secrets, focused tests, practical
  idempotency, and a committed reusable home in the project.
- Code does not replace scientific judgment, source verification, authorship
  approval, or any user-only external action.
- Preserve every final code-first decision in `../automation/decision_log.jsonl`
  and every reusable code path in `../automation/artifact_catalog.json`. Search
  the registry before writing code; append superseding decisions instead of
  editing accepted history; validate the registry before commit.
