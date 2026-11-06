---
id: "llms_059"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 59
source_url: "https://huggingface.co/docs/safetensors"
language: "en"
retrieved_at: "2026-11-01 22:41:26"
content_hash: "743dae15e0338bf98d3e00fb7325160137da294d965f7abd486060127b808442"
---

# LLMs

Source: https://huggingface.co/docs/safetensors

---

Safetensors documentation

Safetensors

Getting started

API

You are viewing main version, which requires installation from source. If you'd like
			regular pip install, checkout the latest stable version ([v0.5.0-rc.0](https://huggingface.co/docs/safetensors/v0.5.0-rc.0/index)).

# 

Safetensors is a new simple format for storing tensors safely (as opposed to pickle) and that is still fast (zero-copy). Safetensors is really [fast 🚀](https://huggingface.co/speed).

## 

with pip:

`pip install safetensors`
with conda:

`conda install -c conda-forge safetensors`
## 

### 

```
from safetensors import safe_open
tensors = {}
with safe_open("model.safetensors", framework="pt", device=0) as f:
    for k in f.keys():
        tensors[k] = f.get_tensor(k)
```
Loading only part of the tensors (interesting when running on multiple GPU)

```
from safetensors import safe_open
tensors = {}
with safe_open("model.safetensors", framework="pt", device=0) as f:
    tensor_slice = f.get_slice("embedding")
    vocab_size, hidden_dim = tensor_slice.get_shape()
    tensor = tensor_slice[:, :hidden_dim]
```
### 

```
import torch
from safetensors.torch import save_file
tensors = {
    "embedding": torch.zeros((2, 2)),
    "attention": torch.zeros((2, 3))
}
save_file(tensors, "model.safetensors")
```
## 

Let’s say you have safetensors file named `model.safetensors`, then `model.safetensors` will have the following internal format:

## 

Safetensors is being used widely at leading AI enterprises, such as [Hugging Face](https://huggingface.co/), [EleutherAI](https://www.eleuther.ai/), and [StabilityAI](https://stability.ai/). Here is a non-exhaustive list of projects that are using safetensors:

[Update on GitHub](https://github.com/huggingface/safetensors/blob/main/docs/source/index.mdx)