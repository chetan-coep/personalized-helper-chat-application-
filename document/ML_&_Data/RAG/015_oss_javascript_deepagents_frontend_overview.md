---
id: "rag_015"
technology: "RAG"
category: "ML & Data"
title: "Overview - Docs by LangChain"
doc_order: 15
source_url: "https://docs.langchain.com/oss/javascript/deepagents/frontend/overview"
language: "en"
retrieved_at: "2026-11-03 17:58:15"
content_hash: "e613126ad7c1430ae914976e9ef430983b7103f1ef87017ece4937d86713753d"
---

# Overview - Docs by LangChain

Source: https://docs.langchain.com/oss/javascript/deepagents/frontend/overview

---

Build frontends that visualize deep agent workflows in real time. These patterns show how to render subagent progress, task planning, streaming content, and IDE-like sandbox experiences from agents created with

`createDeepAgent`.
Deep agents are most useful when the UI makes delegation visible. Instead of
showing a single opaque assistant bubble, the LangChain SDKs expose the
coordinator, subagent discovery, custom state, and sandbox-backed artifacts so
users can inspect how a long-running task is being decomposed and completed.
## Architecture

Deep Agents use a coordinator-worker architecture. The main agent plans tasks and delegates to specialized subagents, each running in isolation. On the frontend, the v1 stream handle surfaces coordinator messages on the root stream and exposes subagent discovery snapshots for scoped subagent views.
[`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream)the same way as with

`createAgent`. Pass a [type parameter](https://docs.langchain.com/oss/javascript/langchain/frontend/overview)for type-safe stream state. Deep agent patterns use

`stream.subagents`, selector helpers such as `useMessages(stream, subagent)`, and custom state values like `stream.values.todos` to render subagent-specific UIs.
## What the SDK exposes

Deep agent UIs usually need more than the final answer. The frontend SDK gives you structured projections for the parts of the run users care about:
## Patterns

## Subagent streaming

## Todo list

## Sandbox

## Related patterns

The
[LangChain frontend patterns](https://docs.langchain.com/oss/javascript/langchain/frontend/overview), including markdown messages, tool calling, and human-in-the-loop, all work with deep agents too. Deep Agents are built on the same LangGraph runtime, so

`useStream` provides the same core API.
For lower-level graph visualizations, see the
[LangGraph frontend patterns](https://docs.langchain.com/oss/javascript/langgraph/frontend/overview). They show how to map graph nodes and state keys directly to UI components.