# 🧠 Multi-Agent Research System (LangGraph + RAG + ChromaDB)

A production-oriented multi-agent AI system that performs intelligent research using a structured workflow and Retrieval-Augmented Generation (RAG), delivering context-aware and reliable responses.

---

## 🚀 Overview

This system uses a multi-agent architecture to process user queries through multiple stages:

1. **Planner Agent** → Refines the user query
2. **Retriever Agent** → Fetches relevant context using RAG (ChromaDB + embeddings)
3. **Research Agent** → Generates structured research notes
4. **Answer Generator** → Produces final answer with confidence and sources

The system is designed with reliability, modularity, and scalability in mind.

---

## 🏗️ Architecture

User Query
↓
Planner Agent (Query Refinement)
↓
Retriever (RAG using ChromaDB → Retrieved Context)
↓
Research Agent (Generates Research Notes)
↓
Answer Generation (Final Answer)
↓
Structured Output (Confidence + Sources + JSON Export)

---

## 🏗️ Architecture Diagram

![Architecture](assets/architecture_diagram.png)

## 🔄 Workflow

1. User submits a query through the Streamlit interface
2. Planner agent refines the query for better retrieval
3. Retriever fetches relevant context from ChromaDB using embeddings
4. Research agent analyzes the context and generates structured notes
5. Final answer is synthesized based on retrieved knowledge
6. System outputs confidence score, sources, and downloadable JSON report

---

## 🧠 Key Features

* Multi-agent workflow using LangGraph
* RAG pipeline with ChromaDB (persistent vector database)
* OpenAI embeddings for semantic search
* Structured output validation using Pydantic
* Retry mechanism for handling invalid or malformed LLM outputs
* Logging for observability and debugging
* JSON export of results
* Modular and scalable architecture

---

## 🌟 Highlights

* Designed a multi-agent AI system using LangGraph
* Implemented RAG pipeline with persistent ChromaDB
* Built structured output system with validation and retries
* Developed an end-to-end Streamlit application for research automation

---

## 🛠️ Tech Stack

* Python
* LangGraph
* LangChain
* ChromaDB
* OpenAI API
* Pydantic
* Streamlit

---

## 🧪 Example Queries

* What is RAG and how does it improve LLM performance?
* Explain how a multi-agent AI system works
* What are the risks of AI adoption in enterprises?
* How is generative AI used in customer support?

---

## 📸 Demo Screenshots

### 🏠 Home Screen

![Home](assets/home_screen.png)

### 🔍 Sample Query & Output

![Output](assets/sample_output.png)

### 📚 Retrieved Context (RAG)

![Context](assets/retrieved_context.png)

### 📄 JSON Export

![JSON](assets/json_export.png)

### 🕘 Run History

![History](assets/run_history.png)

---

## ⚙️ Setup Instructions

```bash
git clone <https://github.com/smrutilale21/multi-agent-research-system>
cd multiAgent-system
pip install -r requirements.txt
streamlit run app.py
```

---

## ⚠️ Notes

* ChromaDB files are excluded via `.gitignore`
* `.env` is not committed for security reasons
* Logs are stored locally for debugging purposes

---

## 🔮 Future Improvements

* Add hybrid retrieval (ChromaDB + web search)
* Improve chunking strategy for better retrieval accuracy
* Add evaluation metrics for retrieval quality
* Introduce memory for conversational context

---

## 📌 Conclusion

This project demonstrates a real-world implementation of a multi-agent AI system using RAG, structured outputs, and modular architecture — showcasing strong understanding of scalable and production-ready AI system design.

---