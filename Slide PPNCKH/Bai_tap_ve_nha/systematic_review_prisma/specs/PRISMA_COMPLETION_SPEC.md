# Specification: Complete the HK261 PRISMA Systematic Review

**Document ID:** `HK261-PRISMA-COMPLETION-SPEC-v1`

**Status:** `DRAFT_FOR_HUMAN_APPROVAL`

**Created:** 2026-11-26

**Applies to:** `Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/`

**Current scientific baseline:** 46 reports; 36 working includes, 2 excludes, 8 uncertain; 24 detailed extractions, 12 minimum extractions; 24 partial appraisals; final study count unknown.
**Current manuscript baseline:** 22-page Springer Nature review copy, 53 cited references, explicitly interim and not submitted.

## 1. Objective

Complete a truthful, reproducible systematic review of collaborative neural-network inference in UAV swarms, reported with PRISMA 2020, and produce a consistent LaTeX/PDF manuscript whose claims are supported by accepted full-text evidence.

The specification separates three completion levels so that one cannot be mistaken for another:

1. **Review complete:** searches, record management, selection, extraction, appraisal, synthesis and PRISMA reporting are complete.
2. **Manuscript submission-ready:** review complete, manuscript scientifically and visually verified, venue/template and authorship metadata approved.
3. **HK261 coursework complete:** manuscript actually submitted after explicit authorization, the journal receipt is archived, and course evidence is forwarded as required.

The immediate implementation goal after approval of this specification is **Level 1**. Level 2 requires author decisions. Level 3 requires explicit user authorization and live external actions.

## 2. Authority and precedence

Apply requirements in this order:

1. Current system/developer instructions and the latest user instruction.
2. Official HK261 assignment PDF.
3. Recorded user decisions in `MUST_READ_AI_AGENT/01_PROJECT_CHARTER.md` and canonical `current_state.json`.
4. `protocol.md` and dated protocol amendments.
5. Accepted evidence, project gates and this approved specification.
6. Historical plans, provider output and reviewer comments.

Reviewer comments are inputs, not authority. A requested change enters implementation only after it is verified against the manuscript and sources.

## 3. Confirmed requirements

- Review type: systematic review reported using PRISMA 2020.
- Topic: collaborative DNN/neural-network inference in multi-UAV or UAV-swarm systems, focusing on partitioning, orchestration and resilience.
- Publication window: 2021-01-01 through the documented final search date.
- Evidence must come from real sources. Fabricated citations, DOI values, counts, results, dates, author approvals and submission evidence are forbidden.
- Detailed extraction and quantitative synthesis require readable full text.
- Records, reports and studies are distinct accounting units.
- Reviews may support positioning and citation chaining but are not primary included studies.
- Canonical manuscript is LaTeX compiled to PDF.
- Codex owns writing, project edits, acceptance, Git and final user-facing text.
- Gemini or the approved low-cost fallback may return read-only research evidence; neither writes final prose nor accepts its own output.
- Every task uses one branch/worktree, one task-owned diff, explicit validation, an atomic commit, fast-forward integration and cleanup.
- Every task updates current state and appends matching timestamped event/decision evidence.
- Submission and course email are prohibited until the user explicitly authorizes those external actions.

## 4. Assumptions and open decisions

### 4.1 Assumptions used by this specification

1. The existing 46-report corpus remains evidence, but is not assumed to be the complete corpus.
2. The 36 working inclusions remain provisional until human adjudication and study-family reconciliation finish.
3. The 53 current references remain candidates for the final bibliography; their presence does not replace source, retraction and metadata verification.
4. Narrative synthesis is the default. Meta-analysis is permitted only if a homogeneous subset has compatible outcomes and variance information.
5. A single human author may perform final adjudication under the fixed protocol. Independent dual-human screening and Cohen's kappa are optional robustness enhancements, not universal PRISMA requirements.
6. A unified mathematical formulation is optional and target-dependent. It must not be introduced merely to imitate a survey journal.

### 4.2 Human decisions required

| Decision ID | Decision | Current default | Blocks |
|---|---|---|---|
| DEC-01 | Final venue and template | SN Computer Science/Springer Nature is canonical | Final formatting and submission package |
| DEC-02 | Whether the earlier IEEE-template request supersedes SN Computer Science | Not resolved; do not maintain two active manuscripts | Final template conversion |
| DEC-03 | Author order, corresponding author and supervisor | Unknown | Submission-ready status |
| DEC-04 | Verified HCMUT email, affiliations, ORCID and doctoral student ID | Unknown | Author block and submission |
| DEC-05 | Contributions, funding, conflicts, data availability and final AI declaration | Unknown | Declarations and submission |
| DEC-06 | Examination date | Unknown; never guess | Course deadline calculation |
| DEC-07 | Authorization to submit and later send course email | Not granted | External actions |

Scientific work that does not depend on DEC-01 through DEC-07 should continue after this specification is approved.

## 5. Definitions

- **Record:** one database/export entry before deduplication.
- **Report:** one retrievable paper, preprint or document.
- **Study:** one underlying investigation; several reports may belong to one study.
- **Accepted evidence:** evidence that passed every mandatory criterion in a Codex review table.
- **Uncertain:** evidence is insufficient for a final decision. It is not a synonym for include or exclude.
- **Not reported:** the full report was checked and the item was not found.
- **Not extracted:** the extraction has not yet established whether the item is reported.
- **Review complete:** all Level-1 definition-of-done criteria in Section 8 pass.

## 6. Required project structure

