---
id: "javascript_026"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 26
source_url: "https://developer.mozilla.org/en-US/blog/baseline-unified-view-stable-web-features"
language: "en"
retrieved_at: "2026-11-01 21:51:57"
content_hash: "6b293bec2f2d6dcbaeef3ddd3e88811dede576d494c4c7cd6cc6398450a04eca"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/baseline-unified-view-stable-web-features

---

# Introducing Baseline: a unified view of stable web features

**Note:** We updated the Baseline widgets and rolled it out for more pages to align with the refined Baseline definition. The Baseline definition described in this post is outdated. Read more in the [Baseline's evolution on MDN](https://developer.mozilla.org/en-US/blog/baseline-evolution-on-mdn/) post.


MDN is committed to providing modern web development documentation to over a million developers daily. Due to the rapidly-evolving nature of the web platform, and the tremendous innovation happening in the browser space, developers have a hard time keeping up with the constantly evolving landscape and they lack a common language to talk about the features that are generally available for use on the web. To address these issues, Mozilla has engaged in a two-fold approach.

First, we have actively participated in the [WebDX Community Group](https://www.w3.org/community/webdx/), collaborating with organizations like Google, Apple, W3C and others to develop the Web Platform Feature Set: a common language to describe platform features.

Second, through MDN, Mozilla is now the first to use this dataset to offer a transparent, unified view of stable, well-supported features and display the [Baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) support for the web platform.

## [Background and motivation](https://developer.mozilla.org#background_and_motivation)

In 2019 and 2020, Mozilla and the [MDN Product Advisory Board](https://developer.mozilla.org/en-US/about#our_partners) developed and conducted the [Web Developer Needs Assessment (DNA)](https://insights.developer.mozilla.org/), a large-scale study of developer needs.
One key pain point for developers is inconsistent browser support for platform features.
Through Mozilla's involvement in the WebDX Community Group and MDN's implementation of the Web Feature set, we aim to build a shared understanding and description of the web platform's existing interoperable surface.
By doing so, we hope to provide supporting infrastructure for a more seamless developer experience, reduce the pain points associated with browser incompatibilities, and foster a more collaborative and cohesive web development community.

Our aim is to help simplify and streamline the information presented to developers, enabling them to quickly identify what they can utilize now and what will soon be available.
**Starting today, MDN is introducing Baseline labeling on our site and we plan to cover all relevant features in the coming months.**

## [The Web Platform Baseline](https://developer.mozilla.org#the_web_platform_baseline)

The Web Platform Baseline consists of features natively supported in the core browser set for at least two major versions. We believe this measure of support will be considered the stable foundation of the web platform for most developers. By identifying and agreeing on a core browser set, the project aims to provide clear guidance for developers. They can now check on MDN whether a feature is "Baseline" and be confident that the feature is ready for use.

## [Core browser set](https://developer.mozilla.org#core_browser_set)

The core browser set, which most developers need to support in the absence of specific constraints, should reflect usage numbers, developer expectations, and existing ecosystem support. The core browser set includes the two most recent major versions of Firefox, Chrome, Edge and Safari. As developer expectations and user numbers evolve, the core browser set will be updated accordingly to represent the current state. This dynamic approach ensures that the core browser set remains relevant to the ever-changing landscape of web development.

## [Ongoing maintenance of the web feature set](https://developer.mozilla.org#ongoing_maintenance_of_the_web_feature_set)

We're committed to maintaining the classification of features in the Web Feature Set and updating it as platform features become available and browser versions are released.
This ongoing maintenance will happen in the [Feature Set repository](https://github.com/web-platform-dx/feature-set) of the [WebDX Community Group GitHub organization](https://github.com/web-platform-dx/).
To ensure that the Web Feature Set remains current and baseline remains accurate, we encourage developers to [provide feedback](https://github.com/web-platform-dx/feature-set/issues) and contribute to the feature set repo.