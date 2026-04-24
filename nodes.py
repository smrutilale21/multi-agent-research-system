from langchain.agents import create_agent
from llm import get_llm
from prompts import PLANNER_PROMPT
from state import ResearchState
from tools import search_tool, calculator


llm = get_llm()

research_agent = create_agent(
    model=llm,
    tools=[search_tool, calculator],
    system_prompt=(
        "You are a research agent inside a multi-agent research system. "
        "Use the available tools when helpful. "
        "For general research questions, prefer using search_tool. "
        "For numerical calculations, use calculator. "
        "After using tools if needed, produce a clear final answer."
    ),
)


def planner_node(state: ResearchState) -> dict:
    user_query = state["user_query"]

    prompt = PLANNER_PROMPT.format(user_query=user_query)
    response = llm.invoke(prompt)

    refined_query = response.content.strip()
    
    return {
        "refined_query": refined_query
    }


def research_node(state: ResearchState) -> dict:
    refined_query = state["refined_query"]

    result = research_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": refined_query
                }
            ]
        }
    )

    messages = result["messages"]

    final_answer = ""
    tool_results = []

    for message in messages:
        msg_type = getattr(message, "type", "")
        content = getattr(message, "content", "")

        if msg_type == "tool":
            tool_name = getattr(message, "name", "tool")
            tool_results.append(f"{tool_name}: {content}")
            
        if msg_type == "ai" and content:
            final_answer = content

    return {
        "research_notes": "Tool-assisted research completed.",
        "tool_results": "\n".join(tool_results) if tool_results else "No tools used.",
        "final_answer": final_answer if final_answer else "No final answer generated."
    }