# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Neo4j GraphAcademy course project for building an LLM-powered chatbot using Python. The chatbot uses LangChain with OpenAI to answer questions about movies, leveraging Neo4j as a knowledge graph backend.

## Commands

### Development
```bash
# Install dependencies (uses uv package manager)
uv sync

# Run the Streamlit chatbot application
streamlit run bot.py
```

### Testing & Dev Tools
```bash
# Install dev dependencies (pytest, ruff, ty)
uv sync --group dev

# Run tests (requires Neo4j instance with recommendations dataset and vector index)
pytest

# Lint with Ruff
ruff check .
ruff check . --fix  # Auto-fix issues

# Type check with ty
ty check .
```

## Architecture

### Course Structure
This is a **learning exercise repository** with skeleton files and completed solutions:
- **Root files** (`bot.py`, `agent.py`, `graph.py`, `llm.py`, `tools/`) - Skeleton code with TODO comments for students to complete
- **`solutions/`** - Reference implementations showing the completed versions

### Key Components

**Entry Point**: `bot.py` - Streamlit application that handles chat UI and message history via `st.session_state`

**LLM Layer** (`llm.py`): Initializes OpenAI ChatGPT and embeddings using `langchain_openai`

**Graph Layer** (`graph.py`): Neo4j connection using `langchain_neo4j.Neo4jGraph`

**Agent Layer** (`agent.py`): LangChain ReAct agent with:
- Chat message history stored in Neo4j (`Neo4jChatMessageHistory`)
- `RunnableWithMessageHistory` for conversation context

**Tools** (`tools/`):
- `vector.py` - Vector similarity search for movie plots using Neo4j vector index
- `cypher.py` - Cypher query generation for structured movie data

### Configuration
Secrets stored in `.streamlit/secrets.toml` (see `secrets.toml.example`):
- `OPENAI_API_KEY`, `OPENAI_MODEL`
- `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`

### Session Management
`utils.py` provides `get_session_id()` using Streamlit's script run context for per-user chat history.

## VS Code / VS Code Insiders Setup

The `.vscode/` directory contains full IDE configuration for development.

### Debug Configurations (launch.json)
Key launch configurations available via Run and Debug (F5):
- **Streamlit: Run Chatbot (bot.py)** - Run the main skeleton app
- **Streamlit: Run Solution Bot** - Run the completed solution
- **Pytest: Solution Tests** - Run `solutions/test_solution.py`
- **Debug: Streamlit with Full Tracing** - Debug with `justMyCode: false`

### Tasks (tasks.json)
Run via Terminal > Run Task or `Cmd+Shift+P` > "Tasks: Run Task":
- **ty: Type Check All** - Run ty type checker on project
- **ruff: Lint and Fix All** - Auto-fix linting issues
- **uv: Sync with Dev Dependencies** - Install all dev tools

### Recommended Extensions
Open Extensions sidebar and filter by `@recommended` to install:
- Python, Pylance, debugpy (Microsoft Python stack)
- Ruff (linting/formatting - replaces black, flake8, isort)
- Neo4j for VS Code (Cypher syntax)
- Even Better TOML (pyproject.toml support)

### Code Quality Tools
- **Ruff** - Linting and formatting on save (comprehensive ruleset including security, docstrings, type annotations)
- **ty** - Fast type checker from Astral (run via tasks or CLI)
- **Pylance** - IDE type checking in "basic" mode
- **solutions/** directory is excluded from linting (read-only reference code)
- Google-style docstrings expected (see `pyproject.toml` for example)