| Purpose | Canonical location |
|---|---|
| Protocol and amendments | `protocol.md`, `protocol_amendment_*.md` |
| Exact platform queries | `final_query_translations.md` |
| Immutable raw exports | `sources/raw/` |
| Normalized records | `sources/normalized/` |
| Formal search ledger | `formal_search_log_v0.2.csv` or a versioned successor |
| Record screening | `screening_log.csv` or a versioned successor |
| Report/study linkage | `study_report_map.csv` |
| Full-text evidence | `screening_46/` plus versioned delta intake |
| Final extraction/appraisal | New dated/versioned release directory; do not overwrite accepted releases |
| Claim-source matrix | New final release directory |
| PRISMA checklist | `prisma_2020_checklist_working.md`, promoted only after final audit |
| Manuscript source | `manuscript/sn_computer_science/main.tex` unless DEC-01/DEC-02 changes it |
| Bibliography | `manuscript/sn_computer_science/references.bib` |
| Compiled PDF | Canonical `main.pdf`; user-friendly copies belong under `output/` |
| Current state/history | `MUST_READ_AI_AGENT/current_state.json`, `events.jsonl`, Git |
| Automation evidence | `automation/decision_log.jsonl`, `artifact_catalog.json` |
| Submission proof | `submission_evidence/` |

## 7. Global execution contract

Every task below must use this record before work begins:

```text
TASK: <one concrete task>
OWNER: CODEX_WRITING | GEMINI_RESEARCH | USER_ACTION
OWNED_PATHS: <explicit paths>
BINARY_ACCEPTANCE: <numeric/binary checks>
PRE_TASK_GIT_STATUS: <branch, staged/modified/untracked counts, preceding commit>
CODE_FIRST_DECISION: REUSE_EXISTING | WRITE_SCRIPT | MANUAL -- <reason>
```

For a Gemini task, Codex must commit the structured brief before dispatch. The brief must contain `TASK`, `REQUIRED WORK`, `REQUIRED OUTPUT`, `ACCEPTANCE CRITERIA` and `BOUNDARIES`. Codex then produces a criterion-by-criterion PASS/FAIL review. A result with any mandatory FAIL remains quarantined.

One task must be committed and integrated before the next task starts. Do not group unrelated phases into one commit.

## 8. Definitions of done

### 8.1 Level 1 — systematic review complete

All of the following must pass:

- [ ] Four planned core sources have completed searches or a documented protocol amendment changes the source set before the final search.
- [ ] Every executed search has platform, exact query, filters, actual date, reported total, exported total, immutable raw file and checksum.
- [ ] All raw records are imported; import count equals the sum of exports after documented platform/export limitations.
- [ ] Duplicate normalized DOI count is zero.
- [ ] Duplicate normalized title/year/first-author records are resolved or explicitly linked.
- [ ] Every record has a title/abstract decision.
- [ ] Every potentially eligible report has a retrieval status.
- [ ] Every retrieved full-text report has a final include/exclude decision and one primary reason when excluded.
- [ ] The current eight uncertain reports are reduced to zero unresolved final eligibility decisions.
- [ ] Nguyễn Minh Hiếu has adjudicated every final full-text eligibility decision.
- [ ] Every included report is linked to a final study family or explicitly justified as a standalone study.
- [ ] Final record, report and study counts reconcile with zero unexplained difference.
- [ ] Every included study/report has a complete extraction row; each required field contains a source locator, `not reported`, or a justified `not applicable` value.
- [ ] Every included study has ten appraisal-domain judgments with rationale; no `WITHHELD` or `NOT_ASSESSED` remains.
- [ ] Every quantitative manuscript claim has source, locator, conditions, unit and evidence boundary.
- [ ] All review questions have a claim-source matrix and evidence-bounded synthesis.
- [ ] Reporting-bias, certainty and sensitivity methods are performed where justified, or their non-performance is explicitly justified without implying low bias/high certainty.
- [ ] Final PRISMA flow uses reconciled counts.
- [ ] All 27 PRISMA checklist items contain accurate locators and statuses; `PARTIAL`, `NOT PERFORMED`, `NOT ASSESSED` and `UNCONFIRMED` remain only when genuinely inapplicable or disclosed as a final limitation.

### 8.2 Level 2 — manuscript submission-ready

Level 1 passes, plus:

- [ ] Venue and official template are confirmed once; zero competing active manuscript sources.
- [ ] Author order, consent, corresponding author, supervisor, HCMUT/VNU-HCM affiliations, HCMUT email and ORCIDs are verified.
- [ ] Contributions, funding, conflicts, data availability, acknowledgements and AI declaration are approved.
- [ ] Title, Abstract, Keywords, Methods, Results, Discussion, Introduction and Conclusion agree with the final evidence.
- [ ] All cited sources are opened and verified; unresolved DOI/identity/retraction/correction cases equal zero or are removed.
- [ ] Bibliography contains only cited sources; undefined and uncited bibliography keys equal zero.
- [ ] LaTeX build has zero fatal errors, undefined citations/references and overfull boxes.
- [ ] Every PDF page is visually inspected at readable resolution; clipped/overlapping/unreadable elements equal zero.
- [ ] Independent manuscript review has no unresolved critical finding.
- [ ] All authors approve the exact final PDF and source package.

### 8.3 Level 3 — HK261 coursework complete

Level 2 passes, plus:

- [ ] User explicitly authorizes submission to one verified venue.
- [ ] Portal metadata equals the approved manuscript metadata.
- [ ] System-generated submitted copy, manuscript ID, timestamp and receipt are archived.
- [ ] Exact exam date is known and the three-day deadline is calculated without guessing.
- [ ] User explicitly authorizes the course email.
- [ ] Evidence is forwarded to `duyanhnguyen@hcmut.edu.vn` with the prescribed subject, name, verified doctoral student ID, manuscript ID and receipt.
- [ ] Sent-message evidence is archived without committing credentials or private mailbox contents.

## 9. Dependency graph

```mermaid
flowchart TD
  G0[Governance and protocol freeze] --> S0[Four-source search]
  S0 --> D0[Import and deduplicate]
  D0 --> E0[Title/abstract and full-text selection]
  E0 --> F0[Study-family reconciliation]
  E0 --> X0[Complete extraction]
  F0 --> P0[Final PRISMA arithmetic]
  X0 --> Q0[Ten-domain appraisal]
  Q0 --> Y0[Claim-source matrix and synthesis]
  P0 --> Y0
  Y0 --> M0[Manuscript revision]
  M0 --> V0[Integrity, build and peer review]
  V0 --> A0[Author approval]
  A0 --> U0[Explicitly authorized submission]
  U0 --> C0[Course evidence]
```

