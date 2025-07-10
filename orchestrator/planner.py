# orchestrator/planner.py

import platform
from ollama import chat
from memory.vector_store import query_memory

def plan(prompt: str) -> list[str]:
    # Detect current OS
    os_type = platform.system()  # 'Windows', 'Linux', 'Darwin'

    # Load any related past memory (optional vector search)
    past = query_memory(prompt)

    # OS-friendly name for prompt clarity
    os_name = {
        "Windows": "Windows PowerShell",
        "Linux": "Linux bash",
        "Darwin": "macOS terminal"
    }.get(os_type, "Linux bash")

    # System prompt for the LLM
    system_prompt = (
        f"You are a system automation planner. When given a prompt, return only shell commands "
        f"to execute that task for a {os_name} environment. Do not include explanations, markdown, "
        f"or formatting. Each command must be on its own line."
    )

    # Optional: Add past memory to enrich context
    user_message = prompt
    if past and past.get("documents"):
        history = past.get("documents", [])
        flat_history = []
        for doc in history:
            if isinstance(doc, list):
                for item in doc:
                    if isinstance(item, str):
                        flat_history.append(item)
            elif isinstance(doc, str):
                flat_history.append(doc)

        history_text = "\n".join(flat_history)
        user_message = f"Previously, the user worked on:\n{history_text}\n\nNow they ask:\n{prompt}"

    # Call Ollama LLM
    try:
        response = chat(
            model='llama3',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
    except Exception as e:
        print(f"[Planner Error] LLM call failed: {e}")
        return []

    # Extract response
    raw = response['message']['content']
    print("[LLM Plan Output]\n", raw)

    # Clean response lines (strip bullet points, etc.)
    steps = [line.strip("- ").strip() for line in raw.splitlines() if line.strip() and not line.startswith("```")]
    return steps
