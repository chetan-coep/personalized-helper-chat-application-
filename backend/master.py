"""
Master RAG Assistant for Developers: Code Syntax & Documentation Answer Generator.

Powered by:
- Vector Database: Qdrant Cloud ('tech_documentation' collection)
- Embeddings: FastEmbed ('sentence-transformers/all-MiniLM-L6-v2')
- LLM: OpenAI model on Groq ('openai/gpt-oss-120b')

Designed specifically for developers who understand programming concepts but need
accurate, copy-pasteable syntax, parameter definitions, and official documentation context.
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dotenv import load_dotenv

# Ensure UTF-8 console output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from groq import Groq
from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding

ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_FILE)

# Configuration
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

COLLECTION_NAME = "tech_documentation"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_GROQ_MODEL = "qwen/qwen3.8-27b"
FALLBACK_GROQ_MODEL = "openai/gpt-oss-20b"


# ==============================================================================
# SYSTEM PROMPT & SPECIFICATIONS FOR CODE & SYNTAX ASSISTANCE
# ==============================================================================

SYSTEM_PROMPT = """
You are an Expert Technical Code & Documentation Assistant built specifically to help software developers search official documentation, understand concepts, and write accurate code without having to memorize syntax.

### STRICT SCOPE & BOUNDARY POLICY (CRITICAL):
You are strictly confined to the official technical documentation provided in the context below.
1. You MUST ONLY answer questions that are directly and explicitly covered in the provided documentation context.
2. If the user's question asks about a technology, language, library, database, algorithm, or concept that is NOT directly documented in the provided context (such as questions about Rust, MongoDB, binary search, or any topic absent from the context chunks), you MUST REFUSE to answer.
3. Under NO circumstances should you use outside general pre-training knowledge to fabricate answers or provide external code for out-of-bounds topics.
4. When a question is out of bounds or not found in the context, you MUST respond ONLY with:
"This topic is outside the scope of the indexed documentation. The knowledge base does not contain official documentation for this query. I can only assist with technologies, syntax, and concepts available in the indexed documentation."

### CRITICAL TEXT FORMATTING & STYLE RULES:
- WRITE ALL EXPLANATIONS IN SIMPLE, CLEAN, HUMAN-READABLE PLAIN TEXT.
- NEVER use LaTeX formatting, LaTeX math syntax ($ or $$), or LaTeX macros (such as \\text{}, \\textbf{}, \\frac{}, \\dots, \\cdot).
- NEVER backslash-escape markdown characters (do NOT write \\*, \\_, \\[, \\], \\$).
- DO NOT clutter explanations with repetitive bold labels or nested markdown asterisks.
- Keep explanations clear, natural, and friendly for developers.

### IN-BOUNDS RESPONSE STRUCTURE:
When the question is covered in the documentation context, structure your answer using these exact section headers:

#### 1. Code Solution
```<language>
# Complete, copy-pasteable code snippet with all necessary imports
```

#### 2. Explanation & Why to Use
Write a clear, direct 2-4 sentence paragraph in plain text explaining what this code does, why a developer should use this approach, and when to use it over alternatives.

Then list 2 to 3 concise bullet points with key advantages:
- Benefit 1 in plain text
- Benefit 2 in plain text
- Benefit 3 in plain text

#### 3. Syntax & Parameter Breakdown
- `parameter_or_function`: Clear, plain text explanation of accepted type, default value, and purpose.

#### 4. Important Caveats & Gotchas
Write 1-2 plain sentences highlighting common pitfalls, version constraints, or edge cases mentioned in the documentation.

