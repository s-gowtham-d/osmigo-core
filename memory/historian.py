import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("memory/history.jsonl")

def log_interaction(prompt: str, steps: list[str], approved: list[str]):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "steps": steps,
            "approved": approved
        }, f)
        f.write("\n")
