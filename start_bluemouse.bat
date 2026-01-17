@echo off
chcp 65001 > nul
setlocal

echo 🐭 Starting BlueMouse v6.0...

cd /d "%~dp0"

:: 1. Check Python
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.10+ and add it to PATH.
    pause
    exit /b 1
)

:: 2. Check/Create Venv
if not exist "venv" (
    echo ⚠️  Creating virtual environment...
    python -m venv venv
    echo 📦 Installing dependencies...
    venv\Scripts\pip install -r requirements.txt
    echo ✅ Environment ready.
)

:: 3. Setup MCP Config (Auto-Injection)
echo 🔧 Configuring MCP for VS Code...
venv\Scripts\python setup_mcp.py

:: 4. Start Server and Browser
echo 🚀 Starting API Server...
echo 👉 Please watch the browser popup.
echo.

start "" "http://localhost:8001"
venv\Scripts\python run_standalone.py

pause
