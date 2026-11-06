---
id: "streamlit_064"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 64
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account"
language: "en"
retrieved_at: "2026-11-01 22:26:25"
content_hash: "1511c25e1b55b2ff1169ca724e5bac695e40d0fd849d3e732203979cd053ff52"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account

---

# 

Connecting GitHub to your Streamlit Community Cloud account allows you to deploy apps directly from the files you store in your repositories. It also lets the system check for updates to those files and automatically update your apps. When you first connect your GitHub account to your Community Cloud account, you'll be able to deploy apps from your public repositories to Community Cloud. If you want to deploy from private repositories, you can give Community Cloud additional permissions to do so. For more information about these permissions, see [GitHub OAuth scope](https://docs.streamlit.io/deploy/streamlit-community-cloud/status#github-oauth-scope).

*priority\_high*

#### Important

In order to deploy an app, you must have **admin** permissions to its repository. If you don't have admin access, contact the repository's owner or fork the repository to create your own copy. For more help, see our [community forum](https://discuss.streamlit.io/).

If you are a member of a GitHub organization, that organization is displayed at the bottom of each GitHub OAuth prompt. In this case, we recommend reading about [Organization access](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access) at the end of this page before performing the steps to connect your GitHub account. You must be an organization's owner in GitHub to grant access to that organization.

## 

- You must have a Community Cloud account. See [Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account).
- You must have a GitHub account.

## 

1. In the upper-left corner, click "**Workspaces *warning***."

1. From the drop down, click "**Connect GitHub account**."
2. Enter your GitHub credentials and follow GitHub's authentication prompts.
3. Click "**Authorize streamlit**."
This adds the "Streamlit" OAuth application to your GitHub account. This allows Community Cloud to work with your public repositories and create codespaces for you. In the next section, you can allow Community Cloud to access your private repositories, too. For more information about using and reviewing the OAuth applications on your account, see [Using OAuth apps](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps) in GitHub's docs.

## 

After your Community Cloud account has access to deploy from your public repositories, you can follow these additional steps to grant access to your private repositories.

1. In the upper-left corner, click on your GitHub username.

1. From the drop down, click "**Settings**."
2. On the left side of the dialog, select "**Linked accounts**."
3. Under "Source control," click "**Connect here *arrow\_forward***."
4. Click "**Authorize streamlit**."

## 

To deploy apps from repositories owned by a GitHub organization, Community Cloud must have permission to access the organization's repositories. If you are a member of a GitHub organization when you connect your GitHub account, your OAuth prompts will include a section labeled "Organization access."

If you have already connected your GitHub account and need to add access to an organization, follow the steps in [Manage your GitHub connection](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection) to disconnect your GitHub account and start over. Alternatively, if you are not the owner of an organization, you can ask the owner to create a Community Cloud account for themselves and add permission directly.

### 

For any organization you own, if authorization has not been previously granted or denied, you can click "**Grant**" before you click "**Authorize streamlit**."

### 

For an organization you don't own, if authorization has not been previously granted or denied, you can click "**Request**" before you click "**Authorize streamlit**."

### 

If someone has already started the process of authorizing Streamlit for your organization, the OAuth prompt will show the current status.

#### 

If an organization has already granted Streamlit access, the OAuth prompt shows a green check (*check*).

#### 

If a request has been previously sent but not yet approved, the OAuth prompt show "Access request pending." Follow up with the organization's owner to accept the request in GitHub.

#### 

If a request has been previously sent and denied, the OAuth prompt shows a red X (*close*). In this case, the organization owner will need to authorize Streamlit from GitHub. See GitHub's documentation on [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

## 

Now that you have your account you can [Explore your workspace](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/explore-your-workspace). Or if you're ready to go, jump right in and [Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

[*arrow\_back*Previous: Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account)

[*arrow\_forward*Next: Explore your workspace](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/explore-your-workspace)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.