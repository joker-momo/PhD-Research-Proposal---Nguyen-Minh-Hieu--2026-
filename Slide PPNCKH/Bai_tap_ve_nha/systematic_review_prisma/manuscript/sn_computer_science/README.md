# Canonical SN Computer Science LaTeX source

User policy:always LaTeX compiled to PDF. main.tex and references.bib are canonical;Word is historical.

The source uses the official sn-jnl class with sn-vancouver-num bibliography. Current working corpus:24 included among27 assessed;34 cited references;17pages. Domain9 aggregate is withheld pending consistent reassessment. Author metadata/declarations are provisional;this is not a submission-approved manuscript.

Build with Tectonic:tectonic --keep-logs --keep-intermediates main.tex.
Native alternative:pdflatex main.tex,bibtex main,pdflatex main.tex,pdflatex main.tex. A complete TeX Live installation needs the standard packages used by the official class,including sttools(cuted),appendix,booktabs,threeparttable and wrapfig. The isolated TeX Live2025 user-tree compatibility check is recorded with the dataset.

Checks cover resolved citations,counts,build warnings and rendered pages. They do not establish final PRISMA completeness or author consent. Dated releases preserve their source hashes;older23-study releases remain historical.
