# 🤖 AI Projects & Productive Tools

A collection of beginner-friendly Python AI and utility scripts — including a Groq-powered chatbot and a live weather forecasting bot.

---

## 📁 Project Structure

```
AI/
├── chatbot2.py      # AI chatbot powered by Groq (LLaMA 3.1)
├── new.py           # Weather report fetcher (v2, clean version)
├── weather.py       # Weather forecasting bot using wttr.in
├── .env             # API keys (NOT pushed to GitHub — gitignored)
├── .gitignore       # Excludes .env from git tracking
└── README.md        # This file
```

---

## 🚀 Projects Overview

### 1. `chatbot2.py` — AI Chatbot (Groq + LLaMA 3.1)
A terminal-based chatbot that uses the **Groq API** with the `llama-3.1-8b-instant` model.

**Features:**
- Sends user messages to the LLaMA 3.1 model via Groq
- Loops continuously until you type `exit`, `bye`, or `quit`

**How to run:**
```bash
pip install groq
python chatbot2.py
```

> ⚠️ Set your Groq API key in a `.env` file or directly in the script.

---

### 2. `weather.py` — Weather Forecasting Bot
A simple CLI tool that fetches live weather reports using [wttr.in](https://wttr.in).

**How to run:**
```bash
pip install requests
python weather.py
```

---

### 3. `new.py` — Weather Report Fetcher (v2)
An improved version of the weather tool with better error handling.

**How to run:**
```bash
pip install requests
python new.py
```

---

## 🛠️ How This Project Was Pushed to GitHub

> The full story of what happened when pushing to GitHub — including the problem and how it was fixed.

### ❌ Problem: GitHub Blocked the Push (Secret Detection)

When attempting to push with `git push origin main`, GitHub's **Push Protection** blocked it:

```
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote:
remote: - GITHUB PUSH PROTECTION
remote:   Resolve the following violations before pushing again
remote:
remote:     - Push cannot contain secrets
remote:
remote:       —— Groq API Key ——————————————————————
remote:        locations:
remote:          - commit: 3a2657bd...   path: .env:1
remote:          - commit: 7191f899...   path: .gitignore:1
remote:          - commit: 3e1084a3...   path: chatbot2.py:2
```

**Why?** Old commits in git history still contained a real Groq API key, even though `.env` was later added to `.gitignore`. Git never forgets — deleted files still live in the commit history.

---

### ✅ Solution: Rewrite History with a Fresh Orphan Branch

Instead of trying to scrub individual commits, we created a **brand new git history** with zero old commits (called an "orphan branch"), staged only the clean files, and force-pushed it as the new `main`.

---

### 📋 Commands Used (Step by Step)

#### Step 1 — Check project status and remote
```bash
git status
# Output: On branch main, nothing to commit, working tree clean

git remote -v
# Output: origin  https://github.com/praveen0-100/AI-projects-and-productive-proj.git (fetch/push)
```

#### Step 2 — Try pushing (this FAILED due to secret detection)
```bash
git push origin main
# BLOCKED by GitHub Push Protection — Groq API key found in old commits
```

#### Step 3 — Create an orphan branch (zero commit history)
```bash
git checkout --orphan fresh-start
# Switched to a new branch 'fresh-start'
# This branch has NO history — completely fresh slate
```

#### Step 4 — Stage only the clean files (exclude .env)
```bash
git add .gitignore chatbot2.py new.py weather.py
# .env is excluded because it's listed in .gitignore
```

#### Step 5 — Make the first clean commit
```bash
git commit -m "Initial commit - AI projects (chatbot, weather tools)"
# [fresh-start (root-commit) d273b47] Initial commit - AI projects (chatbot, weather tools)
# 4 files changed, 55 insertions(+)
```

#### Step 6 — Force push the clean branch as main
```bash
git push origin fresh-start:main --force
# To https://github.com/praveen0-100/AI-projects-and-productive-proj.git
# * [new branch]   fresh-start -> main   ✅ SUCCESS
```

#### Step 7 — Switch local branch back to main and clean up
```bash
git checkout -B main fresh-start
# Switched to and reset branch 'main'

git branch -d fresh-start
# Deleted branch fresh-start (was d273b47)
```

---

### 🔐 Security Notes

- `.env` is listed in `.gitignore` — it will **never** be pushed to GitHub.
- The old Groq API key that was exposed in previous commits has been wiped from history.
- **Rotate your Groq API key** at [console.groq.com](https://console.groq.com) since it was previously exposed.

---

## 📦 Requirements

```bash
pip install groq requests
```

---

## 🔗 Repository

**GitHub:** [https://github.com/praveen0-100/AI-projects-and-productive-proj](https://github.com/praveen0-100/AI-projects-and-productive-proj)

---

## 👤 Author

**Praveen Prabakaran**  
GitHub: [@praveen0-100](https://github.com/praveen0-100)
