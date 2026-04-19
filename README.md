# 🤖 AI Chatbot — Flask + Groq + LLaMA3

> A real AI chatbot with a beautiful web UI built with Python Flask + Groq API (FREE).

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat&logo=flask&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Free%20API-orange?style=flat)
![CI](https://github.com/YOUR_USERNAME/flask-chatbot/actions/workflows/ci.yml/badge.svg)

---

## 📁 Project Structure

```
flask-chatbot/
├── app.py                         ← Flask server (START HERE)
├── chatbot.py                     ← Groq AI logic
├── config.py                      ← Your API key (hidden from GitHub)
├── config.example.py              ← Safe template on GitHub
├── requirements.txt               ← flask + groq
├── test_app.py                    ← Tests
├── .gitignore                     ← Hides config.py
├── templates/
│   └── index.html                 ← Beautiful chat UI
└── .github/
    └── workflows/
        └── ci.yml                 ← Auto-runs tests on every push
```

---

## ▶️ HOW TO RUN IN VS CODE — Step by Step

### Step 1 — Get Free Groq API Key
1. Go to 👉 **https://console.groq.com**
2. Sign up with Google
3. Click **API Keys → Create API Key**
4. Copy the key (starts with `gsk_...`)

### Step 2 — Open folder in VS Code
```
File → Open Folder → select flask-chatbot folder
```

### Step 3 — Open terminal in VS Code
```
Terminal → New Terminal   (or Ctrl + `)
```

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Add API key to config.py
Open `config.py` and paste your key:
```python
GROQ_API_KEY = "gsk_your_real_key_here"
```

### Step 6 — Run tests
```bash
python test_app.py
```

### Step 7 — Start the server!
```bash
python app.py
```

### Step 8 — Open in browser
```
http://localhost:5000
```
Your chatbot UI is live! 🎉

---

## 🚀 HOW TO PUSH TO GITHUB FROM SCRATCH

### Step 1 — Create repo on GitHub
1. Go to **https://github.com**
2. Click **New** (green button, top left)
3. Repository name: `flask-chatbot`
4. Set to **Public**
5. ❌ Do NOT check "Add README" (we have one)
6. Click **Create repository**

### Step 2 — Open VS Code terminal in your project folder

```bash
# Check you are in the right folder (should show your files)
ls
# Should show: app.py  chatbot.py  config.py  templates/  etc.
```

### Step 3 — Initialize Git
```bash
git init
```

### Step 4 — Stage all files
```bash
git add .
```

### Step 5 — Check what will be pushed (optional but good habit)
```bash
git status
# config.py should NOT appear here (hidden by .gitignore) ✅
```

### Step 6 — Commit
```bash
git commit -m "feat: Add Flask AI Chatbot with Groq API"
```

### Step 7 — Connect to GitHub
```bash
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/flask-chatbot.git
```

### Step 8 — Push!
```bash
git branch -M main
git push -u origin main
```

### Step 9 — Verify on GitHub
Go to `https://github.com/YOUR_USERNAME/flask-chatbot`
You should see all your files there ✅
config.py should NOT be there ✅ (hidden safely)

---

## 🔄 Every Time You Make Changes

```bash
# After changing any file:
git add .
git commit -m "update: Improve chatbot responses"
git push
```
GitHub Actions (CI/CD) will automatically run your tests! ✅

---

## 📋 Git Commit Message Examples

```bash
git commit -m "feat: Add Flask chatbot UI"
git commit -m "fix: Fix error handling in chatbot.py"
git commit -m "update: Add more quick suggestions"
git commit -m "docs: Update README"
git commit -m "test: Add more test cases"
```

---

## ✅ What Gets Pushed to GitHub

| File | Pushed? | Why |
|------|---------|-----|
| app.py | ✅ Yes | Main server |
| chatbot.py | ✅ Yes | Bot logic |
| config.py | ❌ NO | Has your secret API key |
| config.example.py | ✅ Yes | Safe template |
| templates/index.html | ✅ Yes | Chat UI |
| requirements.txt | ✅ Yes | Dependencies |
| test_app.py | ✅ Yes | Tests |
| .gitignore | ✅ Yes | Hides config.py |
| .github/workflows/ci.yml | ✅ Yes | CI/CD pipeline |

---

⭐ Star this repo if you found it useful!
