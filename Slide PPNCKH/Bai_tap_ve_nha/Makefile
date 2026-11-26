# Makefile for LaTeX Homework

MAIN = main

all: pdf

pdf:
	latexmk -pdf -synctex=1 -interaction=nonstopmode $(MAIN).tex

xe:
	latexmk -xelatex -synctex=1 -interaction=nonstopmode $(MAIN).tex

clean:
	latexmk -c
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.synctex.gz *.fdb_latexmk *.fls

distclean: clean
	rm -f $(MAIN).pdf

.PHONY: all pdf xe clean distclean
