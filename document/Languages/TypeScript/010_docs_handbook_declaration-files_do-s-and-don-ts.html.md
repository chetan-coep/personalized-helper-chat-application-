---
id: "typescript_010"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - Do's and Don'ts"
doc_order: 10
source_url: "https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html"
language: "en"
retrieved_at: "2026-11-03 17:56:32"
content_hash: "a9958d5418a2077d8bf1a00476066dd5fdeaf5b57a0d842861199045d5c2f5d0"
---

# TypeScript: Documentation - Do's and Don'ts

Source: https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html

---

❌ **Don’t** ever use the types `Number`, `String`, `Boolean`, `Symbol`, or `Object`
These types refer to non-primitive boxed objects that are almost never used appropriately in JavaScript code.

ts

✅ **Do** use the types `number`, `string`, `boolean`, and `symbol`.

ts

Instead of `Object`, use the non-primitive `object` type ([added in TypeScript 2.2](https://www.typescriptlang.org/release-notes/typescript-2-2.html#object-type)).

❌ **Don’t** ever have a generic type which doesn’t use its type parameter.
See more details in [TypeScript FAQ page](https://github.com/Microsoft/TypeScript/wiki/FAQ#why-doesnt-type-inference-work-on-this-interface-interface-foot--).

❌ **Don’t** use `any` as a type unless you are in the process of migrating a JavaScript project to TypeScript. The compiler *effectively* treats `any` as “please turn off type checking for this thing”. It is similar to putting an `@ts-ignore` comment around every usage of the variable. This can be very helpful when you are first migrating a JavaScript project to TypeScript as you can set the type for stuff you haven’t migrated yet as `any`, but in a full TypeScript project you are disabling type checking for any parts of your program that use it.

In cases where you don’t know what type you want to accept, or when you want to accept anything because you will be blindly passing it through without interacting with it, you can use [`unknown`](https://www.typescriptlang.org/play/#example/unknown-and-never).

❌ **Don’t** use the return type `any` for callbacks whose value will be ignored:

ts

✅ **Do** use the return type `void` for callbacks whose value will be ignored:

ts

❔ **Why:** Using `void` is safer because it prevents you from accidentally using the return value of `x` in an unchecked way:

ts

❌ **Don’t** use optional parameters in callbacks unless you really mean it:

ts

This has a very specific meaning: the `done` callback might be invoked with 1 argument or might be invoked with 2 arguments.
The author probably intended to say that the callback might not care about the `elapsedTime` parameter,
but there’s no need to make the parameter optional to accomplish this —
it’s always legal to provide a callback that accepts fewer arguments.

✅ **Do** write callback parameters as non-optional:

ts

❌ **Don’t** write separate overloads that differ only on callback arity:

ts

✅ **Do** write a single overload using the maximum arity:

ts

❔ **Why:** It’s always legal for a callback to disregard a parameter, so there’s no need for the shorter overload.
Providing a shorter callback first allows incorrectly-typed functions to be passed in because they match the first overload.

❌ **Don’t** put more general overloads before more specific overloads:

ts

✅ **Do** sort overloads by putting the more general signatures after more specific signatures:

ts

❔ **Why:** TypeScript chooses the *first matching overload* when resolving function calls.
When an earlier overload is “more general” than a later one, the later one is effectively hidden and cannot be called.

❌ **Don’t** write several overloads that differ only in trailing parameters:

ts

✅ **Do** use optional parameters whenever possible:

ts

Note that this collapsing should only occur when all overloads have the same return type.

❔ **Why:** This is important for two reasons.

TypeScript resolves signature compatibility by seeing if any signature of the target can be invoked with the arguments of the source,
*and extraneous arguments are allowed*.
This code, for example, exposes a bug only when the signature is correctly written using optional parameters:

ts

The second reason is when a consumer uses the “strict null checking” feature of TypeScript.
Because unspecified parameters appear as `undefined` in JavaScript, it’s usually fine to pass an explicit `undefined` to a function with optional arguments.
This code, for example, should be OK under strict nulls:

ts

❌ **Don’t** write overloads that differ by type in only one argument position:

ts

✅ **Do** use union types whenever possible:

ts

Note that we didn’t make `b` optional here because the return types of the signatures differ.

❔ **Why:** This is important for people who are “passing through” a value to your function:

ts