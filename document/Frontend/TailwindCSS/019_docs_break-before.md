---
id: "tailwindcss_019"
technology: "TailwindCSS"
category: "Frontend"
title: "break-before - Layout - Tailwind CSS"
doc_order: 19
source_url: "https://tailwindcss.com/docs/break-before"
language: "en"
retrieved_at: "2026-11-03 17:59:37"
content_hash: "2f2b70a18e91cdce05a12f3733b489de7412dcfa41805aeb9bd122d5b315e5ed"
---

# break-before - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/break-before

---

Layout

Utilities for controlling how a column or page should break before an element.

| Class | Styles | 
|---|---|
| `break-before-auto` | `break-before: auto;` | 
| `break-before-avoid` | `break-before: avoid;` | 
| `break-before-all` | `break-before: all;` | 
| `break-before-avoid-page` | `break-before: avoid-page;` | 
| `break-before-page` | `break-before: page;` | 
| `break-before-left` | `break-before: left;` | 
| `break-before-right` | `break-before: right;` | 
| `break-before-column` | `break-before: column;` | 

Use utilities like `break-before-column` and `break-before-page` to control how a column or page break should behave before an element:

`<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-before-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>`
Prefix a `break-before` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<div class="break-before-column md:break-before-auto ...">  <!-- ... --></div>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).