---
id: "rag_021"
technology: "RAG"
category: "ML & Data"
title: "Tracing quickstart - Docs by LangChain"
doc_order: 21
source_url: "https://docs.langchain.com/langsmith/observability-quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:07"
content_hash: "4d182c5e71e11b6305a2080fb34193ff00222d58ad8e086bf5e3a9dc1b185ee5"
---

# Tracing quickstart - Docs by LangChain

Source: https://docs.langchain.com/langsmith/observability-quickstart

---

LangSmith gives you end-to-end visibility into your agent by capturing

[*traces*](https://docs.langchain.com/langsmith/observability-concepts#traces); a complete record of every step that ran during a request, from the inputs passed in to the final output returned. In this quickstart, you will add tracing to an AI assistant and view the results in LangSmith. Traces belong to an

[agent and one of its environments](https://docs.langchain.com/langsmith/agent-registry)within a workspace. This quickstart creates the agent in LangSmith, then configures your code to send traces to its identifier and environment. Compatibility instructions cover older workspaces and self-hosted LangSmith.

## Prerequisites

Before you begin, make sure you have:
- **A LangSmith account**: Sign up or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-observability-quickstart).
- **A LangSmith API key**: Follow the [Create an API key](https://docs.langchain.com/langsmith/create-account-api-key) guide.
- **A model provider API key**: Generate one from the [OpenAI dashboard](https://platform.openai.com/account/api-keys), the [Claude Console](https://platform.claude.com/settings/keys), or [Google AI Studio](https://aistudio.google.com/apikey) for Gemini.

Select your provider in the tabs on each step. The Anthropic and Gemini examples are in Python and TypeScript only, because the LangSmith Java SDK wraps only the OpenAI client.

## 1. Set up your environment

1. 
Create a directory for your agent code, install the dependencies, and configure the required environment variables:
  - OpenAI
  - Anthropic
  - Gemini
2. 
Export your environment variables in your shell:
  - OpenAI
  - Anthropic
  - Gemini

   Before sending traces, create the agent in LangSmith:
  1. 
In an [agent-based workspace](https://docs.langchain.com/langsmith/agent-registry), open **+ Agent**, choose **Observability**, and create an agent with an **Agent name** and **Agent ID**. This requires the `projects:create` permission. If the agent already exists, reuse it.
  2. 
Copy the **Agent ID** and choose an environment: `local`, `development`, `staging`, or `production`.
  3. 
Configure [agent addressing](https://docs.langchain.com/langsmith/log-traces-to-agent) before running the agent:

   Register the agent once, not for every trace. Remove`LANGSMITH_PROJECT`, `LANGCHAIN_PROJECT`, and `LANGCHAIN_SESSION` from the environment where your code runs. Do not combine legacy destination settings with agent addressing. To create the agent with an SDK call or API request, see [Create an agent programmatically](https://docs.langchain.com/langsmith/create-an-agent#create-an-agent-programmatically). Project-based workspaces and self-hosted LangSmith Agent addressing is available in agent-based workspaces on LangSmith Cloud. In a project-based workspace, including self-hosted LangSmith, set`LANGSMITH_PROJECT` to your tracing project name instead of setting the two agent variables.If your account is in a region other than US (the default), also set`LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won’t be recognized and requests will fail to authenticate.Region GCP US GCP EU GCP APAC AWS US For example, EU accounts:`export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
For other providers, use the [`@traceable` decorator](https://docs.langchain.com/langsmith/annotate-code#use-%40traceable-%2F-traceable) to trace calls manually.

## 2. Build the app

The following app uses two LangSmith tools to add tracing:
- **Provider wrapper**: wraps the [OpenAI](https://docs.langchain.com/langsmith/trace-openai), [Anthropic](https://docs.langchain.com/langsmith/trace-anthropic), or [Gemini](https://docs.langchain.com/langsmith/trace-with-google-gemini) client so every LLM call is automatically logged as a nested span. The Gemini wrapper is in [beta](https://docs.langchain.com/langsmith/release-stages).
- **Traceable wrapper**: wraps a function so its inputs, outputs, and any nested spans appear as a single trace in LangSmith. Use `@traceable` in Python, `traceable` in TypeScript and Kotlin, and `Tracing.traceFunction` in Java.

The

`assistant` function calls a tool (`get_context`) to retrieve relevant context, then passes that context to the model. Using the traceable wrapper on both functions captures the full pipeline in one trace, with the tool call and LLM call as nested spans.
Create a file called `app.py`, `index.ts`, `App.java`, or `App.kt` with the following code:
- OpenAI
- Anthropic
- Gemini

## 3. Run the app

## 4. View your trace

In the
[LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-observability-quickstart), select your agent, go to

**Tracing**, and select the environment configured during setup. In a project-based workspace, open the project named by

`LANGSMITH_PROJECT`. For more information, see [Navigate agents](https://docs.langchain.com/langsmith/navigate-agents). Click the

`assistant` row to open the trace. The **Trajectory**tab shows the conversation as it was sent to the model. Select the

**Details**tab to see the full run tree, including the

`assistant` function with the `get_context` tool call and the model call nested inside it.
The outer span captures your `assistant` function’s inputs and outputs. The nested **get\_context**span (

**getContext**in TypeScript) records the tool call, and the model span (

**ChatOpenAI**,

**ChatAnthropic**, or

**ChatGoogleGenerativeAI**) records the exact prompt sent to the model and the response returned.

## Next steps

- [Tracing integrations](https://docs.langchain.com/langsmith/integrations): LangChain, LangGraph, Anthropic, and other providers.
- [Trace an agent](https://docs.langchain.com/langsmith/observability-llm-tutorial): a full lifecycle tutorial, from prototyping through production.
- [Filter traces](https://docs.langchain.com/langsmith/filter-traces): search the traces in an agent environment.
- [Log traces to an agent](https://docs.langchain.com/langsmith/log-traces-to-agent): configure the agent and environment in code or with environment variables.
- [Agent Registry](https://docs.langchain.com/langsmith/agent-registry): how workspaces organize agents and their environments.