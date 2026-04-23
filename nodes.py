from llm import get_llm
from prompts import PLANNER_PROMPT, RESEARCH_PROMPT
from state import ResearchState


llm = get_llm()


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

    prompt = RESEARCH_PROMPT.format(refined_query=refined_query)
    response = llm.invoke(prompt)
    content = response.content.strip()

    research_notes = ""
    final_answer = content

    if "RESEARCH_NOTES:" in content and "FINAL_ANSWER:" in content:
        parts = content.split("FINAL_ANSWER:")
        notes_part = parts[0].replace("RESEARCH_NOTES:", "").strip()
        answer_part = parts[1].strip()
        research_notes = notes_part
        final_answer = answer_part

    return {
        "research_notes": research_notes,
        "final_answer": final_answer
    }