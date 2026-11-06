---
id: "javascript_043"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 43
source_url: "https://developer.mozilla.org/en-US/blog/html-details-exclusive-accordions"
language: "en"
retrieved_at: "2026-11-01 21:52:36"
content_hash: "98ade28b1be171d7091c513fbc2f095d8aef85f7722bd2eb153825c556c5ecda"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/html-details-exclusive-accordions

---

# Exclusive accordions using the HTML details element

The [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details#name) attribute of the [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) element is soon to be supported across all major browsers.
Firefox 130 should also have support, enabling most engines to handle common UI accordion patterns using only `<details>` elements.
This is good news for developers who have been writing custom handling for these cases from scratch.
Let's explore what the attribute allows you to do with some quick examples.

**Note:**
This feature's stable in [Chrome 120](https://chromestatus.com/feature/6710427028815872), [Safari 17.2](https://developer.apple.com/documentation/safari-release-notes/safari-17_2-release-notes#HTML) and is enabled in [Firefox Nightly](https://bugzilla.mozilla.org/show_bug.cgi?id=1856460), so you can already start trying it out.

**Update (April 2025):** This feature is enabled by default in stable releases since [Firefox 130](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/130).

## [How does `<details>` work?](https://developer.mozilla.org#how_does_details_work)

If you're unfamiliar with `<details>`, it's an element that creates a 'disclosure widget' in which information is visible only when the widget is toggled to an "open" state.
You should include in it a [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary) element, which is used for the text describing the disclosure.
If you omit the `<summary>`, a browser-specific string like "Details" will be used by default.
Click the two elements below to toggle them between open and closed states and notice the missing `<summary>` in the first one:

```
<details>
  <p>
    The response phrase for 413 "Content Too Large" used to be "Payload Too
    Large", and this message is still widely used.
  </p>
</details>
<details>
  <summary>System configuration</summary>
  <ul>
    <li>200GB RAM</li>
    <li>4PB storage</li>
  </ul>
</details>
```
Since an accordion is a series of expandable sections that allow users to show or hide content, a series of `<details>` elements can be used to create an accordion-like interface.
With the use of the `name` attribute, as we'll see later, these elements can closely mimic the behavior of common accordions, in which only one section can be open at a time, with other sections automatically closing when a new one is expanded.

There's great potential for `<details>` elements to fit into your pages because some minimal styling can go a long way to create interactive accordions using only HTML and CSS.

```
<details>
  <summary>System configuration</summary>
  <ul>
    <li>200GB RAM</li>
    <li>4PB storage</li>
  </ul>
</details>
<details>
  <summary>Recommended settings</summary>
  <ul>
    <li>Extreme mode: on</li>
    <li>Raytracing: enabled</li>
  </ul>
</details>
<details>
  <summary>Other details</summary>
  <ul>
    <li>Material: Faux Leather, Metal</li>
    <li>Item Weight: 10.2Kg</li>
  </ul>
</details>
```
## [Using `<details name>` to create exclusive accordions](https://developer.mozilla.org#using_details_name_to_create_exclusive_accordions)

A common use case for accordions is that only one of them should be open at any one time.
The addition of the `name` attribute lets you connect multiple `<details>` elements and make an accordion exclusive, so only one `<details>` element with the same name can be open at any time, and the browser toggles all others with the same name to a "closed" state.
It's quite nice to be able to include this when you want to group multiple `<details>` elements and ensure exclusivity:

```
<details name="tech-specs">
  <summary>System configuration</summary>
  <ul>
    <li>200GB RAM</li>
    <li>4PB storage</li>
  </ul>
</details>
<details name="tech-specs">
  <summary>Recommended settings</summary>
  <ul>
    <li>Extreme mode: on</li>
    <li>Raytracing: enabled</li>
  </ul>
</details>
<details name="tech-specs">
  <summary>Other details</summary>
  <ul>
    <li>Material: Faux Leather, Metal</li>
    <li>Item Weight: 10.2Kg</li>
  </ul>
</details>
```
An FAQ is a good use case for these types of exclusive accordions where the visitor can focus on one topic at a time:

```
<details name="faq">
  <summary>Can I request a refund?</summary>
  <p>
    Yes, you have up to 30 days to request a refund. See our T&C for details.
  </p>
</details>
<!-- etc. -->
```
## [Further reading](https://developer.mozilla.org#further_reading)

If you want to learn more, you can have a read through these other resources:

- [Exclusive Accordion (Explainer)](https://open-ui.org/components/accordion.explainer/) by [@dbaron](https://github.com/dbaron) (2023)
- [Exclusive Accordion](https://developer.chrome.com/docs/css-ui/exclusive-accordion) by [Bramus](https://www.bram.us/) on developer.chrome.com (2023)
- [New to the web platform in December](https://web.dev/blog/web-platform-12-2023) on web.dev (2023)

## [Summary](https://developer.mozilla.org#summary)

With more support landing for this feature in more stable browsers, it's a good indicator that the web platform is providing better functionality for features that web developers have had to write themselves.
If you're looking for a polyfill, there's a great [post by Bramus](https://developer.chrome.com/docs/css-ui/exclusive-accordion#polyfill_the_exclusive_accordion), which includes a polyfill for browsers that don't support this yet.

I hope you enjoyed this post and you'll get more mileage out of the `<details>` element, which is a flexible and useful element for a lot of cases.
Feel free to [get in touch with us](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels) and let me know what you think or if I've missed something.
Don't get too lost in the `<details>` and have fun!