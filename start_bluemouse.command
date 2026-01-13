#!/bin/bash

# 1. 切換到腳本所在目錄
cd "$(dirname "$0")"

# 2. 設置控制台顏色
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}🐭 正在啟動藍圖小老鼠 v6.0...${NC}"

# 2. Check for API Keys (Optional but recommended)
if [ -z "$ANTHROPIC_API_KEY" ] && [ -z "$OPENAI_API_KEY" ] && [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  [Warning] No API Keys detected in environment."
    echo "   BlueMouse will run in 'Local Mode' (using Ollama if available)."
    echo "   To use Cloud AI, please export ANTHROPIC_API_KEY or GEMINI_API_KEY in your .zshrc profile."
fi

# 3. 設置 API Key (請在這裡填入您的 Key)
# export ANTHROPIC_API_KEY="AIzaSyAPspAV_s-2XYnvv5qfokQJaefy0YUmEy8"

# 4. 強制清理端口 8001 (解決 'Address already in use' 問題)
PORT=8001
PID=$(lsof -t -i:$PORT)
if [ -n "$PID" ]; then
    echo -e "${RED}⚠️  檢測到端口 $PORT 被佔用 (PID: $PID)，正在清理...${NC}"
    kill -9 $PID
    echo -e "${GREEN}✅ 舊進程已關閉${NC}"
fi

# 5. 檢查虛擬環境
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ 未檢測到虛擬環境，正在自動修復...${NC}"
    python3 -m venv venv
    ./venv/bin/pip install fastmcp uvicorn fastapi pydantic websockets anthropic
    echo -e "${GREEN}✅ 環境修復完成${NC}"
fi

# 5.1 自動配置 VS Code MCP (Auto-Injection)
echo -e "${CYAN}🔧 正在配置 VS Code工作區設定...${NC}"
./venv/bin/python setup_mcp.py

# 6. 自動打開瀏覽器 (延遲 2 秒執行)
(sleep 2 && open "bluemouse_saas.html") &

# 7. 啟動大腦 (Server)
echo -e "${GREEN}🚀 啟動 API Server...${NC}"
echo -e "${CYAN}👉 請留意自動彈出的網頁視窗${NC}"
echo "---------------------------------------------------"

./venv/bin/python api_server_v2.py
