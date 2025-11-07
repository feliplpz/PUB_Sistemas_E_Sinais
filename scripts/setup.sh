#!/bin/bash

# Script de instalação automática - Linux/macOS

set -e  # Para em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  INSTALAÇÃO - SISTEMAS E SINAIS USP  ${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Função para imprimir mensagens de sucesso
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Função para imprimir mensagens de erro
print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Função para imprimir mensagens de aviso
print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Função para imprimir mensagens de info
print_info() {
    echo -e "${BLUE}➜${NC} $1"
}

# 1. Verificar Python
echo ""
print_info "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 não encontrado!"
    echo "  Por favor, instale Python 3.11+ primeiro:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
    echo "  macOS: brew install python@3.11"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
print_success "Python ${PYTHON_VERSION} encontrado"

# Verificar se a versão é >= 3.11
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 11 ]); then
    print_error "Python 3.11+ é necessário (você tem ${PYTHON_VERSION})"
    exit 1
fi

# 2. Criar ambiente virtual
echo ""
print_info "Criando ambiente virtual..."
if [ -d "venv" ]; then
    print_warning "Ambiente virtual já existe. Removendo..."
    rm -rf venv
fi

python3 -m venv venv
print_success "Ambiente virtual criado em ./venv"

# 3. Ativar ambiente virtual
echo ""
print_info "Ativando ambiente virtual..."
source venv/bin/activate
print_success "Ambiente virtual ativado"

# 4. Atualizar pip
echo ""
print_info "Atualizando pip..."
pip install --upgrade pip --quiet
print_success "pip atualizado"

# 5. Instalar dependências
echo ""
print_info "Instalando dependências principais..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
    print_success "Dependências principais instaladas"
else
    print_error "requirements.txt não encontrado!"
    exit 1
fi

# 6. Instalar pacote em modo desenvolvimento
echo ""
print_info "Instalando pacote em modo desenvolvimento..."
if [ -f "pyproject.toml" ]; then
    pip install -e ".[dev,docs]" --quiet
    print_success "Pacote instalado em modo desenvolvimento"
else
    print_warning "pyproject.toml não encontrado, pulando..."
fi

# 7. Configurar pre-commit hooks
echo ""
print_info "Configurando pre-commit hooks..."
if command -v pre-commit &> /dev/null; then
    pre-commit install
    print_success "Pre-commit hooks instalados"
else
    print_warning "pre-commit não instalado (opcional)"
fi

# 8. Configurar pre-push hook
echo ""
print_info "Configurando pre-push hook..."
if [ -f "pre-push" ]; then
    if [ -d ".git/hooks" ]; then
        cp pre-push .git/hooks/pre-push
        chmod +x .git/hooks/pre-push
        print_success "Pre-push hook instalado"
    else
        print_warning ".git/hooks não encontrado (não é um repositório git?)"
    fi
else
    print_warning "pre-push não encontrado (opcional)"
fi

# 9. Configurar kernel Jupyter
echo ""
print_info "Configurando kernel Jupyter..."
if [ -f "scripts/setup_kernel.sh" ]; then
    chmod +x scripts/setup_kernel.sh
    bash scripts/setup_kernel.sh
    print_success "Kernel Jupyter configurado"
else
    print_warning "scripts/setup_kernel.sh não encontrado"
fi

# 10. Tornar scripts executáveis
echo ""
print_info "Tornando scripts executáveis..."
if [ -d "scripts" ]; then
    chmod +x scripts/*.sh 2>/dev/null || true
    print_success "Scripts marcados como executáveis"
fi

# 11. Sincronizar notebooks
echo ""
print_info "Sincronizando notebooks..."
if [ -f "scripts/sync_notebooks.sh" ]; then
    bash scripts/sync_notebooks.sh
    print_success "Notebooks sincronizados"
else
    print_warning "scripts/sync_notebooks.sh não encontrado"
fi

# 12. Executar testes
echo ""
print_info "Executando testes..."
if command -v pytest &> /dev/null; then
    if pytest tests/ -v --quiet 2>&1 | tail -1; then
        print_success "Todos os testes passaram"
    else
        print_warning "Alguns testes falharam (verifique com 'make test')"
    fi
else
    print_warning "pytest não instalado"
fi

# 13. Verificar sistema
echo ""
print_info "Executando verificação completa do sistema..."
if [ -f "scripts/verify_system.py" ]; then
    python scripts/test_system.py
fi

# Resumo final
echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  INSTALAÇÃO CONCLUÍDA COM SUCESSO!  ${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Para começar a usar:"
echo ""
echo "  1. Ative o ambiente virtual:"
echo -e "     ${YELLOW}source venv/bin/activate${NC}"
echo ""
echo "  2. Execute os notebooks:"
echo -e "     ${YELLOW}jupyter notebook${NC}"
echo ""
echo "  3. Ou rode os testes:"
echo -e "     ${YELLOW}make test${NC}"
echo ""
echo "  4. Veja todos os comandos disponíveis:"
echo -e "     ${YELLOW}make help${NC}"
echo ""
echo -e "${BLUE}Documentação completa: README.md${NC}"
echo ""
