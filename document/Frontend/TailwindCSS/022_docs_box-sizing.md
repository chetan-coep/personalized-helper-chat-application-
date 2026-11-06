---
id: "tailwindcss_022"
technology: "TailwindCSS"
category: "Frontend"
title: "box-sizing - Layout - Tailwind CSS"
doc_order: 22
source_url: "https://tailwindcss.com/docs/box-sizing"
language: "en"
retrieved_at: "2026-11-03 17:59:39"
content_hash: "b32ff7d6e5493c3588057bca786d947b010b1c7567178fbc3516abfa1b0136fc"
---

# box-sizing - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/box-sizing

---

Layout

Utilities for controlling how the browser should calculate an element's total size.

| Class | Styles | 
|---|---|
| `box-border` | `box-sizing: border-box;` | 
| `box-content` | `box-sizing: content-box;` | 

Use the `box-border` utility to set an element's `box-sizing` to `border-box`, telling the browser to include the element's borders and padding when you give it a height or width.

This means a 100px × 100px element with a 2px border and 4px of padding on all sides will be rendered as 100px × 100px, with an internal content area of 88px × 88px:

Tailwind makes this the default for all elements in our [preflight base styles](https://tailwindcss.com/docs/preflight).

Use the `box-content` utility to set an element's `box-sizing` to `content-box`, telling the browser to add borders and padding on top of the element's specified width or height.

This means a 100px × 100px element with a 2px border and 4px of padding on all sides will actually be rendered as 112px × 112px, with an internal content area of 100px × 100px:

Prefix a `box-sizing` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<div class="box-content md:box-border ...">  <!-- ... --></div>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).