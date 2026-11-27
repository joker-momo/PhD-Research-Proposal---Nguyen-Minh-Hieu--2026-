## TASK

Independently check the original-source evidence for the disjoint HK261 report subset in the attached targets.json, as a batch of the 887-item advisory source review.

## REQUIRED WORK

1. Before extraction, open original HKF-118.pdf and report its printed title plus an exact contiguous 5–9-word body excerpt from physical page 2 with section. If you cannot open that PDF file itself, report the exact access issue and stop extraction.
2. Read targets.json. Its source-keyed arrays contain kind, check key, suggested physical page and section, plus optional outcome metric hints. For each report, read the attached HKF-numbered text parts in order. They are transcribed from the hash-checked original through Apple PDFKit and marked with original 1-based physical PDF pages. Begin with the suggested locations and follow relevant sections, tables, captions and appendices. A suggested locator is only a lead. For HKF-130, when listed, the source is deliberately withheld. Return UNRESOLVED with an access-gap reason for each of its listed keys.
3. Technical keys cover topology and decision roles; workload/model/data/baselines; partition and assignments; decision, objective, constraints and solver; platform and evaluation modality; network/mobility/event response. Supply what the original establishes and state missing subfields.
4. For each outcome, identify observed metric, exact printed literal, original units, evaluated method and comparator where stated, and conditions/denominator. Preserve approximate notation. Configuration values, unlabeled curves, workload parameters, and remote citations cannot establish observed outcomes. For coverage read the supplied results and classify VERIFIED_EXACT, PLOT_ONLY, or PRINTED_UNRESOLVED. State checked locations and why.
5. For appraisal use D01 question/system model; D02 constraints/assumptions; D03 reconstructable configuration; D04 comparators/conditions; D05 metric and objective alignment; D06 repetitions, variability or sensitivity; D07 network/mobility realism; D08 conclusions vs evaluation scope; D09 relevant author artifacts; D10 limitations/declarations. First state YES (affirmative), PARTIAL (incomplete), NO (observed contrary/inadequate), NOT_REPORTED (checked relevant accessible sections), or NOT_APPLICABLE (justify). Then state the evidence and rationale. Third-party references do not prove author artifact availability. A paper's technical setting does not automatically validate later conclusions.
6. Use the parent Task alone unless non-overlapping internal workers are supported and actually available. In that case report exact worker assignments. Where a figure/table or formula cannot be read reliably in source text, report UNRESOLVED and the relevant page or caption. Never guess values from plotted positions.

## REQUIRED OUTPUT

First output `PREFLIGHT` and one object with `file`, `title`, `page`, `section`, and `quote`. Then output JSONL, one entry for every target. Use exactly the supplied ID, kind and key. Use this schema:

```json
{"id":"HKF-118","kind":"appraisal","key":"D01","status":"VERIFIED","finding":"YES: ...","evidence":[{"page":2,"section":"...","quote":"exact contiguous same-line text"}],"note":""}
```

Use status VERIFIED, PARTIAL, UNRESOLVED, or NOT_REPORTED. Use exact short anchors on the physical source page, preserving words and punctuation. Include more than one anchor when a claim or coverage needs it. Table numbers may be sourced with a same-row printed cell sequence only if the supplied layout makes its meaning clear. For absence, include checked sections and what could not be found. An inaccessible original may use an empty evidence array with an explicit reason. For reports read, list scholarly identity once per report (title, authors, year, venue, DOI or DOI_NOT_FOUND, with UNKNOWN where absent), outside the JSONL. Finish with returned key count, unresolved keys, normalized duplicate count or relationships, worker statement, and END_HK261_SOURCE_BATCH.

## ACCEPTANCE CRITERIA

- Original-PDF preflight with 1 exact page-2 anchor. Unique requested-key coverage must match targets.json, or enumerate each inaccessible or missing key. Unexpected and duplicate keys must equal zero.
- All assessed findings carry source page, section/table/figure, and at least 1 short original anchor; supported numerical findings carry original value, unit, metric and conditions or explicit unavailable fields. Unsupported quantitative claims and fabricated matches equal zero.
- Every report accessed has an identity line or explicit unknown bibliographic fields and no undetected duplicate DOI/title. Every unresolved item is enumerated. No decisions written into R1/R2. Every assertion considered for adoption is independently checked by Codex against the original PDF.

## BOUNDARIES

Read only the authorized attachments, using native PDF reading and the provided PDFKit page text. Do not upload to external tools, write files, open web sources, access other folders, infer human approval, or amend HK261 records. Do not extract operational military, combat, targeting or weapon details, scenarios or effect metrics. Restrict any dual-use report to non-operational bibliographic and scholarly assessment. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
