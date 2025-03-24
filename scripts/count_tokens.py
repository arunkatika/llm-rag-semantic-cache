# scripts/count_tokens.py

from transformers import AutoTokenizer

# Load tokenizer for Nomic embedding model
tokenizer = AutoTokenizer.from_pretrained("nomic-ai/nomic-embed-text-v1.5")

def count_tokens(text: str) -> int:
    """Counts tokens using the Nomic embedding tokenizer."""
    tokens = tokenizer.tokenize(text)
    return len(tokens)
