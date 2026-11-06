"""
Stage 3: Extract & Prepare for Qdrant
Extracts sections from cleaned markdown documents, splits into header-aware
semantic chunks with breadcrumb context, and formats deterministic Qdrant point objects.
Exports points to documentation/qdrant_points/.
"""

import re
import json
import uuid
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "document"
POINTS_DIR = DOCS_DIR / "qdrant_points"

UUID_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
DEFAULT_CHUNK_SIZE = 1800      # ~450 tokens
DEFAULT_CHUNK_OVERLAP = 250    # ~60 tokens


def extract_frontmatter(content: str) -> Tuple[Dict[str, str], str]:
    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1]
            body = parts[2].strip()
            for line in raw_fm.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    frontmatter[k.strip()] = v.strip().strip('"').strip("'")
    return frontmatter, body


def split_sections_by_headings(body: str) -> List[Dict[str, Any]]:
    heading_pattern = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)
    matches = list(heading_pattern.finditer(body))

    if not matches:
        return [{"heading": "Introduction", "level": 1, "text": body.strip()}]

    sections = []
    if matches[0].start() > 0:
        lead_text = body[:matches[0].start()].strip()
        if lead_text:
            sections.append({"heading": "Overview", "level": 1, "text": lead_text})

    for i, match in enumerate(matches):
        level = len(match.group(1))
        heading = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        text = body[start:end].strip()
        sections.append({"heading": heading, "level": level, "text": text})

    return sections


def chunk_sections_with_breadcrumbs(
    sections: List[Dict[str, Any]],
    doc_title: str,
    max_chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP
) -> List[Dict[str, Any]]:
    chunks = []
    breadcrumb = [doc_title]

    for sec in sections:
        heading = sec["heading"]
        level = sec["level"]
        text = sec["text"]

        if level <= 1:
            breadcrumb = [doc_title, heading]
        elif level == 2:
            breadcrumb = [doc_title] + ([breadcrumb[1]] if len(breadcrumb) > 1 else []) + [heading]
        else:
            breadcrumb = breadcrumb[:2] + [heading]

        breadcrumb_str = " > ".join(dict.fromkeys(breadcrumb))
        full_text = f"## {heading}\n\n{text}" if text else f"## {heading}"

        if len(full_text) <= max_chunk_size:
            chunks.append({
                "section": heading,
                "breadcrumb": breadcrumb_str,
                "text": full_text
            })
        else:
            lines = full_text.split("\n")
            current_lines = []
            current_len = 0

            for line in lines:
                l_len = len(line) + 1
                if current_len + l_len > max_chunk_size and current_lines:
                    chunks.append({
                        "section": heading,
                        "breadcrumb": breadcrumb_str,
                        "text": "\n".join(current_lines).strip()
                    })
                    # Overlap
                    keep_lines = []
                    keep_len = 0
                    for rev in reversed(current_lines):
                        if keep_len + len(rev) > overlap:
                            break
                        keep_lines.insert(0, rev)
                        keep_len += len(rev) + 1
                    current_lines = keep_lines
                    current_len = keep_len

                current_lines.append(line)
                current_len += l_len

            if current_lines:
                chunks.append({
                    "section": heading,
                    "breadcrumb": breadcrumb_str,
                    "text": "\n".join(current_lines).strip()
                })

    return chunks


def process_markdown_file(file_path: Path) -> List[Dict[str, Any]]:
    content = file_path.read_text(encoding="utf-8", errors="replace")
    fm, body = extract_frontmatter(content)

    doc_id = fm.get("id", file_path.stem)
    technology = fm.get("technology", file_path.parent.name)
    category = fm.get("category", file_path.parent.parent.name)
    title = fm.get("title", file_path.stem)
    doc_order = int(fm.get("doc_order", 0))
    source_url = fm.get("source_url", "")

    sections = split_sections_by_headings(body)
    raw_chunks = chunk_sections_with_breadcrumbs(sections, doc_title=title)

    points = []
    total_chunks = len(raw_chunks)

    for chunk_idx, ch in enumerate(raw_chunks):
        point_uuid = str(uuid.uuid5(UUID_NAMESPACE, f"{doc_id}:{chunk_idx}"))
        chunk_text = ch["text"]

        point = {
            "id": point_uuid,
            "payload": {
                "point_id": point_uuid,
                "doc_id": doc_id,
                "doc_order": doc_order,
                "chunk_index": chunk_idx,
                "total_chunks": total_chunks,
                "technology": technology,
                "category": category,
                "title": title,
                "section": ch["section"],
                "breadcrumb": ch["breadcrumb"],
                "source_url": source_url,
                "content": chunk_text,
                "char_count": len(chunk_text),
                "token_estimate": len(chunk_text) // 4
            }
        }
        points.append(point)

    return points


def extract_and_prepare_all(category_filter: str = None, tech_filter: str = None):
    print("=" * 65)
    print("STAGE 3: EXTRACTING & PREPARING POINTS FOR QDRANT")
    print("=" * 65)

    POINTS_DIR.mkdir(parents=True, exist_ok=True)
    master_file = POINTS_DIR / "all_qdrant_points.jsonl"

    total_points = 0
    summary = {}

    with master_file.open("w", encoding="utf-8") as master_f:
        for cat_dir in sorted(DOCS_DIR.iterdir()):
            if not cat_dir.is_dir() or cat_dir.name in ["qdrant_points", "__pycache__"]:
                continue

            category = cat_dir.name
            if category_filter and category_filter.lower() not in category.lower():
                continue

            for tech_dir in sorted(cat_dir.iterdir()):
                if not tech_dir.is_dir():
                    continue

                tech = tech_dir.name
                if tech_filter and tech_filter.lower() != tech.lower():
                    continue

                md_files = sorted(tech_dir.glob("*.md"))
                tech_points = []

                for md_file in md_files:
                    pts = process_markdown_file(md_file)
                    tech_points.extend(pts)
                    for p in pts:
                        master_f.write(json.dumps(p) + "\n")

                tech_points_file = POINTS_DIR / f"{category}_{tech}_points.json"
                tech_points_file.write_text(
                    json.dumps({
                        "category": category,
                        "technology": tech,
                        "total_points": len(tech_points),
                        "points": tech_points
                    }, indent=2),
                    encoding="utf-8"
                )

                summary[f"{category}/{tech}"] = len(tech_points)
                total_points += len(tech_points)

    print(f"\nExtraction & Chunking Summary:")
    print(f"Total Points Prepared: {total_points}")
    print(f"Master Points File: {master_file}")
    for k, v in summary.items():
        print(f"  - {k}: {v} points")

    return total_points


def main():
    parser = argparse.ArgumentParser(description="Stage 3: Extract and prepare Qdrant points.")
    parser.add_argument("--category", type=str, help="Filter by category")
    parser.add_argument("--tech", type=str, help="Filter by technology")
    args = parser.parse_args()

    extract_and_prepare_all(category_filter=args.category, tech_filter=args.tech)


if __name__ == "__main__":
    main()

