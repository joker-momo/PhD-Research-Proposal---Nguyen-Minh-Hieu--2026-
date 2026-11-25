# HK261 Split-Brain Workspace Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve every HK261 research artifact, reconcile the divergent root and research worktrees, and make the root checkout the single portable workspace for Codex and Antigravity.

**Architecture:** Treat the current research worktree as the source of accepted screening state, the dirty root checkout as an untrusted-but-preserved source of main-only canonical artifacts, and a verified external backup as the rollback boundary. Import only inventoried HK261 paths, make the 46-report manifest workspace-relative, merge the root's CodeGraph commit into the migration branch, then fast-forward `main` and restore the ignored evidence pack into the root checkout. Remove the cache symlink only after two independent checksum comparisons pass.

**Tech Stack:** Git worktrees, Python 3 standard library, `pypdf`, JSON/CSV/Markdown, SHA-256 (`shasum -a 256`), `rsync`, project hook/tests.

**Spec:** `MUST_READ_AI_AGENT/CURRENT_HANDOFF.md`, `MUST_READ_AI_AGENT/06_FILE_MAP.md`, and the user-approved migration constraints recorded in **Global Constraints** below.

## Global Constraints

- Scope is only `Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/` plus Git metadata needed to merge the existing root CodeGraph commit; do not modify, stage, clean, stash, or delete unrelated root-checkout files.
- Preserve all 46 PDFs and all 46 extracted-text files before removing any worktree or symlink; SHA-256 mismatch count must equal zero.
- Remove `sources/candidate_fulltext` from the final root workspace after the durable evidence pack is verified; do not leave a second live PDF source.
- The canonical shared workspace after migration is `/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)` on `main`.
- Both Codex and Antigravity must use that exact root checkout after migration; no hidden research worktree remains active.
- Preserve accepted screening state through commit `5eaae0e7febdbd25047fca4cccab8aad776414ac`; do not dispatch Batch 04 during migration.
- Preserve the root-only CodeGraph commit `60b068c345f8be28853c70d53c4e6ac7fa000423`.
- Track canonical metadata, scripts, tests, and checksum ledgers; keep copyrighted/full-text PDFs and extracted text ignored by Git.
- Never bulk-add the root's untracked research tree. Every imported path must have an explicit disposition in the reconciliation inventory.
- A pre-existing dirty root is not a migration failure. Success means zero new uncommitted agent residue and zero unclassified paths inside `systematic_review_prisma/`.

## Review Focus

- A PDF copied successfully but corrupted or replaced: compare source, backup, and restored-root SHA-256 values for all 46 IDs.
- A manifest works only in the old worktree: tests must resolve all 46 relative PDF/text locators after copying the project to a temporary directory.
- A root-only artifact is silently lost: inventory every root-only path before changing the root project directory and require an explicit `IMPORT`, `ARCHIVE`, `GENERATED`, or `SYMLINK_REMOVE` disposition.
- The symlink is removed before its unique files are preserved: block removal until cache inventory and backup checksums both pass.
- Git integration overwrites unrelated user work: stage only explicit project paths, require a fast-forward merge, and compare the root's out-of-scope status before and after.

---

### Task 1: Freeze and Verify the Rollback Set

**Files:**
- Create: `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/README.md`
- Create: `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/checksums/research_pdf.sha256`
- Create: `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/checksums/research_text.sha256`
- Create: `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/checksums/cache_candidate_fulltext.sha256`
- Create: `migration/reconciliation_inventory.tsv`

**Interfaces:**
- Consumes: clean migration branch at `5eaae0e`; dirty root baseline at `60b068c`; research `screening_46/{pdf,text}`; root `sources/candidate_fulltext` symlink target.
- Produces: immutable backup directories plus an inventory with columns `path`, `side`, `kind`, `size_bytes`, `sha256_or_link_target`, `disposition`, `reason`.

- [ ] **Step 1: Capture both Git baselines without mutation**

