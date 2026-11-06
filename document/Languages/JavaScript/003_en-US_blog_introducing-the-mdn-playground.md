---
id: "javascript_003"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 3
source_url: "https://developer.mozilla.org/en-US/blog/introducing-the-mdn-playground"
language: "en"
retrieved_at: "2026-11-01 21:52:46"
content_hash: "3282a16b0dc7e64dd5584fd0b075e28c22b84c27b0a6c881fbd06634e3660185"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/introducing-the-mdn-playground

---

# Introducing the MDN Playground: Bring your code to life!

At Mozilla, we are constantly striving to empower web developers and provide them with the best resources to create amazing experiences on the web. Today, we are thrilled to announce a groundbreaking addition to MDN â the MDN Playground! (Yeah, you got me, maybe this sounds a bit too exciting).

## [What is the MDN Playground?](https://developer.mozilla.org#what_is_the_mdn_playground)

The MDN Playground is pretty much what you expect it to be â a simple way to preview HTML, CSS, and JavaScript. For now it covers most of the basics; like basic autocomplete, formatting with the one and only [prettier](https://prettier.io/), and the option to share your amazing work (given you're [logged in](https://developer.mozilla.org/users/fxa/login/authenticate/?next=%2Fen-US%2Fblog%2Fintroducing-the-mdn-playground%2F)).

## [Why the MDN Playground?](https://developer.mozilla.org#why_the_mdn_playground)

This is a good question. There are plenty of playgrounds around, so why another one? Well, in theory, a playground is not that complicated to build (big [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em) on *theory* here) and we wanted it integrated with MDN. So we thought why not write one, *famous last words*.

Jokes aside, the idea of having a playground on MDN had been floating around forever. Having interactive examples in our articles was a great start, but some things need more space and more freedom. Sharing your ideas and solutions is key and this should not be a third party experience. But one thing that felt like a small game changer was the integration with our existing [live samples](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Page_structures/Code_examples#traditional_live_samples).

You can now break out any existing live sample on MDN into the Playground (look for that little `Play` button above the live samples). This empowers you to make some changes to the code you just read, which helps to better understand what's going on or to send a customized version to your friends. Don't get lost there yet, but check out this [random animation example](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations#mouse_following_animation) that you can now remix.

```
<h1>Hello MDN Playground</h1>
```
I hope this somehow covers the why. This will allow us to unify how we display and interact with code, [interactive examples](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Page_structures/Code_examples#interactive_examples) being next on the list.

## [Key features of the MDN Playground](https://developer.mozilla.org#key_features_of_the_mdn_playground)

Some product features, pretty much true but really trying to sell this (so take it with a grain of ð§):

### [Instant prototyping](https://developer.mozilla.org#instant_prototyping)

The MDN Playground offers a hassle-free way to quickly prototype and test your ideas. Simply write or paste your HTML, CSS, and JavaScript code into the playground, and see the results instantly rendered in the preview area. Whether you're working on a small tweak or building a complex web application, the playground provides a space tailored to your needs.

### [Live interaction](https://developer.mozilla.org#live_interaction)

In addition to static code examples, the MDN Playground brings code to life by enabling interactivity. You can interact with your code in real time, making changes and observing their effects right away. This dynamic feedback loop allows for rapid iteration and a deeper understanding of how different code snippets behave.

### [Expanded code examples](https://developer.mozilla.org#expanded_code_examples)

We know how frustrating it can be to read code examples in documentation and not be able to experiment with them immediately. With the MDN Playground, this problem will become a thing of the past. Whenever you come across a code example on MDN, you'll now find a convenient `Play` button. Clicking it will open the example in the MDN Playground, ready for you to explore and modify.

### [Collaborative capabilities](https://developer.mozilla.org#collaborative_capabilities)

The MDN Playground also supports collaboration, making it easier than ever to work with colleagues or seek help from the community. You can share your code playgrounds with others, allowing them to view and remix your code. Whether you're collaborating on a project or receiving feedback on your code, the playground fosters a collaborative environment for developers worldwide.

## [How to access the MDN Playground](https://developer.mozilla.org#how_to_access_the_mdn_playground)

To start using the MDN Playground, simply visit [developer.mozilla.org/en-US/play](https://developer.mozilla.org/en-US/play) and dive into the world of interactive web development. The playground is accessible on all modern web browsers, and it's completely free to use.

## [Join the community](https://developer.mozilla.org#join_the_community)

The MDN Playground is not just a tool, it's a community-driven initiative. We encourage you to join our vibrant community of developers, where you can share your experiences, learn from others, and contribute to the evolution of the playground. Together, we can shape the future of web development and make it more accessible to everyone.

## [Conclusion](https://developer.mozilla.org#conclusion)

The MDN Playground marks a significant milestone in our continuous effort to empower developers with the best tools and resources. With its seamless integration into MDN Web Docs, instant prototyping capabilities, live interaction, and collaborative features, the playground is set to revolutionize the way you experiment with code.

We invite you to explore the MDN Playground today and unlock a new level of creativity and productivity in your web development journey. Let's build the web of tomorrow, together!

Happy coding! (Keep reading if you want to know [how this works](https://developer.mozilla.org/#under_the_hood)).

## [Demos](https://developer.mozilla.org#demos)

>
  ### [Spinning Firefox](https://developer.mozilla.org#spinning_firefox)

```
<div class="scene">
  <div class="cube">
    <div class="face front"></div>
    <div class="face back"></div>
    <div class="face right"></div>
    <div class="face left"></div>
    <div class="face top"></div>
    <div class="face bottom"></div>
  </div>
</div>
```
### [A keyboard](https://developer.mozilla.org#a_keyboard)

```
<div id="synth">
  <div class="keyboard">
    <div class="key white" data-note="C"></div>
    <div class="key black" data-note="C#"></div>
    <div class="key white" data-note="D"></div>
    <div class="key black" data-note="D#"></div>
    <div class="key white" data-note="E"></div>
    <div class="key white" data-note="F"></div>
    <div class="key black" data-note="F#"></div>
    <div class="key white" data-note="G"></div>
    <div class="key black" data-note="G#"></div>
    <div class="key white" data-note="A"></div>
    <div class="key black" data-note="A#"></div>
    <div class="key white" data-note="B"></div>
  </div>
</div>
```
## [Under the hood](https://developer.mozilla.org#under_the_hood)

>
  ### [Editing](https://developer.mozilla.org#editing)

We decided to go with [CodeMirror](https://codemirror.net/) for editing. As they phrase it:

CodeMirror is a code editor component for the web. It can be used in websites to implement a text input field with support for many editing features, and has a rich programming interface to allow further extension.


We considered [Monaco](https://microsoft.github.io/monaco-editor/), but decided for a more lightweight approach. So far it feels like the right choice, let's wait for [feedback](https://survey.alchemer.com/s3/7402374/MDN-Playground-What-s-next).

### [Running and communicating](https://developer.mozilla.org#running_and_communicating)

A simple [`runner.html`](https://github.com/mdn/yari/blob/main/client/public/runner.html) in an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe). There's a bit more to it. The [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe) is pointed to `<random-uuid>.mdnplay.dev` so we isolate all instances. The [`runner.html`](https://github.com/mdn/yari/blob/main/client/public/runner.html) gets the code to execute via [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) from MDN. It doesn't do too much. Given a code object called `state` like `{ html: "some HTML", css: "some CSS", js: "some JavaScript" }` that's what's happening:

```
// Add CSS via a style tag to head
const style = document.createElement("style");
style.textContent = state.css;
document.head.appendChild(style);
// Setting HTML to the body.
// This could just be document.body.innerHTML = state.html
// But this won't execute script tags (which we want).
setHTML(document.body, state.html);
// Add JavaScript via script tag to the body
const script = document.createElement("script");
script.textContent = state.js;
document.body.appendChild(script);
dispatchEvent(new Event("load"));
```
Read through the [`runner.html`](https://github.com/mdn/yari/blob/main/client/public/runner.html) if you want to get into the details.

### [Sharing and formatting](https://developer.mozilla.org#sharing_and_formatting)

Sharing your playground can be done either via using the *copy markdown to clipboard* button, which makes it easy to include the playground code in an MDN article or add it to an GitHub issue. If you want to share more than just the plain code and enable people to preview and interact you can create a permalink to a playground (you need to be [logged in](https://developer.mozilla.org/users/fxa/login/authenticate/?next=%2Fen-US%2Fblog%2Fintroducing-the-mdn-playground%2F)). *If you receive a shared playground and the content is malicious or inappropriate you can flag the playground and we'll take care of it*.

Formatting is basic but good. We just let [prettier](https://prettier.io/) do the work and have the opinions. It's up to you to press the button, so if you prefer a nice minified one liner for your code, be our guest.

### [Breaking out live samples](https://developer.mozilla.org#breaking_out_live_samples)

We're still looking for the best wording here, *move to playground*, *expand to...*, and so on. We'll see. It's not that important what we call it. While working on the playground, I found it to be really useful; it changed how I use MDN for my daily work.

Earlier, *live samples* were built during deployment. Let's not go into the details but it was ugly, and unfortunately it still is. To support the current live samples we scrape the page to find the correct code pieces and glue them together. In a brave new world this would look like:

```
<pre class="html live-sample___breaking">
  <h1>Breaking the internet!</h1>
</pre>
<pre id="output"></pre>
```
```
function getCode(cls) {
  const code = {};
  document.querySelectorAll(`pre.live-sample___${cls}`).forEach((pre) => {
    let lang = getLanguage(pre);
    if (lang === null) {
      return;
    }
    code[lang] = (code[lang] || "") + pre.textContent;
  });
  return code;
}
```
So once we have the code, we just send it to the iframe as mentioned or put it into [sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) and send users to the playground via the `Play` button.

## [What's next](https://developer.mozilla.org#whats_next)

Well, to some degree that's up to you. To tell us what you want to see, you can [provide feedback in our survey](https://survey.alchemer.com/s3/7402374/MDN-Playground-What-s-next).