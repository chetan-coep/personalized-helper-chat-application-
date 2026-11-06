---
id: "llms_031"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 31
source_url: "https://huggingface.co/docs/accelerate"
language: "en"
retrieved_at: "2026-11-01 22:40:22"
content_hash: "36629f0d7161432c5d0ef493e000c53f1aa70aa7b9d15884e2ef2d9eb441ad78"
---

# LLMs

Source: https://huggingface.co/docs/accelerate

---

Accelerate documentation

Accelerate

# 

Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration by adding just four lines of code! In short, training and inference at scale made simple, efficient and adaptable.

```
+ from accelerate import Accelerator
+ accelerator = Accelerator()
+ model, optimizer, training_dataloader, scheduler = accelerator.prepare(
+     model, optimizer, training_dataloader, scheduler
+ )
  for batch in training_dataloader:
      optimizer.zero_grad()
      inputs, targets = batch
      inputs = inputs.to(device)
      targets = targets.to(device)
      outputs = model(inputs)
      loss = loss_function(outputs, targets)
+     accelerator.backward(loss)
      optimizer.step()
      scheduler.step()
```
Built on `torch_xla` and `torch.distributed`, Accelerate takes care of the heavy lifting, so you don’t have to write any custom code to adapt to these platforms.
Convert existing codebases to utilize [DeepSpeed](https://huggingface.co/usage_guides/deepspeed), perform [fully sharded data parallelism](https://huggingface.co/usage_guides/fsdp), and have automatic support for mixed-precision training!

To get a better idea of this process, make sure to check out the [Tutorials](https://huggingface.co/basic_tutorials/overview)!


This code can then be launched on any system through Accelerate’s CLI interface:

`accelerate launch {my_script.py}`
[Tutorials Learn the basics and become familiar with using Accelerate. Start here if you are using Accelerate for the first time!](https://huggingface.co/basic_tutorials/overview)

[How-to guides Practical guides to help you achieve a specific goal. Take a look at these guides to learn how to use Accelerate to solve real-world problems.](https://huggingface.co/usage_guides/explore)

[Conceptual guides High-level explanations for building a better understanding of important topics such as avoiding subtle nuances and pitfalls in distributed training and DeepSpeed.](https://huggingface.co/concept_guides/gradient_synchronization)

[Reference Technical descriptions of how Accelerate classes and methods work.](https://huggingface.co/package_reference/accelerator)

[Update on GitHub](https://github.com/huggingface/accelerate/blob/main/docs/source/index.md)