Search, screening, extraction and manuscript writing may use parallel read-only research tasks only when their inputs are frozen and their owned records do not overlap. Acceptance and project writes remain sequential under Codex.

## 10. Task specification

### Phase G — governance, scope and canonical baseline

#### G-01 — Approve this specification

- **Owner:** `USER_ACTION`; Codex records the decision.
- **Dependencies:** none.
- **Required work:** Review scope, completion levels, task dependencies, open decisions and non-goals. Record requested amendments before research resumes.
- **Output:** Approved spec version or a dated superseding version.
- **Acceptance:** One explicit user approval; unresolved spec objections listed; zero implementation task started before approval.
- **Verify:** Git history contains the approved version; `current_state.json.next_task` points to G-02 or another approved first task.

#### G-02 — Restore a canonical, non-ambiguous working baseline

- **Owner:** `CODEX_WRITING`; any user-created rename requires confirmation.
- **Dependencies:** G-01.
- **Required work:** Resolve the current deleted `main.pdf` plus same-hash renamed copy; remove or ignore `.DS_Store` residue without deleting user research; ensure one canonical manuscript PDF and optional copy under `output/`.
- **Output:** Canonical path matches `06_FILE_MAP.md`; task-owned Git status clean.
- **Acceptance:** `main.pdf` exists at the canonical path; SHA-256 equals the accepted PDF or a newly built verified PDF; ambiguous duplicate active PDFs = 0; task-owned dirty paths = 0.
- **Verify:** `git status --short`, SHA-256 comparison, project-state validation.

#### G-03 — Confirm review scope and venue/template policy

- **Owner:** `USER_ACTION` for DEC-01/DEC-02; `CODEX_WRITING` records the choice.
- **Dependencies:** G-01.
- **Required work:** Confirm SN Computer Science/Springer or explicitly replace it with an IEEE journal/template. Verify current venue scope and current official template if the decision changes.
- **Output:** One dated venue decision; one canonical manuscript path.
- **Acceptance:** Active venue count = 1; active manuscript source count = 1; historical versions clearly labelled; no silent template conversion.
- **Verify:** Project charter, file map and current state agree.

#### G-04 — Freeze final protocol before the final search

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** G-01; G-03 only if venue imposes relevant review requirements.
- **Required work:** Recheck RQs, eligibility, date boundary, source set, query concepts, selection, extraction, appraisal and synthesis. Create a dated amendment only for an actual change and state its impact on completed work.
- **Output:** Frozen protocol plus amendments and version identifier.
- **Acceptance:** Every method element has one canonical definition; undisclosed retrospective changes = 0; RQs and extraction fields map one-to-one.
- **Verify:** Protocol diff audit and amendment table.

### Phase S — reproducible identification search

#### S-01 — Validate platform queries and seed coverage

- **Owner:** `GEMINI_RESEARCH` for verification notes; `CODEX_WRITING` accepts and writes.
- **Dependencies:** G-04.
- **Required work:** Verify the eight translated queries against the frozen concepts and known seeds. Identify syntax unsupported by each platform. Do not execute or claim searches.
- **Output:** Query validation matrix for IEEE, ACM, Scopus and Web of Science.
- **Acceptance:** 8/8 queries present; all mandatory concepts represented; 20 seed × 8 query cells evaluated or documented shortfall; unsupported syntax count and corrections explicit; fabricated result counts = 0.
- **Verify:** Deterministic matrix checker or CSV assertions; Codex PASS/FAIL table.

#### S-02 — Execute and archive IEEE Xplore search

- **Owner:** `USER_ACTION` if institutional login/takeover is required; otherwise `CODEX_WRITING`; Gemini may verify metadata afterward.
- **Dependencies:** S-01.
- **Required work:** Run the approved IEEE query through the official interface, apply the date/document filters, export all permitted results and record caps/errors.
- **Output:** Immutable raw export and one search-log row.
- **Acceptance:** Exact query, filters, actual timestamp, reported total, exported total, file name, checksum and limitation all non-empty; reported/export arithmetic explained; no inferred count after access failure.
- **Verify:** Raw file parses; row count equals exported total or documented platform export behavior.

#### S-03 — Execute and archive ACM Digital Library search

- **Owner/dependencies/work/output:** Same contract as S-02, using ACM's official interface.
- **Dependencies:** S-01.
- **Acceptance:** Same eight required log fields; raw export parse succeeds; no Cloudflare/access page counted as a result export.
- **Verify:** Parsed count and checksum.

#### S-04 — Execute and archive Scopus search

- **Owner/dependencies/work/output:** Same contract as S-02, using institutional Scopus access.
- **Dependencies:** S-01.
- **Acceptance:** Same eight required log fields; complete export or explicit documented platform cap and continuation exports.
- **Verify:** Sum of continuation exports equals logged exported total; duplicate export rows identified for later deduplication, not silently removed from raw files.

#### S-05 — Execute and archive Web of Science Core Collection search

- **Owner/dependencies/work/output:** Same contract as S-02, using institutional Web of Science access.
- **Dependencies:** S-01.
- **Acceptance:** Same eight required log fields; complete export or explicit documented platform cap and continuation exports.
- **Verify:** Parsed count, checksum and continuation arithmetic.

#### S-06 — Supplementary citation searching

- **Owner:** `GEMINI_RESEARCH`; Codex accepts.
- **Dependencies:** S-02 through S-05.
- **Required work:** Perform backward and forward citation searching for included primary studies and directly relevant reviews using official/publisher/citation-index locators. Supplementary records undergo the same eligibility process.
- **Output:** Supplementary-discovery ledger with parent source and discovery method.
- **Acceptance:** Every supplementary record has parent locator and discovery date; duplicate DOI/title after comparison with core exports is labelled, not silently dropped; unresolved items explicit; unsupported claims = 0.
- **Verify:** Codex criterion table and normalized identity checker.

