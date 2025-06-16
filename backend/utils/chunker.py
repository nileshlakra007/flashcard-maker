from typing import List
import nltk

nltk.download('punkt', quiet=True)

nltk.download("punkt_tab", quiet=True)

def split_text_into_chunks(text: str, max_tokens: int = 200) -> List[str]:
    """Simple chunking by sentences using nltk."""
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = []
    token_count = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        if token_count + len(words) > max_tokens and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            token_count = 0
        current_chunk.append(sentence)
        token_count += len(words)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks
