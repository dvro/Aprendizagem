
clean:
	@rm *.dvi -R
	@rm *.log -R
	@rm *.bbl -R
	@rm *.blg -R
	@rm *.toc -R
	@rm *.lof -R
	@rm *.lot -R
	@rm *.out -R
	@rm *.aux -R

build:
	@latex aprendizagem

bib:
	@bibtex aprendizagem
	@latex aprendizagem
	@latex aprendizagem

pdf:
	@dvipdfm aprendizagem.dvi

all:
	@make build
	@make bib
	@make pdf
	@make clean

