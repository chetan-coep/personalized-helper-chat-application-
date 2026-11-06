"""
Stage 1: Resource Downloader
Downloads official technical documentation and multi-modal resources (web docs, sitemaps, YouTube).

Features:
- Dual discovery: Sitemap parsing + BFS link crawler fallback.
- Scope-constrained path and English-only language filtering.
- Multi-modal support: YouTube transcript extraction via yt-dlp & faster-whisper.
"""

import sys
import re
import json
import time
import hashlib
import argparse
from pathlib import Path
from urllib.parse import urlparse, urljoin, urldefrag
import xml.etree.ElementTree as ET

import requests
import trafilatura
import lxml.html
from tqdm import tqdm

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "document"
MANIFEST_FILE = OUTPUT_DIR / "manifest.json"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
REQUEST_TIMEOUT = 20
REQUEST_DELAY = 0.4
MAX_RETRIES = 3
DEFAULT_MAX_PAGES = 50

NON_ENGLISH_PATH_PARTS = {
    "de", "es", "fr", "it", "ja", "ko", "pt", "pt-br", "ru",
    "zh", "zh-cn", "zh-tw", "sk", "fa", "uk", "nl", "pl", "tr"
}

session = requests.Session()
session.headers.update({
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
})

# Curated Documentation Sources
SOURCES = {
    "Languages": {
        "C++": {
            "url": "https://en.cppreference.com/w/cpp",
            "scope_prefix": "https://en.cppreference.com/w/cpp",
            "aliases": ["https://en.cppreference.com/cpp"]
        },
        "C": {
            "url": "https://en.cppreference.com/w/c",
            "scope_prefix": "https://en.cppreference.com/w/c",
            "aliases": ["https://en.cppreference.com/c"]
        },
        "Python": {
            "url": "https://docs.python.org/3/tutorial/index.html",
            "scope_prefix": "https://docs.python.org/3/"
        },
        "JavaScript": {
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
            "scope_prefix": "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
        },
        "TypeScript": {
            "url": "https://www.typescriptlang.org/docs/",
            "scope_prefix": "https://www.typescriptlang.org/docs/"
        },
        "SQL": {
            "url": "https://www.postgresql.org/docs/current/sql.html",
            "scope_prefix": "https://www.postgresql.org/docs/current/"
        },
    },

    "Backend & APIs": {
        "Node.js": {
            "url": "https://nodejs.org/docs/latest/api/",
            "scope_prefix": "https://nodejs.org/docs/latest/api/"
        },
        "Express.js": {
            "url": "https://expressjs.com/en/",
            "scope_prefix": "https://expressjs.com/en/"
        },
        "FastAPI": {
            "url": "https://fastapi.tiangolo.com/",
            "scope_prefix": "https://fastapi.tiangolo.com/"
        },
        "REST APIs": {
            "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP",
            "scope_prefix": "https://developer.mozilla.org/en-US/docs/Web/HTTP"
        },
        "Socket.IO": {
            "url": "https://socket.io/docs/v4/",
            "scope_prefix": "https://socket.io/docs/v4/"
        },
        "JWT": {
            "url": "https://jwt.io/introduction",
            "scope_prefix": "https://jwt.io/introduction"
        },
        "Prisma ORM": {
            "url": "https://www.prisma.io/docs/",
            "scope_prefix": "https://www.prisma.io/docs/"
        },
    },

    "Frontend": {
        "React.js": {
            "url": "https://react.dev/learn",
            "scope_prefix": "https://react.dev/"
        },
        "Vite": {
            "url": "https://vite.dev/guide/",
            "scope_prefix": "https://vite.dev/guide/"
        },
        "TailwindCSS": {
            "url": "https://tailwindcss.com/docs/",
            "scope_prefix": "https://tailwindcss.com/docs/"
        },
        "HTML5": {
            "url": "https://developer.mozilla.org/en-US/docs/Web/HTML",
            "scope_prefix": "https://developer.mozilla.org/en-US/docs/Web/HTML"
        },
        "CSS3": {
            "url": "https://developer.mozilla.org/en-US/docs/Web/CSS",
            "scope_prefix": "https://developer.mozilla.org/en-US/docs/Web/CSS"
        },
        "Leaflet": {
            "url": "https://leafletjs.com/reference.html",
            "scope_prefix": "https://leafletjs.com/"
        },
        "Streamlit": {
            "url": "https://docs.streamlit.io/",
            "scope_prefix": "https://docs.streamlit.io/"
        },
    },

    "Databases": {
        "MySQL": {
            "url": "https://dev.mysql.com/doc/refman/8.4/en/",
            "scope_prefix": "https://dev.mysql.com/doc/refman/8.4/en/"
        },
        "PostgreSQL": {
            "url": "https://www.postgresql.org/docs/current/",
            "scope_prefix": "https://www.postgresql.org/docs/current/"
        },
        "Schema Design": {
            "url": "https://www.postgresql.org/docs/current/ddl.html",
            "scope_prefix": "https://www.postgresql.org/docs/current/ddl"
        },
    },

    "ML & Data": {
        "scikit-learn": {
            "url": "https://scikit-learn.org/stable/",
            "scope_prefix": "https://scikit-learn.org/stable/"
        },
        "XGBoost": {
            "url": "https://xgboost.readthedocs.io/en/stable/",
            "scope_prefix": "https://xgboost.readthedocs.io/en/stable/"
        },
        "pandas": {
            "url": "https://pandas.pydata.org/docs/user_guide/index.html",
            "scope_prefix": "https://pandas.pydata.org/docs/"
        },
        "NumPy": {
            "url": "https://numpy.org/doc/stable/",
            "scope_prefix": "https://numpy.org/doc/stable/"
        },
        "SHAP": {
            "url": "https://shap.readthedocs.io/en/latest/",
            "scope_prefix": "https://shap.readthedocs.io/en/latest/"
        },
        "RAG": {
            "url": "https://docs.langchain.com/oss/python/langchain/overview",
            "scope_prefix": "https://docs.langchain.com/"
        },
        "LLMs": {
            "url": "https://huggingface.co/docs/transformers/",
            "scope_prefix": "https://huggingface.co/docs/transformers/"
        },
    },

    "Core Concepts": {
        "Data Structures & Algorithms": {
            "url": "https://cp-algorithms.com/",
            "scope_prefix": "https://cp-algorithms.com/"
        },
        "OOP": {
            "url": "https://docs.oracle.com/javase/tutorial/java/concepts/index.html",
            "scope_prefix": "https://docs.oracle.com/javase/tutorial/java/concepts/"
        },
        "DBMS": {
            "url": "https://15445.courses.cs.cmu.edu/fall2022/schedule.html",
            "scope_prefix": "https://15445.courses.cs.cmu.edu/"
        },
        "Operating Systems": {
            "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/",
            "scope_prefix": "https://pages.cs.wisc.edu/~remzi/OSTEP/"
        },
    }
}


