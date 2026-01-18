"""
Antigravity 內聯問題生成器
在 Antigravity 環境中直接生成蘇格拉底問題，無需外部 AI 調用
"""

import re
from typing import Dict, List


def generate_questions_inline(requirement: str, language: str = 'zh-TW') -> dict:
    """
    根據需求智能生成災難導向問題
    
    🎯 真正智能化：根據複雜度動態調整問題數量 (1-5個)
    讓每個有需求的人都能得到最適合的問題
    """
    
    # 🚨 BlueMouse Interception Logic (The "Blue Alert")
    # This matches the marketing claim: "It asked the deadly question BEFORE I pressed Enter"
    destructive_patterns = [
        r'drop\s+table', 
        r'delete\s+from', 
        r'truncate\s+table',
        r'remove\s+database'
    ]
    
    if any(re.search(p, requirement, re.IGNORECASE) for p in destructive_patterns):
        # 這是文案中提到的 "Blue Alert"
        print("\033[94m[BlueMouse] 🛑 Analyzing potential destructive command...\033[0m")
        
        # 根據語言選擇對應的文字
        is_chinese = language == 'zh-TW'
        
        return {
            "questions": [{
                "id": "critical_stop",
                "text": "⚠️ CRITICAL STOP: You are executing DROP without Environment Check. Is this PROD? (你正在執行刪除指令。你確定這不是正式環境嗎？)" if is_chinese else "⚠️ CRITICAL STOP: You are executing DROP without Environment Check. Is this PROD?",
                "options": [
                    {
                        "label": "A. No, it's Prod (攔截)" if is_chinese else "A. No, it's Prod (Block)",
                        "description": "立即停止執行,保護正式環境" if is_chinese else "Stop execution immediately to protect production",
                        "risk_score": "安全" if is_chinese else "Safe",
                        "value": "block"
                    },
                    {
                        "label": "B. Yes, it's Dev (放行)" if is_chinese else "B. Yes, it's Dev (Proceed)",
                        "description": "確認是開發環境,允許執行" if is_chinese else "Confirm it's development environment, allow execution",
                        "risk_score": "高風險" if is_chinese else "High Risk",
                        "value": "proceed"
                    }
                ],
                "type": "critical_alert",
                "risk_analysis": "高風險操作攔截" if is_chinese else "High Risk Operation Blocked"
            }]
        }

    # 1. 分析需求複雜度
    from requirement_complexity_analyzer import analyze_requirement_complexity
    
    complexity_info = analyze_requirement_complexity(requirement)
    question_count = complexity_info['question_count']
    detected_scenarios = complexity_info['scenarios']
    
    print(f"  🎯 複雜度分析: 分數={complexity_info['complexity_score']}, 問題數={question_count}")
    
    # 🚨 強制檢測 Crypto 場景 (Override)
    if re.search(r'bitcoin|btc|eth|crypto|區塊鏈|比特幣|加密貨幣|錢包|交易所', requirement, re.IGNORECASE):
        if 'crypto' not in detected_scenarios:
            detected_scenarios.insert(0, 'crypto')
            
    print(f"  🔍 檢測場景: {detected_scenarios}")
    
    # 正規化需求
    req_lower = requirement.lower()
    
    # 場景匹配
    scenarios = {
        '部落格|blog|post|cms|內容管理': 'blog',
        '電商|購物|訂單|商品|庫存|ecommerce|shop|cart|order': 'ecommerce',
        '預約|預訂|排程|日曆|booking|calendar|schedule': 'booking',
        '聊天|即時通訊|訊息|社交|chat|message|social': 'chat',
        '待辦|任務|todo|gtd|list|task': 'todo',
        '視頻|影片|直播|媒體|video|stream|media': 'video',
        '支付|金流|交易|錢包|payment|wallet|transaction': 'payment',
        '加密貨幣|比特幣|區塊鏈|crypto|bitcoin|btc|eth|blockchain': 'crypto',
        '用戶|會員|帳號|user|auth|login|register': 'user_auth',
        '搜尋|檢索|查詢|search|query|find': 'search',
        '文件|檔案|上傳|儲存|file|upload|storage': 'file_storage',
    }
    
    detected_scenario = None
    for pattern, scenario in scenarios.items():
        if re.search(pattern, req_lower):
            detected_scenario = scenario
            break
            
    # If no match, check generic
    if not detected_scenario:
        detected_scenario = 'generic'

    # 2. 根據場景和複雜度生成問題
    
    # 優先使用內置的特定生成器 (因為它們包含與 Code Generator 對應的 value 邏輯)
    # 這裡引用下方定義的函數，Python runtime 支持
    questions_map = {
        'blog': generate_blog_questions,
        'booking': generate_booking_questions,
        'todo': generate_todo_questions,
        'video': generate_video_questions,
        'search': generate_search_questions,
        'file_storage': generate_file_storage_questions,
        'ecommerce': generate_ecommerce_questions,
        'chat': generate_chat_questions,
        'payment': generate_payment_questions,
        'user_auth': generate_user_auth_questions,
        'crypto': generate_crypto_questions,
        'generic': generate_generic_questions,
    }

    scenario_mapping = {
        'blog': 'blog', '部落格': 'blog',
        'ecommerce': 'inventory', '電商': 'inventory',
        'payment': 'payment', '支付': 'payment',
        'user_auth': 'authentication', 'authentication': 'authentication', '會員': 'authentication', '用戶': 'authentication',
        'chat': 'chat', '聊天': 'chat',
        'booking': 'booking', '預約': 'booking',
        'todo': 'todo', '待辦': 'todo',
        'api': 'api_integration', 'privacy': 'privacy', 'security': 'security', 
        'frontend': 'frontend', 'data': 'data_consistency',
        'Web3': 'payment',
        'crypto': 'crypto', 'bitcoin': 'crypto', 'btc': 'crypto', '區塊鏈': 'crypto',
    }

    target_scenarios = detected_scenarios if detected_scenarios else [detected_scenario]
    primary_key = target_scenarios[0]
    primary_scenario = scenario_mapping.get(primary_key, primary_key)
    
    # 特殊處理 Ecommerce -> inventory, 但我們想要 ecommerce generator
    if primary_key in ['ecommerce', '電商']:
        primary_scenario = 'ecommerce'

    # 1. 嘗試 Internal Generators
    if primary_scenario in questions_map:
        generator = questions_map[primary_scenario]
        result = generator(requirement, language)
        if result and result.get('questions'):
             print(f"  ✨ 生成了 {len(result['questions'])} 個問題 (Internal Generator: {primary_scenario})")
             return result

    # 2. 如果 Internal Failed, 嘗試 QUESTION_LIBRARY (Legacy/Fallback)
    from socratic_questions_library import get_questions_for_module, get_random_questions, QUESTION_LIBRARY
    result = {"questions": []}
    all_questions = []
    
    
    for sc in target_scenarios:
        lib_key = scenario_mapping.get(sc, sc)
        if sc in ['ecommerce', '電商']:
            if 'inventory' in QUESTION_LIBRARY: all_questions.extend(QUESTION_LIBRARY['inventory'])
            if 'payment' in QUESTION_LIBRARY: all_questions.extend(QUESTION_LIBRARY['payment'])
            continue
        if lib_key in QUESTION_LIBRARY:
            all_questions.extend(QUESTION_LIBRARY[lib_key])
            
    if all_questions:
        import random
        seen = set()
        unique_questions = []
        for q in all_questions:
             # Handle both dict (internal) and string options (library)
             text = q.get('text', '')
             if text not in seen:
                seen.add(text)
                unique_questions.append(q)
        random.shuffle(unique_questions)
        result['questions'] = unique_questions[:max(question_count, 3)]
        print(f"  ✨ 生成了 {len(result['questions'])} 個問題 (Library)")
    else:
        # Final Fallback
        generator = generate_generic_questions
        result = generator(requirement, language)
        print(f"  ✨ 生成了 {len(result.get('questions', []))} 個問題 (Generic)")
        
    return result


