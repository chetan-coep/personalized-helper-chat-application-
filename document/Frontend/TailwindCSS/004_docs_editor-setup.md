---
id: "tailwindcss_004"
technology: "TailwindCSS"
category: "Frontend"
title: "Editor setup - Getting started - Tailwind CSS"
doc_order: 4
source_url: "https://tailwindcss.com/docs/editor-setup"
language: "en"
retrieved_at: "2026-11-03 17:59:23"
content_hash: "37d038db2664e20b911cf45378d5733ad8ebb3cbd7ea4fbee7777c612ba4223d"
---

# Editor setup - Getting started - Tailwind CSS

Source: https://tailwindcss.com/docs/editor-setup

---

Getting started

Tooling to improve the developer experience when working with Tailwind CSS.

Tailwind CSS uses custom CSS syntax like `@theme`, `@variant`, and `@source`, and in some editors this can trigger warnings or errors where these rules aren't recognized.

If you're using VS Code, our official [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) plugin includes a dedicated Tailwind CSS language mode that has support for all of the custom at-rules and functions Tailwind uses.

In some cases, you may need to disable native CSS linting/validations if your editor is very strict about the syntax it expects in your CSS files.

[Cursor](https://cursor.com/?utm_source=tailwind) is an AI-native code editor with features like context-aware autocomplete and built-in coding agents. Since it supports VS Code extensions, all of the Tailwind CSS tooling you're already familiar with works out of the box – including our official [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) extension and the [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) for class sorting.

Check out and download [Cursor](https://cursor.com/?utm_source=tailwind).

[Zed](https://zed.dev/?utm_source=tailwind) is a fast, modern code editor, designed from the ground-up for cutting-edge development workflows, including agentic editing with AI. It has built-in support for Tailwind CSS autocompletions, linting, and hover previews, without the need to install and configure a separate extension. It also integrates tightly with Prettier, so our official [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) works seamlessly with Zed when installed.

Check out [Zed](https://zed.dev/?utm_source=tailwind) and learn more about [how it works with Tailwind CSS](https://zed.dev/docs/languages/tailwindcss?utm_source=tailwind).

The official [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) extension for Visual Studio Code enhances the Tailwind development experience by providing users with advanced features such as autocomplete, syntax highlighting, and linting.

Check out the project [on GitHub](https://github.com/tailwindcss/intellisense) to learn more, or [add it to Visual Studio Code](vscode:extension/bradlc.vscode-tailwindcss) to get started now.

We maintain an official [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) for Tailwind CSS that automatically sorts your classes following our [recommended class order](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#how-classes-are-sorted).

It works seamlessly with custom Tailwind configurations, and because it’s just a Prettier plugin, it works anywhere Prettier works — including every popular editor and IDE, and of course on the command line.

`<!-- Before --><button class="text-white px-4 sm:px-8 py-2 sm:py-3 bg-sky-700 hover:bg-sky-800">Submit</button><!-- After --><button class="bg-sky-700 px-4 py-2 text-white hover:bg-sky-800 sm:px-8 sm:py-3">Submit</button>`
Check out the plugin [on GitHub](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) to learn more and get started.

JetBrains IDEs like WebStorm, PhpStorm, and others include support for intelligent Tailwind CSS completions in your HTML.