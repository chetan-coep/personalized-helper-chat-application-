---
id: "javascript_046"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 46
source_url: "https://developer.mozilla.org/en-US/blog/interop2023-mdn-doc-updates"
language: "en"
retrieved_at: "2026-11-01 21:52:41"
content_hash: "7fb63587ff1499e2e7b70586504c56238fd0a5ad36c660ae44596a616f38654c"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/interop2023-mdn-doc-updates

---

# Interop 2023: MDN updates

Interoperability on the web means ensuring that web platform features work in a spec-compliant way across as many devices and browsers as possible. With Interop 2024 having just kicked off, this post explains what the Interop project is, recaps what's landed on MDN based on Interop 2023, and offers a glimpse into what's coming next to the web platform.

## [What is the Interop project?](https://developer.mozilla.org#what_is_the_interop_project)

The [Interop project](https://github.com/web-platform-tests/interop#the-interop-project) is a benchmark and test suite that tracks the interoperability of web features across different browsers.
However, Interop is more than tests; it is a joint initiative among browser vendors to identify important features that would benefit from consistency across browsers and drive development toward them over a calendar year.

Over the last three years, developers have worked together to increase overall Interop benchmark scores.
Like previous years, the [Interop 2024](https://wpt.fyi/interop-2024) dashboard shows the features that browser vendors have agreed to work on collectively and the progress in web feature compatibility scores across different browsers.

The main goal of this initiative is to ensure developers can create seamless web experiences for everyone, regardless of their browser choice. When developers can build upon a consistent web platform, everyone who uses the web benefits from it in their daily online activities.

A key benefit of the web platform is that it's defined by standards, rather than by the code of a single implementation.
This creates a shared platform that isn't tied to specific hardware, a company, or a business model. - [Interop 2022 announcement, Mozilla Hacks](https://hacks.mozilla.org/2022/03/interop-2022/)


## [How does Interop work?](https://developer.mozilla.org#how_does_interop_work)

The Interop team chooses focus areas [based on user and web developer feedback](https://github.com/web-platform-tests/interop/blob/main/2024/selection-process.md) to identify features or groups of features that are particularly problematic due to poor or inconsistent browser support.
A suite of [headless browser tests](https://github.com/web-platform-tests/wpt?tab=readme-ov-file#the-web-platform-tests-project) asserts that browsers behave in a specification-compliant way for each focus area.

An accelerator behind the scenes is that browser vendors can ship [Web Platform Tests](https://web-platform-tests.org/) (WPT) alongside code changes, which [automated processes](https://github.com/web-platform-tests/wpt/pull/45101) can pick up, and tests can be efficiently downstreamed to the WPT project.
Shipping fixes and features with a tight feedback loop with Interop lets browser developers directly see the impact of their efforts on the web ecosystem, which is a significant motivating factor for driving the open web forward.

## [Interop 2023 outcomes](https://developer.mozilla.org#interop_2023_outcomes)

A lot of code changes landed in multiple browsers that were aimed at improving Interop scores.
As you can see in the screenshot below, the overall benchmark results present a nice picture of increased cross-browser compatibility.
To get insights into the project's progress, you can use this [interactive dashboard](https://wpt.fyi/interop-2023).

Some focus areas had a dramatic change over the course of the year.
For example, the features within [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables), which were lingering at a mere 4% in January 2023, surged to an 89.5% passing score by the end of the year:

CSS [Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid) is another great example that went from 12.5% to 90.8% passing overall score last year:

The benchmark results paint an exciting picture of success for the project goals that encourage conformance to web standards everywhere.

## [Interop 2023 updates on MDN](https://developer.mozilla.org#interop_2023_updates_on_mdn)

The role of the MDN team in Interop involves ensuring that there is reliable and up-to-date documentation for the features included in Interop, especially for those that have reached cross-browser support. This enables developers to confidently build for the web using functionalities that have recently become stable across major browser releases.

[Interop 2023](https://github.com/web-platform-tests/interop/tree/main/2023) was one of the team's documentation goals last year.
Our intention was to audit the MDN content corresponding to the focus areas in Interop 2023 and update the docs to keep them accurate and useful as the features and their support evolved.

A lot of features such as [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has) reached stable status across all major browser engines in 2023 and that meant we could remove a lot of experimental warnings and update code to use the latest syntax, where appropriate.

### [MDN highlights from Interop 2023](https://developer.mozilla.org#mdn_highlights_from_interop_2023)

2023 was a big year for CSS, and we saw a lot of improvements landing for CSS color support, which led to some great documentation improvements. Here's a few interesting picks from changes that landed from the team's focus on Interop:

- [docs(CSS): Add module landing page for CSS Properties and Values API](https://github.com/mdn/content/pull/30503)
- [docs(CSS): Add module landing page for overscroll behavior](https://github.com/mdn/content/pull/30981)
- [docs(CSS): Add module landing page for CSS transforms module](https://github.com/mdn/mdn/issues/488)
- [docs(HTML): Inert - notes about content not being perceivable](https://github.com/mdn/content/pull/25548)

If you want to see everything else that was covered in the Interop 2023 tasks and PRs, check the [MDN Interop 2023 tracking issue](https://github.com/mdn/mdn/issues/416) on GitHub which has links to 56 PRs and subtasks.
Aside from reference docs and guides, we've written a fair bit about Interop topics like CSS colors, border images, and container queries on the MDN blog:

### [2023 focus areas](https://developer.mozilla.org#2023_focus_areas)

Here's the focus areas from Interop 2023 with links to the MDN docs for each area. We hope all of the work in keeping these docs updated has made a difference in your experience reading through them and in your web development journey.

#### CSS

| Focus Area | Description | 
|---|---|
| [Border Image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image) | How an image can be used as the border of an element. | 
| [Color Spaces and Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value) | Different ways to specify color values and color spaces. | 
| [Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries) | Encapsulation based on parent container's size. | 
| [Containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment) | Isolating a subtree from the rest of the document. | 
| [CSS Math Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions) | Mathematical functions like `min()`, `sin()`. | 
| [CSS Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes) | State selectors for elements (e.g., `:hover`, `:focus`). | 
| [Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property) | Custom CSS variables for reusable values. | 
| [Flexbox](https://developer.mozilla.org/docs/Learn_web_development/Core/CSS_layout/Flexbox) | A layout for arranging elements in a one-dimensional flow. | 
| [Font Feature Detection and Palettes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette) | Advanced typographic features. | 
| [Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout) | A grid-based layout system. | 
| [:has()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has) | Select elements based on its descendants. | 
| [Masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking) | How to partially or fully hide elements using masking layers. | 
| [Media Queries 4](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using) | Apply styles based on device characteristics. | 
| [Motion Path](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Motion_path) | Position elements along paths for animations. | 
| [Scrolling](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior) | Control scrolling in web documents. | 
| [Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid) | Extend CSS Grid to allow grid items to relate to an ancestor's grid. | 
| [Transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform) | Perform 2D and 3D transformations to elements. | 

#### HTML

| Focus Area | Description | 
|---|---|
| [Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form) | Using forms for collecting user input. | 
| [Inert](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert) | Make elements non-interactive and invisible to assistive technologies. | 

#### APIs

| Focus Area | Description | 
|---|---|
| [Modules in Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) | Use Web Workers to run scripts in background threads. | 
| [Offscreen Canvas](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas) | Rendering graphics via scripts without updating the main page. | 
| [Pointer and Mouse Events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) | Handling input from mouse and touch interfaces. | 
| [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) | The API for creating and managing URLs. | 
| [Web Codecs (video)](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) | Codecs for encoding and decoding audio and video. | 

#### Other

- [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components): A collection of technologies allowing to create reusable custom elements.

## [Summary](https://developer.mozilla.org#summary)

We're excited to see what's landing on the web platform in 2024, and we're going to be keenly watching Interop to see what the next movers and shakers are. We see Interop as one of the most important and exciting initiatives that motivates browser vendors to build a compliant and open web.

We hope you enjoyed this post!
Feel free to [get in touch with us](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels) and let us know what you think.
If you want to find out more about Interop, here's a list of resources to announcements and project pages:

- [Announcing Interop 2024](https://hacks.mozilla.org/2024/02/announcing-interop-2024/) on hacks.mozilla.org
- [Interop 2024](https://web.dev/blog/interop-2024) on web.dev
- [The web just gets better with Interop 2024](https://webkit.org/blog/14955/the-web-just-gets-better-with-interop/) on webkit.org
- [WPT](https://web-platform-tests.org/) homepage
- [Interop 2024 project page](https://wpt.fyi/interop-2024) on wpt.fyi