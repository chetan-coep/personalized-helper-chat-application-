---
id: "llms_050"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 50
source_url: "https://huggingface.co/docs/openenv"
language: "en"
retrieved_at: "2026-11-01 22:41:10"
content_hash: "fc5de4851d73f4a567b011fdaa385479765a62335f202b3c835325e22dfb1fe2"
---

# LLMs

Source: https://huggingface.co/docs/openenv

---

OpenEnv documentation

OpenEnv: Agentic Execution Environments

[v0.10.0](https://huggingface.co/docs/openenv/v0.10.0/index)).

# 

An end-to-end framework for creating, deploying and using isolated execution environments for agentic RL, with a simple Gymnasium-style API.

`reset()`, `step()` and `state()`, sync or async, over a WebSocket.

Each environment is a Docker image that runs locally, on a cloud sandbox, or as a Hugging Face Space.

Games, coding sandboxes, browsers, finance, simulators and more, in the [catalog](https://huggingface.co/environments).

TRL, Unsloth, SkyRL, ART, Oumi, torchforge, Miles and more. See [Training with OpenEnv](https://huggingface.co/guides/training).

[Harbor](https://huggingface.co/environments/harbor) runs Claude Code, Codex, OpenCode and other harnesses, and captures their tokens for RL.

MCP environments expose their tools over `/mcp` in production mode.

## 

1. **[Getting Started](https://huggingface.co/getting-started)**: install OpenEnv, connect to an environment and run your first step.
2. **[Train an agent](https://huggingface.co/guides/training)**: pick a way to train and a framework. [Harbor](https://huggingface.co/environments/harbor) captures coding agents that run their own loop, for training.
3. **[Build your own environment](https://huggingface.co/guides/first-environment)**, then [deploy it](https://huggingface.co/getting_started/environment-builder) to Hugging Face Spaces.
4. **[Explore environments](https://huggingface.co/environments)**: browse the catalog.

The [tutorials](https://huggingface.co/tutorials/index) include a 5-part Getting Started series that needs no GPU, and the [Concepts](https://huggingface.co/guides/concepts) pages explain how the pieces fit.

## 

OpenEnv is openly governed by a technical committee that coordinates project direction, RFCs and releases through the public [GitHub repository](https://github.com/huggingface/OpenEnv). The [charter](https://github.com/huggingface/OpenEnv/blob/main/GOVERNANCE.md) explains how it works, and the [README](https://github.com/huggingface/OpenEnv#community-support--acknowledgments) lists the committee members and supporters. Bug reports, feature requests and new environments are welcome as issues or pull requests, see [Contributing](https://huggingface.co/contributing). For the changelog, see [GitHub Releases](https://github.com/huggingface/OpenEnv/releases).

OpenEnv is in early development, so APIs may still change. Bug fixes are welcome. For larger changes, open or claim an issue first so the change can be discussed.


[Update on GitHub](https://github.com/huggingface/openenv/blob/main/docs/source/index.md)