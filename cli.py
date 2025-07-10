from orchestrator.planner import plan
from executor.executor import dry_run, execute
from memory.historian import log_interaction  # <-- Import historian logger

def main():
    prompt = input("Enter your prompt: ")
    steps = plan(prompt)

    approved_steps = []  # <-- Track which steps the user approved

    for cmd in steps:
        dry_run(cmd)
        should_run = input("Run this? [y/N]: ")
        if should_run.lower() == 'y':
            execute(cmd)
            approved_steps.append(cmd)

    # ✅ Log the entire interaction
    log_interaction(prompt, steps, approved_steps)

if __name__ == "__main__":
    main()