Run `git status --porcelain=v1`, `git rev-parse HEAD`, `git branch --show-current`, and `git worktree list --porcelain` for the root and research worktrees; save the outputs in the backup README. Expected: migration branch clean; root baseline recorded exactly, including unrelated modifications.

- [ ] **Step 2: Copy the rollback sources without deleting originals**

Copy the complete root `systematic_review_prisma/` tree with symlinks preserved and the research `screening_46/pdf/` and `screening_46/text/` directories into the backup root using `rsync -a`; do not use `--delete`.

- [ ] **Step 3: Generate normalized SHA-256 ledgers**

Generate ledgers sorted by relative path for the 46 research PDFs, 46 research texts, and every regular file under the cache symlink target. Expected counts: PDF `46`, text `46`, cache PDF `29`; any observed count change blocks the migration and is reported rather than normalized away.

- [ ] **Step 4: Verify the backup copies independently**

Regenerate checksums from the backup copies and compare with `diff -u`. Expected: three empty diffs and checksum mismatch count `0`.

- [ ] **Step 5: Build the reconciliation inventory**

List every path that exists only in root, only in the research worktree, or differs by content. Assign exactly one disposition: `IMPORT`, `KEEP_RESEARCH`, `ARCHIVE`, `GENERATED`, or `SYMLINK_REMOVE`. Expected: blank disposition count `0`; paths outside `systematic_review_prisma/` included in the inventory `0`.

- [ ] **Step 6: Commit the inventory**

Run the pre-commit cleanup gate, stage only `migration/reconciliation_inventory.tsv`, and commit with `docs(hk261): inventory split-brain workspace state`.

### Task 2: Restore the Canonical Research Contract

**Files:**
- Create from root baseline when absent: `protocol.md`
- Create from root baseline when absent: `protocol_amendment_001.md`
- Create from root baseline when absent: `protocol_amendment_002.md`
- Create from root baseline when absent: `final_query_translations.md`
- Create from root baseline when absent: `formal_search_log_v0.2.csv`
- Create from root baseline when absent: `screening_log.csv`
- Create from root baseline when absent: `study_report_map.csv`
- Create from root baseline when absent: `prisma_2020_checklist_working.md`
- Modify: `migration/reconciliation_inventory.tsv`

**Interfaces:**
- Consumes: Task 1 inventory and backup; canonical path list in `MUST_READ_AI_AGENT/06_FILE_MAP.md`.
- Produces: one migration branch containing every mandatory canonical path while retaining the newer accepted screening state.

- [ ] **Step 1: Verify each import source against the root backup**

For each of the eight missing canonical files, compare the live root file to its backup checksum and record the checksum in the inventory. Expected: eight matches; mismatch count `0`.

- [ ] **Step 2: Import only the eight approved canonical files**

Add the files byte-for-byte from the verified backup. Do not overwrite an existing migration-branch file and do not import a directory wholesale.

- [ ] **Step 3: Check the entire canonical file map**

Verify every non-historical path in `MUST_READ_AI_AGENT/06_FILE_MAP.md` exists. Expected: missing required path count `0`; paths still intentionally external or ignored are labelled in the inventory.

- [ ] **Step 4: Audit scientific identity fields**

Check that protocol dates, 2021 cutoff, target venue, and screening counts were not changed by the byte-for-byte import. Expected: protocol window begins `2021-01-01`; accepted screening remains `18/46`, `17 INCLUDE`, `1 EXCLUDE`.

- [ ] **Step 5: Commit the canonical contract restoration**

Run cleanup and secret scans, stage the eight files plus the inventory, and commit with `fix(hk261): restore canonical review contract`.

### Task 3: Make Screening Paths Portable With Tests

**Files:**
- Create: `scripts/screening_paths.py`
- Create: `scripts/test_screening_paths.py`
- Modify: `scripts/check_46screening.py`
- Modify: `scripts/prepare_46screening.py`
- Modify: `screening_46/manifest.json`

