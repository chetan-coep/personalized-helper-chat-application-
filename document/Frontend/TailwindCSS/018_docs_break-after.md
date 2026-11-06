---
id: "tailwindcss_018"
technology: "TailwindCSS"
category: "Frontend"
title: "break-after - Layout - Tailwind CSS"
doc_order: 18
source_url: "https://tailwindcss.com/docs/break-after"
language: "en"
retrieved_at: "2026-11-03 17:59:36"
content_hash: "e2eecdedd38613285f16528dcf448ce658c3f9b891e8f42a008ae93efa5aa150"
---

# break-after - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/break-after

---

Layout

Utilities for controlling how a column or page should break after an element.

| Class | Styles | 
|---|---|
| `break-after-auto` | `break-after: auto;` | 
| `break-after-avoid` | `break-after: avoid;` | 
| `break-after-all` | `break-after: all;` | 
| `break-after-avoid-page` | `break-after: avoid-page;` | 
| `break-after-page` | `break-after: page;` | 
| `break-after-left` | `break-after: left;` | 
| `break-after-right` | `break-after: right;` | 
| `break-after-column` | `break-after: column;` | 

Use utilities like `break-after-column` and `break-after-page` to control how a column or page break should behave after an element:

`<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-after-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>`
Prefix a `break-after` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<div class="break-after-column md:break-after-auto ...">  <!-- ... --></div>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).