### Phase D — import, normalization and deduplication

#### D-01 — Import all raw exports into a normalized record ledger

- **Owner:** `CODEX_WRITING`; code-first preference `REUSE_EXISTING`, then a small tested parser if formats require it.
- **Dependencies:** S-02 through S-06.
- **Required work:** Preserve raw files unchanged; parse every export; normalize field names, DOI and titles; retain source and raw-row provenance.
- **Output:** Versioned normalized record ledger and import audit.
- **Acceptance:** Every parsed raw row maps to exactly one normalized input row before deduplication; missing mandatory identity fields explicitly marked; import exceptions = 0 or documented per row; raw-file hash changes = 0.
- **Verify:** Automated count reconciliation and schema validation.

#### D-02 — Deduplicate records and link publication versions

- **Owner:** `GEMINI_RESEARCH` may investigate ambiguous identities; `CODEX_WRITING` accepts and writes.
- **Dependencies:** D-01.
- **Required work:** Deduplicate first by normalized DOI, then normalized title/year/first author; link preprint, conference and journal reports instead of deleting relationships.
- **Output:** Deduplicated record ledger, duplicate map and version-link candidates.
- **Acceptance:** Duplicate normalized DOI count in retained records = 0; duplicate normalized title identity count = 0 or explicitly linked; every removed record has retained-record ID and reason; arithmetic `raw normalized = retained + duplicates` has difference 0.
- **Verify:** Reproducible deduplication script/tests and Codex semantic review of ambiguous pairs.

#### D-03 — Map the existing 46 reports into the final record ledger

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** D-02.
- **Required work:** Link each existing report to one or more discovery records, or document why the report originates only from supplementary/user-supplied discovery.
- **Output:** 46-row provenance overlay.
- **Acceptance:** Existing report IDs accounted = 46/46; mapped-to-core, supplementary and user-supplied counts sum to 46; unmapped reports have explicit provenance limitation; four prior arXiv records reconciled.
- **Verify:** ID set equality and count arithmetic.

### Phase E — screening and final eligibility

#### E-01 — Title/abstract screening of all deduplicated records

- **Owner:** `GEMINI_RESEARCH` first pass; `CODEX_WRITING` acceptance; human author final gate occurs in E-05.
- **Dependencies:** D-02.
- **Required work:** Apply frozen eligibility criteria to every deduplicated record. Preserve include/exclude/uncertain and one reason.
- **Output:** Complete title/abstract screening ledger.
- **Acceptance:** Decision coverage = 100%; duplicate IDs = 0; every exclude has one controlled-vocabulary reason; every factual decision has source URL/export locator; silent omissions = 0.
- **Verify:** Schema/count checker and Codex PASS/FAIL review.

#### E-02 — Retrieve lawful full texts for potentially eligible new records

- **Owner:** `CODEX_WRITING` manages files; lawful retrieval priority is `paper-lookup` → `lawful-paper-pdf-retriever` → `nature-downloader`; user may supply inaccessible PDFs.
- **Dependencies:** E-01.
- **Required work:** Record lawful URL, version, retrieval date, readability and checksum. Do not use unauthorized retrieval routes.
- **Output:** Full-text intake ledger and lawful PDFs/text derivatives.
- **Acceptance:** Every potentially eligible record has status `retrieved`, `not retrieved after documented attempts`, or `awaiting user access`; every retrieved file opens and has identity/version evidence; corrupt files = 0.
- **Verify:** PDF open/text check, checksum and title-page identity audit.

#### E-03 — Full-text screening of new reports

- **Owner:** `GEMINI_RESEARCH` structured evidence; `CODEX_WRITING` accepts.
- **Dependencies:** E-02.
- **Required work:** Apply all inclusion/exclusion criteria to readable full texts with page/section evidence. Assign one primary reason to each exclusion.
- **Output:** Accepted full-text screening records and review tables.
- **Acceptance:** 100% retrieved reports decided or explicitly uncertain; every decision has exact locator; quantitative unsupported claims = 0; rejected A2A findings adopted = 0.
- **Verify:** Quote/page matcher plus Codex criterion table.

#### E-04 — Resolve the eight existing uncertain reports

- **Owner:** `GEMINI_RESEARCH` may verify official dates/scope; `CODEX_WRITING` accepts; author adjudicates in E-05.
- **Dependencies:** G-04 and available official evidence.
- **Required work:** Resolve C05, C09, C10, C13, C14, C19 publication timing and C06/SNCS scope using official publisher/DOI/full-text evidence. If public evidence remains unavailable, prepare one consolidated human decision packet without inventing dates.
- **Output:** Eight-row decision packet and accepted evidence review.
- **Acceptance:** Exactly 8 IDs; each row has binary question, evidence, locator, protocol rule, recommended decision and impact; unsupported date = 0; final `UNCERTAIN` after human adjudication = 0.
- **Verify:** Exact-ID and source-locator assertions.

#### E-05 — Human full-text eligibility adjudication

- **Owner:** `USER_ACTION` — Nguyễn Minh Hiếu; Codex records decisions.
- **Dependencies:** E-03 and E-04.
- **Required work:** Review every final full-text include/exclude decision, not only the eight prior uncertain reports. Record confirmation or correction with date.
- **Output:** Author-approved eligibility ledger.
- **Acceptance:** Human adjudication coverage = 100%; uncertain final decisions = 0; every correction retains prior decision history and reason.
- **Verify:** Adjudication field non-empty for every full-text report; count arithmetic.

#### E-06 — Reconcile study families and report versions

