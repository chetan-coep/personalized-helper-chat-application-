---
id: "javascript_040"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 40
source_url: "https://developer.mozilla.org/en-US/blog/goodbye-third-party-cookies"
language: "en"
retrieved_at: "2026-11-01 21:52:31"
content_hash: "88b1c4fb0bf5869509998fd3cc6e33c156a3f905fd56040b356b40d7ab59f637"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/goodbye-third-party-cookies

---

# Saying goodbye to third-party cookies in 2024

The tail end of 2023 welcomes positive news for web privacy, as Chrome announces it is to join Firefox and Safari in deprecating third-party cookies in 2024 â starting with 1% of users from Q1 2024 to facilitate testing and ramping up from there.

This article explains the issues behind third-party cookies, what has been done already to mitigate those issues, Chrome's plans to disable them starting in Q1 2024, and how this all affects web developers and the users of their products.

## [The problem with cookies](https://developer.mozilla.org#the_problem_with_cookies)

Cookies have been around for a very long time on the web. In a nutshell, the idea is that a site can set a cookie on a user's browser via the [`Set-Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) response header once a resource has been requested. This cookie can contain whatever data strings the site owners wish, and is generally used to provide state to websites.

For example, a cookie allows websites to retrieve information such as whether the user previously logged in, what they added to their shopping cart, their theme preferences and other personalization settings, saved game state, etc.

**Note:** Cookies used to be the primary method of storing client-side site data, although now more useful technologies exist for that purpose such as [Web Storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) and [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).


The above use cases can all be achieved with cookies set for documents existing on the same domain as the URL loaded in the browser. These are referred to as *first party cookies*.

Problems can arise when cookies are set for components that exist on different domains than the embedding document, such as images, or other documents embedded via [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)s. These cross-site cookies are commonly referred to as *third-party cookies*âbut the behavior and potential issues are the same whether you own all the involved sites or not.

Third-party components can store information in their cookies from any and all documents they are embedded in. The originating third-party domain can then get access to all those third-party cookies, aggregating information from each one. This may sound harmless at first, and there are many legitimate uses of third-party cookies â for example a company might want to share user login state and profile information across multiple sites that it owns that are on different domains, or record analytics across its different properties to investigate user journeys and build more usable experiences. An ad tech company might want to infer user interests from the sites they visit to serve them more relevant ads.

However, in the worst cases, third-party cookies are used to track users around the web, building up a detailed profile of them that could include not only interests but also deeply personal information such as gender, sexuality, religion, political affiliation, etc. This information can be used to build creepy, invasive online experiences and is also sold to other third parties. In such cases, they are referred to as *tracking cookies*.

