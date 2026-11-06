# Module 1: Technical Documentation RAG Pipeline for Qdrant

A clean, production-ready pipeline that downloads technical documentation and multimedia resources, cleans and sequences them, extracts header-aware semantic chunks with breadcrumb metadata, and pushes dense vector embeddings into Qdrant Cloud.

---

## 1. Pipeline Architecture

```
Stage 1: 01_download_resources.py
   └── Dual Discovery: Sitemap parser + BFS Link Crawler fallback
   └── English-only filtering & path-scoped scraping
   └── YouTube video transcript extraction (faster-whisper + yt-dlp)
         │
         ▼
Stage 2: 02_clean_resources.py
   └── Purges non-English locales (/de/, /es/, etc.) and irrelevant junk pages
   └── Normalizes markdown encoding and metadata frontmatter
   └── Assigns sequential reading order (001_..., 002_...)
   └── Generates toc.json per technology and master_toc.json
         │
         ▼
Stage 3: 03_extract_and_prepare.py
   └── Header-aware semantic markdown chunking (#, ##, ###)
   └── Contextual breadcrumbs preservation (e.g. FastAPI > Tutorial > Path Parameters)
   └── Deterministic UUIDv5 IDs for idempotent upserts
   └── Exports points to documentation/qdrant_points/
         │
         ▼
Stage 4: 04_push_to_qdrant.py
   └── Embeds chunks using FastEmbed (sentence-transformers/all-MiniLM-L6-v2, 384d)
   └── Creates collection 'tech_documentation' on Qdrant Cloud
   └── Configures payload indexes: technology, category, section, doc_order, source_url
   └── Batch upserts points directly into Qdrant Cloud
         │
         ▼
Search: query_rag.py
   └── Semantic search across all docs or filtered by technology/category
   └── Retrieves exact context chunks ready for LLM prompt injection
```

---

## 2. File Organization

| File | Purpose |
| :--- | :--- |
| [`01_download_resources.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/01_download_resources.py) | **Stage 1**: Downloads official docs & extracts YouTube audio transcripts |
| [`02_clean_resources.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/02_clean_resources.py) | **Stage 2**: Cleans foreign languages/junk, formats frontmatter, sequences files |
| [`03_extract_and_prepare.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/03_extract_and_prepare.py) | **Stage 3**: Chunks documents by headings, generates UUIDs & metadata points |
| [`04_push_to_qdrant.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/04_push_to_qdrant.py) | **Stage 4**: Embeds and uploads points with payload indexes to Qdrant Cloud |
| [`main.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/main.py) | **Orchestrator**: Runs all stages end-to-end or individual stages via flags |
| [`master.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/master.py) | **Master Code & Syntax Copilot**: Generates syntax-accurate code answers using Groq OpenAI model grounded in Qdrant |
| [`query_rag.py`](file:///C:/final_year/temp%20project/ai%20course/project/module1/query_rag.py) | **RAG Query Tool**: Searches Qdrant Cloud and retrieves context chunks |
| [`.env`](file:///C:/final_year/temp%20project/ai%20course/project/module1/.env) | Configuration credentials (`QDRANT_URL`, `QDRANT_API_KEY`, `GROQ_API_KEY`) |

---

## 3. How to Run

### Run Entire Pipeline End-to-End
```bash
cd "C:\final_year\temp project\ai course\project\module1"
uv run python main.py --all
```

### Run Individual Stages

#### Stage 1: Download Resources
```bash
# Download all technologies (default 50 pages each)
uv run python 01_download_resources.py

# Download specific technology with custom page limit
uv run python 01_download_resources.py --tech React.js --limit 40
uv run python 01_download_resources.py --tech pandas --limit 40

# Extract transcript from a YouTube video
uv run python 01_download_resources.py --youtube "https://www.youtube.com/watch?v=..." --youtube-out "transcript.md"
```

#### Stage 2: Clean and Organize
```bash
uv run python 02_clean_resources.py
```

#### Stage 3: Extract and Prepare Qdrant Points
```bash
uv run python 03_extract_and_prepare.py
```

#### Stage 4: Push to Qdrant Cloud
```bash
uv run python 04_push_to_qdrant.py
```

---

## 4. Master Code Syntax Assistant (LLM Generation)

Use `master.py` to query the AI assistant grounded in your Qdrant documentation:

```bash
# 1. Ask a syntax/code question with technology filter
uv run python master.py "How do I define a path parameter with validation?" --tech FastAPI
uv run python master.py "How do I filter rows with multiple conditions?" --tech pandas
uv run python master.py "How do I pass props and use useState?" --tech React.js

# 2. Interactive developer mode (chat continuous)
uv run python master.py --interactive
```

---

## 5. Querying & Accessing Raw Points (RAG Context)

### CLI Query
```bash
# Filtered by technology
uv run python query_rag.py "How do I define path parameters?" --tech FastAPI
uv run python query_rag.py "How do I merge dataframes?" --tech pandas

# Global semantic search
uv run python query_rag.py "What is semantic search?"
```

### Python RAG Implementation
```python
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding

load_dotenv()
client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))
model = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

query = "How to define path parameters in FastAPI?"
vector = list(model.embed([query]))[0].tolist()

results = client.query_points(
    collection_name="tech_documentation",
    query=vector,
    query_filter=models.Filter(
        must=[models.FieldCondition(key="technology", match=models.MatchValue(value="FastAPI"))]
    ),
    limit=3,
    with_payload=True
)

context = "\n\n---\n\n".join(pt.payload["content"] for pt in results.points)
print(context)
```
