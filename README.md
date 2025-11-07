# Sistemas e Sinais - USP

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-80%25+-success.svg)](htmlcov/)

Simulações interativas para o aprendizado de Sistemas e Sinais.

---

## Instalação Rápida

### Método 1: Instalação Automática (Recomendado)

**Linux / macOS:**
```bash
git clone https://github.com/feliplpz/PUB_Sistemas_E_Sinais.git
cd PUB_Sistemas_E_Sinais
chmod +x setup.sh
./setup.sh
source venv/bin/activate
```

**Windows:**
```cmd
git clone https://github.com/feliplpz/PUB_Sistemas_E_Sinais.git
cd PUB_Sistemas_E_Sinais
setup.cmd
venv\Scripts\activate
```

### Método 2: Instalação Manual

Veja [INSTALL.md](INSTALL.md) para instruções detalhadas.

---

## Para Alunos - Notebooks Interativos

Clique nos links abaixo para abrir direto no Google Colab:

| # | Tópico | Colab | Descrição |
|---|--------|-------|-----------|
| 01 | Modelo Predador-Presa | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/feliplpz/PUB_Sistemas_E_Sinais/blob/main/notebooks/predador_presa.ipynb) | Sistema de Lotka-Volterra |

### Uso Local

```bash
# Ative o ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Inicie Jupyter
jupyter notebook

# Ou use JupyterLab
jupyter lab
```

---

## Estrutura do Projeto

```
PUB_Sistemas_E_Sinais/
├── src/                      # Código-fonte
│   ├── __init__.py
│   └── lotka_volterra.py
├── tests/                    # Testes
│   ├── __init__.py
│   ├── conftest.py
│   └── test_predador_presa.py
├── notebooks/                # Notebooks Jupyter
│   └── predador_presa.py
├── scripts/                  # Scripts auxiliares
│   ├── setup_kernel.sh
│   ├── setup.sh
│   ├── setup.cmd
│   ├── sync_notebooks.sh
│   ├── sync_notebooks.cmd
│   ├── run_tests.sh
│   └── verify_system.py
├── docs/                     # Documentação Sphinx
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
├── .github/                  # CI/CD
│   └── workflows/
│       └── ci.yml
├── requirements.txt          # Dependências
├── pyproject.toml           # Configuração do projeto
├── Makefile                 # Comandos úteis
├── .pre-commit-config.yaml  # Pre-commit hooks
├── pre-push                 # Pre-push hook
└── README.md                # Documentação principal
```

---

## 🛠Comandos Úteis

### Via Makefile

```bash
make help      # Ver todos os comandos disponíveis
make install   # Instalar dependências
make test      # Executar testes com cobertura
make lint      # Verificar qualidade do código
make format    # Formatar código (black + isort)
make docs      # Gerar documentação
make clean     # Limpar arquivos temporários
make sync      # Sincronizar notebooks (.py ↔ .ipynb)
make kernel    # Configurar kernel Jupyter
```

### Comandos Diretos

```bash
# Testes
pytest tests/ -v                           # Todos os testes
pytest tests/ -v --cov=src                 # Com cobertura
pytest tests/ -k test_equilibrio           # Teste específico

# Formatação
black src/ tests/                          # Formatar código
isort src/ tests/                          # Organizar imports
ruff check src/                            # Linting

# Notebooks
jupytext --sync notebooks/*.py             # Sincronizar notebooks
jupyter notebook                           # Iniciar Jupyter

# Documentação
cd docs && make html                       # Gerar docs HTML
```

---

## Executar Testes

```bash
# Método 1: Via Makefile
make test

# Método 2: Via pytest
pytest tests/ -v

# Método 3: Via script
./scripts/run_tests.sh

# Ver relatório de cobertura
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

---

## 🔍 Verificação do Sistema

Execute a verificação completa para garantir que tudo está configurado:

```bash
python scripts/test_system.py
```

Este script verifica:
- ✅ Versão do Python
- ✅ Estrutura de diretórios
- ✅ Arquivos de configuração
- ✅ Código-fonte e testes
- ✅ Dependências instaladas
- ✅ Ferramentas de qualidade
- ✅ Escalabilidade do projeto

---

## Workflow de Desenvolvimento

### 1. Criar/Editar Notebooks

```bash
# Edite o arquivo .py no seu IDE favorito
# notebooks/predador_presa.py

