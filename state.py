from typing import TypedDict
from typing import List


class ResearchState(TypedDict):
    user_query: str
    refined_query: str
    retrieved_context: str
    research_notes: str
    sources: List[str]
    final_answer: str
    confidence: str