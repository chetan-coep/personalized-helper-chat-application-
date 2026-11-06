---
id: "react.js_018"
technology: "React.js"
category: "Frontend"
title: "React Developer Tools – React"
doc_order: 18
source_url: "https://react.dev/learn/react-developer-tools"
language: "en"
retrieved_at: "2026-11-03 17:58:35"
content_hash: "1ecd064dc1f1481a8b7683ec43f087ce6e10f0d787c4ed71feaaa6d96d0045f4"
---

# React Developer Tools – React

Source: https://react.dev/learn/react-developer-tools

---

Use React Developer Tools to inspect React [components](https://react.dev/learn/your-first-component), edit [props](https://react.dev/learn/passing-props-to-a-component) and [state](https://react.dev/learn/state-a-components-memory), and identify performance problems.

### You will learn

- How to install React Developer Tools

The easiest way to debug websites built with React is to install the React Developer Tools browser extension. It is available for several popular browsers:

Now, if you visit a website **built with React,** you will see the *Components* and *Profiler* panels.

For other browsers (for example, Safari), install the [`react-devtools`](https://www.npmjs.com/package/react-devtools) npm package:

```
# Yarn
yarn global add react-devtools
# Npm
npm install -g react-devtools
```
Next open the developer tools from the terminal:

`react-devtools`
Then connect your website by adding the following `<script>` tag to the beginning of your website’s `<head>`:

```
<html>
  <head>
    <script src="http://localhost:8097"></script>
```
Reload your website in the browser now to view it in developer tools.

To inspect apps built with [React Native](https://reactnative.dev/), you can use [React Native DevTools](https://reactnative.dev/docs/react-native-devtools), the built-in debugger that deeply integrates React Developer Tools. All features work identically to the browser extension, including native element highlighting and selection.

For versions of React Native earlier than 0.76, please use the standalone build of React DevTools by following the [Safari and other browsers](https://react.dev#safari-and-other-browsers) guide above.