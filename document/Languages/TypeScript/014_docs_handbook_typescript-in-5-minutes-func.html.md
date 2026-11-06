---
id: "typescript_014"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - TypeScript for Functional Programmers"
doc_order: 14
source_url: "https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html"
language: "en"
retrieved_at: "2026-11-03 17:56:37"
content_hash: "77eb39f7acb1a9a1580258c5c50083ef4af4d18f93016b98dc6eb009a2d1a8fe"
---

# TypeScript: Documentation - TypeScript for Functional Programmers

Source: https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html

---

TypeScript began its life as an attempt to bring traditional object-oriented types to JavaScript so that the programmers at Microsoft could bring traditional object-oriented programs to the web. As it has developed, TypeScript’s type system has evolved to model code written by native JavaScripters. The resulting system is powerful, interesting and messy.

This introduction is designed for working Haskell or ML programmers who want to learn TypeScript. It describes how the type system of TypeScript differs from Haskell’s type system. It also describes unique features of TypeScript’s type system that arise from its modelling of JavaScript code.

This introduction does not cover object-oriented programming. In practice, object-oriented programs in TypeScript are similar to those in other popular languages with OO features.

In this introduction, I assume you know the following:

- How to program in JavaScript, the good parts.
- Type syntax of a C-descended language.

