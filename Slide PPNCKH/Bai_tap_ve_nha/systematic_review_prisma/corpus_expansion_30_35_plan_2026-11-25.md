# Corpus Re-Audit and Expansion Plan — 30–35 Included Studies

**Status:** Active from 25 November 2026  
**Owner:** Codex for decisions, verification, project files, and manuscript writing; Gemini A2A for research notes and structured evidence only.  
**Final target:** 30–35 unique, full-text, protocol-eligible primary studies published from 1 January 2021 through the final search date.

**Target journal:** SN Computer Science (Springer Nature), selected by the user on 25 November 2026. Candidate discovery searches this journal first, but journal identity does not override eligibility.

## Protocol boundary

“Does not meet requirements” means that a report fails at least one fixed eligibility criterion or meets an exclusion criterion. The protocol does not permit exclusion solely because a paper receives a low aggregate methodological-quality score. Quality weaknesses will remain in the appraisal and will bound the synthesis. Any later decision to impose a quality threshold requires a dated protocol amendment before the new threshold is applied.

## Work packages

| Package | Responsible agent | Input | Quantified output | Completion gate | Status |
|---|---|---|---|---|---|
| A. Re-audit current corpus | Gemini research; Codex review | 20 priority records and all 20 current PDFs; protocol and amendments | Exactly 20 decisions, each with 14 criterion checks and at least two full-text locators; detailed extraction for S13/S19/S20 | All mandatory A2A criteria PASS; no duplicate DOI/title; counts sum to 20 | Previous task failed after service interruption; revised brief prepared at `corpus_expansion/reaudit_20_fulltext_brief.md`, queued after active correction |
| B. Discover new candidates | Gemini research; Codex review | SN Computer Science-first search, eight final queries, and current 20 DOI/title records | 25 candidates or documented shortfall; quantified SNCS screening log; all uncertainties explicit | All mandatory A2A criteria PASS; every claim sourced; no unsupported dates or numeric claims | 25-record return archived; initial gate FAIL; correction active as `01a21164-a8d1-7cae-832f-6af7d32dd360` |
| C. Metadata verification | Codex | Accepted Package B output | Crossref/publisher verification for 100% of candidates; zero missing title/authors/year/venue/DOI markers | Binary field and duplicate audit passes | Pending B |
| D. Full-text intake | User retrieves PDFs from DOI/library links; Codex verifies | Accepted candidates lacking accessible full text | Identity/readability check for every received PDF | Title/DOI match and full report confirmed | Pending B |
| E. Eligibility screening | Codex | Verified candidate PDFs | One decision and, for exclusions, one primary reason per report | No abstract-only report marked included | Pending D |
| F. Extraction and appraisal | Codex, with Gemini research notes subject to review gate | All newly included full reports | Complete extraction row plus 10-domain appraisal for every included study | Required fields complete or `not reported`; evidence locators present | Pending E |
| G. Corpus reconciliation | Codex | Re-audited old studies plus new included studies | Final included count of 30–35; zero duplicate studies/reports | PRISMA arithmetic passes and all counts agree | Pending F |
| H. Manuscript revision | Codex only | Accepted reconciled evidence | Updated Methods, Results, Discussion, Introduction, structured Abstract, tables, flow diagram, bibliography, checklist, PDF, editable source and supplement in the official Springer Nature format for SN Computer Science | Build/citation/integrity/visual audits pass | Pending G |

## Decision rules

1. A report enters the final 30–35 only after readable full text is available and all eligibility criteria pass.
2. Abstract-only records remain candidates and do not contribute results, quality judgments, or manuscript claims.
3. Duplicate conference/journal or preprint/published versions are linked as reports of one study; the most complete peer-reviewed report supplies evidence.
4. Reviews and surveys support citation chaining and context only; they do not count toward the 30–35 primary studies.
5. If fewer than 30 studies remain after full-text screening, repeat Package B with a new non-overlapping batch of 15 candidates.
6. If more than 35 studies pass, retain the complete eligible set in the systematic review rather than selectively removing valid studies to hit an arbitrary maximum; report the actual reconciled count.

## Current arithmetic

- Existing priority records: 20.
- Current PDF intake: 20, including newly recognized S13/S19/S20; three identity/page-count checks passed. Full re-audit remains pending.
- Current included studies before re-audit: 16.
- Current exclusion: 1 short demonstration report.
- Existing reports pending new eligibility/extraction: S13/S19/S20; no longer missing PDFs.
- Additional included studies needed to reach 30–35 from the current 16: 14–19.
- New discovery pool requested from Gemini: 25, allowing documented attrition during metadata and full-text screening.
