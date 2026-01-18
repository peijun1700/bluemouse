# 🐭 BlueMouse v6.6
### The AI Safety Layer for Cursor & Claude
**Stop Vibe Coding. Start Engineering.**

[![Glama | bluemouse](https://glama.ai/mcp/servers/@peijun1700/bluemouse/badge)](https://glama.ai/mcp/servers/@peijun1700/bluemouse)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-blue?style=for-the-badge)](docs/reports/STATUS_REPORT_v6.6.md)
[![License](https://img.shields.io/badge/License-AGPLv3-red?style=for-the-badge)](LICENSE)

[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Local-green?style=for-the-badge)](PRIVACY.md)
[![Compatible](https://img.shields.io/badge/Works%20With-Cursor%20%7C%20Claude-purple?style=for-the-badge)](CURSOR_GUIDE.md)

> **[中文文檔](README_ZH.md)** | **English** | **Contact:** bluemouse.ai@gmail.com

---

## 🌟 Why BlueMouse?

In the era of **Vibe Coding**, AI generates code faster than we can read. But even the best AI (Claude 3.5 / 4.5) hallucinates. 

**BlueMouse is your Airbag.** 

It's not another coding tool—it's a **Quality Gate** that stops bad code before it happens.

### The Problem
- ❌ AI generates code by "vibes" without deep logic validation
- ❌ Edge cases are completely ignored
- ❌ Tech debt explodes silently
- ❌ You find bugs in production, not development

### The Solution
- ✅ **17-Layer Validation** - Every line passes through AST parsing, type checking, and security audits
- ✅ **Socratic Interview** - AI must answer logic questions before generating code
- ✅ **Zero Infrastructure Cost** - 100% local execution, no servers needed
- ✅ **One-Word Start** - Just type "Start" in Cursor

---

## 🔥 Core Features

### 🦠 Parasitic Architecture
**$0 Infrastructure Cost.** BlueMouse sits between you and the compiler, intercepting commands in <10ms. No servers, no subscriptions, no cloud dependencies.

### 🧠 Socratic Logic Gate
Before writing code, BlueMouse interviews the AI with critical questions:
- *"For concurrent orders, pessimistic lock or optimistic lock?"*
- *"On payment failure, rollback immediately or retry 3 times?"*

Forces you (and AI) to think before coding.

### 🛡️ 17-Layer Validation
Code generation passes through 17 logic gates:
1. **Syntax** - Correctness
2. **Type** - Static type checking (Pydantic/MyPy)
3. **Security** - OWASP Top 10 scanning
4. **Logic** - Business logic integrity
5. **Performance** - Complexity analysis
... and 12 more layers

### 👆 One-Word Start
```bash
# Just drag the folder into Cursor and type:
Start
```
BlueMouse automatically injects `.cursorrules` and starts protecting your code.

---

## 🏆 Industrial Grade Certification

BlueMouse v6.6 has passed rigorous stress tests:

| Test Protocol | Status | Description |
| :--- | :--- | :--- |
| **Antarctica Protocol** | ✅ **PASSED** | 100% functionality in offline/air-gapped environments |
| **Bilingual Acid Test** | ✅ **PASSED** | Seamless dynamic language switching (zh-TW / en-US) |
| **Data Resilience** | ✅ **PASSED** | Validated against 28 high-concurrency/financial-risk scenarios |
| **Security Hardening** | ✅ **PASSED** | XSS, SQL Injection, Path Traversal protection |
| **Vetting Depth** | ✅ **17 LAYERS** | Code generation piped through 17 logic gates |

---

## 🚀 Quick Start

### System Requirements
- **Python**: 3.9+
- **OS**: macOS / Linux / Windows
- **Disk Space**: ~50MB
- **Network**: Optional (works 100% offline)

### Installation

#### Option 1: One-Click Start (Recommended)
**Mac/Linux:**
```bash
./start_bluemouse.command
```

**Windows:**
```bash
start_bluemouse.bat
```

#### Option 2: Manual Start
**Mac/Linux:**
```bash
python3 -m pip install -r requirements.txt
python3 start_v6.py
```

**Windows:**
```bash
python -m pip install -r requirements.txt
python start_v6.py
```

The server will start on `http://localhost:8001` and your browser will open automatically.

---

## 📖 Usage

### 1. Enter Your Vision
Describe what you want to build:
```
I want to build an e-commerce platform with user authentication
```

### 2. Answer Socratic Questions
BlueMouse will ask critical logic questions:
- Database concurrency strategy?
- Error handling approach?
- Security measures?

### 3. Get Validated Code
After passing 17 layers of validation, download your project ZIP containing:
- ✅ Source code
- ✅ Architecture diagrams
- ✅ Installation guide
- ✅ Cost estimation
- ✅ Validation report

---

## 🛡️ Enterprise Security

### 100% Local Execution
- ✅ No data leaves your machine
- ✅ No cloud dependencies
- ✅ No telemetry or tracking
- ✅ Works in air-gapped environments

### AGPLv3 License
- ✅ Open source for transparency
- ✅ Commercial use requires compliance
- ✅ Protects against closed-source forks

**Read our [Privacy Whitepaper](PRIVACY.md)** for technical details.

---

## 🔧 Troubleshooting

### `python3: command not found`
**Mac/Linux:**
```bash
brew install python3
```
**Windows:** Download from [python.org](https://www.python.org/downloads/)

### `pip install` fails
Try using a mirror:
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Port 8001 already in use
```bash
# Find and kill the process
lsof -ti:8001 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :8001   # Windows
```

### Permission denied
```bash
chmod +x start_bluemouse.command  # Mac/Linux
```

### `ModuleNotFoundError`
```bash
pip install -r requirements.txt --force-reinstall
```

### Browser doesn't open
Manually navigate to: `http://localhost:8001`

**More help:** See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 📚 Documentation

- **[System Architecture](BlueMouse_v6.6_MASTER_ARCH.md)** - Technical deep dive
- **[Changelog](CHANGELOG.md)** - Version history
- **[Privacy Policy](PRIVACY.md)** - Data handling details
- **[License](LICENSE)** - AGPLv3 terms
- **[Cursor Integration Guide](CURSOR_GUIDE.md)** - IDE setup

---

## 🌍 Community

- **GitHub Issues**: [Report bugs or request features](https://github.com/peijun1700/bluemouse/issues)
- **Discussions**: [Join the conversation](https://github.com/peijun1700/bluemouse/discussions)
- **Email**: bluemouse.ai@gmail.com

---

## 🎯 Roadmap

### v6.6 (Current)
- ✅ 17-Layer validation system
- ✅ Socratic question library (22 questions, 10 categories)
- ✅ Bilingual support (zh-TW / en-US)
- ✅ Zero-cost parasitic architecture

### v7.0 (Planned)
- 🔄 Frontend template generation
- 🔄 Custom question library
- 🔄 Team collaboration features
- 🔄 Enterprise audit logs

---

## 📄 License

BlueMouse is licensed under **AGPLv3**.

**What this means:**
- ✅ Free for personal use
- ✅ Free for open-source projects
- ⚠️ Commercial use requires compliance (or contact us for licensing)

See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Built with:
- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation
- **Anthropic Claude** - AI reasoning (optional)
- **Ollama** - Local AI models (optional)

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/peijun1700/bluemouse?style=social)
![GitHub forks](https://img.shields.io/github/forks/peijun1700/bluemouse?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/peijun1700/bluemouse?style=social)

---

**Made with ❤️ by developers who care about code quality**

**Stop Vibe Coding. Start Engineering.** 🐭
