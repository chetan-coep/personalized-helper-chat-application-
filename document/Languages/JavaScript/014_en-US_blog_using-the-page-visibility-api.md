---
id: "javascript_014"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 14
source_url: "https://developer.mozilla.org/en-US/blog/using-the-page-visibility-api"
language: "en"
retrieved_at: "2026-11-01 21:53:51"
content_hash: "3952f524cafae61475ff6e19f372b45515fadc3439e2d5982cb3b2bb6d0abda1"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/using-the-page-visibility-api

---

# Using the Page Visibility API

Checking document visibility gives you insight into how visitors are interacting with your pages and can provide hints about the status of your applications.
The [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) lets you find out the visibility of a page and set up event listeners to do something when page visibility changes.
Let's look at what page visibility means, how you can use this API, and some common pitfalls to avoid.

## [What's the Page Visibility API?](https://developer.mozilla.org#whats_the_page_visibility_api)

Initially, the Page Visibility API was developed as a [independent specification](https://www.w3.org/TR/page-visibility-2/), but it's been incorporated directly into the HTML spec under [Page visibility](https://html.spec.whatwg.org/multipage/interaction.html#page-visibility).
This API exposes a way to determine a document's visibility state so you can check if a web page is "visible" or "hidden".
This sounds straightforward, but pages can be "hidden" in several different ways.

A page is "hidden" if the browser window with the page is minimized, if it's completely obscured by another application, or the user switches to another tab. Page visibility also changes to "hidden" if the operating system's screen lock is activated, so mobile device behavior is also taken into consideration. By contrast, a page remains "visible" even when it's partially visible on the screen.

## [How to check page visibility changes](https://developer.mozilla.org#how_to_check_page_visibility_changes)

You can check the visibility of a document using [`document.visibilityState`](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState), which will return either `visible` or `hidden`.
Alternatively, you can check the value of the [`document.hidden`](https://developer.mozilla.org/en-US/docs/Web/API/Document/hidden) Boolean property:

```
console.log(document.visibilityState); // "visible"
console.log(document.hidden); // false
```
In practice, it's convenient to use the [`visibilitychange`](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilitychange_event) event so you can trigger logic when the visibility state of a page changes instead of checking the visibility manually:

```
document.addEventListener("visibilitychange", (event) => {
  // doSomething();
});
```
When the state changes, you can check the page visibility and then do something depending on the result:

```
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    // do something if the page visibility changes to hidden
  } else {
    // do something if the page visibility changes to visible
  }
});
```
It's worth noting that there's no `document.visible`, so if you're only interested in that state, you can use `document.visibilityState === "visible"` (or `!document.hidden`):

```
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "visible") {
    // The page is visible again!
  }
});
```
## [Why page visibility is useful](https://developer.mozilla.org#why_page_visibility_is_useful)

Page visibility is useful in many cases, but the most likely fits are in analytics, managing usage of compute resources, and adding functionality that can improve user experience (UX) on a range of devices. Let's take a look at these in more detail.

### [Session lifecycle in analytics](https://developer.mozilla.org#session_lifecycle_in_analytics)

In the analytics domain, it's common to record the point when pages change from `visible` to `hidden`.
A page changing to a `hidden` state might be the last event that's observable by a page, so developers often treat it as the end of the user's session.
However, this heavily depends on how you define 'a session'.
You may define a session based on a fixed period of inactivity as opposed to relying solely on 'first page hide'.
Therefore, this use case will vary according to your needs:

```
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden") {
    navigator.sendBeacon("/log", analyticsData);
  }
};
```
### [Managing resources efficiently](https://developer.mozilla.org#managing_resources_efficiently)

The ability to determine page visibility opens up the opportunity to **stop doing something** when the visitor is **no longer viewing the page**.
This capability is really powerful considering that it allows us to manage client (or even server) resources in a conscious way.

When it comes to managing resources, browsers play a significant role in this with features like [tab unloading](https://hacks.mozilla.org/2021/10/tab-unloading-in-firefox-93/) and optimizing [what background tabs are doing](https://archive.fosdem.org/2023/schedule/event/mozilla_firefox_energy_use).
We can still shift the solution left by looking at how we build web applications.
This allows us to include checks for efficiency earlier in the development cycle or make conscious performance improvements in areas that browsers don't automatically handle.

There's an excellent opportunity to use smaller bitrate video, or to throttle or pause network activity if regular real-time communication (WebSockets and WebRTC) happens with a server.
IndexedDB processes can be optimized as browsers don't throttle these connections to avoid timeouts.
You can find more information about what browsers handle in the "Policies in place to aid background page performance" section on the [Page Visibility API page](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API#policies_in_place_to_aid_background_page_performance).

### [Improving user experience](https://developer.mozilla.org#improving_user_experience)

When the page changes from `hidden` to `visible`, we could assume that a visitor has returned to our page, so we can restart anything that we may have paused when the page was hidden.
However, there are a few logical traps, especially concerning media, that you could fall into.
Therefore, you need to be careful when resuming actions in such cases.
We'll look at examples of this in detail in the next section.

## [Patterns to avoid with page visibility checks](https://developer.mozilla.org#patterns_to_avoid_with_page_visibility_checks)

Giving people control over when to start, resume, and skip media is essential for the usability of your pages, so this API should be used with caution to ensure your visitors have agency while browsing. You also shouldn't presume that visitors want media to be paused automatically when a page is hidden. Exposing a user preference or allowing visitors to opt-in to this kind of functionality is highly recommended.

There used to be a code snippet on MDN on the `visibilitychange` page that was a good example of how this API can cause usability issues.
Can you spot what the problem is in the JavaScript code below?

```
<audio
  controls
  src="https://mdn.github.io/webaudio-examples/audio-basics/outfoxing.mp3"></audio>
```
```
const audio = document.querySelector("audio");
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    audio.pause();
  } else {
    audio.play();
  }
});
```
In the HTML, there is an `<audio>` element with controls visible so the user can start and stop the media.
In JavaScript, we're looking at the `visibilitychange` event and doing the following:

- If the page is hidden, pause the audio.
- If the page is shown, play the audio.

This sounds reasonable at first, but we encounter issues such as audio autoplaying when the user switches to another tab and back again or when restoring a browser window after it's been minimized.
The point is that page visibility may toggle between `hidden` and `visible` without the user ever interacting with the `<audio>` element.

This situation becomes even more surprising and distracting if the `<audio>` element is located below the page fold and is not visible when the page loads.
You might unintentionally prompt your users to search for tabs where audio is playing and lead them to a place where it's not obvious what is playing, which can be extremely frustrating.

To avoid usability issues, it's always a good idea to see if people have interacted with the media before resuming playback.
One way of doing this is to store the state of the audio player when the page is hidden.
When the page visibility changes to `visible` again, we resume media playback *only if it was playing when the page was hidden*.

Let's modify the event listener to store the audio state on page hide.
A boolean `playingOnHide` variable is sufficient for this purpose; we can set it when the document's visibility changes to `hidden`:

```
// Initialize as false; we're not auto playing audio when the page loads
let playingOnHide = false;
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    // Page changed to "hidden" state, store if audio playing
    playingOnHide = !audio.paused;
    // Pause audio if page is hidden
    audio.pause();
  }
});
```
As with `document.hidden`, there is no `audio.playing` state, so we have to check `!audio.paused` (not paused) instead.
That means the `playingOnHide` Boolean can be set to whatever the value of `!audio.paused` is on page hide, and we're pretty much done.
The only other state the visibility of the page can be is `visible`, so in the `else` statement, we handle the playing logic:

```
let playingOnHide = false;
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    playingOnHide = !audio.paused;
    audio.pause();
  } else {
    // Page became visible! Resume playing if audio was "playing on hide"
    if (playingOnHide) {
      audio.play();
    }
  }
});
```
The finished code looks like this with a neat little gate for checking the audio state on page hide:

```
<audio
  controls
  src="https://mdn.github.io/webaudio-examples/audio-basics/outfoxing.mp3"></audio>
```
```
const audio = document.querySelector("audio");
let playingOnHide = false;
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    playingOnHide = !audio.paused;
    audio.pause();
  } else {
    if (playingOnHide) {
      audio.play();
    }
  }
});
```
## [Summary](https://developer.mozilla.org#summary)

I hope you enjoyed this post about page visibility and why I think it opens up interesting opportunities for resource management, analytics, UX, and other use cases.
I'm looking forward to hearing your thoughts on different ways to use this API and what other efficiency gains developers can make use of that browsers don't handle well.
Are there any other patterns that developers should avoid when using this API?
Feel free to [get in touch with us](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels) and let us know what you think or if I've missed something!