def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        try:
            return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


manifest = load_manifest()


def save_manifest():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
    return url.rstrip("/")


def is_english_url(url: str) -> bool:
    path_segments = [seg.lower() for seg in urlparse(url).path.split("/") if seg]
    return not any(seg in NON_ENGLISH_PATH_PARTS for seg in path_segments)


def is_within_scope(url: str, base_url: str, scope_prefix: str, aliases=None) -> bool:
    parsed_base = urlparse(base_url)
    parsed_url = urlparse(url)

    if parsed_url.netloc != parsed_base.netloc:
        return False

    if not is_english_url(url):
        return False

    clean_scope = normalize_url(scope_prefix)
    clean_url = normalize_url(url)
    if clean_url.startswith(clean_scope):
        return True

    if aliases:
        for alias in aliases:
            if clean_url.startswith(normalize_url(alias)):
                return True

    return False


def fetch_url(url: str) -> requests.Response | None:
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT)
            if resp.status_code >= 400:
                return None
            return resp
        except requests.RequestException:
            if attempt == MAX_RETRIES - 1:
                return None
            time.sleep(1.2 ** attempt)
    return None


def extract_markdown_content(html: str, url: str) -> tuple[str, str]:
    title = ""
    try:
        dom = lxml.html.fromstring(html.encode("utf-8", errors="ignore"))
        title_el = dom.xpath("//title/text()")
        if title_el:
            title = title_el[0].strip()
    except Exception:
        pass

    markdown = trafilatura.extract(
        html,
        url=url,
        output_format="markdown",
        include_tables=True,
        include_links=True,
        include_images=False,
        include_comments=False,
        include_formatting=True,
        favor_precision=True
    )
    return (markdown or "", title)


