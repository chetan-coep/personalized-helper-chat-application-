---
id: "rag_018"
technology: "RAG"
category: "ML & Data"
title: "Evaluation quickstart - Docs by LangChain"
doc_order: 18
source_url: "https://docs.langchain.com/langsmith/evaluation-quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:01"
content_hash: "4ee4ef9d542d8d77e1c33e3fd08f1a05fcbcb80f3b2752ebc5c1d5adfcadf8a7"
---

# Evaluation quickstart - Docs by LangChain

Source: https://docs.langchain.com/langsmith/evaluation-quickstart

---

[*Evaluations*](https://docs.langchain.com/langsmith/evaluation-concepts)are a quantitative way to measure the performance of LLM applications. LLMs can behave unpredictably, even small changes to prompts, models, or inputs can significantly affect results. Evaluations provide a structured way to identify failures, compare versions, and build more reliable AI applications. Running an evaluation in LangSmith requires three key components:

- [*Dataset*](https://docs.langchain.com/langsmith/evaluation-concepts#datasets): A set of test inputs (and optionally, expected outputs).
- [*Target function*](https://docs.langchain.com/langsmith/define-target-function): The part of your application you want to test—this might be a single LLM call with a new prompt, one module, or your entire workflow.
- [*Evaluators*](https://docs.langchain.com/langsmith/evaluation-concepts#evaluators): Functions that score your target function’s outputs.

This quickstart guides you through running a starter evaluation that checks the correctness of LLM responses, using either the LangSmith SDK or UI.

## Prerequisites

Before you begin, make sure you have:
- **A LangSmith account**: Sign up or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-evaluation-quickstart).
- **A LangSmith API key**: Follow the [Create an API key](https://docs.langchain.com/langsmith/create-account-api-key) guide.
- **An OpenAI API key**: Generate this from the [OpenAI dashboard](https://platform.openai.com/account/api-keys).

**Select the UI or SDK filter for instructions:**

- UI
- SDK

## 1. Set workspace secrets

In the
[LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=snippets-langsmith-set-workspace-secrets), ensure that your API key is set as a

[workspace secret](https://docs.langchain.com/langsmith/set-up-hierarchy#configure-workspace-settings).Adding workspace secrets requires permission to manage secrets in the workspace. If you do not have it, ask a workspace admin to add the secret for you or to grant you access.To add a workspace secret:

1. 
Navigate to  **Settings** > **Integrations** > **Provider secrets**.
2. 
Select **+ Secret**.
3. 
Under **Provider**, select your model provider. LangSmith names the secret with the environment variable the provider expects, such as `OPENAI_API_KEY`. Enter your secret in that field.
If your provider is not listed, leave **Custom** as the provider. Enter the environment variable name your provider expects as the **Key** and your API key as the **Value**.
4. 
Select **Save**.

If your provider authenticates with OAuth2 `client_credentials`, configure the credentials on the model configuration instead. Workspace secrets are not required in that case. See [OAuth client credentials](https://docs.langchain.com/langsmith/model-configurations#oauth-client-credentials).

## 2. Create a prompt

The
[Playground](https://docs.langchain.com/langsmith/prompt-engineering-concepts#playground)makes it possible to run evaluations over different prompts, new models, or test different model configurations.

1. 
In the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-evaluation-quickstart), click **Playground** in the sidebar.
2. 
Under the **Prompts** panel, modify the **system** prompt to:
Leave the**Human** message as is: `{question}`.

## 3. Create a dataset

1. 
Click **Set up Evaluation**, which will open a **New Experiment** table at the bottom of the page.
2. 
In the **Select or create a new dataset** dropdown, click the **+ New** button to create a new dataset.
3. 
Add the following examples to the dataset:
4. 
Click **Save** and enter a name to save your newly created dataset.

## 4. Add an evaluator

1. Click **+ Evaluator** and select **Correctness** from the **Prebuilt Evaluator** options.
2. In the **Correctness** panel, click **Save**.

## 5. Run your evaluation

1. 
Select  **Start** on the top right to run your evaluation. This will create an [*experiment*](https://docs.langchain.com/langsmith/evaluation-concepts#experiment) with a preview in the **New Experiment** table. You can view in full by clicking the experiment name.

## Next steps

- For more details on evaluations, refer to the [Evaluation documentation](https://docs.langchain.com/langsmith/evaluation).
- Learn how to [create and manage datasets in the UI](https://docs.langchain.com/langsmith/manage-datasets-in-application#create-a-dataset-and-add-examples).
- Learn how to [run an evaluation from the Playground](https://docs.langchain.com/langsmith/run-evaluation-from-playground).