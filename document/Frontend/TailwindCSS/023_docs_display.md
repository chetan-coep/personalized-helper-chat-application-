---
id: "tailwindcss_023"
technology: "TailwindCSS"
category: "Frontend"
title: "display - Layout - Tailwind CSS"
doc_order: 23
source_url: "https://tailwindcss.com/docs/display"
language: "en"
retrieved_at: "2026-11-03 17:59:39"
content_hash: "e915a8411a5883e119ef8fea8d5f0de3e4ea0a37fc98e0f0ac4f30c23b2baa80"
---

# display - Layout - Tailwind CSS

Source: https://tailwindcss.com/docs/display

---

Layout

Utilities for controlling the display box type of an element.

| Class | Styles | 
|---|---|
| `inline` | `display: inline;` | 
| `block` | `display: block;` | 
| `inline-block` | `display: inline-block;` | 
| `flow-root` | `display: flow-root;` | 
| `flex` | `display: flex;` | 
| `inline-flex` | `display: inline-flex;` | 
| `grid` | `display: grid;` | 
| `inline-grid` | `display: inline-grid;` | 
| `contents` | `display: contents;` | 
| `table` | `display: table;` | 
| `inline-table` | `display: inline-table;` | 
| `table-caption` | `display: table-caption;` | 
| `table-cell` | `display: table-cell;` | 
| `table-column` | `display: table-column;` | 
| `table-column-group` | `display: table-column-group;` | 
| `table-footer-group` | `display: table-footer-group;` | 
| `table-header-group` | `display: table-header-group;` | 
| `table-row-group` | `display: table-row-group;` | 
| `table-row` | `display: table-row;` | 
| `list-item` | `display: list-item;` | 
| `hidden` | `display: none;` | 
| `sr-only` | ``` position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border-width: 0; ```  | 
| `not-sr-only` | ``` position: static; width: auto; height: auto; padding: 0; margin: 0; overflow: visible; clip-path: none; white-space: normal; ```  | 

Use the `inline`, `inline-block`, and `block` utilities to control the flow of text and elements:

Use the `flow-root` utility to create a block-level element with its own [block formatting context](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Block_formatting_context):

Use the `flex` utility to create a block-level flex container:

Use the `inline-flex` utility to create an inline flex container that flows with text:

Use the `grid` utility to create a grid container:

Use the `inline-grid` utility to create an inline grid container:

Use the `contents` utility to create a "phantom" container whose children act like direct children of the parent:

Use the `table`, `table-row`, `table-cell`, `table-caption`, `table-column`, `table-column-group`, `table-header-group`, `table-row-group`, and `table-footer-group` utilities to create elements that behave like their respective table elements:

Use the `hidden` utility to remove an element from the document:

To visually hide an element but keep it in the document, use the [visibility](https://tailwindcss.com/docs/visibility#making-elements-invisible) property instead.

Use `sr-only` to hide an element visually without hiding it from screen readers:

`<a href="#">  <svg><!-- ... --></svg>  <span class="sr-only">Settings</span></a>`
Use `not-sr-only` to undo `sr-only`, making an element visible to sighted users as well as screen readers:

`<a href="#">  <svg><!-- ... --></svg>  <span class="sr-only sm:not-sr-only">Settings</span></a>`
This can be useful when you want to visually hide something on small screens but show it on larger screens for example.

Prefix a `display` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

`<div class="flex md:inline-flex ...">  <!-- ... --></div>`
Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).