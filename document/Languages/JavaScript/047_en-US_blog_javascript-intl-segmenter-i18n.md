---
id: "javascript_047"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 47
source_url: "https://developer.mozilla.org/en-US/blog/javascript-intl-segmenter-i18n"
language: "en"
retrieved_at: "2026-11-01 21:52:50"
content_hash: "95fec385dde61defdb9469f84502c77e92690cf0a3fdeebc45d332ae1c2675ef"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/javascript-intl-segmenter-i18n

---

# Locale-sensitive text segmentation in JavaScript with Intl.Segmenter

Earlier this year, the JavaScript [`Intl.Segmenter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter) object gained support in all three major browser engines, meaning it's achieved [Baseline status](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) of "newly available".
Now, your applications can natively retrieve meaningful information from strings in a variety of locales in the latest browsers.
This is great news for developers that are building locale-aware apps or UIs and writing custom handling or using third-party libraries for this purpose.
Let's explore what this opens up with some hands-on examples.

## [What is text segmentation used for?](https://developer.mozilla.org#what_is_text_segmentation_used_for)

Text segmentation is a way to divide text into units like characters, words, and sentences. Let's say you have the following Japanese text and you'd like to perform a word count:

å¾è¼©ã¯ç«ã§ãããååã¯ãã¬ãã


If you're unfamiliar with Japanese, you might try built-in string methods in your first attempt. For English strings, a rough way to count the words is to split by space characters:

```
const str = "How many words. Are there?";
const words = str.split(" ");
console.log(words);
// ["How","many","words.","Are","there?"]
console.log(words.length);
// 5
```
The punctuation is mixed in with the word matches, and this will be inaccurate, but it's a good approximation.
The problem is we don't have any spaces separating the characters in the Japanese string.
Maybe your next idea would be to reach for `str.length` to count the characters.
Using string length, you'd get `15`, and if you remove the full stops (`ã`) you might guess **13 words**.

The problem is we actually have **8 words** in the string without punctuation: `'å¾è¼©' 'ã¯' 'ç«' 'ã§' 'ãã' 'åå' 'ã¯' 'ãã¬ã'`.
If you rely on string methods for a word count, you'll quickly run into trouble as you can't reliably split by specific character and you can't use spaces as separators like you can in English.

This is what locale-sensitive segmentation is built for.
The format for creating a segmenter in the `Intl` namespace is as follows:

```
new Intl.Segmenter(locales, options);
```
Let's try passing the string into the segmenter with the `ja-JP` locale for Japanese, and we explicitly set each segment to be of word-level granularity:

```
const jaSegmenter = new Intl.Segmenter("ja-JP", { granularity: "word" });
const segments = jaSegmenter.segment("å¾è¼©ã¯ç«ã§ãããååã¯ãã¬ãã");
console.log(Array.from(segments));
```
This example logs the following array to the console:

```
[
  {
    "segment": "å¾è¼©",
    "index": 0,
    "input": "å¾è¼©ã¯ç«ã§ãããååã¯ãã¬ãã",
    "isWordLike": true
  },
  {
    "segment": "ã¯",
    "index": 2,
    "input": "å¾è¼©ã¯ç«ã§ãããååã¯ãã¬ãã",
    "isWordLike": true
  },
  {
    "segment": "ç«",
    "index": 3,
    "input": "å¾è¼©ã¯ç«ã§ãããååã¯ãã¬ãã",
    "isWordLike": true
  },
  // etc.
```
For each item in the array, we get the segment, it's index as it appears in the original string, the full input string, and a Boolean `isWordLike` to disambiguate words from punctuation etc.
Now we have a robust and structured way to interact with the words that is locale-aware.
The segmenter's granularity is `word` in this example, so we can filter each item based on whether it's `isWordLike` to ignore punctuation:

```
const jaString = "å¾è¼©ã¯ç«ã§ãããååã¯ãã¬ãã";
const jaSegmenter = new Intl.Segmenter("ja-JP", { granularity: "word" });
const segments = jaSegmenter.segment(jaString);
const words = Array.from(segments)
  .filter((item) => item.isWordLike)
  .map((item) => item.segment);
console.log(words);
// ["å¾è¼©","ã¯","ç«","ã§","ãã","åå","ã¯","ãã¬ã"]
console.log(words.length);
// 8
```
This looks much better. We have an array with Japanese words using the segmenter, ready for adding locale-aware word count to our application. We'll explore that use case a bit more with a small example in the following sections. Before that, we'll take a look at the rest of the options that you can pass into a segmenter.

## [Intl.Segmenter options and configuration](https://developer.mozilla.org#intl.segmenter_options_and_configuration)

We've seen above that you can split input by `word` according to the locale.
If you don't pass any options, the default behavior is to split by `grapheme`, which is the user-perceived **character**.
This is useful if you're doing a character count on strings in different encodings or languages where characters are made of combined characters such as `à¤à¤¿à¤à¤¤à¥` in Hindi:

```
const str = "à¤à¤¿à¤à¤¤à¥";
console.log(str.length);
// 5 <- oops
const hindiSegmenter = new Intl.Segmenter("hi");
const hindiSegments = hindiSegmenter.segment(str);
const hiGraphemes = Array.from(hindiSegments).map((item) => item.segment);
console.log(hiGraphemes);
// ["à¤à¤¿à¤","à¤¤à¥"]
console.log(hiGraphemes.length);
// 2 <- looks better
```
The last option you might need is to segment text by sentence, which is also very convenient if you don't want to keep track of language-specific full-stops.
Some languages may use a period character `.`, but this is not always consistent.
Let's take the following example:

```
const hindiText = "à¤µà¤¾à¤à¥à¤¯ à¤à¤à¥¤ à¤µà¤¾à¤à¥à¤¯ à¤¦à¥à¥¤"; // <- what do I split on here?
const hiSegmenter = new Intl.Segmenter("hi", { granularity: "sentence" });
const hiSegments = hiSegmenter.segment(hindiText);
const hiSentences = Array.from(hiSegments).map((item) => item.segment);
console.log(hiSentences);
// ["à¤µà¤¾à¤à¥à¤¯ à¤à¤à¥¤ ","à¤µà¤¾à¤à¥à¤¯ à¤¦à¥à¥¤"]
console.log(hiSentences.length);
// 2
```
In another Hindi example, we have a character that looks similar to a pipe (`à¥¤`) that's separating sentences.
Now you don't have to track Western periods or other locale-specific equivalents to split text into sentences.

If you want to check support for a locale, you can use [`supportedLocalesOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/supportedLocalesOf).
This returns an array with the provided locales that are supported in segmentation without having to fall back to the default locale.
The following checks if the segmenter can use Hindi, Japanese, and German for segmentation:

```
console.log(Intl.Segmenter.supportedLocalesOf(["hi", "ja-JP", "de"]));
// Array ["hi", "ja-JP", "de"] <- all are supported
```
## [Japanese locale word count example](https://developer.mozilla.org#japanese_locale_word_count_example)

If your browser supports `Intl.Segmenter`, you can try out the following example.
There's some Japanese text from Wikipedia, and a `<pre>` element below it to show the output of our script.

```
<p id="text-content">
  ã¦ã£ãããã£ã¢æ¥æ¬èªçç¨ã®ã¦ã£ãã¯2001å¹´5æé ã«éè¨ããã¾ããããå½åã¯ã½ããã¦ã§ã¢ãæ¥æ¬èªã®æåã«å¯¾å¿ãã¦ããªãã£ãããããã¼ãåã§æ¸ããã¦ãã¾ãããæ¥æ¬èªçã¨ãã¦ã®å®è³ªçãªå·çã»ç·¨éãéå§ãããã®ã¯ãæ¥æ¬èªã®æåãä½¿ç¨åºæ¥ãæ§ã«ãªã£ã2002å¹´9æä»¥éã®ãã¨ã§ããç¾å¨ã§ã¯1,428,684é 
ç®ã®è¨äºãä½æããã¦ãããåè¨èªçã®ä¸ã§ãè¦æ¨¡ã®å¤§ããç©ã®ä¸ã¤ã«ãªã£ã¦ãã¾ããã¦ã£ãããã£ã¢æ¥æ¬èªçã®æ©ã¿ã«ã¤ãã¦ã¯Wikipedia:çºè¡¨ããåç
§ãã ããã
</p>
<pre id="word-count">Word count: 0</pre>
```
If you've followed all of the snippets so far, you shouldn't see anything surprising here.
The only difference is that we're getting the selected text using [`window.getSelection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getSelection) before passing that into the segmenter which we've wrapped in a function.
After that, we're listening for the [`mouseup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event) event when it's fired on the paragraph and adding the output of the `countSelection` function to the `<pre>` element:

```
function countSelection() {
  const selection = window.getSelection();
  const selectedText = selection.toString();
  const jaSegmenter = new Intl.Segmenter("ja-JP", { granularity: "word" });
  const segments = jaSegmenter.segment(selectedText);
  const words = Array.from(segments)
    .filter((item) => item.isWordLike)
    .map((item) => item.segment);
  document.getElementById("word-count").textContent =
    `Word count: ${words.length}\n - "${words}"`;
}
document
  .getElementById("text-content")
  .addEventListener("mouseup", countSelection);
```
To try it out, select some of the Japanese text below with your mouse.
On `mouseup`, we log the word count along with the output of the segmenter with word-level granularity:

## [Further reading](https://developer.mozilla.org#further_reading)

If you want to learn more about `Intl.Segmenter`, you can have a read through these other resources:

- [The Intl.Segmenter object is now part of Baseline](https://web.dev/blog/intl-segmenter) on web.dev (2024)
- [Using the Intl segmenter API](https://polypane.app/blog/using-the-intl-segmenter-api/) polypane.app (2023)
- [International Text Segmentation with Intl.Segmenter in JavaScript](https://javascript.plainenglish.io/international-text-segmentation-with-intl-segmenter-in-javascript-639eb1865263) by Zachary Lee (2023)
- [Intl.Segmenter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter) reference page

## [Summary](https://developer.mozilla.org#summary)

Developers now have better ergonomics for locale-sensitive text segmentation with JavaScript in the latest browsers.
This feature is particularly useful for handling non-Latin languages, where the usual string manipulation methods will be unreliable.
If your app needs to handle multiple locales and you're regularly working with text manipulation, `Intl.Segmenter` can help segment text by word, characters, or sentences based on locale.
This simplifies tasks such as word or character count, sentence-splitting, string comparisons and more advanced text processing.

Feel free to [get in touch with us](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels) and let me know what you think or if I've missed something.
I hope you enjoyed this post and have fun adding more i18n to your apps and pages.