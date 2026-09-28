"""Interactive semantic search in your terminal.

Embeds a corpus (one document per line) and lets you type queries to see the
closest documents ranked by cosine similarity.

Usage:
    python semantic_search.py                     # built-in sample corpus
    python semantic_search.py my_notes.txt        # your own file, one doc per line
    python semantic_search.py -k 5 -q "cheap flights"   # one-shot query, no prompt
"""
import argparse
import sys
import time

import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

SAMPLE_CORPUS = [
    "How to bake sourdough bread at home with a starter",
    "Quick weeknight pasta recipes with garlic and olive oil",
    "Couch to 5K: a running plan for complete beginners",
    "Strength training exercises you can do without a gym",
    "Why stretching after a workout reduces soreness",
    "Getting started with Python for data analysis",
    "Understanding how large language models generate text",
    "How to set up a home Wi-Fi mesh network",
    "Backpacking through Southeast Asia on a budget",
    "How to beat jet lag on long-haul flights",
    "Index funds versus picking individual stocks",
    "How to build an emergency savings fund",
]


def load_embedder():
    """Return an embed(texts) -> unit-vector array function and a label."""
    try:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(MODEL_NAME)
        return (lambda texts: model.encode(list(texts), normalize_embeddings=True)), MODEL_NAME
    except Exception as err:
        print(f"[fallback] could not load {MODEL_NAME} ({type(err).__name__}); "
              "using character n-gram hashing, which matches spelling, not meaning.",
              file=sys.stderr)
        from sklearn.feature_extraction.text import HashingVectorizer

        hasher = HashingVectorizer(analyzer="char_wb", ngram_range=(3, 4), n_features=2**12,
                                   alternate_sign=False, norm="l2")
        return (lambda texts: hasher.transform(list(texts)).toarray()), "char-ngram hashing"


def search(query, docs, doc_vectors, embed, k):
    q = embed([query])[0]
    scores = doc_vectors @ q  # unit vectors, so dot product == cosine similarity
    top = np.argsort(-scores)[:k]
    return [(float(scores[i]), docs[i]) for i in top]


def print_results(query, results):
    print(f"\n🔎 {query}")
    for score, doc in results:
        bar = "█" * max(0, int(score * 20))
        print(f"  {score:6.3f} {bar:<20} {doc}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("corpus", nargs="?", help="text file with one document per line")
    parser.add_argument("-k", type=int, default=3, help="number of results (default 3)")
    parser.add_argument("-q", "--query", help="run a single query and exit")
    args = parser.parse_args()

    if args.corpus:
        with open(args.corpus, encoding="utf-8") as f:
            docs = [line.strip() for line in f if line.strip()]
    else:
        docs = SAMPLE_CORPUS

    embed, label = load_embedder()
    start = time.perf_counter()
    doc_vectors = embed(docs)
    print(f"Indexed {len(docs)} docs with {label} -> {doc_vectors.shape[1]} dims "
          f"in {time.perf_counter() - start:.2f}s")

    if args.query:
        print_results(args.query, search(args.query, docs, doc_vectors, embed, args.k))
        return

    print("Type a query (empty line or Ctrl-D to quit).")
    while True:
        try:
            query = input("\nquery> ").strip()
        except EOFError:
            break
        if not query:
            break
        print_results(query, search(query, docs, doc_vectors, embed, args.k))


if __name__ == "__main__":
    main()
