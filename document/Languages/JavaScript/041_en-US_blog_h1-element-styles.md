---
id: "javascript_041"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 41
source_url: "https://developer.mozilla.org/en-US/blog/h1-element-styles"
language: "en"
retrieved_at: "2026-11-01 21:52:33"
content_hash: "48ca081a48aae656b13f4a9f9ee69f602e877819c7f97f75c8559ca741ac1b95"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/h1-element-styles

---

# Default styles for h1 elements are changing

Browsers are starting to roll out changes in default UA styles for nested section headings. Developers should check that their sites don't rely on UA styles for certain cases to avoid unexpected results and failing Lighthouse checks. In this post, we'll have a look at what the incoming changes are, how to identify if it's an issue on your pages, and some hints for conformant and better-structured websites.

## [What's changing](https://developer.mozilla.org#whats_changing)

The HTML spec used to define an outline algorithm that gave [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements) elements an implicit semantic heading level based on how many sectioning elements ([`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section), [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside), [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav), and [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)) it was nested inside.

The browser rendering was such that `section > h1` would have the same font-size and margin as `<h2>`. The `section > section > h1` would be represented as `<h3>`, and so on. The default rendering was implemented in browsers in their UA styles, but not the heading level in the [accessibility tree](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree) (what screen readers use). Websites started to use sectioning elements, but didn't expect to see the automatic heading levels from the outline algorithm.

In general, this created confusion about where developers could use `<h1>` elements, tools handled the HTML differently, and the outline algorithm was considered problematic. The outline algorithm was [removed from the HTML spec in 2022](https://github.com/whatwg/html/pull/7829), but the UA stylesheet rules still remain. The rules in the default styles are what browser vendors are starting to remove now.

```
/* where x is :is(article, aside, nav, section) */
x h1 { margin-block: 0.83em; font-size: 1.50em; }
x x h1 { margin-block: 1.00em; font-size: 1.17em; }
x x x h1 { margin-block: 1.33em; font-size: 1.00em; }
x x x x h1 { margin-block: 1.67em; font-size: 0.83em; }
x x x x x h1 { margin-block: 2.33em; font-size: 0.67em; }
```
For example:

```
<body>
  <h1>Level 1</h1>
  <section>
    <h1>Level 2</h1>
    <section>
      <h1>Level 3</h1>
      <section>
        <h1>Level 4</h1>
      </section>
    </section>
  </section>
</body>
```
This looks as follows in the old UA styles:

The new UA styles will have this appearance:

And here's the HTML example above with your browser's default styles:

## [What to expect and when](https://developer.mozilla.org#what_to_expect_and_when)

Alongside the changes in browser styles, page auditing tools like Lighthouse now flag cases of `<h1>`s without defined [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size) as bad practice. Here's the gist of what to expect:

- `<h1>` will no longer adapt its style based on surrounding sectioning elements like `<section>`, `<article>`, `<nav>`, and `<aside>`. UA stylesheet will apply the same style to `<h1>` with no implicit styles that demote `<h1>` to match `<h2>`, `<h3>`, etc.
- Lighthouse will flag a warning if `<h1>` is used without a specified font-size and is nested in `<section>`, `<article>`, `<nav>`, or `<aside>`. The Lighthouse deprecation warning to look out for is `H1UserAgentFontSizeInSection`. Hints for dealing with this are described in the next section.

In terms of when this is happening, changes are rolling out in the following browsers in this timeline:

### [Firefox](https://developer.mozilla.org#firefox)

- From March 31, 2025, Firefox is rolling out changes to 50% of [Beta 138](https://www.mozilla.org/en-US/firefox/channel/desktop/#beta) users to remove UA styles for `h1` in `article`, `aside`, `nav`, or `section` on desktop, then 100% of Beta 138 starting April 14. The plan is to roll out to 5% of users on the Firefox 138 stable release, ramp up to 10% of users, then ship on all platforms in Firefox 140. [bug 1885509](https://bugzilla.mozilla.org/show_bug.cgi?id=1885509).
- Since Firefox 136, developers will see a console warning for `h1`s in `article`/`aside`/`nav`/`section` without author-defined font-size or margins: [bug 1937568](https://bugzilla.mozilla.org/show_bug.cgi?id=1937568).
- To test in Firefox with the new behavior, set `layout.css.h1-in-section-ua-styles.enabled` to false in about:config.

### [Chrome](https://developer.mozilla.org#chrome)

- Since version 136, Chrome shows deprecation warnings for `<h1>` inside the 4 elements, when the `<h1>` uses the default smaller font size. Marking something deprecated in Chromium **will lower Lighthouse scores** for "Best Practices": [issue 394111284](https://issues.chromium.org/issues/394111284)

### [Safari](https://developer.mozilla.org#safari)

- The implementation bug to track for Safari is [bug 292765](https://bugs.webkit.org/show_bug.cgi?id=292765).

## [Fixing the Lighthouse warning](https://developer.mozilla.org#fixing_the_lighthouse_warning)

Lighthouse has recently [inherited a check](https://github.com/GoogleChrome/lighthouse/issues/16404) based on Chromium's DevTools warnings for sites that don't specify a `font-size` for `<h1>` elements in `<section>`, `<article>`, `<nav>`, or `<aside>`. The new rule is called `H1UserAgentFontSizeInSection` and shows up since March following the addition of deprecation warnings. If you see the `<h1>` warning, make sure you're applying an explicit `<h1>` font-size and margins. Here's some recommended styles to use:

```
h1 {
  margin-block: 0.67em;
  font-size: 2em;
}
```
To avoid overwriting other style rules that target `<h1>` you can use [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where), which has zero [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity):

```
:where(h1) {
  margin-block: 0.67em;
  font-size: 2em;
}
```
The MDN page for heading elements now contains [the usage notes listed above](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#specifying_a_uniform_font_size_for_h1) so there is a visible place for developers to see this information.

## [Summary](https://developer.mozilla.org#summary)

Here's some things to keep in mind:

- **Do not** rely on default browser styles for conveying a heading hierarchy. Explicitly define your document hierarchy using `<h2>` for second-level headings, `<h3>` for third-level, etc.
- Always define your own `font-size` and `margin` for `<h1>` elements.
- Consider updating your CSS resets to account for the change.
- Audit your site [using Lighthouse](https://pagespeed.web.dev/) and browser [DevTools](https://firefox-dev.tools/) to check for deprecated usage.
- Check the [usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#specifying_a_uniform_font_size_for_h1) on the MDN documentation for HTML section headings.