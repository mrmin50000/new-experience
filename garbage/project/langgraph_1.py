from typing import Literal

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph

load_dotenv()

import os
from langfuse.langchain import CallbackHandler

public_key=os.getenv("LANGFUSE_PUBLIC_KEY", "sk-lf-d1c806cb-62c2-4291-bc16-ab125b5143f8"),
secret_key=os.getenv("LANGFUSE_SECRET_KEY", "pk-lf-ee117d96-6eb1-425c-ad81-e70e441ee798"),
host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

langfuse_handler = CallbackHandler()

from langfuse import get_client
 
langfuse = get_client()

@tool
def write_email(to: str, subject: str, content: str) -> str:
    """Write a draft of email."""
    return f"Черновик письма создан\n\nTo: {to}\n\nSubject: {subject}\n\nContent:\n{content}"


@tool
def send_email(to: str, subject: str, content: str) -> str:
    """Send an email."""
    return f"Письмо отправлено\n\nTo: {to}\n\nSubject: {subject}\n\nContent:\n{content}"

inference_server_url = "http://localhost:11434/v1" 


llm = ChatOpenAI(
    model="qwen3",
    base_url=inference_server_url,
    api_key="no-key",
)

tools = [write_email, send_email]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools, tool_choice="auto")


def call_llm(state: MessagesState):
    """Run LLM with tools."""
    output = llm_with_tools.invoke(state["messages"])
    return {"messages": [output]}


def run_tool(state: MessagesState):
    """Perform the tool call."""
    result = []

    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"]).replace("\\n", "\n")
        result.append(
            {"role": "tool", "content": observation, "tool_call_id": tool_call["id"]}
        )

    return {"messages": result}


def should_continue(state: MessagesState) -> Literal["run_tool", "__end__"]:
    """Route to tool handler, or end if no tool calls are made."""
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "run_tool"

    return END


workflow = StateGraph(MessagesState)
workflow.add_node("router", call_llm)
workflow.add_node("run_tool", run_tool)
workflow.add_node("answer", call_llm)
workflow.add_edge(START, "router")
workflow.add_conditional_edges(
    "router", should_continue, {"run_tool": "run_tool", END: END}
)
workflow.add_edge("run_tool", "answer")
workflow.add_edge("answer", END)

app = workflow.compile()

print(
    app.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "hello, can you help me write and send an email to",
                }
            ]
        },
        config={"callbacks": [langfuse_handler]}
    )
)
