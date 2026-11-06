---
id: "streamlit_079"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 79
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization"
language: "en"
retrieved_at: "2026-11-01 22:26:21"
content_hash: "e48072d9bb62febd89ba4c7043bd652d3e8e1d0ec92f9e99b09a31b72fecaf53"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization

---

# 

Streamlit Community Cloud copies all the files in your repository and executes `streamlit run` from its root directory. Because Community Cloud is creating a new Python environment to run your app, you need to include a declaration of any [App dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) in addition to any [Configuration](https://docs.streamlit.io/develop/concepts/configuration) options.

You can have multiple apps in your repository, and their entrypoint files can be anywhere in your repository. However, you can only have one configuration file. This page explains how to correctly organize your app, configuration, and dependency files. The following examples assume you are using `requirements.txt` to declare your dependencies because it is the most common. As explained on the next page, Community Cloud supports other formats for configuring your Python environment.

## 

In the following example, the entrypoint file (`your_app.py`) is in the root of the project directory alongside a `requirements.txt` file to declare the app's dependencies.

```
your_repository/
├── requirements.txt
└── your_app.py
```
If you are including custom configuration, your config file must be located at `.streamlit/config.toml` within your repository.

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── your_app.py
```
Additionally, any files that need to be locally available to your app should be included in your repository.

*star*

#### Tip

If you have really big or binary data that you change frequently, and git is running slowly, you might want to check out [Git Large File Store (LFS)](https://git-lfs.github.com/) as a better way to store large files in GitHub. You don't need to make any changes to your app to start using it. If your GitHub repository uses LFS, it will *just work* with Streamlit Community Cloud.

## 

When your entrypoint file is in a subdirectory, the configuration file must stay at the root. However, your dependency file may be either at the root or next to your entrypoint file.

Your dependency file can be at the root of your repository while your entrypoint file is in a subdirectory.

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── subdirectory
    └── your_app.py
```
Alternatively, your dependency file can be in the same subdirectory as your entrypoint file.

```
your_repository/
├── .streamlit/
│   └── config.toml
└── subdirectory
    ├── requirements.txt
    └── your_app.py
```
Although most Streamlit commands interpret paths relative to the entrypoint file, some commands interpret paths relative to the working directory. On Community Cloud, the working directory is always the root of your repository. Therefore, when developing and testing your app locally, execute `streamlit run` from the root of your repository. This ensures that paths are interpreted consistently between your local environment and Community Cloud.

In the previous example, this would look something like this:

```
cd your_repository
streamlit run subdirectory/your_app.py
```
*star*

#### Tip

Remember to always use forward-slash path separators in your paths. Community Cloud can't work with backslash-separated paths.

## 

When you have multiple apps in one repository, they share the configuration file (`.streamlit/config.toml`) at the root of your repository. To give an app its own configuration, place a `.streamlit/config.toml` file next to its entrypoint file in a subdirectory. Its values take precedence over the shared file. A dependency file may be shared or configured separately for these multiple apps. To define separate dependency files for your apps, place each entrypoint file in its own subdirectory along with its own dependency file. To learn more about how Community Cloud prioritizes and parses dependency files, see [App dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies).

[*arrow\_back*Previous: Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)

[*arrow\_forward*Next: App dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.