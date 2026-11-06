---
id: "streamlit_060"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 60
source_url: "https://docs.streamlit.io/develop/api-reference/caching-and-state"
language: "en"
retrieved_at: "2026-11-01 22:27:26"
content_hash: "764d4e820f61d554d29e820cc2a3b5c4334a702da0f3c7d7e87103ad86125b01"
---

# Streamlit

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state

---

# 

Optimize performance and add statefulness to your app!

## 

Streamlit provides powerful [cache primitives](https://docs.streamlit.io/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

[Cache dataFunction decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).Python](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)

[Cache resourceFunction decorator to cache functions that return global resources (e.g. database connections, ML models).Python](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)

## 

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

[ContextPython](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.context)

[Session StateSave data between reruns and across pages.Python](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)

[Query parametersGet, set, or clear the query parameters that are shown in the browser's URL bar.Python](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params)

[*arrow\_back*Previous: Execution flow](https://docs.streamlit.io/develop/api-reference/execution-flow)

[*arrow\_forward*Next: st.cache\_data](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.