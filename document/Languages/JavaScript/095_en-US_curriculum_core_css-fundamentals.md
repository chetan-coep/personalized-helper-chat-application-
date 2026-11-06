---
id: "javascript_095"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 95
source_url: "https://developer.mozilla.org/en-US/curriculum/core/css-fundamentals"
language: "en"
retrieved_at: "2026-11-01 21:54:27"
content_hash: "640f05a73e06cb2bcc3c5f835640adb75a30b4eb276936f20ff33592c6dba5cf"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/curriculum/core/css-fundamentals

---

CSS enables you to add style to your web pages including color, text, positioning and layout, and animation. In our first CSS module, we cover all the fundamental language mechanics you need to understand how CSS works.

The purpose of CSS â style, layout, and provide other visual enhancements to web pages (such as animation).

Key CSS syntax:

Rules.

Selectors.

Declarations.

Properties (including custom properties).

Values (including shorthand values).

At-rules and descriptors.

Default browser styles â understand that the browser provides default CSS styling to HTML elements so that it is in some way usable even with no user-defined styles at all:

Understand also therefore that HTML has nothing to do with styling.

Use this to reinforce the idea of separating semantics and structure (semantic HTML) from presentation (CSS), and not using presentational markup.

Study CSS resets, first to prove that browser styles exist and show what a page looks like when they are removed, but also as a technique for providing a blank canvas for developers to build styles on top of.

Applying CSS to an HTML document â inline styles, internal stylesheets, external stylesheets:

Why external stylesheets are usually the best option.

IDs are unique per document â you should use an ID to select one specific element.

You can have multiple classes per element, and these can be used to layer on styles as required.

IDs and classes should be used sparingly where they make sense for selections, but you shouldn't use them for everything â keep your HTML as clean and uncluttered as possible.

Basic styling of easy-to-style form elements, like \<input type="text">.

Using CSS resets to overcome \<input> font styling inheritance and box styling default differences.

Understand that not all form elements are easy to style, and why:

System styles are applied to some form elements, making consistent styling difficult across browsers.

More complex form elements have internal (shadow DOM) elements that define the structure of their inner workings. These are often impossible to access and style individually.

Using appearance: none to work around system styling for \<input> types like search, checkbox, and radio.

Mitigating issues with difficult-to-style types such as datetime-local, color, etc.

Notes:

Conforming to this curriculum module doesn't require having foolproof, conclusive answers to every possible form styling problem. Some form elements are difficult to style, as the resources make clear. However, you should at least be able to handle a wide range of form styling needs and understand the issues around some of the more difficult styling issues.

Use the HTML validator to see if you have any invalid markup on your page â this could be causing your CSS to not apply as desired.

Use the CSS validator to check for badly-formed CSS code. A missing semi-colon can cause a whole section of CSS declarations to not apply.

Use browser developer tools to inspect the CSS that is applied to HTML elements on a page.

Modify the applied CSS to figure out what changes are needed to get what you want. This includes enabling and disabling declarations, modifying values, and adding new declarations.

Use layout inspection tools to inspect the box model, grids, flexbox, and other layout features (see also CSS Layout).