---
id: "javascript_025"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 25
source_url: "https://developer.mozilla.org/en-US/blog/baseline-evolution-on-mdn"
language: "en"
retrieved_at: "2026-11-01 21:51:55"
content_hash: "89a68511f18a47fc1e40a9c6a8ec29cf0967eb9c86ee5f5949787f3a42340b11"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/baseline-evolution-on-mdn

---

# Baseline's evolution on MDN

**Today we're updating the Baseline widget and rolling it out for more pages to align with the refined Baseline definition and help developers understand the status of web platform features better.**

First introduced [in May 2023](https://developer.mozilla.org/en-US/blog/baseline-unified-view-stable-web-features/), Baseline offered a new way of looking at the state of the web platform. It established a common measure for new features coming to the web and existing ones. The idea was simple: if a feature is available in the last two versions of major browsers, it's considered widely supported and safe to use. It becomes a part of Baseline.

Based on the data of the [Web Features](https://github.com/web-platform-dx/web-features) project maintained by the [WebDX Community Group](https://www.w3.org/community/webdx/), we implemented the initial Baseline definition by labeling several widely supported features, such as [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid) and [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image), as well as the not widely supported [`isContextLost`](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/isContextLost), with a widget right at the top of MDN reference pages. Before reading the page, you can tell if the feature can be reliably used.

## [Updated widget](https://developer.mozilla.org#updated_widget)

In addition to the existing "Limited availability" and "Widely available" widgets, which have been slightly adjusted, a new one sits in the middle of the Baseline timeline. The "Newly available" widget marks features that have recently become available in all stable versions of core browsers, for example, [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer).

By opening the widget, you'll now see additional information about the feature and the date when it became newly available. Today, we're expanding the Baseline widget coverage to 315 pages. We will continue to roll it out with the development of the [Web Features](https://github.com/web-platform-dx/web-features) dataset.

## [Refined definition](https://developer.mozilla.org#refined_definition)

Updated widgets follow the Baseline definition refined by the Web Features governance team.

First of all, the core browsers list is now expanded to include mobile versions of browsers. Sometimes, features get shipped on one platform, and the other follows only after some time. The core browser set now includes:

- Apple Safari (macOS and iOS)
- Mozilla Firefox (desktop and Android)
- Google Chrome (desktop and Android)
- Microsoft Edge (desktop)

There are two main events on the Baseline timeline for a feature:

1. **Newly available.** The feature is marked as interoperable from the day the last core browser implements it. It marks the moment when developers can start getting excited and learning about a feature.
2. **Widely available.** The feature is marked as having wider support thirty months or 2.5 years later. It marks the moment when it's safe to start using a feature without explicit cross-browser compatibility knowledge.

## [Feature example](https://developer.mozilla.org#feature_example)

To understand the Baseline better, let's look at the timeline of the CSS custom properties implementation in core browsers, listed in the order of its first appearance:

1. **Firefox 31:** July 22, 2014
2. **Chrome 49:** March 2, 2016
3. **Safari 9.1:** March 21, 2016
4. **Edge 15:** April 5, 2017

According to the Baseline definition, CSS custom properties became **"newly available"** on April 5, 2017, with the Edge 15 release, and therefore, became a part of "Baseline 2017". However, availability in all major browsers doesn't mean you can safely use a feature: it takes time for users to update their browsers or, in some cases, they have to update their operating system or even the device itself to get a new browser version. That's why, only thirty months later, on October 5, 2019, CSS custom properties were considered **"widely available"**.

The Web Features governance team may override the status of a feature in case of errors or misleading data. For example, they might hold a feature back until implementation bugs are resolved. The goal is not strict compliance with the definition but to reflect the practical reality of using these features.

**Note:** You can read the [detailed Baseline definition](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) in the MDN Glossary.


Like the web platform, the Baseline project has been made possible because of the effort of many parties. We at MDN collaborated closely with partners, including W3C's WebDX Community Group, Google, and Microsoft to bring the refined Baseline definition and widgets to MDN pages, based on community feedback. And we're not stopping here: if you have anything to say, please click the feedback icon in any expanded widget to let us know what you think.