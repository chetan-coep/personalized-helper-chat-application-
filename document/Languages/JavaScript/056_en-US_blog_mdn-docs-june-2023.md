---
id: "javascript_056"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 56
source_url: "https://developer.mozilla.org/en-US/blog/mdn-docs-june-2023"
language: "en"
retrieved_at: "2026-11-01 21:53:10"
content_hash: "4f0123d57da6156d01f16e8e012b47f490a0fc2de2182b4a31428f27c263485f"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/mdn-docs-june-2023

---

# MDN doc updates: CSS selectors & media queries, WebGPU & WebTransport APIs, Progressive web apps

Hello, everyone! With the rapid enhancements in open web technologies across various browsers, the team at MDN, along with our partners at [Open Web Docs](https://openwebdocs.org/) and our contributors, has been diligently working to ensure that our documentation remains up to date for all of you.

We are excited to share that there have been several noteworthy updates to MDN docs. This post touches upon some of those significant additions and updates to MDN.

## [CSS `of <selector>` syntax](https://developer.mozilla.org#css_of_selector_syntax)

A new feature has been added to two CSS pseudo-classes to provide you with more options!
It's the new `of <selector>` syntax, which can be used with the [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child#the_of_selector_syntax) and [`:nth-last-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#the_of_selector_syntax) pseudo-classes.

Until now, while using these pseudo-classes, you could select sibling elements based on their position in the group, such as by specifying `even`, `odd`, or by specifying the notation [`An+B`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child#functional_notation). The `of <selector>` syntax lets you further narrow down the selection of elements and then target elements based on their `even`, `odd`, or `An+B` position. Support for this syntax is currently available in [Firefox and Safari](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#browser_compatibility). Here's a sneak peak into how you can use this new syntax:

```
/* using An+B notation in a 10-item list */
li:nth-child(-n + 3) {
  /* styles to apply to the first three list items */
}
/* using An+B notation with `of <selector>` in a 10-item list */
/* assuming 2nd and 5th list items have the class `important` */
li:nth-child(-n + 3 of .important) {
  /* styles to apply to the 2nd and 5th list items */
}
```
[Dave Letorey](https://github.com/dletorey) has documented this new syntax for the `:nth-child()` and `:nth-last-child()` pseudo-classes and also added some cool examples to demo how to use `of <selector>` with [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child#using_of_selector) and [`:nth-last-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#of_selector_syntax_example), [how it differs from selector `:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child#of_selector_syntax_vs_selector_nth-child), and [how to use it with striped tables](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child#using_of_selector_to_fix_striped_tables).

## [`<image>` value for CSS `content` property](https://developer.mozilla.org#image_value_for_css_content_property)

For the `<image>` value that can be specified with the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content) property, there's now wider support among browsers to also specify an `image-set()` and `<gradient>`.

Check out the new examples that [Dave](https://github.com/dletorey) has added to show replacement of an element's content with an `<image>` data type using [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_url), [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_gradient), and [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#element_replacement_with_image-set).

## [String matching in CSS `:lang()` pseudo-class](https://developer.mozilla.org#string_matching_in_css_lang_pseudo-class)

In Firefox, the [`:lang()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang) pseudo-class can now use string-matching semantics (including `*` wildcards) for matching language codes rather than prefix-matching semantics. Additionally, comma-separated lists of languages are now supported for matching multiple languages. Isn't this great:

```
/* Matches nl and de */
:lang("nl", "de") {
  color: green;
}
```
[Brian Smith](https://github.com/bsmth) has updated the [`:lang()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang) page with all the new parameter details, and he's also added some interesting [examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#examples).

## [CSS media features](https://developer.mozilla.org#css_media_features)

The experimental new CSS media feature [`prefers-reduced-transparency`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-transparency) lets you detect if a user has enabled the setting on their device to minimize the amount of transparent or translucent layer effects. This feature is currently only available in Firefox. Thanks to [CanadaHonk](https://github.com/CanadaHonk) for adding this new reference page for us.

Here's a quick look at what this feature looks like:

```
@media (prefers-reduced-transparency) {
  .translucent {
    opacity: 0.8;
  }
}
```
[Dipika Bhattacharya](https://github.com/dipikabh/) updated the [`scripting`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scripting) media feature to reflect that it is now fully supported in Firefox. However, being supported in only one browser, the feature still remains pretty much experimental. You can use this media query to style your CSS based on whether scripting, such as JavaScript, is available on the current document, only during initial page load, or not available at all.

Similarly, support for another media feature, [`inverted-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors), has been added to Firefox; however, this one is available behind a flag (`layout.css.inverted-colors.enabled`). You can use the `inverted-colors` media query to detect if your user agent or operating system has inverted all colors.

## [`ray()` value for CSS `offset-path` property](https://developer.mozilla.org#ray_value_for_css_offset-path_property)

The syntax for the [`ray()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray) function, which can be specified as a value for the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path) property, has been updated in the specification. `<ray-size>` is now optional, and the default value of `<ray-size>` is `closest-side`.

```
ray() = ray( <angle> && <ray-size>? && contain? )
<ray-size> = closest-side | closest-corner | farthest-side | farthest-corner | sides
```
[Dipika](https://github.com/dipikabh/) has added a new reference page for the [`ray()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray) function to document all the parameter details. Check out the examples to see how you can use this function value in `offset-path` to [animate an element along the ray path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray#animating_an_element_along_the_ray). Support for the `ray()` function is still behind flags on various browsers. The new syntax is also not yet adopted in all browsers.

## [ECMAScript module support](https://developer.mozilla.org#ecmascript_module_support)

Great news! Firefox also now supports static ([`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)) and dynamic ([`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)) loading of [ECMAScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) in dedicated and shared workers.
In addition, Firefox has added support for static import in service workers and worklets â this support is currently available only in Firefox. You can't use dynamic import in service workers and worklets because it is prohibited by the specification.

[Hamish Willee](https://github.com/hamishwillee) has made sure to update the impacted docs.

## [WebGPU API](https://developer.mozilla.org#webgpu_api)

Thanks to [Chris Mills](https://github.com/chrisdavidmills), documentation for the [WebGPU API](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) is now available on MDN. This API provides support for performing computation and graphics rendering by using the Graphics Processing Unit (GPU) of a device. Learn about the different [interfaces](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API#interfaces), including those for representing pipelines and for handling errors and queries.

This is still an experimental technology, so check [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API#browser_compatibility) before using it.

## [WebTransport API](https://developer.mozilla.org#webtransport_api)

The [WebTransport API](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport_API) specification has recently undergone updates.
[Hamish](https://github.com/hamishwillee) has updated all the relevant docs so you can learn about these features. There are [new constructor options](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport/WebTransport#parameters) â `allowPooling`, `requireUnreliable`, and `congestionControl`. There's also a few new properties â [reliability](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport/reliability), `draining`, and [congestionControl](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport/congestionControl). These are currently available only in [Firefox](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport#browser_compatibility).

## [Compression Streams API](https://developer.mozilla.org#compression_streams_api)

The interfaces provided by the [Compression Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Compression_Streams_API) are used to compress and decompress data using the `gzip` and `deflate` formats. [Firefox](https://developer.mozilla.org/en-US/docs/Web/API/Compression_Streams_API#browser_compatibility) also supports this API now.

[Brian](https://github.com/bsmth) has added a description for the compression methods â `gzip`, `deflate`, `deflate-raw` â used in the [CompressionStream](https://developer.mozilla.org/en-US/docs/Web/API/CompressionStream/CompressionStream#parameters) and [DecompressionStream](https://developer.mozilla.org/en-US/docs/Web/API/DecompressionStream/DecompressionStream#parameters) objects.

## [WebRTC API](https://developer.mozilla.org#webrtc_api)

Firefox finally added support for a bunch of WebRTC methods, properties, and dictionaries: [RTCRtpSender.getCapabilities()](https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpSender/getCapabilities_static), [RTCRtpReceiver.getCapabilities()](https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpReceiver/getCapabilities_static), [RTCRtpSender.setStreams()](https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpSender/setStreams), [RTCSctpTransport](https://developer.mozilla.org/en-US/docs/Web/API/RTCSctpTransport), [RTCPeerConnection.sctp](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/sctp), [RTCPeerConnection.connectionState](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState), [RTCPeerConnectionStats](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnectionStats), and [RTCAudioSourceStats](https://developer.mozilla.org/en-US/docs/Web/API/RTCAudioSourceStats). These docs have been spruced up by [Hamish](https://github.com/hamishwillee).

The WebRTC Statistics API has evolved significantly in recent years. The documentation and compatibility information were significantly out of date. As part of the above work, Hamish and [Vinyl Da.i'gyu-Kazotetsu](https://github.com/queengooborg) have also updated the browser compatibility information for all statistics-related interfaces and dictionaries.
This is part of an ongoing work to document the dictionaries that reflect browser compatibility for web features. If you're curious, you can keep track of their progress in the [RTCStatsReport statistics types](https://developer.mozilla.org/en-US/docs/Web/API/RTCStatsReport#the_statistic_types) table.

## [What's next?](https://developer.mozilla.org#whats_next)

A lot of exciting work is happening in different corners of MDN. You can already see parts of these projects live on the site.

### [Progressive web apps](https://developer.mozilla.org#progressive_web_apps)

There is a lot of great work happening to revamp the [Progressive web apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) documentation on MDN.

While the project is still ongoing, a lot of ground has been covered to create new [how-tos](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to), [installation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable) and [best practices](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices) guides, and reference pages. Kudos to [Estelle Weyl](https://github.com/estelle), [Patrick Brosset](https://github.com/captainbrosset), and [Will Bamberg](https://github.com/wbamberg) for reviving these docs. You can look forward to having access to the complete doc set very soon.

### [CSS module landing pages](https://developer.mozilla.org#css_module_landing_pages)

[Estelle](https://github.com/estelle) has been churning fascinating "in action" examples on the module landing pages in the CSS area of MDN. Check some of them out and you'd be delighted too - [Animations in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#animations_in_action), [Colors in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#colors_in_action), and [Filter effects in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects#filter_effects_in_action).

The addition of these examples is part of a bigger project to revamp the CSS module landing pages. The idea is for the landing pages to help connect all the dots when looking at a set of properties defined in a CSS module. This project is still in progress and should wrap up in the coming months.

## [Summary](https://developer.mozilla.org#summary)

I hope these updates were useful and provided you an insight into what's happening on the web and what's keeping the MDN staff, our partners, and contributors busy. Keep an eye out for more such updates in the coming weeks (*psst CSS nesting*).

Let us know you have any feedback or questions about this post. Feel free to join the discussion in the MDN Web Docs [Discord server](https://developer.mozilla.org/discord) or leave a comment on MDN's [GitHub discussion](https://github.com/orgs/mdn/discussions/categories/the-mdn-web-docs-blog).