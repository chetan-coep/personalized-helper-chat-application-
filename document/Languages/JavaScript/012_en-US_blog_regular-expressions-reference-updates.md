---
id: "javascript_012"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 12
source_url: "https://developer.mozilla.org/en-US/blog/regular-expressions-reference-updates"
language: "en"
retrieved_at: "2026-11-01 21:53:34"
content_hash: "d4dab0f2c3f9308147815108e5f883b06774895f122df1efe041c698ccd1de75"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/regular-expressions-reference-updates

---

# New reference pages on MDN for JavaScript regular expressions

Our JavaScript regular expressions (regex) documentation is one of the most popular resources on MDN Web Docs.
Thanks to the efforts of [Joshua Chen](https://github.com/Josh-Cena), we now have dedicated pages for each feature with more comprehensive information about the syntax and semantics, with browser compatibility information included.
Let's take a look at the new pages, how the information is organized, and how the new documentation can help you write regular expressions in JavaScript.

## [JavaScript regular expressions guide](https://developer.mozilla.org#javascript_regular_expressions_guide)

Before this initiative, we started off with a [regular expressions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) that explains what regular expressions are and how to use them in JavaScript.
The guide has a few sub-pages that split out content into the following sections:

These guides and the cheat sheet are great if you are new to regex or you need a refresher on the basic concepts. What we were missing were accelerators for readers who are already familiar with the basics and want to quickly look up the specific details of a language feature.

The first step to refresh this topic and add new documentation was a [GitHub discussion](https://github.com/orgs/mdn/discussions/196) to gather feedback, followed by an initial [pull request by Josh](https://github.com/mdn/content/pull/22210) with suggested changes and a scaffold for the new pages.
After a few rounds of revisions, we're happy to have the changes land in MDN's content repository and the new pages are now live.

## [Regular expressions reference pages](https://developer.mozilla.org#regular_expressions_reference_pages)

The [regular expressions reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions) is the entry point for all of the new documentation.
There are 18 new pages for individual features, and existing content with deprecated information has been removed.
The new references are organized into the following sections and categories:

- [Creating regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#creating_regular_expressions) - how to create a regular expression in JavaScript
- [Flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#regex_flags) - the flags that change how a regex is interpreted
- [Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#assertions) - if a pattern matches a condition, such as the start of a string or a word boundary
- [Atoms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#atoms) - the units that make up a pattern, such as character classes and literal characters
- [Other features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#other_features) - features like quantifiers that help you compose patterns

The content [organized under atoms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#atoms) is where most of the new docs are located, and it's likely where you'll spend most of your time if you're looking to compose a regex.
With the information organized into sections like this, there's now a clear path to find the information you need or gain a deeper understanding of how features work.

Having a reference for each feature means it appears more prominently in search results and is easier to locate. Additionally, each page is included in the sidebar navigation, so if you've landed on the documentation for a feature but meant to look up something else, you should be able to find it quickly.

### [Highlights from the new pages](https://developer.mozilla.org#highlights_from_the_new_pages)

The new pages are comprehensive in terms of syntax and semantics, with a description section that hopefully will help you understand when there are gotchas or caveats to be aware of. Aside from the syntax and semantics, it's always helpful to see examples of using a feature. Let's look at some of the examples that are my favorites in the following few sections.

### [Capturing groups and named capturing groups](https://developer.mozilla.org#capturing_groups_and_named_capturing_groups)

The [capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group) reference has a nice example that shows how to match a date in the format `YYYY-MM-DD` and extract the year, month, and day.
This is useful because it's a common operation that you might need to do without the overhead of a full date parsing library:

```
function parseDate(input) {
  const parts = /^(\d{4})-(\d{2})-(\d{2})$/.exec(input);
  if (!parts) {
    return null;
  }
  return parts.slice(1).map((p) => parseInt(p, 10));
}
parseDate("2019-01-01"); // [2019, 1, 1]
parseDate("2019-06-19"); // [2019, 6, 19]
```
One of the most common complaints about regular expressions is how hard they are to read.
If you're using capturing groups, you can use [named capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#using_named_capturing_groups) to make your patterns a bit easier to understand:

```
function parseLog(entry) {
  const { author, timestamp } = /^(?<timestamp>\d+),(?<author>.+)$/.exec(
    entry,
  ).groups;
  return `${author} committed on ${new Date(
    parseInt(timestamp) * 1000,
  ).toLocaleString()}`;
}
parseLog("1560979912,Caroline"); // "Caroline committed on 6/19/2019, 5:31:52 PM"
```
This one is nice because it shows how to parse a log entry, extract the timestamp and author, and format the result into something more readable. Someone reading the code for the first time will have an easier time understanding what the regex is doing.

#### Unicode character class escape

The [Unicode character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#scripts_and_script_extensions) page has a great example that illustrates how to detect if a string contains a character from different scripts.
This can be useful if you are trying to detect strings in different languages without having to manually or exhaustively specify certain characters (or ranges of characters) in your pattern:

```
const mixedCharacters = "aÎµÐ";
// Using the canonical "long" name of the script
mixedCharacters.match(/\p{Script=Latin}/u); // a
// Using a short alias (ISO 15924 code) for the script
mixedCharacters.match(/\p{Script=Grek}/u); // Îµ
// Using the short name sc for the Script property
mixedCharacters.match(/\p{sc=Cyrillic}/u); // Ð
```
#### Character classes

The regular expressions [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class) might be considered one of the most basic features, but there is an example on the reference page showing how they can be powerful in certain use cases.
The example shows how to match hexadecimal digits, and I like this because it illustrates how ranges work in combination with the `i` flag to match without case sensitivity:

```
function isHexadecimal(str) {
  return /^[0-9A-F]+$/i.test(str);
}
isHexadecimal("2F3"); // true
isHexadecimal("beef"); // true
isHexadecimal("undefined"); // false
```
### [Browser compatibility information](https://developer.mozilla.org#browser_compatibility_information)

Each of the regular expressions reference pages have [browser compatibility data](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#browser_compatibility) for the corresponding feature.
This means that the browser support information is now more granular and you can see the browser versions that support or don't support a feature.

## [What's next?](https://developer.mozilla.org#whats_next)

The regular expressions references will help more advanced users find the information they need quickly and also help beginners learn more about regular expressions.
These references will also greatly help with documenting the new `v` mode that is currently in development and is expected to add support for set difference/subtraction, set intersection, and nested character classes.
Having individual reference pages for each regular expression feature will make it easier to give a more detailed explanation of the new features using the `v` flag.
For more information on this flag, check out the [TC39 proposal](https://github.com/tc39/proposal-regexp-v-flag).

## [Summary](https://developer.mozilla.org#summary)

We've covered some of the highlights of the new regular expressions reference pages and I hope you find them useful. We're happy to have this new content with the significant improvements made by Josh and the rest of the MDN Web Docs team. If you want to dive in to the new pages, be sure to check out these landing pages for the references and the guide:

If you enjoyed this article or if you have any feedback, feel free to join the discussion in the MDN Web Docs [Discord server](https://developer.mozilla.org/discord) or leave a comment on the [GitHub discussion](https://github.com/orgs/mdn/discussions/categories/the-mdn-web-docs-blog).

Happy pattern matching!