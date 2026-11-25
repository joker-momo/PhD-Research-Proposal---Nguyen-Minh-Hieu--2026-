@/Users/joker/.codex/RTK.md

# HK261 worktree entry point

For HK261/PRISMA work, first read
`Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md`
and every required file in its manifest. This applies after restart, compaction,
and model changes. Do not mix coursework with the dissertation roadmap.

Before EACH new task, publish exactly these five fields:
TASK: one concrete task
OWNER: CODEX_WRITING or GEMINI_RESEARCH
OWNED_PATHS: explicit paths
BINARY_ACCEPTANCE: countable or binary checks
PRE_TASK_GIT_STATUS: branch, staged/modified/untracked counts, preceding commit

Run Git status immediately before starting. Any staged, modified, or untracked
residue BLOCKS the next task and any A2A dispatch. Finish, validate, inspect the
diff, stage explicit owned paths, and commit the current task first. Never erase,
stash, or hide residue to pass this gate. Record its SHA and verify a clean tree.
Preparing a new brief is a Codex writing task: commit it before dispatch.

Codex owns all writing/editing, project files, acceptance reviews, Git, and final
text. Gemini via the approved A2A router owns research, discovery, extraction,
factual verification, classification, and structured evidence synthesis. A
research worker must not edit project files or write final prose. Each A2A brief
must have TASK, REQUIRED WORK, REQUIRED OUTPUT, ACCEPTANCE CRITERIA, BOUNDARIES.
Accept evidence only after a criterion-by-criterion PASS/FAIL review has all
mandatory criteria PASS. A correction is the same research task, with its brief
committed before retry. Never equate transport completion with acceptance.

Project hook configuration and verification limits: `.codex/hooks/README.md`.
Hooks are an additional guardrail; manually enforce these rules even if hooks
are untrusted, skipped, unavailable, or the tool path bypasses interception.

## Advisory skill router

On each user prompt, `.codex/hooks/skill_router.py` may suggest at most one
primary skill and two non-overlapping supporting skills. An explicitly named,
installed skill has first priority. If it reports `SKILLS: none`, continue with
the stated reason. The router is advisory and must never block uncertain input.

Before acting, read every selected `SKILL.md` completely at the printed
`READ_FULL_SKILL_MD` path. Do not treat the router output as proof that this was
done. `academic-pipeline` orchestrates academic work and must not be co-loaded
with an equivalent research pipeline. Research/discovery/verification remains
Gemini-owned through the approved A2A route; writing/editing remains Codex-owned.
For lawful paper retrieval, use `paper-lookup`, then
`lawful-paper-pdf-retriever`, then `nature-downloader`. Never automatically
select a retriever whose default flow includes unauthorized sources.
