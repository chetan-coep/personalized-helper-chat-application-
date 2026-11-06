---
id: "javascript_048"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 48
source_url: "https://developer.mozilla.org/en-US/blog/javascript-set-methods"
language: "en"
retrieved_at: "2026-11-01 21:52:51"
content_hash: "8c357b0c0fe039d5c4faa9dec174861af67190462637611368a8d4689ff68c36"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/javascript-set-methods

---

New JavaScript `Set` methods are arriving!
Since [Firefox 127](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/127#javascript), these methods are available in most major browser engines, which means you won't need [a polyfill to make them work](https://github.com/zloirock/core-js?tab=readme-ov-file#set) everywhere.

This article is a good read for people who are new to `Set` in JavaScript and are looking to find out how to use these new JavaScript methods.
I'll highlight some advantages of using these methods with basic examples to show why you might reach for these instead of building your own implementations.

For those of you looking for the TL;DR, here's the gist of new methods that have cross-browser support:

- [`intersection()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection) returns a new set with elements in both this set and the given set.
- [`union()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union) returns a new set with all elements in this set and the given set.
- [`difference()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/difference) returns a new set with elements in this set but not in the given set.
- [`symmetricDifference()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/symmetricDifference) returns a new set with elements in either set, but not in both.
- [`isSubsetOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isSubsetOf) returns a boolean indicating if all elements of a set are in a specific set.
- [`isSupersetOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isSupersetOf) returns a boolean indicating if all elements of a set are in a specific set.
- [`isDisjointFrom()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isDisjointFrom) returns a boolean indicating if this set has no elements in common with a specific set.

If you've read (or skimmed) through the above list and are confused, don't worry, we'll describe what they do in the following sections.
Each of these methods are used to check what the contents of sets are compared to the contents of another specific set.

A set is similar to an [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), except that each value can only be stored once.
For example, we can take a list of items, add them all to a set, and then inspect the results of the set.
The list on the right is the contents of the `<ol>` list on the left, but converted to a set.
We have all duplicates removed from the list because we're guaranteed that a set is unique:

```
<div id="container">
  <div>
    <span>My list</span>
    <ol>
      <li>apple</li>
      <li>pear</li>
      <li>carrot</li>
      <li>pear</li>
      <li>apple</li>
      <li>yoshi</li>
    </ol>
  </div>
  <div>
    <span>My set</span>
    <ol id="set"></ol>
  </div>
</div>
```

```
const allListItems = document.querySelectorAll("li");
const setList = document.getElementById("set");
// Create a new set and add list items
const mySet = new Set();
allListItems.forEach((item) => {
  mySet.add(item.textContent);
});
// List the items in the set
mySet.forEach((item) => {
  const li = document.createElement("li");
  li.textContent = item;
  setList.appendChild(li);
});
```

```
body {
  font-family: monospace;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
```

This might not look like much in a small example such as this, but it's really convenient to have a built-in way to make unique collections of items, especially over larger data and more complex data types and objects.
For example, consider that you can add elements to a set like so:

```
const dogs = new Set();
const yoshi = { name: "Yoshi", personality: "Friendly" };
dogs.add(yoshi);
```

It's also typically faster to check if an element is in a set as opposed to in an Array, so this fits use cases where you need to keep an eye on performance in larger data sets.
You can also compose new sets with specific logical properties based on existing sets, and we'll take a look at some examples of that below.

We'll be covering all of the new methods below, but if you want to see everything you can do with a `Set`, check the [Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#instance_methods) documentation.

This is a good example to start us off if you're not familiar with sets.
With the union, we can check what elements are in 'either or both' sets.
In the example below, we have two lists and we want to make a third one that contains all items from both lists, but without duplicates:

```
<div id="container">
  <div>
    <span>Set one</span>
    <ol id="set-one">
      <li>apple</li>
      <li>banana</li>
      <li>pear</li>
      <li>carrot</li>
    </ol>
  </div>
  <div>
    <span>Set two</span>
    <ol id="set-two">
      <li>banana</li>
      <li>peach</li>
      <li>plum</li>
      <li>apple</li>
    </ol>
  </div>
  <div>
    <span>Union set</span>
    <ol id="union"></ol>
  </div>
</div>
```

```
body {
  font-family: monospace;
}
.match {
  color: cornflowerblue;
  font-weight: bold;
  text-decoration: underline;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
```

```
const listOneItems = document.querySelectorAll("#set-one li");
const listTwoItems = document.querySelectorAll("#set-two li");
const allListItems = document.querySelectorAll("li");
const unionList = document.getElementById("union");
// Create sets for each list
const set1 = new Set();
const set2 = new Set();
// Add list items to each set
listOneItems.forEach((item) => {
  set1.add(item.textContent);
});
listTwoItems.forEach((item) => {
  set2.add(item.textContent);
});
```

```
// Create a union of both sets
const unionSet = set1.union(set2);
// List the items in the union
unionSet.forEach((item) => {
  const li = document.createElement("li");
  li.textContent = item;
  unionList.appendChild(li);
});
```

We're using the HTML [`textContent`](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent) of each list item so we have sets of strings, but you can see how this can be powerful if we consider that sets can contain data types like arrays or objects.

This is helpful because we don't need any custom implementations to remove duplicates, do equality checks, or make other comparisons.
Once we have elements in a set, we know they're all unique, and the `union` method is an optimized way to make a third set of (unique) items that appear in 'either or both' sets.

With set intersection, we can check what elements occur in both sets to see what the overlap is.
In this example, instead of displaying the intersection set as a third list like we did with `union` above, we can use it to highlight elements that are 'both sets only':

```
<div id="container">
  <div>
    <span>Set one</span>
    <ol id="set-one">
      <li>apple</li>
      <li>banana</li>
      <li>pear</li>
      <li>carrot</li>
      <li>plum</li>
    </ol>
  </div>
  <div>
    <span>Set two</span>
    <ol id="set-two">
      <li>banana</li>
      <li>peach</li>
      <li>plum</li>
      <li>celery</li>
      <li>apricots</li>
    </ol>
  </div>
</div>
```

```
body {
  font-family: monospace;
}
.match {
  color: cornflowerblue;
  font-weight: bold;
  text-decoration: underline;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
```

```
const listOneItems = document.querySelectorAll("#set-one li");
const listTwoItems = document.querySelectorAll("#set-two li");
const allListItems = document.querySelectorAll("li");
// Create sets for each list
const set1 = new Set();
const set2 = new Set();
// Add list items to each set
listOneItems.forEach((item) => {
  set1.add(item.textContent);
});
listTwoItems.forEach((item) => {
  set2.add(item.textContent);
});
```

```
// Make the intersection set
const intersectionSet = set1.intersection(set2);
// Loop through lists and highlight if they're in the intersection
allListItems.forEach((item) => {
  if (intersectionSet.has(item.textContent)) {
    item.className = "match";
  }
});
```

Before we look at difference, let's look at `symmetricDifference` which might sound complex, but hopefully the example below demystifies that.
What the symmetric difference does is lets us check which elements are in either set, but **not both**.

```
<div id="container">
  <div>
    <span>Set one</span>
    <ol id="set-one">
      <li>apple</li>
      <li>banana</li>
      <li>pear</li>
      <li>carrot</li>
      <li>plum</li>
    </ol>
  </div>
  <div>
    <span>Set two</span>
    <ol id="set-two">
      <li>banana</li>
      <li>peach</li>
      <li>plum</li>
      <li>celery</li>
      <li>apricots</li>
    </ol>
  </div>
</div>
```

```
body {
  font-family: monospace;
}
.match {
  color: cornflowerblue;
  font-weight: bold;
  text-decoration: underline;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
```

```
const listOneItems = document.querySelectorAll("#set-one li");
const listTwoItems = document.querySelectorAll("#set-two li");
const allListItems = document.querySelectorAll("li");
// Create sets for each list
const set1 = new Set();
const set2 = new Set();
// Add list items to each set
listOneItems.forEach((item) => {
  set1.add(item.textContent);
});
listTwoItems.forEach((item) => {
  set2.add(item.textContent);
});
```

```
const setNotBoth = set1.symmetricDifference(set2);
allListItems.forEach((item) => {
  if (setNotBoth.has(item.textContent)) {
    item.className = "match";
  }
});
```

If this is all new and you're struggling to understand, compare the *symmetric difference* with the *intersection* example.
You should see that the `symmetricDifference` method does the opposite logical operation of the `intersection`.

With set difference, we can check which elements are in one set but not in another.
For this example, we are creating two new sets instead of one.
The first one (`set1only`) is created with `set1.difference(set2)` and what we get back is a new set of items that are 'set one only'.
We do the same with the new set `set2only` to find items that are in set two but not in the first one.
For each list, we can use the sets created with `difference` to highlight list items that don't appear in the other list.

```
<div id="container">
  <div>
    <span>Set one</span>
    <ol id="set-one">
      <li>apple</li>
      <li>banana</li>
      <li>pear</li>
      <li>carrot</li>
      <li>plum</li>
    </ol>
  </div>
  <div>
    <span>Set two</span>
    <ol id="set-two">
      <li>banana</li>
      <li>peach</li>
      <li>plum</li>
      <li>celery</li>
      <li>apricots</li>
    </ol>
  </div>
</div>
```

```
body {
  font-family: monospace;
}
.setOneMatch {
  color: cornflowerblue;
  font-weight: bold;
  text-decoration: underline;
}
.setTwoMatch {
  color: orange;
  font-weight: bold;
  text-decoration: underline;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
```

```
const listOneItems = document.querySelectorAll("#set-one li");
const listTwoItems = document.querySelectorAll("#set-two li");
const allListItems = document.querySelectorAll("li");
// Create sets for each list
const set1 = new Set();
const set2 = new Set();
// Add list items to each set
listOneItems.forEach((item) => {
  set1.add(item.textContent);
});
listTwoItems.forEach((item) => {
  set2.add(item.textContent);
});
```

```
const set1only = set1.difference(set2);
const set2only = set2.difference(set1);
allListItems.forEach((item) => {
  if (set1only.has(item.textContent)) {
    item.className = "setOneMatch";
  } else if (set2only.has(item.textContent)) {
    item.className = "setTwoMatch";
  }
});
```

The last of the new methods and concepts that we can explore are subset, superset, and 'disjoint from' methods.
By now, you're familiar with the set operations that return new sets.
The subset, superset, and disjoint from methods don't return new sets, but a [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) value to indicate certain state or logical checks.

The first two we can look at are **subset** and **superset**.
Instead of highlighting list items, we have some statements or assertions like "Set one is a subset of set two".
We then add some text (`TRUE` / `FALSE`) to the list item depending on the result of a check like `if (set1.isSupersetOf(set2))`:

```
<div id="container">
  <div>
    <span>Set one</span>
    <ul id="set-one">
      <li>A</li>
      <li>B</li>
      <li>C</li>
    </ul>
  </div>
  <div>
    <span>Set two</span>
    <ul id="set-two">
      <li>A</li>
      <li>B</li>
      <li>C</li>
      <li>D</li>
      <li>E</li>
    </ul>
  </div>
</div>
<span>Subsets:</span>
<ul id="assertions">
  <li id="1subset2">Set one is a subset of set two</li>
  <li id="2subset1">Set two is a subset of set one</li>
</ul>
<span>Supersets:</span>
<ul id="assertions">
  <li id="1superset2">Set one is a superset of set two</li>
  <li id="2superset1">Set two is a superset of set one</li>
</ul>
```

```
const listOneItems = document.querySelectorAll("#set-one li");
const listTwoItems = document.querySelectorAll("#set-two li");
const assertItems = document.querySelectorAll("#assertions li");
// subsets
const oneSubTwo = document.getElementById("1subset2");
const twoSubOne = document.getElementById("2subset1");
// supersets
const oneSupTwo = document.getElementById("1superset2");
const twoSupOne = document.getElementById("2superset1");
// Create sets
const set1 = new Set();
const set2 = new Set();
// Add list items to each set
listOneItems.forEach((item) => {
  set1.add(item.textContent);
});
listTwoItems.forEach((item) => {
  set2.add(item.textContent);
});
if (set2.isSubsetOf(set1)) {
  twoSubOne.textContent += " [TRUE]";
} else {
  twoSubOne.textContent += " [FALSE]";
}
if (set1.isSupersetOf(set2)) {
  oneSupTwo.textContent += " [TRUE]";
} else {
  oneSupTwo.textContent += " [FALSE]";
}
if (set2.isSupersetOf(set1)) {
  twoSupOne.textContent += " [TRUE]";
} else {
  twoSupOne.textContent += " [FALSE]";
}
```

```
if (set1.isSubsetOf(set2)) {
  oneSubTwo.textContent += " [TRUE]";
} else {
  oneSubTwo.textContent += " [FALSE]";
}
```

```
body {
  font-family: sans-serif;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
li {
  font-weight: bold;
}
#container ul {
  border-radius: 10px;
  display: flex;
  gap: 2rem;
  padding: 1rem;
  justify-content: space-evenly;
  list-style: none;
  border: 1px solid black;
}
#set-one {
  background-color: paleturquoise;
}
#set-two {
  background-color: lightsteelblue;
}
```

So with **subset**, we can check if all the items from a set appear in another set or not.
With **superset**, we're doing the opposite, to see if a set has all items from another set, plus some additional items.

The last method for us to look at is `isDisjointFrom()` where we can find out if two sets have **no common elements**.
The first and second sets below are not disjoint from each other as they have one element ("C") in common.
The third set is disjoint from the other two as it has no items in common with either set:

```
<div id="container">
  <div>
    <span>Set one</span>
    <ul id="set-one">
      <li>A</li>
      <li>B</li>
      <li>C</li>
    </ul>
  </div>
  <div>
    <span>Set two</span>
    <ul id="set-two">
      <li>C</li>
      <li>D</li>
      <li>E</li>
    </ul>
  </div>
  <div>
    <span>Set three</span>
    <ul id="set-three">
      <li>F</li>
      <li>G</li>
      <li>H</li>
    </ul>
  </div>
</div>
<span>Disjoint from:</span>
<ul>
  <li id="1disjointFrom2">Set one is disjoint from set two</li>
  <li id="2disjointFrom3">Set two is disjoint from set three</li>
  <li id="3disjointFrom1">Set three is disjoint from set one</li>
</ul>
```

```
body {
  font-family: sans-serif;
}
#container {
  display: flex;
  gap: 1rem;
  justify-content: space-evenly;
}
li {
  font-weight: bold;
}
#container ul {
  border-radius: 10px;
  display: flex;
  gap: 2rem;
  padding: 1rem;
  justify-content: space-evenly;
  list-style: none;
  border: 1px solid black;
}
#set-one {
  background-color: paleturquoise;
}
#set-two {
  background-color: lightsteelblue;
}
#set-three {
  background-color: lavender;
}
```

```
const listOneItems = document.querySelectorAll("#set-one li");
const listTwoItems = document.querySelectorAll("#set-two li");
const listThreeItems = document.querySelectorAll("#set-three li");
// Create sets
const set1 = new Set();
const set2 = new Set();
const set3 = new Set();
// Add list items to each set
listOneItems.forEach((item) => {
  set1.add(item.textContent.trim());
});
listTwoItems.forEach((item) => {
  set2.add(item.textContent.trim());
});
listThreeItems.forEach((item) => {
  set3.add(item.textContent.trim());
});
// Assertions
const oneDisjointTwo = document.getElementById("1disjointFrom2");
const twoDisjointThree = document.getElementById("2disjointFrom3");
const threeDisjointOne = document.getElementById("3disjointFrom1");
if (set1.isDisjointFrom(set2)) {
  oneDisjointTwo.textContent += " [TRUE]";
} else {
  oneDisjointTwo.textContent += " [FALSE]";
}
if (set2.isDisjointFrom(set3)) {
  twoDisjointThree.textContent += " [TRUE]";
} else {
  twoDisjointThree.textContent += " [FALSE]";
}
if (set3.isDisjointFrom(set1)) {
  threeDisjointOne.textContent += " [TRUE]";
} else {
  threeDisjointOne.textContent += " [FALSE]";
}
```

I hope you enjoyed this post about `Set` methods and why I think sets are an interesting concept to understand.
Do you know different ways to use these methods in real-world examples?
Feel free to [get in touch with us](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels) and let me know what you think or if I've missed something!
You should be all `Set` for your next project, so see you next time!