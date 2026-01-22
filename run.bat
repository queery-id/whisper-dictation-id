@echo off
title Whisper Dictation - Indonesian
echo ========================================
echo   Whisper Dictation - Indonesian
echo ========================================
echo.

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Virtual environment not found!
    echo Run this first: python -m venv .venv
    echo Then: .venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

echo Starting Whisper Dictation...
echo Press Ctrl+Win+H to start/stop recording
echo.
.venv\Scripts\python.exe src\main.py

pause
