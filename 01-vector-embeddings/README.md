# 01 · Vector Embeddings

> **One-line idea:** an embedding turns a thing (a word, a sentence, an image, a
> product) into a list of numbers, and things with similar meanings end up with
> similar numbers.

## Why it matters

Computers can't compare meanings directly, but they can compare numbers.
Embeddings are the bridge. Semantic search, recommendations, clustering,
de-duplication, and RAG (retrieval-augmented generation) all work the same
way: embed everything, then look for vectors that are close together.

## Key ideas

| Term | Plain meaning |
|------|---------------|
| **Vector** | A list of numbers, e.g. `[0.12, -0.80, 0.33, ...]`. It's a point in space. |
| **Dimension** | How many numbers are in the list. Modern text models use 384 to 3072. |
| **Embedding model** | A function (usually a neural net) that maps input to a vector. |
| **Cosine similarity** | The angle between two vectors: `1` means same direction, `0` means unrelated, `-1` means opposite. |
| **Dense vs sparse** | One-hot and bag-of-words vectors are *sparse* (mostly zeros, no sense of meaning). Learned embeddings are *dense* (every number carries some signal). |
| **Semantic search** | Find documents whose vectors are nearest to the query's vector. This works even when they share no keywords. |
| **Dimensionality reduction** | PCA or t-SNE squashes 384-D vectors into 2-D so you can plot them. |

## What's in this folder

| File | What it does |
|------|--------------|
| [`vector_embeddings.ipynb`](vector_embeddings.ipynb) | The main walkthrough: intuition, similarity math from scratch, word vectors learned from a tiny corpus, sentence embeddings, semantic search, visualization, and exercises. |
| [`semantic_search.py`](semantic_search.py) | A terminal playground. Load a corpus, type queries, and see ranked matches with similarity scores. |

## Run it locally

```bash
cd 01-vector-embeddings
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab vector_embeddings.ipynb
```

The first time you run the sentence-embedding section, it downloads
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
(about 90 MB) and caches it. After that everything runs offline. If the download
fails (no internet, or a firewall), the notebook falls back to a small model it
trains on the spot, so every cell still runs.

## Learning path

1. **Intuition:** hand-craft 3-D vectors for animals and foods and plot them.
2. **Similarity:** implement dot product, cosine similarity, and Euclidean distance in NumPy.
3. **Learned vectors:** see why one-hot vectors fail, then learn word vectors from co-occurrence counts plus SVD.
4. **Pretrained models:** embed sentences with a transformer and read the similarity heatmap.
5. **Semantic search:** rank documents by meaning, and compare that with keyword matching.
6. **Visualize:** PCA and t-SNE maps, and k-means clusters.
7. **Exercises:** see the end of the notebook.

## Terminal playground

```bash
python semantic_search.py                        # interactive, built-in sample docs
python semantic_search.py my_notes.txt -k 5      # your own file, one doc per line
python semantic_search.py -q "cheap flights"     # single query
```

## Exercise tracker

Tick these off as you finish them. Put solutions in new notebook cells, or in
an `exercises/` folder here.

- [ ] 1. `most_similar`: nearest items by cosine similarity
- [ ] 2. Metric showdown: cosine vs. dot product vs. Euclidean
- [ ] 3. Word arithmetic: `king - man + woman`
- [ ] 4. Break it: three queries where semantic search fails
- [ ] 5. Your own corpus: embed, plot, cluster
- [ ] 6. Hybrid search: keyword + semantic
- [ ] 7. Compare models: MiniLM vs. MPNet
- [ ] 8. Stretch: brute-force search at 10k and 1M vectors

## Takeaways

_Filled in after finishing the chapter. See [LEARNING_LOG.md](../LEARNING_LOG.md)._
