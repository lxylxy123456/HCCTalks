SOURCES = $(wildcard *Talk*.tex)

TARGETS = $(SOURCES:%.tex=$(TMP)/%.pdf)

HTML_SOURCES = $(wildcard *Talk*.html)

HTML_TARGETS = $(HTML_SOURCES:%.html=$(TMP)/%.html)

TMP = /tmp

all:

ALL: $(TARGETS) $(HTML_TARGETS)

$(TARGETS): $(TMP)/%.pdf : %.tex LatexConfig.tex
	mkdir -p $(TMP)
	pdflatex -shell-escape -output-directory $(TMP) $^

$(HTML_TARGETS): $(TMP)/%.html : %.html
	mkdir -p $(TMP)
	cp $^ $@

clean_tmp: 
	rm -f \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.aux) \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.log) \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.nav) \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.out) \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.snm) \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.toc) \
		$(TARGETS:$(TMP)/%.pdf=$(TMP)/%.vrb)
	rm -rf /tmp/TalkSvg/

clean_pdf:
	rm -f $(TARGETS) $(HTML_TARGETS)

clean: clean_tmp clean_pdf