#### 5. Official Documentation References
- Source: [Title / Section](source_url)
""".strip()


# ==============================================================================
# RETRIEVAL ENGINE (QDRANT CLOUD) WITH GENERALIZED SEMANTIC MEANING EXTRACTION
# & COSINE SIMILARITY CALCULATION ACROSS ALL DOMAINS
# ==============================================================================

INDEXED_TECHNOLOGIES = [
    "Python", "JavaScript", "TypeScript", "C", "C++", "SQL",
    "FastAPI", "Express.js", "Node.js", "Prisma ORM", "JWT",
    "React.js", "Streamlit", "TailwindCSS", "Vite",
    "pandas", "NumPy", "LLMs", "RAG", "XGBoost", "scikit-learn", "SHAP",
    "Data Structures & Algorithms", "OOP", "MySQL"
]

UNINDEXED_TOPICS_REGEX = [
    r"\bbinary[- ]search\b",
    r"\brust\b",
    r"\bmongodb\b",
    r"\bmongo\b",
    r"\bangular\b",
    r"\bvue(?:js)?\b",
    r"\bkubernetes\b",
    r"\bk8s\b",
    r"\bdocker\b",
    r"\bgraphql\b",
    r"\bredis\b",
    r"\bkafka\b",
    r"\bflutter\b",
    r"\bswift\b",
    r"\bkotlin\b",
    r"\bruby\b",
    r"\brails\b",
    r"\bspring\b",
    r"\bflask\b",
    r"\bdjango\b",
    r"\bhaskell\b",
    r"\belixir\b",
]

SEMANTIC_INTENT_PROMPT = f"""You are a Semantic Technical Intent Extractor for developer documentation.
Our knowledge base contains documentation ONLY for these exact technologies:
{', '.join(INDEXED_TECHNOLOGIES)}

Scope Note:
- Our Data Structures & Algorithms documentation only covers algebraic & number-theory algorithms (binary exponentiation, bit manipulation, euclidean algorithm, discrete log, FFT, Fibonacci). General search/sort algorithms like binary search are NOT indexed.
- Unindexed technologies include Rust, MongoDB, Angular, Vue, Docker, Kubernetes, etc.

Given ANY developer question across ANY domain:
1. If the question asks about an unindexed technology, database, language, or algorithm (such as Rust, MongoDB, binary search, Docker, Angular, etc.), set TECH to 'OUT_OF_BOUNDS'.
2. Otherwise, identify the closest relevant technology from the list above.
3. Formulate a precise, canonical technical documentation search query.

Output format (strictly 2 lines):
TECH: <exact name from the list above, or OUT_OF_BOUNDS>
CANONICAL: <concise technical concept query>"""


class DocumentationRetriever:
    def __init__(self):
        if not QDRANT_URL or not QDRANT_API_KEY:
            raise ValueError("QDRANT_URL and QDRANT_API_KEY must be set in .env")

        self.client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        self.embedding_model = TextEmbedding(model_name=EMBEDDING_MODEL_NAME)
        self.collection_name = COLLECTION_NAME
        self.groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

    def extract_semantic_intent(self, question: str) -> Tuple[Optional[str], str]:
        """
        Analyzes the question regardless of phrasing style or typos across all domains.
        Extracts target technology and a canonical technical search phrase.
        """
        if not self.groq_client:
            return None, question

        try:
            resp = self.groq_client.chat.completions.create(
                model=DEFAULT_GROQ_MODEL,
                messages=[
                    {"role": "system", "content": SEMANTIC_INTENT_PROMPT},
                    {"role": "user", "content": question}
                ],
                max_tokens=300,
                temperature=0.0
            )
            content = resp.choices[0].message.content.strip()
            tech = None
            canonical = question

            for line in content.splitlines():
                line = line.strip()
                if line.upper().startswith("TECH:"):
                    val = line[5:].strip()
                    if "OUT_OF_BOUNDS" in val.upper():
                        tech = "OUT_OF_BOUNDS"
                    elif val in INDEXED_TECHNOLOGIES:
                        tech = val
                    elif "react" in val.lower():
                        tech = "React.js"
                    elif "fastapi" in val.lower():
                        tech = "FastAPI"
                    elif "oop" in val.lower() or "object" in val.lower():
                        tech = "OOP"
                    elif "sql" in val.lower():
                        tech = "SQL"
                    elif "mysql" in val.lower():
                        tech = "MySQL"
                    elif "pandas" in val.lower():
                        tech = "pandas"
                    elif "scikit" in val.lower() or "sklearn" in val.lower():
                        tech = "scikit-learn"
                elif line.upper().startswith("CANONICAL:"):
                    c = line[10:].strip()
                    if c:
                        canonical = c

            self.last_detected_tech = tech
            return tech, canonical
        except Exception:
            return None, question

    def retrieve_context(
        self,
        query: str,
        technology: Optional[str] = None,
        category: Optional[str] = None,
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Extracts semantic meaning, embeds dense vector, and calculates Cosine Similarity in Qdrant.
        Retrieves the highest cosine similarity documentation chunks.
        """
        # 1. Extract semantic meaning across any domain and asking style
        detected_tech, canonical_query = self.extract_semantic_intent(query)
        target_tech = technology or detected_tech

        # 2. Formulate enriched query for cosine similarity embedding
        search_phrase = f"Technology: {target_tech} | {canonical_query}" if target_tech else canonical_query
        query_vector = list(self.embedding_model.embed([search_phrase]))[0].tolist()

        retrieved_points = []
        seen_ids = set()

        # 3. If target technology is identified, run scoped search
        if target_tech:
            scoped_filter = models.Filter(must=[
                models.FieldCondition(key="technology", match=models.MatchValue(value=target_tech))
            ])
            scoped_results = self.client.query_points(
                collection_name=self.collection_name,
                query=query_vector,
                query_filter=scoped_filter,
                limit=top_k,
                with_payload=True
            )
            for pt in scoped_results.points:
                if pt.id not in seen_ids:
                    seen_ids.add(pt.id)
                    retrieved_points.append(pt)

        # 4. Global search across all documentation points
        global_results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k,
            with_payload=True
        )
        for pt in global_results.points:
            if pt.id not in seen_ids:
                seen_ids.add(pt.id)
                retrieved_points.append(pt)

        # 5. Rank strictly by Cosine Similarity score descending
        retrieved_points.sort(key=lambda p: p.score, reverse=True)

        retrieved_docs = []
        for pt in retrieved_points[:top_k]:
            retrieved_docs.append({
                "score": pt.score,
                "technology": pt.payload.get("technology", ""),
                "category": pt.payload.get("category", ""),
                "title": pt.payload.get("title", ""),
                "section": pt.payload.get("section", ""),
                "breadcrumb": pt.payload.get("breadcrumb", ""),
                "source_url": pt.payload.get("source_url", ""),
                "content": pt.payload.get("content", ""),
            })

        return retrieved_docs


