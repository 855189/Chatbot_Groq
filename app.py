"""
=====================================
  app.py — Flask Web Server
  Run: python app.py
  Opens in browser: http://localhost:5000
=====================================
"""

from flask import Flask, render_template, request, jsonify
from chatbot import GeminiChatbot

app = Flask(__name__)
bot = GeminiChatbot()


@app.route("/")
def home():
    """Serve the main chat page."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please type a message!"})

    if not bot.ready:
        return jsonify({"response": "❌ Bot not connected. Check your API key in config.py"})

    response = bot.chat(user_message)
    return jsonify({"response": response})


@app.route("/clear", methods=["POST"])
def clear():
    bot.clear_history()
    return jsonify({"status": "cleared"})


@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": bot.conversation_history})


if __name__ == "__main__":
    print("\n" + "="*50)
    print("  🤖 AI Chatbot — Flask + Groq")
    print("  🌐 Open browser: http://localhost:5000")
    print("  🛑 Press Ctrl+C to stop")
    print("="*50 + "\n")
    app.run(debug=True)