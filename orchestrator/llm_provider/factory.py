# orchestrator/llm_provider/factory.py

import os
from .ollama import OllamaProvider
# from .openai import OpenAIProvider (add later)

def get_llm_provider():
    provider = os.getenv("OSMIGO_LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        return OllamaProvider()
    # elif provider == "openai":
    #     return OpenAIProvider()

    raise ValueError(f"Unsupported LLM provider: {provider}")
