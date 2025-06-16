import pdfplumber
from typing import List


def extract_text_from_pdf(filepath: str) -> str:
    """Extracts text from a PDF file."""
    text_parts: List[str] = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts)
