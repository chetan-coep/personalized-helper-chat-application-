---
id: "typescript_022"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Handbook - Interfaces"
doc_order: 22
source_url: "https://www.typescriptlang.org/docs/handbook/interfaces.html"
language: "en"
retrieved_at: "2026-11-03 17:56:52"
content_hash: "627c1514bb432d6a0484e3e99f38c5ff0311ddac5b797c382e58ecaa0a238b0f"
---

# TypeScript: Handbook - Interfaces

Source: https://www.typescriptlang.org/docs/handbook/interfaces.html

---

One of TypeScript’s core principles is that type checking focuses on the *shape* that values have.
This is sometimes called “duck typing” or “structural subtyping”.
In TypeScript, interfaces fill the role of naming these types, and are a powerful way of defining contracts within your code as well as contracts with code outside of your project.

The easiest way to see how interfaces work is to start with a simple example:

ts

The type checker checks the call to `printLabel`.
The `printLabel` function has a single parameter that requires that the object passed in has a property called `label` of type `string`.
Notice that our object actually has more properties than this, but the compiler only checks that *at least* the ones required are present and match the types required.
There are some cases where TypeScript isn’t as lenient, which we’ll cover in a bit.

We can write the same example again, this time using an interface to describe the requirement of having the `label` property that is a string:

ts

The interface `LabeledValue` is a name we can now use to describe the requirement in the previous example.
It still represents having a single property called `label` that is of type `string`.
Notice we didn’t have to explicitly say that the object we pass to `printLabel` implements this interface like we might have to in other languages.
Here, it’s only the shape that matters. If the object we pass to the function meets the requirements listed, then it’s allowed.

It’s worth pointing out that the type checker does not require that these properties come in any sort of order, only that the properties the interface requires are present and have the required type.

Not all properties of an interface may be required. Some exist under certain conditions or may not be there at all. These optional properties are popular when creating patterns like “option bags” where you pass an object to a function that only has a couple of properties filled in.

Here’s an example of this pattern:

tsSquareConfig {color ?: string;width ?: number;}functioncreateSquare (config :SquareConfig ): {color : string;area : number } {letnewSquare = {color : "white",area : 100 };if (config .color ) {newSquare .color =config .color ;}if (config .width ) {newSquare .area =config .width \*config .width ;}returnnewSquare ;}letmySquare =createSquare ({color : "black" });[Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgMoEcCucoQMID2IMwA5sgN4BQyyCBANgVAPwBcyAzmFKKQNw1kAd2AATMAAt2yEJgC2AI2iCAvlSoxMIBGGBE6uOJAzZcACnrEyHUznxESpAJQcKdRsw7deIAcns4DjklaGRVSiEGCDBZCGE7XGQAXkoPJigOACJhSWBILIAaAKMOAEYABgrwwVpgGGRLRzIAOnoM50jaWhB4xIg2zygUj2tSQYza8KF6xqsnFtEJSU7qbriErHsWwJH51qWpZAAqUYXDySn1WlwwTCgQDf61DWjY+QBPfr2jEy2LdztLzILKKBiIADWWXCzn4QA)

Interfaces with optional properties are written similar to other interfaces, with each optional property denoted by a `?` at the end of the property name in the declaration.

The advantage of optional properties is that you can describe these possibly available properties while still also preventing use of properties that are not part of the interface.
For example, had we mistyped the name of the `color` property in `createSquare`, we would get an error message letting us know:

