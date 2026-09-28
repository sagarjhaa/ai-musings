# ai-musings

A hands-on learning journal for AI tools and technologies. Each concept gets its
own chapter folder with a plain-language explanation, a runnable notebook, and
exercises you can do on your own machine.

## Chapters

| # | Concept | What it covers | Status |
|---|---------|-------------------|--------|
| 01 | [Vector Embeddings](01-vector-embeddings/) | Similarity metrics from scratch, word vectors from co-occurrence, semantic search, 2D embedding maps | 📘 Notebook ready · exercises in progress |
| 02 | Tokenization | How text becomes tokens; why token counts drive cost and context limits | ⏳ |
| 03 | Transformers & Attention | The architecture behind every modern LLM | ⏳ |
| 04 | Prompt Engineering | System prompts, few-shot examples, chain-of-thought, structured outputs | ⏳ |
| 05 | Vector Databases | Storing and searching millions of embeddings (FAISS, Chroma, pgvector) | ⏳ |
| 06 | Retrieval-Augmented Generation (RAG) | Grounding LLM answers in your own documents | ⏳ |
| 07 | Tool Use & Function Calling | Letting a model call APIs and code | ⏳ |
| 08 | Model Context Protocol (MCP) | The standard for connecting AI apps to tools and data | ⏳ |
| 09 | AI Agents | Loops of plan → act → observe; multi-agent systems | ⏳ |
| 10 | Evaluation (Evals) | Measuring whether an AI system is actually good | ⏳ |
| 11 | Fine-Tuning | Adapting a model to a task (LoRA, instruction tuning) | ⏳ |
| 12 | Running LLMs Locally | Open-weight models, quantization, Ollama / llama.cpp | ⏳ |
| 13 | Multimodal AI | Models that see, hear and generate images | ⏳ |
| 14 | AI Safety & Guardrails | Prompt injection, hallucinations, content filtering | ⏳ |
| 15 | LLMOps & Production | Cost, latency, caching, observability, deployment | ⏳ |
| 16 | AI-Assisted Coding | Working effectively with coding agents like Claude Code | ⏳ |

The roadmap is a guide, not a contract; chapters get added as I get to them.
Progress by day is in [LEARNING_LOG.md](LEARNING_LOG.md).

## Repo layout

Every chapter follows the same shape so they're easy to navigate:

```
NN-concept-name/
├── README.md          # the concept in plain language, plus how to run things
├── requirements.txt   # dependencies for this chapter only
├── *.ipynb            # the main walkthrough notebook
└── *.py               # small scripts to play with the concept from a terminal
```

## Running a chapter locally

Each chapter has its own virtual environment so dependencies don't collide:

```bash
cd 01-vector-embeddings
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab                        # or: jupyter notebook
```
