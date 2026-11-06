---
id: "streamlit_003"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 3
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart"
language: "en"
retrieved_at: "2026-11-01 22:26:35"
content_hash: "11805124129661f3cd6ed44954a1ea410bb027e1034d733e18b2dcb838e73372"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart

---

# 

This is a concise set of steps to create your Streamlit Community Cloud account, deploy a sample app, and start editing it with GitHub Codespaces. For other options and complete explanations, start with [Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account).

You will sign in to your GitHub account during this process. Community Cloud will use the email from your GitHub account to create your Community Cloud account. For other sign-in options, see [Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account).

## 

- You must have a GitHub account.

## 

1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Click "**Continue to sign-in**."
3. Click "**Continue with GitHub**."
4. Enter your GitHub credentials and follow GitHub's authentication prompts.
5. Fill in your account information, and click "**I accept**" at the bottom.

## 

1. In the upper-left corner, click "**Workspaces *warning***."

1. From the drop down, click "**Connect GitHub account**."
2. Enter your GitHub credentials and follow GitHub's authentication prompts.
3. Click "**Authorize streamlit**."

## 

1. In the upper-left corner, click on your GitHub username.

1. From the drop down, click "**Settings**."
2. On the left side of the dialog, select "**Linked accounts**."
3. Under "Source control," click "**Connect here *arrow\_forward***."
4. Click "**Authorize streamlit**."

## 

1. In the upper-right corner, click "**Create app**."

1. When asked "Do you already have an app?" click "**Nope, create one from a template**."
2. From the list of templates on the left, select "**Blank app**."
3. At the bottom, select the option to "**Open GitHub Codespaces...**"
4. At the bottom, click "**Deploy**."

## 

1. Wait for GitHub to set up your codespace. It can take several minutes to fully initialize your codespace. After the Visual Studio Code editor appears in your codespace, it can take several minutes to install Python and start the Streamlit server. When complete, a split screen view displays a code editor on the left and a running app on the right. The code editor opens two tabs by default: the repository's readme file and the app's entrypoint file.
2. Go to the app's entrypoint file (`streamlit_app.py`) in the left pane, and change line 3 by adding "Streamlit" inside `st.title`.
Python```
-st.title("🎈 My new app")
+st.title("🎈 My new Streamlit app")
```
Files are automatically saved in your codespace with each edit.
3. A moment after typing a change, your app on the right side will display a rerun prompt. Click "**Always rerun**."
4. Optional: Continue to make edits and observe the changes within seconds.

## 

1. In the left navigation bar, click the source control icon.

1. In the source control sidebar on the left, enter a name for your commit.
2. Click "***check* Commit**."

1. To stage and commit all your changes, in the confirmation dialog, click "**Yes**." Your changes are committed locally in your codespace.
2. To push your commit to GitHub, in the source control sidebar on the left, click "***cached* 1 *arrow\_upward***."
3. To push commits to "origin/main," in the confirmation dialog, click "**OK**."
Your changes are now saved to your GitHub repository. Community Cloud will immediately reflect the changes in your deployed app.
4. Optional: To see your updated, published app, return to the "**My apps**" section of your workspace at [share.streamlit.io](https://share.streamlit.io), and click on your app.

## 

When you stop interacting with your codespace, GitHub will generally stop your codespace for you. However, the surest way to avoid undesired use of your capacity is to stop or delete your codespace when you are done.

1. Go to [github.com/codespaces](https://github.com/codespaces). At the bottom of the page, all your codespaces are listed. Click the overflow menu icon (*more\_horiz*) for your codespace.

1. If you want to return to your work later, click "**Stop codespace**." Otherwise, click "**Delete**."
2. Congratulations! You just deployed an app to Streamlit Community Cloud. 🎉 Return to your workspace at [share.streamlit.io/](https://share.streamlit.io/) and [deploy another Streamlit app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

[*arrow\_back*Previous: Get started](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started)

[*arrow\_forward*Next: Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.