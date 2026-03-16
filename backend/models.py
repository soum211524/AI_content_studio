from pydantic import BaseModel


class GenerateRequest(BaseModel):
    topic: str
    template: str
    tone: str
    audience: str
    length: int


class RewriteRequest(BaseModel):
    text: str
    mode: str


class PlagiarismRequest(BaseModel):
    text: str