---
id: "javascript_099"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 99
source_url: "https://developer.mozilla.org/en-US/curriculum/core/javascript-fundamentals"
language: "en"
retrieved_at: "2026-11-01 21:54:34"
content_hash: "03162fbad16ee25bb0b151a6ceb9a0c9fab9b5643ba65e5386bda4950082eabc"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/curriculum/core/javascript-fundamentals

---

JavaScript is a huge topic, with so many different features, styles, and techniques to learn, and so many APIs and tools built on top of it. This module focuses mostly on the essentials of the core language, plus some key surrounding topics â learning these topics will give you a solid basis to work from.

Understand the purpose of loops â a code structure that allows you to do something very similar many times without repeating the same code for each iteration.

Basic for loops.

Looping through collections with for ... of.

Notes:

There are many other types of loop in JavaScript that we haven't listed here. It is not necessary (or useful) to understand all of them at this stage. For now, students need to understand the purpose of loops, and the most common types.

Understand what the DOM is â the browser's internal representation of the document's HTML structure as a hierarchy of objects, which can be manipulated using JavaScript.

Understand the important parts of a web browser and how they are represented in JavaScript â Navigator, Window, and Document.

Understand how DOM nodes exist relative to each other in the DOM tree â root, parent, child, sibling, and descendant.

Getting references to DOM nodes, for example with querySelector() and getElementById().

Creating new nodes, for example with innerHTML() and createElement().

Adding and removing nodes to the DOM with appendChild() and removeChild().

Adding attributes with setAttribute().

Manipulating styles with Element.style.\* and Element.classList.\*.

Understand what third-party code is â functionality written by someone else that you can use in your own project, so you don't have to write everything yourself.

Why developers use third-party code:

Efficiency and productivity: A huge amount of complex functionality is already written for you to use, created in a way that enforces efficient, modular code organization.

Compatibility: Reputable framework code is already optimized to work across browsers/devices, for performance, etc. Many frameworks also have systems to output to specific platforms (e.g. Android or iOS) as build targets.

Support/ecosystem: Popular frameworks have vibrant communities and help resources to provide support, and rich systems of extensions/plugins to add functionality.

The difference between libraries and frameworks:

A library tends to be a single code component that offers a solution to a specific problem, which you can integrate into your own app (for example, chart.js for creating \<canvas>-based charts, or three.js for simplified 3D GPU-based graphics rendering), whereas a framework tends to be a more expansive architecture made up of multiple components for building complete applications.

A library tends to be unopinionated about how you work with it in your codebase, whereas a framework tends to enforce a specific coding style and control flow.

Why should you use frameworks?

They can provide a lot of functionality and save you a lot of time.

A lot of companies use popular frameworks such as React or Angular to write their applications, therefore a lot of jobs list frameworks as requirements for applicants to have.

Why is a framework not always the right choice? A framework:

Can easily be overkill for a small project â you might be better off writing a few lines of vanilla JavaScript to solve the problem or using a tailored library.

Usually adds a lot of JavaScript to the initial download of your application, leading to an initial performance hit and possible usability issues.

Usually comes with its own set of custom syntax and conventions, which can introduce a significant additional learning curve to the project.

May be incompatible with an existing codebase because of its architecture choice.

Will need to be updated regularly, possibly leading to extra maintenance overhead for your application.

May introduce significant accessibility issues for people using assistive technologies because of its architecture (for example, SPA-style client-side routing), which will need to be considered carefully.

How to choose? A good library or framework must:

Solve your problems while offering advantages that significantly outweigh any negatives that it brings to the table.

Have good support and a friendly community.

Be actively maintained â don't choose a codebase that has not been updated for over a year, or has no users.