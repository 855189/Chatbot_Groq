"""
config.example.py — Safe template for GitHub
Copy this → rename to config.py → add your key

Get free Groq key: https://console.groq.com
"""

GROQ_API_KEY = "paste-your-groq-api-key-here"
MODEL_NAME   = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """
You are a friendly helpful AI assistant named GemBot.
Keep responses concise and conversational.
"""

MAX_HISTORY  = 10
TEMPERATURE  = 0.7
