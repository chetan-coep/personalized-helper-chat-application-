---
id: "rag_007"
technology: "RAG"
category: "ML & Data"
title: "Deploy to self-hosted - Docs by LangChain"
doc_order: 7
source_url: "https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview"
language: "en"
retrieved_at: "2026-11-03 17:57:59"
content_hash: "485d819daed3c67d5464fdb2629ba297ed90770c231d92b8f98e59c204ca813a"
---

# Deploy to self-hosted - Docs by LangChain

Source: https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview

---

Self-hosted LangSmith Deployment runs the

[Agent Server](https://docs.langchain.com/langsmith/agent-server), control plane, data plane, and supporting databases inside infrastructure that you operate. LangChain ships the container images, Helm charts, and license; you provide the Kubernetes cluster (or Docker host), PostgreSQL, Redis, and the networking and observability tooling that fit your environment. Self-hosted is the best deployment option when you have data residency, regulatory constraints, custom networking, or air-gapped requirements.

## Topologies

LangSmith supports three self-hosted topologies that trade off setup complexity against control-plane features. Reference pages for
[platform features](https://docs.langchain.com/langsmith/self-hosted-platform-features),

[Agent Server metrics](https://docs.langchain.com/langsmith/self-hosted-agent-server-metrics), and

[diagnostics](https://docs.langchain.com/langsmith/diagnostics-self-hosted)apply to all three.

## Full self-hosted platform

[control plane](https://docs.langchain.com/langsmith/control-plane)UI and APIs,

[data plane](https://docs.langchain.com/langsmith/data-plane)listener, observability, evaluation, and agent deployment management. Best for teams that want the LangSmith product experience inside their own network.

## Hybrid

## Standalone server

## Platform features

## Agent Server metrics

## Diagnostics

## Who manages what

Self-hosted shifts ownership of infrastructure operations from LangChain to your team, which provides flexibility and control over how you configure and operate is layer:
[Postgres](https://docs.langchain.com/langsmith/self-hosted-platform-features#custom-postgresql)and

[Redis](https://docs.langchain.com/langsmith/self-hosted-platform-features#custom-redis), size

[CPU and memory](https://docs.langchain.com/langsmith/self-hosted-platform-features#resource-customization)for your workload, and operate inside your existing network and observability stack. For the corresponding Cloud-managed model, see

[Deploy to Cloud](https://docs.langchain.com/langsmith/deploy-to-cloud-overview).