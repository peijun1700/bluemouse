# Changelog

All notable changes to BlueMouse will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [6.6.1] - 2026-01-17

### Added
- 🌍 **完整雙語支援**: 所有蘇格拉底式問題現在支援中英文動態切換
  - 翻譯 10 個問題類別 (payment, inventory, authentication, data_consistency, api_integration, privacy, chat, booking, frontend, todo)
  - 總計 22 個問題,全部支援 zh-TW 和 en-US
- 📝 **草稿欄語言切換**: 草稿通知現在會根據選擇的語言顯示
- 📋 **系統要求說明**: README 新增詳細的系統要求區段
- 🔧 **故障排除指南**: README 新增完整的故障排除區段,涵蓋 6 個常見問題
- 📖 **手動啟動教學**: README 新增詳細的手動啟動步驟 (Mac/Linux/Windows)
- 📚 **CHANGELOG.md**: 新增版本更新記錄文件

### Changed
- 🌐 **預設語言改為英文**: 首次訪問時預設使用 en-US
- 🔄 **語言偏好持久化**: 用戶選擇的語言會自動保存到 LocalStorage

### Fixed
- 🐛 修復草稿欄文字無法切換語言的問題
- 🐛 修復部分問題類別缺少英文翻譯的問題

## [6.6.0] - 2026-01-16

### Added
- 🎬 **社群媒體策略**: 新增 Instagram/TikTok 拍攝指南
- 📊 **商業可行性分析**: 新增完整的市場分析文檔
- 🏗️ **架構文檔更新**: 更新到 v6.6 主架構文檔

### Changed
- 🚀 優化啟動腳本 (start_bluemouse.command / start_bluemouse.bat)
- 📝 更新使用指南 (USAGE_GUIDE.md)

## [6.0.0] - 2026-01-13

### Added
- 🦠 **寄生架構**: $0 基礎設施成本
- 🧠 **蘇格拉底邏輯門**: AI 代碼生成前的邏輯面試
- 🛡️ **17 層驗證**: 軍規級代碼審查
- 🌐 **MCP 整合**: 支援 Cursor 和 Windsurf
- 📦 **一鍵啟動**: 拖放即用,無需配置
- 🔒 **100% 本地化**: 完全離線運行,零隱私風險
- 🏆 **工業級認證**: 通過 Antarctica Protocol 等嚴格測試

### Security
- ✅ AGPLv3 授權保護
- ✅ 隱私白皮書 (PRIVACY.md)
- ✅ 零數據外傳

---

## Version Naming Convention

- **Major (X.0.0)**: 重大架構變更或破壞性更新
- **Minor (6.X.0)**: 新功能、重要改進
- **Patch (6.6.X)**: Bug 修復、小優化

---

**Note**: 本專案遵循 [Semantic Versioning](https://semver.org/)。
