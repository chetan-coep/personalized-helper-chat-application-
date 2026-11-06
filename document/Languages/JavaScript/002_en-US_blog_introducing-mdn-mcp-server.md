---
id: "javascript_002"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 2
source_url: "https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server"
language: "en"
retrieved_at: "2026-11-01 21:52:44"
content_hash: "dc69ef2cb1ba4fa93703be7b48957073a3703a3c2d5ef7d8b08f2f89c9a4ebdc"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server

---

# Introducing the MDN MCP server

We're excited to announce the release of the [MDN MCP server](https://developer.mozilla.org/en-US/mcp).
[MCP (Model Context Protocol)](https://modelcontextprotocol.io/docs/learn/server-concepts) is an open standard that enables AI tools to connect to external data sources. The MDN MCP server uses this protocol to bring MDN's documentation and browser compatibility data directly into your AI agent or [IDE](https://developer.mozilla.org/en-US/docs/Glossary/IDE).

## [Why we built the MDN MCP](https://developer.mozilla.org#why_we_built_the_mdn_mcp)

More and more AI tools are being integrated into web development workflows, but they can surface outdated web platform information based on their training data and knowledge cutoff.

For example, an LLM or coding agent may not know that a feature like [`@view-transition` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition) exists, or whether it has reached ["Widely Available" baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility#baseline_badges) and is safe to use across browsers.

The MDN MCP gives your coding agent access to accurate, up-to-date web platform information. It also makes it easier for you to access the latest documentation without leaving your preferred tools.

The server is currently experimental. See our [privacy notice](https://developer.mozilla.org/en-US/mcp#privacy_and_data_retention) for details about data handling during this phase.

## [How to use the MDN MCP](https://developer.mozilla.org#how_to_use_the_mdn_mcp)

The MDN MCP server works with any MCP-compatible client, including:

- **Editors**: [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Zed](https://zed.dev/docs/ai/mcp), and [Cursor](https://docs.cursor.com/context/mcp).
- **Agent CLIs**: [Claude Code](https://docs.claude.com/en/docs/claude-code/mcp), [Codex CLI](https://developers.openai.com/codex/mcp), and [Antigravity CLI](https://antigravity.google/docs/mcp) (previously Gemini CLI).
- **Chat apps**: [Claude Desktop](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).

See the links in this list for how to set up MCP with each tool. For installation instructions and other details, check our [MDN MCP server](https://developer.mozilla.org/en-US/mcp) page .

As a quick example, to use it with Claude Code, you would run the following:

```
claude mcp add --transport http mdn https://mcp.mdn.mozilla.net/
```
We're looking forward to seeing how you integrate it into your web development workflow, and the scenarios where you find it most useful.

## [What difference does the MCP make?](https://developer.mozilla.org#what_difference_does_the_mcp_make)

Given the non-deterministic nature of LLMs and the variety of available models, it's often challenging to compare their behavior with or without certain skills, prompts, tools, and MCPs enabled.

We tested Claude Code Opus 4.7 with and without the MDN MCP on a few features recently shipped in [Firefox 151](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/151), asking how to use the features and what the browser support is. Specifically:

1. How to use the `light-dark()` CSS function for images and which browsers support it?
2. How to use the `:buffering` CSS pseudo-class and which browsers support it?
3. How to use the `shadowrootslotassignment` attribute on `<template>` and which browsers support it?
4. How to use the Web Serial API and which browsers support it?

We noticed certain patterns in the results. In most cases, the usage notes from Claude Code with and without the MDN MCP enabled were comparable. Some answers which used the MCP were better structured and more complete. For example, the notes for the [`light-dark()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark) also included examples with linear gradients that weren't directly mentioned in the question but are also supported.

When it came to browser support information, the winner was clear: the MDN MCP produced much better and more reliable results. Claude Code without the MCP got the browser support right only in one case: for the [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering) pseudo-class. For example, Claude Code without the MCP insisted that the declarative [`shadowrootslotassignment`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootslotassignment) attribute is supported in Chrome 120 and Safari 18.3, possibly conflating it with the `Element.attachShadow()`'s [`slotAssignment`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow#slotassignment) option. But in fact, Firefox 151 is the first browser to [ship support for this attribute](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/151#html).

Without the MCP, Claude Code also didn't provide any concrete browser support information about using images in the `light-dark()` function: "support is less uniform than the color variant", while with the MCP, it provided the full table listing Firefox 150 and Chrome (behind a flag) as supported browsers.

The worst performance of Claude Code without the MCP came from the Web Serial API question. Firefox 151 [shipped support for the Web Serial API](https://hacks.mozilla.org/2026/05/web-serial-support-in-firefox/) in May 2026. However, Claude Code without the MCP correctly mentioned Chromium-based browsers as supporting this feature, but also insisted that in Firefox it's:

Not implemented (and not on the roadmap â see Mozilla's standards position: "harmful")


With the MCP enabled, Claude Code correctly identified that Firefox 151 ships support for the Web Serial API, in line with the [release notes](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/151).

Additionally, we noticed that in our tests, responses which used the MDN MCP were roughly twice as fast. Without the MCP, Claude Code had to fetch and parse quite a few HTML pages to find current information, which took some time, but even then didn't provide accurate results.

## [Get involved](https://developer.mozilla.org#get_involved)

Your feedback helps us improve. If you encounter issues, have comments or suggestions, or want to share how you're using the MDN MCP, we'd love to hear from you. Please feel free to come chat with us in the [platform channel](https://discord.com/channels/1009925603572600863/1170042997212184576) in our Discord. If you spot any issues, please raise them in the [mdn/mcp GitHub repository](https://github.com/mdn/mcp/issues).

## [What's next](https://developer.mozilla.org#whats_next)

As AI tools become a bigger part of web development workflows, we're committed to making MDN's documentation available wherever you need it. This release is one step toward that goal, and we're excited to continue improving the experience with your input.