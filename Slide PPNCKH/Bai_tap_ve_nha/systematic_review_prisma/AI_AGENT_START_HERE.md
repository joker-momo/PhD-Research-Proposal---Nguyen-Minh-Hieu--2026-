# AI Agent Start Here

1. Read `MUST_READ_AI_AGENT/context_manifest.yaml`.
2. Read the files in `core_read_order`. From the repository root, run
   `core_state_command` and use its output as the default state context.
3. Read only the policy files in the route matching the current task; union and
   deduplicate routes for a multi-purpose task.
4. Inspect only task-relevant artifacts from `06_FILE_MAP.md`. Read the
   canonical state JSON only for details needed by the current task.

On restart, compaction or model change, repeat these four steps. Historical
handoffs, event logs and full policy documents are not default context unless a
route or investigation requires them. If a required file is missing, stop and
report its exact path; never recreate rules from memory.