tsSquareConfig {color ?: string;width ?: number;}functioncreateSquare (config :SquareConfig ): {color : string;area : number } {letnewSquare = {color : "white",area : 100 };if (config .clor ) {Property 'clor' does not exist on type 'SquareConfig'. Did you mean 'color'?2551Property 'clor' does not exist on type 'SquareConfig'. Did you mean 'color'?// Error: Property 'clor' does not exist on type 'SquareConfig'newSquare .color =config .clor ;Property 'clor' does not exist on type 'SquareConfig'. Did you mean 'color'?2551Property 'clor' does not exist on type 'SquareConfig'. Did you mean 'color'?}if (config .width ) {newSquare .area =config .width \*config .width ;}returnnewSquare ;}letmySquare =createSquare ({color : "black" });[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwFYMEYBQBLAOwBcYAzAQwGNJQBlARwFcLpIBhOQs-Ac1ADeuUKCpwANggD8qRMWhFeAbmGgA7vgAmxABYzQhJgFsARjBUBfXLjJNCVYvi6i2FUoxZsAFGO59UHqwcXDy8AJSoAqISCLLyikqgQRSohqYwoBaCquKQxAaQaoFsoAC8gtGS0KgARGo6+KQ1ADRJrqjYAAydmSoi+GSgPiF8AHRUVWHZIiIgoACisLGgAArwAA4wxACeoADkEwh7oJpwkIgGcPmQAB74cqDOO5v7xcF+vHuqIoSFb+MxaBlaIfcZVPqZVQDIa+UKjDTaHRTIQzApFZhBUbJYGwsYI3SgABUILh+J0EKsIjYxCY0EIaLelmsuXyRm2bxxrncGO8UTEVVqJnE1AA1jVMmElEA)

Some properties should only be modifiable when an object is first created.
You can specify this by putting `readonly` before the name of the property:

ts

You can construct a `Point` by assigning an object literal.
After the assignment, `x` and `y` can’t be changed.

ts

TypeScript comes with a `ReadonlyArray<T>` type that is the same as `Array<T>` with all mutating methods removed, so you can make sure you don’t change your arrays after creation:

tsa : number\[\] = \[1, 2, 3, 4\];letro :ReadonlyArray \<number> =a ;ro \[0\] = 12; // error!Index signature in type 'readonly number\[\]' only permits reading.2542Index signature in type 'readonly number\[\]' only permits reading.ro .push (5); // error!Property 'push' does not exist on type 'readonly number\[\]'.2339Property 'push' does not exist on type 'readonly number\[\]'.ro .length = 100; // error!Cannot assign to 'length' because it is a read-only property.2540Cannot assign to 'length' because it is a read-only property.a =ro ; // error!The type 'readonly number\[\]' is 'readonly' and cannot be assigned to the mutable type 'number\[\]'.4104The type 'readonly number\[\]' is 'readonly' and cannot be assigned to the mutable type 'number\[\]'.[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwFYAsb0GY8BOdbABlCwEZSsAoAG0gBdQBDVAOwFcBbAIxgBtALqgAvKEGUANOll5ZWYQG4GzUPFQAlSKwAmcDvQCeAQVitjAHm78YAPnFtVteINKiJlNMtAhQMPDQAISucAB0AA5ciAAWABQYAJS+-oEIofDhjBwA5kyxTtSkqWDpIbSsTvClAbAZQA)

On the last line of the snippet you can see that even assigning the entire `ReadonlyArray` back to a normal array is illegal.
You can still override it with a type assertion, though:

ts

The easiest way to remember whether to use `readonly` or `const` is to ask whether you’re using it on a variable or a property.
Variables use `const` whereas properties use `readonly`.

In our first example using interfaces, TypeScript lets us pass `{ size: number; label: string; }` to something that only expected a `{ label: string; }`.
We also just learned about optional properties, and how they’re useful when describing so-called “option bags”.

However, combining the two naively would allow an error to sneak in. For example, taking our last example using `createSquare`:

tsSquareConfig {color ?: string;width ?: number;}functioncreateSquare (config :SquareConfig ): {color : string;area : number } {return {color :config .color || "red",area :config .width ?config .width \*config .width : 20,};}letmySquare =createSquare ({colour : "red",width : 100 });Object literal may only specify known properties, but 'colour' does not exist in type 'SquareConfig'. Did you mean to write 'color'?2561Object literal may only specify known properties, but 'colour' does not exist in type 'SquareConfig'. Did you mean to write 'color'?[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAsBWdB2DATgCgBLAOwBcYAzAQwGNJQBlARwFd7pIBhOBVpkA5qADeJUKEZwANggD8qRFWiURAbimgA7mQAmVABbLQFTgFsARjG0BfEiVqcKjKmUEze9Gh268ABSyQqKo-jz8gsIiAJSo4jLyCCpqGpqgkfSoFjYwoPYSOrxUnNAURdLSsgrQqCExAHQ1CKAAPm2gAES8Bl0ANDrSWfXRoo36RsagikmhIhOGJqAAVHNNk8uoaAAMg9L2Dk5ykFSglgCeEbygALzekL6Q15CBiS1lqD2Qff16S8ZUABGHY7AqxTRAA)

Notice the given argument to `createSquare` is spelled *`colour`* instead of `color`.
In plain JavaScript, this sort of thing fails silently.

You could argue that this program is correctly typed, since the `width` properties are compatible, there’s no `color` property present, and the extra `colour` property is insignificant.

However, TypeScript takes the stance that there’s probably a bug in this code.
Object literals get special treatment and undergo *excess property checking* when assigning them to other variables, or passing them as arguments.
If an object literal has any properties that the “target type” doesn’t have, you’ll get an error:

tsmySquare =createSquare ({colour : "red",width : 100 });Object literal may only specify known properties, but 'colour' does not exist in type 'SquareConfig'. Did you mean to write 'color'?2561Object literal may only specify known properties, but 'colour' does not exist in type 'SquareConfig'. Did you mean to write 'color'?[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAsBWdB2DATgCgBLAOwBcYAzAQwGNJQBlARwFd7pIBhOBVpkA5qADeJUKEZwANggD8qRFWiURAbimgA7mQAmVABbLQFTgFsARjG0BfEiVqcKjKmUEze9Gh268ABSyQqKo-jz8gsIiAJSo4jLyCCpqGpqgkfSoFjYwoPYSOrxUnNAURdLSsgrQqCExAHQ1CKAAPm2gAES8Bl0ANDrSWfXRoo36RsagikmhIhOGJqAAVHNNk8uoaAAMg9L2DiQgoAC054ycVOenJHKQVKCWAJ4RvKAAvN6QvpBvkIFEi0yqgepA+v09EtjKgAIw7HYFWKaIA)

Getting around these checks is actually really simple. The easiest method is to just use a type assertion:

ts

However, a better approach might be to add a string index signature if you’re sure that the object can have some extra properties that are used in some special way.
If `SquareConfig` can have `color` and `width` properties with the above types, but could *also* have any number of other properties, then we could define it like so:

ts

We’ll discuss index signatures in a bit, but here we’re saying a `SquareConfig` can have any number of properties, and as long as they aren’t `color` or `width`, their types don’t matter.

One final way to get around these checks, which might be a bit surprising, is to assign the object to another variable:
Since `squareOptions` won’t undergo excess property checks, the compiler won’t give you an error.

ts

The above workaround will work as long as you have a common property between `squareOptions` and `SquareConfig`.
In this example, it was the property `width`. It will however, fail if the variable does not have any common object property. For example:

tssquareOptions = {colour : "red" };letmySquare =createSquare (squareOptions );Type '{ colour: string; }' has no properties in common with type 'SquareConfig'.2559Type '{ colour: string; }' has no properties in common with type 'SquareConfig'.[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwFYME4BQBLAOwBcYAzAQwGNJQBlARwFcLpIBhOQs-Ac1ADeuUKCpwANggD8qRMWhFeAbmGgA7vgAmxABYzQhJgFsARjBUBfXLjJNCVYvi6i2FUoxZsAFGO59UHqwcXDy8AJSoAqISCLLyikqgQRSohqYwoBaCqmzETNCE2SIiYpLQqL6hAHSlCKAAPvWgAERsms0ANKoiyRUhfFUa2jqgUtF+vINauqAAVOPVQzOoaAAMXSIWlrggoAC0B1RMxAd7uOKQxKCIzEEA8gAOjlyIoAC8gtGS+aitkO2ZFQXK5GACegTY7xckDckAhkC8N08kEez0IiDCSiAA)

Keep in mind that for simple code like above, you probably shouldn’t be trying to “get around” these checks.
For more complex object literals that have methods and hold state, you might need to keep these techniques in mind, but a majority of excess property errors are actually bugs.
That means if you’re running into excess property checking problems for something like option bags, you might need to revise some of your type declarations.
In this instance, if it’s okay to pass an object with both a `color` or `colour` property to `createSquare`, you should fix up the definition of `SquareConfig` to reflect that.

Interfaces are capable of describing the wide range of shapes that JavaScript objects can take. In addition to describing an object with properties, interfaces are also capable of describing function types.

To describe a function type with an interface, we give the interface a call signature. This is like a function declaration with only the parameter list and return type given. Each parameter in the parameter list requires both name and type.

ts

Once defined, we can use this function type interface like we would other interfaces. Here, we show how you can create a variable of a function type and assign it a function value of the same type.

ts

For function types to correctly type check, the names of the parameters do not need to match. We could have, for example, written the above example like this:

ts

Function parameters are checked one at a time, with the type in each corresponding parameter position checked against each other.
If you do not want to specify types at all, TypeScript’s contextual typing can infer the argument types since the function value is assigned directly to a variable of type `SearchFunc`.
Here, also, the return type of our function expression is implied by the values it returns (here `false` and `true`).

ts

Had the function expression returned numbers or strings, the type checker would have made an error that indicates return type doesn’t match the return type described in the `SearchFunc` interface.

tsmySearch :SearchFunc ;mySearch = function (src ,sub ) {Type '(src: string, sub: string) => string' is not assignable to type 'SearchFunc'. Type 'string' is not assignable to type 'boolean'.2322Type '(src: string, sub: string) => string' is not assignable to type 'SearchFunc'. Type 'string' is not assignable to type 'boolean'.letresult =src .search (sub );return "string";};[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGY1oFAEsA7AFxgDMBDAY0lAGVJzpKALAMQFcDLQBvHUUAApEcdk0ipERaIQDmAGlCJ2AI1rS5kjQVkBKVCrhwANgwIBuHAF8cIUAFpHldkUf2cpoqAC2AT3qMLKgBTGyclJY4fiEsoAC8oKThRHhwBEKITIrKKrq8-KCeoNCQysZeCZmUAHSIDKHCqrqWAiVEYukARFIyOp2WVuZAA)

Similarly to how we can use interfaces to describe function types, we can also describe types that we can “index into” like `a[10]`, or `ageMap["daniel"]`.
Indexable types have an *index signature* that describes the types we can use to index into the object, along with the corresponding return types when indexing.

Let’s take an example:

ts

Above, we have a `StringArray` interface that has an index signature.
This index signature states that when a `StringArray` is indexed with a `number`, it will return a `string`.

There are four types of supported index signatures: string, number, symbol and template strings. It is possible to support many types of indexers, but the type returned from a numeric indexer must be a subtype of the type returned from the string indexer.

This is because when indexing with a `number`, JavaScript will actually convert that to a `string` before indexing into an object.
That means that indexing with `100` (a `number`) is the same thing as indexing with `"100"` (a `string`), so the two need to be consistent.

tsAnimal {name : string;}interfaceDog extendsAnimal {breed : string;}// Error: indexing with a numeric string might get you a completely separate type of Animal!interfaceNotOkay {\[x : number\]:Animal ;'number' index type 'Animal' is not assignable to 'string' index type 'Dog'.2413'number' index type 'Animal' is not assignable to 'string' index type 'Dog'.\[x : string\]:Dog ;}[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwBYCMBmAUCBIgC7QCWAxsQArwAOMxAngJIB2ZxZAhgDZkAvblzhtUAMz6JIeMm2IxJFSKACCHALZ9QAbzyhQbbhsioS5NgHMA3HgC+eWfMXdloACJxLoSAA8FbAAmiGqa2noGAEbQkJCBZqRyNvaOhACisAiocoF+SaAA7pwAFqDchgCuJuQUoOb5GmSWxcSglpCtTHAVZaAUcBp0vB2QvEx1kHTc0MIqzAygcOKhZFq8AIROCtBKKgBycMQA8gDW3OMRoADavqhsVZEwALqo6qt8tgY3CRaWLx5eWx2IA)

While string index signatures are a powerful way to describe the “dictionary” pattern, they also enforce that all properties match their return type.
This is because a string index declares that `obj.property` is also available as `obj["property"]`.
In the following example, `name`’s type does not match the string index’s type, and the type checker gives an error:

tsNumberDictionary {\[index : string\]: number;length : number; // ok, length is a numbername : string; // error, the type of 'name' is not a subtype of the indexerProperty 'name' of type 'string' is not assignable to 'string' index type 'number'.2411Property 'name' of type 'string' is not assignable to 'string' index type 'number'.}[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwBYCMWBQBLAOwBcYAzAQwGNJQA5AVwFsAjGAEXyuPzkIugBPUAG9coUAG0iAE0gAPVImLQiAcwC6qQszbQA3LnGgANpEJriAC226Y+0CFBwA1gBpT5y1dD5EoClAdVhhjfiZIJRV1BycYeGgPa1piQQAHWjgyUABycMgc339COGIA0EQGFlSM52zk30I5eVCAXyA)

However, properties of different types are acceptable if the index signature is a union of the property types:

ts

Finally, you can make index signatures `readonly` in order to prevent assignment to their indices:

tsReadonlyStringArray {readonly \[index : number\]: string;}letmyArray :ReadonlyStringArray = \["Alice", "Bob"\];myArray \[2\] = "Mallory"; // error!Index signature in type 'ReadonlyStringArray' only permits reading.2542Index signature in type 'ReadonlyStringArray' only permits reading.[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwFYAsaBQBLAOwBcYAzAQwGNJQAlSCgEzkIBsBPAZWOiIHMAgrAodQAb1yhQ0Ri3ZiA2kSaQAHqkIBXALYAjGAF1UiXgIDcuAL65cbSMVA6Ow6KNQNmrTjz6EhImIAvKCKAESCbPg0YQA0oGEAQnB6YYaWzq6iimiGoCFhALIUbGwIHGHmoCCgMPDQAIRAA)

You can’t set `myArray[2]` because the index signature is `readonly`.

A template string can be used to indicate that a particular pattern is allowed, but not all. For example, a HTTP headers object may have a set list of known headers and support any [custom defined properties](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) which are prefixed with `x-`.

tsHeadersResponse {"content-type": string,date : string,"content-length": string// Permit any property starting with 'x-'.\[headerName : \`x-${string}\`\]: string;}functionhandleResponse (r :HeadersResponse ) {// Handle known, and x- prefixedconsttype =r \["content-type"\]constpoweredBy =r \["x-powered-by"\]// Unknown keys without the prefix raise errorsconstorigin =r .origin Property 'origin' does not exist on type 'HeadersResponse'.2339Property 'origin' does not exist on type 'HeadersResponse'.}[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYME4BQuBLAOwBcYAzAQwGNJQAJSSgExkQCVJEAHOIxOgG9coUACJqfMqQC0JAJ7dIY1IhLRiAcwA0I0M0plV6rbtESpkWQBsrmkgAsVoNRqKb8okKAAKMALYEJKCURPKg3PBK0AouJJQxWqAA7kEOoADkAB4yGQB0egDaDkys0ABylP6QqAAGOQAkgq5aAL61ALrGbpoA3Lit+OQArkTUJAR8oA6hzLacPHwCABTQqIwsbAu8-JAAlKDCXmD0s7agANZEcMlE2iFEzKA5EdCQ5ARZkMx6kvzBCiUoAAvKBoIULKQrCQ5IplB1fktgrxkjBvgAhcKg8FiHIotHMGQAI3kYgRem8AFUiFcbkRLpB5IgUmk4MMASVXu9PmDKAQBKAYPAkIj-qAEARNMQQWC8hKpUQBkA)

One of the most common uses of interfaces in languages like C# and Java, that of explicitly enforcing that a class meets a particular contract, is also possible in TypeScript.

ts

You can also describe methods in an interface that are implemented in the class, as we do with `setTime` in the below example:

tsClockInterface {currentTime :Date ;setTime (d :Date ): void;}classClock implementsClockInterface {currentTime :Date = newDate ();setTime (d :Date ) {this.currentTime =d ;}constructor(h : number,m : number) {}}[Try](https://www.typescriptlang.org/play/#code/PTAEAEGcBcCcEsDG0AKsD2AHApraBPASQDt5p4BDAG3gC8Lz1iAuUAM2smwCh5jpcHRNlABhKukQBrEgNhCRAb26hQiAK6xY2fgBV4AW2ysAIg2wBuFaC7R9RgBQATU+YCUrAG7p4TqwF9ubkQqCkhIMQlpUENMKmwjfgjxSRl+QQphUGVVDS0dO0NjUDMBUABeUGJsAHcS8wc3K1Vbe2xnVwE3bOtVaAALeEgAOjztPSKK0D9rQNymGFh1ZHRYB37WYnUDACNcABpQA03tvdhuxUD-IA)

Interfaces describe the public side of the class, rather than both the public and private side. This prohibits you from using them to check that a class also has particular types for the private side of the class instance.

When working with classes and interfaces, it helps to keep in mind that a class has *two* types: the type of the static side and the type of the instance side.
You may notice that if you create an interface with a construct signature and try to create a class that implements this interface you get an error:

tsClockConstructor {new (hour : number,minute : number);}classClock implementsClockConstructor {Class 'Clock' incorrectly implements interface 'ClockConstructor'. Type 'Clock' provides no match for the signature 'new (hour: number, minute: number): any'.2420Class 'Clock' incorrectly implements interface 'ClockConstructor'. Type 'Clock' provides no match for the signature 'new (hour: number, minute: number): any'.currentTime :Date ;constructor(h : number,m : number) {}}[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygOwAYCMBmUAmAFnwwIFYA2QgKBAkQBdoBLAYwYAV4AHGBgTwCSAO2YNmAQwA2zAF4TxcYagBm0xJFphwwuIIC23GazEBBYf1XrNzYQxhrWkUAGEpcVgGsXSxtACu7AigAN7UoKDCkADuoAAUABZw-tCowv76AEYwADSg+rb+9mkZ2dAAlADc1AC+1NSsUhKIiK7uXqDMhlKQ+pB2rW4e3r5MgQzBYRGsKdD9DAAqXZCoACIKkNXTowFB0IklWbn5h2XloXU1QA)

This is because when a class implements an interface, only the instance side of the class is checked. Since the constructor sits in the static side, it is not included in this check.

Instead, you would need to work with the static side of the class directly.
In this example, we define two interfaces, `ClockConstructor` for the constructor and `ClockInterface` for the instance methods.
Then, for convenience, we define a constructor function `createClock` that creates instances of the type that is passed to it:

tsClockConstructor {new (hour : number,minute : number):ClockInterface ;}interfaceClockInterface {tick (): void;}functioncreateClock (ctor :ClockConstructor ,hour : number,minute : number):ClockInterface {return newctor (hour ,minute );}classDigitalClock implementsClockInterface {constructor(h : number,m : number) {}tick () {console .log ("beep beep");}}classAnalogClock implementsClockInterface {constructor(h : number,m : number) {}tick () {console .log ("tick tock");}}letdigital =createClock (DigitalClock , 12, 17);letanalog =createClock (AnalogClock , 7, 32);[Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgMIBsD2CDWrMgDOYUArgmJlMgN4BQyyIEA7sgBQAWmpUAXE1IBbAEbQANMiGhSkASGFioASgEZsOAJLho8JAG46AXzp1QkWIhTrc2i3pT1GYYLnarkAN0zAAJoZM6GFIQCmACZAQoCDhIGxx2BkjKfjQsXHwiEnIU8STuXnlFCSTpBTlBUWg6D3i7XStaJOiwXhAmVmSqLh4oSTLZCGUA0wR0OEJCZAARYABzYDA4dHjkYCEAB3QIIQhwKbqdSyQmxgQCYjIKbs4iqr6pO6VlWhNnVwSXp0ZIi8xtgB0WDm7AARGIIBtkBCNqDhkkTIExhMpgBBEDLTBzVbrLY7PZgA7pLRHBynX5ZK4pLhPCSPSrPV5JFxuL5JM5-QHAsEsnDISi4OGGRiI0zbMDIXzzRbLZAAXki0ViEHi7FmCyWK2JkgAjAAmXUAdnh4uQcAxwPlipicWJ7HRmOx2uQhskAGY9cMgA)

Because `createClock`’s first parameter is of type `ClockConstructor`, in `createClock(AnalogClock, 7, 32)`, it checks that `AnalogClock` has the correct constructor signature.

Another simple way is to use class expressions:

tsClockConstructor {new (hour : number,minute : number):ClockInterface ;}interfaceClockInterface {tick (): void;}constClock :ClockConstructor = classClock implementsClockInterface {constructor(h : number,m : number) {}tick () {console .log ("beep beep");}};letclock = newClock (12, 17);clock .tick ();[Try](https://www.typescriptlang.org/play/#code/PTAEAEGcBcCcEsDG0AKsD2AHApraBPASQDt5p4BDAG3gC8Lz1iAuUAM2smwCgQJj0hALaYaiMgEFi+Vhypdu8YtFwdE2UAGEq6RAGtNTGLACuydLFABvbqFDFsAd1AAKABboTsVsRNCARrgANKBCSiYqPn6BsACUrNq6eiQqsGrYANzcAL7cisqqFOpaOvophcU2duT6LvGgAG7o8AAmWbnciEbQJUkJpQbdpuaWALygiFQUkJC9+qDwIlTYQtjKs4llBWlFGlUTQ2bQFu5RAcGhZzGx1rnVSHp11rZ2B8SQ6MsAdDoA5i4AIkC2EwoGBmABsSydly2Sy3GWPUmSVA4wczk2jwAjAAmEJYgDsUM6Ay+NUeUKAA)

Like classes, interfaces can extend each other. This allows you to copy the members of one interface into another, which gives you more flexibility in how you separate your interfaces into reusable components.

ts

An interface can extend multiple interfaces, creating a combination of all of the interfaces.

tsShape {color : string;}interfacePenStroke {penWidth : number;}interfaceSquare extendsShape ,PenStroke {sideLength : number;}letsquare = {} asSquare ;square .color = "blue";square .sideLength = 10;square .penWidth = 5.0;[Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgMoAs4AcUG8BQyyCA9gDYlQBcyAzmFKAOYDc+AvvvqJLIigAUIIVAxIBrPIWQ4QAdWAATMOhogArgFsARtDadu4aPCRoAjurhQUEAB6QQi2mkw4ANMiEixk5ASK0ShAAMsJMKmpaulD6XGQQYHQWVigAvH7syHDOqMnWbLR5EAB0pBRQyOkARNpk6hBVBUXFgYohYSqVyACMAAxNltbFsgrK6F0ArMX9QA)

As we mentioned earlier, interfaces can describe the rich types present in real world JavaScript. Because of JavaScript’s dynamic and flexible nature, you may occasionally encounter an object that works as a combination of some of the types described above.

One such example is an object that acts as both a function and an object, with additional properties:

tsCounter {(start : number): string;interval : number;reset (): void;}functiongetCounter ():Counter {letcounter = function (start : number) {} asCounter ;counter .interval = 123;counter .reset = function () {};returncounter ;}letc =getCounter ();c (10);c .reset ();c .interval = 5.0;[Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgMIHsCu5rIN4BQyyAFAM5hxRgBcyImAtgEbQCUdFUoA5gNxFkoSFABucADZ0GLaAOJQIZCGBIdko9MAAmAgL4ECMbAjDB0IZDxUZsItXVs4o+QRJXIEWZ8gC8yYxBTc0tySmppJlYoNnw9ZDgyNG8ReU8U6AA6YWhxCT9kAEYAJgBmNK87LMVlMALA4ItSWLw9NMUwTChLSud9Q3c6hALrMCd7NgEEEkKABkmCBEyalTUp7Oc8goBWTNm+IA)

When interacting with 3rd-party JavaScript, you may need to use patterns like the above to fully describe the shape of the type.

When an interface type extends a class type it inherits the members of the class but not their implementations. It is as if the interface had declared all of the members of the class without providing an implementation. Interfaces inherit even the private and protected members of a base class. This means that when you create an interface that extends a class with private or protected members, that interface type can only be implemented by that class or a subclass of it.

This is useful when you have a large inheritance hierarchy, but want to specify that your code works with only subclasses that have certain properties. The subclasses don’t have to be related besides inheriting from the base class. For example:

tsControl {privatestate : any;}interfaceSelectableControl extendsControl {select (): void;}classButton extendsControl implementsSelectableControl {select () {}}classTextBox extendsControl {select () {}}classImageControl implementsSelectableControl {Class 'ImageControl' incorrectly implements interface 'SelectableControl'. Types have separate declarations of a private property 'state'.2420Class 'ImageControl' incorrectly implements interface 'SelectableControl'. Types have separate declarations of a private property 'state'.privatestate : any;select () {}}[Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAMX0BY1dMcAoAYwBsBDRRUAYTgDsAXeC0AbxNFAAdoASwBuVFpFCIWYyKipMAngG4SAXxIlBrGADMqZCQGVIFSGWkAjU41btQkAB7imAEzo22cDt16ITZlgAKAEpUYThBFxV1cmpaUAAhAFcWFmZ7J0hXd2ZPDkEAWz5TAqyWOmNTcyorSA87H0l-cxCudRjKGjoAFUcWBLgHDOc3BlyGniaqoOC2tQ1O+IBJAqoAczrxr1BC4shS1grmy2st70mBERlJaXE5RRVfY9bOdqA)

In the above example, `SelectableControl` contains all of the members of `Control`, including the private `state` property.
Since `state` is a private member it is only possible for descendants of `Control` to implement `SelectableControl`.
This is because only descendants of `Control` will have a `state` private member that originates in the same declaration, which is a requirement for private members to be compatible.

Within the `Control` class it is possible to access the `state` private member through an instance of `SelectableControl`.
Effectively, a `SelectableControl` acts like a `Control` that is known to have a `select` method.
The `Button` and `TextBox` classes are subtypes of `SelectableControl` (because they both inherit from `Control` and have a `select` method). The `ImageControl` class has its own `state` private member rather than extending `Control`, so it cannot implement `SelectableControl`.