def safe_slug(text: str) -> str:
    text = re.sub(r'[<>:"/\\|?*#]', "_", text)
    text = re.sub(r"\s+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")[:90]


def discover_sitemap_urls(base_url: str) -> list[str]:
    parsed = urlparse(base_url)
    domain_root = f"{parsed.scheme}://{parsed.netloc}"

    candidates = [
        urljoin(domain_root, "/sitemap.xml"),
        urljoin(domain_root, "/sitemap_index.xml"),
        urljoin(domain_root, "/sitemap-index.xml"),
        urljoin(domain_root, "/sitemap-0.xml"),
        urljoin(base_url, "sitemap.xml"),
    ]

    discovered = []

    def parse_sitemap_xml(sitemap_url: str, depth=0):
        if depth > 3:
            return
        resp = fetch_url(sitemap_url)
        if not resp:
            return
        if "html" in resp.headers.get("content-type", "").lower() and "xml" not in resp.headers.get("content-type", "").lower():
            return
        try:
            root = ET.fromstring(resp.content)
        except Exception:
            return

        for elem in root:
            tag = elem.tag.split("}")[-1]
            loc = None
            for child in elem:
                if child.tag.split("}")[-1] == "loc" and child.text:
                    loc = child.text.strip()
                    break
            if not loc:
                continue
            if tag == "sitemap":
                parse_sitemap_xml(loc, depth + 1)
            elif tag == "url":
                discovered.append(loc)

    for c in candidates:
        parse_sitemap_xml(c)
        if discovered:
            break

    return list(dict.fromkeys(discovered))


def crawl_links_bfs(base_url: str, scope_prefix: str, aliases: list, max_pages: int) -> list[str]:
    visited = set()
    queue = [base_url]
    discovered = []

    while queue and len(discovered) < max_pages:
        current_url = queue.pop(0)
        norm_url = normalize_url(current_url)

        if norm_url in visited:
            continue
        visited.add(norm_url)

        if not is_within_scope(norm_url, base_url, scope_prefix, aliases):
            continue

        discovered.append(norm_url)

        resp = fetch_url(norm_url)
        if not resp or "text/html" not in resp.headers.get("content-type", "").lower():
            continue

        try:
            dom = lxml.html.fromstring(resp.content)
            for a in dom.xpath("//a[@href]"):
                href = a.get("href")
                if not href or href.startswith("javascript:") or href.startswith("mailto:"):
                    continue

                full_url = normalize_url(urljoin(norm_url, href))
                if re.search(r"\.(png|jpg|jpeg|gif|svg|pdf|zip|tar|gz|exe|deb|rpm|whl)$", urlparse(full_url).path, re.I):
                    continue

                if is_within_scope(full_url, base_url, scope_prefix, aliases) and full_url not in visited:
                    if full_url not in queue:
                        queue.append(full_url)
        except Exception:
            continue

    return discovered


def download_and_save_doc(url: str, tech_name: str, category: str, doc_order: int, tech_dir: Path) -> dict | None:
    norm_url = normalize_url(url)
    resp = fetch_url(norm_url)
    if not resp or "text/html" not in resp.headers.get("content-type", "").lower():
        return None

    resp.encoding = resp.apparent_encoding or "utf-8"
    markdown, title = extract_markdown_content(resp.text, norm_url)
    if not markdown or len(markdown.strip()) < 120:
        return None

    if not title:
        title = tech_name

    content_hash = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
    doc_id = f"{safe_slug(tech_name).lower()}_{doc_order:03d}"

    parsed = urlparse(norm_url)
    path_slug = safe_slug(parsed.path.strip("/").replace("/", "_")) or "index"
    filename = f"{doc_order:03d}_{path_slug}.md"
    file_path = tech_dir / filename

    now_iso = time.strftime("%Y-%m-%d %H:%M:%S")

    frontmatter = f"""---
id: "{doc_id}"
technology: "{tech_name}"
category: "{category}"
title: "{title}"
doc_order: {doc_order}
source_url: "{norm_url}"
language: "en"
retrieved_at: "{now_iso}"
content_hash: "{content_hash}"
---

# {title}

Source: {norm_url}

---

{markdown}
"""
    file_path.write_text(frontmatter, encoding="utf-8")

    manifest[norm_url] = {
        "id": doc_id,
        "doc_order": doc_order,
        "technology": tech_name,
        "category": category,
        "title": title,
        "file": str(file_path.relative_to(OUTPUT_DIR)),
        "source_url": norm_url,
        "hash": content_hash,
        "last_downloaded": now_iso
    }

    return {
        "id": doc_id,
        "doc_order": doc_order,
        "title": title,
        "file": filename,
        "source_url": norm_url,
        "content_hash": content_hash
    }


