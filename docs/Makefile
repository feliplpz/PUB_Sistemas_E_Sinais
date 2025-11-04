SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

help:
	@echo "Use 'make html' para gerar HTML"

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html
	@echo "Build completo. HTML em $(BUILDDIR)/html/"

clean:
	rm -rf $(BUILDDIR)/*

.PHONY: help html clean
