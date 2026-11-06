---
id: "rag_016"
technology: "RAG"
category: "ML & Data"
title: "Deep Agents overview - Docs by LangChain"
doc_order: 16
source_url: "https://docs.langchain.com/oss/javascript/deepagents/overview"
language: "en"
retrieved_at: "2026-11-03 17:58:16"
content_hash: "4e5c8d756befa3c6b9b0e148d18e679ceb29179dae6ae7fee26660195c3eb6d9"
---

# Deep Agents overview - Docs by LangChain

Source: https://docs.langchain.com/oss/javascript/deepagents/overview

---

Deep Agents is the

[agent harness](https://docs.langchain.com/oss/javascript/concepts/products#agent-harnesses-like-the-deep-agents-sdk)for complex, multi-step work. It adds planning, a virtual filesystem for context, subagent spawning, and long-term memory on top of LangChain and LangGraph. Start with

[Managed Deep Agents](https://docs.langchain.com/langsmith/javascript/managed-deep-agents-overview)to run production agents without having to manage infrastructure. Alternatively, for maximum flexibility while using the same Deep Agents harness, use the

[Deep Agents SDK](https://docs.langchain.com#self-host-with-the-sdk)and host agents yourself, or run a custom

[LangSmith Deployment](https://docs.langchain.com/langsmith/deployment).

## Choose how to run Deep Agents

## Managed Deep Agents

## Deep Agents SDK

- **Take actions in an environment**: Take actions via tools, read and write files, execute code
- **Connect to your data**: Load memories, skills, and domain knowledge at the right moment
- **Manage growing context**: Summarize history and offload large results across long runs
- **Parallelize tasks**: Delegate to general or specialized subagents running in isolated context windows
- **Stay in the loop**: Pause for human approval at critical decision points
- **Improve over time**: Update memory, skills, and prompts based on real usage

Optional capabilities such as

[task planning](https://docs.langchain.com#task-planning)and

[skills](https://docs.langchain.com#skills)extend the harness when your use case needs them. See

[Core capabilities](https://docs.langchain.com#core-capabilities)for a full breakdown of each component.

## Self-host with the SDK

Use the open source SDK when you run the agent in your own process or container, need a custom
[backend](https://docs.langchain.com/oss/javascript/deepagents/backends), store, or checkpointer, or want a

[LangSmith Deployment](https://docs.langchain.com/langsmith/deployment)you configure yourself. For managed deployment instead, see

[Managed Deep Agents](https://docs.langchain.com/langsmith/javascript/managed-deep-agents-overview).

### Try it

### Quickstart

## View example trace

[Quickstart](https://docs.langchain.com/oss/javascript/deepagents/quickstart/)and

[Customization guide](https://docs.langchain.com/oss/javascript/deepagents/customization/)to build with the SDK.

## Core capabilities

Deep Agents is an
[“agent harness”](https://docs.langchain.com/oss/javascript/concepts/products#agent-harnesses-like-the-deep-agents-sdk). It is the same core tool calling loop as other agent frameworks, but with built-in capabilities that make agents reliable for real tasks:

## Execution environment

## Context management

## Delegation

## Steering

[`deepagents`](https://www.npmjs.com/package/deepagents)is a standalone library built on top of

[LangChain](https://docs.langchain.com/oss/javascript/langchain/)’s core building blocks for agents and using

[LangGraph](https://docs.langchain.com/oss/javascript/langgraph/)’s tooling for running agents in production.

[LangChain](https://docs.langchain.com/oss/javascript/langchain/)is the framework that provides the core building blocks for your agents. To learn more about the differences between LangChain, LangGraph, and Deep Agents, see

[Frameworks, runtimes, and harnesses](https://docs.langchain.com/oss/javascript/concepts/products). For a side-by-side comparison with Anthropic’s harness, see

[Deep Agents vs. Claude Agent SDK](https://docs.langchain.com/oss/javascript/deepagents/comparison). For building custom agents without these built-in capabilities, consider using LangChain’s

[`createAgent`](https://docs.langchain.com/oss/javascript/langchain/agents)or building a custom

[LangGraph](https://docs.langchain.com/oss/javascript/langgraph/overview)workflow.

## Execution environment

The execution environment is where an agent acts. It has four layers:
- **[Tools](https://docs.langchain.com#tools-and-mcp)**: custom functions, APIs, and databases the agent can call
- **[Virtual filesystem](https://docs.langchain.com#virtual-filesystem-access)**: file tools backed by pluggable backends
- **[Filesystem permissions](https://docs.langchain.com#filesystem-permissions)**: declarative access control over which paths agents can read or write
- **[Code execution](https://docs.langchain.com#code-execution)**: sandboxed shell execution and an in-process JavaScript interpreter

**[Streaming](https://docs.langchain.com#streaming)**allows you to keep up with everything happening using typed event streams for messages, tools, values, and delegated tasks.

### Tools and MCP

Pass custom functions, LangChain tools, or tools from any
[MCP server](https://docs.langchain.com/oss/javascript/deepagents/tools#mcp-tools)with the

`tools=` parameter. Deep Agents fully support the [Model Context Protocol (MCP)](https://docs.langchain.com/oss/javascript/langchain/mcp), letting you connect to databases, APIs, file systems, and more through a standard interface. For more information on defining custom tools, using MCP servers, and the full list of built-in harness tools, see

[Tools](https://docs.langchain.com/oss/javascript/deepagents/tools).

### Virtual filesystem access

The harness provides a configurable virtual filesystem which can be backed by different
[pluggable backends](https://docs.langchain.com/oss/javascript/deepagents/backends): in-memory state, local disk, LangGraph store, composite routing, or a custom backend with

[permission rules](https://docs.langchain.com/oss/javascript/deepagents/permissions)for read and write access. The backends support the following file system operations:

## Supported multimodal file extensions


## Running without the default filesystem tools


[harness profile](https://docs.langchain.com/oss/javascript/deepagents/profiles#harness-profiles)with

`excluded_tools`:
[`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware)itself via

`excluded_middleware` is intentionally rejected—it is required scaffolding in the [Deep Agents stack](https://docs.langchain.com/oss/javascript/deepagents/customization#deep-agents-stack). Use

`excluded_tools` to hide only the model-visible tool surface and leave the middleware in place. To remove the `task` tool, see [Running without subagents](https://docs.langchain.com/oss/javascript/deepagents/subagents#running-without-subagents).

[backends](https://docs.langchain.com/oss/javascript/deepagents/backends). To generate a durable repository wiki that agents can read from the filesystem, see

[OpenWiki](https://docs.langchain.com/oss/openwiki/overview).

### Filesystem permissions

The harness supports declarative permission rules that control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools listed above and are evaluated in declaration order with first-match-wins semantics. Define permissions by passing a list of rules to`permissions=` when creating the agent. Each rule includes:
- `operations`: `"read"` and/or `"write"`
- `paths`: Glob patterns for files or directories
- `mode`: `"allow"` or `"deny"`

Rules are evaluated top to bottom, and the first matching rule wins. If no rule matches, the operation is allowed. This model lets you restrict agents to specific directories (for example,

`/workspace/`), protect sensitive files such as `.env` or credentials, and give subagents narrower access than the parent agent.
Permissions do not apply to [sandbox backends](https://docs.langchain.com/oss/javascript/deepagents/sandboxes), which support arbitrary command execution via the

`execute` tool. For custom validation logic, use [backend policy hooks](https://docs.langchain.com/oss/javascript/deepagents/backends#add-policy-hooks). For the full rule structure, examples, and subagent inheritance, see

[Permissions](https://docs.langchain.com/oss/javascript/deepagents/permissions).

### Code execution

Deep Agents supports code execution in two ways:
- [Sandbox backends](https://docs.langchain.com/oss/javascript/deepagents/sandboxes) expose an `execute` tool for shell commands in an isolated environment.
- [Interpreters](https://docs.langchain.com/oss/javascript/deepagents/interpreters) add an `eval` tool that runs JavaScript in a scoped QuickJS runtime.

Use sandbox backends when the agent needs to install dependencies, run tests, call CLIs, or work with an operating-system filesystem. Sandbox backends implement the

`SandboxBackendProtocolV2`; when detected, the harness adds the `execute` tool to the agent’s available tools.
Use interpreters when the agent needs a lightweight programmable layer for loops, batching, deterministic data transformations, or programmatic tool calling. Interpreters do not provide shell access, package installs, or filesystem and network access.
For sandbox setup, providers, and file transfer APIs, see [Sandboxes](https://docs.langchain.com/oss/javascript/deepagents/sandboxes). For the QuickJS runtime and programmatic tool calling, see

[Interpreters](https://docs.langchain.com/oss/javascript/deepagents/interpreters).

### Streaming

[Event streaming](https://docs.langchain.com/oss/javascript/deepagents/event-streaming)exposes agent runs as typed projections for messages, tool calls, values, and output. Deep Agents add

`stream.subagents` so each delegated task gets its own handle with independent message, tool-call, and nested subagent streams.
## Context management

The context management component controls what the agent knows, how long it can operate within token limits, and what it retains across sessions. It has four layers:
- **[Skills](https://docs.langchain.com#skills)**: on-demand domain knowledge loaded progressively from skill files
- **[Memory](https://docs.langchain.com#memory)**: persistent instructions and preferences loaded at startup from `AGENTS.md` files
- **[Summarization and context offloading](https://docs.langchain.com#summarization-and-context-offloading)**: automatic compression of conversation history and large tool results
- **[Prompt caching](https://docs.langchain.com#prompt-caching)**: static prompt sections are cache-eligible to speed up inference and reduce cost on supported models

### Skills

Skills package specialized workflows, domain knowledge, and custom instructions for your deep agent. Each skill follows the
[Agent Skills standard](https://agentskills.io/)and lives in a directory with a

`SKILL.md` file. Skills can also include scripts, templates, reference docs, and other supporting resources.
Deep Agents load skills with progressive disclosure: the agent reads `SKILL.md` frontmatter at startup, then reads full skill content only when a task needs it. This keeps startup context compact while still making rich capabilities available on demand.
For more information, see [Skills](https://docs.langchain.com/oss/javascript/deepagents/skills).

### Memory

Memory gives your deep agent persistent context across conversations, such as coding style, preferences, conventions, and project guidelines. Memory uses
[`AGENTS.md` files](https://agents.md/)that you pass through the

`memory` parameter when creating the agent. Unlike skills, memory files are always loaded, and the content is stored in the configured backend (`StateBackend`, `StoreBackend`, or `FilesystemBackend`).
The agent can also update memory based on interactions and feedback, so preferences and patterns can carry forward without needing to restate them in each thread.
For configuration details and examples, see [Memory](https://docs.langchain.com/oss/javascript/deepagents/customization#memory). To generate a repository wiki that coding agents discover through

`AGENTS.md`, see [OpenWiki](https://docs.langchain.com/oss/openwiki/overview).

### Summarization and context offloading

The harness manages context so deep agents can handle long-running work within token limits while keeping the most relevant information in scope. This context flow has four parts:
- **Input context**: System prompt, memory, skills, and tool prompts define what the agent starts with.
- **Compression**: Built-in offloading and summarization compress conversation history and large intermediate results.
- **Isolation**: Subagents quarantine heavy subtasks and return only final results (see [Delegation](https://docs.langchain.com#delegation)).
- **Long-term memory**: Persistent storage in the virtual filesystem carries information across threads.

Together, these mechanisms support multi-step tasks that exceed a single context window while reducing manual context trimming and token usage. For configuration details, see

[Context engineering](https://docs.langchain.com/oss/javascript/deepagents/context-engineering). For multimodal inputs and tool outputs, see

[Multimodal](https://docs.langchain.com/oss/javascript/deepagents/multimodal).

### Prompt caching

For Anthropic and Amazon Bedrock models,`create_deep_agent` automatically applies prompt caching to static sections of the system prompt—the base agent instructions, memory, and skill content that repeat on every turn. This avoids reprocessing the same tokens across calls, reducing both latency and cost on long-running agents.
Prompt caching is enabled by default when using an Anthropic model, or a Bedrock model (Claude or Nova). No configuration is required.
For other providers, see [Middleware integrations](https://docs.langchain.com/oss/javascript/integrations/middleware)for available provider-specific caching middleware.

## Delegation

The delegation component enables agents to break large problems into smaller, parallelizable units of work. It has two layers:
- **[Task planning](https://docs.langchain.com#task-planning)**: an opt-in `write_todos` tool for structured task tracking
- **[Subagents](https://docs.langchain.com#subagents)**: ephemeral child agents that handle isolated subtasks

### Task planning

Task planning is an opt-in harness capability that lets agents maintain a structured task list during execution. Starting in v0.7 task planning is opt-in only. In earlier versions, task planning middleware was included by default. Planning is often useful for:
- Long or complicated multi-step tasks
- Less capable models that benefit from an explicit accountability tool
- UIs that stream progress from agent state (see [Todo list](https://docs.langchain.com/oss/javascript/deepagents/frontend/todo-list))

Pass

[`TodoListMiddleware`](https://reference.langchain.com/javascript/langchain/index/todoListMiddleware)to the middleware parameter to give the agent a

`write_todos` tool for maintaining a structured task list during execution.
`'pending'`, `'in_progress'`, `'completed'`) and are persisted in agent state. This gives agents a lightweight planning layer for organizing long-running and multi-step work.
For configuration options and behavior details, see [To-do list](https://docs.langchain.com/oss/javascript/langchain/middleware/built-in#to-do-list).

### Subagents

The harness includes a built-in`task` tool that lets the main agent create ephemeral subagents for isolated, long-running, multi-step, or parallel tasks.
Two subagent types are available: synchronous subagents (the default) block the supervisor until they return a single report, and [async subagents](https://docs.langchain.com/oss/javascript/deepagents/async-subagents)run in parallel and support mid-flight steering via launch, check, update, and cancel tools. Subagent execution provides:

- **Isolated or inherited context**: By default, each invocation creates a new agent instance with its own context (`mode: "isolated"`). Use `mode: "fork"` to inherit the parent’s full conversation history instead. See [Forked subagents](https://docs.langchain.com/oss/javascript/deepagents/subagents#forked-subagents).
- **Autonomous execution**: The subagent runs independently until completion.
- **Single handoff**: It returns one final report to the main agent.
- **Configurable strategy**: Use the [default `general-purpose` subagent](https://docs.langchain.com/oss/javascript/deepagents/subagents#default-subagent) (enabled by default) or define [custom subagents](https://docs.langchain.com/oss/javascript/deepagents/subagents#custom-subagents).
- **Stateless messaging**: Subagents are stateless and cannot send multiple messages back.
- **Context and token efficiency**: Heavy subtask work stays isolated and is compressed into a compact result.

For more information, see

[Subagents](https://docs.langchain.com/oss/javascript/deepagents/subagents). To remove the

`task` tool, see [Running without subagents](https://docs.langchain.com/oss/javascript/deepagents/subagents#running-without-subagents).

## Steering

The steering component gives humans control over agent behavior at runtime and sets filesystem permissions for agent work.
### Human-in-the-loop

Deep Agents integrate with LangGraph interrupts so you can pause for approval on sensitive tool calls. Enable this behavior with the`interrupt_on` parameter in `create_deep_agent`.
`interrupt_on` accepts a mapping of tool names to interrupt configurations. For example, `interrupt_on={"edit_file": True}` pauses before every edit, letting you approve the call, add guidance, or modify tool inputs before execution.
This gives you a runtime safety and control layer for destructive operations, expensive API calls, and interactive debugging.
For more information, see [Human-in-the-loop](https://docs.langchain.com/oss/javascript/deepagents/human-in-the-loop).

## Get started

## Managed Deep Agents

## SDK quickstart

## Customization

## Code

## ACP

## Reference

`deepagents` API reference