---
id: "llms_057"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 57
source_url: "https://huggingface.co/docs/peft"
language: "en"
retrieved_at: "2026-11-01 22:41:21"
content_hash: "6123c23129fe5137df31402b2e088aee984e6a0a469a00a95dc47a5dde52da30"
---

# LLMs

Source: https://huggingface.co/docs/peft

---

PEFT documentation

PEFT

Get started

Guides

Methods

API reference

# 

🤗 PEFT (Parameter-Efficient Fine-Tuning) is a library for efficiently adapting large pretrained models to various downstream applications without fine-tuning all of a model’s parameters because it is prohibitively costly. PEFT methods only fine-tune a small number of (extra) model parameters - significantly decreasing computational and storage costs - while yielding performance comparable to a fully fine-tuned model. This makes it more accessible to train and store large language models (LLMs) and other big models on consumer hardware.

PEFT is integrated with the Transformers, Diffusers, and Accelerate libraries to provide a faster and easier way to load, train, and use large models for inference.

There are numerous methods to "adapt" existing models, often extensively integrating into the model. PEFT can be thought of as a framework for arbitrary methods of model adaption (modifying weights, wrapping layers, manipulating KV-caches, ...) while also serving as a reference implementation for many fine-tuning methods.

[Update on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/index.md)