import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from master import RAGAnswerGenerator
from server import parse_llm_markdown

gen = RAGAnswerGenerator()

test_cases = [
    # 10 In-Bounds Tests (Must return is_out_of_bounds = False, valid code & concept)
    ("how to chain feature scaling and logistic regression together in scikit learn", True, "scikit-learn"),
    ("what are the four pillers of oop", True, "OOP"),
    ("how to declare optional query parameters with default values and validation in fastapi", True, "FastAPI"),
    ("what is indexing in sql database and how i can implement it", True, "SQL"),
    ("fastest way to turn column of strings into datetime without erroring in pandas", True, "pandas"),
    ("how to use useState to manage component state in react", True, "React.js"),
    ("how to create a custom logging middleware in express", True, "Express.js"),
    ("how to sign a token with expiration time and verify it in jwt", True, "JWT"),
    ("how to use dataclasses with default factory in python", True, "Python"),
    ("how to cache expensive function results using st.cache_data in streamlit", True, "Streamlit"),

    # 5 Out-of-Bounds Tests (Must return is_out_of_bounds = True, NO code)
    ("explain binary search", False, "Unindexed Algorithm"),
    ("what is rust borrow checker and lifetime annotations", False, "Unindexed Language (Rust)"),
    ("how to write an aggregation pipeline in mongodb with match and group", False, "Unindexed DB (MongoDB)"),
    ("how to use two-way data binding with ngModel in angular", False, "Unindexed Framework (Angular)"),
    ("how to define resource limits in a kubernetes pod deployment yaml", False, "Unindexed DevOps (Kubernetes)"),
]

passed = 0
failed = 0

print("=" * 75, flush=True)
print("RUNNING 15-QUESTION SYSTEM INTEGRITY & BOUNDARY TEST SUITE", flush=True)
print("=" * 75 + "\n", flush=True)

for i, (query, should_be_in_bounds, domain) in enumerate(test_cases, 1):
    t0 = time.time()
    res = gen.generate_answer(query)
    parsed = parse_llm_markdown(res["answer"])
    dt = time.time() - t0

    is_in_bounds = not parsed["is_out_of_bounds"]
    has_code = bool(parsed.get("code"))

    if should_be_in_bounds:
        # Expected: In-Bounds with valid code
        success = is_in_bounds and has_code
        status_label = "PASS" if success else "FAIL"
    else:
        # Expected: Out-of-Bounds (refused) with NO code
        success = (not is_in_bounds) and (not has_code)
        status_label = "PASS" if success else "FAIL"

    if success:
        passed += 1
    else:
        failed += 1

    print(f"[{i:02d}/15] [{status_label}] Domain: {domain}", flush=True)
    print(f"       Query: '{query}'", flush=True)
    print(f"       Result: In-Bounds={is_in_bounds} | Has Code={has_code} | Time: {dt:.2f}s", flush=True)
    if should_be_in_bounds and not success:
        print(f"       ERROR: Expected in-bounds answer, but was refused: {parsed.get('caveats')}", flush=True)
    elif not should_be_in_bounds and not success:
        print(f"       ERROR: Expected refusal, but hallucinated code:\n{parsed.get('code')[:100]}...", flush=True)
    print("-" * 75, flush=True)

print("\n" + "=" * 75, flush=True)
print(f"TEST SUITE SUMMARY: {passed} PASSED, {failed} FAILED (Total: 15)", flush=True)
print("=" * 75, flush=True)

