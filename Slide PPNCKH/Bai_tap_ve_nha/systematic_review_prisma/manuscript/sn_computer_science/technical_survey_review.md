# Technical survey comparison review

This review applies to the alternative manuscript based on `7a6675d`. The
comparison PDF retains the accepted PRISMA census and uses the Springer Nature
class with a 216 mm text block and compact bibliography spacing. It is an
HK261 coursework comparison draft.

## 27 November 2026 claim audit

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Prose and source coverage | PASS | S4 links 146 entries across 90 prose lines. The checker compares audited line identities with the LaTeX source. Figures, tables, headings that introduce coded groups, and equations use the S4 item crosswalk. |
| Table 2 and 3 source map | PASS | All 46 studies have an original PDF and checksum, accepted extraction file, grouped locators with status, and D09 judgment and rationale. Original-file hashes match for 46 included and three pending PDFs. |
| Nine quantitative contrasts | PASS | Rechecked the report tables and interpretation boundaries. Original page renders reviewed for R0014 pp. 12–13, R0074 p. 16, R0075 p. 10 and R0125 p. 3. Text-layer checks used pypdf 6.21.4 or PDFium via pypdfium2 5.13.0. Render R0014 physical p. 12, Table III for the 20- and four-node values and read p. 11 for the metric definition. Rescheduling latency on p. 13, Table IV uses a different boundary. |
| Revised PDF layout | PASS | 28 pages rendered. Matched all 13 S4 item pages with the final LaTeX auxiliary labels. No unresolved citation or cross-reference warnings and no overfull boxes. |
| Evidence gaps | OPEN | The claim map marks 13 OPEN entries and 16 NARROWED entries. Pending eligibility, incomplete recovery conditions, and undocumented human verification and author declarations are identified explicitly. Whole-corpus row locators come from the accepted extraction and appraisal, with targeted direct checks for claims at risk of overstatement. |

## Initial comparison checkpoint

The table below describes the earlier 29-page comparison build and its source checks.

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Structure and length | PASS | Seven numbered sections, five numbered figures and five numbered tables in a 29-page A4 PDF. |
| PRISMA arithmetic | PASS | 693 identified, 228 duplicates, 465 screened, 328 excluded at title/abstract, 137 sought, 136 assessed, 87 full-text exclusions, three awaiting classification, one unretrieved and 46 included studies. Numbers agree with the accepted reconciliation. |
| Study-level coverage | PASS | The generator checks that the distinct 46 included study representatives are cited exactly once in each of Tables 2 and 3 and all are cited in analytical prose in sections 4–5. The primary coding ledger assigns one category per study in each counted dimension. |
| Comparative outcomes | PASS | Nine comparisons across seven studies. Checked the accepted ledger and the originals at R0080 p. 5 Table I, R0092 p. 13 Table V, R0075 p. 10 Table III, R0074 p. 16 Sect. 4.2, R0014 p. 12 Table III, R0062 p. 6 unavailability test, and R0125 p. 3 Table I and Sect. IV.B. The R0014 table was checked in the original-page render. Values retain reported uncertainty types and settings where available. |
| Appraisal | PASS | Ten domains, each with denominator 46. Figures and summary counts use the accepted appraisal summary. |
| References and compilation | PASS | 54 compiled references, 53 distinct DOI links, 53/53 recorded DOI works returned an exact DOI match and HTTP 200 from Crossref. R0113 retains a verified publisher record and an unresolved DOI. Four `1--1` page fields were removed and non-ASCII bibliography characters were converted to LaTeX accents. No missing citations or references, no overfull boxes. The included PRISMA graphic renders with the same PDF version warning as the baseline. |
| PDF inspection | PASS | Rendered all 29 pages. Inspected the full pagination, multi-page table continuations, figure labels, equations and bibliography links. |
| Final adjudication and independent human verification | OPEN | This PDF uses the 46 reconciled study IDs and preserves three reports as awaiting classification. No author adjudication or independent human agreement statistic is documented. |

## Eligibility boundaries checked for this draft

- R0081. Physical pp. 1–2 describe a working prototype and the official ACM
  list identifies it as a demo. The accepted record still lacks evidence to
  close E7 for the assessed report. Keep the report pending.
  [ACM MobiSys accepted demos](https://www.sigmobile.org/mobisys/2022/accepted-demos.html)
- R0082. The retained six-page deposit and arXiv record have the corresponding
  title and byline. The arXiv record gives a related WCNC DOI and flags text
  overlap with another preprint. The metadata links the deposit to the
  proceedings record. The exact assessed version and scope of overlap remain
  unresolved for inclusion. Keep the report pending.
  [Original arXiv record](https://arxiv.org/abs/2305.15858v1)
- R0132. Physical p. 10, Sect. 8.1–8.2 describes evaluated scenarios and
  performance metrics. The checked evidence has not established that the
  evaluated UAVs collaborate on the neural inference workload under E2/E3.
  Keep the report pending.
- Baseline references [14], [45], [46] and [47] map to R0292, R0113, R0145 and
  R0223 respectively. R0292 supplies tracking-state handoff and
  hardware-in-the-loop evidence, R0113 reports cooperative spiking inference
  alongside continual learning, R0145 evaluates coordinated language-model
  inference roles inside a wider planning application, and R0223 evaluates
  task and feedback orchestration with a shared language model. The technical
  tables distinguish each from neural-layer partitioning. For R0292 the
  bibliography follows the registered title; the retained assessment copy
  displays an alternative title with the matching byline. R0113's missing DOI
  is recorded independently of its evaluation evidence.
- Supplemental studies are represented through the accepted extraction and
  appraisal locks, with test boundaries carried into Table 3. No new
  eligibility criterion based on venue prestige was applied.

The seven contextual reviews in Table 1 sit outside the primary corpus.
Their DOI identities were confirmed. The table records unverified search
windows as NR and limits the gap claim to the sampled surveys.
