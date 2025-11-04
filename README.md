# 📊 Sistemas e Sinais - USP

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simulações interativas para o aprendizado de Sistemas e Sinais.

---

## 🚀 Para Alunos

Clique nos links abaixo para abrir direto no Google Colab:

| # | Tópico | Colab |
|---|--------|-------|
| 01 | Modelo Predador-Presa | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/feliplpz/PUB_Sistemas_E_Sinais/blob/main/notebooks/predador_presa.ipynb) |

---

## 🛠️ Setup Local

```bash
git clone https://github.com/feliplpz/PUB_Sistemas_E_Sinais.git
cd PUB_Sistemas_E_Sinais

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## 📝 Workflow

```bash
# Edite o .py no PyCharm
# notebooks/01_predador_presa.py

# Gere o .ipynb
jupytext --sync notebooks/01_predador_presa.py

# Teste
jupyter notebook

# Formate
black notebooks/
isort notebooks/

# Commit
git add .
git commit -m "Add: predador-presa"
git push
```

---

## 📧 Contato

**Felipe Lopez**
felipe_lopez@usp.br
Universidade de São Paulo (USP)

## 📄 Licença

MIT License - veja [LICENSE](LICENSE)
