---
id: "typescript_007"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - Declaration Reference"
doc_order: 7
source_url: "https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html"
language: "en"
retrieved_at: "2026-11-03 17:56:28"
content_hash: "81114466bca993c8b2c63a25d9d60eb4fdfde0a2f3082426d352a3abe0359d3c"
---

# TypeScript: Documentation - Declaration Reference

Source: https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html

---

The purpose of this guide is to teach you how to write a high-quality definition file. This guide is structured by showing documentation for some API, along with sample usage of that API, and explaining how to write the corresponding declaration.

These examples are ordered in approximately increasing order of complexity.

*Documentation*

The global variable `myLib` has a function `makeGreeting` for creating greetings,
and a property `numberOfGreetings` indicating the number of greetings made so far.


*Code*

ts

*Declaration*

Use `declare namespace` to describe types or values accessed by dotted notation.

ts

*Documentation*

The `getWidget` function accepts a number and returns a Widget, or accepts a string and returns a Widget array.

*Code*

ts

*Declaration*

ts

*Documentation*

When specifying a greeting, you must pass a `GreetingSettings` object.
This object has the following properties:

1 - greeting: Mandatory string

2 - duration: Optional length of time (in milliseconds)

3 - color: Optional string, e.g. ‘#ff00ff’


*Code*

ts

*Declaration*

Use an `interface` to define a type with properties.

ts

*Documentation*

Anywhere a greeting is expected, you can provide a `string`, a function returning a `string`, or a `Greeter` instance.


*Code*

ts

*Declaration*

You can use a type alias to make a shorthand for a type:

ts

*Documentation*

The `greeter` object can log to a file or display an alert.
You can provide LogOptions to `.log(...)` and alert options to `.alert(...)`


*Code*

ts

*Declaration*

Use namespaces to organize types.

ts

You can also create nested namespaces in one declaration:

ts

*Documentation*

You can create a greeter by instantiating the `Greeter` object, or create a customized greeter by extending from it.


*Code*

ts

*Declaration*

Use `declare class` to describe a class or class-like object.
Classes can have properties and methods as well as a constructor.

ts

*Documentation*

The global variable `foo` contains the number of widgets present.


*Code*

ts

*Declaration*

Use `declare var` to declare variables.
If the variable is read-only, you can use `declare const`.
You can also use `declare let` if the variable is block-scoped.

ts

*Documentation*

You can call the function `greet` with a string to show a greeting to the user.


*Code*

ts

*Declaration*

Use `declare function` to declare functions.

ts