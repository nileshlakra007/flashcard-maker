import os
from typing import List, Tuple
import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

PROMPT_TEMPLATE = (
    "You are a helpful AI study assistant. Read the following content and "
    "generate concise flashcards in Q&A format for revision. "
    "Be accurate, use simple language, and avoid duplicates.\n\nCONTENT:\n{chunk}"
)


def generate_flashcards(chunk: str) -> List[Tuple[str, str]]:
    """Send a chunk to OpenAI API and parse flashcards."""
    if not OPENAI_API_KEY:
        raise RuntimeError("OpenAI API key not configured")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(chunk=chunk)}],
    )
    text = response.choices[0].message.content
    flashcards = []
    for line in text.splitlines():
        if ':' in line:
            question, answer = line.split(':', 1)
            flashcards.append((question.strip(), answer.strip()))
    return flashcards
