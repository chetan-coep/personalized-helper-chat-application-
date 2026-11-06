---
id: "rag_025"
technology: "RAG"
category: "ML & Data"
title: "Quickstart - Docs by LangChain"
doc_order: 25
source_url: "https://docs.langchain.com/oss/javascript/deepagents/quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:17"
content_hash: "b9ff173bcdaa6dc1d1d1b8c98aa79584e82680b2b20e980b9c872001a0517acf"
---

# Quickstart - Docs by LangChain

Source: https://docs.langchain.com/oss/javascript/deepagents/quickstart

---

This guide walks you through creating your first deep agent with the Deep Agents SDK. Use the SDK for maximum flexibility and host agents yourself or run a custom

[LangSmith Deployment](https://docs.langchain.com/langsmith/deployment). To run agents in production without having to manage infrastructure, see the

[Managed Deep Agents quickstart](https://docs.langchain.com/langsmith/javascript/managed-deep-agents-quickstart)instead. You will build a research agent that can conduct research and write reports.

Build the Deep Agents research quickstart

## Prerequisites

Before you begin, make sure you have an API key from a model provider (e.g., Gemini, Anthropic, OpenAI).
## Step 1: Install dependencies

[Tavily](https://tavily.com/)for search, install the Tavily package as well:

## Step 2: Set up your API keys

- Google
- OpenAI
- Anthropic
- OpenRouter
- Fireworks
- Baseten
- Ollama
- Other

## Step 3: Create a search tool

Google, OpenAI, and Anthropic offer built-in web search tools that run server-side: no extra package or API key needed. Pass a provider tool dict directly to`create_deep_agent`.
- Provider search (recommended)
- Tavily (any provider)

## Step 4: Create a deep agent

Pass your search tool and model to`create_deep_agent`. Pass a `model` string in `provider:model` format, or an [initialized model instance](https://docs.langchain.com/oss/javascript/deepagents/models#configure-model-parameters). See

[supported models](https://docs.langchain.com/oss/javascript/deepagents/models#supported-models)for all providers and

[suggested models](https://docs.langchain.com/oss/javascript/deepagents/models#suggested-models)for tested recommendations.

## Step 5: Set up LangSmith tracing

[agent-based workspace](https://docs.langchain.com/langsmith/agent-registry),

[create an agent](https://docs.langchain.com/langsmith/create-an-agent)once before sending traces. Use

[agent addressing](https://docs.langchain.com/langsmith/log-traces-to-agent)to select its identifier and environment. If an integration requires

`project_name`, use the selected environment’s [`tracer_session_name`](https://docs.langchain.com/langsmith/create-an-agent#use-an-environment-project)as a compatibility value.

[LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-deepagents-quickstart)provides you with visibility into your agent’s execution, allowing you to view tool calls, subagent delegation, and LLM responses. Sign up at

[smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-deepagents-quickstart), create an API key, and set these environment variables:

## Step 6: Run the agent

## How does it work?

Your deep agent automatically:
1. **Conducts research** by calling the `internet_search` tool to gather information.
2. **Manages context** by using file system tools ([`write_file`](https://docs.langchain.com/oss/javascript/deepagents/overview#virtual-filesystem-access), [`read_file`](https://docs.langchain.com/oss/javascript/deepagents/overview#virtual-filesystem-access)) to offload large search results.
3. **Spawns subagents** as needed to delegate complex subtasks to specialized subagents.
4. **Synthesizes a report** to compile findings into a coherent response.

To add structured task planning with

`write_todos`, opt in with [`TodoListMiddleware`](https://reference.langchain.com/javascript/langchain/index/todoListMiddleware). See

[Task planning](https://docs.langchain.com/oss/javascript/deepagents/overview#task-planning).

## Examples

For examples of agents and patterns you can build with Deep Agents, see
[Examples](https://github.com/langchain-ai/deepagents/tree/main/examples).

## Streaming

Deep Agents have built-in
[streaming](https://docs.langchain.com/oss/javascript/langchain/event-streaming)for real-time updates from agent execution using LangGraph. This allows you to observe output progressively and review and debug agent and subagent work, such as tool calls, tool results, and LLM responses.

## Next steps

Now that you’ve built your first deep agent:
- **Customize your agent**: Learn about [customization options](https://docs.langchain.com/oss/javascript/deepagents/customization), including custom system prompts, tools, and subagents.
- **Add long-term memory**: Enable [persistent memory](https://docs.langchain.com/oss/javascript/deepagents/memory) across conversations.
- **Deploy to production**: Use [Managed Deep Agents](https://docs.langchain.com/langsmith/javascript/managed-deep-agents-overview) to create, run, and operate deep agents in LangSmith.
- **Test and evaluate**: Use [LangSmith evaluation](https://docs.langchain.com/langsmith/evaluation-quickstart) to run automated tests and measure your agent’s performance against a dataset.