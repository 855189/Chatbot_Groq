"""
=====================================
  chatbot.py — Groq Chatbot Brain
=====================================
"""

from groq import Groq
from datetime import datetime
import config


class GeminiChatbot:
    def __init__(self):
        self.ready = False
        self.conversation_history = []
        self.client = None
        self._initialize()

    def _initialize(self):
        """Connect to Groq API."""
        try:
            if not config.GROQ_API_KEY or config.GROQ_API_KEY.strip() == "" or "paste" in config.GROQ_API_KEY.lower():
                print("\n⚠️  ERROR: Add your Groq API key in config.py")
                print("👉 Get free key at: https://console.groq.com\n")
                return

            self.client = Groq(api_key=config.GROQ_API_KEY.strip())

            # Test the connection with a real API call
            self.client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=5
            )

            print("✅ Connected to Groq AI successfully!")
            self.ready = True

        except Exception as e:
            print(f"\n❌ Failed to connect: {e}\n")
            self.ready = False

    def chat(self, user_message: str) -> str:
        """Send message to Groq, get response."""
        try:
            self.conversation_history.append({
                "role": "user",
                "message": user_message,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            messages = [{"role": "system", "content": config.SYSTEM_PROMPT}]

            for entry in self.conversation_history[-config.MAX_HISTORY:]:
                role = "assistant" if entry["role"] == "bot" else "user"
                messages.append({"role": role, "content": entry["message"]})

            response = self.client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=messages,
                temperature=config.TEMPERATURE,
                max_tokens=500
            )

            bot_reply = response.choices[0].message.content.strip()

            self.conversation_history.append({
                "role": "bot",
                "message": bot_reply,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            if len(self.conversation_history) > config.MAX_HISTORY * 2:
                self.conversation_history = self.conversation_history[-(config.MAX_HISTORY * 2):]

            return bot_reply

        except Exception as e:
            error_msg = str(e)
            if "invalid_api_key" in error_msg.lower() or "401" in error_msg:
                return "❌ Invalid API key. Check config.py"
            elif "rate_limit" in error_msg.lower() or "429" in error_msg:
                return "⚠️ Too many requests. Wait a few seconds and try again."
            elif "decommissioned" in error_msg.lower():
                return "❌ Model outdated. Change MODEL_NAME in config.py"
            else:
                return f"❌ Error: {error_msg}"

    def clear_history(self):
        self.conversation_history = []