# Gere o .ipynb
make sync
# ou
jupytext --sync notebooks/predador_presa.py

# Teste no Jupyter
jupyter notebook
```

### 2. Antes de Commitar

```bash
# Formatar código (automático com pre-commit)
make format

# Verificar qualidade
make lint

# Executar testes
make test

# Commit
git add .
git commit -m "Add: nova feature"
```

### 3. Antes de Push

```bash
# Testes são executados automaticamente
git push
# Se testes falharem, push é bloqueado
```

---

## Recursos do Projeto

### Qualidade de Código

- **Black**: Formatação automática de código
- **isort**: Organização de imports
- **Ruff**: Linting rápido (substitui flake8, pylint)
- **pydocstyle**: Verificação de docstrings (NumPy style)
- **Pre-commit hooks**: Verificação automática antes de commit
- **Pre-push hooks**: Testes obrigatórios antes de push

### Testes

- **pytest**: Framework de testes
- **pytest-cov**: Cobertura de código (mínimo 80%)
- **Testes abrangentes**: 100+ testes cobrindo todos os casos

### Documentação

- **Sphinx**: Geração de documentação
- **NumPy docstrings**: Documentação padronizada
- **Read the Docs theme**: Interface moderna
- **Auto-documentação**: Docs geradas automaticamente do código

### CI/CD

- **GitHub Actions**: Testes automáticos em PRs
- **Multi-versão**: Python 3.11 e 3.12
- **Coverage reports**: Integração com Codecov

### Notebooks

- **Jupytext**: Sincronização .py ↔ .ipynb
- **Versionamento**: Notebooks em formato .py (Git-friendly)
- **Google Colab**: Links diretos para execução online

---

## Dependências

### Principais

- **NumPy** >= 1.24.0 - Computação numérica
- **Matplotlib** >= 3.7.0 - Visualizações
- **SciPy** >= 1.10.0 - Métodos científicos
- **Jupyter** >= 1.0.0 - Notebooks interativos

### Desenvolvimento

- **pytest** >= 7.4.0 - Testes
- **black** >= 23.0.0 - Formatação
- **ruff** >= 0.3.0 - Linting
- **pre-commit** >= 3.5.0 - Git hooks

### Documentação

- **Sphinx** >= 7.2.0 - Geração de docs
- **sphinx-rtd-theme** >= 2.0.0 - Tema
- **numpydoc** >= 1.6.0 - NumPy docstrings

---

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add: minha feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Convenções

- **Commits**: Use mensagens descritivas (Add/Fix/Update/Remove)
- **Código**: Siga PEP8 (verificado por ruff)
- **Docstrings**: Use formato NumPy
- **Testes**: Mantenha cobertura mínima de 80%

---

## Documentação Adicional

- [INSTALL.md](INSTALL.md) - Guia de instalação detalhado
- [SETUP.md](SETUP.md) - Setup rápido para desenvolvedores
- [INDEX.md](INDEX.md) - Índice de arquivos de configuração
- [docs/README.md](docs/README.md) - Como gerar documentação

---

## Solução de Problemas

### Python não encontrado

```bash
# Linux/Ubuntu
sudo apt install python3.11 python3.11-venv

# macOS
brew install python@3.11

# Windows
# Baixe de python.org e marque "Add to PATH"
```

### Testes falhando

```bash
# Limpar cache
make clean

# Reinstalar dependências
pip install -r requirements.txt --force-reinstall

# Executar testes
make test
```

### Mais ajuda

- Execute: `python scripts/verify_system.py`
- Consulte: [INSTALL.md](INSTALL.md)
- Contato: felipe_lopez@usp.br

---

## Contato

**Felipe Lopez**
Email: felipe_lopez@usp.br
Instituição: Universidade de São Paulo (USP)

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## Agradecimentos

- Universidade de São Paulo (USP)
- Comunidade Python científico
- Contribuidores do projeto

---

## Status do Projeto

- ✅ **Versão:** 0.1.0
- ✅ **Status:** Ativo
- ✅ **Python:** 3.11+
- ✅ **Testes:** Passing
- ✅ **Cobertura:** 80%+
- ✅ **Docs:** Atualizadas

---

**Última atualização:** Novembro 2025
