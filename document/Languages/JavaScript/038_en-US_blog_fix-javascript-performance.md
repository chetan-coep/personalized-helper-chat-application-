---
id: "javascript_038"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 38
source_url: "https://developer.mozilla.org/en-US/blog/fix-javascript-performance"
language: "en"
retrieved_at: "2026-11-01 21:52:26"
content_hash: "6b982659b80896df47aecb918d5640f59c0b794db86515cc58f785145823c0c8"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/fix-javascript-performance

---

# Fixing your website's JavaScript performance

When it comes to web performance, you may think of techniques like compression, asset optimization, or even HTTP caching. These are really important, and there's plenty of existing resources covering ways to fix or implement them. However, some less-discussed performance bottlenecks can severely impact website speed. In this post, we'll discuss three issues that often originate from inefficient JavaScript patterns:

- **Long tasks:** JavaScript operations that monopolize the main thread, leading to unresponsive user interfaces.
- **Large bundle sizes:** JavaScript code that's too big to download, parse, and execute quickly.
- **Hydration issues:** The process of attaching JavaScript functionality to server-rendered HTML.

While these are not new problems, modern web practices and web frameworks can exacerbate these issues, putting them in the spotlight once again.

**Note:**
These issues can also stem from other sources, such as CSS.
For example, a [long task](https://developer.mozilla.org/en-US/docs/Glossary/Long_task) can be caused by a complex CSS selector that takes a long time to match elements.
However, the focus of this post is on JavaScript.

Here's more information on each bottleneck, along with high-level commentary on addressing such performance issues.

## [Long tasks](https://developer.mozilla.org#long_tasks)

Long tasks occur when there's constant [main thread](https://developer.mozilla.org/en-US/docs/Glossary/Main_thread) activity that blocks the browser for 50ms or more.
Note that many JavaScript and browser [rendering tasks are performed sequentially](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model) while on the main thread.

When the main thread is busy, it cannot handle user interactions, or do other important rendering tasks. This can lead to noticeable delays in page responsiveness.

Let's run a [website speed test](https://www.debugbear.com/test/website-speed?utm_campaign=mdn-1) on a Next.js page.
This page is server-rendered and then hydrated on the client. Interestingly, the page shows that the user saw useful content quite early on, in spite of the large HTML payload.

The **lab-based test** that captures this page load shows an acceptable Largest Contentful Paint ([LCP](https://developer.mozilla.org/en-US/docs/Glossary/Largest_contentful_paint)) time, and no Cumulative Layout Shift ([CLS](https://developer.mozilla.org/en-US/docs/Glossary/CLS)).
This simplified diagram shows what happens when a user interacts during a long task.

The problem here is that even content may be loaded in a timely manner, the page was not interactive for a long time as the browser was busy parsing and executing the JavaScript. During the slow hydration process, the user saw content that appeared to be interactive, but was not. This meant that the page appeared 'frozen' while the user was trying to interact with it.

This example is particularly interesting because it puts emphasis on parse and execution times, not just download times.

### [How to shorten your long tasks](https://developer.mozilla.org#how_to_shorten_your_long_tasks)

1. **Yield to the main thread:** Break up your work into smaller, manageable tasks.
This effectively gives the browser a break, allowing it to handle user interactions and rendering.
You can learn more about this technique in our [article on using the Scheduler API](https://www.debugbear.com/blog/scheduler-yield?utm_campaign=mdn-1).
2. **Use Web Workers:** While it might not make your code run faster, [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) allow you to run JavaScript in the background, keeping your main thread free for user interactions and rendering.
3. **Optimize your rendering patterns:** Implement techniques like:
  - [Reducing DOM size](https://www.debugbear.com/blog/excessive-dom-size?utm_campaign=mdn-1): Fewer elements mean less work for the browser.
  - [Eliminating layout thrashing](https://web.dev/articles/avoid-large-complex-layouts-and-layout-thrashing): Avoiding multiple forced reflows can improve performance.
  - [Using efficient CSS selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/CSS#:~:text=before%20serving%20them.-,Simplify%20selectors,-%3A%20People%20often%20write): Complex selectors can slow down rendering.

As a general performance strategy, you should [minimize main thread work](https://www.debugbear.com/docs/performance/minimize-main-thread-work?utm_campaign=mdn-1) and activity.

## [Large bundle sizes](https://developer.mozilla.org#large_bundle_sizes)

A large bundle size refers to the total amount of JavaScript code that needs to be downloaded, parsed, and executed when a user visits your website. The 'bundle' is a JavaScript file that contains your application code, along with any dependencies. Oversized JavaScript bundles can lead to several issues:

- **Lower cache hit rates:** Large files are more likely to be invalidated and re-downloaded because they are more likely to change.
This reduces the benefits of caching.
- **Slower download times:** Larger files take longer to download, especially on slower connections.
- **Increased parsing and execution times:** This one is easily overlooked: even on a fast network connection, parsing and executing large JavaScript files can take a significant amount of time, especially on mobile devices.
Slow parse and execution times also contribute to long tasks.

The last point is also an issue for user interactions. Users interact with pages expecting immediate feedback, but if the browser is busy parsing and executing JavaScript, it can't respond to user input.

The previous screenshot shows a page that has a number of large JavaScript bundles. The page rendering is blocked by:

- The download time of the JavaScript bundles.
- The parser-blocking nature of the JavaScript bundles.
- Execution time of the JavaScript bundles.

### [How to address large bundle sizes](https://developer.mozilla.org#how_to_address_large_bundle_sizes)

- **Implement [tree shaking](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking)** to remove unused code from your final bundle.
- **Use code splitting** to break your application into smaller chunks that can be loaded selectively.
- **Use lazy loading** to [defer](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#defer) the loading of non-critical resources until they're needed.
- [**Remove unused code**](https://www.debugbear.com/blog/reduce-unused-javascript?utm_campaign=mdn-1) by using the Coverage Panel in Chrome DevTools or Edge DevTools to identify and eliminate unused code.
Coverage is compatible with source maps so you can understand exactly what source code file is unused, and can be safely removed/deferred.
- **Move to native web platform features** where possible, reducing the need for custom JavaScript code.
Many common patterns and features that were historically implemented from scratch using JavaScript now have native browser support.
This means you can achieve the same functionality with less code.

Here are some powerful web platform features that can replace common JavaScript implementations:

- [**CSS scroll snapping**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap) instead of JavaScript-powered carousels.
- [**View Transitions**](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) for smooth transitions between pages and page components.
- [**CSS grid**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout) for complex page layouts.
- [**Intersection Observer**](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) for in-viewport detection for UI elements or components.
- [**Native lazy loading**](https://www.debugbear.com/blog/image-lazy-loading?utm_campaign=mdn-1) for images and iframes.
- [**Popover API**](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API) for accessible popup functionality.

And here are some additional web platform features to be aware of.
You can start to try these out, but be mindful that they don't have cross-browser support yet.
If you use these features, you should check that your website [continues to be usable](https://developer.mozilla.org/en-US/docs/Glossary/Graceful_degradation) on browsers which don't yet support such features.

- [**Speculation rules**](https://www.debugbear.com/blog/speculation-rules?utm_campaign=mdn-1) with prerendering for instant navigation, replacing some SPA (Single Page Application) behavior (currently Chromium-only).
- [**Scroll-driven animations**](https://scroll-driven-animations.style/) for effects tied to scroll position (currently Chromium-only).
- [**Anchor positioning**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using) for tooltips and floating elements (currently [experimental](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#browser_compatibility)).

## [Hydration issues](https://developer.mozilla.org#hydration_issues)

JavaScript bundle sizes used to be easier to understand.
Developers knew what went into them; they consisted of the developer's own code, the framework's code, and third-party library code.
All these parts were combined into one file (like `app-v123.js`) during the build process.
This made it simpler to identify what was causing large file sizes.

However over time, JavaScript web frameworks introduced server-side rendering. This new approach created a different kind of HTML response, leading to hydration issues.

### [What is hydration in web development?](https://developer.mozilla.org#what_is_hydration_in_web_development)

[Hydration](https://www.debugbear.com/blog/javascript-hydration?utm_campaign=mdn-1) is the process of attaching JavaScript functionality to server-rendered HTML, making the HTML interactive on the client-side.
Popular frameworks like Next.js use certain hydration techniques by default.

While hydration can complement server-side rendering (SSR) capabilities, it can introduce performance challenges:

- **Increased document size:** Some frameworks serialize state into the HTML source as JSON, bloating the initial payload and even [duplicating data](https://web.dev/articles/rendering-on-the-web#rehydration-duplication).
In addition, the inlined serialized state carries a parse and execution cost, as discussed earlier.
- **Interactivity delays:** Users may experience a frustrating period where [the page is visible but not yet interactive](https://developer.mozilla.org/en-US/docs/Glossary/Time_to_interactive).
The larger the hydration payload, the longer this delay is.
This is sometimes referred to as the uncanny valley.
- **Wasteful rebuilding:** Some JavaScript frameworks offering SSR functionality effectively lead to the DOM being built twice â once on the server and again on the client during hydration.
This redundancy can waste resources and slow down the time to interactivity.

You should always consider the impact of popular JavaScript frameworks and libraries on performance. The abundance of resources, tutorials, and starter kits for popular frameworks can sometimes lead developers to choose them without fully considering the performance implications.

For some web developers, creating a website with a JavaScript framework is the default choice, no matter the use case. Framework popularity does not always translate to better UX, so you must balance developer ergonomics, maintainability, and user experience.

Debugbear's [HTML Size Analyzer](https://www.debugbear.com/html-size-analyzer?utm_campaign=mdn-1) is particularly useful as it breaks down the size of the HTML document, showing the size of the initial HTML payload and the size of the hydration payload.
The previous screenshot shows that the large HTML document is largely due to:

- 50kb of paragraph text (the content the user sees first)
- 50kb of JSON data (the hydration payload)

It's not a coincidence that the JSON data is the same size as the paragraph text. This is because the JSON data is a serialized version of the paragraph text. This duplication is a common issue with hydration payloads.

### [Strategies for mitigating hydration issues](https://developer.mozilla.org#strategies_for_mitigating_hydration_issues)

Here are some avenues you can explore to improve the performance of web apps that have issues with hydration. You should be aware that using one of these techniques can involve significant architectural changes, and in some cases, can involve moving to a different JavaScript framework.

1. **[Progressive hydration](https://www.patterns.dev/react/progressive-hydration) / Selective hydration:** Prioritize hydrating the most critical parts of your application first, deferring less important components until later.
2. **[Islands architecture](https://deno.com/blog/intro-to-islands):** Implement "[islands](https://docs.astro.build/en/concepts/islands/)" of interactivity within a sea of static content, reducing the overall hydration cost.
With islands architecture, you typically use directives to mark which islands should be hydrated.
3. **[Resumability](https://qwik.dev/docs/concepts/resumable/):** Instead of rebuilding the entire DOM, explore frameworks that can "resume" the server-rendered state more efficiently.
At times, almost no JavaScript is sent down during page load, but the necessary JavaScript is fetched and executed when needed, such as [on user interaction](https://www.patterns.dev/vanilla/import-on-interaction/).

#### Server-side rendering

Consider ditching complex frameworks, and instead use a server-side rendered application with vanilla client-side JavaScript:

1. Use regular hyperlinks and form submissions for navigation.
2. Implement View Transitions API for smooth page transitions.
3. Add a thin layer of JavaScript only where absolutely necessary.

For example, you can use:

- [Hotwire](https://hotwired.dev/) for basic client-side functionality.
- [Stimulus](https://stimulus.hotwired.dev/) for more advanced client-side interactions.
- [Turn](https://domchristie.github.io/turn/) for smooth transitions between pages and components.

When you combine these tools with effective caching strategies and page preloading, you can create highly performant web applications without sacrificing functionality and user experience.

## [Measure how JavaScript performance impacts real users](https://developer.mozilla.org#measure_how_javascript_performance_impacts_real_users)

The [Interaction to Next Paint](https://www.debugbear.com/docs/metrics/interaction-to-next-paint?utm_campaign=mdn-1) (INP) metric measures how quickly a website responds to user input.
If the page freezes for half a second after an interaction, then the page will not feel responsive to the user.
INP can be calculated in the browser using the [Event Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEventTiming) or using a library like [web-vitals.js](https://github.com/GoogleChrome/web-vitals).

When an interaction causes rendering delays, the [Long Animation Frames API](https://www.debugbear.com/blog/long-animation-frames?utm_campaign=mdn-1) can tell you what specific scripts were responsible.
Every time there's a rendering delay a [`PerformanceEntry`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEntry) with the type `long-animation-frame` is recorded.
You can access these events like this:

```
performance.getEntriesByType("long-animation-frame");
```
The `invokerType` tells you why the script was running.
In the example below the value is `classic-script`, which means the processing occurred during the initial evaluation of the script file.

DebugBear [real user monitoring](https://www.debugbear.com/real-user-monitoring?utm_campaign=mdn-1) can visualize this data for visitors on your website, showing when different scripts were running during the interaction.

You can also see what page element the user interacted with and when the interaction occurred. If the user interacts with a page soon after loading this often causes additional delays, as some parts of the page are still loading, which will delay event handlers.

Continuously monitoring INP scores on your websites gives you insight into what pages on your website often display poor interaction responsiveness, and how different visitor groups have experienced your website over time. Based on the Long Animation Frames data you can also see scripts are most often responsible for interaction delays.

## [Summary](https://developer.mozilla.org#summary)

This post explored three lesser-known performance bottlenecks caused by excessive JavaScript: long tasks, large bundle sizes, and hydration issues. We examined how web frameworks can sometimes amplify these problems, resulting in slower load times and negatively impacting user interactions. Finally, we discussed approaches to mitigate these bottlenecks and what you can do to measure how slow JavaScript impacts your visitors.

We hope you found this post helpful and that it inspires you to build more efficient, high-performing websites that provide a smoother experience for users.

*This post is sponsored by [DebugBear](https://www.debugbear.com?utm_campaign=mdn-1). DebugBear helps website developers deliver a better user experience and pass Google's Core Web Vitals assessment. Get detailed page speed recommendations and continuously monitor synthetic and real user page speed metrics.*