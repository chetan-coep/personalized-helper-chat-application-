---
id: "llms_053"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 53
source_url: "https://huggingface.co/docs/optimum-habana"
language: "en"
retrieved_at: "2026-11-01 22:41:15"
content_hash: "94d4b3bebbe52e201834cf5de50de595ad756e3a6b1d7f3502785b8fd457cf39"
---

# LLMs

Source: https://huggingface.co/docs/optimum-habana

---

Optimum Habana documentation

Optimum for Intel® Gaudi® AI Accelerator

# 

Optimum for Intel Gaudi AI accelerator is the interface between Hugging Face libraries (Transformers, Diffusers, Accelerate,…) and [Intel Gaudi AI Accelerators (HPUs)](https://docs.habana.ai/en/latest/index.html).
It provides a set of tools that enable easy model loading, training and inference on single- and multi-HPU settings for various downstream tasks as shown in the table below.

[Tutorials Learn the basics and become familiar with training transformers on HPUs with 🤗 Optimum. Start here if you are using 🤗 Optimum for Intel Gaudi for the first time!](https://huggingface.co/tutorials/overview)

[How-to guides Practical guides to help you achieve a specific goal. Take a look at these guides to learn how to use 🤗 Optimum for Intel Gaudi to solve real-world problems.](https://huggingface.co/usage_guides/overview)

The Intel Gaudi AI accelerator family currently includes three product generations:
[Intel Gaudi 1](https://habana.ai/products/gaudi/),
[Intel Gaudi 2](https://habana.ai/products/gaudi2/), and
[Intel Gaudi 3](https://habana.ai/products/gaudi3/).
Each server is equipped with 8 devices, known as Habana Processing Units (HPUs), providing 128GB of memory on Gaudi 3,
96GB on Gaudi 2, and 32GB on the first-gen Gaudi. For more details on the underlying hardware architecture, check out the
[Gaudi Architecture Overview](https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html).
Optimum for Intel Gaudi library is fully compatible with all three generations of Gaudi accelerators.

For in-depth examples of running workloads on Gaudi, explore the following blog posts:

- [Benchmarking Intel Gaudi 2 with NVIDIA A100 GPUs](https://huggingface.co/blog/habana-gaudi-2-benchmark)
- [Accelerating Vision-Language Models: BridgeTower on Habana Gaudi2](https://huggingface.co/blog/bridgetower)

The following model architectures, tasks and device distributions have been validated for Optimum for Intel Gaudi:

In the tables below, ✅ means single-card, multi-card and DeepSpeed have all been validated.


- Transformers:

| Architecture | Training | Inference | Tasks | 
|---|---|---|---|
| BERT | ✅ | ✅ |  | 
| RoBERTa | ✅ | ✅ |  | 
| ALBERT | ✅ | ✅ |  | 
| DistilBERT | ✅ | ✅ |  | 
| GPT2 | ✅ | ✅ |  | 
| BLOOM(Z) |  |  |  | 
| StarCoder / StarCoder2 | ✅ |  |  | 
| GPT-J |  |  |  | 
| GPT-Neo |  |  |  | 
| GPT-NeoX |  |  |  | 
| OPT |  |  |  | 
| Llama 2 / CodeLlama / Llama 3 / Llama Guard / Granite | ✅ | ✅ |  | 
| StableLM |  |  |  | 
| Falcon |  | ✅ |  | 
| CodeGen |  |  |  | 
| MPT |  |  |  | 
| Mistral |  |  |  | 
| Phi | ✅ |  |  | 
| Mixtral |  |  |  | 
| Persimmon |  |  |  | 
| Qwen2 / Qwen3 |  |  |  | 
| Qwen2-MoE |  |  |  | 
| Gemma | ✅ |  |  | 
| Gemma2 |  | ✅ |  | 
| Gemma3 |  | ✅ |  | 
| XGLM |  |  |  | 
| Cohere |  |  |  | 
| T5 / Flan T5 | ✅ | ✅ |  | 
| BART |  |  |  | 
| ViT | ✅ | ✅ |  | 
| Swin | ✅ | ✅ |  | 
| Wav2Vec2 | ✅ | ✅ |  | 
| Whisper | ✅ | ✅ |  | 
| SpeechT5 |  |  |  | 
| CLIP | ✅ | ✅ |  | 
| BridgeTower | ✅ | ✅ |  | 
| ESMFold |  |  |  | 
| Blip |  |  |  | 
| OWLViT |  |  |  | 
| ClipSeg |  |  |  | 
| Llava / Llava-next / Llava-onevision |  |  |  | 
| idefics2 |  |  |  | 
| Paligemma |  |  |  | 
| Segment Anything Model |  |  |  | 
| VideoMAE |  |  |  | 
| TableTransformer |  |  |  | 
| DETR |  |  |  | 
| Mllama |  | ✅ |  | 
| MiniCPM3 |  |  |  | 
| Baichuan2 |  |  |  | 
| DeepSeek-V2 | ✅ | ✅ |  | 
| DeepSeek-V3 / Moonlight |  | ✅ |  | 
| ChatGLM |  |  |  | 
| Qwen2-VL |  |  |  | 
| Qwen2.5-VL |  |  |  | 
| VideoLLaVA |  |  |  | 
| GLM-4V |  |  |  | 
| Arctic |  |  |  | 
| GPT-OSS |  |  |  | 

- Diffusers

| Architecture | Training. | Inference | Tasks | 
|---|---|---|---|
| Stable Diffusion | ✅ | ✅ |  | 
| Stable Diffusion XL | ✅ | ✅ |  | 
| Stable Diffusion Depth2img |  |  |  | 
| Stable Diffusion 3 | ✅ | ✅ |  | 
| LDM3D |  |  |  | 
| FLUX.1 |  |  |  | 
| Qwen Image |  |  |  | 
| Text to Video |  |  |  | 
| Image to Video |  |  |  | 
| i2vgen-xl |  |  |  | 
| Wan |  | ✅ |  | 

- PyTorch Image Models/TIMM:

| Architecture | Training | Inference | Tasks | 
|---|---|---|---|
| FastViT |  |  |  | 

- TRL:

| Architecture | Training | Inference | Tasks | 
|---|---|---|---|
| Llama 2 | ✅ |  |  | 
| Llama 2 | ✅ |  |  | 
| Stable Diffusion | ✅ |  |  | 

Other models and tasks supported by the 🤗 Transformers and 🤗 Diffusers library may also work.
You can refer to this [section](https://github.com/huggingface/optimum-habana#how-to-use-it) for using them with 🤗 Optimum for Intel Gaudi.
In addition, [this page](https://huggingface.co/examples) explains how to modify any [example](https://github.com/huggingface/transformers/tree/main/examples/pytorch) from the 🤗 Transformers library to make it work with 🤗 Optimum for Intel Gaudi.

[Update on GitHub](https://github.com/huggingface/optimum-habana/blob/main/docs/source/index.mdx)