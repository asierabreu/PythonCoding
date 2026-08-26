from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from duckduckgo_search import DDGS
import os


# --- LLM ---
llm = ChatOllama(model="llama3.2", temperature=0)

# --- Checkpoint ---
checkpointer = MemorySaver()

# --- Tools ---
@tool
def web_search(query: str) -> str:
    """Search the web for current information. Use this when you need to find
    up-to-date facts, news, or information that might not be in your training data."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    if not results:
        return "No results found."
    output = ""
    for r in results:
        output += f"**{r['title']}**\n{r['body']}\n{r['href']}\n\n"
    return output


@tool
def read_file(file_path: str) -> str:
    """Read the contents of a local file. Use this when the user asks you to
    read, analyze, or summarize a file on their computer. The file_path should
    be a relative or absolute path to a text file."""
    try:
        resolved = os.path.abspath(file_path)
        with open(resolved, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content) > 10000:
            return content[:10000] + "\n\n[... file truncated at 10,000 characters]"
        return content
    except FileNotFoundError:
        return f"Error: File not found at '{file_path}'"
    except Exception as e:
        return f"Error reading file: {e}"


tools = [web_search, read_file]


# --- System Prompt ---
system_prompt = """You are a helpful research assistant. You can search the web
for current information and read local files when asked.

When answering questions:
- Use the web_search tool for questions about current events, recent news, or
  anything that might have changed after your training data cutoff
- Use the read_file tool when the user asks you to read or analyze a file
- Always cite your sources when using web search results
- Be concise but thorough in your answers
"""


# --- Create the Agent ---
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt,
    checkpointer=checkpointer,
)


# --- Interactive Loop ---
def main():
    print("AI Research Assistant")
    print("Type 'quit' to exit, 'new' to start a fresh conversation.\n")

    config = {"configurable": {"thread_id": "session-1"}}
    session_count = 1

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "new":
            session_count += 1
            config = {"configurable": {"thread_id": f"session-{session_count}"}}
            print("Started a new conversation.\n")
            continue

        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
        )

        # Get the last AI message from the response
        ai_message = response["messages"][-1]
        print(f"\nAgent: {ai_message.content}\n")


if __name__ == "__main__":
    main()