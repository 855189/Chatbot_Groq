"""
=====================================
  test_app.py — Tests
  Run: python test_app.py
=====================================
"""

import config

passed = 0
failed = 0


def test(description, condition):
    global passed, failed
    if condition:
        print(f"  ✅ PASS — {description}")
        passed += 1
    else:
        print(f"  ❌ FAIL — {description}")
        failed += 1


print("\n🧪 Running Tests...\n")
print("─" * 40)

# ── Test 1: Config ─────────────────────────
print("📦 Test Group 1: Config")
test("GROQ_API_KEY exists",          hasattr(config, 'GROQ_API_KEY'))
test("GROQ_API_KEY is string",       isinstance(config.GROQ_API_KEY, str))
test("GROQ_API_KEY not empty",       len(config.GROQ_API_KEY) > 0)
test("GROQ_API_KEY changed",         config.GROQ_API_KEY != "paste-your-groq-api-key-here")
test("MODEL_NAME is set",            len(config.MODEL_NAME) > 0)
test("SYSTEM_PROMPT is set",         len(config.SYSTEM_PROMPT) > 10)

# ── Test 2: Imports ────────────────────────
print("\n📦 Test Group 2: Imports")
try:
    import flask
    test("flask installed", True)
except ImportError:
    test("flask installed ← RUN: pip install flask", False)

try:
    import groq
    test("groq installed", True)
except ImportError:
    test("groq installed ← RUN: pip install groq", False)

try:
    from chatbot import GeminiChatbot
    test("chatbot.py imports OK", True)
except Exception as e:
    test(f"chatbot.py imports — ERROR: {e}", False)

try:
    from app import app
    test("app.py imports OK", True)
except Exception as e:
    test(f"app.py imports — ERROR: {e}", False)

# ── Test 3: Flask Routes ───────────────────
print("\n🌐 Test Group 3: Flask Routes")
try:
    from app import app
    client = app.test_client()

    res = client.get('/')
    test("GET / returns 200", res.status_code == 200)
    test("HTML page loads", b'Chatbot' in res.data or b'chatbot' in res.data.lower())

except Exception as e:
    test(f"Flask routes — ERROR: {e}", False)

# ── Test 4: Live API ───────────────────────
print("\n🤖 Test Group 4: Live Groq API")
if config.GROQ_API_KEY == "paste-your-groq-api-key-here":
    print("  ⏭️  SKIPPED — Add your Groq API key in config.py")
    print("  👉 Get free key: https://console.groq.com")
else:
    try:
        from app import app
        client = app.test_client()

        import json
        res = client.post('/chat',
            data=json.dumps({"message": "Say hello"}),
            content_type='application/json'
        )
        data = json.loads(res.data)
        test("POST /chat returns 200",     res.status_code == 200)
        test("Response has 'response' key", 'response' in data)
        test("Response is not empty",      len(data.get('response', '')) > 0)
        print(f"\n  📨 Sample: '{data.get('response','')[:60]}'")

    except Exception as e:
        test(f"Live API — ERROR: {e}", False)

# ── Results ────────────────────────────────
print("\n" + "─" * 40)
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")
print(f"📊 Total  : {passed + failed}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED!")
    print("▶️  Run: python app.py")
    print("🌐 Open: http://localhost:5000")
elif config.GROQ_API_KEY == "paste-your-groq-api-key-here":
    print("\n👉 Add your Groq API key in config.py")
    print("👉 Get free key: https://console.groq.com")
else:
    print("\n⚠️  Fix the failed tests above.")
print("─" * 40 + "\n")