# ==============================================================================
# ANSWER GENERATOR (OPENAI MODEL ON GROQ)
# ==============================================================================

class RAGAnswerGenerator:
    def __init__(self, model_name: str = DEFAULT_GROQ_MODEL):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY must be set in .env")

        self.groq_client = Groq(api_key=GROQ_API_KEY)
        self.model_name = model_name
        self.retriever = DocumentationRetriever()

    def format_context_string(self, docs: List[Dict[str, Any]]) -> str:
        """Formats retrieved chunks into structured context for the prompt."""
        if not docs:
            return "No matching documentation found in vector database."

        formatted_parts = []
        for i, d in enumerate(docs, 1):
            header = f"--- [DOCUMENT CHUNK {i}] ---"
            meta = (
                f"Technology: {d['technology']} | Category: {d['category']}\n"
                f"Document: {d['title']}\n"
                f"Section: {d['section']}\n"
                f"Breadcrumb: {d['breadcrumb']}\n"
                f"Source URL: {d['source_url']}\n"
                f"Relevance Score: {d['score']:.4f}"
            )
            content = d['content'].strip()
            formatted_parts.append(f"{header}\n{meta}\n\n{content}")

        return "\n\n" + "\n\n".join(formatted_parts) + "\n\n"

    def generate_answer(
        self,
        question: str,
        technology: Optional[str] = None,
        category: Optional[str] = None,
        top_k: int = 4,
        temperature: float = 0.1
    ) -> Dict[str, Any]:
        """
        Retrieves documentation context from Qdrant and generates an answer using Groq LLM.
        """
        OUT_OF_BOUNDS_MSG = (
            "This topic is outside the scope of the indexed documentation. "
            "The knowledge base does not contain official documentation for this query. "
            "I can only assist with technologies, syntax, and concepts available in the indexed documentation."
        )

        # 0. Early check for explicit unindexed topics (binary search, rust, mongodb, docker, etc.)
        q_lower = question.lower()
        for pat in UNINDEXED_TOPICS_REGEX:
            if re.search(pat, q_lower):
                return {
                    "question": question,
                    "technology": technology,
                    "model_used": self.model_name,
                    "answer": OUT_OF_BOUNDS_MSG,
                    "retrieved_sources": []
                }

        # 1. Retrieve context chunks from Qdrant
        retrieved_docs = self.retriever.retrieve_context(
            query=question,
            technology=technology,
            category=category,
            top_k=top_k
        )

        max_score = max((d["score"] for d in retrieved_docs), default=0.0)
        last_tech = getattr(self.retriever, "last_detected_tech", None)

        if last_tech == "OUT_OF_BOUNDS" or not retrieved_docs or max_score < 0.35:
            return {
                "question": question,
                "technology": technology,
                "model_used": self.model_name,
                "answer": OUT_OF_BOUNDS_MSG,
                "retrieved_sources": []
            }

        # Auto-populate technology from the top retrieved document if not provided
        if not technology and retrieved_docs:
            technology = retrieved_docs[0]["technology"]

        formatted_context = self.format_context_string(retrieved_docs)

        # 2. Build User Prompt with Question and Context
        user_message_content = f"""
# DEVELOPER QUERY:
{question}

# RETRIEVED DOCUMENTATION CONTEXT:
{formatted_context}

Please provide the syntax solution, code snippet, and parameter explanation according to your specifications.
Important Instructions:
- Ground your answer strictly in the provided documentation context.
- Write the explanation in simple, natural plain text without LaTeX symbols ($ or $$), macros, or backslash-escaped characters.
""".strip()

        # 3. Call OpenAI model via Groq API (with automatic model fallback)
        try:
            response = self.groq_client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message_content}
                ],
                temperature=temperature,
                max_tokens=2048,
            )
            actual_model = self.model_name
        except Exception as e:
            fallback = FALLBACK_GROQ_MODEL if self.model_name == DEFAULT_GROQ_MODEL else DEFAULT_GROQ_MODEL
            if "rate_limit" in str(e).lower() or "429" in str(e):
                response = self.groq_client.chat.completions.create(
                    model=fallback,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_message_content}
                    ],
                    temperature=temperature,
                    max_tokens=2048,
                )
                actual_model = fallback
            else:
                raise e

        answer_text = response.choices[0].message.content

        return {
            "question": question,
            "technology": technology,
            "model_used": actual_model,
            "answer": answer_text,
            "retrieved_sources": retrieved_docs
        }


