---
id: "rag_022"
technology: "RAG"
category: "ML & Data"
title: "Prompt engineering quickstart - Docs by LangChain"
doc_order: 22
source_url: "https://docs.langchain.com/langsmith/prompt-engineering-quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:08"
content_hash: "31612b9b8aa30376f80b25780b0305a526066e764046ddb65054a9fffd0e9142"
---

# Prompt engineering quickstart - Docs by LangChain

Source: https://docs.langchain.com/langsmith/prompt-engineering-quickstart

---

Prompts guide the behavior of Large Language Models (LLM).

[*Prompt engineering*](https://docs.langchain.com/langsmith/prompt-engineering-concepts)is the process of crafting, testing, and refining the instructions you give to an LLM so it produces reliable and useful responses. LangSmith provides tools to create, version, test, and collaborate on prompts. You’ll also encounter common concepts like

[*prompt templates*](https://docs.langchain.com/langsmith/prompt-engineering-concepts#prompts-vs-prompt-templates), which let you reuse structured prompts, and

[*variables*](https://docs.langchain.com/langsmith/prompt-engineering-concepts#f-string-vs-mustache), which allow you to dynamically insert values (such as a user’s question) into a prompt. In this quickstart, you’ll create, test, and improve prompts using either the UI or the SDK. This quickstart will use OpenAI as the example LLM provider, but the same workflow applies across other providers.

## Prerequisites

Before you begin, make sure you have:
- **A LangSmith account**: Sign up or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-prompt-engineering-quickstart).
- **A LangSmith API key**: Follow the [Create an API key](https://docs.langchain.com/langsmith/create-account-api-key) guide.
- **An OpenAI API key**: Generate this from the [OpenAI dashboard](https://platform.openai.com/account/api-keys).

Select the tab for UI or SDK workflows:

- UI
- SDK

## 1. Set workspace secret

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

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-prompt-engineering-quickstart), navigate to the **Prompts** section in the left-hand menu.
2. Click on **+ Prompt** to create a prompt.
3. Modify the prompt by editing or adding prompts and input variables as needed.

## 3. Test a prompt

1. 
Under the **Prompts** heading select the gear  icon next to the model name, which will launch the **Prompt Settings** window on the **Model Configuration** tab.
2. 
Set the [model configuration](https://docs.langchain.com/langsmith/managing-model-configurations) you want to use. The **Provider** and **Model** you select will determine the parameters that are configurable on this configuration page. Once set, click **Save as**.
3. 
Specify the input variables you would like to test in the **Inputs** box and then click **Start**.
To learn about more options for configuring your prompt in the Playground, refer to[Configure prompt settings](https://docs.langchain.com/langsmith/managing-model-configurations).
4. 
After testing and refining your prompt, click **Save** to store it for future use.

## 4. Iterate on a prompt

LangSmith allows for team-based prompt iteration.
[Workspace](https://docs.langchain.com/langsmith/administration-overview#workspaces)members can experiment with prompts in the Playground and save their changes as a new

[*commit*](https://docs.langchain.com/langsmith/prompt-engineering-concepts#commits)when ready.To improve your prompts:

- Reference the documentation provided by your model provider for best practices in prompt creation, such as:
- Build and refine your prompts with the Prompt Canvas—an interactive tool in LangSmith. Learn more in the [Prompt Canvas guide](https://docs.langchain.com/langsmith/write-prompt-with-ai).
- Tag specific commits to mark important moments in your commit history.
  1. To create a commit, navigate to the **Playground** and select **Commit**. Choose the prompt to commit changes to and then **Commit**.
  2. Navigate to **Prompts** in the left-hand menu. Select the prompt. On the prompt detail page, select **Tag** on the top right to add a [commit tag](https://docs.langchain.com/langsmith/manage-prompts#commit-tags).

## Next steps

- Learn more about how to store and manage prompts using the Prompt Hub in the [Create a prompt guide](https://docs.langchain.com/langsmith/create-a-prompt).
- Learn how to set up the Playground to [Test multi-turn conversations](https://docs.langchain.com/langsmith/multiple-messages) in this tutorial.
- Learn how to test your prompt’s performance over a dataset instead of individual examples, refer to [Run an evaluation from the Playground](https://docs.langchain.com/langsmith/run-evaluation-from-playground).