#!/bin/bash

echo "Executando testes do modelo Predador-Presa..."
echo "=============================================="
echo ""

pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html

echo ""
echo "=============================================="
echo "Testes concluídos!"
echo ""
echo "Para ver relatório de cobertura detalhado:"
echo "  Abra: htmlcov/index.html"
