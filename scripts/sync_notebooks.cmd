@echo off
echo Sincronizando notebooks...

for %%f in (notebooks\*.py) do (
    echo   - %%f
    jupytext --sync "%%f"
)

echo Sincronizacao completa!
