---
id: "llms_034"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 34
source_url: "https://huggingface.co/docs/chat-ui"
language: "en"
retrieved_at: "2026-11-01 22:40:30"
content_hash: "bb9904e6128d9ddf921ceaa329fdeae73c2e530de534ab6b144b031be74650b1"
---

# LLMs

Source: https://huggingface.co/docs/chat-ui

---

Chat UI documentation

Chat UI

[Chat UI](https://huggingface.co/docs/chat-ui/index)

# 

Open source chat interface with support for tools, multimodal inputs, and intelligent routing across models. The app uses MongoDB and SvelteKit behind the scenes. Try the live version called [HuggingChat on hf.co/chat](https://huggingface.co/chat) or [setup your own instance](https://huggingface.co/installation/local).

Chat UI connects to any OpenAI-compatible API endpoint, making it work with:

- [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers)
- [Ollama](https://ollama.ai)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [OpenRouter](https://openrouter.ai)
- Any other OpenAI-compatible service

**[MCP Tools](https://huggingface.co/configuration/mcp-tools)**: Function calling via Model Context Protocol (MCP) servers

**[LLM Router](https://huggingface.co/configuration/llm-router)**: Intelligent routing to select the best model for each request

**[Multimodal](https://huggingface.co/configuration/overview)**: Image uploads on models that support vision

**[OpenID](https://huggingface.co/configuration/open-id)**: Optional user authentication via OpenID Connect

## 

**Step 1 - Create `.env.local`:**

```
OPENAI_BASE_URL=https://router.huggingface.co/v1
OPENAI_API_KEY=hf_************************
```
You can use any OpenAI-compatible endpoint:

| Provider | `OPENAI_BASE_URL` | `OPENAI_API_KEY` | 
|---|---|---|
| Hugging Face | `https://router.huggingface.co/v1` | `hf_xxx` | 
| Ollama | `http://127.0.0.1:11434/v1` | `ollama` | 
| llama.cpp | `http://127.0.0.1:8080/v1` | `sk-local` | 
| OpenRouter | `https://openrouter.ai/api/v1` | `sk-or-v1-xxx` | 

**Step 2 - Install and run:**

```
git clone https://github.com/huggingface/chat-ui
cd chat-ui
npm install
npm run dev -- --open
```
That’s it! Chat UI will automatically discover available models from your endpoint.

MongoDB is optional for development. When `MONGODB_URL` is not set, Chat UI uses an embedded database that persists to `./db`.


For production deployments, see the [installation guides](https://huggingface.co/installation/local).

[Update on GitHub](https://github.com/huggingface/chat-ui/blob/main/docs/source/index.md)