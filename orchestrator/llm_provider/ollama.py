# orchestrator/llm_provider/ollama.py

import ollama
from .base import LLMProvider

class OllamaProvider(LLMProvider):
    def chat(self, prompt: str, system_prompt: str = "") -> str:
        response = ollama.chat(
            model='llama3:latest',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        return response['message']['content']
