# 🎬 BlueMouse 短影音劇本 (中英雙語雙軌制)

**核心策略 (Core Strategy)**: 
不解釋技術原理，直接展示「恐懼」與「救命瞬間」。
**格式**: 9:16 直式影片
**風格**: 快節奏、螢幕錄影實況 + 文字壓字
**音效**: 懸疑心跳聲 -> 警報聲 -> 舒緩音樂 (Lo-Fi beat)

---

## 🎥 劇本 1: 刪庫危機 (The Delete DB Heart Attack)
**目標受眾**: 初學者、接案工程師 (怕賠錢的人)

**開場 Hook (0-2秒)**:
*   **畫面**: Cursor/VSCode 畫面，你的手在打字打很快。
*   **文字 (CN)**: 「視角：AI 差點刪了我的正式庫，但我沒檢查...」
*   **Text (EN)**: "POV: AI almost deleted my production DB and I didn't verify."
*   **音效**: 急促的心跳聲。

**動作 (2-8秒)**:
*   **你的指令 (Prompt)**: 
    *   (CN) "重構 clean_up 函數，把舊的資料表直接 drop 掉。"
    *   (EN) "Refactor clean_up function. Just drop the old tables."
*   **AI 生成中**: 畫面上看到 AI 正在寫 `DROP TABLE users;` ...
*   **高潮點 (Climax)**: 突然！螢幕跳出一個 **藍色警報視窗 (Blue Modal)** 🛑
*   **BlueMouse 訊息**: 
    *   "⚠️ **CRITICAL STOP**: You are executing a DROP command without Environment Check. Is this PROD?" 
    *   (系統預設是英文，不用改，這樣看起來更專業)

**救贖 (8-12秒)**:
*   **畫面**: 滑鼠游標停在 "No, it's Prod! (不，這是正式環境)" 按鈕上，按下拒絕。
*   **文字 (CN)**: 「BlueMouse 剛剛救了我的職業生涯。🤯」
*   **Text (EN)**: "BlueMouse saved my job. 🤯"
*   **結尾 CTA**: 
    *   (CN)「別讓 AI 裸奔。下載連結在首頁。」
    *   (EN) "Don't code naked. Link in bio."

---

## 🎥 劇本 2: 無限迴圈 (The Infinite Loop / AWS Bill)
**目標受眾**: 雲端使用者 (怕 AWS 帳單爆炸的人)

**開場 Hook (0-2秒)**:
*   **畫面**: 效能監視器 (Activity Monitor) CPU 飆到 100%，紅色圖表。
*   **文字 (CN)**: 「為什麼我的 AWS 帳單突然變五千美金？」
*   **Text (EN)**: "Why is my AWS bill $5,000?"

**鋪陳 (2-7秒)**:
*   **畫面**: 鏡頭拉近到 Python 程式碼。在一個複雜的函數裡，藏著一個 `while True` 卻沒有寫 `break` (AI 寫的爛扣)。
*   **文字 (CN)**: 「我直接複製貼上 ChatGPT 給的代碼...」
*   **Text (EN)**: "I copied this from ChatGPT blindly..."

**解決方案 (7-12秒)**:
*   **畫面**: BlueMouse 的「邏輯檢查報告」(Markdown预览介面)。
*   **重點**: 紅色框框圈出那個迴圈。
*   **文字 (CN)**: 「它在我部署"之前"就抓到了。」
*   **Text (EN)**: "It caught the bug BEFORE I deployed."

---

## 🎥 劇本 3: 金鑰外洩 (The Secret Key Leak)
**目標受眾**: 所有開發者 (最常見的資安意外)

**開場 Hook (0-2秒)**:
*   **畫面**: Git Commit 紀錄在快速滾動。
*   **文字 (CN)**: 「死定了，我把 API Key 推到公開 Github 了。」
*   **Text (EN)**: "I accidentally committed my API Keys to GitHub."

**攔截 (2-8秒)**:
*   **畫面**: 你把專案資料夾拖進 Cursor (展示 One-Word Start 一鍵啟動)。
*   **你的指令**: "Push to origin master."
*   **BlueMouse**: 🛑 BLOCKED (被攔截)。
*   **蘇格拉底提問**: "I see `.env` files in your commit list. Are you sure?" (我看到你在提交環境變數檔，你確定嗎？)

**教訓 (8-12秒)**:
*   **畫面**: 你趕快把檔案移除。
*   **文字 (CN)**: 「這是真正的邏輯防火牆。」
*   **Text (EN)**: "The Logic Firewall is real."
*   **結尾 CTA**: 
    *   (CN)「GitHub 免費下載。裝一下吧。」
    *   (EN) "Get your firewall. Free on GitHub."

---

## 🛠️ 拍攝執行指南 (How to Execute)

1.  **分開錄製**: 
    *   您可以錄一次畫面，然後用剪輯軟體(剪映/CapCut) 分別壓上「中文」和「英文」的字幕，輸出成兩支影片。這樣最省力。
2.  **真實操作**: 
    *   請真的在電腦上執行這些操作。BlueMouse 的反應是真實的，觀眾看得出來是不是特效。
3.  **封面圖**:
    *   那張 "Critical Stop" 的封面圖是通用的，不需要翻譯，"SAVED MY JOB" 這種簡單英文大家看得懂，看起來比較像歐美大片。
