---
id: "streamlit_094"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 94
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app"
language: "en"
retrieved_at: "2026-11-01 22:27:01"
content_hash: "024779f86b30e240483e4dbdf76a79be5935bb2ae88d91102157f268907ce6e1"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app

---

# 

Streamlit Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you move or rename one of these coordinates without preparation, you will lose access to administer any associated app.

## 

If you need to rename your repository, move your entrypoint file, or otherwise change a deployed app's GitHub coordinates, do the following:

1. Delete your app.
2. Make your desired changes in GitHub.
3. Redeploy your app.

## 

If you have changed a repository so that Community Cloud can no longer find your app on GitHub, your app will be missing or shown as view-only. View-only means that you can't edit, reboot, delete, or view settings for your app. You can only access analytics.

You may be able to regain control as follows:

1. Revert the change you made to your app so that Community Cloud can see the owner, repository, branch, and entrypoint file it expects.
2. Sign out of Community Cloud and GitHub.
3. Sign back in to Community Cloud and GitHub.
4. If you have regained access, delete your app. Proceed with your original change, and redeploy your app. If this does not restore access to your app, please [contact Snowflake support](https://docs.streamlit.io/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud) for assistance. They can delete your disconnected apps so you can redeploy them. For the quickest help, please provide a complete list of your affected apps by URL.

[*arrow\_back*Previous: Reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)

[*arrow\_forward*Next: Upgrade Python](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.