@echo off
title AI Paste
cd /d "%~dp0backend"
echo Starting AI Paste...
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
pause
