"""
Master Documentation & Qdrant RAG Pipeline Orchestrator.

Pipeline Flow:
  Stage 1: Download Resources  (01_download_resources.py)
  Stage 2: Clean Resources     (02_clean_resources.py)
  Stage 3: Extract & Prepare   (03_extract_and_prepare.py)
  Stage 4: Push to Qdrant      (04_push_to_qdrant.py)

Usage:
  # Run entire pipeline end-to-end
  uv run python main.py --all

  # Run specific stages
  uv run python main.py --clean --prepare --push
  uv run python main.py --download --tech React.js --limit 30
"""

import sys
import time
import argparse
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

# Import individual stages
from importlib import import_module
stage1 = import_module("01_download_resources")
stage2 = import_module("02_clean_resources")
stage3 = import_module("03_extract_and_prepare")
stage4 = import_module("04_push_to_qdrant")


def run_pipeline(
    do_download: bool = False,
    do_clean: bool = False,
    do_prepare: bool = False,
    do_push: bool = False,
    tech: str = None,
    category: str = None,
    limit: int = 50,
    push_limit: int = None,
    recreate: bool = False
):
    print("=" * 70)
    print("RAG DOCUMENTATION & QDRANT PIPELINE")
    print("=" * 70)

    start_time = time.time()

    # Stage 1: Download
    if do_download:
        print("\n>>> STAGE 1: DOWNLOADING RESOURCES...")
        for cat_name, tech_dict in stage1.SOURCES.items():
            if category and category.lower() not in cat_name.lower():
                continue
            for t_name, cfg in tech_dict.items():
                if tech and tech.lower() != t_name.lower():
                    continue
                stage1.download_technology(t_name, cfg, cat_name, max_pages=limit)
        stage1.save_manifest()

    # Stage 2: Clean
    if do_clean:
        print("\n>>> STAGE 2: CLEANING & ORGANIZING RESOURCES...")
        stage2.clean_and_organize()

    # Stage 3: Extract & Prepare
    if do_prepare:
        print("\n>>> STAGE 3: EXTRACTING & PREPARING POINTS...")
        stage3.extract_and_prepare_all(category_filter=category, tech_filter=tech)

    # Stage 4: Push to Qdrant
    if do_push:
        print("\n>>> STAGE 4: PUSHING POINTS TO QDRANT CLOUD...")
        stage4.push_points_to_qdrant(limit=push_limit, recreate=recreate)

    elapsed = round(time.time() - start_time, 1)
    print("\n" + "=" * 70)
    print(f"PIPELINE RUN COMPLETED IN {elapsed}s!")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="Master RAG Documentation Pipeline.")
    parser.add_argument("--all", action="store_true", help="Run all 4 stages end-to-end")
    parser.add_argument("--download", action="store_true", help="Run Stage 1: Download resources")
    parser.add_argument("--clean", action="store_true", help="Run Stage 2: Clean resources")
    parser.add_argument("--prepare", action="store_true", help="Run Stage 3: Extract & prepare Qdrant points")
    parser.add_argument("--push", action="store_true", help="Run Stage 4: Push points to Qdrant")
    parser.add_argument("--tech", type=str, help="Filter by technology name")
    parser.add_argument("--category", type=str, help="Filter by category name")
    parser.add_argument("--limit", type=int, default=50, help="Max download pages per technology")
    parser.add_argument("--push-limit", type=int, default=None, help="Max points to upload to Qdrant")
    parser.add_argument("--recreate", action="store_true", help="Recreate Qdrant collection on push")
    args = parser.parse_args()

    # If no flags passed, default to --all
    if not (args.all or args.download or args.clean or args.prepare or args.push):
        args.all = True

    run_pipeline(
        do_download=args.all or args.download,
        do_clean=args.all or args.clean,
        do_prepare=args.all or args.prepare,
        do_push=args.all or args.push,
        tech=args.tech,
        category=args.category,
        limit=args.limit,
        push_limit=args.push_limit,
        recreate=args.recreate
    )


if __name__ == "__main__":
    main()

