---
id: "typescript_011"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - Library Structures"
doc_order: 11
source_url: "https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html"
language: "en"
retrieved_at: "2026-11-03 17:56:33"
content_hash: "288caf42634d5aba2bd0466554ec2f4c2c46d3804eba346e484141807c5a3230"
---

# TypeScript: Documentation - Library Structures

Source: https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html

---

Broadly speaking, the way you *structure* your declaration file depends on how the library is consumed.
There are many ways of offering a library for consumption in JavaScript, and you’ll need to write your declaration file to match it.
This guide covers how to identify common library patterns, and how to write declaration files which correspond to that pattern.

Each type of major library structuring pattern has a corresponding file in the [Templates](https://www.typescriptlang.org/docs/handbook/declaration-files/templates.html) section.
You can start with these templates to help you get going faster.

First, we’ll review the kinds of libraries TypeScript declaration files can represent.
We’ll briefly show how each kind of library is *used*, how it is *written*, and list some example libraries from the real world.

Identifying the structure of a library is the first step in writing its declaration file.
We’ll give hints on how to identify structure both based on its *usage* and its *code*.
Depending on the library’s documentation and organization, one might be easier than the other.
We recommend using whichever is more comfortable to you.

Question to ask yourself while looking at a library you are trying to type.

1. How do you obtain the library? For example, can you *only* get it through npm or only from a CDN?
2. How would you import it? Does it add a global object? Does it use `require` or `import`/`export` statements?

Almost every modern Node.js library falls into the module family.
These type of libraries only work in a JS environment with a module loader.
For example, `express` only works in Node.js and must be loaded using the CommonJS `require` function.

ECMAScript 2015 (also known as ES2015, ECMAScript 6, and ES6), CommonJS, and RequireJS have similar notions of *importing* a *module*.
In JavaScript CommonJS (Node.js), for example, you would write

js

In TypeScript or ES6, the `import` keyword serves the same purpose:

ts

You’ll typically see modular libraries include one of these lines in their documentation:

js

or

js

As with global modules, you might see these examples in the documentation of [a UMD](https://www.typescriptlang.org#umd) module, so be sure to check the code or documentation.

Modular libraries will typically have at least some of the following:

- Unconditional calls to `require` or `define`
- Declarations like `import * as a from 'b';` or `export c;`
- Assignments to `exports` or `module.exports`

They will rarely have:

- Assignments to properties of `window` or `global`

There are four templates available for modules,
[`module.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html), [`module-class.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-class-d-ts.html), [`module-function.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html) and [`module-plugin.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-plugin-d-ts.html).

You should first read [`module.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html) for an overview on the way they all work.

Then use the template [`module-function.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-function-d-ts.html) if your module can be *called* like a function:

js

Use the template [`module-class.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-class-d-ts.html) if your module can be *constructed* using `new`:

js

If you have a module which when imported, makes changes to other modules use template [`module-plugin.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-plugin-d-ts.html):

js

A *global* library is one that can be accessed from the global scope (i.e. without using any form of `import`).
Many libraries simply expose one or more global variables for use.
For example, if you were using [jQuery](https://jquery.com/), the `$` variable can be used by simply referring to it:

ts

You’ll usually see guidance in the documentation of a global library of how to use the library in an HTML script tag:

html

Today, most popular globally-accessible libraries are actually written as UMD libraries (see below). UMD library documentation is hard to distinguish from global library documentation. Before writing a global declaration file, make sure the library isn’t actually UMD.

Global library code is usually extremely simple. A global “Hello, world” library might look like this:

js

or like this:

js

When looking at the code of a global library, you’ll usually see:

- Top-level `var` statements or `function` declarations
- One or more assignments to `window.someName`
- Assumptions that DOM primitives like `document` or `window` exist

You *won’t* see:

- Checks for, or usage of, module loaders like `require` or `define`
- CommonJS/Node.js-style imports of the form `var fs = require("fs");`
- Calls to `define(...)`
- Documentation describing how to `require` or import the library

Because it’s usually easy to turn a global library into a UMD library, very few popular libraries are still written in the global style.
However, libraries that are small and require the DOM (or have *no* dependencies) may still be global.

The template file [`global.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-d-ts.html) defines an example library `myLib`.
Be sure to read the [“Preventing Name Conflicts” footnote](https://www.typescriptlang.org#preventing-name-conflicts).

A *UMD* module is one that can *either* be used as module (through an import), or as a global (when run in an environment without a module loader).
Many popular libraries, such as [Moment.js](https://momentjs.com/), are written this way.
For example, in Node.js or using RequireJS, you would write:

ts

whereas in a vanilla browser environment you would write:

js

[UMD modules](https://github.com/umdjs/umd) check for the existence of a module loader environment.
This is an easy-to-spot pattern that looks something like this:

js

If you see tests for `typeof define`, `typeof window`, or `typeof module` in the code of a library, especially at the top of the file, it’s almost always a UMD library.

Documentation for UMD libraries will also often demonstrate a “Using in Node.js” example showing `require`,
and a “Using in the browser” example showing using a `<script>` tag to load the script.

Most popular libraries are now available as UMD packages.
Examples include [jQuery](https://jquery.com/), [Moment.js](https://momentjs.com/), [lodash](https://lodash.com/), and many more.

Use the [`module-plugin.d.ts`](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-plugin-d-ts.html) template.

There are several kinds of dependencies your library might have. This section shows how to import them into the declaration file.

If your library depends on a global library, use a `/// <reference types="..." />` directive:

ts

If your library depends on a module, use an `import` statement:

ts

If your global library depends on a UMD module, use a `/// <reference types` directive:

ts

If your module or UMD library depends on a UMD library, use an `import` statement:

ts

Do *not* use a `/// <reference` directive to declare a dependency to a UMD library!

Note that it’s possible to define many types in the global scope when writing a global declaration file. We strongly discourage this as it leads to possible unresolvable name conflicts when many declaration files are in a project.

A simple rule to follow is to only declare types *namespaced* by whatever global variable the library defines.
For example, if the library defines the global value ‘cats’, you should write

ts

But *not*

ts

This guidance also ensures that the library can be transitioned to UMD without breaking declaration file users.

Many popular libraries, such as Express, expose themselves as a callable function when imported. For example, the typical Express usage looks like this:

ts

In ES6-compliant module loaders, the top-level object (here imported as `exp`) can only have properties;
the top-level module object can *never* be callable.

The most common solution here is to define a `default` export for a callable/constructable object;
module loaders commonly detect this situation automatically and replace the top-level object with the `default` export.
TypeScript can handle this for you, if you have [`"esModuleInterop": true`](https://www.typescriptlang.org/tsconfig/#esModuleInterop) in your tsconfig.json.