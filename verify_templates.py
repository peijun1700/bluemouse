
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from socratic_generator import detect_category, layer4_fallback

def test_detection():
    test_cases = [
        ("我要做一個購物網站", "ecommerce"),
        ("Build a crypto wallet", "fintech"),
        ("Social media app for dogs", "social"),
        ("Netflix clone", "content"),
        ("Enterprise ERP system", "saas"),
        ("Just a simple todo list", "default")
    ]
    
    print("🧪 Testing Category Detection...")
    for req, expected in test_cases:
        result = detect_category(req)
        status = "✅" if result == expected else f"❌ (Got {result})"
        print(f"  {status} Input: '{req}' -> {expected}")

def test_generation():
    print("\n🧪 Testing Question Generation (Layer 4)...")
    
    # Test Fintech
    req = "I want a bitcoin exchange"
    print(f"  Input: {req}")
    result = layer4_fallback(req, "zh-TW")
    q_text = result['questions'][0]['text']
    print(f"  -> Generated Question: {q_text}")
    
    if "轉帳" in q_text or "Network Partition" in q_text:
         print("  ✅ Correctly loaded Fintech templates")
    else:
         print("  ❌ Failed to load Fintech templates")

if __name__ == "__main__":
    test_detection()
    test_generation()
