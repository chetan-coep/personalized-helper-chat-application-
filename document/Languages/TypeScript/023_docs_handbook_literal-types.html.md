---
id: "typescript_023"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Handbook - Literal Types"
doc_order: 23
source_url: "https://www.typescriptlang.org/docs/handbook/literal-types.html"
language: "en"
retrieved_at: "2026-11-03 17:56:53"
content_hash: "cdedc393a6a0c0879d0582dd7876eca98b9378badf112b69257765671327a308"
---

# TypeScript: Handbook - Literal Types

Source: https://www.typescriptlang.org/docs/handbook/literal-types.html

---

A literal is a more concrete sub-type of a collective type.
What this means is that `"Hello World"` is a `string`, but a `string` is not `"Hello World"` inside the type system.

There are three sets of literal types available in TypeScript today: strings, numbers, and booleans; by using literal types you can allow an exact value which a string, number, or boolean must have.

When you declare a variable via `var` or `let`, you are telling the compiler that there is the chance that this variable will change its contents.
In contrast, using `const` to declare a variable will inform TypeScript that this object will never change.

tshelloWorld = "Hello World";// On the other hand, a let can change, and so the compiler declares it a stringlethiWorld = "Hi World";[Try](https://www.typescriptlang.org/play/#code/PTAEHUFMHICdNAWwIYGsCWA7A5qZpsBXZWZTAF0gXIAtlzRb0BnUANxPWQCMAbSAFAhQNSL14B7cBNi8AJqADu6caEyQ2kWKADGdHJAA0obgE9QhZllw6JmZuQB0AoWADKE4wBVTAB0huOrDovgzMkOSstNR+1BImCABEABJikhAy8onGmBJh5ME4Arb2DKLiUpkKALygKWnx0rJyiQDcLsIA8piMoqB5otr6csb4-Aw6ZLr62EZ4mArM8dG6Eoi+KlqgcpA6vCSQrOgM+A6F2ALjIuhN8qC1KegZzW1AA)

The process of going from an infinite number of potential cases (there is an infinite number of possible string values) to a smaller, finite number of potential case (in `helloWorld`’s case: 1) is called narrowing.

In practice string literal types combine nicely with union types, type guards, and type aliases. You can use these features together to get enum-like behavior with strings.

tsEasing = "ease-in" | "ease-out" | "ease-in-out";classUIElement {animate (dx : number,dy : number,easing :Easing ) {if (easing === "ease-in") {// ...} else if (easing === "ease-out") {} else if (easing === "ease-in-out") {} else {// It's possible that someone could reach this// by ignoring your types though.}}}letbutton = newUIElement ();button .animate (0, 0, "ease-in");button .animate (0, 0,"uneasy" );Argument of type '"uneasy"' is not assignable to parameter of type 'Easing'.2345Argument of type '"uneasy"' is not assignable to parameter of type 'Easing'.[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAsBWAUAC4CeADpKAKICGiAlgHYDmoAvKAESQ2QC0D7oAD4cuiXnACuBAcM7c+9HpOkBuPHgDGAGxqJQAVQCSFLZAC2kegVABvPKFBV6tM1QKQAFABMAHqnoSZgBGMAA0oF5E-oEh0OGiDIyo1HRMAJS29g6gtABmoB4JTKwsbHJiCuwZdtnZIKAAdE1ZDgC+oJBaYjn5hTSJJWWi4lJVmbXtnd15BUXMpUPyDEqj1S2gk13kNbWg9YYEAOR6JHCIdEGmoAQAFm6giHAWcPTkGpJaXqDQXBo31zdaIh1g56kEiDlGPQEAMiJJoNdSJA9LdJIwbg11q0stjsXhTNYglICC9WKBXgB3AzGUwWKweNJqIkEEn0BpOFxuTwABnCvJES3oVSZxJe7OcrncHn5-PYEleNCIwqAA)

You can pass any of the three allowed strings, but any other string will give the error


String literal types can be used in the same way to distinguish overloads:

ts

TypeScript also has numeric literal types, which act the same as the string literals above.

ts

A common case for their use is for describing config values:

ts

TypeScript also has boolean literal types. You might use these to constrain object values whose properties are interrelated.

ts