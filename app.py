import json
import streamlit as st
from graph import build_graph

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Multi-Agent Research System")
st.write("Production-ready Multi-Agent RAG system using LangGraph, ChromaDB, and OpenAI.")

if "run_history" not in st.session_state:
    st.session_state.run_history = []

query = st.text_area(
    "Enter your research query",
    height=150,
    placeholder="Example: What is RAG and why is it useful?"
)

if st.button("Run Research Workflow", use_container_width=True):
    if not query.strip():
        st.error("Please enter a query.")
    else:
        try:
            graph = build_graph()

            with st.spinner("Running planner, retriever, and researcher..."):
                result = graph.invoke(
                    {
                        "user_query": query,
                        "refined_query": "",
                        "retrieved_context": "",
                        "research_notes": "",
                        "sources": "",
                        "final_answer": "",
                        "confidence": ""
                    }
                )

            st.session_state.run_history.append(
                {
                    "user_query": result["user_query"],
                    "refined_query": result["refined_query"],
                    "confidence": result["confidence"]
                }
            )

            st.success("Workflow completed")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Query")
                st.write(result["user_query"])

                st.subheader("Refined Query")
                st.write(result["refined_query"])

                st.subheader("Confidence")
                st.write(result["confidence"])

            with col2:
                st.subheader("Research Notes")
                st.write(result["research_notes"])

                st.subheader("Sources")
                st.write(result["sources"])

            with st.expander("View Retrieved Context"):
                st.write(result["retrieved_context"])

            st.subheader("Final Answer")
            st.write(result["final_answer"])

            report = {
                "user_query": result["user_query"],
                "refined_query": result["refined_query"],
                "research_notes": result["research_notes"],
                "sources": result["sources"],
                "confidence": result["confidence"],
                "final_answer": result["final_answer"],
                "retrieved_context": result["retrieved_context"]
            }

            st.download_button(
                label="Download Research Report JSON",
                data=json.dumps(report, indent=2),
                file_name="research_report.json",
                mime="application/json",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

with st.sidebar:
    st.header("Run History")

    if st.session_state.run_history:
        for i, item in enumerate(reversed(st.session_state.run_history), start=1):
            st.write(f"**{i}. {item['user_query']}**")
            st.caption(f"Refined: {item['refined_query']}")
            st.caption(f"Confidence: {item['confidence']}")
    else:
        st.caption("No runs yet.")