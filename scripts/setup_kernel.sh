bash#!/bin/bash

KERNEL_NAME="sistemas-sinais"

echo "Configurando kernel Jupyter: $KERNEL_NAME"

pip install ipykernel --quiet

python -m ipykernel install --user --name=$KERNEL_NAME --display-name "Python (Sistemas e Sinais)"

echo "✅ Kernel '$KERNEL_NAME' instalado!"
echo ""
echo " No Jupyter, selecione: 'Python (Sistemas e Sinais)'"
