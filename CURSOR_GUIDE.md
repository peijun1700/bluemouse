# 🐭 How to Use BlueMouse in Cursor

**BlueMouse works natively with Cursor.** 
You don't need a cloud server. It runs 100% locally on your machine.

Since Cursor acts as an improved VS Code with AI superpowers, integrating BlueMouse (the "Prefrontal Cortex") gives Cursor users the ultimate coding experience: **Logic-First AI**.

---

## 🚀 Setup Guide (30 Seconds)

### Step 1: Open Cursor Settings
1. Press `Cmd + ,` (Mac) or `Ctrl + ,` (Windows) to open Settings.
2. In the search bar, type **MCP**.
3. Or navigate to **Features > MCP** (if available in your version).

*Note: If you can't find the UI, you can manually edit the config file. See Option B.*

### Step 2: Add New MCP Server

Click **"Add New Server"** and fill in the details:

*   **Name**: `BlueMouse`
*   **Type**: `stdio` (Standard Input/Output)
*   **Command**: `uv` (or `python`, see note below)
*   **Arguments**:
    *   `/absolute/path/to/bluemouse_v6_release_final/server.py`

> **💡 Important**: You must use the **absolute path** to the `server.py` file on your computer.
> Example: `/Users/peijunchen0410/Desktop/bluemouse_v6_release_final/server.py`

#### Using Python directly (Recommended)
You should point directly to the python executable in the virtual environment:

*   **Command**: `/Users/peijunchen0410/Desktop/bluemouse_v6_release_final/venv/bin/python`
*   **Arguments**: `server.py`

> **Note**: Do NOT use `start_bluemouse.command` for Cursor anymore. That script is now exclusively for the Standalone App (Web UI).

### Step 3: Verify Connection
1. Cursor should show a green indicator (Operational).
2. Open Composer (`Cmd + I` or `Cmd + L`).
3. Ask it: *"BlueMouse, analyze my project structure."*
4. You should see BlueMouse tools being called!

---

## 🛠 Option B: Manual Config (Advanced)

If you prefer configuration files, create or edit `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "BlueMouse": {
      "command": "python3",
      "args": [
        "/Users/peijunchen0410/Desktop/bluemouse_v6_release_final/server.py"
      ],
      "env": {
        "ANTHROPIC_API_KEY": "sk-ant-..."
      }
    }
  }
}
```

## ❓ FAQ

**Q: Is this Cloud MCP?**
A: No. This is **Local MCP**. All logic runs on your machine. No code leaves your computer except to the LLM provider you already use (Claude/OpenAI).

**Q: Does it conflict with Antigravity?**
A: No. Antigravity uses the same protocol. You can have both running.

---
*Empower your Cursor with Logic.*
