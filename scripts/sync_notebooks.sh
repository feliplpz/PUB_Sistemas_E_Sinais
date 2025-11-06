#!/bin/bash

echo "Sincronizando notebooks..."

for notebook in notebooks/*.py; do
    if [ -f "$notebook" ]; then
        echo "  ✓ $(basename $notebook)"
        jupytext --sync "$notebook"
    fi
done

echo " Sincronização completa"
