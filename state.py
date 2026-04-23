from typing import TypedDict


class ResearchState(TypedDict):
    user_query: str
    refined_query: str
    research_notes: str
    final_answer: str