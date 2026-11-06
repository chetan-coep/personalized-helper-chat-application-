---
id: "streamlit_087"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 87
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app"
language: "en"
retrieved_at: "2026-11-01 22:26:49"
content_hash: "96cc79fc35b99d6144f75956d21615806330c3dc8c628fa1706c76a1818f76c3"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app

---

# 

You can manage your deployed app from your workspace at [share.streamlit.io](https://share.streamlit.io) or directly from `<your-custom-subdomain>.streamlit.app`. You can view, deploy, delete, reboot, or favorite an app.

## 

Streamlit Community Cloud is organized into workspaces, which automatically group your apps according to their repository's owner in GitHub. Your workspace is indicated in the upper-left corner. For more information, see [Switching workspaces](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/explore-your-workspace#switching-workspaces).

To deploy or manage any app, always switch to the workspace matching the repository's owner first.

### 

If you have many apps in your workspace, you can pin apps to the top by marking them as favorite (*star*). For more information, see [Favorite your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app).

### 

Each app has a menu accessible from the overflow icon (*more\_vert*) to the right.

- **Edit with Codespaces** — See [Edit your app with GitHub Codespaces](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces)
- **Reboot** — See [Reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
- **Delete** — See [Delete your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
- **Analytics** — See [App analytics](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
- **Settings** — See [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings)

If you have view-only access to an app, all options in the app's menu will be disabled except analytics.

## 

You can manage your deployed app directly from the app itself! Just make sure you are signed in to Community Cloud, and then visit your app.

### 

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Manage app**" in the lower-right corner.
2. Once you've clicked on "**Manage app**", you will be able to view your app's logs. This is your primary place to troubleshoot any issues with your app.
3. You can access more developer options by clicking the overflow icon (*more\_vert*) at the bottom of your Cloud logs. To conveniently download your logs, click "**Download log**."

Other options accessible from Cloud logs are:

- **Analytics** — See [App analytics](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics).
- **Reboot app** — See [Reboot your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app).
- **Delete app** — See [Delete your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app).
- **Settings** — See [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings).
- **Your apps** — Takes you to your [app workspace](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#manage-your-app-from-your-workspace).
- **Documentation** — Takes you to our documentation.
- **Support** — Takes you to [our forums](https://discuss.streamlit.io/)!

### 

From your app at `<your-custom-subdomain>.streamlit.app`, you can always access the [app chrome](https://docs.streamlit.io/develop/concepts/architecture/app-chrome) just like you can when developing locally. The option to deploy your app is removed, but you can still clear your cache from here.

## 

### 

Your GitHub repository is the source for your app, so that means that any time you push an update to your repository you'll see it reflected in the app in almost real time. Try it out!

Streamlit also smartly detects whether you touched your dependencies, in which case it will automatically do a full redeploy for you—which will take a little more time. But since most updates don't involve dependency changes, you should usually see your app update in real time.

### 

To add or remove dependencies at any point, just update `requirements.txt` (Python dependenciess) or `packages.txt` (Linux dependencies), and commit the changes to your repository on GitHub. Community Cloud detects the change in your dependencies and automatically triggers (re)installation.

It is best practice to pin your Streamlit version in `requirements.txt`. Otherwise, the version may be auto-upgraded at any point without your knowledge, which could lead to undesired results (e.g. when we deprecate a feature in Streamlit).

## 

### 

All Community Cloud users have access to the same resources and are subject to the same limits. These limits may change at any time without notice. If your app meets or exceeds its limits, it may slow down from throttling or become nonfunctional. The limits as of February 2024 are approximately as follows:

- CPU: 0.078 cores minimum, 2 cores maximum
- Memory: 690MB minimum, 2.7GBs maximum
- Storage: No minimum, 50GB maximum

Symptoms that your app is running out of resources include the following:

- Your app is running slowly.
- Your app displays "🤯 This app has gone over its resource limits."
- Your app displays "😦 Oh no."

### 

Streamlit offers increased resources for apps with good-for-the-world use cases. Generally, these apps are used by an educational institution or nonprofit organization, are part of an open-source project, or benefit the world in some way. If your app is **not** primarily used by a for-profit company you can [apply for increased resources](https://info.snowflake.com/streamlit-resource-increase-request.html).

### 

If your app is running slow or showing the error pages mentioned above, we first highly recommend going through and implementing the suggestions in the following blog posts to prevent your app from hitting the resource limits and to detect if your Streamlit app leaks memory:

If your app exceeds its resource limits, developers and viewers alike will see "😦 Oh no."

If see "😦 Oh no." when viewing your app, first check your Cloud logs for any specific errors. If there are no errors in your Cloud logs you are likely dealing with a resource issue.

#### 

If you are signed in to a developer account for an app over its limits, you can access "**Manage app**" from the lower-right corner of the app to reboot it and clear its memory. "**Manage app**" will be red and have a warning icon (*error*).

### 

All apps without traffic for 12 hours go to sleep. Community Cloud hibernates apps to conserve resources and allow the best communal use of the platform. To keep your app awake, simply visit your app.

When someone visits a sleeping app, they will see the sleeping page:

To wake the app up, click "**Yes, get this app back up!**" This can be done by *anyone* who has access to view the app, not just the app developer!

You can see which of your apps are asleep from your workspace. Sleeping apps have a moon icon (*bedtime*) to the right.

[*arrow\_back*Previous: Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)

[*arrow\_forward*Next: App analytics](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.