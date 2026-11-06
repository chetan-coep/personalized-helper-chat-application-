---
id: "streamlit_098"
technology: "Streamlit"
category: "Frontend"
title: "Streamlit"
doc_order: 98
source_url: "https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app"
language: "en"
retrieved_at: "2026-11-01 22:27:07"
content_hash: "205b7a11668aaad52cdb9b7ea839cf4ee5a0ff8edfe91e87d19f93264eb12884"
---

# Streamlit

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app

---

# 

Embedding Streamlit Community Cloud apps enriches your content by integrating interactive, data-driven applications directly within your pages. Whether you're writing a blog post, a technical document, or sharing resources on platforms like Medium, Notion, or even StackOverflow, embedding Streamlit apps adds a dynamic component to your content. This allows your audience to interact with your ideas, rather than merely reading about them or looking at screenshots.

Streamlit Community Cloud supports both [iframe](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-iframes) and [oEmbed](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-oembed) methods for embedding **public** apps. This flexibility enables you to share your apps across a wide array of platforms, broadening your app's visibility and impact. In this guide, we'll cover how to use both methods effectively to share your Streamlit apps with the world.

## 

Streamlit Community Cloud supports embedding **public** apps using the subdomain scheme. To embed a public app, add the query parameter `/?embed=true` to the end of the `*.streamlit.app` URL.

For example, say you want to embed the [30DaysOfStreamlit app](https://30days.streamlit.app/). The URL to include in your iframe is: `https://30days.streamlit.app/?embed=true`:

```
<iframe
  src="https://30days.streamlit.app?embed=true"
  style="height: 450px; width: 100%;"
></iframe>
```
*priority\_high*

#### Important

There will be no official support for embedding private apps.

In addition to allowing you to embed apps via iframes, the `?embed=true` query parameter also does the following:

- Removes the toolbar with the app menu icon (*more\_vert*).
- Removes the padding at the top and bottom of the app.
- Removes the footer.

For granular control over the embedding behavior, Streamlit allows you to specify one or more instances of the `?embed_options` query parameter (e.g. to show the toolbar, open the app in dark theme, etc). [Click here for a full list of Embed options.](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options)

## 

Streamlit's oEmbed support allows for a simpler embedding experience. You can directly drop a Streamlit app's URL into a Medium, Ghost, or Notion page (or any of more than 700 content providers that supports oEmbed or [embed.ly](https://embed.ly/)). The embedded app will automatically appear! This helps Streamlit Community Cloud apps seamlessly integrate into these platforms, improving the visibility and accessibility of your apps.

### 

When creating content in a Notion page, Medium article, or Ghost blog, you only need to paste the app's URL and hit "**Enter**." The app will then render automatically at that spot in your content. You can use your undecorated app URL without the `?embed=true` query parameter.

```
https://30days.streamlit.app/
```
Here's an example of [@chrieke](https://github.com/chrieke)'s [Prettymapp app](https://chrieke-prettymapp-streamlit-prettymappapp-1k0qxh.streamlit.app/) embedded in a Medium article:

*star*

#### Tip

Ensure the platform hosting the embedded Streamlit app supports oEmbed or [embed.ly](https://embed.ly/).

### 

oEmbed should work out of the box for several platforms including but not limited to:

Please check the specific platform's documentation to verify support for oEmbed.

### 

The only noteworthy differences between the methods is that iframing allows you to customize the app's embedding behavior (e.g. showing the toolbar, opening the app in dark theme, etc) using the various `?embed_options` described in the next section.

## 

When [Embedding with iframes](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-iframes), Streamlit allows you to specify one or more instances of the `?embed_options` query parameter for granular control over the embedding behavior.

Both `?embed` and `?embed_options` are invisible to [`st.query_params`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params). You can't get or set their values.

The supported values for `?embed_options` are listed below:

1. Show the toolbar at the top right of the app which includes the app menu (*more\_vert*), running man, and link to GitHub.
JavaScript```
/?embed=true&embed_options=show_toolbar
```
2. Show padding at the top and bottom of the app. JavaScript```
/?embed=true&embed_options=show_padding
```
3. Show the footer reading "Made with Streamlit." (This doesn't apply to Streamlit versions 1.29.0 and later since the footer was removed from the library.) JavaScript```
/?embed=true&embed_options=show_footer
```
4. Hide the "skeleton" that appears while an app is loading. JavaScript```
/?embed=true&embed_options=hide_loading_screen
```
5. Disable scrolling for the main body of the app. (The sidebar will still be scrollable.) JavaScript```
/?embed=true&embed_options=disable_scrolling
```
6. Open the app with light theme. JavaScript```
/?embed=true&embed_options=light_theme
```
7. Open the app with dark theme. JavaScript```
/?embed=true&embed_options=dark_theme
```

You can also combine the params:

```
/?embed=true&embed_options=show_toolbar&embed_options=show_padding&embed_options=show_footer&embed_options=disable_scrolling
```
### 

You can conveniently build an embed link for your app — right from your app!

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Click "**Embed**" to access a list of selectable embed options.
3. Select your embed options and click "**Get embed link**" to copy the embed link to your clipboard.

[*arrow\_back*Previous: Share your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app)

[*arrow\_forward*Next: Search indexability](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.