- **Owner:** `GEMINI_RESEARCH` investigates; `CODEX_WRITING` accepts; ambiguous merges may require author decision.
- **Dependencies:** E-05.
- **Required work:** Compare all candidate report pairs, including the 37 unresolved mechanical candidates. Shared authors/citations alone are insufficient. Use evidence of shared data, experiment, system version or explicit extension.
- **Output:** Complete `study_report_map.csv`, pair decisions and final study IDs.
- **Acceptance:** Every included report maps to one final study ID; unresolved candidate pairs = 0; unsupported merges = 0; same-report versions linked; final unique-study count reproducible.
- **Verify:** Pair coverage, report-set equality and family arithmetic.

### Phase X — complete extraction and appraisal

#### X-01 — Complete detailed extraction for the 12 minimum-extraction reports

- **Owner:** `GEMINI_RESEARCH`; Codex accepts and writes.
- **Dependencies:** E-05; family information may be provisional until E-06 but report IDs remain stable.
- **Required work:** Read full text and populate every frozen extraction field with source locators. Do not turn `not extracted` into `not reported` without checking the report.
- **Output:** 12 detailed report-level extraction rows and evidence review.
- **Acceptance:** Exactly 12 target IDs; required field coverage = 100% with locator/`not reported`/justified N/A; every numeric value has conditions and units; unsupported quantitative claims = 0.
- **Verify:** Schema, ID and locator checks; Codex field-by-field sample plus all quantitative cells.

#### X-02 — Extract all newly included reports

- **Owner:** `GEMINI_RESEARCH`; Codex accepts and writes.
- **Dependencies:** E-03/E-05.
- **Required work/output:** Same extraction schema and evidence standard as X-01 for every delta inclusion.
- **Acceptance:** Extraction rows equal delta included reports; missing rows = 0; detailed-field completion and quantitative evidence checks pass 100%.
- **Verify:** Set equality with final included-report ledger.

#### X-03 — Reassess Domain 9 for the existing 24-report subset

- **Owner:** `GEMINI_RESEARCH` may collect artifact evidence; `CODEX_WRITING` accepts.
- **Dependencies:** G-04.
- **Required work:** Apply the literal Domain-9 rule consistently to all 24 reports using code/data/trace/implementation evidence.
- **Output:** 24 Domain-9 judgments with rationales and locators.
- **Acceptance:** Judgments = 24; `WITHHELD` = 0; each judgment has rationale and evidence; coding rule applied identically.
- **Verify:** Field completeness and Codex consistency review.

#### X-04 — Complete ten-domain appraisal for every included study

- **Owner:** `GEMINI_RESEARCH` structured evidence; `CODEX_WRITING` accepts.
- **Dependencies:** X-01, X-02, X-03 and E-06.
- **Required work:** Produce yes/partial/no/not-applicable judgments with rationales. When several reports belong to one study, use the correct evidence set without double counting.
- **Output:** Final study-level appraisal table.
- **Acceptance:** Included studies × 10 domain cells accounted for; `NOT_ASSESSED` and `WITHHELD` = 0; every non-N/A judgment has locator; N/A has explicit justification.
- **Verify:** Cell-count arithmetic and structured rationale audit.

#### X-05 — Final source, metadata and integrity audit

- **Owner:** `GEMINI_RESEARCH` verification notes; `CODEX_WRITING` accepts and updates bibliography.
- **Dependencies:** E-06, X-01/X-02.
- **Required work:** Open every included original source and verify title, authors, year, venue, DOI, version, correction/retraction status and peer-review/publication type.
- **Output:** Source audit ledger and corrected bibliography evidence.
- **Acceptance:** Included sources checked = 100%; unresolved DOI/identity/version/retraction cases = 0 or source removed; duplicate DOI = 0; source URL/locator present for every check.
- **Verify:** DOI resolver/publisher metadata comparison plus Codex review. Line wrapping in a PDF is not a DOI error.

### Phase Y — synthesis and scientific contribution

#### Y-01 — Build the final claim-source matrix for RQ1–RQ5

- **Owner:** `CODEX_WRITING`; Gemini may return structured cross-report evidence.
- **Dependencies:** E-06, X-04, X-05.
- **Required work:** Map each intended synthesis claim to study IDs, reports, locators, conditions, evidence type and quality limitations.
- **Output:** Claim-source matrix.
- **Acceptance:** Every final Results/Discussion claim has at least one accepted evidence row; unsupported claims = 0; quantitative claims missing conditions/units = 0; report-level and study-level denominators explicit.
- **Verify:** Automated manuscript-claim registry where possible plus manual semantic audit.

#### Y-02 — Produce evidence-derived technical taxonomy

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** Y-01.
- **Required work:** Classify at minimum architecture, partition semantics, orchestration decisions, mobility/network assumptions and resilience mechanism. Separate peer-to-peer intra-swarm inference from multi-UAV-assisted hierarchical edge/cloud inference.
- **Output:** Taxonomy table/tree and definitions.
- **Acceptance:** Every leaf has at least one accepted study or is labelled an empty evidence gap; mutually exclusive/overlapping dimensions identified; C11/C16-like boundary cases represented without calling them cross-UAV layer execution.
- **Verify:** Study-set coverage and claim-source links.

#### Y-03 — Create publication-ready scientific figures and comparison tables

- **Owner:** `CODEX_WRITING`; deterministic plotting/diagram code preferred and retained.
- **Dependencies:** Y-02.
- **Required work:** Create one architecture figure and one taxonomy figure because they materially clarify the synthesis; create evidence-derived trend figures only when denominators are final. Split the current broad characteristics table into focused views when the venue permits.
- **Output:** Vector figures, source data/code and focused tables.
- **Acceptance:** At least 2 evidence-derived figures; every plotted count matches final ledgers; labels readable in grayscale; no decorative or AI-invented technical content; figure source/code committed.
- **Verify:** Data-to-figure assertions and rendered PDF inspection.

#### Y-04 — Decide reporting-bias, certainty and sensitivity treatment

