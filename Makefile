.PHONY: help install test lint format docs clean kernel sync

help:
	@echo "Comandos disponíveis:"
	@echo "  make install    - Instalar dependências"
	@echo "  make test       - Rodar testes"
	@echo "  make lint       - Verificar código (ruff)"
	@echo "  make format     - Formatar código (black + isort)"
	@echo "  make docs       - Gerar documentação"
	@echo "  make kernel     - Configurar kernel Jupyter"
	@echo "  make sync       - Sincronizar notebooks"
	@echo "  make clean      - Limpar arquivos temporários"

install:
	pip install -r requirements.txt
	pip install -e ".[dev,docs]"
	pre-commit install

test:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

lint:
	ruff check src/
	black --check src/ tests/
	isort --check-only src/ tests/

format:
	black src/ tests/
	isort src/ tests/
	ruff check --fix src/

docs:
	cd docs && make html
	@echo "Docs em: docs/_build/html/index.html"

kernel:
	./scripts/setup_kernel.sh

sync:
	./scripts/sync_notebooks.sh

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf docs/_build/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
