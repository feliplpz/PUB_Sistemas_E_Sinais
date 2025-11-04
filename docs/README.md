# Setup da Documentação

## Estrutura criada:

```
docs/
├── conf.py          # Configuração Sphinx
├── index.rst        # Página principal
├── api.rst          # API reference
├── Makefile         # Build commands
├── _static/         # Arquivos estáticos (vazio)
└── _templates/      # Templates customizados (vazio)
```

## Como usar:

```bash
# 1. Copie a pasta docs/ para seu projeto
cp -r docs/ /seu/projeto/

# 2. Gere a documentação
make docs

# 3. Abra no navegador
open docs/_build/html/index.html
```

## O que a documentação mostra:

- API automática do módulo `lotka_volterra`
- Todas as funções com seus docstrings
- Parâmetros e retornos formatados
- Tema Read the Docs

## Para expandir:

Adicione mais páginas em `docs/`:

```rst
# docs/tutorial.rst
Tutorial
========

Seu conteúdo aqui...
```

E adicione no `index.rst`:

```rst
.. toctree::
   :maxdepth: 2

   api
   tutorial
```