**Interfaces:**
- Consumes: manifest record fields `source`, `pdf`, and `text`.
- Produces: `resolve_screening_path(screening_root: Path, locator: str) -> Path` and `to_screening_locator(screening_root: Path, path: Path) -> str`; relative locators are resolved from `screening_46/`, while absolute locators remain readable only for backward-compatible audit artifacts.

- [ ] **Step 1: Write failing unit tests**

Add tests named `test_relative_locator_resolves_from_screening_root`, `test_absolute_locator_remains_backward_compatible`, `test_locator_outside_screening_root_is_rejected_for_new_manifest`, and `test_manifest_resolves_after_project_copy`. Assertions must cover all 46 PDF and 46 text records.

- [ ] **Step 2: Run the tests and confirm the expected failure**

Run `python3 -m unittest scripts/test_screening_paths.py -v`. Expected: failure because `screening_paths.py` does not yet provide the two declared functions.

- [ ] **Step 3: Implement the path helpers**

Implement the two exact interfaces in `scripts/screening_paths.py`. New locators must use POSIX relative paths and reject `..` traversal outside `screening_46/`.

- [ ] **Step 4: Update manifest consumers and producer**

Use `resolve_screening_path` in `check_46screening.py`. Make `prepare_46screening.py` emit `pdf/<ID>.pdf` and `text/<ID>.txt`; retain original provenance in a non-executable `source_provenance` field and set `source` to the canonical relative PDF locator.

- [ ] **Step 5: Rewrite the frozen manifest mechanically**

For exactly 46 records, replace absolute `pdf` and `text` values with relative locators, preserve IDs/DOIs/titles/SHA-256/page counts/status unchanged, move the old source string to `source_provenance`, and set `source` to the canonical relative PDF locator.

- [ ] **Step 6: Run portability and accepted-batch regression tests**

Run `python3 -m unittest scripts/test_screening_paths.py -v`, then run `check_46screening.py` against the three accepted batch JSON files. Expected: all unit tests pass; each accepted batch reports zero `mechanical_errors`; quote match counts are unchanged.

- [ ] **Step 7: Commit the portable manifest change**

Run the cleanup gate, stage only the five owned files, and commit with `fix(hk261): make screening evidence paths portable`.

### Task 4: Install the Durable 46-Report Evidence Pack

**Files:**
- Create: `screening_46/evidence_checksums.sha256`
- Modify: `screening_46/.gitignore`
- Preserve ignored: `screening_46/pdf/*.pdf`
- Preserve ignored: `screening_46/text/*.txt`
- Modify: `migration/reconciliation_inventory.tsv`

**Interfaces:**
- Consumes: verified Task 1 backup and Task 3 relative manifest.
- Produces: one canonical ignored evidence pack at `screening_46/{pdf,text}` plus a tracked checksum ledger covering all 92 files.

- [ ] **Step 1: Create the tracked evidence ledger**

Generate sorted SHA-256 entries using paths relative to `screening_46/`. Expected: exactly 92 unique rows, 46 under `pdf/` and 46 under `text/`.

- [ ] **Step 2: Verify manifest-to-ledger correspondence**

For each manifest ID, verify the PDF digest equals its `sha256`, both PDF and text paths exist, and both appear once in the ledger. Expected: missing files `0`, duplicate IDs `0`, PDF digest mismatches `0`, unreferenced ledger rows `0`.

- [ ] **Step 3: Harden ignore rules without hiding metadata**

Keep `pdf/` and `text/` ignored; explicitly ensure `manifest.json`, `evidence_checksums.sha256`, briefs, accepted results, and reviews are not ignored.

- [ ] **Step 4: Validate from a temporary relocated project copy**

Copy the project plus ignored evidence pack to a temporary directory, run the Task 3 unit tests and batch checks there, then remove only the explicit temporary copy. Expected: all checks pass with no reference to `/Users/joker/.codex/worktrees/` or `~/.cache/codex-artifacts/`.

- [ ] **Step 5: Commit the durable-evidence metadata**

Stage only the checksum ledger, `.gitignore`, and inventory; commit with `chore(hk261): register durable screening evidence pack`.

### Task 5: Authorize Cache-Symlink Retirement Safely

