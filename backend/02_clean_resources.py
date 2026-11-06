"""
Stage 2: Resource Cleaner & Sequencer
Cleans documentation files, removes non-English / junk files, normalizes encoding,
and organizes documentation into contiguous sequential order (001_..., 002_...).
Generates per-technology toc.json and root master_toc.json.
"""

import json
import re
import hashlib
from pathlib import Path
from typing import Tuple, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "document"
MASTER_TOC_FILE = DOCS_DIR / "master_toc.json"

NON_ENGLISH_PATTERNS = [
    r"_de_", r"_de\.", r"/de/",
    r"_es_", r"_es\.", r"/es/",
    r"_fr_", r"_fr\.", r"/fr/",
    r"_ja_", r"_ja\.", r"/ja/",
    r"_zh[-_]cn", r"_zh\.", r"/zh/",
    r"_ru_", r"_ru\.", r"/ru/",
    r"_pt[-_]br", r"_pt\.", r"/pt/",
    r"_ko_", r"_ko\.", r"/ko/",
]

IRRELEVANT_KEYWORDS = [
    "about_contact", "about_rfc-editor", "about_rpc",
    "authors_ise", "authors_rfc", "authors_independent",
    "authors_style", "materials_editorial", "materials_format",
]


def is_non_english(text: str) -> bool:
    t = text.lower()
    return any(re.search(pat, t) for pat in NON_ENGLISH_PATTERNS)


def is_irrelevant_file(name: str) -> bool:
    name_low = name.lower()
    return any(k in name_low for k in IRRELEVANT_KEYWORDS)


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

    # If title not found in frontmatter, extract first header
    title = frontmatter.get("title")
    if not title:
        m = re.search(r"^#{1,3}\s+(.+)$", body, re.MULTILINE)
        if m:
            title = m.group(1).strip()
    frontmatter["title"] = title or "Documentation"
    return frontmatter, body


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = re.sub(r"\s+", "_", name)
    return name[:100].strip("_")


def clean_and_organize(dry_run: bool = False):
    print("=" * 65)
    print("STAGE 2: CLEANING & ORGANIZING RESOURCES")
    print(f"Documentation Directory: {DOCS_DIR}")
    print("=" * 65)

    if not DOCS_DIR.exists():
        print(f"Directory {DOCS_DIR} does not exist.")
        return

    purged_count = 0
    organized_docs = {}

    for category_dir in sorted(DOCS_DIR.iterdir()):
        if not category_dir.is_dir() or category_dir.name in ["qdrant_points", "__pycache__"]:
            continue

        category = category_dir.name
        organized_docs[category] = {}

        for tech_dir in sorted(category_dir.iterdir()):
            if not tech_dir.is_dir():
                continue

            tech = tech_dir.name
            md_files = sorted(tech_dir.glob("*.md"))
            valid_files = []

            for f in md_files:
                name = f.name
                if is_non_english(name) or is_irrelevant_file(name):
                    if not dry_run:
                        f.unlink()
                    purged_count += 1
                    continue
                valid_files.append(f)

            # Sort files logically (indexes and tutorials first)
            def doc_sort_key(p: Path):
                s = p.stem.lower()
                if "index" in s or "overview" in s or "intro" in s:
                    return (0, s)
                if "getting_started" in s or "tutorial" in s or "quickstart" in s:
                    return (1, s)
                if "guide" in s or "learn" in s:
                    return (2, s)
                if "api" in s or "reference" in s:
                    return (3, s)
                return (4, s)

            valid_files.sort(key=doc_sort_key)

            tech_toc = []
            order_counter = 1

            for f in valid_files:
                content = f.read_text(encoding="utf-8", errors="replace")
                fm, body = extract_frontmatter(content)

                source_url = fm.get("source_url", "")
                tech_name = fm.get("technology", tech)
                category_name = fm.get("category", category)
                title = fm.get("title", f.stem)
                doc_id = f"{sanitize_filename(tech).lower()}_{order_counter:03d}"
                content_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()

                new_frontmatter = f"""---
id: "{doc_id}"
technology: "{tech_name}"
category: "{category_name}"
title: "{title}"
doc_order: {order_counter}
source_url: "{source_url}"
language: "en"
retrieved_at: "{fm.get('retrieved_at', '')}"
content_hash: "{content_hash}"
---

"""
                clean_document = new_frontmatter + body

                slug = sanitize_filename(f.stem)
                slug = re.sub(rf"^{re.escape(tech)}_+", "", slug, flags=re.IGNORECASE)
                slug = re.sub(r"^\d+_+", "", slug)
                new_filename = f"{order_counter:03d}_{slug}.md"
                new_path = tech_dir / new_filename

                if not dry_run:
                    if f != new_path and new_path.exists():
                        new_path.unlink()
                    new_path.write_text(clean_document, encoding="utf-8")
                    if f != new_path and f.exists():
                        f.unlink()

                tech_toc.append({
                    "id": doc_id,
                    "doc_order": order_counter,
                    "title": title,
                    "file": new_filename,
                    "source_url": source_url,
                    "content_hash": content_hash
                })
                order_counter += 1

            organized_docs[category][tech] = {
                "total_documents": len(tech_toc),
                "documents": tech_toc
            }

            if not dry_run:
                (tech_dir / "toc.json").write_text(
                    json.dumps({"technology": tech, "category": category, "documents": tech_toc}, indent=2),
                    encoding="utf-8"
                )

    if not dry_run:
        MASTER_TOC_FILE.write_text(json.dumps(organized_docs, indent=2), encoding="utf-8")

    print(f"\nCleanup Summary:")
    print(f"Purged Non-English/Junk Files: {purged_count}")
    for cat, techs in organized_docs.items():
        print(f"\n[{cat}]")
        for t, d in techs.items():
            print(f"  - {t}: {d['total_documents']} ordered documents")
    print(f"\nMaster TOC saved to: {MASTER_TOC_FILE}")


if __name__ == "__main__":
    clean_and_organize()

