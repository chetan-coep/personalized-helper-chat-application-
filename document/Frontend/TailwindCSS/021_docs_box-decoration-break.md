---
id: "tailwindcss_021"
technology: "TailwindCSS"
category: "Frontend"
title: "box-decoration-break - Layout - Tailwind CSS"
doc_order: 21
source_url: "https://tailwindcss.com/docs/box-decoration-break"
language: "en"
retrieved_at: "2026-11-03 17:59:38"
content_hash: "88ba4ba5e4f075920b829363abb757fbf8ed37b4ebd7589de93a4c896f3c287e"
---

# box-decoration-break - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/box-decoration-break

---

Layout

Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.

| Class | Styles | 
|---|---|
| `box-decoration-clone` | `box-decoration-break: clone;` | 
| `box-decoration-slice` | `box-decoration-break: slice;` | 

Use the `box-decoration-slice` and `box-decoration-clone` utilities to control whether properties like background, border, border-image, box-shadow, clip-path, margin, and padding should be rendered as if the element were one continuous fragment, or distinct blocks:

Prefix a `box-decoration-break` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<div class="box-decoration-clone md:box-decoration-slice ...">  <!-- ... --></div>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).