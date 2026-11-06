# DocSyntax AI — Developer Code & Documentation Assistant

DocSyntax AI is an AI-powered documentation search and code syntax copilot built for developers who know programming concepts but need quick, accurate syntax and implementation rationale directly grounded in official documentation.

---

## 1. 3-Panel Blueprint Interface

The application interface strictly follows the 3-functional-panel design:

```
┌──────────────────────────────────────────────┬──────────────────────────────────────────────┐
│                                              │                                              │
│  EXPLANATION & WHY TO USE                    │  SYNTAX WITH CODE                            │
│  - Conceptual rationale                      │  - Direct, copyable implementation syntax    │
│  - Concrete use cases ("why to use")         │  - Parameter and type breakdowns             │
│  - Edge-cases, constraints, and gotchas      │  - Full height right panel                   │
│                                              │                                              │
├──────────────────────────────────────────────┤                                              │
│                                              │                                              │
│  USER'S PROMPT FOR THE LLM                   │                                              │
│  - Input bar with [TechName] chip support    │                                              │
│  - "Indexed Technologies" button             │                                              │
│  - Dark / Light mode (natural matte palette) │                                              │
│                                              │                                              │
└──────────────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 2. Project Architecture & Organization

The codebase is organized into three distinct, clean folders:

```
project/
├── backend/                  # Python API, RAG Pipeline & LLM generation
│   ├── .env                  # Secret credentials (ignored in git)
│   ├── .gitignore            # Git rules ignoring .env, .venv, caches
│   ├── 01_download_resources.py  # Stage 1: Documentation & transcript downloader
│   ├── 02_clean_resources.py     # Stage 2: Doc cleaner, frontmatter & TOC generator
│   ├── 03_extract_and_prepare.py # Stage 3: Semantic chunker & UUIDv5 generator
│   ├── 04_push_to_qdrant.py      # Stage 4: Dense vector embedding & Qdrant Cloud push
│   ├── master.py             # Grounded LLM generator (openai/gpt-oss-120b on Groq)
│   ├── query_rag.py          # Fast semantic search client for Qdrant Cloud
│   ├── server.py             # FastAPI server & static file host
│   └── pyproject.toml        # Dependencies managed by uv
│
├── frontend/                 # Client UI (HTML5, CSS3, Vanilla JS)
│   ├── index.html            # 3-panel semantic layout matching blueprint
│   ├── style.css             # Natural, eye-comfortable dark & light themes
│   ├── app.js                # UI controller, state manager & API client
│   └── start_ui.bat          # Standalone frontend viewer
│
├── document/                 # Cleaned documentation, TOC & vector points
│   ├── Core_Concepts/        # OOP, DSA, DBMS, Operating Systems
│   ├── Frontend/             # React.js, TailwindCSS, Streamlit, Vite
│   ├── Backend_&_APIs/       # FastAPI, Express.js, Node.js, Prisma ORM, JWT
│   ├── Languages/            # Python, JavaScript, TypeScript, C, C++, SQL
│   ├── ML_&_Data/            # pandas, NumPy, LLMs, RAG, XGBoost, scikit-learn, SHAP
│   ├── master_toc.json       # Master table of contents across all 24+ technologies
│   └── qdrant_points/        # 12,321 semantic points with dense vectors
│
├── run.bat                   # 1-Click launcher for both backend & frontend
├── .gitignore                # Root gitignore protecting private credentials
└── README.md                 # Complete system documentation
```

---

## 3. Key Capabilities & Guardrails

1. **Strict Documentation Grounding**:
   - Every response is synthesized exclusively from vector embeddings stored in Qdrant Cloud (`tech_documentation` collection).
   - If a user asks questions outside the indexed technologies (e.g., Rust, MongoDB, general binary search algorithms), the model strictly refuses to answer and directs the user to indexed technologies.

2. **24+ Indexed Technologies**:
   - Access the **"Indexed Technologies"** modal on the top bar to inspect all indexed frameworks, languages, and tools.
   - Click any badge to auto-populate the query with a technology filter tag (e.g., `[FastAPI] How to define query parameters?`).

3. **Natural Color Palette**:
   - Carefully tuned light and dark themes using muted, natural parchment and slate-olive tones to eliminate screen glare and eye fatigue during extended coding sessions.

---

## 4. How to Run

### Quick Start (Windows)
Double-click [`run.bat`](file:///C:/final_year/temp%20project/ai%20course/project/run.bat) in the `project/` directory.

### Manual Start
```bash
cd "c:\final_year\temp project\ai course\project\backend"
uv run python server.py
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 5. Environment Variables

Create `project/backend/.env` with your API credentials:
```ini
QDRANT_URL=https://<your-cluster>.qdrant.io
QDRANT_API_KEY=<your-qdrant-api-key>
GROQ_API_KEY=<your-groq-api-key>
```
*(All `.env` files are ignored by git in both `project/.gitignore` and `project/backend/.gitignore`)*

