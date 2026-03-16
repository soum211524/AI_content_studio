from groq import Groq

client = Groq(
    api_key="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"
)

def rewrite_content(text, mode):

    prompt = f"""
You are an expert writing assistant.

Rewrite the following text according to the requested mode.

Mode: {mode}

Available modes:
- Simplify
- Professional
- Marketing
- Expand
- Shorten

Text:
{text}

Instructions:
Keep the original meaning but improve the writing according to the selected mode.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content