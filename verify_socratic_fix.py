
import asyncio
from socratic_generator import layer4_fallback, normalize_question_format

# Mock requirement to trigger fallback
req = "Ecommerce system using Bitcoin"
lang = "zh-TW"

# Test Layer 4 Fallback (Fusion Mode)
print("Testing Layer 4 Fallback...")
res = layer4_fallback(req, lang)
questions = res.get("questions", [])

if not questions:
    print("❌ No questions generated.")
else:
    q1 = questions[0]
    options = q1.get("options", [])
    if options and isinstance(options[0], dict):
        print("✅ Options are properly normalized to objects.")
        print(f"   Sample Option Label: {options[0].get('label')}")
        print(f"   Sample Risk Score: {options[0].get('risk_score')}")
    else:
        print("❌ Options are still strings!")
        print(f"   Sample: {options[0] if options else 'None'}")

# Test Manual Normalization Logic
print("\nTesting Manual Normalization...")
legacy_q = {
    "text": "Legacy Question",
    "options": ["A. Opt1", "B. Opt2"],
    "risk_analysis": {"0": "Risk1", "1": "Risk2"}
}
norm_q = normalize_question_format(legacy_q)
if isinstance(norm_q["options"][0], dict) and norm_q["options"][0]["risk_score"] == "Risk1":
    print("✅ Normalization logic works.")
else:
    print("❌ Normalization logic failed.")
