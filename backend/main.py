from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os

# Request models
from models import GenerateRequest, RewriteRequest, PlagiarismRequest

# AI Engines
from generator import generate_content
from rewriter import rewrite_content
from plagiarism import plagiarism_score

# LangChain + Groq — Dost AI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# DOST AI

class ChatMessage(BaseModel):
    role: str       
    content: str

class DostChatRequest(BaseModel):
    message: str
    history: List[ChatMessage] = []

class DostChatResponse(BaseModel):
    reply: str




llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="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",
    temperature=0.7,
    max_tokens=1024,
)

DOST_SYSTEM_PROMPT = """You are Dost AI, a warm, knowledgeable, and slightly witty AI writing companion built into content.io — an AI-powered content generation platform.

Your personality:
- Friendly and approachable, like a trusted colleague ("dost" means friend in Hindi/Urdu)
- Concise but never curt — you give complete, useful answers without padding
- Deeply knowledgeable about content writing, copywriting, SEO, social media, storytelling, and marketing
- You speak in plain English. No jargon unless the user uses it first.
- You remember the conversation context and refer back to it naturally

Your capabilities:
- Help users brainstorm ideas for blogs, social media, scripts, emails, product descriptions, and more
- Critique and improve drafts users share with you
- Explain writing techniques, content strategy, SEO principles
- Give feedback on tone, structure, and clarity
- Suggest templates, formats, and frameworks for any content type
- Answer questions about the content.io platform features (Generate, Rewrite, Plagiarism Check, History)

Rules:
- Never pretend to be a human
- If asked something outside content/writing/marketing, gently redirect
- Keep responses focused — if a user pastes a long draft, give specific, actionable feedback
- Always end complex advice with a concrete next step or example
"""

dost_prompt = ChatPromptTemplate.from_messages([
    ("system", DOST_SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{message}"),
])

dost_chain = dost_prompt | llm


@app.get("/")
def home():
    return {"message": "AI Content Generator Studio Backend Running"}


# --------------------------------
# CONTENT GENERATION
# --------------------------------
@app.post("/generate")
def generate(data: GenerateRequest):
    result = generate_content(
        data.topic,
        data.template,
        data.tone,
        data.audience,
        data.length
    )
    return {"generated_content": result}



# Rewrite

@app.post("/rewrite")
def rewrite(data: RewriteRequest):
    result = rewrite_content(
        data.text,
        data.mode
    )
    return {"rewritten_text": result}


# --------------------------------
# PLAGIARISM CHECK
# --------------------------------
@app.post("/plagiarism")
def plagiarism(data: PlagiarismRequest):
    score = plagiarism_score(data.text)
    return {"similarity_score": score}


# --------------------------------
# SEO — models
# --------------------------------
class SeoScoreRequest(BaseModel):
    keyword: str
    content: str

class SeoMetaRequest(BaseModel):
    topic: str
    keyword: str = ""
    description: str = ""

class SeoOutlineRequest(BaseModel):
    topic: str
    keyword: str = ""
    audience: str = ""
    article_type: str = "how-to guide"


SEO_SYSTEM_PROMPT = """You are an expert SEO strategist and content analyst. You return ONLY valid JSON — no markdown fences, no explanation, just the raw JSON object."""


def call_groq_json(user_prompt: str) -> str:
    from langchain_core.messages import HumanMessage as HM, SystemMessage as SM
    msgs = [SM(content=SEO_SYSTEM_PROMPT), HM(content=user_prompt)]
    resp = llm.invoke(msgs)
    return resp.content


# --------------------------------
# SEO — Score & Feedback
# --------------------------------
@app.post("/seo/score")
def seo_score(data: SeoScoreRequest):
    import json, re
    prompt = f"""Analyze this content for SEO quality. Target keyword: "{data.keyword}"

Content:
{data.content[:3000]}

Return JSON with this exact shape:
{{
  "score": <integer 0-100>,
  "verdict": "<Poor|Needs Work|Good|Excellent>",
  "summary": "<one sentence overall assessment>",
  "suggestions": [
    {{"status": "<ok|warn|err>", "title": "<short label>", "detail": "<actionable advice>"}},
    ...
  ]
}}

Evaluate: keyword presence in first 100 words, keyword density (ideal 1-2%), content length, readability, heading structure signals, meta-readiness, LSI/related terms, call to action presence. Provide 6-8 suggestions."""

    raw = call_groq_json(prompt)
    raw = re.sub(r"```json|```", "", raw).strip()
    return json.loads(raw)


# --------------------------------
# SEO — Meta Generator
# --------------------------------
@app.post("/seo/meta")
def seo_meta(data: SeoMetaRequest):
    import json, re
    prompt = f"""Generate SEO-optimized meta tags for this page.

Topic: {data.topic}
Target keyword: {data.keyword or "not specified"}
Context: {data.description or "not provided"}

Return JSON with this exact shape:
{{
  "meta_title": "<compelling title, 50-60 chars, includes keyword>",
  "meta_description": "<engaging description, 140-155 chars, includes keyword and CTA>",
  "keywords": ["<keyword1>", "<keyword2>", "<keyword3>", "<keyword4>", "<keyword5>"]
}}

Rules: title must be under 60 chars, description under 160 chars, both must feel natural not stuffed."""

    raw = call_groq_json(prompt)
    raw = re.sub(r"```json|```", "", raw).strip()
    return json.loads(raw)


# --------------------------------
# SEO — Article Outline
# --------------------------------
@app.post("/seo/outline")
def seo_outline(data: SeoOutlineRequest):
    import json, re
    prompt = f"""Create a full SEO-optimized article outline.

Topic: {data.topic}
Primary keyword: {data.keyword or "not specified"}
Target audience: {data.audience or "general readers"}
Article type: {data.article_type}

Return JSON with this exact shape:
{{
  "outline": [
    {{"level": "H1", "heading": "<main title with keyword>", "tip": "<SEO tip for this section>"}},
    {{"level": "H2", "heading": "<section heading>", "tip": "<keyword or LSI term to include>"}},
    {{"level": "H3", "heading": "<sub-section>", "tip": ""}},
    ...
  ]
}}

Include: 1 H1, 5-7 H2s, 2-3 H3s under key H2s. Each H2 tip should name a specific keyword or LSI term to naturally include. H1 tip should be the primary SEO strategy note."""

    raw = call_groq_json(prompt)
    raw = re.sub(r"```json|```", "", raw).strip()
    return json.loads(raw)


# --------------------------------
# DOST AI
# --------------------------------
@app.post("/dost/chat", response_model=DostChatResponse)
async def dost_chat(data: DostChatRequest):
    # Convert history to LangChain message objects
    lc_history = []
    for msg in data.history:
        if msg.role == "user":
            lc_history.append(HumanMessage(content=msg.content))
        elif msg.role == "assistant":
            lc_history.append(AIMessage(content=msg.content))

    response = await dost_chain.ainvoke({
        "history": lc_history,
        "message": data.message,
    })

    return DostChatResponse(reply=response.content)