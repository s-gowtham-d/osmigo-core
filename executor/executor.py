# executor/executor.py
import subprocess

def dry_run(command: str):
    print(f"[Dry Run] Would execute: {command}")

def execute(command: str):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            print("[Output]:", result.stdout)
        if result.stderr:
            print("[Error]:", result.stderr)
    except Exception as e:
        print("[Execution Error]:", str(e))
