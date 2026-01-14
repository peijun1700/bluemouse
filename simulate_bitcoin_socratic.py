
import asyncio
import json
from socratic_generator import layer4_fallback, normalize_question_format, load_knowledge_base

# Ensure KB is loaded
load_knowledge_base()

req = "我要做一個比特幣電商交易平台，支持高併發秒殺"
lang = "zh-TW"

print(f"🤖 模擬輸入: {req}")
res = layer4_fallback(req, lang)
questions = res.get("questions", [])

# Normalize (simulating the fix)
questions = [normalize_question_format(q) for q in questions]

print(f"\n✅ 生成了 {len(questions)} 個蘇格拉底問題：\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['text']}")
    print(f"   (類別: {q.get('category', 'unknown')})")
    for opt in q.get('options', []):
        print(f"   - [{opt.get('risk_score')}] {opt.get('label')}")
        # print(f"     預測後果: {opt.get('description')}")
    print("-" * 50)