- **Owner:** `CODEX_WRITING` with methodology evidence from Gemini if needed.
- **Dependencies:** X-04 and Y-01.
- **Required work:** Determine which methods are applicable to heterogeneous systems evidence. Perform justified analyses or explain why no defensible method applies. Do not equate methodological appraisal with certainty.
- **Output:** Methods, Results and limitation statements plus analysis artifacts where applicable.
- **Acceptance:** Each of the three topics has an explicit method/justification and corresponding result/limitation; unsupported low-bias/high-certainty claim = 0; sensitivity analysis follows the frozen protocol or a dated amendment.
- **Verify:** Methods–Results traceability table.

#### Y-05 — Formulate research gaps and future directions without personal-topic leakage

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** Y-01 through Y-04.
- **Required work:** Derive gaps from the evidence and select one central research idea satisfying the assignment. Remove `doctoral-alignment map` from the public Methods. Present ResNet-18, NS-3, ROS 2/PX4/Gazebo only as justified examples, not as predetermined conclusions. Address CNN/YOLO/ViT/LLM/MoE distinctions only to the extent supported by included evidence.
- **Output:** Evidence-linked gap matrix, exactly one central research-idea statement, and future-work text.
- **Acceptance:** Every gap cites supporting study/appraisal evidence; central ideas selected = 1; the idea states problem, evidence gap, proposed approach and measurable outcomes; personal-project rationale statements = 0; unsupported trend claims = 0; tool-specific prescriptions are labelled examples and alternatives stated.
- **Verify:** Claim-source audit and adversarial reviewer pass.

#### Y-06 — Optional unified problem formulation

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** Y-02 and explicit target-journal need.
- **Required work:** Add a common notation/model only if it accurately covers the reviewed decision spaces without erasing incompatible semantics.
- **Output:** Optional equation/notation section.
- **Acceptance:** User/venue approves the addition; every variable maps to taxonomy dimensions; unsupported universality claim = 0. Otherwise record `NOT_APPLICABLE` and do not add equations for appearance.
- **Verify:** Domain review against at least three distinct architecture classes.

### Phase M — manuscript revision

Use the drafting loop Methods → Results → Discussion → Introduction, then update Conclusion, Abstract, Keywords and Title. Codex writes all final prose.

#### M-01 — Rewrite Methods from the final audit trail

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** S through X complete; G-04 frozen.
- **Output:** Reproducible Methods with actual sources/dates, selection, extraction, appraisal and synthesis.
- **Acceptance:** Planned-but-unexecuted searches are not described as executed; every method has a corresponding artifact; records/reports/studies used correctly; AI role and human adjudication accurately disclosed.
- **Verify:** Method-to-artifact traceability matrix, PRISMA items 5–15 and 24.

#### M-02 — Rewrite Results using final counts and synthesis

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** Y-01 through Y-04 and final PRISMA arithmetic.
- **Output:** Final selection, characteristics, appraisal and RQ results.
- **Acceptance:** `working`, `interim`, `awaiting classification`, unknown study count and partial-extraction language removed only when evidence resolves them; every number recalculates from release data; no projected result appears as observed.
- **Verify:** Automated number/citation audit plus claim-source matrix.

#### M-03 — Rewrite Discussion

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** M-02 and Y-05.
- **Output:** Interpretation, comparison, limitations and evidence-bounded future directions.
- **Acceptance:** Every scientific statement has Results/source support; repeated defensive hedging is consolidated; limitations remain accurate; tool/personal-project bias = 0.
- **Verify:** Discussion-to-Results mapping and no-slop editorial pass.

#### M-04 — Rewrite Introduction and contribution statement

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** M-02/M-03.
- **Output:** Funnel-shaped Introduction, gap, RQs and numbered contributions.
- **Acceptance:** Problem, motivation, approach and contribution all explicit; novelty bounded by verified prior reviews; no exhaustive absence claim without exhaustive evidence.
- **Verify:** Prior-review gap matrix and citation audit.

#### M-05 — Finalize Conclusion

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** M-02/M-03.
- **Output:** Evidence-bounded conclusion.
- **Acceptance:** Answers the RQs, states applicable conditions and contribution, introduces no new result/reference, and separates findings from future work.
- **Verify:** Sentence-level Results support audit.

#### M-06 — Finalize Title, Abstract and Keywords

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** M-01 through M-05.
- **Output:** Final front matter.
- **Acceptance:** Title accurately identifies systematic review and scope; Abstract is 150–300 words and reports actual methods/counts/findings/limitations; keywords match title and content; `interim` remains only if Level 1 is not complete.
- **Verify:** Word count and cross-section consistency check.

#### M-07 — Verify and normalize all references

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** X-05 and all prose stable.
- **Output:** Final `references.bib` and bibliography.
- **Acceptance:** cited-key set equals bibliography-key set; undefined/uncited keys = 0; DOI duplicates = 0; all originals opened; venue style consistent. Do not “fix” valid DOI line wrapping. Normalize author capitalization only when identity is preserved.
- **Verify:** BibTeX parser, DOI normalization and LaTeX build.

#### M-08 — Add verified authorship and declarations

- **Owner:** `USER_ACTION` supplies/approves; `CODEX_WRITING` formats.
- **Dependencies:** DEC-03 through DEC-05 human decisions and M-06.
- **Output:** Author block, affiliations, correspondence and declarations.
- **Acceptance:** Nguyễn Minh Hiếu is first or corresponding author; supervisor included with consent; HCMUT/VNU-HCM affiliation first; verified HCMUT email; no guessed funding/conflict/contribution/ORCID.
- **Verify:** Author approval record and exact metadata comparison.

#### M-09 — Apply the one approved official journal template

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** G-03, M-01 through M-08.
- **Output:** Final source tree using the official template.
- **Acceptance:** Official template provenance recorded; template files unmodified unless the publisher permits and change is documented; zero active IEEE/Springer source ambiguity; page/word constraints met or documented.
- **Verify:** Template checksum/provenance and build.

