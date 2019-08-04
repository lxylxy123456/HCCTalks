SOURCES = $(wildcard *Talk*.tex) \

TARGETS = $(SOURCES:%.tex=/tmp/%.pdf)

all:

ALL: $(TARGETS)

$(TARGETS): /tmp/%.pdf : %.tex LatexConfig.tex
	pdflatex -shell-escape -output-directory /tmp $^

clean_tmp: 
	rm -f \
		$(TARGETS:/tmp/%.pdf=/tmp/%.aux) \
		$(TARGETS:/tmp/%.pdf=/tmp/%.log) \
		$(TARGETS:/tmp/%.pdf=/tmp/%.nav) \
		$(TARGETS:/tmp/%.pdf=/tmp/%.out) \
		$(TARGETS:/tmp/%.pdf=/tmp/%.snm) \
		$(TARGETS:/tmp/%.pdf=/tmp/%.toc) \
		$(TARGETS:/tmp/%.pdf=/tmp/%.vrb)
	rm -rf /tmp/TalkSvg/

clean_pdf:
	rm -f $(TARGETS)

clean: clean_tmp clean_pdf

