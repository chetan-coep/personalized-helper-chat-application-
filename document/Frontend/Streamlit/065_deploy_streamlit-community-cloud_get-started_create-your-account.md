---
id: "streamlit_065"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 65
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account"
language: "en"
retrieved_at: "2026-11-01 22:26:27"
content_hash: "f892e00f40eb253325c6e482d2da62aa1836e285d776c81ff30e7216a86607ef"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account

---

# 

Before you can start deploying apps for the world to see, you need to sign up for your Streamlit Community Cloud account.

Each Community Cloud account is associated with an email. Two accounts can't have the same email. When sharing a private app, you will assign viewing privileges by email. Additionally, two accounts can't have the same source control (GitHub account). If you try to create a second Community Cloud account with the same source control, Community Cloud will merge the accounts.

## 

Community Cloud allows you to sign in using one of the three following methods:

- Emailed, one-use codes
- GitHub

*priority\_high*

#### Important

Even when you sign in through GitHub, the authentication flow returns your email address to Community Cloud. Changing the email on your GitHub account can affect your Community Cloud account if you sign in through GitHub.

1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Click "**Continue to sign-in**."
3. Continue with one of the three options listed below. 
  1. In the "Email" field, enter your email address.
  2. Click "**Continue**." (If prompted, verify you are human.)
  3. Go to your email inbox, and copy your one-time, six-digit code. The code is valid for ten minutes.
  4. Return to the authentication page, and enter your code. (If prompted, verify you are human.)
  1. Click "**Continue with Google**."
  2. Enter your Google credentials, and follow Google's authentication prompts.
  1. Click "**Continue with GitHub**."
  2. Enter your GitHub credentials, and follow GitHub's authentication prompts. This adds the "Streamlit Community Cloud" OAuth application to your GitHub account. This application is only used to pass your email when you sign in to Community Cloud. On the next page, you'll perform additional steps to allow Community Cloud to access your repositories. For more information about using and reviewing the OAuth applications on your account, see [Using OAuth apps](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps) in GitHub's docs.
4. Fill in your information, and click "**Continue**" at the bottom.
The "Primary email" field is prefilled with the email you used to sign in. If you change this email in the account setup form, it will only impact marketing emails; it will not reflect on your new account. To change the email associated with your account after it's created, see [Update your email address](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/update-your-email).

## 

Congratulations on creating your Streamlit Community Cloud account! A warning icon (*warning*) next to "**Workspaces**" in the upper-left corner is expected; this indicates that your account is not yet connected to GitHub. Even if you created your account by signing in through GitHub, your account does not yet have permission to access your repositories. Continue to the next page to connect your GitHub account.

[*arrow\_back*Previous: Quickstart](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart)

[*arrow\_forward*Next: Connect your GitHub account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.