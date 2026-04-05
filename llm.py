import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_review(text):
    prompt = f"""
You are an AI that analyzes product reviews.

Return ONLY in JSON format:
{{
  "sentiment": "Positive or Negative",
  "score": "1-10",
  "summary": "One-line summary"
}}

Review: {text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content
    return json.loads(content)