If you need to learn the good parts of JavaScript, read
[JavaScript: The Good Parts](https://shop.oreilly.com/product/9780596517748.do).
You may be able to skip the book if you know how to write programs in
a call-by-value lexically scoped language with lots of mutability and
not much else.
[R<sup>4</sup>RS Scheme](https://people.csail.mit.edu/jaffer/r4rs.pdf) is a good example.

[The C++ Programming Language](http://www.stroustrup.com/4th.html) is
a good place to learn about C-style type syntax. Unlike C++,
TypeScript uses postfix types, like so: `x: string` instead of `string x`.

JavaScript defines 8 built-in types:

| Type | Explanation | 
|---|---|
| `Number` | a double-precision IEEE 754 floating point. | 
| `String` | an immutable UTF-16 string. | 
| `BigInt` | integers in the arbitrary precision format. | 
| `Boolean` | `true` and `false`. | 
| `Symbol` | a unique value usually used as a key. | 
| `Null` | equivalent to the unit type. | 
| `Undefined` | also equivalent to the unit type. | 
| `Object` | similar to records. | 

TypeScript has corresponding primitive types for the built-in types:

- `number`
- `string`
- `bigint`
- `boolean`
- `symbol`
- `null`
- `undefined`
- `object`

| Type | Explanation | 
|---|---|
| `unknown` | the top type. | 
| `never` | the bottom type. | 
| object literal | e.g. `{ property: Type }` | 
| `void` | for functions with no documented return value | 
| `T[]` | mutable arrays, also written `Array<T>` | 
| `[T, T]` | tuples, which are fixed-length but mutable | 
| `(t: T) => U` | functions | 

Notes:

1. Function syntax includes parameter names. This is pretty hard to get used to! ts2. Object literal type syntax closely mirrors object literal value syntax: ts3. `[T, T]` is a subtype of `T[]`. This is different than Haskell, where tuples are not related to lists.

JavaScript has boxed equivalents of primitive types that contain the
methods that programmers associate with those types. TypeScript
reflects this with, for example, the difference between the primitive
type `number` and the boxed type `Number`. The boxed types are rarely
needed, since their methods return primitives.

ts

Note that calling a method on a numeric literal requires it to be in parentheses to aid the parser.

TypeScript uses the type `any` whenever it can’t tell what the type of
an expression should be. Compared to `Dynamic`, calling `any` a type
is an overstatement. It just turns off the type checker
wherever it appears. For example, you can push any value into an
`any[]` without marking the value in any way:

ts

And you can use an expression of type `any` anywhere:

ts

`any` is contagious, too — if you initialize a variable with an
expression of type `any`, the variable has type `any` too.

ts

To get an error when TypeScript produces an `any`, use
`"noImplicitAny": true`, or `"strict": true` in `tsconfig.json`.

Structural typing is a familiar concept to most functional programmers, although Haskell and most MLs are not structurally typed. Its basic form is pretty simple:

ts

Here, the object literal `{ x: "hi", extra: 1 }` has a matching
literal type `{ x: string, extra: number }`. That
type is assignable to `{ x: string }` since
it has all the required properties and those properties have
assignable types. The extra property doesn’t prevent assignment, it
just makes it a subtype of `{ x: string }`.

Named types just give a name to a type; for assignability purposes
there’s no difference between the type alias `One` and the interface
type `Two` below. They both have a property `p: string`. (Type aliases
behave differently from interfaces with respect to recursive
definitions and type parameters, however.)

ts

In TypeScript, union types are untagged. In other words, they are not
discriminated unions like `data` in Haskell. However, you can often
discriminate types in a union using built-in tags or other properties.

tsstart (arg : string | string\[\] | (() => string) | {s : string }): string {// this is super common in JavaScriptif (typeofarg === "string") {returncommonCase (arg );} else if (Array .isArray (arg )) {returnarg .map (commonCase ).join (",");} else if (typeofarg === "function") {returncommonCase (arg ());} else {returncommonCase (arg .s );}functioncommonCase (s : string): string {// finally, just convert a string to another stringreturns ;}}[Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABAZygQwE5QBQChGKYDmAXClBjGEYgD7mXUDaAunYttgJSIC8AfAypEe9AN4oyqRjQC+uLlIrDEY-IgD0GxFAAWMZIgMoQABwCmGRBDgBbWwiNIAUmgBuaAMoRKpqOphgDigATws4IOI+Xl5EACJpYTieNQICDHMoEAwkG3sEAGE0ZHNsYi4AbnVZRHMAGxKjIOwAQQwMNBCAOgM2jpCyjBEU9XTM7KRiLts0U2w8hzAikq4ugCs4Kmw4gBpkqoIa+sbA4LDzCMIh6Ni40EhYBGTVUcQMrJzrO0Xl0uJuSrVWoNcwvNJvcafBaFYp-IZdZCAw64dT3aDwXLfGElbDIJQyRRCahgtJaRDAKhoOp1EI7RBrECoL5gNyWKCEIk0KBwQhgOB6Syc17vCYoA6IeSyIA)

`string`, `Array` and `Function` have built-in type predicates,
conveniently leaving the object type for the `else` branch. It is
possible, however, to generate unions that are difficult to
differentiate at runtime. For new code, it’s best to build only
discriminated unions.

The following types have built-in predicates:

| Type | Predicate | 
|---|---|
| string | `typeof s === "string"` | 
| number | `typeof n === "number"` | 
| bigint | `typeof m === "bigint"` | 
| boolean | `typeof b === "boolean"` | 
| symbol | `typeof g === "symbol"` | 
| undefined | `typeof undefined === "undefined"` | 
| function | `typeof f === "function"` | 
| array | `Array.isArray(a)` | 
| object | `typeof o === "object"` | 

Note that functions and arrays are objects at runtime, but have their own predicates.

In addition to unions, TypeScript also has intersections:

ts

`Combined` has two properties, `a` and `b`, just as if they had been
written as one object literal type. Intersection and union are
recursive in case of conflicts, so `Conflicting.a: number & string`.

Unit types are subtypes of primitive types that contain exactly one
primitive value. For example, the string `"foo"` has the type
`"foo"`. Since JavaScript has no built-in enums, it is common to use a set of
well-known strings instead. Unions of string literal types allow
TypeScript to type this pattern:

ts

When needed, the compiler *widens* — converts to a
supertype — the unit type to the primitive type, such as `"foo"`
to `string`. This happens when using mutability, which can hamper some
uses of mutable variables:

tss = "right";pad ("hi", 10,s ); // error: 'string' is not assignable to '"left" | "right"'Argument of type 'string' is not assignable to parameter of type '"left" | "right"'.2345Argument of type 'string' is not assignable to parameter of type '"left" | "right"'.[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAsBWAUACaQDGANgIbSSgBmArgHbEAuAlnA6AA7kEAUKUImbRWDAOYAaUA1QM6AWwBGMaQVZUW7WaABEpSDWa7QAHz2jxAC2MBKVMNESA3HhCgAtF+J1mXj3gGzEKgALwWrNbGrjz8ulasutIAjAAM0oi2zqDuMPDQqADkjmLihaCsiDJwweSIiJEM5EoGoMxwoIX6hsZmEVG6hUA)

Here’s how the error happens:

- `"right": "right"`
- `s: string` because `"right"` widens to `string` on assignment to a mutable variable.
- `string` is not assignable to `"left" | "right"`

You can work around this with a type annotation for `s`, but that
in turn prevents assignments to `s` of variables that are not of type
`"left" | "right"`.

ts

TypeScript has some obvious places where it can infer types, like variable declarations:

ts

But it also infers types in a few other places that you may not expect if you’ve worked with other C-syntax languages:

ts

Here, `n: number` in this example also, despite the fact that `T` and `U`
have not been inferred before the call. In fact, after `[1,2,3]` has
been used to infer `T=number`, the return type of `n => n.toString()`
is used to infer `U=string`, causing `sns` to have the type
`string[]`.

Note that inference will work in any order, but intellisense will only
work left-to-right, so TypeScript prefers to declare `map` with the
array first:

ts

Contextual typing also works recursively through object literals, and
on unit types that would otherwise be inferred as `string` or
`number`. And it can infer return types from context:

ts

The type of `o` is determined to be `{ inference: string }` because

1. Declaration initializers are contextually typed by the
declaration’s type: `{ inference: string }`.
2. The return type of a call uses the contextual type for inferences,
so the compiler infers that `T={ inference: string }`.
3. Arrow functions use the contextual type to type their parameters,
so the compiler gives `o: { inference: string }`.

And it does so while you are typing, so that after typing `o.`, you
get completions for the property `inference`, along with any other
properties you’d have in a real program.
Altogether, this feature can make TypeScript’s inference look a bit
like a unifying type inference engine, but it is not.

Type aliases are mere aliases, just like `type` in Haskell. The
compiler will attempt to use the alias name wherever it was used in
the source code, but does not always succeed.

ts

The closest equivalent to `newtype` is a *tagged intersection*:

ts

An `FString` is just like a normal string, except that the compiler
thinks it has a property named `__compileTimeOnly` that doesn’t
actually exist. This means that `FString` can still be assigned to
`string`, but not the other way round.

The closest equivalent to `data` is a union of types with discriminant
properties, normally called discriminated unions in TypeScript:

ts

Unlike Haskell, the tag, or discriminant, is just a property in each
object type. Each variant has an identical property with a different
unit type. This is still a normal union type; the leading `|` is
an optional part of the union type syntax. You can discriminate the
members of the union using normal JavaScript code:

tsShape =| {kind : "circle";radius : number }| {kind : "square";x : number }| {kind : "triangle";x : number;y : number };functionarea (s :Shape ) {if (s .kind === "circle") {returnMath .PI \*s .radius \*s .radius ;} else if (s .kind === "square") {returns .x \*s .x ;} else {return (s .x \*s .y ) / 2;}}[Try](https://www.typescriptlang.org/play/#code/C4TwDgpgBAygFgQ0lAvAKClAPlA3lAawEsA7AEwC4oAiAYyICdaAbCagbigYTKIFcAzlRJ8AtgCMIDKAF8M2PIVKUaAgI58EDNpwAewsZOlzMOfMXJVqwBkQQkA5qw5R9UERKmcQBz8fZoaABmfCS0wEQA9iRQWhAIABRCsIiQAJR48kRBUEkAdBZkqCgoNPRMzhm48pjawHwMMQCyCMBweQAKAJJQAFRQAnncvIJ9A0M8-AIBmDJQEMwC0Nm5g4XFpdTqmtrUVTVcEPWN47pjg7ozsvOL0NWYtUcNMfln-YMgGQD0UABMV3IZEA)

Note that the return type of `area` is inferred to be `number` because
TypeScript knows the function is total. If some variant is not
covered, the return type of `area` will be `number | undefined` instead.

Also, unlike Haskell, common properties show up in any union, so you can usefully discriminate multiple members of the union:

ts

Like most C-descended languages, TypeScript requires declaration of type parameters:

ts

There is no case requirement, but type parameters are conventionally single uppercase letters. Type parameters can also be constrained to a type, which behaves a bit like type class constraints:

ts

TypeScript can usually infer type arguments from a call based on the type of the arguments, so type arguments are usually not needed.

Because TypeScript is structural, it doesn’t need type parameters as
much as nominal systems. Specifically, they are not needed to make a
function polymorphic. Type parameters should only be used to
*propagate* type information, such as constraining parameters to be
the same type:

ts

In the first `length`, T is not necessary; notice that it’s only
referenced once, so it’s not being used to constrain the type of the
return value or other parameters.

TypeScript does not have higher kinded types, so the following is not legal:

ts

Point-free programming — heavy use of currying and function composition — is possible in JavaScript, but can be verbose. In TypeScript, type inference often fails for point-free programs, so you’ll end up specifying type parameters instead of value parameters. The result is so verbose that it’s usually better to avoid point-free programming.

JavaScript’s modern module syntax is a bit like Haskell’s, except that
any file with `import` or `export` is implicitly a module:

ts

You can also import commonjs modules — modules written using node.js’ module system:

ts

You can export with an export list:

ts

Or by marking each export individually:

ts

The latter style is more common but both are allowed, even in the same file.

In JavaScript, mutability is the default, although it allows variable
declarations with `const` to declare that the *reference* is
immutable. The referent is still mutable:

js

TypeScript additionally has a `readonly` modifier for properties.

ts

It also ships with a mapped type `Readonly<T>` that makes
all properties `readonly`:

ts

And it has a specific `ReadonlyArray<T>` type that removes
side-affecting methods and prevents writing to indices of the array,
as well as special syntax for this type:

ts

You can also use a const-assertion, which operates on arrays and object literals:

ts

However, none of these options are the default, so they are not consistently used in TypeScript code.

This doc is a high level overview of the syntax and types you would use in everyday code. From here you should:

- Read the full Handbook [from start to finish](https://www.typescriptlang.org/docs/handbook/intro.html)
- Explore the [Playground examples](https://www.typescriptlang.org/play#show-examples)