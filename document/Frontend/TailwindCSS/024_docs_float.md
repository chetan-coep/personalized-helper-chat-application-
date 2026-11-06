---
id: "tailwindcss_024"
technology: "TailwindCSS"
category: "Frontend"
title: "float - Layout - Tailwind CSS"
doc_order: 24
source_url: "https://tailwindcss.com/docs/float"
language: "en"
retrieved_at: "2026-11-03 17:59:40"
content_hash: "989a4ac2ceb54479e4cecf47ece52782a72239549d14fcd3d2c199d507bf03e0"
---

# float - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/float

---

Layout

Utilities for controlling the wrapping of content around an element.

| Class | Styles | 
|---|---|
| `float-right` | `float: right;` | 
| `float-left` | `float: left;` | 
| `float-start` | `float: inline-start;` | 
| `float-end` | `float: inline-end;` | 
| `float-none` | `float: none;` | 

Use the `float-right` utility to float an element to the right of its container:

Use the `float-left` utility to float an element to the left of its container:

Use the `float-start` and `float-end` utilities, which use [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts) to map to either the left or right side based on the text direction:

Use the `float-none` utility to reset any floats that are applied to an element:

Prefix a `float` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<img class="float-right md:float-left" src="/img/mountains.jpg" />`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).