**Files:**
- Classify for removal during root promotion: `sources/candidate_fulltext` symlink
- Modify: `migration/reconciliation_inventory.tsv`
- Create: `migration/cache_candidate_disposition.tsv`

**Interfaces:**
- Consumes: cache checksum ledger from Task 1 and canonical evidence checksums from Task 4.
- Produces: a per-cache-file disposition mapping and proof that no unique report will be lost when Task 7 retires the live symlink.

- [ ] **Step 1: Map every cache file to the canonical pack or archive**

For every regular cache file, record `cache_relative_path`, `sha256`, `canonical_id_or_ARCHIVE_ONLY`, `canonical_relative_path_or_backup`, and `match_status`. Expected: cache file count equals Task 1 count; blank mappings `0`.

- [ ] **Step 2: Prove report coverage before removal**

Verify every C01-C25 and SNCS PDF has one matching canonical ID by checksum or an explicit version-difference note with both copies retained in backup. Expected: IDs covered `26/26`; unexplained unique cache PDFs `0`.

- [ ] **Step 3: Mark only the symlink for retirement**

Do not mutate the live root checkout or delete the target cache directory in this task. After Steps 1-2 pass, mark the link `SYMLINK_REMOVE` in the inventory and verify no migration-branch artifact depends on it. Task 7 removes it from the live workspace by archiving the old root project tree and intentionally not restoring the link.

- [ ] **Step 4: Scan for obsolete cache dependencies**

Search active scripts, manifests, briefs 04-08, and canonical docs for the literal cache target and old worktree prefix. Expected: executable/current references `0`; historical accepted briefs may retain old locators only when labelled historical and not used for future dispatch.

- [ ] **Step 5: Commit the symlink disposition evidence**

Stage the two migration TSV files; commit with `fix(hk261): retire external candidate fulltext link`.

### Task 6: Reconcile Git Histories on the Migration Branch

**Files:**
- Merge existing root-only tracked files: `.codegraph/.gitignore`, `.codegraph/config.json`, `.cursor/rules/codegraph.mdc`
- Modify if required by conflict only: task-owned project paths already listed above

**Interfaces:**
- Consumes: migration branch with Tasks 1-5 and root `main` at `60b068c`.
- Produces: one migration branch that contains both histories and can fast-forward `main`.

- [ ] **Step 1: Verify root `main` has not advanced unexpectedly**

Run `git rev-parse main`. Expected: `60b068c345f8be28853c70d53c4e6ac7fa000423`; if different, stop and re-audit the new commits.

- [ ] **Step 2: Merge `main` into the migration branch**

Run a non-squash, non-force merge. Resolve conflicts only inside the owned project paths; the CodeGraph files must retain the root version.

- [ ] **Step 3: Run the full migration verification suite**

Run unit tests, three accepted-batch mechanical checks, `git diff --check`, manifest/checksum verification, canonical-path existence check, cache/worktree literal scan, and project hook tests. Expected: failures `0`, unsupported deleted paths `0`.

- [ ] **Step 4: Audit the merge commit**

Inspect `git diff main...HEAD`, run the dead-code/cleanup gate, and verify no unrelated root file appears. Commit conflict resolution only if Git did not create the merge commit automatically.

### Task 7: Promote the Root Checkout as the Single Workspace

**Files:**
- Replace only the root `systematic_review_prisma/` working tree with the verified migration result
- Restore ignored: root `screening_46/pdf/*.pdf`
- Restore ignored: root `screening_46/text/*.txt`
- Preserve: all out-of-scope root files exactly as captured in Task 1

**Interfaces:**
- Consumes: merged migration branch and verified backup.
- Produces: root `main` at the migration tip, with the portable 46-report evidence pack and no live cache symlink.

- [ ] **Step 1: Re-check the live root baseline**

Compare out-of-scope `git status --porcelain=v1` to Task 1. Expected: no unexpected path/content change caused by the migration; any user change made since Task 1 is preserved and recorded.

- [ ] **Step 2: Move the old root project directory to the rollback backup**