def download_technology(tech_name: str, config: dict, category: str, max_pages: int = DEFAULT_MAX_PAGES):
    base_url = config["url"]
    scope_prefix = config.get("scope_prefix", base_url)
    aliases = config.get("aliases", [])

    print(f"\n[{category}] Processing {tech_name}...")
    tech_dir = OUTPUT_DIR / safe_slug(category) / safe_slug(tech_name)
    tech_dir.mkdir(parents=True, exist_ok=True)

    sitemap_urls = discover_sitemap_urls(base_url)
    valid_urls = [u for u in sitemap_urls if is_within_scope(u, base_url, scope_prefix, aliases)]

    if len(valid_urls) < 5:
        print(f"  Sitemap returned {len(valid_urls)} pages. Running Link Crawler fallback...")
        crawler_urls = crawl_links_bfs(base_url, scope_prefix, aliases, max_pages)
        valid_urls = list(dict.fromkeys(valid_urls + crawler_urls))

    if not valid_urls:
        valid_urls = [base_url]

    valid_urls = valid_urls[:max_pages]
    print(f"  Downloading {len(valid_urls)} pages for {tech_name}...")

    toc_docs = []
    order_idx = 1
    for url in tqdm(valid_urls, desc=f"  {tech_name}", unit="doc"):
        try:
            doc_info = download_and_save_doc(url, tech_name, category, order_idx, tech_dir)
            if doc_info:
                toc_docs.append(doc_info)
                order_idx += 1
            save_manifest()
            time.sleep(REQUEST_DELAY)
        except Exception as err:
            print(f"    Failed {url}: {err}")

    (tech_dir / "toc.json").write_text(
        json.dumps({"technology": tech_name, "category": category, "documents": toc_docs}, indent=2),
        encoding="utf-8"
    )
    return toc_docs


# Multi-modal YouTube Extractor
def extract_youtube_transcript(video_url: str, output_path: str = None) -> str:
    """Extracts and transcribes audio from a YouTube video URL."""
    import tempfile
    import yt_dlp
    from faster_whisper import WhisperModel

    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts = {
            "format": "m4a/bestaudio/best",
            "outtmpl": f"{temp_dir}/%(id)s.%(ext)s",
            "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            audio_file = f"{temp_dir}/{info['id']}.mp3"

        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(audio_file)
        text = " ".join(seg.text.strip() for seg in segments)

        if output_path:
            Path(output_path).write_text(text, encoding="utf-8")
        return text


def main():
    parser = argparse.ArgumentParser(description="Stage 1: Download documentation & multimedia resources.")
    parser.add_argument("--tech", type=str, help="Specific technology to download")
    parser.add_argument("--category", type=str, help="Specific category to download")
    parser.add_argument("--limit", type=int, default=DEFAULT_MAX_PAGES, help="Max pages per technology")
    parser.add_argument("--youtube", type=str, help="YouTube URL to transcribe")
    parser.add_argument("--youtube-out", type=str, help="Output markdown path for YouTube transcript")
    args = parser.parse_args()

    if args.youtube:
        print(f"Transcribing YouTube video: {args.youtube}")
        text = extract_youtube_transcript(args.youtube, output_path=args.youtube_out)
        print(f"Transcription complete ({len(text)} chars).")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for cat_name, tech_dict in SOURCES.items():
        if args.category and args.category.lower() not in cat_name.lower():
            continue
        for t_name, cfg in tech_dict.items():
            if args.tech and args.tech.lower() != t_name.lower():
                continue
            download_technology(t_name, cfg, cat_name, max_pages=args.limit)

    save_manifest()
    print("\nStage 1: Resource downloading completed.")


if __name__ == "__main__":
    main()

