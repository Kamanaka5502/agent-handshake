import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def think(request):
    prompt = f"""
You are an AI agent.

The system is asking whether to perform this action:

Action: {request.action}
Required role: {request.required_role}
Allowed modes: {request.allowed_modes}

Explain what you would do and why.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message["content"]
