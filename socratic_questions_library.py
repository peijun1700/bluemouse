"""
蘇格拉底式問題庫
收集高質量的決策型/邊界型問題範例

🚨 核心修正 2: Data Trap 的核心資產
這些問題用於收集人類的高價值決策數據
"""

from typing import Dict, List, Any

# ========================================
# 問題庫 - 按場景分類
# ========================================

QUESTION_LIBRARY: Dict[str, List[Dict[str, Any]]] = {
    
    # 付款/交易場景 (Payment/Transaction)
    "payment": [
        {
            "text": {
                "zh-TW": "如果付款 API 在扣款後超時(30秒無響應),你要如何確認付款是否成功?",
                "en-US": "If payment API times out after deduction (30s no response), how to confirm payment success?"
            },
            "category": "error_handling",
            "options": {
                "zh-TW": ["A. 立即重試付款請求", "B. 調用查詢付款狀態 API", "C. 標記為待確認,人工處理"],
                "en-US": ["A. Retry payment immediately", "B. Call payment status query API", "C. Mark as pending, manual handling"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 重複扣款風險", "1": "✅ 標準做法", "2": "⚠️ 用戶體驗差"},
                "en-US": {"0": "⚠️ Duplicate charge risk", "1": "✅ Standard practice", "2": "⚠️ Poor UX"}
            },
            "trap": "Testing idempotency and distributed transaction understanding"
        },
        {
            "text": {
                "zh-TW": "用戶付款成功但訂單建立失敗,你要如何處理?",
                "en-US": "User payment succeeded but order creation failed, how to handle?"
            },
            "category": "recovery",
            "options": {
                "zh-TW": ["A. 自動退款給用戶", "B. 重試建立訂單 (最多3次)", "C. 保留付款記錄,允許用戶重新下單"],
                "en-US": ["A. Auto refund to user", "B. Retry order creation (max 3 times)", "C. Keep payment record, allow re-order"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 損失交易機會", "1": "✅ 自動恢復", "2": "⚠️ 客服成本高"},
                "en-US": {"0": "⚠️ Lost transaction", "1": "✅ Auto recovery", "2": "⚠️ High support cost"}
            },
            "trap": "Testing compensating transaction understanding"
        },
        {
            "text": {
                "zh-TW": "如果用戶在付款過程中按下 '上一頁',系統會發生什麼?",
                "en-US": "If user clicks 'back' during payment, what happens?"
            },
            "category": "state_management",
            "options": {
                "zh-TW": ["A. 重複建立訂單", "B. 鎖定訂單,提示 '付款中'", "C. 無反應"],
                "en-US": ["A. Duplicate order creation", "B. Lock order, show 'Payment in progress'", "C. No response"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 髒數據風險", "1": "✅ 狀態機保護", "2": "⚠️ 用戶困惑"},
                "en-US": {"0": "⚠️ Dirty data risk", "1": "✅ State machine protection", "2": "⚠️ User confusion"}
            },
            "trap": "Testing frontend state locking awareness"
        }
    ],

    # 庫存/並發場景 (Inventory/Concurrency)
    "inventory": [
        {
            "text": {
                "zh-TW": "兩個用戶同時購買最後一件商品,你要如何處理?",
                "en-US": "Two users buy the last item simultaneously, how to handle?"
            },
            "category": "concurrency",
            "options": {
                "zh-TW": ["A. 先到先得 (DB Lock)", "B. 兩者都成功,超賣後補貨", "C. 使用 Redis 原子操作"],
                "en-US": ["A. First come first served (DB Lock)", "B. Both succeed, restock after oversell", "C. Use Redis atomic operations"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "✅ 安全但慢", "1": "⚠️ 商業風險", "2": "✅ 高性能推薦"},
                "en-US": {"0": "✅ Safe but slow", "1": "⚠️ Business risk", "2": "✅ High performance recommended"}
            },
            "trap": "Testing concurrency control capability"
        },
        {
            "text": {
                "zh-TW": "閃購活動 (Flash Sale) 流量瞬間暴增 100倍,數據庫撐不住怎麼辦?",
                "en-US": "Flash Sale traffic surges 100x, database can't handle it, what to do?"
            },
            "category": "performance",
            "options": {
                "zh-TW": ["A. 升級數據庫規格", "B. 引入 Redis 預扣庫存 + 消息隊列", "C. 限流 (Rate Limit)"],
                "en-US": ["A. Upgrade database specs", "B. Introduce Redis pre-deduction + message queue", "C. Rate limiting"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 成本極高且無效", "1": "✅ 標準架構", "2": "✅ 保護系統但犧牲體驗"},
                "en-US": {"0": "⚠️ Extremely costly and ineffective", "1": "✅ Standard architecture", "2": "✅ Protects system but sacrifices UX"}
            },
            "trap": "Testing high concurrency architecture design"
        }
    ],

    # 認證/安全場景 (Auth/Security)
    "authentication": [
        {
            "text": {
                "zh-TW": "用戶連續登入失敗 5 次,你要如何處理?",
                "en-US": "User failed to login 5 times in a row, how should you handle it?"
            },
            "category": "security",
            "options": {
                "zh-TW": ["A. 鎖定帳號 30 分鐘", "B. 要求圖形驗證碼", "C. 不處理"],
                "en-US": ["A. Lock account for 30 minutes", "B. Require CAPTCHA", "C. Do nothing"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "✅ 標準防禦", "1": "✅ 平衡體驗", "2": "⚠️ 暴力破解風險"},
                "en-US": {"0": "✅ Standard defense", "1": "✅ Balanced UX", "2": "⚠️ Brute force risk"}
            },
            "trap": "Testing brute force defense awareness"
        },
        {
            "text": {
                "zh-TW": "JWT Token 被盜用了，服務端能強制讓它失效嗎？",
                "en-US": "If JWT Token is stolen, can the server force it to expire?"
            },
            "category": "security",
            "options": {
                "zh-TW": ["A. 不能，JWT 是無狀態的", "B. 可以，使用 Redis 黑名單機制", "C. 可以，刪除用戶"],
                "en-US": ["A. No, JWT is stateless", "B. Yes, use Redis blacklist", "C. Yes, delete user"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 安全漏洞", "1": "✅ 標準解決方案", "2": "⚠️ 過度反應"},
                "en-US": {"0": "⚠️ Security vulnerability", "1": "✅ Standard solution", "2": "⚠️ Overreaction"}
            },
            "trap": "Testing JWT mechanism understanding"
        },
        {
            "text": {
                "zh-TW": "如果資料庫被 SQL Injection 注入，所有用戶密碼洩漏，後果是什麼？",
                "en-US": "If database is SQL injected and all passwords leaked, what's the consequence?"
            },
            "category": "security",
            "options": {
                "zh-TW": ["A. 密碼是明文，全部完蛋", "B. 密碼有加鹽 Hash，暫時安全但需重置", "C. 只有管理員受影響"],
                "en-US": ["A. Passwords are plaintext, total disaster", "B. Passwords are salted & hashed, temporarily safe but need reset", "C. Only admins affected"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "💀 災難性後果 (未加密)", "1": "✅ 縱深防禦生效", "2": "⚠️ 錯誤認知"},
                "en-US": {"0": "💀 Catastrophic (no encryption)", "1": "✅ Defense in depth works", "2": "⚠️ Wrong assumption"}
            },
            "trap": "Testing password storage security awareness"
        }
    ],

    # 數據一致性 (Data Consistency)
    "data_consistency": [
        {
            "text": {
                "zh-TW": "主資料庫寫入成功但快取更新失敗,如何保證一致性?",
                "en-US": "Database write succeeded but cache update failed, how to ensure consistency?"
            },
            "category": "consistency",
            "options": {
                "zh-TW": ["A. 回滾資料庫", "B. 設定快取過期時間 (TTL)", "C. 無限重試"],
                "en-US": ["A. Rollback database", "B. Set cache TTL", "C. Infinite retry"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 影響性能", "1": "✅ 最終一致性", "2": "⚠️ 可能死鎖"},
                "en-US": {"0": "⚠️ Performance impact", "1": "✅ Eventual consistency", "2": "⚠️ Possible deadlock"}
            },
            "trap": "Testing CAP theorem and eventual consistency"
        },
        {
            "text": {
                "zh-TW": "微服務 A 調用 微服務 B 失敗，如何保證數據不丟失？",
                "en-US": "Microservice A calls microservice B failed, how to prevent data loss?"
            },
            "category": "reliability",
            "options": {
                "zh-TW": ["A. 記錄 Log", "B. 使用消息隊列 (Kafka/RabbitMQ) 重試", "C. 放棄操作"],
                "en-US": ["A. Log it", "B. Use message queue (Kafka/RabbitMQ) for retry", "C. Abandon operation"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 難以自動恢復", "1": "✅ 可靠性設計", "2": "⚠️ 數據丟失"},
                "en-US": {"0": "⚠️ Hard to auto-recover", "1": "✅ Reliability design", "2": "⚠️ Data loss"}
            },
            "trap": "Testing distributed system reliability"
        }
    ],

    # API 集成 (API Integration)
    "api_integration": [
        {
            "text": {
                "zh-TW": "第三方 API 響應時間超過 5 秒,你要如何處理?",
                "en-US": "Third-party API response time exceeds 5 seconds, how to handle?"
            },
            "category": "reliability",
            "options": {
                "zh-TW": ["A. 等待直到超時", "B. Circuit Breaker (熔斷機制)", "C. 返回錯誤"],
                "en-US": ["A. Wait until timeout", "B. Circuit Breaker", "C. Return error"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 雪崩效應風險", "1": "✅ 保護系統", "2": "⚠️ 體驗差"},
                "en-US": {"0": "⚠️ Avalanche effect risk", "1": "✅ Protects system", "2": "⚠️ Poor UX"}
            },
            "trap": "Testing service governance capability"
        },
        {
            "text": {
                "zh-TW": "如何防止惡意用戶重複調用你的 API (Replay Attack)?",
                "en-US": "How to prevent malicious users from replaying your API (Replay Attack)?"
            },
            "category": "security",
            "options": {
                "zh-TW": ["A. 檢查 User-Agent", "B. 使用 Nonce + Timestamp 簽名", "C. 限制 IP"],
                "en-US": ["A. Check User-Agent", "B. Use Nonce + Timestamp signature", "C. Limit IP"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 易被偽造", "1": "✅ 標準防禦", "2": "⚠️ 誤殺無辜"},
                "en-US": {"0": "⚠️ Easy to forge", "1": "✅ Standard defense", "2": "⚠️ False positives"}
            },
            "trap": "Testing API security design"
        }
    ],

    # 隱私保護 (Privacy)
    "privacy": [
        {
            "text": {
                "zh-TW": "日誌 (Log) 中包含用戶的信用卡號，這可以嗎？",
                "en-US": "Logs contain user credit card numbers, is this acceptable?"
            },
            "category": "compliance",
            "options": {
                "zh-TW": ["A. 可以，方便除錯", "B. 不行，必須脫敏 (Masking)", "C. 只有內部人員能看就行"],
                "en-US": ["A. Yes, convenient for debugging", "B. No, must mask sensitive data", "C. OK if only internal staff can see"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "💀 嚴重違規 (PCI-DSS)", "1": "✅ 合規做法", "2": "⚠️ 內部威脅風險"},
                "en-US": {"0": "💀 Serious violation (PCI-DSS)", "1": "✅ Compliant practice", "2": "⚠️ Insider threat risk"}
            },
            "trap": "Testing privacy compliance awareness"
        },
        {
            "text": {
                "zh-TW": "歐盟用戶要求刪除所有數據 (GDPR)，但備份裡還有，怎麼辦？",
                "en-US": "EU user requests data deletion (GDPR), but backups still have it, what to do?"
            },
            "category": "compliance",
            "options": {
                "zh-TW": ["A. 不用管備份", "B. 標記為已刪除，恢復時過濾", "C. 銷毀所有備份"],
                "en-US": ["A. Ignore backups", "B. Mark as deleted, filter on restore", "C. Destroy all backups"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 法律風險", "1": "✅ 可行方案", "2": "⚠️ 不切實際"},
                "en-US": {"0": "⚠️ Legal risk", "1": "✅ Feasible solution", "2": "⚠️ Impractical"}
            },
            "trap": "Testing GDPR compliance handling"
        }
    ],

    # 聊天/通訊場景 (Chat/Messaging)
    "chat": [
        {
            "text": {
                "zh-TW": "如果用戶離線時收到100條訊息，重新上線後如何同步?",
                "en-US": "If user receives 100 messages while offline, how to sync when back online?"
            },
            "category": "performance",
            "options": {
                "zh-TW": ["A. 一次性推送所有訊息", "B. 分批推送 (Pagination)", "C. 只顯示最後一條"],
                "en-US": ["A. Push all messages at once", "B. Batch push (Pagination)", "C. Show only last message"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 卡頓/流量爆炸", "1": "✅ 標準做法", "2": "⚠️ 信息丟失"},
                "en-US": {"0": "⚠️ Lag/traffic explosion", "1": "✅ Standard practice", "2": "⚠️ Message loss"}
            },
            "trap": "Testing real-time messaging sync mechanism"
        },
        {
            "text": {
                "zh-TW": "訊息發送後，對方未讀，發送方刪除了訊息，對方還能看到嗎?",
                "en-US": "Message sent but unread, sender deletes it, can receiver still see it?"
            },
            "category": "consistency",
            "options": {
                "zh-TW": ["A. 能看到 (雙向刪除需特殊處理)", "B. 不能看到 (物理刪除)", "C. 看運氣"],
                "en-US": ["A. Can see (two-way delete needs special handling)", "B. Cannot see (physical delete)", "C. Depends on luck"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "✅ 隱私保護挑戰", "1": "⚠️ 數據找回困難", "2": "⚠️ 不確定性"},
                "en-US": {"0": "✅ Privacy protection challenge", "1": "⚠️ Data recovery difficult", "2": "⚠️ Uncertainty"}
            },
            "trap": "Testing message recall/delete logic"
        }
    ],

    # 預約/排程場景 (Booking)
    "booking": [
        {
            "text": {
                "zh-TW": "兩個用戶同時預約同一時段，系統如何避免衝突？",
                "en-US": "Two users book the same time slot simultaneously, how to avoid conflict?"
            },
            "category": "concurrency",
            "options": {
                "zh-TW": ["A. 先到先得 (Database Constraint)", "B. 候補機制", "C. 人工協調"],
                "en-US": ["A. First come first served (Database Constraint)", "B. Waitlist mechanism", "C. Manual coordination"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "✅ 強一致性", "1": "⚠️ 用戶體驗", "2": "⚠️ 運營成本"},
                "en-US": {"0": "✅ Strong consistency", "1": "⚠️ User experience", "2": "⚠️ Operational cost"}
            },
            "trap": "Testing resource contention handling"
        }
    ],

    # 待辦/任務場景 (Todo)
    "todo": [
        {
            "text": {
                "zh-TW": "刪除父任務時,子任務應該如何處理?",
                "en-US": "When deleting a parent task, how should child tasks be handled?"
            },
            "category": "data_integrity",
            "options": {
                "zh-TW": ["A. 級聯刪除 (Cascade Delete)", "B. 子任務變為獨立任務 (Orphan)", "C. 禁止刪除"],
                "en-US": ["A. Cascade Delete", "B. Child tasks become independent (Orphan)", "C. Prevent deletion"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "✅ 數據清潔", "1": "⚠️ 數據碎片", "2": "⚠️ 僵化"},
                "en-US": {"0": "✅ Clean data", "1": "⚠️ Data fragmentation", "2": "⚠️ Rigidity"}
            },
            "trap": "Testing data relationship integrity"
        },
        {
            "text": {
                "zh-TW": "如果兩個用戶同時編輯同一個任務,如何處理衝突?",
                "en-US": "If two users edit the same task simultaneously, how to handle conflicts?"
            },
            "category": "concurrency",
            "options": {
                "zh-TW": ["A. 最後寫入勝出 (Last Write Wins)", "B. 樂觀鎖 + 版本號檢查", "C. 鎖定編輯 (只允許一人編輯)"],
                "en-US": ["A. Last Write Wins", "B. Optimistic Lock + Version Check", "C. Lock editing (only one user can edit)"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 數據丟失", "1": "✅ 安全且高效", "2": "⚠️ 用戶體驗差"},
                "en-US": {"0": "⚠️ Data loss", "1": "✅ Safe and efficient", "2": "⚠️ Poor UX"}
            },
            "trap": "Testing concurrent editing awareness"
        },
        {
            "text": {
                "zh-TW": "任務列表有 10,000+ 項任務時,如何優化載入速度?",
                "en-US": "With 10,000+ tasks in the list, how to optimize loading speed?"
            },
            "category": "performance",
            "options": {
                "zh-TW": ["A. 一次載入全部 (簡單但慢)", "B. 分頁載入 (Pagination)", "C. 虛擬滾動 (Virtual Scrolling)"],
                "en-US": ["A. Load all at once (simple but slow)", "B. Pagination", "C. Virtual Scrolling"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 瀏覽器崩潰", "1": "✅ 標準做法", "2": "✅ 最佳性能但複雜"},
                "en-US": {"0": "⚠️ Browser crash", "1": "✅ Standard practice", "2": "✅ Best performance but complex"}
            },
            "trap": "Testing performance optimization knowledge"
        }
    ],

    # 前端安全 (Frontend Security)
    "frontend": [
        {
            "text": {
                "zh-TW": "用戶在評論區輸入了 `<script>alert(1)</script>`，會發生什麼？",
                "en-US": "User inputs `<script>alert(1)</script>` in comment section, what happens?"
            },
            "category": "security",
            "options": {
                "zh-TW": ["A. 彈出視窗 (XSS 攻擊成功)", "B. 被轉義顯示為純文本", "C.瀏覽器崩潰"],
                "en-US": ["A. Alert pops up (XSS attack succeeded)", "B. Escaped and displayed as plain text", "C. Browser crashes"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "💀 嚴重漏洞 (XSS)", "1": "✅ 安全編碼", "2": "⚠️ 錯誤認知"},
                "en-US": {"0": "💀 Serious vulnerability (XSS)", "1": "✅ Secure coding", "2": "⚠️ Wrong assumption"}
            },
            "trap": "Testing XSS defense awareness"
        },
        {
            "text": {
                "zh-TW": "API Token 應該存在哪裡最安全？",
                "en-US": "Where should API Token be stored most securely?"
            },
            "category": "security",
            "options": {
                "zh-TW": ["A. LocalStorage", "B. HttpOnly Cookie", "C. JS 變量"],
                "en-US": ["A. LocalStorage", "B. HttpOnly Cookie", "C. JS variable"]
            },
            "risk_analysis": {
                "zh-TW": {"0": "⚠️ 易受 XSS 攻擊", "1": "✅ 防止 XSS 竊取", "2": "⚠️ page refresh 後丟失"},
                "en-US": {"0": "⚠️ Vulnerable to XSS", "1": "✅ Prevents XSS theft", "2": "⚠️ Lost after page refresh"}
            },
            "trap": "Testing frontend storage security"
        }
    ]
}


# ========================================
# 問題生成輔助函數
# ========================================

def localize_question(question: Dict[str, Any], language: str = "en-US") -> Dict[str, Any]:
    """
    將問題本地化為指定語言
    
    Args:
        question: 問題字典
        language: 語言代碼 (zh-TW, en-US)
        
    Returns:
        本地化後的問題
    """
    # 類型檢查:確保 language 是字串
    if not isinstance(language, str):
        language = "en-US"
    
    localized = {
        "category": question["category"],
        "trap": question.get("trap", "")
    }
    
    # 處理 text 字段
    if isinstance(question["text"], dict):
        localized["text"] = question["text"].get(language, question["text"].get("en-US", ""))
    else:
        localized["text"] = question["text"]
    
    # 處理 options 字段
    if isinstance(question["options"], dict):
        localized["options"] = question["options"].get(language, question["options"].get("en-US", []))
    else:
        localized["options"] = question["options"]
    
    # 處理 risk_analysis 字段
    if isinstance(question["risk_analysis"], dict):
        # 檢查是否為雙語結構
        if "zh-TW" in question["risk_analysis"] or "en-US" in question["risk_analysis"]:
            localized["risk_analysis"] = question["risk_analysis"].get(language, question["risk_analysis"].get("en-US", {}))
        else:
            localized["risk_analysis"] = question["risk_analysis"]
    else:
        localized["risk_analysis"] = question["risk_analysis"]
    
    return localized


def get_questions_by_category(category: str, language: str = "en-US") -> List[Dict[str, Any]]:
    """
    根據類別和語言獲取問題
    
    Args:
        category: 問題類別 (payment, inventory, authentication, etc.)
        language: 語言代碼 (zh-TW, en-US)
        
    Returns:
        本地化後的問題列表
    """
    questions = QUESTION_LIBRARY.get(category, [])
    return [localize_question(q, language) for q in questions]


def get_random_questions(count: int = 5, language: str = "en-US") -> List[Dict[str, Any]]:
    """
    隨機獲取指定數量的問題
    
    Args:
        count: 問題數量
        language: 語言代碼 (zh-TW, en-US)
        
    Returns:
        本地化後的問題列表
    """
    import random
    
    all_questions = []
    for questions in QUESTION_LIBRARY.values():
        all_questions.extend(questions)
    
    selected = random.sample(all_questions, min(count, len(all_questions)))
    return [localize_question(q, language) for q in selected]


def get_questions_for_module(module_name: str, module_description: str, language: str = "en-US") -> List[Dict[str, Any]]:
    """
    根據模組名稱和描述智能選擇問題
    
    Args:
        module_name: 模組名稱
        module_description: 模組描述
        language: 語言代碼 (zh-TW, en-US)
        
    Returns:
        本地化後的相關問題列表
    """
    text = (module_name + " " + module_description).lower()
    
    selected_questions = []
    
    # 根據關鍵詞匹配問題類別
    if any(kw in text for kw in ['付款', '支付', 'payment', '交易']):
        selected_questions.extend(get_questions_by_category('payment', language))
    
    if any(kw in text for kw in ['庫存', 'inventory', '商品', '購物']):
        selected_questions.extend(get_questions_by_category('inventory', language))
    
    if any(kw in text for kw in ['登入', '認證', 'auth', '用戶', 'user']):
        selected_questions.extend(get_questions_by_category('authentication', language))
    
    if any(kw in text for kw in ['數據', 'data', '快取', 'cache']):
        selected_questions.extend(get_questions_by_category('data_consistency', language))
    
    if any(kw in text for kw in ['api', '接口', '第三方', 'integration']):
        selected_questions.extend(get_questions_by_category('api_integration', language))
    
    # 如果沒有匹配,返回隨機問題
    if not selected_questions:
        selected_questions = get_random_questions(5, language)
    
    return selected_questions[:5]  # 最多返回 5 個問題


# ========================================
# 問題質量評估
# ========================================

def evaluate_question_quality(question: Dict[str, Any]) -> Dict[str, Any]:
    """
    評估問題質量
    
    Args:
        question: 問題字典
        
    Returns:
        評估結果
    """
    score = 0
    feedback = []
    
    # 檢查必要字段
    required_fields = ['text', 'category', 'options', 'risk_analysis']
    for field in required_fields:
        if field in question:
            score += 25
        else:
            feedback.append(f"缺少必要字段: {field}")
    
    # 檢查選項數量
    if 'options' in question and len(question['options']) >= 3:
        feedback.append("✅ 選項數量充足")
    else:
        feedback.append("⚠️ 選項數量不足 (建議 3-4 個)")
        score -= 10
    
    # 檢查風險分析
    if 'risk_analysis' in question:
        if all(key in question['risk_analysis'] for key in ['0', '1', '2']):
            feedback.append("✅ 風險分析完整")
        else:
            feedback.append("⚠️ 風險分析不完整")
            score -= 10
    
    return {
        "score": max(0, score),
        "feedback": feedback,
        "quality": "優秀" if score >= 90 else "良好" if score >= 70 else "需改進"
    }


if __name__ == "__main__":
    # 測試問題庫
    print("=" * 70)
    print("🧪 蘇格拉底式問題庫測試")
    print("=" * 70)
    print()
    
    # 測試各類別問題數量
    print("📊 問題庫統計:")
    total = 0
    for category, questions in QUESTION_LIBRARY.items():
        count = len(questions)
        total += count
        print(f"  - {category:20s}: {count} 個問題")
    print(f"\n  總計: {total} 個問題")
    print()
    
    # 測試智能選擇
    print("🎯 智能問題選擇測試:")
    test_modules = [
        ("付款系統", "處理用戶付款和訂單"),
        ("庫存管理", "管理商品庫存"),
        ("用戶認證", "處理用戶登入和權限")
    ]
    
    for name, desc in test_modules:
        questions = get_questions_for_module(name, desc)
        print(f"\n  模組: {name}")
        print(f"  匹配到 {len(questions)} 個問題:")
        for q in questions[:2]:  # 只顯示前2個
            print(f"    - {q['text'][:50]}...")
    
    print()
    print("✅ 問題庫測試完成!")
