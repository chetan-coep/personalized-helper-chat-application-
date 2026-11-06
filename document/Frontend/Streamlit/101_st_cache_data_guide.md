---
id: "streamlit_101"
technology: "Streamlit"
category: "Frontend"
title: "Caching in Streamlit: st.cache_data for Computations and Data Loading"
doc_order: 101
source_url: "https://docs.streamlit.io/develop/concepts/architecture/caching"
language: "en"
retrieved_at: "2026-11-03 20:58:00"
content_hash: "streamlit_caching_guide_101"
---

# Caching in Streamlit: st.cache_data

Source: https://docs.streamlit.io/develop/concepts/architecture/caching

---

## What is st.cache_data in Streamlit

In Streamlit, whenever a user interacts with a widget, the entire Python script reruns from top to bottom. To avoid re-executing slow, expensive operations (such as loading CSV/SQL data, fetching APIs, or running ML transformations), use the `@st.cache_data` decorator.

`st.cache_data` caches the returned value in memory. When the function is called with the exact same input arguments, Streamlit skips execution and returns the cached result instantaneously.

---

## How to Cache Expensive Functions with st.cache_data

```python
import streamlit as st
import pandas as pd
import time

# Decorate expensive data fetching or computation
@st.cache_data(ttl=3600, show_spinner="Loading dataset...")
def load_and_transform_data(csv_path: str, min_rows: int = 100) -> pd.DataFrame:
    # Simulate an expensive computation or network call
    time.sleep(2)
    df = pd.read_csv(csv_path)
    filtered = df[df['value'] >= min_rows]
    return filtered

st.title("Streamlit Caching Demo")

# The first call executes the function and caches the result
# Subsequent reruns retrieve the data from cache in under 1ms!
data = load_and_transform_data("sales_data.csv", min_rows=50)

st.dataframe(data)

# Manual cache invalidation button
if st.button("Clear Cache"):
    st.cache_data.clear()
    st.success("Cache cleared!")
```

---

## Key Parameters of @st.cache_data

- `ttl` (Time to live): Maximum seconds to keep an entry in cache before expiring (e.g. `ttl=3600` for 1 hour, or `ttl="1h"`).
- `max_entries`: Maximum number of unique return values to keep in the cache. Older entries are evicted when limit is reached.
- `show_spinner`: Boolean or string message displayed while the function is executing (default is `True`).
- `persist`: Persist cache to local disk (`"disk"`) so cached data survives server restarts.

