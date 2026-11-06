"""
FastAPI Server connecting Frontend UI with Master RAG Backend.
Serves the Frontend statically at '/' and provides API endpoints for
querying documentation points and listing supported technologies.
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Optional, List, Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# Ensure backend folder is in path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"
DOCUMENT_DIR = PROJECT_DIR / "document"
MASTER_TOC_FILE = DOCUMENT_DIR / "master_toc.json"

if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

load_dotenv(CURRENT_DIR / ".env")

from master import RAGAnswerGenerator

app = FastAPI(
    title="DocSyntax AI API",
    description="Backend API for Documentation Code & Syntax Search",
    version="1.0.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize generator once on startup
generator = None

try:
    generator = RAGAnswerGenerator()
    print("RAGAnswerGenerator initialized successfully.")
except Exception as e:
    print(f"Warning: RAGAnswerGenerator initialization error: {e}")


# ==============================================================================
# PYDANTIC SCHEMAS
# ==============================================================================

class QueryRequest(BaseModel):
    query: str
    technology: Optional[str] = None
    category: Optional[str] = None
    top_k: Optional[int] = 4


class QueryResponse(BaseModel):
    query: str
    technology: Optional[str] = None
    is_out_of_bounds: bool
    raw_answer: str
    code: Optional[str] = None
    language: Optional[str] = "python"
    concept: Optional[str] = None
    why_to_use: Optional[List[str]] = None
    caveats: Optional[str] = None
    syntax_breakdown: Optional[List[Dict[str, str]]] = None
    sources: Optional[List[Dict[str, Any]]] = None


# ==============================================================================
# HELPER: PARSE & CLEAN LLM ANSWER FOR 3-PANEL UI
# ==============================================================================

def clean_plain_text(text: str) -> str:
    """Removes LaTeX tokens, backslash escapes, and formats clean plain text."""
    if not text:
        return ""
    # Strip LaTeX math environments and delimiters
    t = re.sub(r"\\\[(.*?)\\\]", r"\1", text, flags=re.DOTALL)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.DOTALL)
    t = re.sub(r"\$\$(.*?)\$\$", r"\1", t, flags=re.DOTALL)
    t = re.sub(r"\$([^$\n]+)\$", r"\1", t)

    # Strip LaTeX commands: \text{...}, \textbf{...}, \textit{...}, etc.
    t = re.sub(r"\\(?:text|textbf|textit|texttt|mathrm|mathbf)\{([^}]+)\}", r"\1", t)
    t = re.sub(r"\\(?:dots|ldots|cdots)", "...", t)
    t = re.sub(r"\\(?:times|cdot)", "x", t)

    # Unescape common escaped markdown symbols
    t = t.replace(r"\*", "*").replace(r"\_", "_").replace(r"\[", "[").replace(r"\]", "]")
    t = t.replace(r"\$", "$").replace(r"\\", "")

    return t.strip()


def parse_llm_markdown(raw_answer: str) -> Dict[str, Any]:
    """Parses structured LLM answer into code, explanation, and syntax breakdown."""
    is_out_of_bounds = "outside the scope of the indexed documentation" in raw_answer.lower()

    if is_out_of_bounds:
        return {
            "is_out_of_bounds": True,
            "raw_answer": raw_answer,
            "code": None,
            "language": None,
            "concept": clean_plain_text(raw_answer),
            "why_to_use": [],
            "caveats": "This topic is outside the indexed official documentation.",
            "syntax_breakdown": [],
            "sources": []
        }

    # Extract Code snippet
    code = ""
    language = "python"
    code_match = re.search(r"```([a-zA-Z0-9_\-+]*)\n([\s\S]*?)```", raw_answer)
    if code_match:
        language = code_match.group(1).strip() or "code"
        code = code_match.group(2).strip()

    # Extract Explanation & Why to Use
    concept_lines = []
    why_to_use = []
    caveats = ""

    why_match = re.search(r"(?:####\s*2\.\s*Explanation & Why to Use|\*\*2\.\s*Explanation & Why to Use\*\*|\bExplanation & Why to Use\b)([\s\S]*?)(?:####\s*3|\*\*3\.|####\s*3\.\s*Syntax)", raw_answer)
    if why_match:
        exp_block = why_match.group(1).strip()
        lines = exp_block.splitlines()

        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue

            # Check if this is a bullet point
            if re.match(r"^[-*•]\s+", line_str):
                bullet_text = re.sub(r"^[-*•]\s+", "", line_str)
                # Strip redundant sub-headers like "**Why Use This Approach**:" or "**How It Works**:"
                clean_bullet = re.sub(r"^\*\*.*?\*\*[:–-]?\s*", "", bullet_text).strip()
                clean_bullet = clean_plain_text(clean_bullet)
                if clean_bullet and len(clean_bullet) > 3:
                    why_to_use.append(clean_bullet)
            else:
                # Narrative paragraph line: remove sub-headings like "- **Why Use This Approach**"
                cleaned_line = re.sub(r"^[-*•]\s*", "", line_str)
                cleaned_line = re.sub(r"^\*\*.*?\*\*[:–-]?\s*", "", cleaned_line).strip()
                cleaned_line = clean_plain_text(cleaned_line)
                if cleaned_line:
                    concept_lines.append(cleaned_line)

    concept = "\n\n".join(concept_lines) if concept_lines else ""

    # Extract Caveats
    caveats_match = re.search(r"(?:####\s*4\.\s*Important Caveats & Gotchas|\*\*4\.\s*Important Caveats & Gotchas\*\*|\bImportant Caveats\b)([\s\S]*?)(?:####\s*5|\*\*5\.|\Z)", raw_answer)
    if caveats_match:
        cav_text = caveats_match.group(1).strip()
        cav_lines = [re.sub(r"^[-*•]\s*", "", l).strip() for l in cav_text.splitlines() if l.strip()]
        caveats = clean_plain_text(" ".join(cav_lines))

    # Extract Syntax Breakdown
    syntax_breakdown = []
    syntax_match = re.search(r"(?:####\s*3\.\s*Syntax & Parameter Breakdown|\*\*3\.\s*Syntax & Parameter Breakdown\*\*|\bSyntax & Parameter Breakdown\b)([\s\S]*?)(?:####\s*4|\*\*4\.|\Z)", raw_answer)
    if syntax_match:
        syn_block = syntax_match.group(1).strip()
        items = re.findall(r"(?:^|\n)\s*[-•*]\s*`?([^`:\n]+)`?\s*[:–-]\s*(.+)", syn_block)
        for name, desc in items[:6]:
            syntax_breakdown.append({
                "name": clean_plain_text(name.strip()),
                "desc": clean_plain_text(desc.strip())
            })

    return {
        "is_out_of_bounds": False,
        "raw_answer": raw_answer,
        "code": code,
        "language": language,
        "concept": concept or "Refer to the syntax and documentation breakdown below.",
        "why_to_use": why_to_use[:4] if why_to_use else ["Provides idiomatic, officially documented syntax."],
        "caveats": caveats or "Review parameter types and version compatibility in documentation.",
        "syntax_breakdown": syntax_breakdown
    }


# ==============================================================================
# API ENDPOINTS
# ==============================================================================

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "DocSyntax AI",
        "cluster_connected": bool(os.getenv("QDRANT_URL"))
    }


@app.get("/api/technologies")
def get_supported_technologies():
    """Returns the list of all indexed technologies categorized."""
    if MASTER_TOC_FILE.exists():
        try:
            toc = json.loads(MASTER_TOC_FILE.read_text(encoding="utf-8"))
            categories = []
            total_technologies = 0
            for cat, techs in toc.items():
                if cat == "qdrant_points":
                    continue
                tech_list = []
                for t, data in techs.items():
                    tech_list.append({
                        "name": t,
                        "documents_count": data.get("total_documents", len(data.get("documents", [])))
                    })
                    total_technologies += 1
                categories.append({
                    "category": cat.replace("_&_", " & ").replace("_", " "),
                    "raw_category": cat,
                    "technologies": sorted(tech_list, key=lambda x: x["name"])
                })
            return {
                "total_technologies": total_technologies,
                "categories": categories
            }
        except Exception as e:
            print(f"Error reading master_toc: {e}")

    # Fallback list of curated technologies
    return {
        "total_technologies": 24,
        "categories": [
            {
                "category": "Languages",
                "technologies": [{"name": t} for t in ["Python", "JavaScript", "TypeScript", "C", "C++", "SQL"]]
            },
            {
                "category": "Backend & APIs",
                "technologies": [{"name": t} for t in ["FastAPI", "Express.js", "Node.js", "Prisma ORM", "JWT", "REST APIs", "Socket.IO"]]
            },
            {
                "category": "Frontend",
                "technologies": [{"name": t} for t in ["React.js", "Streamlit", "TailwindCSS", "Vite", "HTML5", "CSS3", "Leaflet"]]
            },
            {
                "category": "ML & Data",
                "technologies": [{"name": t} for t in ["pandas", "NumPy", "LLMs", "RAG", "XGBoost", "scikit-learn", "SHAP"]]
            },
            {
                "category": "Core Concepts",
                "technologies": [{"name": t} for t in ["Data Structures & Algorithms", "OOP", "DBMS", "Operating Systems"]]
            }
        ]
    }


@app.post("/api/query", response_model=QueryResponse)
def execute_query(req: QueryRequest):
    if not generator:
        raise HTTPException(status_code=500, detail="Backend RAG generator is not initialized.")

    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        result = generator.generate_answer(
            question=req.query,
            technology=req.technology,
            category=req.category,
            top_k=req.top_k or 4
        )

        parsed = parse_llm_markdown(result["answer"])

        # Format sources
        sources = []
        for s in result.get("retrieved_sources", []):
            sources.append({
                "title": s.get("title"),
                "section": s.get("section"),
                "source_url": s.get("source_url"),
                "technology": s.get("technology"),
                "breadcrumb": s.get("breadcrumb")
            })

        return QueryResponse(
            query=req.query,
            technology=req.technology,
            is_out_of_bounds=parsed["is_out_of_bounds"],
            raw_answer=result["answer"],
            code=parsed["code"],
            language=parsed["language"],
            concept=parsed["concept"],
            why_to_use=parsed["why_to_use"],
            caveats=parsed["caveats"],
            syntax_breakdown=parsed["syntax_breakdown"],
            sources=sources
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing query: {str(e)}")


# ==============================================================================
# MOUNT FRONTEND STATIC FILES
# ==============================================================================

if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    print("\n" + "=" * 65)
    print("STARTING DOCSYNTAX AI APPLICATION SERVER")
    print("Frontend & API running on: http://localhost:8000")
    print("=" * 65 + "\n")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=False)

