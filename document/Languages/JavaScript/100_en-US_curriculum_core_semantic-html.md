---
id: "javascript_100"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 100
source_url: "https://developer.mozilla.org/en-US/curriculum/core/semantic-html"
language: "en"
retrieved_at: "2026-11-01 21:54:36"
content_hash: "c626df481143dcff4e7faedbeb5f63dc981d4ba41a9b93e4c2b75fb603895da2"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/curriculum/core/semantic-html

---

HTML is the technology that defines the content and structure of any website. Written properly, it should also define the semantics (meaning) of the content in a machine-readable way, which is vital for accessibility, search engine optimization, and making use of the built-in features browsers provide for content to work optimally. This module covers the basics of the language, before looking at key areas such as document structure, links, lists, images, forms, and more.

The need for a doctype at the top of HTML documents. Its original intended purpose, and the fact that now it is somewhat of a historical artifact.

The need to set the language of a document using the lang attribute in the opening \<html> tag.

The HTML head, and its purpose as a metadata container for the document including key uses:

Setting information like character encoding and title.

Providing metadata for search engines (e.g. \<meta name="description">) and social media platforms (e.g. Open Graph Data), and the Search Engine Optimization (SEO) benefits.

Linking to icons for use on browsers and mobile platforms.

Linking to stylesheets and script files.

The HTML body and its purpose as a container for the page content.

The anatomy of an HTML element â element, opening tag, content, closing tag, attributes.

What void elements (also known as empty elements) are, and how they differ from other elements.

How to create a good document structure with headings and content beneath those headings.

Using semantic HTML rather than presentational HTML:

Some presentational markup should no longer be used at all (e.g. \<big> and \<font>); it is deprecated.

Some presentational markup has been repurposed to have new semantic meaning (e.g. \<i> and \<b>).

It is tempting to just use \<div> elements wherever a block-level container is required, but you should be aware of the other available structural elements and their benefits (such as improved accessibility). Examples include \<main>, \<section>, \<article>, \<header>, \<nav>, and \<footer>.

Notes:

One key point to understand here is the difference between semantic and presentational markup, what these terms mean, and why semantic markup is important to SEO and accessibility.

The need for heading levels to be used logically, i.e. no skipping levels or using them arbitrarily because you want to achieve a certain font size (that's a job for CSS).

SEO benefits: for example, keywords are boosted in headings.

Notes:

This conformance criterium doesn't require that you go too deep into strategies for writing SEO-friendly content, although you should understand what this means.

Accessibility benefits: Assistive technology (AT) such as screen readers use headings and landmarks as signposts to navigate content. HTML documents are very difficult for AT users to use without headings.

Understanding that HTML needs to be correctly nested. If not, the browser has to guess what you meant your structure to be, and it might not be what you wanted.

Validating your markup using the HTML validator or another similar tool (for example, view source in Firefox highlights validation errors with a dotted red underline).

The HTML structure for the three types of lists â unordered, ordered, and description.

Understand that description lists are less commonly used than the other two types, with use cases mainly in areas such as academia and documentation.

The correct usage for each list type.

Notes:

Unordered lists are for marking up a list of items where the order doesn't matter, such as a shopping list.

Ordered lists are for marking up a list of items where the order does matter, such as a set of directions.

Description lists are for associating a list of terms with descriptions of those terms, for example, product names and descriptions in a shopping cart.

The broader use cases of lists, such as navigation menus.

Correct usage of elements for emphasis and importance, such as \<strong> and \<em>.

Understand HTML elements that represent other less common semantic requirements, for example:

Quotations.

Abbreviations and acronyms.

Addresses.

Times and dates.

Superscript and subscript.

HTML entities.

Other text markup features such as \<u>, \<s>, and \<ruby>.

Notes:

It is not necessary to have an exhaustive understanding of all the semantic elements HTML offers at this stage, but you should understand that they exist, and how to look them up using MDN if you need them.

Aside from links, \<button> and form elements are the main tools for building controls for users to interact with your sites.

Notes:

There are a lot of input types and form features not explicitly mentioned here; the purpose is to get a good general introduction to buttons and form elements, and learn the most common cases. The advanced/specialized cases can be studied on a need-to-know basis, as part of a web developer's constant learning throughout their career.

\<button>:

Button types â button, submit, and reset.

Why reset buttons are nearly always a bad idea.

Common \<input> types â text, number, file, checkbox, radio, password, search, and submit.

Make sure to understand that client-side form validation is really a usability enhancement, to be used alongside server-side form validation. It is not a substitute for it.

Making forms accessible â Correct semantics, \<label>, and the for attribute.

Notes:

Going back to the argument for semantic HTML (see also 2.2 Good document structure), you should understand why it is important to use the right element for the right job. For example, use a \<button> to submit your form, and not a \<div> programmed to behave like a \<button>.

Understand the features programmed into \<button>s and form elements by the browser by default, and how important they are. Examples include keyboard accessibility, focus outlines, and semantic meaning for AT to identify the elements and communicate their meaning.

Form states and why they are important â :focus, :readonly, :disabled, etc.

\<textarea>.

\<select> and \<option>.

\<form> elements:

Form submission: what happens when a form is submitted.

The difference between submission methods â GET, POST, etc.