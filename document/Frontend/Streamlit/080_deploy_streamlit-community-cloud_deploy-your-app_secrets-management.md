---
id: "streamlit_080"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 80
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management"
language: "en"
retrieved_at: "2026-11-01 22:26:22"
content_hash: "4bfef04f8250024a9ed6ea41609f73d31269106286ee2f50efe9c2b1699febc5"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

---

# 

## 

If you are [connecting to data sources](https://docs.streamlit.io/develop/tutorials/databases), you will likely need to handle credentials or secrets. Storing unencrypted secrets in a git repository is a bad practice. If your application needs access to sensitive credentials, the recommended solution is to store those credentials in a file that is not committed to the repository and to pass them as environment variables.

## 

Community Cloud lets you save your secrets within your app's settings. When developing locally, you can use `st.secrets` in your code to read secrets from a `.streamlit/secrets.toml` file. However, this `secrets.toml` file should never be committed to your repository. Instead, when you deploy your app, you can paste the contents of your `secrets.toml` file into the "**Advanced settings**" dialog. You can update your secrets at any time through your app's settings in your workspace.

### 

- You should understand how to use `st.secrets` and `secrets.toml`. See [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management).

### 

While deploying your app, you can access "**Advanced settings**" to set your secrets. After your app is deployed, you can view or update your secrets through the app's settings. The deployment workflow is fully described on the next page, but the "**Advanced settings**" dialog looks like this:

Simply copy and paste the contents of your local `secrets.toml` file into the "Secrets" field within the dialog. After you click "**Save**" to commit the changes, that's it!

### 

If you need to add or edit your secrets for an app that is already deployed, you can access secrets through your [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings). See [View or update your secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-update-your-secrets).

[*arrow\_back*Previous: App dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)

[*arrow\_forward*Next: Deploy!](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.