---
id: "rag_023"
technology: "RAG"
category: "ML & Data"
title: "Managed Deep Agents quickstart - Docs by LangChain"
doc_order: 23
source_url: "https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:10"
content_hash: "52c3f151b95ac49b68e9fcb3aff4b5ebb5e41f57861c782b85d6ad6c0ca44c71"
---

# Managed Deep Agents quickstart - Docs by LangChain

Source: https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart

---

Create and deploy your first Managed Deep Agent: scaffold a project, configure the model and instructions, add search, test in

[LangSmith Studio](https://docs.langchain.com/langsmith/studio), and deploy with the

[`mda` CLI](https://docs.langchain.com/langsmith/python/managed-deep-agents-cli). Managed Deep Agents supplies the

[Deep Agents harness](https://docs.langchain.com/oss/python/deepagents/overview)and hosted runtime. After this quickstart, the

[tutorial](https://docs.langchain.com/langsmith/python/managed-deep-agents-tutorial)adds durable memory and a daily schedule on the same project.

## Prerequisites

To follow along, you need:
- 
Python and `uv`.
- An API key for your model provider of choice.

## Add the `managed-deep-agents` skill

The [`managed-deep-agents` skill](https://github.com/langchain-ai/langchain-skills/blob/main/config/skills/managed-deep-agents/SKILL.md)walks a coding agent through building, testing, and deploying a Managed Deep Agent with the

`mda` CLI. To add it to the current project, run:
Build a Managed Deep Agent with the quickstart

## Create and deploy an agent

Set up the project

Add your keys

`.env`:`mda deploy` adds the provider key to the deployment. You can also use any [other chat provider](https://docs.langchain.com/oss/python/integrations/chat/).

Set up LangSmith

`mda dev`, deploys the agent with `mda deploy`, and opens the agent in [LangSmith Studio](https://docs.langchain.com/langsmith/studio)so you can chat with it and inspect traces.

[Sign up for LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-managed-deep-agents-quickstart)if you do not already have an account.To create a LangSmith API key, open

[Settings](https://smith.langchain.com/settings), go to

**API Keys**, and click

**Create API Key**. For more details, see

[Create an account and API key](https://docs.langchain.com/langsmith/create-account-api-key).Add your LangSmith API key to

`.env`:
Edit the instructions

`instructions.md` and describe how the agent should behave:
[LangSmith Context Hub](https://docs.langchain.com/langsmith/python/managed-deep-agents-context-hub), where you can update them without redeploying the agent.

Configure your model and search

`agent.py`:
[Models](https://docs.langchain.com/oss/python/langchain/models).

## Using another provider?


[Tavily API key](https://app.tavily.com)to

`.env`:`internet_search` tool:
[Custom tools](https://docs.langchain.com/langsmith/python/managed-deep-agents-tools).

Run locally

`mda dev` loads the API keys from `.env`, starts a local Agent Server, and opens the agent in LangSmith Studio.In Studio, send:`agent.py` or `agent.ts`.In an [agent-based workspace](https://docs.langchain.com/langsmith/agent-registry), tracing will result in errors until you register the agent. For details, see

[Trace local runs](https://docs.langchain.com/langsmith/python/managed-deep-agents-local-development#trace-local-runs).

Deploy the agent

[LangSmith Agent Server](https://docs.langchain.com/langsmith/agent-server). When deployment finishes, the CLI prints the deployment dashboard URL.Open that URL. You should see the deployment in a ready state. Send the same research question from the previous step and confirm the hosted agent returns an answer with a search tool call. For deployment options and secrets handling, see

[Deploy a Managed Deep Agent](https://docs.langchain.com/langsmith/python/managed-deep-agents-deploy). To inspect the agent’s execution after it runs, use

[LangSmith observability](https://docs.langchain.com/langsmith/observability-quickstart).