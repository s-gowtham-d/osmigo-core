# cli.py

from orchestrator.planner import plan
from executor.executor import dry_run, execute

def main():
    prompt = input("Enter your prompt: ")
    steps = plan(prompt)

    for cmd in steps:
        dry_run(cmd)
        should_run = input("Run this? [y/N]: ")
        if should_run.lower() == 'y':
            execute(cmd)

if __name__ == "__main__":
    main()
