---
id: "tailwindcss_016"
technology: "TailwindCSS"
category: "Frontend"
title: "aspect-ratio - Layout - Tailwind CSS"
doc_order: 16
source_url: "https://tailwindcss.com/docs/aspect-ratio"
language: "en"
retrieved_at: "2026-11-03 17:59:35"
content_hash: "357ebd89e7ad11c0fb89e38d94e853f88406f9be5a2fe287d261505066c74b8c"
---

# aspect-ratio - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/aspect-ratio

---

Layout

Utilities for controlling the aspect ratio of an element.

| Class | Styles | 
|---|---|
| `aspect-``<ratio>` | `aspect-ratio:` `<ratio>`; | 
| `aspect-square` | `aspect-ratio: 1 / 1;` | 
| `aspect-video` | `aspect-ratio: var(--aspect-video); /* 16 / 9 */` | 
| `aspect-auto` | `aspect-ratio: auto;` | 
| `aspect-(``<custom-property>`) | `aspect-ratio: var(``<custom-property>`); | 
| `aspect-[``<value>`] | `aspect-ratio:` `<value>`; | 

Use `aspect-` utilities like `<ratio>``aspect-3/2` to give an element a specific aspect ratio:

Resize the example to see the expected behavior

Use the `aspect-video` utility to give a video element a 16 / 9 aspect ratio:

Use the `aspect-[` syntax to set the aspect ratio based on a completely custom value:`<value>`\]

`<img class="aspect-[calc(4*3+1)/3] ..." src="/img/villas.jpg" />`
For CSS variables, you can also use the `aspect-(` syntax:`<custom-property>`)

`<img class="aspect-(--my-aspect-ratio) ..." src="/img/villas.jpg" />`
This is just a shorthand for `aspect-[var(` that adds the `<custom-property>`)\]`var()` function for you automatically.

Prefix an `aspect-ratio` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<iframe class="aspect-video md:aspect-square ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

Use the `--aspect-*` theme variables to customize the aspect ratio utilities in your project:

`@theme {  --aspect-retro: 4 / 3; }`
Now the `aspect-retro` utility can be used in your markup:

`<iframe class="aspect-retro" src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>`
Learn more about customizing your theme in the [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme).