# ai-musings

A hands-on learning journal for AI tools and technologies. Each concept gets its
own chapter folder with a plain-language explanation, a runnable notebook, and
exercises you can do on your own machine.

## Chapters

| # | Concept | What you'll build | Status |
|---|---------|-------------------|--------|
| 01 | [Vector Embeddings](01-vector-embeddings/) | Similarity metrics from scratch, word vectors from co-occurrence, semantic search, 2D embedding maps | 🚧 In progress |
| 02 | Vector Databases | _planned_ | ⏳ |
| 03 | Retrieval-Augmented Generation (RAG) | _planned_ | ⏳ |
| 04 | Tokenization | _planned_ | ⏳ |
| 05 | Prompting & Tool Use | _planned_ | ⏳ |

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
