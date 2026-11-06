---
id: "rag_019"
technology: "RAG"
category: "ML & Data"
title: "Quickstart - Docs by LangChain"
doc_order: 19
source_url: "https://docs.langchain.com/langsmith/fleet/quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:02"
content_hash: "dee5f1addf1c3507afc3ff6e90bcb926ac9694abd916b8a44bbbb00a2d675638"
---

# Quickstart - Docs by LangChain

Source: https://docs.langchain.com/langsmith/fleet/quickstart

---

By the end of this quickstart, you will have an Executive Assistant that labels the Gmail messages needing your attention and pauses for approval before acting, all set up without code or a model API key and controlled through chat. You will start from the prebuilt

**Executive Assistant**

[template](https://docs.langchain.com/langsmith/fleet/templates), which manages your inbox, calendar, and daily brief.

## Before you start

You need:
- A LangSmith account ([sign up here](https://smith.langchain.com/agents?skipOnboarding=true&utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-fleet-quickstart)).
- A Gmail account.
- A Google Calendar.

Fleet manages the AI model for you, so you do not need your own model provider API key. For more information, see

[Models](https://docs.langchain.com/langsmith/fleet/essentials#models).

## 1. Create your agent

Choose a template

1. Select **Templates** in the left-hand navigation, or click **+** in **My Agents** and select **From template**.
2. Select the **Executive Assistant** template to create your agent.
3. Click **Create Agent** at the top right.

Answer onboarding questions

## 2. Connect tools

Your agent asks you to connect to your Gmail and Google Calendar accounts. A connection gives your agent the
[tools](https://docs.langchain.com/langsmith/fleet/tools)to use a service. A

[channel](https://docs.langchain.com/langsmith/fleet/channels)lets the service trigger the agent. You connect Gmail and Google Calendar here, then add Gmail as a channel in

[Configure your agent](https://docs.langchain.com#3-configure-your-agent).

Connect Gmail

1. In the **Gmail** row, click **Connect** on the right.
2. In the dialog, click **+ Connect new account**.
3. Choose your account and click **Continue**.
4. Review permissions and click **Allow**.
5. LangSmith redirects you back to Fleet. Select **Gmail** to expand the row.
6. Click **Choose account** and select the account you chose in step 3.

Connect Google Calendar

1. Connecting Gmail authorized your Google account for Gmail only, not Google Calendar. To grant calendar access, click **Update permissions** on the right in the **Google Calendar** row.
2. In the dialog, click **Reauthorize**.
3. Choose your account and click **Continue**.
4. Review permissions and click **Allow**.
5. LangSmith redirects you back to Fleet. Close the dialog.
6. Click **Save and continue**.

## 3. Configure your agent

There are two ways to configure your agent:
- Chatting with your agent directly
- Modifying settings in the [agent sidebar](https://docs.langchain.com/langsmith/fleet/essentials#agent-sidebar)

This section describes how to configure your agent using the agent sidebar.

Open the agent sidebar

**Configure**at the top right to open the agent sidebar.

Configure a tool to ask for approval

**Connections**drawer, click

**Gmail**to view the available tools. By default, the tools are enabled and set to

**Auto**, so they run without your approval.For

**Apply Label**, click

**Ask**, so your agent pauses and waits for your approval before continuing. You can accept the proposed action, or reject it and tell the agent what to change. For more information, see

[Human-in-the-loop](https://docs.langchain.com/langsmith/fleet/essentials#human-in-the-loop).

Connect channels

**Channels**drawer. Click

**Gmail**. Select the account that you set up for

**Connections**. Click

**Confirm**.

Save your changes

**Save**at the top of the sidebar to save your changes, then click

**X**to close the panel.

## 4. Test your agent

Send your agent a task

*Apply a “Review” label to emails that I receive, which require some kind of review from me.*

Accept or reject the agent's action

**Accept**to approve the agent’s proposed action or tell the agent what it did wrong and click

**Reject**.

Check your inbox in Gmail

**Accept**, emails that need review now have the

**Review**label in your inbox.

## Edit your agent

You may want to update your agent’s instructions or include more tools. You can chat with your agent directly to ask for updates, or configure it from the
[agent sidebar](https://docs.langchain.com/langsmith/fleet/essentials#agent-sidebar):

- Edit the agent’s instructions (its `AGENTS.md`) in the **Knowledge** drawer. See [Instructions](https://docs.langchain.com/langsmith/fleet/essentials#instructions).
- Add integrations and tools in the **Connections** drawer, and set each tool to run automatically or [ask for approval](https://docs.langchain.com/langsmith/fleet/essentials#human-in-the-loop). See [Tools](https://docs.langchain.com/langsmith/fleet/tools).
- Connect [Slack](https://docs.langchain.com/langsmith/fleet/slack-app), [Gmail](https://docs.langchain.com/langsmith/fleet/channels#add-a-gmail-channel), or [Microsoft Teams](https://docs.langchain.com/langsmith/fleet/teams-app) in the **Channels** drawer.
- Run your agent on a [schedule](https://docs.langchain.com/langsmith/fleet/schedules) in the **Schedules** drawer.
- Change the [model](https://docs.langchain.com/langsmith/fleet/manage-agent-settings#change-the-model) in the **Advanced settings** drawer.