---
id: "typescript_005"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - Indexed Access Types"
doc_order: 5
source_url: "https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html"
language: "en"
retrieved_at: "2026-11-03 17:56:26"
content_hash: "ab883c2924d706f209b0374dcdc15e42952a3b6d86fdcf37819c0c1f872a5f86"
---

# TypeScript: Documentation - Indexed Access Types

Source: https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html

---

We can use an *indexed access type* to look up a specific property on another type:

ts

The indexing type is itself a type, so we can use unions, `keyof`, or other types entirely:

ts

You’ll even see an error if you try to index a property that doesn’t exist:

ts

Another example of indexing with an arbitrary type is using `number` to get the type of an array’s elements.
We can combine this with `typeof` to conveniently capture the element type of an array literal:

tsMyArray = \[{name : "Alice",age : 15 },{name : "Bob",age : 23 },{name : "Eve",age : 38 },\];typePerson = typeofMyArray \[number\];typeAge = typeofMyArray \[number\]\["age"\];// OrtypeAge2 =Person \["age"\];[Try](https://www.typescriptlang.org/play/#code/MYewdgzgLgBAsgTwIICcUEMEwLwwNoBQMMA3jGOgLYCmAXDAERIA2AlsNQwDQzoDmdGAEYArDAC+XIqXJVBDAEIgARt14D6AJgDMEqcTIUa9BgFEAbpx79B2gBx6CAXQDcBAlAQAHajAAK1CgQ4Dgwnj4gAGbwyGiYeGAArpTKga4EAPQZxDAAegD8Ht6+SAKh4dRRMagYCAnJqShOeAw2DOlZOQWZ2QDyKEU+MKXUmqEBQeAtbR3ZxAVAA)

You can only use types when indexing, meaning you can’t use a `const` to make a variable reference:

ts

2749Type 'key' cannot be used as an index type.'key' refers to a value, but is being used as a type here. Did you mean 'typeof key'?key = "age";typeAge =Person \[key \];Type 'key' cannot be used as an index type.'key' refers to a value, but is being used as a type here. Did you mean 'typeof key'?2538[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwFYDMAOdB2AFgE4AoAFwE8AHSUABRkTgDtQBeUAb1AEMBzSKhYBXALYAjGAG5QLXmKGhE5aAEsW-WbwA2agG5KJcODsi82AX2mkQoALSOAxiPKP7pJ6xWgA1pEoOUAAiAUhgmypaUABBQSDGJFYAbX9KAF1pIA)

However, you can use a type alias for a similar style of refactor:

ts