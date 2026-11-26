# HK261 hooks and validation

These hooks are project guardrails, not a security boundary. They use the
repository selected by Codex and do not change tracked project content.
Automatic live activation remains **UNVERIFIED** until the Codex UI records a
real prompt delivery and a harmless blocked dispatch.

## Hook map

| Event | Script | Behavior |
|---|---|---|
| UserPromptSubmit | `task_gate.py` | Prints one compact AGENTS/pre-task reminder |
| UserPromptSubmit | `skill_router.py` | Suggests owner, code-first mode and at most three skills |
| SessionStart | `task_gate.py` | Prints the same compact reminder |
| PreToolUse/Bash | `task_gate.py` | Checks recognized A2A dispatch without changing files |

The gate recognizes literal `a2a-route`, `a2a send` and
`run_screening_batches.py` commands. Before allowing them it requires:

1. no residue in HK261, `.codex/` or root `AGENTS.md`;
2. the latest project commit to include
   `MUST_READ_AI_AGENT/current_state.json`;
3. valid canonical state and matching latest event;
4. one matching active code-first decision and valid artifact registry.

`CURRENT_HANDOFF.md` and `corpus_expansion/current_tasks.md` are static
compatibility pointers. They are no longer task-state inputs.

## Canonical state commands

```bash
python3 .codex/hooks/project_state.py validate
python3 .codex/hooks/project_state.py show
python3 .codex/hooks/automation_registry.py validate
python3 .codex/hooks/automation_registry.py search "<task keywords>"
```

`project_state.py` rejects duplicate JSON keys, invalid/future/unknown-zone
timestamps, inconsistent task times, malformed evidence counts and an event that
does not match the current task and `updated_at`.

## Skill catalog cache

`skill_router.py` caches discovered skill names and paths for 600 seconds at
`~/.cache/codex/skill_router/catalog-v1.json`. A valid cache avoids recursive
`SKILL.md` discovery on every prompt. Missing files, changed roots, expiry,
invalid JSON or schema mismatch trigger a safe rescan. Cache write failure never
blocks the prompt. Override the location with `CODEX_SKILL_CACHE`; tests use
temporary paths.

The router remains advisory. An explicitly named installed skill wins; it
suppresses equivalent pipelines, caps the route at one primary plus two support
skills and prints each selected `SKILL.md` path for the agent to read.

## Test tiers

Use the smallest tier affected by the change; do not repeatedly run an unchanged
green command merely for reassurance.

Quick unit tier for state/router/registry changes:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 .codex/hooks/test_project_state.py -q
PYTHONDONTWRITEBYTECODE=1 python3 .codex/hooks/test_skill_router.py -q
PYTHONDONTWRITEBYTECODE=1 python3 .codex/hooks/test_automation_registry.py -q
```

Full hook tier before merge, after gate/config changes, or before claiming the
hook package valid:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s .codex/hooks -p 'test_*.py' -q
```

Current expected total: 78 tests = 4 context + 7 state + 33 router + 16 registry
+ 18 gate.
The gate suite uses disposable Git repositories and is intentionally slower than
the pure unit tier.

Measured budgets and the reproducible before/after method are recorded in
`MUST_READ_AI_AGENT/CONTEXT_BUDGET.md`. The compact task reminder is 69
characters (about 17 heuristic tokens); the warm router uses its catalog cache.

## Activation evidence and limits

Direct subprocess tests prove implementation behavior, not Codex UI activation.
Before upgrading activation to PASS, review/trust `.codex/hooks.json` in Codex,
observe the compact reminder on a real prompt, and perform a harmless live
blocked-dispatch check.

Aliases, dynamically constructed commands, unknown wrappers, interactive stdin,
MCP dispatch and specialized tool paths can evade literal detection. Finishing
commands remain available so invalid state can be repaired. The root
`AGENTS.md` contract remains mandatory even when a hook is skipped.
