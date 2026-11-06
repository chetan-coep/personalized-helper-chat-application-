---
id: "streamlit_095"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 95
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python"
language: "en"
retrieved_at: "2026-11-01 22:27:02"
content_hash: "8c6f087bcf6d5604eee15a635ab752d9438948c497c961feacd517895946e0fd"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python

---

# 

Dependencies within Python can be upgraded in place by simply changing your environment configuration file (typically `requirements.txt`). However, Python itself can't be changed after deployment.

When you deploy an app, you can select the version of Python through the "**Advanced settings**" dialog. After you have deployed an app, you must delete it and redeploy it to change the version of Python it uses.

1. Take note of your app's settings: 
  - Current, custom subdomain.
  - GitHub coordinates (repository, branch, and entrypoint file path).
  - Secrets.
When you delete an app, its custom subdomain is immediately available for reuse.
2. [Delete your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app).
3. [Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).
  1. On the deployment page, select your app's GitHub coordinates.
  2. Set your custom domain to match your deleted instance.
  3. Click "**Advanced settings**."
  4. Choose your desired version of Python.
  5. Optional: If your app had secrets, re-enter them.
  6. Click "**Save**."
  7. Click "**Deploy**."

In a few minutes, Community Cloud will redirect you to your redployed app.

[*arrow\_back*Previous: Rename your app in GitHub](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)

[*arrow\_forward*Next: Upgrade Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.