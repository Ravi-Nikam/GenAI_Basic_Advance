# GenAI: Basic to Advanced 🚀

A comprehensive repository for mastering Generative AI, LLM application development, Retrieval-Augmented Generation (RAG), Agentic workflows with LangGraph, and Model Context Protocol (MCP).

---

## 📚 Repository Overview

This repository is organized into dedicated modules, transitioning from foundational concepts to production-grade Generative AI systems:

```text
GenAI_Basic_Advance/
├── Basic_Advance_RAG/    # Retrieval-Augmented Generation (Loaders, Splitting, Embeddings, FAISS, ChromaDB)
├── eLanggraph/           # Agentic workflows, stateful graphs, tool integration, and human-in-the-loop
├── langchain_tut/        # Deep-dive LangChain tutorials (Models, Prompts, Tools, Structured Output)
├── mcplangchain/         # Model Context Protocol (MCP) servers and clients using LangChain
├── Graph.ipynb           # Graph & workflow visualization experiments
└── p-value.ipynb         # Statistical analysis & evaluation
```

---

## 📂 Modules & Contents

### 1. 🔍 [Basic_Advance_RAG](./Basic_Advance_RAG)
End-to-end implementation of Retrieval-Augmented Generation architectures:
- **Document Ingestion & Parsing**: Handling PDFs and rich text using `pypdf` and `PyMuPDF`.
- **Text Chunking & Splitting**: Semantic and recursive chunking via `langchain-text-splitters`.
- **Embeddings**: Local embedding models using `sentence-transformers`.
- **Vector Stores & Indexing**: Similarity search and vector persistence with **FAISS** and **ChromaDB**.
- **LLM Synthesis**: High-speed inference with **Groq** (`langchain-groq`) and **Google Gemini**.

### 2. 🤖 [eLanggraph](./eLanggraph)
Building stateful, multi-actor AI agents using LangGraph:
- **Basic Chatbot** (`basicchatbot.ipynb`): Core state transitions and cycle management.
- **Tool Calling** (`chatwithtool.ipynb`): Binding tools to agents for dynamic execution.
- **Human-in-the-Loop** (`human_inthe_loop.ipynb`): Approval checkpoints, state inspection, and manual overrides.
- **Cheat Sheet**: High-level syntax summary (`basic-of-langgraph.md`).

### 3. 🦜 [langchain_tut](./langchain_tut)
Systematic progression through the LangChain ecosystem:
- `1-langchain_intro.ipynb`: Architecture basics and core primitives.
- `2-diff-models.ipynb`: Comparing Chat Models, LLMs, and providers.
- `3-tools.ipynb`: Custom tool creation and tool decorators.
- `4-messages.ipynb`: Managing `SystemMessage`, `HumanMessage`, and `AIMessage` history.
- `5-strcutredoutput.ipynb`: Enforcing schema validation with Pydantic and JSON outputs.
- `middleware.ipynb`: Pipeline interception and hooks.

### 4. 🔌 [mcplangchain](./mcplangchain)
Integrating Anthropic's Model Context Protocol (MCP) with LangChain:
- **MCP Servers**: Exposing tools via servers (`mathserver.py`, `wetherserver.py`).
- **MCP Client**: Orchestrating MCP tools from LangChain (`client.py`, `async_example.py`).

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.11+
- Recommended: [uv](https://docs.astral.sh/uv/) or standard `pip` / `venv`

### Installation

Clone the repository:
```bash
git clone https://github.com/Ravi-Nikam/GenAI_Basic_Advance.git
cd GenAI_Basic_Advance
```

Create and activate a virtual environment:

**Using PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Using Command Prompt (cmd):**
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**Using Bash:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies for the module you want to work on (e.g., `Basic_Advance_RAG`):
```bash
pip install -r Basic_Advance_RAG/requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root or the module directory (it is ignored by Git to keep your credentials safe):

```env
# LLM Providers
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Search & Tools
TAVILY_API_KEY=your_tavily_api_key_here

# LangSmith Tracing (Optional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_PROJECT=GenAI_Basic_Advance
```

---

## 🛡️ License

This project is licensed under the MIT License - feel free to use and adapt it for your learning and projects.
