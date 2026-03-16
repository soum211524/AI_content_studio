from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
import os

router = APIRouter()



class ChatMessage(BaseModel):
    role: str          # "user" or "assistant"
    content: str

class DostChatRequest(BaseModel):
    message: str
    history: List[ChatMessage] = []   # full conversation so far (excluding current message)

class DostChatResponse(BaseModel):
    reply: str

# ── LangChain setup ────────────────────────────────────────────────────────


GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.7,
    max_tokens=1024,
)

# Custom system prompt for Dost AI — a friendly, knowledgeable content assistant
SYSTEM_PROMPT = """You are Dost AI, a warm, knowledgeable, and slightly witty AI writing companion built into content.io — an AI-powered content generation platform.

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

# LangChain prompt template with message history
prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{message}"),
])

chain = prompt_template | llm

# ── Endpoint ───────────────────────────────────────────────────────────────

@router.post("/dost/chat", response_model=DostChatResponse)
async def dost_chat(data: DostChatRequest):
    # Convert history from request format to LangChain message objects
    lc_history = []
    for msg in data.history:
        if msg.role == "user":
            lc_history.append(HumanMessage(content=msg.content))
        elif msg.role == "assistant":
            lc_history.append(AIMessage(content=msg.content))

    # Invoke the chain
    response = await chain.ainvoke({
        "history": lc_history,
        "message": data.message,
    })

    return DostChatResponse(reply=response.content)
