# gen_script.py

from agents.coder_agent import generate_script

if __name__ == "__main__":
    prompt = input("What script should I generate? ")
    script = generate_script(prompt)

    with open("generated_script.sh" if not script.startswith("powershell") else "generated_script.ps1", "w") as f:
        f.write(script)

    print("✅ Script written to file.")
