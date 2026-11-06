---
id: "typescript_003"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - JS Projects Utilizing TypeScript"
doc_order: 3
source_url: "https://www.typescriptlang.org/docs/handbook/intro-to-js-ts.html"
language: "en"
retrieved_at: "2026-11-03 17:56:24"
content_hash: "0aa1e39716a3fc1bbdbfc5290ae6d67d9991b7fe506faba81e95413f16b2c935"
---

# TypeScript: Documentation - JS Projects Utilizing TypeScript

Source: https://www.typescriptlang.org/docs/handbook/intro-to-js-ts.html

---

The type system in TypeScript has different levels of strictness when working with a codebase:

- A type-system based only on inference with JavaScript code
- Incremental typing in JavaScript [via JSDoc](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html)
- Using `// @ts-check` in a JavaScript file
- TypeScript code
- TypeScript with [`strict`](https://www.typescriptlang.org/tsconfig#strict) enabled

Each step represents a move towards a safer type-system, but not every project needs that level of verification.

This is when you use an editor which uses TypeScript to provide tooling like auto-complete, jump to symbol and refactoring tools like rename.
The [homepage](https://www.typescriptlang.org/) has a list of editors which have TypeScript plugins.

In a `.js` file, types can often be inferred. When types can’t be inferred, they can be specified using JSDoc syntax.

JSDoc annotations that come before a declaration will be used to set the type of that declaration. For example:

js

You can find the full list of supported JSDoc patterns [in JSDoc Supported Types](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html).

The last line of the previous code sample would raise an error in TypeScript, but it doesn’t by default in a JS project.
To enable errors in your JavaScript files add: `// @ts-check` to the first line in your `.js` files to have TypeScript raise it as an error.

js

If you have a lot of JavaScript files you want to add errors to then you can switch to using a [`jsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html).
You can skip checking some files by adding a `// @ts-nocheck` comment to files.

TypeScript may offer you errors which you disagree with, in those cases you can ignore errors on specific lines by adding `// @ts-ignore` or `// @ts-expect-error` on the preceding line.

js

To learn more about how JavaScript is interpreted by TypeScript read [How TS Type Checks JS](https://www.typescriptlang.org/docs/handbook/type-checking-javascript-files.html)