# ===== 各場景問題生成器 =====

def generate_blog_questions(requirement: str, language: str) -> dict:
    """部落格系統問題"""
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_blog_draft_recovery",
                    "type": "single_choice",
                    "text": "如果作者正在編輯文章時突然斷線或當機，未保存的內容該如何處理？",
                    "options": [
                        {
                            "label": "A. 每30秒自動保存草稿",
                            "description": "內容不會丟失，但會產生大量冗餘版本，佔用儲存空間。",
                            "risk_score": "儲存空間浪費",
                            "value": "auto_save"
                        },
                        {
                            "label": "B. 僅在手動保存時儲存",
                            "description": "節省空間，但用戶容易忘記保存，斷線時所有內容丟失。",
                            "risk_score": "高數據丟失風險",
                            "value": "manual_save"
                        },
                        {
                            "label": "C. 使用瀏覽器 localStorage 暫存",
                            "description": "體驗好，但有5MB容量限制，隱私模式下不可用。",
                            "risk_score": "容量限制，隱私問題",
                            "value": "localstorage"
                        }
                    ]
                },
                {
                    "id": "q2_blog_spam",
                    "type": "single_choice",
                    "text": "如果部落格每秒收到數百條垃圾留言攻擊，系統如何防禦？",
                    "options": [
                        {
                            "label": "A. 所有評論需人工審核",
                            "description": "最安全，但嚴重延遲顯示，降低用戶互動意願。",
                            "risk_score": "用戶體驗極差",
                            "value": "manual_review"
                        },
                        {
                            "label": "B. AI 自動過濾",
                            "description": "高效，但可能誤刪正常評論，引發用戶抱怨。",
                            "risk_score": "誤殺率10-20%",
                            "value": "ai_filter"
                        },
                        {
                            "label": "C. IP速率限制（每分鐘3條）",
                            "description": "簡單有效，但無法防禦分散式攻擊，誤傷共用IP用戶。",
                            "risk_score": "誤傷正常用戶",
                            "value": "rate_limit"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_blog_questions_en(requirement, language)


def generate_ecommerce_questions(requirement: str, language: str) -> dict:
    """電商系統問題"""
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_ecommerce_inventory",
                    "type": "single_choice",
                    "text": "如果商品庫存只剩1件，但2個用戶幾乎同時下單，系統該如何處理？",
                    "options": [
                        {
                            "label": "A. 悲觀鎖：只讓第一個下單",
                            "description": "絕對不會超賣，但高流量時用戶需排隊，體驗差。",
                            "risk_score": "高並發性能差",
                            "value": "pessimistic_lock"
                        },
                        {
                            "label": "B. 樂觀鎖：讓兩個都下單，後取消一個",
                            "description": "性能好，但被取消的用戶會不滿，可能流失。",
                            "risk_score": "用戶體驗衝突",
                            "value": "optimistic_lock"
                        },
                        {
                            "label": "C. 預留庫存：下單時先鎖定，15分鐘內付款",
                            "description": "平衡性能與體驗，但可能被惡意佔用庫存。",
                            "risk_score": "庫存佔用攻擊",
                            "value": "reserve_inventory"
                        }
                    ]
                },
                {
                    "id": "q2_ecommerce_payment",
                    "type": "single_choice",
                    "text": "如果用戶付款成功，但支付回調失敗（網絡問題），訂單狀態錯誤怎麼辦？",
                    "options": [
                        {
                            "label": "A. 定期輪詢支付平台核對",
                            "description": "最可靠，但增加系統負載，且有延遲。",
                            "risk_score": "延遲5-10分鐘",
                            "value": "polling"
                        },
                        {
                            "label": "B. 依賴支付平台重試回調",
                            "description": "零負載，但如果平台也失敗，就永遠不會更新。",
                            "risk_score": "數據不一致風險",
                            "value": "rely_callback"
                        },
                        {
                            "label": "C. 人工介入處理異常訂單",
                            "description": "準確率100%，但人力成本高，處理慢。",
                            "risk_score": "人力成本高",
                            "value": "manual_fix"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_ecommerce_questions_en(requirement, language)


def generate_booking_questions(requirement: str, language: str) -> dict:
    """預約系統問題"""
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_booking_conflict",
                    "type": "single_choice",
                    "text": "如果2個用戶同時預約同一時段，系統如何避免衝突？",
                    "options": [
                        {
                            "label": "A. 先到先得，鎖定時段",
                            "description": "公平簡單，但高峰期很多用戶會預約失敗。",
                            "risk_score": "用戶滿意度低",
                            "value": "first_come"
                        },
                        {
                            "label": "B. 候補機制，自動遞補",
                            "description": "最大化利用率，但候補通知延遲，用戶可能錯過。",
                            "risk_score": "通知不及時",
                            "value": "waitlist"
                        },
                        {
                            "label": "C. 彈性時段，建議替代時間",
                            "description": "降低衝突，但用戶可能不接受替代時段。",
                            "risk_score": "用戶接受度低",
                            "value": "flexible_slot"
                        }
                    ]
                },
                {
                    "id": "q2_booking_no_show",
                    "type": "single_choice",
                    "text": "如果用戶預約後爽約（no-show），浪費服務資源，如何應對？",
                    "options": [
                        {
                            "label": "A. 收取訂金，爽約不退款",
                            "description": "有效減少爽約，但可能嚇跑新用戶，降低轉化率。",
                            "risk_score": "轉化率下降20%",
                            "value": "deposit"
                        },
                        {
                            "label": "B. 信用評分制，多次爽約限制預約",
                            "description": "懲罰慣犯，但初犯用戶可能因一次意外被誤判。",
                            "risk_score": "誤傷正常用戶",
                            "value": "credit_score"
                        },
                        {
                            "label": "C. 提前24小時提醒，可免費取消",
                            "description": "用戶體驗好，但仍有20%爽約率，資源浪費。",
                            "risk_score": "20%資源浪費",
                            "value": "reminder_only"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_booking_questions_en(requirement, language)


def generate_chat_questions(requirement: str, language: str) -> dict:
    """聊天系統問題"""
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_chat_offline",
                    "type": "single_choice",
                    "text": "如果用戶離線時收到100條訊息，重新上線後如何同步？",
                    "options": [
                        {
                            "label": "A. 一次性推送所有訊息",
                            "description": "最完整，但可能導致UI卡頓，流量爆炸。",
                            "risk_score": "UI卡頓，流量消耗大",
                            "value": "push_all"
                        },
                        {
                            "label": "B. 分批推送，每次10條",
                            "description": "流暢，但用戶需等待多次載入，體驗不連貫。",
                            "risk_score": "體驗不連貫",
                            "value": "batch_push"
                        },
                        {
                            "label": "C. 只顯示摘要+未讀數，用戶主動查看",
                            "description": "節省流量，但用戶可能錯過重要訊息。",
                            "risk_score": "錯過重要訊息",
                            "value": "summary_only"
                        }
                    ]
                },
                {
                    "id": "q2_chat_delivery",
                    "type": "single_choice",
                    "text": "如果訊息發送時網絡不穩定，如何確保送達？",
                    "options": [
                        {
                            "label": "A. 無限重試直到成功",
                            "description": "送達率100%，但可能產生重複訊息，且耗電。",
                            "risk_score": "重複訊息，耗電",
                            "value": "infinite_retry"
                        },
                        {
                            "label": "B. 重試3次後標記為失敗",
                            "description": "節能，但用戶需手動重發，體驗差。",
                            "risk_score": "用戶體驗差",
                            "value": "limited_retry"
                        },
                        {
                            "label": "C. 背景持續重試，但不阻塞UI",
                            "description": "體驗好，但實現複雜，可能有狀態不一致。",
                            "risk_score": "狀態同步複雜",
                            "value": "background_retry"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_chat_questions_en(requirement, language)


def generate_todo_questions(requirement: str, language: str) -> dict:
    """待辦清單問題"""
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_todo_delete",
                    "type": "single_choice",
                    "text": "如果用戶刪除了一個包含10個子任務的父任務，系統應該如何處理？",
                    "options": [
                        {
                            "label": "A. 連同子任務一起刪除",
                            "description": "邏輯清晰，但用戶可能誤刪重要子任務。",
                            "risk_score": "意外數據丟失",
                            "value": "cascade_delete"
                        },
                        {
                            "label": "B. 只刪除父任務，子任務變成獨立任務",
                            "description": "保留數據，但可能產生大量孤兒任務，難管理。",
                            "risk_score": "數據混亂",
                            "value": "orphan_children"
                        },
                        {
                            "label": "C. 刪除前強制確認，並支持撤銷",
                            "description": "最安全，但多一步操作，降低效率。",
                            "risk_score": "操作繁瑣",
                            "value": "confirm_undo"
                        }
                    ]
                },
                {
                    "id": "q2_todo_sync",
                    "type": "single_choice",
                    "text": "如果用戶在手機和電腦同時編輯同一任務，如何解決衝突？",
                    "options": [
                        {
                            "label": "A. 最後寫入者獲勝",
                            "description": "實現簡單，但先編輯的內容會被覆蓋。",
                            "risk_score": "數據丟失",
                            "value": "last_write_wins"
                        },
                        {
                            "label": "B. 提示用戶手動合併",
                            "description": "保證不丟失，但需要用戶理解技術概念，門檻高。",
                            "risk_score": "用戶體驗差",
                            "value": "manual_merge"
                        },
                        {
                            "label": "C. 智能合併（如附加而非覆蓋）",
                            "description": "體驗好，但邏輯複雜，可能產生奇怪結果。",
                            "risk_score": "合併錯誤",
                            "value": "auto_merge"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_todo_questions_en(requirement, language)


def generate_generic_questions(requirement: str, language: str) -> dict:
    """通用問題（未匹配到具體場景）"""
    # 簡單提取關鍵詞作為上下文 (取前10個字，避免過長)
    context = requirement[:15] + "..." if len(requirement) > 15 else requirement
    
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_concurrency",
                    "type": "single_choice",
                    "text": f"如果您的「{context}」突然爆紅，同時有 10萬人湧入，您希望系統如何反應？",
                    "options": [
                        {
                            "label": "A. 悲觀鎖：保證數據絕不出錯，但用戶需排隊等待",
                            "description": "絕對安全，適合金融或高價資源，但體驗較慢。",
                            "risk_score": "低風險，高延遲",
                            "value": "pessimistic"
                        },
                        {
                            "label": "B. 樂觀鎖：優先讓用戶操作，衝突時再提示重試",
                            "description": "體驗流暢，適合大多數應用，但在極端併發下會有失敗率。",
                            "risk_score": "高風險，低延遲",
                            "value": "optimistic"
                        },
                        {
                            "label": "C. 使用 Redis 高速緩存抗壓",
                            "description": "極快，能承載巨大流量，但增加架構複雜度。",
                            "risk_score": "依賴外部服務",
                            "value": "redis"
                        }
                    ]
                },
                {
                    "id": "q2_data_growth",
                    "type": "single_choice",
                    "text": f"隨著「{context}」運行一段時間，數據量達到 1000萬筆時，您最擔心什麼？",
                    "options": [
                        {
                            "label": "A. 查詢變慢：即使是簡單的搜索也要幾秒鐘",
                            "description": "需要提前規劃索引 (Index) 和讀寫分離。",
                            "risk_score": "性能瓶頸",
                            "value": "perf_degradation"
                        },
                        {
                            "label": "B. 數據安全：擔心被駭客竊取或勒索",
                            "description": "需要加強加密和備份機制。",
                            "risk_score": "安全風險",
                            "value": "security_breach"
                        },
                        {
                            "label": "C. 維護成本：伺服器費用過高",
                            "description": "需要考慮冷熱數據分離或歸檔策略。",
                            "risk_score": "成本失控",
                            "value": "high_cost"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_generic_questions_en(requirement, language)


# ===== 英文版本 =====


def generate_blog_questions_en(requirement: str, language: str) -> dict:
    """Blog System Questions (English)"""
    return {
        "questions": [
            {
                "id": "q1_blog_draft_recovery",
                "type": "single_choice",
                "options": [{"value": "auto_save"}, {"value": "manual_save"}, {"value": "localstorage"}]
            }
        ]
    }

def generate_ecommerce_questions_en(requirement: str, language: str) -> dict:
    return {"questions": []}

def generate_booking_questions_en(requirement: str, language: str) -> dict:
    return generate_generic_questions_en(requirement, language)

def generate_chat_questions_en(requirement: str, language: str) -> dict:
    return generate_generic_questions_en(requirement, language)

def generate_todo_questions_en(requirement: str, language: str) -> dict:
    return generate_generic_questions_en(requirement, language)

def generate_generic_questions_en(requirement: str, language: str) -> dict:
    return {"questions": []}


# ===== 其他場景 =====

def generate_video_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_payment_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_user_auth_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_search_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_file_storage_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_crypto_questions(requirement: str, language: str) -> dict:
    """加密貨幣系統問題"""
    if language == 'zh-TW':
        return {
            "questions": [
                {
                    "id": "q1_crypto_conf",
                    "type": "single_choice",
                    "text": "比特幣區塊確認需要 10 分鐘，用戶付款後要讓他等多久？",
                    "options": [
                        {
                            "label": "A. 0 確認 (Zero Confirmation)",
                            "description": "用戶體驗極佳，秒級反應。但面臨 Double Spending (雙花) 攻擊風險。",
                            "risk_score": "資金損失風險",
                            "value": "zero_conf"
                        },
                        {
                            "label": "B. 等待 1 個區塊 (約 10 分鐘)",
                            "description": "基本安全。但用戶要在頁面上發呆 10 分鐘，轉換率會掉。",
                            "risk_score": "用戶流失",
                            "value": "one_conf"
                        },
                        {
                            "label": "C. 閃電網絡 (Lightning Network)",
                            "description": "秒級到帳且安全。但技術開發難度極高，且用戶需有閃電錢包。",
                            "risk_score": "開發門檻極高",
                            "value": "lightning"
                        }
                    ]
                },
                {
                    "id": "q2_crypto_custody",
                    "type": "single_choice",
                    "text": "用戶的私鑰 (Private Key) 誰來管？",
                    "options": [
                        {
                            "label": "A. 託管錢包 (Custodial)",
                            "description": "平台代管，體驗好。但平台被駭就全沒了。",
                            "risk_score": "極高資安風險",
                            "value": "custodial"
                        },
                        {
                            "label": "B. 用戶自管 (Non-Custodial)",
                            "description": "用戶自己記助記詞。安全，但忘記密碼無法找回。",
                            "risk_score": "客服地獄",
                            "value": "non_custodial"
                        }
                    ]
                }
            ]
        }
    else:
        return generate_generic_questions_en(requirement, language)

def generate_video_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_payment_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_user_auth_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_search_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)

def generate_file_storage_questions(requirement: str, language: str) -> dict:
    return generate_generic_questions(requirement, language)


def generate_mixed_scenario_questions(scenarios: List[str], count: int, language: str) -> dict:
    """
    多場景混合問題生成
    
    當檢測到多個場景時，從每個場景中選取最核心的問題
    """
    all_questions = []
    
    # 場景優先級
    scenario_map = {
        '部落格': 'blog',
        '電商': 'ecommerce',
        '預約': 'booking',
        '聊天': 'chat',
        '支付': 'payment',
        '會員': 'user_auth',
    }
    
    generators = {
        'blog': generate_blog_questions,
        'ecommerce': generate_ecommerce_questions,
        'booking': generate_booking_questions,
        'chat': generate_chat_questions,
        'user_auth': generate_user_auth_questions,
    }
    
    # 從每個場景收集第一個問題
    for scenario in scenarios[:count]:
        scenario_key = scenario_map.get(scenario)
        if scenario_key and scenario_key in generators:
            gen = generators[scenario_key]
            result = gen('', language)
            if 'questions' in result and len(result['questions']) > 0:
                # 取第一個最重要的問題
                all_questions.append(result['questions'][0])
    
    # 補充到目標數量
    while len(all_questions) < count and len(all_questions) < 5:
        # 從第二優先級問題補充
        for scenario in scenarios[:count]:
            if len(all_questions) >= count:
                break
            scenario_key = scenario_map.get(scenario)
            if scenario_key and scenario_key in generators:
                gen = generators[scenario_key]
                result = gen('', language)
                if 'questions' in result and len(result['questions']) > 1:
                    all_questions.append(result['questions'][1])
        break  # 避免無限循環
    
    return {
        'questions': all_questions[:count]
    }