Legislation such as the [General Data Privacy Regulation](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (GDPR) in the European Union and the [California Consumer Privacy Act](https://www.oag.ca.gov/privacy/ccpa) (CCPA) have helped by making it a legal requirement for companies to be transparent about the cookies they set and the information they collect, for example by asking customers to opt in to such data collection, allowing them to see what data a company hold on them, and allowing them to delete it if they wish. However, it is still not always crystal clear to customers how their data is being used.

## [How browsers have responded to this](https://developer.mozilla.org#how_browsers_have_responded_to_this)

Browser vendors such as Mozilla and Apple provide general defaults that block third-party cookies, while also including exceptions and heuristics in their source code to work around long-standing third-party cookie issues with popular websites.

For example:

- Mozilla's [Anti-tracking policy](https://wiki.mozilla.org/Security/Anti_tracking_policy) has led to Firefox blocking third-party cookies from known trackers by default (see [Firefox tracking protection](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Firefox_tracking_protection) and [Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop)). Enhanced Tracking Protection can be set to Standard, Strict, or Custom. [Standard mode](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop#w_standard-enhanced-tracking-protection) enables [Total Cookie Protection](https://blog.mozilla.org/en/products/firefox/firefox-rolls-out-total-cookie-protection-by-default-to-all-users-worldwide/), which gives third-party cookies a separate cookie jar per site, thereby preventing cross-site tracking. In [Strict mode](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop#w_strict-enhanced-tracking-protection), Firefox blocks all third-party cookies.
- Apple also has a similar [Tracking prevention policy](https://webkit.org/tracking-prevention-policy/); following this has led to a similar set of third-party cookie protections that are enabled by default; see [Intelligent Tracking Prevention](https://webkit.org/tracking-prevention/#intelligent-tracking-prevention-itp) (ITP) for details.
- The [Brave](https://brave.com/) browser also blocks tracking cookies by default.

It is possible to allow usage of third-party cookies on a case-by-case basis in Firefox via browser settings. In Safari however, control is more limited â you can turn off cross-site tracking prevention, but allowing access to third-party cookies per frame can only be done at the code level, via the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API).

### [Google's long(er) game](https://developer.mozilla.org#googles_longer_game)

This brings us on to Google who, from a cursory glance, seem to be slower off the mark than other browsers with regards to third-party cookie protection. At time of writing, third-party cookies are blocked only when in Incognito mode by default, although users can set Chrome to block third-party cookies all the time if they wish.

**Note:** Microsoft Edge also currently does not block third-party cookies by default.


Google's seemingly-slow response is a result of its vested interest in the business uses of third-party cookies, which includes advertising by a wide range of different organizations, including Google, as well as third-party authentication services and many other uses besides. Chrome also has a large share of the browser market which amplifies concern about the potential of breaking critical journeys for their user base, for example logging into government services or buying groceries.

Rather than quickly going for a blanket disabling option, Google has opted for a more nuanced solution â phasing out third-party cookies more slowly while developing new technologies to ensure that valid use cases have a privacy-focused way forward after third-party cookies are disabled by default, rather than potentially motivating sites to move to more covert forms of tracking or moving content behind sign-ins and paywalls.

These new web platform features are collected under the blanket of the [Privacy Sandbox](https://developer.chrome.com/privacy-sandbox/) project, and have already undergone much development and testing. Some now enjoy cross-browser support, for example the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API), paving the way towards better cross-browser consistency in handling cross-site cookies.

These features have now reached the point where Google feels that they are mature enough to support their intended use cases, allowing Google to proceed to the step of starting to disable third-party cookies.

Chrome will disable third-party cookies for 1% of users from Q1 2024 to facilitate testing, gradually ramping up to 100% of users from Q3 2024. Reaching the 100% figure depends on Google addressing any remaining competition concerns from the UK's [Competition and Markets Authority](https://www.gov.uk/cma-cases/investigation-into-googles-privacy-sandbox-browser-changes) (CMA).

## [How this affects web developers](https://developer.mozilla.org#how_this_affects_web_developers)

As a result of this change, web developers may well experience higher volumes of users having broken experiences on their web properties, especially if they directly set third-party cookies, or use third-party services that set third-party cookies.

To work around such issues, you are advised to:

1. Audit your third-party cookie usage. Third party cookies have a [`SameSite=None`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#samesitesamesite-value) value set; you should therefore be able to identify them by searching for this setting in your browser DevTools, for example in the [Firefox Storage Inspector](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/) or the [Chrome Application panel](https://developer.chrome.com/docs/devtools/application/cookies/).
2. Test functionality that uses third party cookies for breakage. You can set your browser to block third party cookies in its settings. Chrome 118+ also has a flag, `chrome://flags/#test-third-party-cookie-phaseout`, which when enabled will set Chrome to block third-party cookies and ensure that new functionality and mitigations are active in order to best simulate the state after the phase out.
  - You should validate if your `SameSite=None` cookies are really still needed. It's possible that they could have been marked as such to provide a quick fix in the past.
3. Fix critical functionality that is broken. There are various alternatives that may work for you, for example:
  - Initially at least, you could make your code more resilient so that it provides a less personalized experience when third party cookie data is not available rather than breaking altogether. Follow the principles of [graceful degradation](https://developer.mozilla.org/en-US/docs/Glossary/Graceful_degradation).
  - You could choose to gather such data via alternative means, such as user surveys or quizzes, or looking at data you already have such as product order histories to infer trends.
  - If your third-party cookies are only used across a small number of related, known websites, you could use the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API) and/or [Related Website Sets](https://developer.chrome.com/blog/related-website-sets/) to allow cross-site cookie access only for those specific sites. Storage Access prompts the user to provide permission for a site to use third party cookies on a per-frame basis.
    - If you've already implemented a solution using the Storage Access API for Firefox or Safari then this is a good time to check your implementation against Chrome's behavior, which was updated to provide full support in version 119.
    - Related Website Sets can be considered a progressive enhancement of the Storage Access API: The API can be used in just the same way, but sites in the set will not prompt users for permission to access third party cookies.
  - If your third-party cookies are being used on a 1:1 basis with the top-level sites they are generated on, you could use [Cookies Having Independent Partitioned State (CHIPS)](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Third-party_cookies/Partitioned_cookies), also known as partitioned cookies, to opt your cookies into partitioned storage with a separate cookie jar per top-level site. This only requires adding the `partitioned` attribute to your existing cross-site cookies. They can then be used in an unrestricted fashion, but they can't be shared with other sites. Note that CHIPS is currently Chromium-only.
  - You can start to explore the different features available in Google's Privacy Sandbox project to see if they fit your use case (these are currently Chromium-only). For example:
    - [Federated Credential Management (FedCM) API](https://developer.mozilla.org/en-US/docs/Web/API/FedCM_API): Enables federated identity services allowing users to sign in to sites and services.
    - [Private State Tokens](https://developer.chrome.com/docs/privacy-sandbox/private-state-tokens/): Enables anti-fraud and anti-spam by exchanging limited, non-identifying information across sites.
    - [Topics API](https://developer.chrome.com/docs/privacy-sandbox/topics/overview/): Enables interest-based advertising and content personalization.
    - [Protected Audience API](https://developer.chrome.com/docs/privacy-sandbox/protected-audience/): Enables remarketing and custom audiences.
    - [Attribution Reporting API](https://developer.chrome.com/docs/privacy-sandbox/attribution-reporting/): Enables measurement of ad impressions and conversions.

## [Summary](https://developer.mozilla.org#summary)

Getting rid of third-party cookies from the web has been a long time coming, and the story is not yet finished. However, Chrome's announcement is a big step towards making it happen. You can help â use the resources above to check whether your sites and apps could migrate away from using third-party cookies using the features available today. Spread the word on this to encourage others to do the same. And give browser vendors feedback on what's still missing.

Note: The `developer.chrome.com` article [Preparing for the end of third-party cookies](https://developer.chrome.com/blog/cookie-countdown-2023oct/) has more information about testing from a Chrome point of view, and how to use privacy sandbox technologies to work around your issues.