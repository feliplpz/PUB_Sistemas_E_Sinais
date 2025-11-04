# Arquivos de Configuração Criados

## Arquivos prontos para usar:

1. **`.pre-commit-config.yaml`** → Raiz do projeto
   - Black, isort, ruff, pydocstyle
   - Roda automaticamente no `git commit`

2. **`pyproject.toml`** → Raiz do projeto
   - Configuração completa: black, isort, ruff, pytest
   - Coverage mínimo 80%
   - Notebooks excluídos do lint

3. **`Makefile`** → Raiz do projeto
   - Comandos úteis: test, lint, format, docs

4. **`requirements.txt`** → Raiz do projeto
   - Todas as dependências (core + dev + docs)

5. **`pre-push`** → Copiar para `.git/hooks/pre-push`
   - Roda testes antes do push
   - Bloqueia se coverage < 80%

6. **`ci.yml`** → `.github/workflows/ci.yml`
   - GitHub Actions CI
   - Testa Python 3.11 e 3.12
   - Gera docs automaticamente

7. **`SETUP.md`** → Instruções de instalação

##  Ordem de instalação:

```bash
# 1. Copiar arquivos para o projeto
# 2. Instalar
pip install -r requirements.txt
pip install -e ".[dev,docs]"

# 3. Ativar hooks
pre-commit install
cp pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push

# 4. Testar
make test
```

## Features:

1. Formatação automática no commit
2. Lint PEP8 apenas em src/
3. Testes obrigatórios no push
4. Coverage mínimo 80%
5. Docstrings obrigatórios em src/
6. CI no GitHub
7. Notebooks ignorados no lint

## Próximos passos:

1. Copie os arquivos
2. Rode `make install`
3. Faça um commit de teste
4. Tente fazer push (vai rodar testes)
5. Profit!
