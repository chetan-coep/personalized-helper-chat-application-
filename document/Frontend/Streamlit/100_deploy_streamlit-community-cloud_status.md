---
id: "streamlit_100"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 100
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/status"
language: "en"
retrieved_at: "2026-11-01 22:27:12"
content_hash: "0dc13f0c8ee3e906e33c9e5b1ec7ff8e50d2c5a6c35a6ebf19f6578516a63ae3"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/status

---

# 

## 

You can view the current status of Community Cloud at [streamlitstatus.com](https://www.streamlitstatus.com/).

## 

To deploy your app, Streamlit requires access to your app's source code in GitHub and the ability to manage the public keys associated with your repositories. The default GitHub OAuth scopes are sufficient to work with apps in public GitHub repositories. However, to access your private repositories, we create a read-only [GitHub Deploy Key](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys) and then access your repo using an SSH key. When we create this key, GitHub notifies repo admins of the creation as a security measure.

Streamlit requires the additional `repo` OAuth scope from GitHub to work with your private repos and manage deploy keys. We recognize that the `repo` scope provides Streamlit with extra permissions that we do not really need and which, as people who prize security, we'd rather not even be granted. This was the permission model available from GitHub when Community Cloud was created. However, we are working on adopting the new GitHub permission model to reduce uneeded permissions.

### 

Because of the OAuth limitations noted above, a developer must have administrative permissions to a repository to deploy apps from it.

## 

You can deploy multiple apps from your repository, and your entrypoint file(s) may be anywhere in your directory structure. However, Community Cloud initializes all apps from the root of your repository, even if the entrypoint file is in a subdirectory. This has the following consequences:

- Streamlit reads the `.streamlit/config.toml` file at the root (of each branch) of your repository. If your entrypoint file is in a subdirectory, Streamlit also reads the `.streamlit/config.toml` file in that subdirectory, and its values take precedence. For more information, see [Working with configuration options](https://docs.streamlit.io/develop/concepts/configuration/options).
- You must declare image, video, and audio file paths for Streamlit commands relative to the root of your repository. For example, `st.image`, `st.logo`, and the `page_icon` parameter in `st.set_page_config` expect file locations relative to your working directory (i.e. where you execute `streamlit run`).

## 

Community Cloud is built on Debian Linux.

- Community Cloud uses Debian 11 ("bullseye"). To browse available packages that can be installed, see the [package list](https://packages.debian.org/bullseye/).
- All file paths must use forward-slash path separators.

## 

- You cannot mix and match Python package managers for a single app. Community Cloud configures your app's Python environment based on the first environment configuration file it finds. For more information, see [Other Python package managers](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#other-python-package-managers).
- We recommend that you use the latest version of Streamlit to ensure full Community Cloud functionality. Be sure to take note of Streamlit's [current requirements](https://github.com/streamlit/streamlit/blob/develop/lib/pyproject.toml) for package compatibility when planning your environment, especially `protobuf>=5.26.1,<8`.
- If you pin `streamlit< 1.20.0`, you must also pin `altair<5`. Earlier versions of Streamlit did not correctly restrict Altair's version. A workaround script running on Community Cloud will forcibly install `altair<5` if a newer version is detected. This could unintentionally upgrade Altair's dependencies in violation of your environment configuration. Newer versions of Streamlit support Altair version 5.
- Community Cloud only supports released versions of Python that are still receiving security updates. You may not use end-of-life, prerelease, or feature versions of Python. For more information, see [Status of Python versions](https://devguide.python.org/versions/).

## 

The following configuration options are set within Community Cloud and will override any contrary setting in your `config.toml` file:

```
[client]
showErrorDetails = false
[runner]
fastReruns = true
[server]
runOnSave = true
enableXsrfProtection = true
[browser]
gatherUsageStats = true
```
## 

If you need to whitelist IP addresses for a connection, Community Cloud is currently served from the following IP addresses:

*priority\_high*

#### Warning

These IP addresses may change at any time without notice.

## 

- When you print something to the Cloud logs, you may need to do a `sys.stdout.flush()` before it shows up.
- Community Cloud hosts all apps in the United States. This is currently not configurable.
- Community Cloud rate limits app updates from GitHub to no more than five per minute.

[*arrow\_back*Previous: Manage your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account)

[*arrow\_forward*Next: Snowflake](https://docs.streamlit.io/deploy/snowflake)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.