---
id: "llms_048"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 48
source_url: "https://huggingface.co/docs/lighteval"
language: "en"
retrieved_at: "2026-11-01 22:41:02"
content_hash: "5dfd3f96c1d622a6d1e19233460255e520e4927fd2b22efb7fb35e91131c24b5"
---

# LLMs

Source: https://huggingface.co/docs/lighteval

---

Lighteval documentation

Lighteval

Getting started

Guides

API

Reference

# 

🤗 Lighteval is your all-in-one toolkit for evaluating Large Language Models (LLMs) across multiple backends with ease. Dive deep into your model’s performance by saving and exploring detailed, sample-by-sample results to debug and see how your models stack up.

## 

### 

Evaluate your models using the most popular and efficient inference backends:

- `eval`: Use [inspect-ai](https://inspect.aisi.org.uk/) as backend to evaluate and inspect your models ! (prefered way)
- `transformers`: Evaluate models on CPU or one or more GPUs using [🤗
Accelerate](https://github.com/huggingface/transformers)
- `nanotron`: Evaluate models in distributed settings using [⚡️
Nanotron](https://github.com/huggingface/nanotron)
- `vllm`: Evaluate models on one or more GPUs using [🚀
VLLM](https://github.com/vllm-project/vllm)
- `custom`: Evaluate custom models (can be anything)
- `sglang`: Evaluate models using [SGLang](https://github.com/sgl-project/sglang) as backend
- `inference-endpoint`: Evaluate models using Hugging Face’s [Inference Endpoints API](https://huggingface.co/inference-endpoints/dedicated)
- `tgi`: Evaluate models using [🔗 Text Generation Inference](https://huggingface.co/docs/text-generation-inference/en/index) running locally
- `litellm`: Evaluate models on any compatible API using [LiteLLM](https://www.litellm.ai/)
- `inference-providers`: Evaluate models using [HuggingFace’s inference providers](https://huggingface.co/docs/inference-providers/en/index) as backend\*\*: Distributed training and evaluation

### 

- **Extensive Task Library**: 1000s pre-built evaluation tasks
- **Custom Task Creation**: Build your own evaluation tasks
- **Flexible Metrics**: Support for custom metrics and scoring
- **Detailed Analysis**: Sample-by-sample results for deep insights

### 

Customization at your fingertips: create [new tasks](https://huggingface.co/adding-a-custom-task),
[metrics](https://huggingface.co/adding-a-new-metric) or [model](https://huggingface.co/evaluating-a-custom-model) tailored to your needs, or browse all our existing tasks and metrics.

### 

Seamlessly experiment, benchmark, and store your results on the Hugging Face Hub, S3, or locally.

## 

### 

pip install lighteval

### 

#### 

#### 

```
lighteval eval "hf-inference-providers/openai/gpt-oss-20b" \
    gpqa:diamond \
    --bundle-dir gpt-oss-bundle \
    --repo-id OpenEvals/evals
```
Resulting Space:

[Update on GitHub](https://github.com/huggingface/lighteval/blob/main/docs/source/index.mdx)