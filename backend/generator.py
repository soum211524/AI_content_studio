from groq import Groq
from templates import templates

client = Groq(api_key="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")

def generate_content(topic, template, tone, audience, length):

    template_prompt = templates.get(template)

    prompt = f"""
{template_prompt}

Topic: {topic}
Tone: {tone}
Audience: {audience}
Length: {length} words
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content