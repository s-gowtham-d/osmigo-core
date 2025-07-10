# cli.py

from orchestrator.planner import plan
from executor.executor import dry_run, execute
from memory.historian import log_interaction  # Logs interactions
from memory.vector_store import embed_and_store  # Stores in vector DB

def main():
    prompt = input("Enter your prompt: ")

    # 🧠 Plan the actions using LLM
    steps = plan(prompt)
    approved_steps = []

    for cmd in steps:
        dry_run(cmd)  # Just print the command
        should_run = input("Run this? [y/N]: ")
        if should_run.lower() == 'y':
            execute(cmd)  # Actually execute it
            approved_steps.append(cmd)

    # 📝 Log interaction to historian
    log_interaction(prompt, steps, approved_steps)

    # 💾 Store prompt and metadata in vector store
    embed_and_store(prompt, metadata={"source": "cli"})

if __name__ == "__main__":
    main()
