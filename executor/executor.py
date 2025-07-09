import subprocess

def dry_run(command: str):
    print(f"[Dry Run] Would execute: {command}")

def execute(command: str):
    subprocess.run(command, shell=True)
