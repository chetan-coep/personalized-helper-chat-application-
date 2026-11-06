@echo off
title DocSyntax AI - Developer Code & Documentation Assistant
color 0A

echo ======================================================================
echo           DOCSYNTAX AI - STARTING UNIFIED APPLICATION
echo ======================================================================
echo.

cd /d "%~dp0backend"

:: Check if uv is installed
where uv >nul 2>nul
if %errorlevel% equ 0 (
    echo [INFO] Found uv package manager.
    echo [INFO] Starting backend server and serving frontend on http://localhost:8000...
    echo.
    start "" http://localhost:8000
    uv run python server.py
) else (
    echo [INFO] uv not found, falling back to python...
    if exist ".venv\Scripts\activate.bat" (
        call .venv\Scripts\activate.bat
    )
    start "" http://localhost:8000
    python server.py
)

pause

