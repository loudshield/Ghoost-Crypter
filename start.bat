@echo off
title GHOOST CRYPTER
cls

echo [*] Starting GHOOST CRYPTER...
echo [*] Checking Python...

where py >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b
)

echo [*] Installing requirements...
py -m pip install --upgrade pip >nul
py -m pip install -r requirements.txt

echo.
echo [*] Launching Ghoost...
echo.

py main.py

pause
