---
id: "tailwindcss_025"
technology: "TailwindCSS"
category: "Frontend"
title: "clear - Layout - Tailwind CSS"
doc_order: 25
source_url: "https://tailwindcss.com/docs/clear"
language: "en"
retrieved_at: "2026-11-03 17:59:41"
content_hash: "3ceccee2d2be4f6e5cb0358a852eb2279f4de4a0196eb1d3b8c81c3d2402bdac"
---

# clear - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/clear

---

Layout

Utilities for controlling the wrapping of content around an element.

| Class | Styles | 
|---|---|
| `clear-left` | `clear: left;` | 
| `clear-right` | `clear: right;` | 
| `clear-both` | `clear: both;` | 
| `clear-start` | `clear: inline-start;` | 
| `clear-end` | `clear: inline-end;` | 
| `clear-none` | `clear: none;` | 

Use the `clear-left` utility to position an element below any preceding left-floated elements:

Use the `clear-right` utility to position an element below any preceding right-floated elements:

Use the `clear-both` utility to position an element below all preceding floated elements:

Use the `clear-start` and `clear-end` utilities, which use [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts) to map to either the left or right side based on the text direction:

Use the `clear-none` utility to reset any clears that are applied to an element:

Prefix a `clear` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<p class="clear-left md:clear-none ...">  Lorem ipsum dolor sit amet...</p>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).