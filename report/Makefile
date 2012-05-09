
clean:
	@rm *.dvi -R
	@rm *.log -R
	@rm *.bbl -R
	@rm *.blg -R
	@rm *.toc -R
	@rm *.lof -R
	@rm *.lot -R

build:
	@latex aprendizagem

bib:
	@bibtex aprendizagem
	@latex aprendizagem
	@latex aprendizagem

pdf:
	@rm *.pdf
	@dvipdfm aprendizagem.dvi

all:
	@make clean
	@make build
	@make bib
	@make pdf

