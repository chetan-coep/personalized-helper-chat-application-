---
id: "llms_038"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 38
source_url: "https://huggingface.co/docs/evaluate"
language: "en"
retrieved_at: "2026-11-01 22:40:44"
content_hash: "40d797b606ff86ca2e45e8ace0ea17be5da667565b952b500f84bfa027b9aa78"
---

# LLMs

Source: https://huggingface.co/docs/evaluate

---

Evaluate documentation

Evaluate on the Hub

[Choosing the right metric](https://huggingface.co/docs/evaluate/choosing_a_metric)

[Adding new evaluations](https://huggingface.co/docs/evaluate/creating_and_sharing)

[Using the evaluator](https://huggingface.co/docs/evaluate/base_evaluator)

[Using the evaluator with custom pipelines](https://huggingface.co/docs/evaluate/custom_evaluator)

[Creating an EvaluationSuite](https://huggingface.co/docs/evaluate/evaluation_suite)

# 



You can evaluate AI models on the Hub in multiple ways and this page will guide you through the different options:

- **Community Leaderboards** bring together the best models for a given task or domain and make them accessible to everyone by ranking them.
- **Model Cards** provide a comprehensive overview of a model’s capabilities from the author’s perspective.
- **Libraries and Packages** give you the tools to evaluate your models on the Hub.

## 

Community leaderboards show how a model performs on a given task or domain. For example, there are leaderboards for question answering, reasoning, classification, vision, and audio. If you’re tackling a new task, you can use a leaderboard to see how a model performs on it.

Here are some examples of community leaderboards:

| Leaderboard | Model Type | Description | 
|---|---|---|
| [MTEB](https://huggingface.co/spaces/mteb/leaderboard) | Embedding | The Massive Text Embedding Benchmark leaderboard compares 100+ text and image embedding models across 1000+ languages. Refer to the publication of each selectable benchmark for details on metrics, languages, tasks, and task types. Anyone is welcome to add a model, add benchmarks, help improve zero-shot annotations, or propose other changes to the leaderboard. | 
| [GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | Agentic | GAIA is a benchmark which aims at evaluating next-generation LLMs (LLMs with augmented capabilities due to added tooling, efficient prompting, access to search, etc). (See [the paper](https://arxiv.org/abs/2311.12983) for more details.) | 
| [OpenVLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard) | Vision Language Models | The OpenVLM Leaderboard evaluates 272+ Vision-Language Models (including GPT-4v, Gemini, QwenVLPlus, LLaVA) across 31 different multi-modal benchmarks using the VLMEvalKit framework. It focuses on open-source VLMs and publicly available API models. | 
| [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) | Audio | The Open ASR Leaderboard ranks and evaluates speech recognition models on the Hugging Face Hub. Models are ranked based on their Average WER, from lowest to highest. | 
| [LLM-Perf Leaderboard](https://huggingface.co/spaces/llm-perf/leaderboard) | LLM Performance | The 🤗 LLM-Perf Leaderboard 🏋️ is a leaderboard at the intersection of quality and performance. Its aim is to benchmark the performance (latency, throughput, memory & energy) of Large Language Models (LLMs) with different hardware, backends and optimizations using Optimum-Benchmark. | 

There are many more leaderboards on the Hub. Check out all the leaderboards via this [search](https://huggingface.co/spaces?category=model-benchmarking) or use this [dedicated Space](https://huggingface.co/spaces/OpenEvals/find-a-leaderboard) to find a leaderboard for your task.

## 

Model cards provide an overview of a model’s capabilities evaluated by the community or the model’s author. They are a great way to understand a model’s capabilities and limitations.

Unlike leaderboards, model card evaluation scores are often created by the author, rather than by the community.

For information on reporting results, see details on [the Model Card Evaluation Results metadata](https://huggingface.co/docs/hub/en/model-cards#evaluation-results).

## 

There are a number of open-source libraries and packages that you can use to evaluate your models on the Hub. These are useful if you want to evaluate a custom model or performance on a custom evaluation task.

### 

LightEval is a library for evaluating LLMs. It is designed to be comprehensive and customizable. Visit the LightEval [repository](https://github.com/huggingface/lighteval) for more information.

For more recent evaluation approaches that are popular on the Hugging Face Hub that are currently more actively maintained, check out [LightEval](https://github.com/huggingface/lighteval).

### 

A library for easily evaluating machine learning models and datasets.

With a single line of code, you get access to dozens of evaluation methods for different domains (NLP, Computer Vision, Reinforcement Learning, and more!). Be it on your local machine or in a distributed training setup, you can evaluate your models in a consistent and reproducible way!

Visit the 🤗 Evaluate [organization](https://huggingface.co/evaluate-metric) for a full list of available metrics. Each metric has a dedicated Space with an interactive demo for how to use the metric, and a documentation card detailing the metrics limitations and usage.

[Tutorials Learn the basics and become familiar with loading, computing, and saving with 🤗 Evaluate. Start here if you are using 🤗 Evaluate for the first time!](https://huggingface.co/installation)

[How-to guides Practical guides to help you achieve a specific goal. Take a look at these guides to learn how to use 🤗 Evaluate to solve real-world problems.](https://huggingface.co/choosing_a_metric)

[Conceptual guides High-level explanations for building a better understanding of important topics such as considerations going into evaluating a model or dataset and the difference between metrics, measurements, and comparisons.](https://huggingface.co/types_of_evaluations)

[Reference Technical descriptions of how 🤗 Evaluate classes and methods work.](https://huggingface.co/package_reference/main_classes)

[\< > Update on GitHub](https://github.com/huggingface/evaluate/blob/main/docs/source/index.mdx)