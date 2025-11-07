@echo off
REM Script de instalacao automatica - Windows


setlocal EnableDelayedExpansion

echo ========================================
echo   INSTALACAO - SISTEMAS E SINAIS USP
echo ========================================
echo.

REM 1. Verificar Python
echo [INFO] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale Python 3.11+ primeiro:
    echo https://www.python.org/downloads/
    echo.
    echo Certifique-se de marcar "Add Python to PATH" durante a instalacao
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% encontrado

REM Verificar versao Python >= 3.11
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if %MAJOR% LSS 3 (
    echo [ERRO] Python 3.11+ necessario ^(voce tem %PYTHON_VERSION%^)
    pause
    exit /b 1
)

if %MAJOR% EQU 3 if %MINOR% LSS 11 (
    echo [ERRO] Python 3.11+ necessario ^(voce tem %PYTHON_VERSION%^)
    pause
    exit /b 1
)

REM 2. Criar ambiente virtual
echo.
echo [INFO] Criando ambiente virtual...
if exist venv (
    echo [AVISO] Ambiente virtual ja existe. Removendo...
    rmdir /s /q venv
)

python -m venv venv
if errorlevel 1 (
    echo [ERRO] Falha ao criar ambiente virtual
    pause
    exit /b 1
)
echo [OK] Ambiente virtual criado em .\venv

REM 3. Ativar ambiente virtual
echo.
echo [INFO] Ativando ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERRO] Falha ao ativar ambiente virtual
    pause
    exit /b 1
)
echo [OK] Ambiente virtual ativado

REM 4. Atualizar pip
echo.
echo [INFO] Atualizando pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo [AVISO] Falha ao atualizar pip, continuando...
) else (
    echo [OK] pip atualizado
)

REM 5. Instalar dependencias principais
echo.
echo [INFO] Instalando dependencias principais...
if not exist requirements.txt (
    echo [ERRO] requirements.txt nao encontrado!
    pause
    exit /b 1
)

pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias
    pause
    exit /b 1
)
echo [OK] Dependencias principais instaladas

REM 6. Instalar pacote em modo desenvolvimento
echo.
echo [INFO] Instalando pacote em modo desenvolvimento...
if exist pyproject.toml (
    pip install -e ".[dev,docs]" --quiet
    if errorlevel 1 (
        echo [AVISO] Falha ao instalar pacote em modo dev
    ) else (
        echo [OK] Pacote instalado em modo desenvolvimento
    )
) else (
    echo [AVISO] pyproject.toml nao encontrado, pulando...
)

REM 7. Configurar pre-commit hooks
echo.
echo [INFO] Configurando pre-commit hooks...
where pre-commit >nul 2>&1
if errorlevel 1 (
    echo [AVISO] pre-commit nao instalado ^(opcional^)
) else (
    pre-commit install
    echo [OK] Pre-commit hooks instalados
)

REM 8. Configurar pre-push hook (nao disponivel nativamente no Windows)
echo.
echo [INFO] Pre-push hook...
if exist pre-push (
    if exist .git\hooks (
        copy /y pre-push .git\hooks\pre-push >nul
        echo [OK] Pre-push hook copiado ^(precisa de Git Bash para executar^)
    ) else (
        echo [AVISO] .git\hooks nao encontrado ^(nao e um repositorio git?^)
    )
) else (
    echo [AVISO] pre-push nao encontrado ^(opcional^)
)

REM 9. Configurar kernel Jupyter
echo.
echo [INFO] Configurando kernel Jupyter...
python -m ipykernel install --user --name=sistemas-sinais --display-name "Python (Sistemas e Sinais)"
if errorlevel 1 (
    echo [AVISO] Falha ao configurar kernel Jupyter
) else (
    echo [OK] Kernel Jupyter configurado
)

REM 10. Sincronizar notebooks
echo.
echo [INFO] Sincronizando notebooks...
if exist scripts\sync_notebooks.cmd (
    call scripts\sync_notebooks.cmd
    echo [OK] Notebooks sincronizados
) else (
    echo [AVISO] scripts\sync_notebooks.cmd nao encontrado
)

REM 11. Executar testes
echo.
echo [INFO] Executando testes...
where pytest >nul 2>&1
if errorlevel 1 (
    echo [AVISO] pytest nao instalado
) else (
    pytest tests\ -v --quiet
    if errorlevel 1 (
        echo [AVISO] Alguns testes falharam ^(verifique com 'pytest tests\''^)
    ) else (
        echo [OK] Todos os testes passaram
    )
)

REM 12. Verificar sistema
echo.
echo [INFO] Executando verificacao completa do sistema...
if exist scripts\verify_system.py (
    python scripts\verify_system.py
)

REM Resumo final
echo.
echo ========================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo ========================================
echo.
echo Para comecar a usar:
echo.
echo   1. Ative o ambiente virtual:
echo      venv\Scripts\activate
echo.
echo   2. Execute os notebooks:
echo      jupyter notebook
echo.
echo   3. Ou rode os testes:
echo      pytest tests\ -v
echo.
echo   4. Para formatar codigo:
echo      black src\ tests\
echo.
echo Documentacao completa: README.md
echo.

pause