### Phase P — PRISMA and reproducibility package

#### P-01 — Reconcile final PRISMA arithmetic

- **Owner:** `CODEX_WRITING`; code-first automated arithmetic required.
- **Dependencies:** D-02, E-05, E-06.
- **Output:** Record/report/study count ledger.
- **Acceptance:** Every transition equation has difference 0; source-specific identification totals match exports; duplicates, exclusions, unavailable reports and includes use correct units.
- **Verify:** Tested arithmetic script and hand-check of definitions.

#### P-02 — Generate final PRISMA 2020 flow diagram

- **Owner:** `CODEX_WRITING`; deterministic generation preferred.
- **Dependencies:** P-01.
- **Output:** Vector flow diagram and source data/code.
- **Acceptance:** All displayed counts equal P-01; unknown placeholders = 0; diagram uses a recognized PRISMA 2020 structure; excluded full-text reasons reconcile with ledger.
- **Verify:** Data-to-figure assertions and visual inspection.

#### P-03 — Complete the 27-item PRISMA checklist

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** Final manuscript pagination.
- **Output:** Final checklist with item/subitem locators.
- **Acceptance:** Items 1–27 all present; page/section locators resolve; status describes actual reporting, not row existence; internal contradictions = 0.
- **Verify:** Checklist parser/count plus manual locator check.

#### P-04 — Package reproducibility materials

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** P-01/P-03 and final release.
- **Output:** Protocol, amendments, queries, logs, ledgers, extraction, appraisal, claim matrix, figure data/code, README and checksums; no publisher PDFs redistributed.
- **Acceptance:** Manifest accounts for 100% packaged files; checksum verification passes; secrets/private credentials/proprietary PDFs = 0; every generated artifact has provenance.
- **Verify:** Checksum command and manifest audit.

### Phase Q — quality assurance and independent review

#### Q-01 — Scientific integrity audit

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** M and P complete.
- **Output:** Machine-readable audit and PASS/FAIL report.
- **Acceptance:** Fabricated/unsupported claims = 0; unresolved citations = 0; duplicate DOI = 0; placeholders = 0; final counts match release; every quantitative claim has a locator.
- **Verify:** Existing/revised integrity scripts plus manual semantic checks.

#### Q-02 — Build and log audit

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** M-09.
- **Commands:** In the canonical manuscript directory run `tectonic --keep-logs --keep-intermediates main.tex`.
- **Acceptance:** Exit 0; fatal errors = 0; undefined citations/references = 0; overfull boxes = 0; nonfatal warnings classified and justified.
- **Verify:** Build log parser and PDF existence/hash.

#### Q-03 — Visual PDF inspection

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** Q-02.
- **Required work:** Render every page and inspect full pages plus dense tables/figures at higher resolution.
- **Acceptance:** Pages inspected = total pages; clipped, overlapping, unreadable, corrupted-font and broken-reference elements = 0; grayscale figure labels readable.
- **Verify:** Contact sheets/page images and signed visual-review log.

#### Q-04 — Independent academic review

- **Owner:** Read-only reviewer agents; Codex synthesizes and accepts.
- **Dependencies:** Q-01 through Q-03.
- **Required work:** Run differentiated editorial, methodology, domain, perspective and adversarial reviews. Reviewers do not edit the manuscript.
- **Output:** Traceable review reports, editorial synthesis and revision matrix.
- **Acceptance:** Every criticism identifies location, evidence and proposed resolution; false-positive DOI/table claims are rejected; critical findings resolved or manuscript remains not ready; reviewer fabrication = 0.
- **Verify:** Concern-to-evidence matrix and Codex re-review.

#### Q-05 — Final author approval

- **Owner:** `USER_ACTION` and all named authors.
- **Dependencies:** Q-04 resolved, M-08.
- **Output:** Approval of exact source/PDF hash and submission metadata.
- **Acceptance:** Approval from every named author; author order/contributions/declarations confirmed; approved PDF hash recorded; unresolved author objection = 0.
- **Verify:** Private approval record referenced without committing private correspondence.

### Phase U — submission and course evidence

These tasks are blocked until the user gives explicit authorization. They are not part of Level-1 review completion.

#### U-01 — Verify live venue and submission route

- **Owner:** `GEMINI_RESEARCH` verifies public facts; `CODEX_WRITING` accepts.
- **Dependencies:** G-03 and Q-05.
- **Acceptance:** Official venue URL, scope, indexing status, discontinued/predatory checks, article type, template and live portal verified from current official sources; unresolved venue-fit issue = 0.
- **Verify:** Codex source-by-source PASS/FAIL review using official venue, index and publisher pages.

#### U-02 — Prepare submission package

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** U-01.
- **Output:** Approved manuscript source/PDF, supplementary files, checklist, cover letter and metadata sheet.
- **Acceptance:** Package manifest complete; metadata matches M-08/Q-05; placeholder = 0; cover-letter claim supported; submitted-copy candidate builds from included source.
- **Verify:** Package manifest, clean-room build and exact metadata diff.

#### U-03 — Submit through the journal portal

- **Owner:** `USER_ACTION` with Codex assistance only after explicit authorization.
- **Dependencies:** U-02 and verified HCMUT credentials controlled by user.
- **Acceptance:** Exactly one venue submission; system-generated submitted copy downloaded; manuscript ID, submission timestamp and receipt archived; no credential stored in Git; no simultaneous submission.
- **Verify:** Portal receipt and submitted-copy hash are reviewed with the user; credential/secret scan passes.

#### U-04 — Archive submission evidence

- **Owner:** `CODEX_WRITING`.
- **Dependencies:** U-03.
- **Acceptance:** Manifest contains submitted copy, receipt, manuscript ID and safe screenshots; sensitive tokens/cookies/passwords = 0; evidence checksum passes.
- **Verify:** Manifest count, checksum verification and secret scan.

#### U-05 — Send HK261 course evidence

