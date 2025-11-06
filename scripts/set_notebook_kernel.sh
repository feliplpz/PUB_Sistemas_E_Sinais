#!/bin/bash

KERNEL_NAME="sistemas-sinais"
KERNEL_DISPLAY="Python (Sistemas e Sinais)"

echo "Configurando kernel nos notebooks..."

for notebook_py in notebooks/*.py; do
    if [ -f "$notebook_py" ]; then
        echo "  ✓ $(basename $notebook_py)"

        if ! grep -q "kernelspec:" "$notebook_py"; then
            cat > /tmp/kernel_header.txt << HEADER
# ---
# jupyter:
#   kernelspec:
#     display_name: $KERNEL_DISPLAY
#     language: python
#     name: $KERNEL_NAME
# ---

HEADER
            cat /tmp/kernel_header.txt "$notebook_py" > /tmp/notebook_temp.py
            mv /tmp/notebook_temp.py "$notebook_py"
            rm /tmp/kernel_header.txt
        fi

        jupytext --sync "$notebook_py"
    fi
done

echo "Kernels configurados!"
