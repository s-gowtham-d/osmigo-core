# 🧠 Osmigo Core
>The AI Brain of the Osmigo Operating System.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)


Osmigo Core is the central cognitive backend for **Osmigo OS**, a privacy-first, AI-native Linux operating system. Its primary role is to understand user intent, plan a sequence of system-level actions, and coordinate their execution through a team of specialized local agents.

## 🚀 Getting Started

Follow these instructions to get a local development environment up and running.

### ⚙️ Prerequisites

Make sure you have the following installed on your system:

*   **Python 3.10+**
*   **Git**
*   **[Ollama](https://ollama.com/)** (with a model like `llama3` pulled)
*   **[Rust & Cargo](https://www.rust-lang.org/tools/install)** (Optional: used by `osmigo-cli`)
*   `virtualenv` (Recommended)

### 🛠️ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-username/osmigo-core.git
    cd osmigo-core
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 🔌 Running the Server

1.  **Verify Ollama is Running**

    Osmigo Core communicates with the LLM via HTTP. Make sure Ollama is running in the background. You can start it with a model like this:
    ```bash
    ollama run llama3
    ```

2.  **Start the API Server**

    Run the FastAPI application using Uvicorn. The `--reload` flag will automatically restart the server when you make changes to the code.
    ```bash
    uvicorn api.routes:ask_router --reload --port 8000
    
    ```
    The API will be available at `http://localhost:8000`.

## ✅ Test Your Installation

Once the server is running, you can test the `/ask` endpoint using `curl` or any API client.

```bash
curl -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"prompt": "List all running Docker containers"}'
```

The expected response will be a structured JSON object containing the planned command, a natural language explanation, and an approval flag.

## 📁 Project Structure

The repository is organized to separate concerns, making it easier to maintain and extend.

```plaintext
osmigo-core/
├── orchestrator/        # Command planner and main orchestrator logic
├── agents/              # Specialized agents (Coder, Observer, Historian)
├── api/                 # FastAPI routes, request/response schemas
├── memory/              # Local vector DB or SQLite for short/long-term memory
├── executor/            # Dry-run simulator and permission manager
├── config/              # Application settings and environment configuration
├── main.py              # Main application entrypoint (if any)
├── requirements.txt     # Python package dependencies
└── README.md            # This file
```

## 🤝 Contributing

We are excited about community contributions! We are currently formalizing our contribution guidelines. Please check back soon for more details on how to contribute.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgements

Built with a lot of ❤️ and the following amazing technologies:

*   [FastAPI](https://fastapi.tiangolo.com/)
*   [Ollama](https://ollama.com/)
*   [Rust](https://www.rust-lang.org/)
