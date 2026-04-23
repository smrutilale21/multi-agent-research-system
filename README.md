# Multi-Agent Research System

A LangGraph-based multi-agent AI system that refines user queries, performs structured research, and generates final answers using a graph-based workflow.

## Overview

This project demonstrates how to build a stateful multi-agent workflow using LangGraph.  
Instead of a simple linear chain, the system uses multiple nodes connected through graph edges, allowing structured execution and shared state management.

The system currently includes:
- a **Planner Agent** to refine the user query
- a **Researcher Agent** to generate research notes
- a graph workflow that passes shared state across agents
- a final output generation flow

This project is designed to showcase:
- LangGraph fundamentals
- multi-step AI workflows
- state management
- node and edge based orchestration
- scalable agent architecture

---

## Features

- Multi-agent architecture using LangGraph
- Shared workflow state using `TypedDict`
- Planner node for query refinement
- Researcher node for information synthesis
- Graph-based execution using nodes and edges
- Modular and extensible structure for adding more agents/tools later

---

## Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **OpenAI API**
- **python-dotenv**

---

## Project Architecture

```text
User Query
   ↓
Planner Agent
   ↓
Researcher Agent
   ↓
Final Answer

## Project Structure

```text
app.py        → entry point
graph.py      → LangGraph workflow
nodes.py      → agent logic
state.py      → shared state
prompts.py    → prompt templates
llm.py        → model configuration