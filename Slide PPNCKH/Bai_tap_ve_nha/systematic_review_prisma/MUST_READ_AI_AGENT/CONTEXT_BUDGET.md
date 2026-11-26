# Context and Hook Budget

Measured on 26 November 2026 in the isolated optimization worktree. Token
figures use the conservative reproducible heuristic `UTF-8 bytes / 4`; actual
model tokenization varies.

## Default onboarding

| Snapshot | Files counted | Bytes | Approx. tokens |
|---|---|---:|---:|
| Before | `AGENTS.md` plus the former 10-file mandatory read set | 52,423 | 13,106 |
| After | `AGENTS.md`, entry point, manifest, README and `current_state.json` | 11,223 | 2,806 |

The optimized set is **78.6% smaller**. The before figure excludes the old
entry-point and manifest while the after figure includes both, so the reported
reduction is conservative. Task-specific policy files are loaded only by the
matching manifest route.

Regression test: `.codex/hooks/test_context_contract.py` enforces a 15,000-byte
ceiling and at least 60% reduction against the recorded baseline.

## Per-prompt hook output and latency

| Hook | Before | After | Change |
|---|---:|---:|---:|
| Task reminder | 1,457 chars / ~364 tokens | 69 chars / ~17 tokens | 95.3% fewer chars |
| Skill router | 586 chars / ~146 tokens | 324 chars / ~81 tokens | 44.7% fewer chars |
| Combined | 2,043 chars / ~510 tokens | 393 chars / ~98 tokens | 80.8% fewer chars |

Representative warm skill-router latency fell from the audit's 149.5 ms to
58.7 ms after cache activation. The measured cold cache population was 417.5 ms;
subsequent valid-cache calls avoid recursive skill discovery. Task-gate runtime
remained about 36 ms.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 .codex/hooks/test_context_contract.py -q
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s .codex/hooks -p 'test_*.py' -q
python3 .codex/hooks/project_state.py validate
python3 .codex/hooks/automation_registry.py validate
```

Historical prose, events and decisions remain available for audit but are not
default model context.
