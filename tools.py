from langchain.tools import tool


@tool
def search_tool(query: str) -> str:
    """
    Use this tool for general research-style questions.
    It returns mock search findings for now.
    Later, this can be replaced with a real web search or retrieval system.
    """
    mock_knowledge = {
        "generative ai in customer support": (
            "Generative AI is used in customer support for chatbots, "
            "ticket summarization, response drafting, multilingual support, "
            "knowledge-base search, and agent assistance."
        ),
        "ai in healthcare": (
            "AI in healthcare is used for medical imaging, diagnosis support, "
            "patient triage, drug discovery, clinical documentation, and workflow automation."
        ),
        "ai for small businesses": (
            "Small businesses use AI for content creation, customer support automation, "
            "email drafting, analytics, and operational efficiency."
        )
    }
    normalized = query.strip().lower()

    for key, value in mock_knowledge.items():
        if key in normalized or normalized in key:
            return value

    return (
        f"Mock search result for '{query}': "
        "AI helps improve efficiency, decision support, automation, and user experience."
    )


@tool
def calculator(expression: str) -> str:
    """
    Use this tool for basic mathematical calculations.
    Example inputs: '25 * 4', '100 / 5', '18 + 7'
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"