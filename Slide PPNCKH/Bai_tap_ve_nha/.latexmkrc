# ---- latexmkrc: Cấu hình biên dịch tối ưu cho LaTeX Workshop & Terminal ----
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$xelatex  = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$pdf_mode = 1; # 1 = pdflatex, 5 = xelatex

$max_repeat = 5;
$bibtex_use = 1;

@generated_exts = qw(aux bbl bcf blg idx ind lof lot out toc acn acr alg fls glg glo gls ist run.xml synctex.gz fdb_latexmk);

$preview_mode = 0;
$preview_continuous_mode = 0;
