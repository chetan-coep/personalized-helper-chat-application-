---
id: "llms_033"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 33
source_url: "https://huggingface.co/docs/bitsandbytes"
language: "en"
retrieved_at: "2026-11-01 22:40:28"
content_hash: "1365228a4ce691b56a4025abbcd46a6faca28ed2f07b12552f9c8553d3cd93c7"
---

# LLMs

Source: https://huggingface.co/docs/bitsandbytes

---

Bitsandbytes documentation

bitsandbytes

Get started

Usage Guides

Explanation

API reference

# 

bitsandbytes enables accessible large language models via k-bit quantization for PyTorch. bitsandbytes provides three main features for dramatically reducing memory consumption for inference and training:

- 8-bit optimizers uses block-wise quantization to maintain 32-bit performance at a small fraction of the memory cost.
- LLM.int8() or 8-bit quantization enables large language model inference with only half the required memory and without any performance degradation. This method is based on vector-wise quantization to quantize most features to 8-bits and separately treating outliers with 16-bit matrix multiplication.
- QLoRA or 4-bit quantization enables large language model training with several memory-saving techniques that don’t compromise performance. This method quantizes a model to 4-bits and inserts a small set of trainable low-rank adaptation (LoRA) weights to allow training.

# 

bitsandbytes is MIT licensed.

[Update on GitHub](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/docs/source/index.mdx)