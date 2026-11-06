---
id: "llms_045"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 45
source_url: "https://huggingface.co/docs/kernels"
language: "en"
retrieved_at: "2026-11-01 22:40:57"
content_hash: "2ff7c093a3d19a0c79d446bb7707ddb980e72c292b981123655c46321132fadb"
---

# LLMs

Source: https://huggingface.co/docs/kernels

---

Kernels documentation

Kernels

Get started

Use kernels

Python API

kernels CLI

Build kernels

kernel-builder CLI

Advanced practices

Kernel specifications

Concepts & design

Resources

You are viewing main version, which requires [installation from source](https://huggingface.co/docs/kernels/installation#installation). If you'd like
			regular pip install, checkout the latest stable version ([v0.18.0](https://huggingface.co/docs/kernels/v0.18.0/index)).

# 

The Kernel Hub allows Python libraries and applications to load compute
kernels directly from the [Hub](https://huggingface.co/). Kernels are a first-class
repository type on the Hub, with dedicated pages that surface supported
hardware and versions. To support dynamic loading, Hub kernels differ from
traditional Python kernel packages in that they are made to be:

- **Portable**: a kernel can be loaded from paths outside `PYTHONPATH`.
- **Unique**: multiple versions of the same kernel can be loaded in the
same Python process.
- **Compatible**: `kernels` must support all recent versions of Python and
the different PyTorch build configurations (various CUDA versions
and C++ ABIs). Furthermore, older C library versions must be supported.

Browse available kernels at [huggingface.co/kernels](https://huggingface.co/kernels).

The Kernels project is divided into two parts:

- Builder: [`kernel-builder`](https://huggingface.co/builder-cli) provides utilities to build, package, and distribute compute kernels in a way that is compatible with the Hugging Face Hub and `kernels`.
- `kernels`: The [`kernels`](https://huggingface.co/basic-usage) is a Python package that lets
users load compatible compute kernels from the Hub. Refer to the [quickstart](https://huggingface.co/basic-usage) to know more.

If you’re looking for a more involved “Why kernels?” answer, refer to [this page](https://huggingface.co/why_kernels).

The [talks page](https://huggingface.co/talks) page has links to talks on the
Kernels project. The [blog page](https://huggingface.co/blog) collects blog posts
on the Kernels project.

[Update on GitHub](https://github.com/huggingface/kernels/blob/main/docs/source/index.md)