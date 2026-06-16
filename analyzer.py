from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def clean_json(text: str):
    """Extract JSON even if LLM adds extra text"""
    text = text.strip()

    # remove code blocks
    text = text.replace("```json", "").replace("```", "")

    # extract JSON block only
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)

    return text


def analyze_document(text):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""
You are an AI document analyzer.

Return ONLY valid JSON. No explanation. No markdown.

STRICT FORMAT:
{{
  "document_type": "Resume | Invoice | Other",
  "summary": "2-3 sentence summary",
  "important_information": [
    {{"key": "Name", "value": "..."}},
    {{"key": "Role", "value": "..."}},
    {{"key": "Experience", "value": "..."}},
    {{"key": "Skills", "value": "..."}}
  ],
  "entities": [
    {{"entity_type": "Person", "entity_name": "..."}},
    {{"entity_type": "Role", "entity_name": "..."}},
    {{"entity_type": "Skill", "entity_name": "..."}}
  ]
}}

DOCUMENT:
{text}
"""
            }
        ],
        temperature=0
    )

    raw = response.choices[0].message.content
    raw = clean_json(raw)

    try:
        return json.loads(raw)
    except Exception:
        return {
            "error": "Failed to parse model output",
            "raw_output": raw
        }