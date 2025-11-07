# Guia de Instalação Completo

## Instalação Automática (Recomendado)

### Linux / macOS

```bash
# 1. Clone o repositório
git clone https://github.com/feliplpz/PUB_Sistemas_E_Sinais.git
cd PUB_Sistemas_E_Sinais

# 2. Torne o script executável
chmod +x setup.sh

# 3. Execute o script de instalação
.scripts/setup.sh

# 4. Ative o ambiente virtual
source venv/bin/activate
```

### Windows

```cmd
REM 1. Clone o repositório
git clone https://github.com/feliplpz/PUB_Sistemas_E_Sinais.git
cd PUB_Sistemas_E_Sinais

REM 2. Execute o script de instalação
scripts\setup.cmd

REM 3. Ative o ambiente virtual
venv\Scripts\activate
```

---

## Instalação Manual

Se preferir instalar manualmente ou o script automático falhar:

### 1. Pré-requisitos

- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **pip** (geralmente vem com Python)

#### Verificar instalação:

```bash
python --version  # ou python3 --version
pip --version     # ou pip3 --version
git --version
```

### 2. Clonar Repositório

```bash
git clone https://github.com/feliplpz/PUB_Sistemas_E_Sinais.git
cd PUB_Sistemas_E_Sinais
```

### 3. Criar Ambiente Virtual

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 4. Atualizar pip

```bash
pip install --upgrade pip
```

### 5. Instalar Dependências

```bash
# Dependências principais
pip install -r requirements.txt

# Pacote em modo desenvolvimento (com ferramentas de dev)
pip install -e ".[dev,docs]"
```

### 6. Configurar Pre-commit Hooks (Opcional)

```bash
pre-commit install
```

### 7. Configurar Pre-push Hook (Opcional)

**Linux/macOS:**
```bash
cp pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

**Windows:**
```cmd
copy pre-push .git\hooks\pre-push
```

### 8. Configurar Kernel Jupyter

```bash
python -m ipykernel install --user --name=sistemas-sinais --display-name "Python (Sistemas e Sinais)"
```

### 9. Sincronizar Notebooks

**Linux/macOS:**
```bash
chmod +x scripts/sync_notebooks.sh
./scripts/sync_notebooks.sh
```

**Windows:**
```cmd
scripts\sync_notebooks.cmd
```

### 10. Verificar Instalação

```bash
python scripts/test_system.py
```

---

## Verificação Pós-Instalação

### Executar Testes

```bash
# Todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ -v --cov=src --cov-report=html

# Usando Makefile
make test
```

### Iniciar Jupyter Notebook

```bash
jupyter notebook
```

### Gerar Documentação

```bash
make docs
# ou
cd docs && make html
```

### Formatar Código

```bash
make format
# ou
black src/ tests/
isort src/ tests/
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
├── setup.sh                  # Script instalação Linux/macOS
├── setup.cmd                 # Script instalação Windows
├── requirements.txt          # Dependências
├── pyproject.toml           # Configuração do projeto
├── Makefile                 # Comandos úteis
├── .pre-commit-config.yaml  # Pre-commit hooks
├── pre-push                 # Pre-push hook
└── README.md                # Documentação principal
```

---

## Solução de Problemas

### Python não encontrado

**Linux/Ubuntu:**
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

**macOS (com Homebrew):**
```bash
brew install python@3.11
```

**Windows:**
- Baixe de [python.org](https://www.python.org/downloads/)
- Marque "Add Python to PATH" durante instalação

### pip não encontrado

```bash
# Linux/macOS
python3 -m ensurepip --upgrade

# Windows
python -m ensurepip --upgrade
```

### Erro ao criar venv

Certifique-se de ter `python3-venv` instalado:

```bash
# Ubuntu/Debian
sudo apt install python3-venv

# Fedora
sudo dnf install python3-virtualenv
```

### Erro de permissão (Linux/macOS)

```bash
# Tornar scripts executáveis
chmod +x setup.sh
chmod +x scripts/*.sh
```

### Testes falhando

```bash
# Limpar cache e reinstalar
rm -rf .pytest_cache htmlcov
pip install -r requirements.txt --force-reinstall
pytest tests/ -v
```

### Jupyter não inicia

```bash
# Reinstalar Jupyter
pip install --upgrade jupyter ipython ipykernel

# Reconfigurar kernel
python -m ipykernel install --user --name=sistemas-sinais
```

### Git hooks não funcionam

```bash
# Reinstalar pre-commit
pip install --upgrade pre-commit
pre-commit install --force

# Verificar hooks
pre-commit run --all-files
```

---

## Comandos Úteis

### Makefile

```bash
make help      # Ver todos os comandos
make install   # Instalar dependências
make test      # Executar testes
make lint      # Verificar código
make format    # Formatar código
make docs      # Gerar documentação
make clean     # Limpar arquivos temporários
make sync      # Sincronizar notebooks
make kernel    # Configurar kernel Jupyter
```

### Git Workflow

```bash
# Antes de commitar (automático com pre-commit)
make format
make lint

# Antes de fazer push (automático com pre-push hook)
make test
```

---

## Recursos Adicionais

- **Documentação Python:** [docs.python.org](https://docs.python.org/3/)
- **Documentação NumPy:** [numpy.org](https://numpy.org/doc/)
- **Documentação Matplotlib:** [matplotlib.org](https://matplotlib.org/stable/)
- **Documentação SciPy:** [scipy.org](https://docs.scipy.org/)
- **Documentação pytest:** [pytest.org](https://docs.pytest.org/)
- **Documentação Jupyter:** [jupyter.org](https://jupyter.org/documentation)

---

## Suporte

Se encontrar problemas:

1. Verifique este guia de instalação
2. Execute `python scripts/verify_system.py`
3. Consulte a seção de Solução de Problemas
4. Entre em contato: felipe_lopez@usp.br

---

## Atualizações

Para atualizar o projeto:

```bash
# Puxar últimas mudanças
git pull origin main

# Atualizar dependências
pip install -r requirements.txt --upgrade

# Reinstalar pacote
pip install -e ".[dev,docs]"

# Sincronizar notebooks
make sync

# Verificar sistema
python scripts/test_system.py
```

---

**Última atualização:** Novembro 2025
**Versão:** 0.1.0
