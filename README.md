# Content Studio AI

> AI-powered content studio — generate, rewrite, SEO optimize & chat with your writing companion.

Built with **FastAPI + Groq LLaMA 3.3 70B + LangChain** on the backend and a clean vanilla HTML/CSS/JS frontend. No frameworks, no bloat — just a fast, professional writing platform.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Generate** | Create content using 15 templates — blogs, LinkedIn, YouTube scripts, Instagram reels, email newsletters, startup pitches, and more |
| **Rewrite** | Transform existing content with 6 modes: Simplify, Professional, Marketing, Expand, Shorten, Formal |
| **Plagiarism Check** | Analyze originality with an animated similarity score and verdict |
| **SEO Optimizer** | SEO score + feedback, meta title/description generator, and full article outline builder |
| **Dost AI** | Conversational AI writing companion with full chat history, powered by LangChain + Groq |
| **History** | Auto-saved generation history with localStorage + backend sync |

---

## 🛠 Tech Stack

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) — Python web framework
- [Groq](https://groq.com/) — LLaMA 3.3 70B inference (blazing fast)
- [LangChain](https://www.langchain.com/) — Dost AI chat chain with memory
- Pydantic — request validation

**Frontend**
- Vanilla HTML, CSS, JavaScript — zero dependencies
- Playfair Display + DM Sans + DM Mono — typography
- Fully responsive, dark-background editorial design

---

## 📁 Project Structure

```
content-studio-ai/
├── backend/
│   ├── main.py               # FastAPI app + all endpoints
│   ├── models.py             # Pydantic request models
│   ├── requirements.txt
│   ├── generator.py      # Content generation logic
│   |── rewriter.py       # Rewrite logic
│   │── plagiarism.py     # Plagiarism scoring
│   
└── frontend/
    └── index.html            # Entire frontend — single file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Groq API key](https://console.groq.com/) (free)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/content-studio-ai.git
cd content-studio-ai
```

### 2. Set up the backend

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Start the server:

```bash
uvicorn main:app --reload
```

Backend runs at `http://127.0.0.1:8000`

### 3. Open the frontend

Just open `frontend/index.html` in your browser. No build step needed.

> Make sure the backend is running first — the frontend connects to `http://127.0.0.1:8000` by default.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/generate` | Generate content |
| `POST` | `/rewrite` | Rewrite content |
| `POST` | `/plagiarism` | Check originality |
| `POST` | `/seo/score` | SEO score + suggestions |
| `POST` | `/seo/meta` | Meta title + description |
| `POST` | `/seo/outline` | Article outline |
| `POST` | `/dost/chat` | Dost AI chat |
| `GET` | `/history` | Fetch generation history |



## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Built with

- [Groq Console](https://console.groq.com/) — for the free LLaMA API
- [LangChain](https://www.langchain.com/) — for Dost AI chat memory
- [FastAPI](https://fastapi.tiangolo.com/) — for the backend
- Playfair Display from Google Fonts — for the editorial aesthetic
Taking longer than usual. Trying again shortly (attempt 5)


