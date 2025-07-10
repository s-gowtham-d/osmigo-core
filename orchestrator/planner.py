from ollama import chat
import platform

def plan(prompt: str) -> list[str]:
    os_type = platform.system()  # 'Windows', 'Linux', 'Darwin'

    # Normalize for LLM wording
    os_name = {
        "Windows": "Windows PowerShell",
        "Linux": "Linux bash",
        "Darwin": "macOS terminal"
    }.get(os_type, "Linux bash")

    system_prompt = (
        f"You are a system automation planner. When given a prompt, return only shell commands "
        f"to execute that task for a {os_name} environment. Do not include explanations or markdown. "
        f"Each command should be on its own line. Start directly with the first command."
    )

    response = chat(
        model='llama3',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    raw = response['message']['content']
    print("[LLM Plan Output]\n", raw)

    steps = [line.strip("- ").strip() for line in raw.splitlines() if line.strip()]
    return steps
