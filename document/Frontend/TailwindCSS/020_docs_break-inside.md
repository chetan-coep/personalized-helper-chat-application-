---
id: "tailwindcss_020"
technology: "TailwindCSS"
category: "Frontend"
title: "break-inside - Layout - Tailwind CSS"
doc_order: 20
source_url: "https://tailwindcss.com/docs/break-inside"
language: "en"
retrieved_at: "2026-11-03 17:59:37"
content_hash: "00d63046325beae1ee802770d72402fdaba6d0542dfd544f269aed976aef31ab"
---

# break-inside - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/break-inside

---

Layout

Utilities for controlling how a column or page should break within an element.

| Class | Styles | 
|---|---|
| `break-inside-auto` | `break-inside: auto;` | 
| `break-inside-avoid` | `break-inside: avoid;` | 
| `break-inside-avoid-page` | `break-inside: avoid-page;` | 
| `break-inside-avoid-column` | `break-inside: avoid-column;` | 

Use utilities like `break-inside-column` and `break-inside-avoid-page` to control how a column or page break should behave within an element:

`<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-inside-avoid-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>`
Prefix a `break-inside` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<div class="break-inside-avoid-column md:break-inside-auto ...">  <!-- ... --></div>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).