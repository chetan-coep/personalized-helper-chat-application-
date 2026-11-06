---
id: "streamlit_073"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 73
source_url: "https://docs.streamlit.io/deploy/concepts/secrets"
language: "en"
retrieved_at: "2026-11-01 22:27:16"
content_hash: "c2a60d3b743b5f12ace8b621618a2e7b02170cf39c9d5926e63089eccff81eac"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/concepts/secrets

---

# 

If you are connecting to data sources or external services, you will likely be handling secret information like credentials or keys. Secret information should be stored and transmitted in a secure manner. When you deploy your app, ensure that you understand your platform's features and mechanisms for handling secrets so you can follow best practice.

Avoid saving secrets directly in your code and keep `.gitignore` updated to prevent accidentally committing a local secret to your repository. For helpful reminders, see [Security reminders](https://docs.streamlit.io/develop/concepts/connections/security-reminders).

If you are using Streamlit Community Cloud, [Secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) allows you save environment variables and store secrets outside of your code. If you are using another platform designed for Streamlit, check if they have a built-in mechanism for working with secrets. In some cases, they may even support `st.secrets` or securely uploading your `secrets.toml` file.

For information about using `st.connection` with environment variables, see [Global secrets, managing multiple apps and multiple data stores](https://docs.streamlit.io/develop/concepts/connections/connecting-to-data#global-secrets-managing-multiple-apps-and-multiple-data-stores).

[*arrow\_back*Previous: Dependencies](https://docs.streamlit.io/deploy/concepts/dependencies)

[*arrow\_forward*Next: Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.