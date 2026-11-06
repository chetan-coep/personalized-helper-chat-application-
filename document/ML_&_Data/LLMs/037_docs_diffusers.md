---
id: "llms_037"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 37
source_url: "https://huggingface.co/docs/diffusers"
language: "en"
retrieved_at: "2026-11-01 22:40:40"
content_hash: "adf912c284f6e7a913f23976231764180ba13c487b2865e3183be4ad891f6dec"
---

# LLMs

Source: https://huggingface.co/docs/diffusers

---

Diffusers documentation

Diffusers

Get started

Inference

Using diffusion pipelines

Adapters and personalization

Optimize and scale

[Basic performance](https://huggingface.co/docs/diffusers/stable_diffusion)

Inference

Community methods

Quantization

Hardware-specific acceleration

Serving and scaling

Modular Diffusers

Train and fine-tune

Resources

Contribute

API



# 

Diffusers provides pretrained diffusion models and the building blocks for custom image, video, and audio workflows.

It has two main paths.

- [DiffusionPipeline](https://huggingface.co/docs/diffusers/v0.42.1/en/api/pipelines/overview#diffusers.DiffusionPipeline) supports few-line inference with pretrained checkpoints, plus adapters like LoRA. This is the easy path for generation.
- [Modular Diffusers](https://huggingface.co/modular_diffusers/overview) enables composable blocks and [ModularPipeline](https://huggingface.co/docs/diffusers/v0.42.1/en/api/modular_diffusers/pipeline#diffusers.ModularPipeline) for custom pipelines when you need more control.

Optimizations such as offloading and quantization keep large models runnable on memory-constrained devices. If memory is not an issue, Diffusers also supports `torch.compile` for faster inference.

Browse trending Diffusers models on the [Hub](https://huggingface.co/models?library=diffusers&sort=trending) now.

## 

If you’re a beginner, start with the [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course/unit0/1). It covers diffusion theory and how to generate images, fine-tune models, and more with Diffusers.

The [Quickstart](https://huggingface.co/quicktour) also includes a copyable agent setup prompt for inference.

## 

- [Inference](https://huggingface.co/using-diffusers/loading) — load pipelines and run generation
- [Optimize and scale](https://huggingface.co/stable_diffusion) — memory, speed, quantization, and serving
- [Modular Diffusers](https://huggingface.co/modular_diffusers/overview) — build custom pipelines from blocks
- [Train and fine-tune](https://huggingface.co/training/overview) — train diffusion models and adapters
- [CLI](https://huggingface.co/using-diffusers/cli) - run and package pipelines from the command line

[Update on GitHub](https://github.com/huggingface/diffusers/blob/main/docs/source/en/index.md)