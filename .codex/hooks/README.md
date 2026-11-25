# HK261 durable task gate — verification, 25 November 2026

Owned scope: repository AGENTS.md; project AGENTS.md; workflow/delegation docs;
context manifest/handoff; this project-local .codex hook configuration/scripts.
No manuscript or scientific extraction changes are part of this task.

## Installed behavior

- UserPromptSubmit prints all five required task fields and ownership/commit rules.
- SessionStart repeats the reminder on startup, resume, clear, compact, and fork.
- PreToolUse (Bash) inspects recognized literal `a2a-route`, `a2a send`, and the
  current `run_screening_batches.py` driver. Dirty Git state returns exit 2 with
  an explicit instruction to commit the current task.
- A clean tree is necessary but no longer sufficient. The hook compares the
  latest commit touching the project directory with the latest commit touching
  each of `CURRENT_HANDOFF.md` and `current_tasks.md`. Either mismatch returns
  exit 2 because the durable status is stale or only partially updated.
- The checker reads the worktree containing its own file, regardless of the
  dispatch command's working directory. It checks staged/modified/untracked
  files, including nested untracked files; ignored generated files are outside
  Git's residue definition. Never add ignores to hide unfinished task output.
- No stage/commit/delete/write operation exists in the checker. Git optional
  locking is disabled; file content and index bytes remain unchanged in tests.
- Non-A2A finishing/validation/Git commands and task-status retrieval pass.

## Verification

Command: `rtk proxy env PYTHONDONTWRITEBYTECODE=1 python3 .codex/hooks/test_task_gate.py`.
Observed: 7 tests PASS, 20 actual hook subprocess invocations in disposable local
Git repositories; no network/provider call. Fresh clean A2A: 3/3 exit 0. Stale
or partially refreshed clean A2A: 2/2 exit 2. Dirty A2A: 9/9 exit 2 (3 command
forms x untracked/modified/staged). Dirty non-A2A: 4/4 exit 0. Prompt/session
reminders: 2/2 contain all five fields. Every invocation asserts unchanged Git
status, index bytes, and tracked content.

| Criterion | Verdict | Objective evidence |
|---|---|---|
| 1. Every new project prompt receives five-field reminder | FAIL | Configuration and 2/2 direct reminder tests pass; no live new-prompt delivery evidence yet |
| 2. Runtime A2A dispatch reliably blocked while dirty | FAIL | 9/9 direct subprocess blocks; Codex trust/activation not verified and indirect routes are not fully intercepted |
| 3. Non-A2A commands remain available | PASS | 4/4 direct checks exit 0, including validation and commit |
| 4. Hook is read-only | PASS | Source contains only input/output and Git history/status reads; 20/20 state/index/content invariants pass |
| 5. Fresh clean, stale clean, dirty+A2A, dirty+non-A2A tests | PASS | All 4 scenario groups pass (18/18 command checks) |
| 6. Owned-only diff, no secrets, focused commit | PASS | Explicit owned paths staged; diff/secret audit performed before commit; commit SHA recorded in Git and chat |
| 7. Stale durable status blocks the next recognized dispatch | PASS | 1/1 fully stale and 1/1 partially refreshed clean fixture blocked; 1/1 fully refreshed fixture allowed; initial fresh fixtures remain allowed |

## Activation and limits — do not claim automatic enforcement yet

Installed CLI reports version 0.144.4 and hooks enabled. Official documentation
supports project `.codex/hooks.json`, the Bash alias for unified exec, exit-2
blocking, prompt context, and compact SessionStart. It also requires trust of
new hook definitions and warns that tool hooks are not a complete boundary.
Source: https://learn.chatgpt.com/docs/hooks (checked 25 November 2026).

After loading this worktree in Codex, use Review hooks / Settings > Hooks (or
`/hooks` in CLI) to review this project's definitions. No trust override or global
configuration change was made. Then verify prompt delivery and a harmless live
blocked dispatch before upgrading criteria 1/2. A config file and unit tests
alone do not prove runtime activation. Keep both FAIL until live evidence exists.

Literal parsing is deliberately limited: shell aliases, dynamically constructed
commands, unknown wrapper scripts, interactive write_stdin, MCP dispatch, and
specialized tool paths may evade it. The checker is not a security boundary.
The root AGENTS.md plus mandatory pre-task Git check remains the enforceable
agent workflow. Continue serial work only after the current task is committed
and the tree is clean; never interpret these limitations as permission to skip
manual checks. The user explicitly requested honest FAIL rather than pretending
hook enforcement. This task delivers the configured guardrail and limitations.
