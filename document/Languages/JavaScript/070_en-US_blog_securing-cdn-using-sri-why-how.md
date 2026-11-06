---
id: "javascript_070"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 70
source_url: "https://developer.mozilla.org/en-US/blog/securing-cdn-using-sri-why-how"
language: "en"
retrieved_at: "2026-11-01 21:53:42"
content_hash: "ccb0b3062a1d25518850489370909d6b5c4c3419a2d62384e0bd217cb6a1fa37"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/securing-cdn-using-sri-why-how

---

# Securing your CDN: Why and how should you use SRI

It has never been easier to use a third-party JavaScript library or an external CSS on your website. All you need to do is include `<script src="https://example.com/whatever.js">` in the `<head>` section of your HTML and you're done, right? Found some cool looking CSS? Make it part of your site with `<link rel="stylesheet" href="...">`.

What could possibly go wrong? A lot, as it turns out. In this post, I'll explain the security implications of adding third-party resources and how you can protect both your site and its users.

## [Problems with relying on your CDN](https://developer.mozilla.org#problems_with_relying_on_your_cdn)

A Content Delivery Network ([CDN](https://developer.mozilla.org/en-US/docs/Glossary/CDN)) is a group of servers, usually spread out around the world, which help accelerate content on your site. Instead of including a popular library on your server, you can tell your visitors to load it from the CDN server nearest to them. This speeds up your page.

However, there's a flipside. When you load services from outside your website, you are giving someone else complete control over your site! You may think that all you're doing is importing some impressive JavaScript to display sparkles whenever anyone clicks on the links on your website - but that library could be taken over by someone malicious. If that happens, visitors to your site could be hijacked. If the CSS is taken over, your visitors could be subject to all sorts of horrible images.

How can you save yourself from such a tragedy?

## [What is SRI and how can it solve this problem](https://developer.mozilla.org#what_is_sri_and_how_can_it_solve_this_problem)

This is why SubResource Integrity was invented. It's a bit of a mouthful, so we'll call it SRI for short. SRI allows you to say "I want exactly this specific version of the imported code and if even a single byte of it changes, don't run it."

When you use SRI, you're protecting your site and your users from compromised code. Even if a person with malicious intentions hacks the server hosting the third-party code, they will **not** be able to take over your site. Pretty cool, huh?

## [How to use SRI](https://developer.mozilla.org#how_to_use_sri)

Let's take a look at how SRI works. Imagine that you want to include jQuery on your site. Here's the SRI code that you can use:

```
<script
  src="https://code.jquery.com/jquery-3.7.0.slim.min.js"
  integrity="sha256-tG5mcZUtJsZvyKAxYLVXrmjKBVLd6VpVccqz/r4ypFE="
  crossorigin="anonymous"></script>
```
And for CSS, it is pretty similar:

```
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/picnic"
  integrity="sha384-v1z6igsPTyRDbi5o+gRfebiF45laQTyfvucMlEmzfyalawh17iTvBbICU08I7ksb"
  crossorigin="anonymous" />
```
As you'll notice, there are two new attributes compared to a normal `<script>` or `<link>` element. These are `crossorigin` and `integrity`.

The [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin) attribute is the easier one to explain. This attribute tells your browser to anonymously request the resource from the server. No username, password, or other identifying information is sent to the server.

The `integrity` attribute is slightly more complicated. It contains a mathematical representation - called a "hash" - of the code you are requesting. The first part `sha384` says that the algorithm being used is SHA384. This tells the browser to use that algorithm to analyze the code being requested. That will generate a long string of characters. If the code on the remote website changes, the SHA384 function will produce a hash that will **not** match the second part of the `integrity` value.

In short, if the code on the remote server has changed, your browser will refuse to run it.

## [How to get the SRI hash](https://developer.mozilla.org#how_to_get_the_sri_hash)

Most libraries will tell you what the SRI hash is, and you can just copy and paste it.
If a site doesn't tell you the hash, you can calculate it yourself. The easiest way is to use the [SRI Hash Generator](https://www.srihash.org/). Paste in the URl to the code, and it will quickly spit out the hash for you to use.

## [Limitations of using SRI](https://developer.mozilla.org#limitations_of_using_sri)

Of course, using SRI does come with some downsides. Because the SHA384 hash demands that the original file remains unchanged, you must specify the version of the file you want. It is impossible to use SRI and always have the latest version of a library. You have to make a choice â keep your site safe or always have the latest features.

And what happens if a remote site is compromised and a malicious file replaces the library you were using? The browser will refuse to run it. Does your site work if a critical JavaScript library is unavailable? If not, your users will be faced with a broken website. That's probably better than a malicious website that compromises your users. But you should use [progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement) to make sure your site will work even if JavaScript and CSS are missing.

Thankfully, SRI has been available in all modern web browsers since 2016. Older browsers will ignore the `crossorigin` and `integrity` attributes, which may leave users of older browsers at risk if the libraries you use are compromised.

## [Summary](https://developer.mozilla.org#summary)

SRI is the best defense you have against third-party JavaScript and CSS being compromised. It's fairly easy to use, but if something does go wrong, you'll need to make sure your site works without external resources.

I hope you enjoyed reading the post and exploring the examples. Feel free to leave your feedback, thoughts, or questions on [Discord](https://developer.mozilla.org/discord) or on [GitHub](https://github.com/orgs/mdn/discussions/categories/the-mdn-web-docs-blog).

## [Useful resources](https://developer.mozilla.org#useful_resources)

- [Subresource integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity) on MDN
- [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) on MDN
- [Digital signature](https://developer.mozilla.org/en-US/docs/Glossary/Signature/Security) on MDN
- [How hashing works](https://en.wikipedia.org/wiki/Hash_function) on Wikipedia