- **Owner:** `USER_ACTION`; Codex prepares text and verifies attachments after explicit authorization.
- **Dependencies:** U-04, verified doctoral student ID and exact exam/deadline information.
- **Acceptance:** Recipient exactly `duyanhnguyen@hcmut.edu.vn`; subject exactly `Bài tập lớn – Tiểu luận lớp PPNCKH HK261`; body includes name, verified student ID and manuscript ID; receipt attached; sent evidence archived safely.
- **Verify:** User confirms the sent message; safe evidence record contains recipient, subject, timestamp and attachment names without credentials or private mailbox exports.

## 11. False-positive review findings that must not become tasks

The following claims from an external AI review were independently checked and are not defects in the current source:

- Ref. 9 DOI is `10.1109/TMC.2025.3628608`, not a truncated value.
- Ref. 17 DOI is `10.1007/s42979-025-04063-5`, not a truncated value.
- Ref. 29 DOI is `10.1109/ICCT67417.2025.11374232`, not a truncated value.
- Ref. 44 uses Latin `MIOT` in `10.1109/MIOT.2025.3575886`; no Greek-character corruption was found.
- Table 1 currently contains `AlexNet; VGG16; YOLO`, a clean S13 objective, `Llama-2 7B/13B/70B`, and a valid C04 citation.
- Table 2 uses explicit dashes for withheld Domain 9; adding a local footnote is an editorial improvement, not recovery of blank data.
- `31th` and uppercase family names originate in deposited metadata; normalize presentation only after checking identity, and never treat them as proof of fabricated references.

## 12. Optional publication-upgrade tasks

These are not PRISMA completion requirements and must not delay Level 1 unless the chosen venue requires them:

- Dual-independent human screening and inter-rater agreement.
- Unified mathematical problem formulation.
- Extra trend visualizations beyond evidence-derived architecture/taxonomy figures.
- Public repository/Zenodo deposit.
- Meta-analysis when no compatible outcomes/variance exist.
- Broadening scope to Transformer/LLM/MoE literature beyond the frozen eligibility criteria.

Any optional task must receive its own approved scope, dependency check and acceptance criteria before implementation.

## 13. Verification commands

Run from repository root unless stated otherwise:

```bash
python3 .codex/hooks/automation_registry.py search "<task keywords>"
python3 .codex/hooks/automation_registry.py validate
python3 .codex/hooks/project_state.py validate
python3 .codex/hooks/project_state.py show
git status --short
git diff --check
```

Manuscript build:

```bash
cd "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/manuscript/sn_computer_science"
tectonic --keep-logs --keep-intermediates main.tex
```

Task-specific scripts/tests must be added to the automation catalog before reuse. A passing script does not replace semantic acceptance by Codex or final scientific responsibility by the authors.

## 14. Boundaries

### Always

- Preserve immutable raw search exports and accepted historical releases.
- Use exact timestamps with timezone and retain task/context IDs.
- Keep source locators for eligibility, extraction, appraisal and synthesis.
- Distinguish record/report/study and simulation/emulation/prototype/physical flight.
- Commit one accepted task before starting another.
- Update state, event and code-first decision in the closing commit.

### Ask first

- Change venue/template or canonical paths.
- Change RQs, eligibility, date range, appraisal domains or synthesis methods.
- Add/remove authors or change author order.
- Make external submissions, emails or public deposits.
- Delete or rewrite user-created artifacts.

### Never

- Invent or infer missing counts, dates, DOI values, results, author consent or receipts.
- Count blocked search pages as searches or zero results.
- Treat raw provider output as accepted evidence.
- Use abstract-only evidence for detailed quantitative synthesis or appraisal.
- Merge study families using shared authors/citations alone.
- Present 46 reports as 46 independent studies without reconciliation.
- Present the current bounded interim release as a completed PRISMA review.
- Submit to more than one venue simultaneously.

## 15. Risks and mitigations

| Risk | Detection | Mitigation |
|---|---|---|
| Institutional database access unavailable | Missing official export/log | User performs manual export; document limitation; do not invent counts |
| Large delta corpus | New-record count after D-02 | Batch only non-overlapping records; freeze IDs; no arbitrary 30–35 cap |
| Conference/journal double counting | Family candidates/extension statements | E-06 evidence-based family reconciliation before final frequencies |
| AI research hallucination | Missing locator/invalid DOI/unsupported number | Mandatory brief schema, deterministic checks and Codex PASS/FAIL review |
| Scope drift toward personal dissertation | Tool-specific future-work language | Y-05 evidence-linked gap matrix and adversarial review |
| Two active templates | Divergent canonical paths | G-03 single venue/template decision and file-map update |
| False-positive reviewer corrections | DOI resolves and source differs from critique | Section 11 exclusion list and source-first verification |
| Dirty workspace or agent collision | Pre-task Git status differs from baseline | Dedicated worktree, explicit paths, no broad staging, commit before next task |
| Deadline pressure | Exam date remains unknown | Ask once; never guess; prioritize Level 1 before optional publication upgrades |

## 16. Progress reporting

At every task close, report:

1. Task ID and actual start/completion timestamps.
2. Commit SHA and integrated branch status.
3. Acceptance criteria table with PASS/FAIL and observed counts.
4. Artifacts created/changed and verification commands.
5. Evidence accepted, rejected and unresolved.
6. Current PRISMA counts using explicit record/report/study units.
7. Next unblocked task and any human decision required.

`MUST_READ_AI_AGENT/current_state.json` is the only current-state source. This specification defines the approved work; it must not become a competing progress tracker. Task checkboxes are not updated here. History belongs in Git, `events.jsonl` and `automation/decision_log.jsonl`.

## 17. Spec approval gate

Implementation must not start until the user either:

- approves `HK261-PRISMA-COMPLETION-SPEC-v1`, or
- requests amendments that Codex records in a superseding spec commit.

Approval of this specification does **not** authorize journal submission, email, public upload, author declarations or protocol changes.
