---
id: "javascript_037"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 37
source_url: "https://developer.mozilla.org/en-US/blog/fix-image-lcp"
language: "en"
retrieved_at: "2026-11-01 21:52:24"
content_hash: "d9563a8cbaec13bcba74f4af2eef7105485664b9c07aa946e109396b65c98ccb"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/fix-image-lcp

---

# Fix your website's Largest Contentful Paint by optimizing image loading

Images make up a big part of most websites.
They're also often the largest element that first appears on your page, and thus the [Largest Contentful Paint (LCP)](https://www.debugbear.com/docs/metrics/largest-contentful-paint?utm_campaign=mdn-3) element - a metric from Google's [Core Web Vitals](https://www.debugbear.com/docs/metrics/core-web-vitals?utm_campaign=mdn-3).
When images load slowly, they can make your LCP time longer.
This hurts your Core Web Vitals scores and overall user experience.
Let's look at how to make images on the web load faster.

## [Introduction](https://developer.mozilla.org#introduction)

When you add an image to your website, there's more happening behind the scenes than you might think.
Starting with the basics, the simplest way to add an image onto a page is with a HTML [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) element:

```
<img src="image.jpg" alt="Description of the image" />
```
You can also add images with CSS background images, which are still [candidates for LCP](https://www.debugbear.com/blog/largest-contentful-paint-background-images?utm_campaign=mdn-3):

```
.container {
  background-image: url("image.jpg");
}
```
Some developers load images using JavaScript instead. This delays when the browser starts downloading the image, since JavaScript has to run first.

```
// Don't load images like this unless you have a good reason
const img = new Image();
img.src = "image.jpg";
document.querySelector(".container").appendChild(img);
```
In fact, the JavaScript approach can be far worse when you have JavaScript files requesting other JavaScript files, which then request images. This is known as a request chain, and is explained later in this article.

To understand image loading, we use network [request waterfalls](https://www.debugbear.com/docs/waterfall?utm_campaign=mdn-3).
These show the timing of all network requests on your page.
Modern performance testing tools like [DebugBear](https://www.debugbear.com/?utm_campaign=mdn-3) can generate these waterfalls for you, and can even identify the LCP element on your page, as shown by the LCP badge in the previous screenshot.

## [How images load on a webpage](https://developer.mozilla.org#how_images_load_on_a_webpage)

What happens when an image loads on a web page? Understanding this process helps explain why certain optimization techniques work.

When the browser finds an image in HTML that it's loading, the browser:

1. Makes a network request to download the image: This is just like downloading any other resource, like CSS or JavaScript.
2. Assigns a [priority](https://www.debugbear.com/blog/request-priorities?utm_campaign=mdn-3) to that request (more on this later): This determines when the image downloads compared to other resources.
3. Decodes the image data once it arrives: This is the process of turning the raw image data into pixels that can be displayed on the screen.
4. [Renders](https://web.dev/articles/rendering-performance) the image on the page: The browser positions and displays the image according to the page layout.

Unlike some resources (such as CSS), image downloads don't block the rest of the page from loading.

## [How image loading affects LCP](https://developer.mozilla.org#how_image_loading_affects_lcp)

LCP is made of [sub-parts](https://www.debugbear.com/blog/lcp-subparts?utm_campaign=mdn-3).
Each sub-part has an impact on the overall LCP score.
The slower the sub-parts, the slower the LCP score.
The following screenshot shows a part of DebugBear's [Real User Monitoring](https://www.debugbear.com/real-user-monitoring?utm_campaign=mdn-3) dashboard that has identified LCP sub-parts for a real page view.

Knowing each sub-part is key to understanding how to improve your LCP score, so let's have a look at the sub-parts in detail.

### [Time to First Byte (TTFB)](https://developer.mozilla.org#time_to_first_byte_ttfb)

This is the time it takes for the server to start responding with the main HTML document. This can be notably slow if:

- There's a large geographic distance between the server and the user.
- There are incorrect cache headers or the website uses an unoptimized cache strategy.

This screenshot shows network timing information for a particular request. It's interesting that the TTFB took longer than the download itself! In fact, the other resources which are highlighted also have a longer TTFB than the download itself!

### [Resource load delay](https://developer.mozilla.org#resource_load_delay)

This is the time it takes the browser to [discover the image and request the image](https://www.debugbear.com/blog/lcp-resource-load-delay?utm_campaign=mdn-3).
This can be slow if:

- The image is in a request chain, where resources have to load before the image can start downloading.
- The image is lazy loaded, which delays the download until the image is near or in the viewport.
- The image is inserted into the DOM using JavaScript - even if that JavaScript is inlined in the HTML. This is because the browser's look-ahead parser has to parse and execute the JavaScript before the image can be discovered.

### [Resource download time](https://developer.mozilla.org#resource_download_time)

This is the time it takes for the image to download, and is likely what most of us think of when we think of a "slow loading image". This can be slow if:

- The image is large and not optimized.
- Off-screen images, or other non-critical resources are downloading at the same time, causing network contention.

The following screenshot shows a collection of JavaScript files where the download time far outweighs the TTFB. Request waterfalls within DebugBear indicate where actual content download is happening within the horizontal blue bars. The darker shades of blue indicate where content download is in progress.

### [Resource render delay](https://developer.mozilla.org#resource_render_delay)

This is the time it takes for the browser to decode the image data and [render it on the page](https://www.debugbear.com/blog/lcp-render-delay?utm_campaign=mdn-3). This can be slow if:

- The image uses a highly compressed format which takes more time to decode.
- Render-blocking resources are still downloading, which can delay the image from rendering.
- The [main thread](https://www.debugbear.com/docs/performance/minimize-main-thread-work?utm_campaign=mdn-3) is blocked, and cannot render the image to the page.
- The image was loaded using a [`<link rel="preload">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload) element, but the page element using the image hasn't been created yet

## [Modern image formats and responsive images](https://developer.mozilla.org#modern_image_formats_and_responsive_images)

Modern image formats help reduce image file sizes while maintaining quality.
Using a modern image format can have a positive impact on the **Resource download time** sub-part of LCP.
The recommended [modern formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types) are:

- [WebP](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types#webp_image): Widely supported and offers good compression.
- [AVIF](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types#avif_image): Newer format with even better compression.

You can use the [Squoosh](https://squoosh.app/) web app to convert your images to these formats.
Here's how to serve different formats for browsers to choose from:

```
<picture>
  <source srcset="image.avif" type="image/avif" />
  <source srcset="image.webp" type="image/webp" />
  <img
    src="image.jpg"
    alt="Description of the image"
    width="1200"
    height="800" />
</picture>
```
The following screenshot shows an LCP resource from a request waterfall.
While TTFB is significant, it doesn't compare to a whole 3 seconds of content download time for the image.
Considering the lab test was run using a [throttled](https://www.debugbear.com/blog/packet-level-throttling?utm_campaign=mdn-3) connection, and considering this image is 1MB in size, this begins to make sense.

Putting the 1MB image into Squoosh, and converting it to AVIF @ 80% quality, gives a 95% saving which results in a 46KB file. This has a positive impact on content download time.

It's important to think about browser support when using modern [image formats](https://www.debugbear.com/blog/image-formats?utm_campaign=mdn-3).
You could also consider configuring your server to serve the right format based on the browser's [Accept header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation/List_of_default_Accept_values#values_for_an_image).

[Responsive images](https://www.debugbear.com/blog/responsive-images?utm_campaign=mdn-3) help you serve the right size for each screen.
This saves bandwidth and processing time.

```
<img
  src="small.jpg"
  srcset="small.jpg 300w, medium.jpg 600w, large.jpg 900w"
  sizes="(max-width: 500px) 300px,
         (max-width: 900px) 600px,
         900px"
  alt="Description of the image" />
```
The example uses an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) element (rather than the [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture) element) with the `srcset` and `sizes` attributes to provide small, medium, and large image candidates for different viewport widths:

- A small image on small screens (less than 500px wide).
- A medium image on medium screens (500px to 900px wide).
- A large image on large screens (over 900px wide).

This way, you don't waste bandwidth for large images on small screens. As a practical example, this website takes a large amount of time to download an LCP image of 2.26MB, even on a mobile viewport.

Upon further investigation, it turns out the image has dimensions of **1920âÃâ1080**.
After optimizing this image to use a modern image format, the developers working on this website can produce different versions of the image suitable for different viewport dimensions.

## [How request chains impact LCP](https://developer.mozilla.org#how_request_chains_impact_lcp)

Sometimes images appear later than they should because of request chains. A request chain happens when one or more resources (outside of the main HTML) have to load before another request can start:

For example, if your JavaScript loads an image, at a high level, the browser has to:

1. Download the HTML.
2. Download the JavaScript: Depending on how the JavaScript is loaded, this can also block page rendering.
3. Execute the JavaScript: There is a parse and execution cost for JavaScript, which is often exacerbated on low-end devices.
4. Start downloading the image.

This creates a chain that delays the image load. You can help break this chain by:

- Using a regular `<img>` element directly in the HTML.
- Using the `<link rel="preload">` element to download the image earlier.

The [preload hint](https://www.debugbear.com/blog/resource-hints-rel-preload-prefetch-preconnect?utm_campaign=mdn-3) tells the browser to download a resource as soon as possible, and is placed in the head of your HTML:

```
<link rel="preload" as="image" href="image.jpg" />
```
In this example, DebugBear identifies that the LCP image is part of a chain, and also offers an [experiment](https://www.debugbear.com/docs/experiments?utm_campaign=mdn-3) to test a fix.

The experiment automatically preloads the request chain for the LCP image, including the LCP image itself, into the main HTML document. With the experiment run, a before and after comparison is available to view:

The previous screenshot shows:

- The CSS resource part of the LCP request chain is now preloaded.
- The LCP image itself is now preloaded.

The before and after LCP score below confirms that an improvement was made.

## [Using fetchpriority=high on key images](https://developer.mozilla.org#using_fetchpriorityhigh_on_key_images)

Browsers assign different priorities to network requests. This determines the order resources download when they compete for bandwidth.
You can increase the priority of your LCP image with the [`fetchpriority` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#fetchpriority):

```
<img src="image.jpg" alt="Description of the image" fetchpriority="high" />
```
This tells the browser to prioritize downloading the image, relative to other resources.
You can also use `fetchpriority` with the [`rel="preload"` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload):

```
<link
  rel="preload"
  href="/background-image.avif"
  as="image"
  fetchpriority="high" />
```
This can be especially useful when the LCP is a background image, and would otherwise be discovered late in the page load - after the CSS has been downloaded and parsed.

This example shows an improvement on Discord, where the **entire** request chain for the LCP image is preloaded, and marked with `fetchpriority="high"`, which helps improve the LCP time.

**Score difference:**

**Request waterfall difference:**

The previous screenshot shows how Discord's LCP image was downloaded much earlier.

The `FP=HIGH` badge confirms that a high `fetchpriority` was specified, so the LCP resource now maintains a high priority, whereas previously, the LCP image started out as a low priority.

The thin red vertical line appears in the DebugBear request waterfall view for a resource which has had its [priority changed](https://www.debugbear.com/blog/request-priorities#can-the-priority-of-a-network-request-change-later-on?utm_campaign=mdn-3).
If the browser is late to discover that a priority change is needed (for example from a `low` priority to a `high` priority), you can assist the browser by applying `fetchpriority="high"` on the applicable resource.

## [Lazy loading images](https://developer.mozilla.org#lazy_loading_images)

Not every image needs to load right away.
Images below the viewport can load later, saving bandwidth for more important resources.
Here's how to [lazy load an image](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading):

```
<img loading="lazy" src="image.jpg" alt="Description of the image" />
```
Consider a web page with 10 images, where only the first image (the LCP element) is visible in the initial viewport. In such a scenario, lazy loading the remaining 9 images can help improve loading of the first image. When you lazy load images below the fold, you:

1. Reduce competition for bandwidth. When you free up bandwidth, the LCP image can sometimes load faster.
2. Let the browser focus on loading important resources first.
3. Save user's data if they never scroll down.

This example shows two different waterfalls for the same website, these examples attempt to show the impact that resource competition can have on an LCP image.

**Waterfall 1** shows a large LCP image that takes a long time to download, and appears to be competing for bandwidth with the other image resources on the page.

**Waterfall 2** shows the same large LCP image, but this time, DebugBear's [request blocking](https://www.debugbear.com/docs/blocking-requests?utm_campaign=mdn-3) is used to block other image resources that are not the main LCP image.
This is done as a test, to show how bandwidth competition impacts resource download time.

If you look closely, the actual data download (the dark blue patches) for the `RB_8220-Large-1.png` image are a lot more concentrated in the second waterfall.
To understand the significant impact this has on timing, take a look at the waterfall comparison view.
For the test run where the LCP image didn't have to compete for bandwidth, the image downloaded in less than half the time!

## [Summary](https://developer.mozilla.org#summary)

Images are a big part of most websites, and can have a big impact on your LCP score. Here's a summary of how to optimize images for LCP:

1. Use modern image formats like WebP and AVIF.
2. Serve responsive images to save bandwidth.
3. Use `preload` and `fetchpriority` to prioritize key images.
4. Lazy load images below the fold to reduce network contention.
5. Avoid request chains that delay image loading.

*This post is sponsored by [DebugBear](https://debugbear.com/?utm_campaign=mdn-3). DebugBear helps teams optimize web performance and Core Web Vitals, providing speed insights and continuous monitoring for faster websites.*