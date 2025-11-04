# Setup Rápido

## 1. Instalar dependências

```bash
pip install -r requirements.txt
pip install -e ".[dev,docs]"
```

## 2. Configurar pre-commit hooks

```bash
pre-commit install
```

## 3. Configurar pre-push hook (testes)

```bash
cp pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

## 4. Configurar kernel Jupyter

```bash
./scripts/setup_kernel.sh
```

## 5. Testar

```bash
make test     # Rodar testes
make lint     # Verificar código
make format   # Formatar código
make docs     # Gerar documentação
```

## Onde colocar cada arquivo

```
seu-projeto/
├── .pre-commit-config.yaml    # Raiz do projeto
├── pyproject.toml              # Raiz do projeto
├── Makefile                    # Raiz do projeto
├── requirements.txt            # Raiz do projeto
├── pre-push                    # Copiar para .git/hooks/
└── .github/
    └── workflows/
        └── ci.yml             # GitHub Actions
```

##  O que acontece agora

### Ao fazer `git commit`:
- ✅ Black formata código automaticamente
- ✅ isort organiza imports
- ✅ Ruff verifica PEP8 em `src/`
- ✅ Verifica docstrings obrigatórios em `src/`
- ❌ Bloqueia commit se houver erros

### Ao fazer `git push`:
- ✅ Roda todos os testes
- ✅ Verifica coverage mínimo (80%)
- ❌ Bloqueia push se testes falharem

### No GitHub (PR):
- ✅ CI roda testes em Python 3.11 e 3.12
- ✅ Verifica formatação
- ✅ Gera documentação
- ✅ Upload de coverage

## 🛠️ Comandos úteis

```bash
make help      # Ver todos os comandos
make format    # Formatar antes de commit
make test      # Rodar testes localmente
make docs      # Gerar docs
```

## 🚨 Troubleshooting

**Pre-commit muito lento?**
```bash
pre-commit run --all-files  # Primeira vez é lenta
```

**Testes falhando?**
```bash
pytest tests/ -v  # Ver detalhes
```

**Documentação não gera?**
```bash
cd docs && make clean && make html
```
