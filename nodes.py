from llm import get_llm
from prompts import PLANNER_PROMPT, RAG_RESEARCH_PROMPT
from retriever import retrieve_context
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


def retriever_node(state: ResearchState) -> dict:
    refined_query = state["refined_query"]

    retrieved_context = retrieve_context(refined_query, k=3)

    return {
        "retrieved_context": retrieved_context
    }


def research_node(state: ResearchState) -> dict:
    refined_query = state["refined_query"]
    retrieved_context = state["retrieved_context"]

    prompt = RAG_RESEARCH_PROMPT.format(
        refined_query=refined_query,
        retrieved_context=retrieved_context
    )

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
        "tool_results": "RAG retrieval completed using local knowledge base.",
        "final_answer": final_answer
    }