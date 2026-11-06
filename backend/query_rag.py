"""
Access & Query Qdrant Cloud Points for LLM RAG.

Usage:
  uv run python query_rag.py "How do I create a route in FastAPI?"
  uv run python query_rag.py "How does pandas merge work?" --tech pandas
  uv run python query_rag.py "What is useState in React?" --tech React.js
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding

ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_FILE)

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "tech_documentation"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def search_qdrant(query: str, tech_filter: str = None, category_filter: str = None, top_k: int = 4):
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    embedding_model = TextEmbedding(model_name=EMBEDDING_MODEL_NAME)

    query_vector = list(embedding_model.embed([query]))[0].tolist()

    filter_conditions = []
    if tech_filter:
        filter_conditions.append(
            models.FieldCondition(key="technology", match=models.MatchValue(value=tech_filter))
        )
    if category_filter:
        filter_conditions.append(
            models.FieldCondition(key="category", match=models.MatchValue(value=category_filter))
        )

    qdrant_filter = models.Filter(must=filter_conditions) if filter_conditions else None

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        query_filter=qdrant_filter,
        limit=top_k,
        with_payload=True
    )

    return search_result.points


def main():
    parser = argparse.ArgumentParser(description="Query Qdrant Cloud Documentation Points.")
    parser.add_argument("query", type=str, help="Search question or query")
    parser.add_argument("--tech", type=str, help="Filter by technology (e.g. FastAPI, pandas, React.js)")
    parser.add_argument("--category", type=str, help="Filter by category (e.g. Frontend, ML_&_Data)")
    parser.add_argument("--top-k", type=int, default=3, help="Number of results")
    args = parser.parse_args()

    print(f"\nSearching for: '{args.query}'...")
    if args.tech:
        print(f"Filter: technology == {args.tech}")

    results = search_qdrant(args.query, tech_filter=args.tech, category_filter=args.category, top_k=args.top_k)

    print(f"\nFound {len(results)} relevant points:\n" + "=" * 60)
    for i, res in enumerate(results, 1):
        payload = res.payload
        print(f"[{i}] Score: {res.score:.4f} | {payload.get('technology')} -> {payload.get('title')}")
        print(f"    Section: {payload.get('section')}")
        print(f"    URL: {payload.get('source_url')}")
        print(f"    Breadcrumb: {payload.get('breadcrumb')}")
        print(f"    Content Preview:\n    {payload.get('content', '')[:250]}...\n")
        print("-" * 60)


if __name__ == "__main__":
    main()

