---
id: "typescript_001"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - Introduction"
doc_order: 1
source_url: "https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html"
language: "en"
retrieved_at: "2026-11-03 17:56:22"
content_hash: "fa0bdeff29e74def592e97549b968eace0ae9fb434c3322aea66117af74334f7"
---

# TypeScript: Documentation - Introduction

Source: https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html

---

The Declaration Files section is designed to teach you how to write a high-quality TypeScript Declaration File. We need to assume basic familiarity with the TypeScript language in order to get started.

If you haven’t already, you should read the [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/basic-types.html)
to familiarize yourself with basic concepts, especially types and modules.

The most common case for learning how .d.ts files work is that you’re typing an npm package with no types.
In that case, you can jump straight to [Modules .d.ts](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html).

The Declaration Files section is broken down into the following sections.

We are often faced with writing a declaration file when we only have examples of the underlying library to guide us.
The [Declaration Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html) section shows many common API patterns and how to write declarations for each of them.
This guide is aimed at the TypeScript novice who may not yet be familiar with every language construct in TypeScript.

The [Library Structures](https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html) guide helps you understand common library formats and how to write a proper declaration file for each format.
If you’re editing an existing file, you probably don’t need to read this section.
Authors of new declaration files are strongly encouraged to read this section to properly understand how the format of the library influences the writing of the declaration file.

In the Template section you’ll find a number of declaration files that serve as a useful starting point when writing a new file. If you already know what your structure is, see the d.ts Template section in the sidebar.

Many common mistakes in declaration files can be easily avoided.
The [Do’s and Don’ts](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html) section identifies common errors,
describes how to detect them,
and how to fix them.
Everyone should read this section to help themselves avoid common mistakes.

For seasoned authors interested in the underlying mechanics of how declaration files work,
the [Deep Dive](https://www.typescriptlang.org/docs/handbook/declaration-files/deep-dive.html) section explains many advanced concepts in declaration writing,
and shows how to leverage these concepts to create cleaner and more intuitive declaration files.

The [Publishing](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html) section explains how to publish your declaration files to an npm package, and shows how to manage your dependent packages.

For JavaScript library users, the [Consumption](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html) section offers a few simple steps to locate and install corresponding declaration files.