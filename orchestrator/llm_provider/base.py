# orchestrator/llm_provider/base.py

from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def chat(self, prompt: str, system_prompt: str = "") -> str:
        pass
