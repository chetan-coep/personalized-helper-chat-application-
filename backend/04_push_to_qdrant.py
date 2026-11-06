"""
Stage 4: Push to Qdrant Cloud
Loads prepared points, computes 384-dim dense embeddings using FastEmbed,
ensures collection and payload indexes exist on Qdrant Cloud, and batch upserts points.
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

from qdrant_client import QdrantClient, models
from qdrant_client.models import Distance, VectorParams, PointStruct, PayloadSchemaType
from fastembed import TextEmbedding

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "document"
POINTS_FILE = DOCS_DIR / "qdrant_points" / "all_qdrant_points.jsonl"
ENV_FILE = Path(__file__).resolve().parent / ".env"

load_dotenv(ENV_FILE)

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "tech_documentation"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_SIZE = 384
BATCH_SIZE = 64


def push_points_to_qdrant(limit: int = None, recreate: bool = False, collection_name: str = COLLECTION_NAME):
    if not QDRANT_URL or not QDRANT_API_KEY:
        raise ValueError("QDRANT_URL and QDRANT_API_KEY must be configured in .env file.")

    if not POINTS_FILE.exists():
        raise FileNotFoundError(f"Prepared points file not found at: {POINTS_FILE}")

    print("=" * 65)
    print("STAGE 4: PUSHING POINTS TO QDRANT CLOUD")
    print(f"Target Cluster: {QDRANT_URL}")
    print(f"Collection Name: {collection_name}")
    print(f"Embedding Model: {EMBEDDING_MODEL_NAME} ({VECTOR_SIZE}d)")
    print("=" * 65)

    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, timeout=30)
    embedding_model = TextEmbedding(model_name=EMBEDDING_MODEL_NAME)

    collections = [c.name for c in client.get_collections().collections]
    if recreate and collection_name in collections:
        print(f"Recreating collection '{collection_name}'...")
        client.delete_collection(collection_name)
        collections.remove(collection_name)

    if collection_name not in collections:
        print(f"Creating collection '{collection_name}'...")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        )

        for field in ["technology", "category", "section", "source_url"]:
            client.create_payload_index(
                collection_name=collection_name,
                field_name=field,
                field_schema=PayloadSchemaType.KEYWORD
            )
            print(f"  Created keyword index on: {field}")

        client.create_payload_index(
            collection_name=collection_name,
            field_name="doc_order",
            field_schema=PayloadSchemaType.INTEGER
        )
        print(f"  Created integer index on: doc_order")

    print(f"Reading points from {POINTS_FILE}...")
    points_to_upload = []
    with POINTS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                points_to_upload.append(json.loads(line))
                if limit and len(points_to_upload) >= limit:
                    break

    total = len(points_to_upload)
    print(f"Total points to upload: {total}")

    start_time = time.time()
    uploaded = 0

    for i in tqdm(range(0, total, BATCH_SIZE), desc="Uploading Batches"):
        batch = points_to_upload[i:i + BATCH_SIZE]
        texts = [pt["payload"]["content"] for pt in batch]

        embeddings = list(embedding_model.embed(texts))
        structs = [
            PointStruct(id=pt["id"], vector=emb.tolist(), payload=pt["payload"])
            for pt, emb in zip(batch, embeddings)
        ]

        client.upsert(collection_name=collection_name, points=structs, wait=True)
        uploaded += len(structs)

    elapsed = round(time.time() - start_time, 1)
    print("\n" + "=" * 65)
    print(f"SUCCESS: Pushed {uploaded} points to Qdrant collection '{collection_name}' in {elapsed}s!")
    print("=" * 65)


def main():
    parser = argparse.ArgumentParser(description="Stage 4: Push documentation points to Qdrant Cloud.")
    parser.add_argument("--limit", type=int, default=None, help="Max points to upload (default all)")
    parser.add_argument("--recreate", action="store_true", help="Recreate collection before pushing")
    parser.add_argument("--collection", type=str, default=COLLECTION_NAME, help="Collection name")
    args = parser.parse_args()

    push_points_to_qdrant(limit=args.limit, recreate=args.recreate, collection_name=args.collection)


if __name__ == "__main__":
    main()

