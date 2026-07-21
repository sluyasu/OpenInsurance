# openinsurance-wiki - reproducible pipeline
# Usage: make <target> COUNTRY=be [INSURER=axa]
#
# The full chain: discover -> download -> extract -> build -> index -> validate
# Everything is resumable and idempotent. `make all` reproduces the wiki from a clone.

COUNTRY ?= be
PY      ?= python3
PIP     ?= $(PY) -m pip

.PHONY: help setup discover download extract ground ground-strict build index validate all

help:
	@echo "Targets (set COUNTRY=<cc>, optional INSURER=<slug>):"
	@echo "  setup      install deps + playwright chromium"
	@echo "  discover   crawl source listing pages -> PDF URLs into sources/<cc>/*.yml"
	@echo "  download   fetch PDFs -> data/<cc>/pdfs/ (resumable, checksummed)"
	@echo "  extract    PDFs -> rich Markdown + JSON via the committed extraction agent (LLM)"
	@echo "  ground     verify extracted quotes exist in the source text"
	@echo "  ground-strict  same, but exit non-zero on any ungrounded quote"
	@echo "  build      extracted data -> wiki/ pages + MOCs (resume-safe)"
	@echo "  index      regenerate AGENTS.md + data/<cc>/index.json"
	@echo "  validate   frontmatter / wikilinks / orphans / citation gates"
	@echo "  all        download -> extract -> ground-strict -> build -> index -> validate"

setup:
	$(PIP) install -r requirements.txt
	$(PY) -m playwright install chromium

discover:
	$(PY) pipeline/discover.py --country $(COUNTRY) $(if $(INSURER),--insurer $(INSURER),)

download:
	$(PY) pipeline/download.py --country $(COUNTRY) $(if $(INSURER),--insurer $(INSURER),)

extract:
	$(PY) pipeline/extract.py --country $(COUNTRY) $(if $(INSURER),--insurer $(INSURER),)

ground:
	$(PY) pipeline/verify_grounding.py --country $(COUNTRY)

ground-strict:
	$(PY) pipeline/verify_grounding.py --country $(COUNTRY) --strict

build:
	$(PY) pipeline/build_wiki.py --country $(COUNTRY)

index:
	$(PY) pipeline/build_index.py --country $(COUNTRY)

validate:
	$(PY) pipeline/validate.py --country $(COUNTRY)

all: download extract ground-strict build index validate