Use a recoverable move to the explicit Task 1 backup location only after verifying that backup. This retires the live `sources/candidate_fulltext` symlink without deleting its cache target. Do not remove, overwrite, or move any sibling outside `systematic_review_prisma/`.

- [ ] **Step 3: Fast-forward `main`**

Run `git merge --ff-only fix/hk261-reconcile-canonical-workspace` in the root checkout. Expected: fast-forward succeeds; `main` contains `60b068c`, `5eaae0e`, and every migration commit.

- [ ] **Step 4: Restore ignored evidence into the root workspace**

Copy the verified 46 PDFs and 46 texts from the backup into root `screening_46/{pdf,text}`. Do not restore `sources/candidate_fulltext`.

- [ ] **Step 5: Verify the root workspace independently**

Run the full Task 6 suite from the root path, verify 92 checksum rows, and assert the manifest contains no absolute `pdf`, `text`, or active `source` locator. Expected: failures `0`; symlink count `0`; cache/worktree active references `0`.

- [ ] **Step 6: Compare root out-of-scope state**

Compare the recorded root baseline to current status excluding the project directory. Expected: migration-caused added/removed/modified paths outside scope `0`.

### Task 8: Publish the Handoff and Remove Temporary Git State

**Files:**
- Modify: `MUST_READ_AI_AGENT/CURRENT_HANDOFF.md`
- Modify: `MUST_READ_AI_AGENT/context_manifest.yaml`
- Modify: `corpus_expansion/current_tasks.md`
- Modify: `migration/reconciliation_inventory.tsv`

**Interfaces:**
- Consumes: verified root workspace from Task 7.
- Produces: current navigation state naming root `main` as the only workspace and Batch 04 as the next still-undispatched research task.

- [ ] **Step 1: Update durable status files**

Record the new `main` SHA, root workspace path, checksum results, backup path, removed symlink, retained out-of-scope dirty baseline, and the fact that Batch 04 remains undispatched.

- [ ] **Step 2: Run freshness and content tests**

Run the status-guard test suite and verify `CURRENT_HANDOFF.md` plus `current_tasks.md` are touched by the latest project commit. Expected: all tests pass and stale-status failures `0`.

- [ ] **Step 3: Commit the final handoff**

Run cleanup/secret/diff checks, stage the four explicit files, and commit with `docs(hk261): publish unified workspace handoff`.

- [ ] **Step 4: Verify root `main` after the handoff commit**

If the handoff commit was created in the migration worktree, fast-forward root `main` once more and rerun the status-guard tests. Expected: root `main` equals the migration tip.

- [ ] **Step 5: Remove the old research worktree and merged branches**

Only after root verification and backup checksum checks pass, remove the old linked worktree normally and delete fully merged local branches `fix/hk261-reconcile-canonical-workspace` and `codex/hk261-c01-evidence`. Never force-delete.

- [ ] **Step 6: Verify final repository topology**

Run `git worktree list --porcelain`, `git branch --merged main`, and scoped status checks. Expected: one project worktree at the root; only `main` retained among agent-created branches; zero new agent-owned uncommitted files; pre-existing unrelated root status preserved.

- [ ] **Step 7: Notify the main thread and IDE handoff**

Report the root path, final SHA, verification commands/results, backup path, and instruction that Codex and Antigravity must both open the root checkout. Do not begin or dispatch Batch 04 in the same task.

## Self-Review Record

- **Spec coverage:** All eight approved migration stages are represented; the two added user constraints are explicit in Tasks 5 and 7.
- **Step scan:** Each checkbox performs one observable mutation or verification; each commit follows a clean-tree gate.
- **Type consistency:** `screening_root`, `locator`, manifest fields, inventory columns, and checksum-ledger semantics are consistent across Tasks 1-8.
- **Review focus:** Each of the five failure modes has an owning test or verification step.
- **Proportion:** The plan is detailed because the migration crosses two divergent histories and two ignored evidence stores; implementation remains limited to the named paths and small path-helper code.
