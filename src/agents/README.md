# Local Ollama Web Search Agent

This agent uses a local Ollama model through LangChain. It can search the web
with DuckDuckGo, read local text files, and keep conversation history while it
is running.

## Requirements

- Python 3.11 or newer
- Ollama installed and running
- Internet access for the DuckDuckGo web search tool

## Install Ollama and a model

Install Ollama from [ollama.com/download](https://ollama.com/download), then
start the local Ollama service:

```bash
ollama serve
```

In another terminal, download the model used by the agent:

```bash
ollama pull llama3.2
```

The agent expects Ollama at its default address, `http://localhost:11434`.
To use another model, pull it with `ollama pull` and update the `model` value
in `web_search_agent.py`.

## Install Python dependencies

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r src/agents/requirements.txt
```

## Run the agent

Make sure `ollama serve` is running, then execute:

```bash
cd src/agents
python web_search_agent.py
```

Enter a question at the `You:` prompt. Use:

- `quit` to exit
- `new` to start a fresh conversation

Questions about current information can use the web search tool. When web
search results are used, the agent includes their URLs in its response.