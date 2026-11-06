---
id: "javascript_094"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 94
source_url: "https://developer.mozilla.org/en-US/curriculum/core/accessibility"
language: "en"
retrieved_at: "2026-11-01 21:54:25"
content_hash: "36d957bb8715c60518f7c2f3c61695598154d5556dc16fea661262707c311701"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/curriculum/core/accessibility

---

Access to web content such as public services, education, e-commerce sites, and entertainment is a human right. No one should be excluded based on disability, race, geography, or other human characteristics. This module discusses the best practices and techniques you should learn to make your websites as accessible as possible.

Understand the point of accessibility â increased usability for everyone, better SEO, and a wider target audience. Also, be aware of the legal requirements.

Understand that accessibility should be considered from the start of a project, and not bolted on at the end.

Understand the Web Content Accessibility Guidelines (WCAG) conformance criteria.

Use semantic HTML, aka "The right element for the right job", because the browser provides so many built-in accessibility hooks. Good examples are \<a> and \<input> elements.

Mobile browsers that provide specific usability advantages for specific \<input> types such as number or tel.

Making tables accessible with \<th>, \<thead>, \<tbody>, \<tfoot>, \<caption>, and the scope attribute (See also 2.8 HTML tables).

Using simple plain language, steering clear of slang and abbreviations where possible, and providing definitions where it is not possible.

Understand the purpose of audio transcripts and text tracks (captions, subtitles, etc.) in making audio and video content accessible (we are not expecting mastery in creating them; that is an advanced topic in its own right).

Keyboard accessibility:

Understand why apps need to be keyboard accessible â many people have difficulty using a mouse or other pointing device.

Understand built-in browser keyboard controls.

Understand when accesskey and tabindex are appropriate to use.

Sensible animation usage â use animation subtly and provide controls to turn it off:

Consider the needs of those with certain cognitive disabilities.

The prefers-reduced-motion media query was created specifically to help with this.

Best practices for hiding content so that it doesn't become inaccessible. For example, display: none makes content unreadable by screen readers, so it needs to be used carefully.

Understand that there is such a thing as too much JavaScript. A simpler approach is usually more accessible, and often better for everyone.

Understand the value of unobtrusive JavaScript:

If possible, use JavaScript as a usability enhancement, which isn't essential for the app to function.

A good example is client-side validation of form inputs.

Use events sensibly so you don't lock out specific control types. For example, mouse-specific events such as mouseover and mouseout could lock out keyboard or touchscreen users.

Screen readers and other assistive technology (AT) types:

What they are used for, and who uses them.

The aim here is not to master the usage of all assistive technology types (there are many that we have not listed below), but to be aware of their existence and the types of people who use them, and also to appreciate how and why accessibility best practices work.

It is also a good idea for web developers to use screen readers or other types of assistive technology, to get an idea of what the web experience is like for users of those technologies.

The importance of source order.

The accessibility layer in browsers, and how assistive technologies hook into it.

Setting up screen readers and using them to test websites on desktop and mobile.

Other assistive technology such as:

Large text or braille keyboards.

Alternative pointing devices such as trackballs, joysticks, and touchpads.

Understand the purpose of WAI-ARIA â to provide semantics to otherwise non-semantic HTML, so that AT users can make sense of the interfaces being presented to them:

The first rule of ARIA: "If you can use a native HTML element or attribute with the semantics and behavior you require already built in, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, then do so."

In other words, using semantic HTML is an ideal, which is not possible at all times. WAI-ARIA is a bridging technology for such cases.

The basic syntax â roles, properties, and states.

Landmarks and signposting.

Enhancing keyboard accessibility.

Announcing dynamic content updates with live regions.