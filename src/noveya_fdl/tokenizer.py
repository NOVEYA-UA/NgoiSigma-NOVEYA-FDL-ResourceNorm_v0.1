TOKENS = {
    "TIME": "Σ::Δ+::NORMA::TIME",
    "ENERGY": "Σ::Δ+::NORMA::ENERGY",
    "MEMORY": "Σ::Δ+::NORMA::MEMORY",
    "ATTN": "Σ::Δ+::NORMA::ATTN",
    "FLOW": "Σ::Δ+::NORMA::FLOW"
}

def tokenize_norm(resource_type: str) -> str:
    key = resource_type.upper()
    return TOKENS.get(key, f"Σ::Δ+::NORMA::{key}")
