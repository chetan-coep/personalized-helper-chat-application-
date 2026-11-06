---
id: "llms_005"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 5
source_url: "https://huggingface.co/learn/context-course"
language: "en"
retrieved_at: "2026-11-01 22:40:33"
content_hash: "23bbfebd2f2b995382fbd7eb959d116d23ccca88af1804eec3a1f4b9d1a3aca4"
---

# LLMs

Source: https://huggingface.co/learn/context-course

---

Context Course documentation

Welcome to The Context Course

# 

This course is about **context engineering** for AI code agents: structuring knowledge so an agent can efficiently find what it needs, when it needs it to improve its generated outputs.

## 

Claude Code, Codex, and OpenCode all share the same constraint: an agent is only as good as the context it has. Good context means fewer wrong turns, cleaner diffs, and less rework.

Across six units you’ll build portable skills, wire up tools through the Model Context Protocol (MCP), package those pieces into plugins, coordinate sub-agents for larger tasks, and study how a minimal agent loop actually works under the hood.

## 

This course is structured into 6 core units:

| Unit | Topic | What You’ll Learn | 
|---|---|---|
| **Unit 0** | Onboarding | Course overview, tool setup, prerequisites | 
| **Unit 1** | Agent Skills | What skills are, how to build and share them, how agents load them | 
| **Unit 2** | Model Context Protocol | MCPs explained, connecting tools and APIs to agents | 
| **Unit 3** | Plugins | Building plugins, designing agent workflows | 
| **Unit 4** | Sub-agents | Spawning specialized agents, multi-agent patterns | 
| **Unit 5** | Hooks | Observing, blocking, and automating the agent lifecycle | 
| **Unit 6** | Bonus: Nano Harness | Building a minimal agent loop from scratch | 

## 

Before starting, you should be comfortable with Python basics (variables, functions, loops, and file I/O), able to navigate directories and run scripts from the command line, and have a Hugging Face account ([huggingface.co](https://huggingface.co)). You’ll also need at least one code agent installed and configured — see the setup section below.

## 

This course works with multiple code agents. Choose at least one to follow along:

This edition of the course uses Claude Code, Codex, and OpenCode as the reference agents throughout. If you’re using Cursor or GitHub Copilot, the same ideas still apply, but their MCP and extension UX differs enough that they are not covered step-by-step here.


Claude Code is Anthropic’s official code agent, accessible via the web, desktop app, or CLI.

curl -fsSL https://claude.ai/install.sh | bash

**Getting started**: Visit [claude.ai/code](https://claude.ai/code) to use Claude Code on the web, or install the CLI above and run `claude` in any project directory. You’ll be prompted to sign in on first use.

Codex is OpenAI’s code agent with multi-agent capabilities.

npm install -g @openai/codex

**Getting started**: Run `codex` and select **Sign in with ChatGPT** to authenticate with a paid ChatGPT plan (Plus, Pro, Business, Edu, or Enterprise), or use an OpenAI API key.

OpenCode is an open source code agent from [opencode.ai](https://opencode.ai):

curl -fsSL https://opencode.ai/install | bash

Or via npm:

npm install -g opencode-ai

**Getting started**: Run `opencode` in any project directory. OpenCode supports multiple LLM providers — configure your preferred provider on first launch.

Pi is a minimal terminal coding harness that you can extend with skills, prompt templates, and TypeScript extensions.

npm install -g @mariozechner/pi-coding-agent

**Getting started**: Run `pi` in any project directory. Authenticate with `/login` to use a subscription-backed provider, or export an API key such as `ANTHROPIC_API_KEY` before launch.

## 

### 

Plan on one unit per week, roughly 2–3 hours each. Context engineering is a practice-heavy skill, so build the examples rather than skimming them.

### 

Each unit mixes conceptual material with runnable code, a hands-on project, and a short quiz.

### 

While we recommend following units in order, you can customize based on your needs:

- **Just want skills?** Start with Unit 1, revisit MCPs when needed
- **Building a plugin for your team?** Start with Unit 3
- **Multi-agent systems?** Begin with Unit 4, return to Unit 1-2 as reference
- **Following along with open source?** All lessons include OpenCode examples alongside Claude Code and Codex

## 

This course offers two levels of certification:

### 

Demonstrates you understand core context engineering concepts. Pass the Unit 1–2 quizzes with 70% or higher to earn this certificate in 2–3 weeks. It’s shareable and displayed on your Hugging Face profile.

### 

Demonstrates mastery of context engineering across all domains. Pass all Unit 1–5 quizzes (70% or higher) and complete the capstone project to earn this certificate in 5–8 weeks. It’s displayed on your Hugging Face profile with a project showcase.

The capstone project will be announced in the course live stream. [Follow the Context Course org on Hugging Face](https://huggingface.co/organizations/context-course/share/BcsYJAxCofWDZncivkBzafSjAcuAxOMWua) to get updates.


Both certificates verify your ability to build and maintain agent skills, connect external tools through MCPs, design multi-agent systems, and optimize context for maximum agent performance.

## 

Every unit follows the same shape: an introduction, conceptual material, practical walkthroughs, a hands-on project, and a quiz. Starter templates and copy-pasteable code are provided throughout so you spend time on the ideas rather than on boilerplate.

## 

**Ben Burtenshaw** — ML Engineer, Hugging Face

Ben focuses on LLM applications with emphasis on post-training and agentic approaches. He leads initiatives around agent best practices and context engineering at Hugging Face.

**Atin Kumar Singh** — ML Researcher & Founding Engineer @ Data Pigeon

Atin’s research focuses on world models and robotics at the DARE Lab, UC Davis. He is a founding engineer at Data Pigeon, an AI-driven EV charging platform. His broader work spans applied ML and infrastructure for AI agents.

**Maya Nielan**

Maya contributed to the Claude Code sections of this course.

**Ryan Whitehead**

Ryan contributed to the Claude Code sections of this course.

## 

Learning is better together. Join the conversation:

- **Discord**: [discord.gg/huggingface](https://discord.gg/huggingface)
- **Share your work**: Tag #ContextCourse on social media
- **Report issues**: GitHub Issues for course content bugs

## 

Install at least one of the agents above, check the prerequisites, then head to Unit 1 to start with agent skills.

[Update on GitHub](https://github.com/huggingface/context-course/blob/main/units/en/unit0/introduction.mdx)