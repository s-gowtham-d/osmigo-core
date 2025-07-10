# agents/coder_agent.py

import platform
from ollama import chat

def generate_script(prompt: str) -> str:
    os_type = platform.system()
    os_name = {
        "Windows": "Windows PowerShell script",
        "Linux": "Linux bash script",
        "Darwin": "macOS terminal script"
    }.get(os_type, "Linux bash script")

    system_prompt = (
        f"You are a professional system coder. When given a prompt, you must return a fully functional {os_name} "
        f"script to achieve the task. Do not explain. Only return the raw script content."
    )

    try:
        response = chat(
            model='llama3:latest',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        script = response['message']['content']
        print("[Coder Agent Output]\n", script)
        return script

    except Exception as e:
        print(f"[Coder Agent Error] Failed to generate script: {e}")
        return "# Error generating script"
