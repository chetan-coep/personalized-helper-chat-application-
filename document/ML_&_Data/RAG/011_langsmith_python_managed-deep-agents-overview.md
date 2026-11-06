---
id: "rag_011"
technology: "RAG"
category: "ML & Data"
title: "Managed Deep Agents - Docs by LangChain"
doc_order: 11
source_url: "https://docs.langchain.com/langsmith/python/managed-deep-agents-overview"
language: "en"
retrieved_at: "2026-11-03 17:58:09"
content_hash: "bf8a7a7d00569be9d9fd910f86eec277149e8a5ad021a6795dddc635fb33b077"
---

# Managed Deep Agents - Docs by LangChain

Source: https://docs.langchain.com/langsmith/python/managed-deep-agents-overview

---

Managed Deep Agents (MDA) is the simplest way to build and deploy production agents. You focus on what your agent does. MDA runs it. There are no servers to run and no infrastructure to wire together. You write the agent’s intelligence: its instructions, the tools it can call, the skills it follows, and you select the model that drives it. MDA provides everything underneath:

- **The Deep Agents harness**: The agent loop that plans, calls tools, manages a filesystem, and delegates to subagents. See [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview).
- **A managed runtime**: Every deployment runs on [LangSmith Agent Server](https://docs.langchain.com/langsmith/agent-server-overview). You get the Agent Server API, threads, runs, streaming, and the [MCP endpoint](https://docs.langchain.com/langsmith/python/managed-deep-agents-mcp-endpoint) without operating the server yourself.

## Example agent

A managed deep agent consists of a project folder that contains the business logic for its behavior:
- Model & configuration
- Instructions
- Skills
- Tools
- Middleware
- MCP Connectors

`mda` CLI, it will automatically run on managed LangSmith infrastructure.
You provide the business logic, and Managed Deep Agents provides the agent harness and production infrastructure.
To get started, see the [Managed Deep Agents quickstart](https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart).

## Core capabilities

Each part of the agent maps to a file or directory. Add the ones your agent needs:
[Project structure](https://docs.langchain.com/langsmith/python/managed-deep-agents-project-structure). Instructions, skills, and optional durable memory are stored in

[Context Hub](https://docs.langchain.com/langsmith/python/managed-deep-agents-context-hub).

## Relationship to Deep Agents

Managed Deep Agents runs the open source
[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)harness rather than a second framework. The agent loop, filesystem tools, subagents, and skills are the same, so there is no second API to learn and an agent you already built keeps working. Managed Deep Agents adds the layer around the agent. The sandbox, durable memory, channels, and schedules above are declarations in a project file rather than services you build and operate.

[Connections](https://docs.langchain.com/langsmith/python/managed-deep-agents-connections)run OAuth, so end users authorize their own accounts instead of you provisioning credentials for each one. LangSmith hosts the result on

[Agent Server](https://docs.langchain.com/langsmith/agent-server-overview). In the code, the difference is narrower: who compiles the agent.

- [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) returns a compiled agent. You run it, and you own the backend, store, checkpointer, and server around it.
- `define_deep_agent` returns a definition. The `mda` CLI hands it to the managed runtime, which supplies those pieces along with memory, skills, and the system prompt, then compiles the agent with [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent).

So

`define_deep_agent` takes the same parameters minus the managed ones, plus a required static `name`. Every `define_*` function works this way: declare what the agent needs, and leave the lifecycle to the runtime.
Start with Managed Deep Agents to run production agents without having to manage infrastructure. Alternatively, for maximum flexibility while using the same Deep Agents harness, use the [Deep Agents SDK](https://docs.langchain.com/oss/python/deepagents/overview#self-host-with-the-sdk)and host agents yourself, or run a custom

[LangSmith Deployment](https://docs.langchain.com/langsmith/deployment). For a side-by-side comparison and steps to convert an agent you already built, see

[Move from Deep Agents](https://docs.langchain.com/langsmith/python/managed-deep-agents-migrate).

## Next steps

## Quickstart

`mda` CLI.