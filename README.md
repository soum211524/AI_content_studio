# ✦ Content Studio AI

<div align="center">

**An intelligent, all-in-one AI writing platform for creators, marketers & founders.**

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-orange?style=for-the-badge)

</div>

---

## What is this?

**Content Studio AI** is a full-stack AI writing platform that puts six powerful tools under one roof — a content generator, a rewrite engine, an originality checker, an SEO suite, a conversational AI companion, and a generation history vault. No subscriptions. No bloat. Just you and your words, powered by one of the fastest LLMs on the planet.

---

## ✦ Features

### 📝 Content Generator
Generate production-ready content across **15 templates** in seconds. Choose your tone, set your audience, define the word count — and let the model do the heavy lifting.

> Supports: Blog Intro · Twitter Thread · LinkedIn Post · Product Description · YouTube Script · Instagram Caption · Instagram Story · Instagram Reel Script · Facebook Post · Email Newsletter · SEO Meta Description · Podcast Intro · Motivational Quote · Startup Pitch · Research Paper

### ✏️ Rewrite Engine
Transform existing content into something sharper, cleaner, or completely different — without losing the core idea. Six rewrite modes cover every use case.

> Modes: Simplify · Professional · Marketing · Expand · Shorten · Formal

### 🔍 Plagiarism Checker
Paste any content and get an instant originality score with a visual similarity meter. Know exactly where you stand before you publish.

### 📈 SEO Optimizer
A complete three-part SEO suite built right into the platform:
- **SEO Score & Feedback** — animated score ring + 6–8 actionable suggestions with pass/warn/fail badges
- **Meta Generator** — AI-generated meta title and description with a live Google SERP preview and character counters
- **Article Outline** — full H1/H2/H3 structure with per-section LSI keyword tips, ready to copy

### 🤖 Dost AI
A conversational AI writing companion (dost = friend in Hindi/Urdu) built with LangChain. Ask anything — content strategy, copywriting tips, draft feedback, platform advice. Full multi-turn memory, typing indicators, quick-start prompts.

### 🗂️ History
Every generation is saved automatically. Browse and reload past content from the sidebar or the full history archive. Syncs with the backend.

---

## ✦ Tech Stack

```
Frontend    Vanilla HTML · CSS · JavaScript   (zero dependencies, zero build step)
Backend     FastAPI · Python 3.10+
LLM         Groq — LLaMA 3.3 70B Versatile   (fastest inference available)
AI Chain    LangChain · LangChain-Groq
Typography  Playfair Display · DM Sans · DM Mono
Storage     localStorage (client) · JSON (server)
```

---

## ✦ Project Structure

```
content-studio-ai/
│
├── backend/
│   ├── main.py                  # All FastAPI routes & Dost AI chain
│   ├── models.py                # Pydantic request/response models
│   ├── requirements.txt
│   ├── ai/
│   │   ├── generator.py         # Content generation logic
│   │   ├── rewriter.py          # Rewrite engine
│   │   └── plagiarism.py        # Originality scoring
│   └── storage/
│       └── history.json         # Persistent generation history
│
└── frontend/
    └── index.html               # Entire UI — one file, no framework
```

---

## ✦ Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com)

### 1. Clone

```bash
git clone https://github.com/yourusername/content-studio-ai.git
cd content-studio-ai
```

### 2. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure environment

Create a `.env` file inside `/backend`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Start the backend

```bash
uvicorn main:app --reload
```

API is live at `http://127.0.0.1:8000`

### 5. Open the frontend

Open `frontend/index.html` directly in your browser. No server, no build, no config.

---

## ✦ API Reference

| Method | Endpoint | Purpose |
|:---:|---|---|
| `GET` | `/` | Health check |
| `POST` | `/generate` | Generate content |
| `POST` | `/rewrite` | Rewrite content |
| `POST` | `/plagiarism` | Originality check |
| `POST` | `/seo/score` | SEO score + suggestions |
| `POST` | `/seo/meta` | Meta title & description |
| `POST` | `/seo/outline` | Article outline |
| `POST` | `/dost/chat` | Dost AI conversation |
| `GET` | `/history` | Fetch generation history |

### Request Examples

**Generate content**
```json
POST /generate
{
  "topic": "The future of AI in healthcare",
  "template": "blog_intro",
  "tone": "Professional",
  "audience": "Healthcare founders",
  "length": 300
}
```

**Dost AI chat**
```json
POST /dost/chat
{
  "message": "Give me 5 hooks for a LinkedIn post about burnout",
  "history": []
}
```

**SEO score**
```json
POST /seo/score
{
  "keyword": "AI content marketing",
  "content": "Your article text here..."
}
```

---

## ✦ Environment Variables

| Variable | Required | Description |
|---|:---:|---|
| `GROQ_API_KEY` | ✅ | Your Groq API key — get one free at console.groq.com |

---

## ✦ License

MIT — free to use, fork, and build on.

---

<div align="center">

Made with ✦ and way too much coffee.

</div>
