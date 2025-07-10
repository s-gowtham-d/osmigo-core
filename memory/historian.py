# memory/historian.py

import os
import json
from datetime import datetime

LOG_DIR = "logs"
INTERACTIONS_LOG = os.path.join(LOG_DIR, "interactions.jsonl")
METRICS_LOG = os.path.join(LOG_DIR, "system_metrics.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)

def log_interaction(prompt, steps):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "steps": steps
    }
    with open(INTERACTIONS_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

def log_system_metrics(data):
    data["timestamp"] = datetime.utcnow().isoformat()
    with open(METRICS_LOG, "a") as f:
        f.write(json.dumps(data) + "\n")
