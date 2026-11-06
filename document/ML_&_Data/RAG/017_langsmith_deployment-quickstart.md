---
id: "rag_017"
technology: "RAG"
category: "ML & Data"
title: "Deploy your app to cloud - Docs by LangChain"
doc_order: 17
source_url: "https://docs.langchain.com/langsmith/deployment-quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:00"
content_hash: "34b8205b1b09acafc98fdf601ca6ba03cb2ab653fdb6d2e3e651795b2220e778"
---

# Deploy your app to cloud - Docs by LangChain

Source: https://docs.langchain.com/langsmith/deployment-quickstart

---

This quickstart shows you how to deploy an application to LangSmith Cloud in GCP using the

[`langgraph deploy`](https://docs.langchain.com/langsmith/cli#deploy)command. Any app that exports a graph from a

[`langgraph.json`](https://docs.langchain.com/langsmith/application-structure#configuration-file-concepts)config deploys the same way, regardless of which framework you used to author the agent.

## Prerequisites

Before you begin, ensure you have:
- 
A [LangSmith account](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-deployment-quickstart) on the [Plus plan or above](https://www.langchain.com/pricing) and an [API key](https://docs.langchain.com/langsmith/create-account-api-key).
- 
(Optional) **Docker** installed and the Docker daemon running for local builds. Not required for remote builds. [Install Docker Desktop](https://docs.docker.com/get-docker/). If Docker is not available, `langgraph deploy` triggers a remote build automatically.
- 
(Optional) On Apple Silicon (M1/M2/M3): [Docker Buildx](https://docs.docker.com/build/install-buildx/) for cross-compiling to `linux/amd64` during local builds.
- 
The [LangGraph CLI](https://docs.langchain.com/langsmith/cli):

## 1. Create a deployable app

`langgraph deploy` deploys any project whose `langgraph.json` exports a graph. Pick the path that matches how you author your agent:
- LangGraph template
- Bring your own framework

## 2. Set your API key

Add your LangSmith API key to a`.env` file in your project root:
`langgraph deploy` command reads this automatically. Alternatively, pass it inline:
## 3. Deploy

Deploy directly from the CLI or via the UI.
- Deploy from CLI
- Deploy from Studio

`--name` to change the name, or `--deployment-type dedicated` for a [Dedicated deployment](https://docs.langchain.com/langsmith/cloud-platform-features#deployment-types).You can also use

`langgraph deploy list` to see all deployments, `langgraph deploy logs` to tail runtime logs, and `langgraph deploy delete <ID>` to remove a deployment. For details, refer to the [CLI reference](https://docs.langchain.com/langsmith/cli#deploy).

## 4. Test in Studio

[Studio](https://docs.langchain.com/langsmith/studio)is an interactive agent IDE connected directly to your deployment. Use it to send messages, inspect intermediate state at each node, edit state mid-run, and replay from any prior checkpoint without writing code. Once the deployment is ready:

1. Go to [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-deployment-quickstart) and select **Deployments** in the left sidebar.
2. Select your deployment to view its details.
3. Click **Studio** in the top right corner to open [Studio](https://docs.langchain.com/langsmith/studio).

## 5. Test the API

Copy the
**API URL**from the deployment details view, then use it to call your application:

- Python SDK (Async)
- Python SDK (Sync)
- JavaScript SDK
- Rest API

1. Install the LangGraph Python SDK:
2. Send a message to the assistant (stateless run):