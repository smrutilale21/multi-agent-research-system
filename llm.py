from langchain_openai import ChatOpenAI
from config import get_openai_api_key


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=get_openai_api_key()
    )