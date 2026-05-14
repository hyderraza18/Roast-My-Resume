from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def roast_resume(text: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a brutally honest, savage but funny resume reviewer. Always reply in pure JSON only, no markdown, no backticks."
            },
            {
                "role": "user",
                "content": f"""Rate this resume 0-100 and roast it.

Resume:
{text[:3000]}

Reply ONLY in this JSON format:
{{
  "score": <integer 0-100>,
  "opening": "<brutal one-liner>",
  "strengths": ["<point 1>", "<point 2>"],
  "weaknesses": ["<point 1>", "<point 2>", "<point 3>"],
  "roast_lines": ["<funny line>", "<funny line>", "<funny line>"],
  "advice": "<single most important fix>"
}}Scoring: 0-30=disaster, 31-50=bad, 51-70=mediocre, 71-85=decent, 86-95=good, 96-100=exceptional
"""
            }
        ]
    )
    return json.loads(response.choices[0].message.content.strip())



