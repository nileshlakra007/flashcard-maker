from typing import List, Tuple
import pandas as pd


def save_csv(flashcards: List[Tuple[str, str]], filepath: str) -> None:
    df = pd.DataFrame(flashcards, columns=["question", "answer"])
    df.to_csv(filepath, index=False)