# ==============================================================================
# CLI & INTERACTIVE CHAT MODE
# ==============================================================================

def run_interactive_mode(generator: RAGAnswerGenerator):
    print("=" * 70)
    print("MASTER DOCUMENTATION & CODE SYNTAX COPILOT (Interactive Mode)")
    print(f"Model: {generator.model_name} | Vector DB: Qdrant Cloud")
    print("Type your syntax/coding question below (type 'exit' or 'quit' to stop).")
    print("Tip: You can specify tech filter by prefixing e.g.: '[FastAPI] how to add middleware'")
    print("=" * 70 + "\n")

    while True:
        try:
            user_input = input("Developer Question > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("\nGoodbye and happy coding!")
                break

            tech_filter = None
            query = user_input

            # Check for [Tech] prefix shortcut
            if user_input.startswith("[") and "]" in user_input:
                tech_part, rest = user_input.split("]", 1)
                tech_filter = tech_part.strip("[").strip()
                query = rest.strip()

            print("\nSearching documentation & generating syntax solution...\n")
            result = generator.generate_answer(query, technology=tech_filter)

            print("=" * 70)
            print(result["answer"])
            print("=" * 70 + "\n")

        except KeyboardInterrupt:
            print("\nSession ended.")
            break
        except Exception as err:
            print(f"\nError: {err}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Master Documentation Syntax Assistant (OpenAI model on Groq + Qdrant RAG)"
    )
    parser.add_argument("query", nargs="?", type=str, help="Question or syntax to look up")
    parser.add_argument("--tech", type=str, help="Filter by technology (e.g. FastAPI, pandas, React.js, Express.js)")
    parser.add_argument("--category", type=str, help="Filter by category (e.g. Backend & APIs, ML & Data)")
    parser.add_argument("--top-k", type=int, default=4, help="Number of documentation chunks to retrieve")
    parser.add_argument("--model", type=str, default=DEFAULT_GROQ_MODEL, help="Groq model to use")
    parser.add_argument("--interactive", action="store_true", help="Launch interactive chat mode")

    args = parser.parse_args()

    generator = RAGAnswerGenerator(model_name=args.model)

    if args.interactive or not args.query:
        run_interactive_mode(generator)
    else:
        print(f"\nProcessing Query: '{args.query}'...")
        if args.tech:
            print(f"Technology Filter: {args.tech}")

        result = generator.generate_answer(
            question=args.query,
            technology=args.tech,
            category=args.category,
            top_k=args.top_k
        )

        print("\n" + "=" * 70)
        print(result["answer"])
        print("=" * 70)


if __name__ == "__main__":
    main()
