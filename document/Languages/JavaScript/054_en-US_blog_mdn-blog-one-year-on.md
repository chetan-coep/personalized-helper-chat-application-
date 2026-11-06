---
id: "javascript_054"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 54
source_url: "https://developer.mozilla.org/en-US/blog/mdn-blog-one-year-on"
language: "en"
retrieved_at: "2026-11-01 21:53:06"
content_hash: "945d036a0bcfd0ef238210f4393261b4fd0a124dc8ce8c0dc803ca5a18ff82a3"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/mdn-blog-one-year-on

---

# A year of publishing the MDN Blog

When we [launched the MDN Blog in May 2023](https://developer.mozilla.org/en-US/blog/welcome-to-the-MDN-blog/), we were excited and curious to see what our readers would think and how the blog would look like one year on.
We're thrilled to see that there's a wonderful variety of articles from the MDN team, guests, and partners that we think help developers build for the web.

We launched the blog with the intention of having a channel that's separate from our usual reference docs where we could experiment more with the format of the content. We also decided to include content sponsored by partners and contributions from guest authors, focusing on web development topics, especially about features that are new or just around the corner. We also wanted to have a place to announce interesting developments on the MDN platform, and share features we're working on and shipping.

A year later is a perfect milestone to look back over highlights from articles we've published and see what we've achieved together. Let's have a look at what we've published, some numbers on our highest-visited articles, who we partnered with for sponsored content, picks from our guest authors, and other updates from the team.

## [What's published on the MDN blog](https://developer.mozilla.org#whats_published_on_the_mdn_blog)

We published 38 articles in total, and it breaks down to the following categories:

There is an overlap between these categories, so this chart presents a general overview of the content we've published. We're posting a lot of news, such as summaries of the latest content added to MDN, announcements of new features added to the MDN website, and updates on what's coming soon to the web platform and MDN itself.

DevOps might be a surprising category for some, but it is an excellent way to describe some of our articles, which guide people in testing and deploying their projects and moving from a collection of files on their machines to a working, maintainable, and scalable web application.

## [Our most-read posts](https://developer.mozilla.org#our_most-read_posts)

Let's take a look at the most popular content overall. Here's our most viewed articles, ordered by number of visits:

JavaScript regex tops our list, and it proves to be a tricky subject for readers to master, whether or not you've `HADC0FFEE`:

```
function isHexadecimal(str) {
  return /^[0-9A-F]+$/i.test(str);
}
isHexadecimal("HADC0FFEE"); // false
```
We're happy to note that accessibility is one of the most-read topics. Having the landmark roles article high up on our list shows that readers are interested in this area, which is a win for designing and promoting accessible web experiences.

```
<aside aria-labelledby="pizza-recipe-heading">
  <h3 id="pizza-recipe-heading">Make your own pie!</h3>
  <p>Below is a list of our favorite pizza recipes.</p>
  <ul>
    <li><a href="/mushroom-pizza">The shroom</a></li>
    <li><a href="/smokey-joe">Smokey Joe</a></li>
    <li><a href="/fromage">Fromage</a></li>
  </ul>
</aside>
```
A lot has happened in the CSS domain over the last year, and our top-five list would certainly not be complete without a CSS topic. What could be better than CSS-driven animations with inspiring examples?

```
.progress {
  height: 1rem;
  background: blue;
  transform-origin: 0 50%;
  animation: scaleProgress auto linear forwards;
  animation-timeline: scroll(root);
}
@keyframes scaleProgress {
  0% {
    transform: scaleX(0);
  }
  100% {
    transform: scaleX(1);
  }
}
```
It's no surprise that JavaScript, CSS, and HTML each have a spot in the most-read posts, as these are the main technology categories that we document on MDN. Our other two posts in the top five are announcements about new functionality shipping on the MDN platform, showing that our readers are interested in finding out what's happening on MDN and the ways that we're continuously improving the site.

## [Guest posts](https://developer.mozilla.org#guest_posts)

We've published seven guest posts, by [Terence Eden](https://shkspr.mobi/blog/), [Michelle Barker](https://css-irl.info/), and [Chris Mills](https://millsdocs.com/), who have written about security, performance, web sustainability, and CSS topics such as container queries, scroll-driven animations, and more.
Here's a few highlights from our guest writers:

- [Saying goodbye to third-party cookies in 2024](https://developer.mozilla.org/en-US/blog/goodbye-third-party-cookies/) by Chris Mills
- [Getting started with CSS container queries](https://developer.mozilla.org/en-US/blog/getting-started-with-css-container-queries/) by Michelle Barker
- [Securing your CDN: Why and how should you use SRI](https://developer.mozilla.org/en-US/blog/securing-cdn-using-sri-why-how/) by Terence Eden

Guest posts like these are a way to not only spread the word about web platform updates, but to promote and demystify techniques that help developers make applications and web pages more secure. This snippet from the SRI post is a great example that prevents the browser from running a script if the SHA-256 hash doesn't match what we expect it to be:

```
<script
  src="https://code.jquery.com/jquery-3.7.0.slim.min.js"
  integrity="sha256-tG5mcZUtJsZvyKAxYLVXrmjKBVLd6VpVccqz/r4ypFE="
  crossorigin="anonymous"></script>
```
We hope that by providing practical hints like the one above, we can propagate better practices and push the web to be a more secure place for developers and everyone who uses their applications.

## [Sponsored content](https://developer.mozilla.org#sponsored_content)

In 2023, [GitLab](https://gitlab.com), [TestGrid](https://testgrid.io/), and [Vultr](https://www.vultr.com/) choose the MDN Blog as a medium to post developer-facing sponsored content.
Together with our partners, we've put a lot of effort into making sure the content is educational, helpful, and timely for web developers, while also bringing value to companies who see our readers as a perfect audience for their products and services.
Here's a selection of posts from our partners:

- [Optimizing DevSecOps workflows with GitLab's conditional CI/CD pipelines](https://developer.mozilla.org/en-US/blog/optimizing-devsecops-workflows-with-gitlab-conditional-ci-cd-pipelines/)
- [Leveraging Bun on Vultr: A superior Node.js alternative](https://developer.mozilla.org/en-US/blog/leveraging-bun-on-vultr-a-superior-node-js-alternative/)
- [Modernizing conventional test automation with TestGrid](https://developer.mozilla.org/en-US/blog/modernizing-test-automation-with-test-grid/)

We're happy to be able to share high-quality resources that our readers find educational and practical, like the potential performance benefits of using Bun as a Node.js alternative:

```
Bun.serve({
  fetch(req) {
    return new Response("Bun!");
  },
});
```
## [MDN team updates](https://developer.mozilla.org#mdn_team_updates)

Of course, we're also happy to share what we're working on at MDN, from documentation projects to platform features and functionality. This is a short list of highlights from the MDN team:

- [Introducing Baseline: a unified view of stable web features](https://developer.mozilla.org/en-US/blog/baseline-unified-view-stable-web-features/)
- [Introducing the MDN Playground: Bring your code to life!](https://developer.mozilla.org/en-US/blog/introducing-the-mdn-playground/)
- [Introducing AI Help (Beta): Your Companion for Web Development](https://developer.mozilla.org/en-US/blog/introducing-ai-help/)
- [Lift-off: The MDN Curriculum launch](https://developer.mozilla.org/en-US/blog/mdn-curriculum-launch/)

Baseline has really resonated with a lot of developers, helping them quickly determine whether features have stable browser support. We're very curious to see how the project grows in the future:

We're also thrilled about the feedback we've received about the [MDN Curriculum](https://developer.mozilla.org/en-US/curriculum/).
We're glad that people getting started in web development are as excited about using this carefully curated learning resource as we are about publishing and maintaining it.

## [Thanks for reading](https://developer.mozilla.org#thanks_for_reading)

That's a wrap for our 'year in review' post.
We want to thank all of our readers and community for the support, feedback, and engagement you've provided. Thank you for reading!
We're looking forward to hearing your thoughts on what you'd like to see more of in the future.
Feel free to [get in touch with us](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels) and let us know what you think!