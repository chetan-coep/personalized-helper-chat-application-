---
id: "tailwindcss_017"
technology: "TailwindCSS"
category: "Frontend"
title: "columns - Layout - Tailwind CSS"
doc_order: 17
source_url: "https://tailwindcss.com/docs/columns"
language: "en"
retrieved_at: "2026-11-03 17:59:35"
content_hash: "30752c6c42715c1db981601fb4bf02e93c81f9d7ae570aff666d9f518cee4262"
---

# columns - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/columns

---

Layout

Utilities for controlling the number of columns within an element.

| Class | Styles | 
|---|---|
| `columns-``<number>` | `columns:` `<number>`; | 
| `columns-3xs` | `columns: var(--container-3xs); /* 16rem (256px) */` | 
| `columns-2xs` | `columns: var(--container-2xs); /* 18rem (288px) */` | 
| `columns-xs` | `columns: var(--container-xs); /* 20rem (320px) */` | 
| `columns-sm` | `columns: var(--container-sm); /* 24rem (384px) */` | 
| `columns-md` | `columns: var(--container-md); /* 28rem (448px) */` | 
| `columns-lg` | `columns: var(--container-lg); /* 32rem (512px) */` | 
| `columns-xl` | `columns: var(--container-xl); /* 36rem (576px) */` | 
| `columns-2xl` | `columns: var(--container-2xl); /* 42rem (672px) */` | 
| `columns-3xl` | `columns: var(--container-3xl); /* 48rem (768px) */` | 
| `columns-4xl` | `columns: var(--container-4xl); /* 56rem (896px) */` | 
| `columns-5xl` | `columns: var(--container-5xl); /* 64rem (1024px) */` | 
| `columns-6xl` | `columns: var(--container-6xl); /* 72rem (1152px) */` | 
| `columns-7xl` | `columns: var(--container-7xl); /* 80rem (1280px) */` | 
| `columns-auto` | `columns: auto;` | 
| `columns-(``<custom-property>`) | `columns: var(``<custom-property>`); | 
| `columns-[``<value>`] | `columns:` `<value>`; | 

Use `columns-` utilities like `<number>``columns-3` to set the number of columns that should be created for the content within an element:

The column width will automatically adjust to accommodate the specified number of columns.

Use utilities like `columns-xs` and `columns-sm` to set the ideal column width for the content within an element:

Resize the example to see the expected behavior

When setting the column width, the number of columns automatically adjusts to ensure they don't get too narrow.

Use the `gap-` utilities to specify the width between columns:`<width>`

Learn more about the gap utilities in the [gap documentation](https://tailwindcss.com/docs/gap).

Use the `columns-[` syntax to set the columns based on a completely custom value:`<value>`\]

`<div class="columns-[30vw] ...">  <!-- ... --></div>`
For CSS variables, you can also use the `columns-(` syntax:`<custom-property>`)

`<div class="columns-(--my-columns) ...">  <!-- ... --></div>`
This is just a shorthand for `columns-[var(` that adds the `<custom-property>`)\]`var()` function for you automatically.

Prefix a `columns` utility with a breakpoint variant like `sm:` to only apply the utility at small screen sizes and above:

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

Use the `--container-*` theme variables to customize the fixed-width column utilities in your project:

`@theme {  --container-4xs: 14rem; }`
Now the `columns-4xs` utility can be used in your markup:

`<div class="columns-4xs">  <!-- ... --></div>`
Learn more about customizing your theme in the [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme).