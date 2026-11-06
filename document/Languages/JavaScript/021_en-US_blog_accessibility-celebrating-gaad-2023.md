---
id: "javascript_021"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 21
source_url: "https://developer.mozilla.org/en-US/blog/accessibility-celebrating-gaad-2023"
language: "en"
retrieved_at: "2026-11-01 21:51:48"
content_hash: "ea3b8f03cb5aad3766dfb81dc074da4b68e56eb0719571c4e97859bf7594eee6"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/accessibility-celebrating-gaad-2023

---

# Celebrating Global Accessibility Awareness Day

The internet is a global community, and accessibility is about making sure that everyone can take part in it. To celebrate [Global Accessibility Awareness Day](https://accessibility.day/) (GAAD), we're sharing some tips to help you make your website more accessible for everyone.

## [Check the Web Content Accessibility Guidelines (WCAG)](https://developer.mozilla.org#check_the_web_content_accessibility_guidelines_wcag)

The standard success criterion and guidelines for ensuring your content is accessible on the web are the [web content accessibility guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/). While it can be daunting to understand and know how to implement all of these guidelines, there is help. The following are three ways to access, read and understand these guidelines.

Now that you know the source of truth, let's dig into some supporting documents and tools.

## [Check the Accessibility Concerns section on MDN Web Docs](https://developer.mozilla.org#check_the_accessibility_concerns_section_on_mdn_web_docs)

Several pages on MDN Web Docs contain a section that describes the accessibility concerns related to the topic you are reading. When you come across these sections, it is always valuable to take a moment to read, understand, and take action if needed. Let us look at a couple of examples.

On the reference page for the HTML [`multiple` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#accessibility_concerns), the accessibility concerns section highlights some critical details to keep in mind when using the attribute so that it is clear to screen reader users what to expect.

The [`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex) attribute is often misunderstood and misused. Incorrect use of the attribute can break user expectations or even the entire experience for those using a keyboard to navigate a page or a form. In addition, if interactive elements are authored using non-interactive elements, they will be hidden from the accessibility tree. It is, therefore, critical to [read the `tabindex` attribute accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#accessibility_concerns) section on the attribute page.

As mentioned in an earlier blog post on [landmark roles](https://developer.mozilla.org/en-US/blog/aria-accessibility-html-landmark-roles/), if HTML already has an element or attribute that satisfies your need, use it over manipulating inappropriate elements using ARIA roles.

The CSS [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity#accessibility_concerns) property is another one that needs to be used with care, especially when there are text elements involved. Many more of these are found across the MDN Web Docs website. Be sure to read these and [ask for help on Discord](https://developer.mozilla.org/discord) if anything is unclear. Also, the [Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) module on MDN Web Docs is a great way to familiarize yourself with the topic further.

## [Check the color contrast of your web pages](https://developer.mozilla.org#check_the_color_contrast_of_your_web_pages)

Low contrast is still one of the biggest problems on web pages, as can be read in the [latest WebAIM million report](https://webaim.org/projects/million/#contrast). This is the [fifth yearly report by WebAIM](https://webaim.org/projects/million/#intro), where they conduct an accessibility evaluation of the home pages of the top one million websites in the world. Things have gotten a little better since 2022, but not by much. So, how can you help to improve these statistics?

There are a number of options. From the start, it is critical to ensure that everyone on the team is aware of the Web Content Accessibility Guidelines (WCAG), specifically [success criterion 1.4.3](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html). There is also a page on MDN Web Docs that covers [color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast) in greater detail.

If your designers use Figma to design your website's pages, components, and layouts, they should install and use the [color contrast plugin](https://www.figma.com/community/plugin/937465522075454889/Color-contrast). Doing this will get you off to a great start and save a lot of time during future phases of the project. If the design tool does not have a plugin or native support for testing color contrast, the open-source [color contrast analyzer (CCA) tool](https://github.com/ThePacielloGroup/CCAe) by the Paciello group is a great tool that can be used with any application on both Windows and macOS.

When you are testing a website in the browser, you have even more options:

- Using the [color picker in a Chromium-based](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/accessibility/color-picker) browser.
- Using the [accessibility inspector](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/index.html) and color picker in Firefox.

When there is no built-in support for testing color contrast, using the CCA tool mentioned earlier is your go-to.

### [Watch a color contrast audit on YouTube](https://developer.mozilla.org#watch_a_color_contrast_audit_on_youtube)

If you want to learn more, watch [a video demonstrating these color contrast tools on YouTube](https://youtu.be/3CmxVjC384Y).

## [Go beyond color contrast with accessibility auditing tools](https://developer.mozilla.org#go_beyond_color_contrast_with_accessibility_auditing_tools)

There is a lot more to web accessibility than color contrast. Topics such as adding alternative text for images that are not purely decorative. Ensuring that your pages are accessible by users who use only a keyboard. When using ARIA attributes, it is critical that they are [used correctly](https://www.deque.com/blog/wai-aria-top-6-mistakes-to-avoid/). If they are not, they can do more harm than good. There is even more you can do to ensure accessibility, depending on your website's or web application's complexity.
Thankfully, some automated tools can help us identify and fix common issues that automation can detect.

The first of these is [Lighthouse](https://github.com/GoogleChrome/lighthouse) from the Google Chrome team. Lighthouse can be used in many different ways, such as from the [command line](https://github.com/GoogleChrome/lighthouse#using-the-node-cli), in [Nodejs](https://github.com/GoogleChrome/lighthouse#using-the-node-module), as part of a [continuous integration pipeline](https://github.com/GoogleChrome/lighthouse-ci), or [in your browser](https://github.com/GoogleChrome/lighthouse#using-lighthouse-in-chrome-devtools) (specifically Chromium-based browsers). A standard run of Lighthouse will test a lot more than just accessibility, but you are able to disable the other tests.

**Note:** It is important to know that while automation tools are helpful, testing with a screen reader or engaging with real users is the only way to truly ensure the experience is inclusive for everyone who wants to use your site or app.


By default, Lighthouse will have all of its audits enabled:

To run only the accessibility audit, be sure to uncheck all the other categories:

There are also browser extensions that can be used in addition to Lighthouse or to fill the gap in those browsers where Lighthouse is not a standard developer feature. One of the most widely used is [Axe from Deque Labs](https://www.deque.com/axe/). Some other popular tools are [WAVE](https://wave.webaim.org/) from WebAIM, and other vision simulators, such as the [NoCoffee browser extension](https://github.com/eeejay/NoCoffee), the built-in [vision simulator in Firefox](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/simulation/index.html), and the [auditing tools in Safari](https://developer.apple.com/videos/play/wwdc2019/514/).

### [Watch the automation tools demo on Youtube](https://developer.mozilla.org#watch_the_automation_tools_demo_on_youtube)

If you want to learn more, watch [a video demonstrating the basics of these automation tools on YouTube](https://youtu.be/YxA_cxyMJ1E).

## [Strive for providing equal access for all](https://developer.mozilla.org#strive_for_providing_equal_access_for_all)

The web is a powerful tool for connecting people, but it is the responsibility of each of us building on the web to ensure that what we create does not exclude anyone. While some might argue that those experiencing challenges are a minority of their site or app users, we'd like you to consider the [curb-cut effect](https://ssir.org/articles/entry/the_curb_cut_effect). The short description of this effect is that affordances made for a particular group of people often end up benefiting society at large.

As its name suggests, the idea comes from the literal curb-cut one finds on most streets, especially in large cities. While originally [introduced post-World War II](https://www.carleton.edu/accessibility-resources/newsletter/curb-cuts-a-brief-history/) to accommodate veteran wheelchair users who found their city streets inaccessible after returning from war, it is now commonplace in many parts of the world. This also did not just happen but took several people speaking up and fighting for their [right to equal access](https://life.berkeley.edu/disability-rights-movement-highlights/).

Every time someone needs to get their heavily loaded dolly onto a curb, or a parent wants to cross the street with a stroller, or somebody wants to pull their heavy luggage at train stations or airports without lifting them onto a curb; they are experiencing the curb-cut effect.

So, not only is it the right thing to do, but your company can [avoid legal action](https://www.startribune.com/lawsuits-targeting-company-websites-for-ada-violations-on-the-rise-visual-hearing-accessible/600275196/), which is both expensive and destructive for a brand. In the end, the affordance you make and the resources you invest today could benefit a much wider portion of society tomorrow, maybe even yourself.

## [Summary](https://developer.mozilla.org#summary)

We're excited to celebrate Global Accessibility Awareness Day with you, and we hope you'll join us in this important work. We know it can be daunting to think about all the ways your site might not be accessible, but we also know that by taking small steps and using the tools and guidelines shared in this post, you are well on your way.