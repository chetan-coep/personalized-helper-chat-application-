---
id: "llms_061"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 61
source_url: "https://huggingface.co/docs/setfit"
language: "en"
retrieved_at: "2026-11-01 22:41:29"
content_hash: "3ebe16233ba985cd0d275cff17bb470d74cd8013b74febd6f1fcf2527c6f2772"
---

# LLMs

Source: https://huggingface.co/docs/setfit

---

SetFit documentation

SetFit

# 

🤗 SetFit is an efficient and prompt-free framework for few-shot fine-tuning of [Sentence Transformers](https://sbert.net/). It achieves high accuracy with little labeled data - for instance, with only 8 labeled examples per class on the Customer Reviews sentiment dataset, 🤗 SetFit is competitive with fine-tuning RoBERTa Large on the full training set of 3k examples!

Compared to other few-shot learning methods, SetFit has several unique features:

- 🗣 **No prompts or verbalizers:** Current techniques for few-shot fine-tuning require handcrafted prompts or verbalizers to convert examples into a format suitable for the underlying language model. SetFit dispenses with prompts altogether by generating rich embeddings directly from text examples.
- 🏎 **Fast to train:** SetFit doesn’t require large-scale models like T0, Llama or GPT-4 to achieve high accuracy. As a result, it is typically an order of magnitude (or more) faster to train and run inference with.
- 🌎 **Multilingual support**: SetFit can be used with any [Sentence Transformer](https://huggingface.co/models?library=sentence-transformers&sort=downloads) on the Hub, which means you can classify text in multiple languages by simply fine-tuning a multilingual checkpoint.

[Tutorials Learn the basics and become familiar with loading pretrained Sentence Transformers and fine-tuning them on data. Start here if you are using 🤗 SetFit for the first time!](https://huggingface.co/tutorials/overview)

[How-to guides Practical guides to help you achieve a specific goal. Take a look at these guides to learn how to use 🤗 SetFit to solve real-world problems.](https://huggingface.co/how_to/overview)

[Conceptual guides High-level explanations for building a better understanding about important topics such as few-shot and contrastive learning.](https://huggingface.co/conceptual_guides/setfit)

[Reference Technical descriptions of how 🤗 SetFit classes and methods work.](https://huggingface.co/reference/main)

[\< > Update on GitHub](https://github.com/huggingface/setfit/blob/main/docs/source/en/index.mdx)