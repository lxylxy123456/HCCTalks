SOURCES = $(wildcard *Talk*.tex)

TARGETS_43 = $(SOURCES:%.tex=$(TMP)/43/%.pdf)

TARGETS_169 = $(SOURCES:%.tex=$(TMP)/169/%.pdf)

HTML_SOURCES = $(wildcard *Talk*.html)

HTML_TARGETS_43 = $(HTML_SOURCES:%.html=$(TMP)/43/%.html)

HTML_TARGETS_169 = $(HTML_SOURCES:%.html=$(TMP)/169/%.html)

TMP = /tmp

all:

ALL: $(TARGETS_43) $(TARGETS_169) $(HTML_TARGETS_43) $(HTML_TARGETS_169)

$(TARGETS_43): $(TMP)/43/%.pdf : %.tex LatexConfig.tex
	mkdir -p $(TMP)/43/
	pdflatex -shell-escape -output-directory $(TMP)/43 $^

$(TARGETS_169): $(TMP)/169/%.pdf : %.tex LatexConfig.tex
	mkdir -p $(TMP)/169/
	pdflatex -shell-escape -output-directory $(TMP)/169 \
		"\def\aspectratio{169}\input" $^

$(HTML_TARGETS_43): $(TMP)/43/%.html : %.html
	mkdir -p $(TMP)/43/
	cp $^ $@

$(HTML_TARGETS_169): $(TMP)/169/%.html : %.html
	mkdir -p $(TMP)/169/
	cp $^ $@

clean_tmp: 
	rm -f \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.aux) \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.log) \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.nav) \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.out) \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.snm) \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.toc) \
		$(TARGETS_43:$(TMP)/43/%.pdf=$(TMP)/43/%.vrb)
	rm -f \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.aux) \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.log) \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.nav) \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.out) \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.snm) \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.toc) \
		$(TARGETS_169:$(TMP)/169/%.pdf=$(TMP)/169/%.vrb)
	rm -rf /tmp/TalkSvg/

clean_pdf:
	rm -f $(TARGETS_43) $(TARGETS_169) $(HTML_TARGETS_43) $(HTML_TARGETS_169)

clean: clean_tmp clean_pdf
	rm -df $(TMP)/43
	rm -df $(TMP)/169

