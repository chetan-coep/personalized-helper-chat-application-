---
id: "rag_026"
technology: "RAG"
category: "ML & Data"
title: "RAG"
doc_order: 26
source_url: "https://python.langchain.com/docs"
language: "en"
retrieved_at: "2026-11-01 22:39:40"
content_hash: "e434a1dd3ae4aeb95aadcc9f5710b0131b9580cfe242108ecb031ee89d3fb60c"
---

# RAG

Source: https://python.langchain.com/docs

---

LangChain provides create\_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.

Copy pageCopy page

Agent = Model + Harness. LangChain provides create\_agent: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior. Start with the primitives and compose exactly what your use case needs. Supports OpenAI, Anthropic, Google, and more.

LangChain vs. LangGraph vs. Deep AgentsStart with Managed Deep Agents for a batteries-included harness (context compression, virtual filesystem, subagents) when you want to run production agents without having to manage infrastructure. Alternatively, for maximum flexibility while using the same Deep Agents harness, use the Deep Agents SDK and host agents yourself, or run a custom LangSmith Deployment. Deep Agents is built on LangChain agents, which you can also use directly.Use LangChain (create\_agent) for a highly customizable harness, easily tailored to your use case and data.Use LangGraph, our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows.Use LangSmith to trace, debug, and evaluate agents built with any of these frameworks. Follow the tracing quickstart to get set up. We recommend you also set up LangSmith Engine which monitors your traces, detects issues, and proposes fixes.

This example demonstrates how to create a simple LangChain agent with a custom tool:

OpenAI

Google Gemini

Claude (Anthropic)

OpenRouter

Fireworks

Baseten

Ollama

Azure

AWS Bedrock

HuggingFace

\# pip install -qU langchain "langchain\[openai\]"from langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="openai:gpt-5.5", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain "langchain\[google-genai\]"from langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="google\_genai:gemini-2.5-flash-lite", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain "langchain\[anthropic\]"from langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="claude-sonnet-4-6", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain langchain-openrouterfrom langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="openrouter:anthropic/claude-sonnet-4-6", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain langchain-fireworksfrom langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain langchain-basetenfrom langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="baseten:zai-org/GLM-5.2", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain langchain-ollamafrom langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="ollama:devstral-2", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain "langchain\[openai\]"import osfrom langchain.agents import create\_agentfrom langchain.chat\_models import init\_chat\_modeldef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"model = init\_chat\_model( "azure\_openai:gpt-5.5", azure\_deployment=os.environ\["AZURE\_OPENAI\_DEPLOYMENT\_NAME"\],)agent = create\_agent( model=model, tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain langchain-awsfrom langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"# US cross-region inference profile; use global.anthropic.claude-sonnet-4-6 for worldwide routing.agent = create\_agent( model="bedrock\_converse:us.anthropic.claude-sonnet-4-6", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

\# pip install -qU langchain "langchain\[huggingface\]"from langchain.agents import create\_agentdef get\_weather(city: str) -> str: """Get weather for a given city.""" return f"It's always sunny in {city}!"agent = create\_agent( model="huggingface:microsoft/Phi-3-mini-4k-instruct", tools=\[get\_weather\], system\_prompt="You are a helpful assistant",)result = agent.invoke( {"messages": \[{"role": "user", "content": "What's the weather in San Francisco?"}\]})print(result\["messages"\]\[-1\].content\_blocks)

Use one interface for chat models, embeddings, and more across providers. Switch models with minimal code changes and keep your application portable as requirements evolve.

Learn more

Highly configurable harness

Start with create\_agent as a minimal harness and add capabilities incrementally through middleware. Compose only what your use case needs, from guardrails and retries to routing and custom tool policies.

Learn more

Built on top of LangGraph

LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more.

Learn more

Debug with LangSmith

Inspect traces, tool calls, state transitions, and latency in one place. Find failure modes, evaluate quality, and improve agent behavior with execution data.

Learn more

Connect these docs to your agent of choice via MCP for real-time answers.