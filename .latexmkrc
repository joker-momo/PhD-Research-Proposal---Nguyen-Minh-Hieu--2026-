# ---- latexmkrc: optimized for fast incremental builds ----

# Use pdflatex with shell-escape (required for tikz externalize)
$pdflatex = 'pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$pdf_mode = 1;

# Only rerun when truly necessary
$max_repeat = 5;

# Use bibtex for bibliography
$bibtex_use = 1;

# Extensions to clean with: latexmk -c
@generated_exts = qw(aux bbl bcf blg idx ind lof lot out toc acn acr alg fls glg glo gls ist run.xml synctex.gz fdb_latexmk);

# Don't auto-open PDF
$preview_mode = 0;
$preview_continuous_mode = 0;
