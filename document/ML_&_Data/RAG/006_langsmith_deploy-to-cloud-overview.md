---
id: "rag_006"
technology: "RAG"
category: "ML & Data"
title: "Deploy to Cloud - Docs by LangChain"
doc_order: 6
source_url: "https://docs.langchain.com/langsmith/deploy-to-cloud-overview"
language: "en"
retrieved_at: "2026-11-03 17:57:58"
content_hash: "4043a0908a305d13d0908b73ea101a99e132369c2bb50b8b4eb6412cd06655a2"
---

# Deploy to Cloud - Docs by LangChain

Source: https://docs.langchain.com/langsmith/deploy-to-cloud-overview

---

[LangSmith Cloud](https://docs.langchain.com/langsmith/cloud)is a

**managed platform for deploying your agents**. LangChain hosts and operates the

[control plane](https://docs.langchain.com/langsmith/control-plane),

[data plane](https://docs.langchain.com/langsmith/data-plane),

[Agent Server](https://docs.langchain.com/langsmith/agent-server)runtime, and supporting databases on AWS and GCP. Push code to a connected GitHub repository or invoke the

`langgraph deploy` CLI, and the platform handles build, provisioning, scaling, and ongoing operations. Deployments come in [two types](https://docs.langchain.com/langsmith/cloud-platform-features#deployment-types):

- **Serverless**: Scales to zero when idle. Suits background agents, testing, and latency-tolerant production workloads.
- **Dedicated**: Stays on and autoscales across replicas. Suits latency-sensitive production workloads.

## Deploy on Cloud

`langgraph deploy` CLI.
## Cloud platform features

## Quickstart

[Managed Deep Agents](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview)offers a CLI-first managed runtime in public beta.