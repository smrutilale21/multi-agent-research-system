from typing import TypedDict


class ResearchState(TypedDict):
    user_query: str
    refined_query: str
    retrieved_context: str
    research_notes: str
    tool_results: str
    final_answer: str