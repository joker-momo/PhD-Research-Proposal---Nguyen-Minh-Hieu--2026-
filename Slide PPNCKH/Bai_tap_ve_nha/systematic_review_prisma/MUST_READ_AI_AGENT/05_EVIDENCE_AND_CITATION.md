# Evidence and Citation Policy

## Evidence hierarchy

Use evidence in this order:

1. Readable original full-text report with stable locator.
2. Publisher or DOI-deposited bibliographic metadata for identity checks.
3. Accepted structured extraction/appraisal reviewed by Codex.
4. Abstract-only metadata, clearly labelled and used only for bounded screening
   or identity statements.
5. Discovery snippets or raw AI/provider output, quarantined until verified.

Source prestige does not replace source verification.

## Units of accounting

- **Record:** database/export entry before deduplication.
- **Report:** one retrievable paper/preprint/document.
- **Study:** underlying investigation; multiple reports may belong to one study.

Never mix these units in PRISMA arithmetic. Link versions and related reports in
`../study_report_map.csv` rather than silently deleting them.

## Eligibility and date boundary

- Eligible publication dates are 2021-01-01 through the documented final search
  date.
- Primary peer-reviewed journal/conference studies are preferred. A preprint may
  contribute unique recent evidence only when explicitly labelled
  non-peer-reviewed.
- Reviews are secondary evidence for gap positioning and citation chaining, not
  included primary studies.
- Federated/distributed training without inference, generic indivisible
  offloading, single-UAV perception without collaboration, and communication-only
  UAV papers are outside scope under the protocol.

## Claim gate

Before a claim enters synthesis or manuscript, record:

- report/study ID;
- page, section, table, figure, equation, or supplied-text locator;
- exact evaluated conditions and units;
- whether evidence is simulation, emulation, analytical, component prototype,
  or physical flight;
- relevant quality/uncertainty limitation;
- status: accepted, unreviewed, rejected, or uncertain.

If any required element is missing, narrow the claim or leave it unresolved.

## Citation gate

- Verify title, authors, year, venue, DOI, and version identity.
- Open the cited original source. Do not cite from memory or copy a reference
  through a secondary paper without checking the original.
- Keep `references.bib` limited to sources actually cited in the manuscript.
- Do not use a DOI link as proof that the exact local PDF is the publisher
  version. Record author-copy/preprint/version uncertainty explicitly.

## Quantitative synthesis

- Do not pool heterogeneous definitions of latency, energy, communication,
  accuracy, reliability, or scalability.
- Meta-analysis requires a sufficiently homogeneous subset with compatible
  outcomes and variance information; otherwise use narrative synthesis and an
  evidence map.
- Preserve denominators and overlapping categories. Never sum overlapping
  modality or mechanism counts as if they were mutually exclusive.
