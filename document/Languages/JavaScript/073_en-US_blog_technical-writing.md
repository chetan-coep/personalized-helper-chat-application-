---
id: "javascript_073"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 73
source_url: "https://developer.mozilla.org/en-US/blog/technical-writing"
language: "en"
retrieved_at: "2026-11-01 21:53:47"
content_hash: "7efd2629a998736209648574a1a9c51238174959fc3e08d67522791fc9913033"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/technical-writing

---

# Creating effective technical documentation

Effective feature documentation is important in enhancing a user's experience with the feature. Good documentation is like a piece of the puzzle that makes everything click â the key for encouraging feature adoption.

To support you in creating effective technical documentation, this article provides an overview of the core principles of technical writing. It also highlights the best practices for creating clear and accessible documentation. Applying these technical writing principles helps us maintain the high quality of content on MDN. Whether you're documenting your own project or product or contributing to technical content in various settings, you can improve the quality of your work by following these best practices.

## [Adopt clarity, conciseness, and consistency](https://developer.mozilla.org#adopt_clarity_conciseness_and_consistency)

These three Cs form the core principles of technical writing. They can take you a long way in producing quality documentation.

### [Clarity](https://developer.mozilla.org#clarity)

For achieving clarity in your writing, apply the following guidelines:

- Use simple words and clear language. Keep in mind the audience, especially if it includes non-native English speakers.
- Be clear about who needs to perform the action. Writing in [active voice](https://www.merriam-webster.com/grammar/active-vs-passive-voice-difference) is not strictly required. However, you should use it when you want to be clear about who needs to perform the action. For example, clarify whether a function is triggered by an event or if the user needs to explicitly call the function.
- Clearly introduce and explain new terms. This helps to lay the foundation for concepts that are covered later in the documentation.
- To avoid ambiguity, specify pronouns clearly.
**Callout:** Replace "it", "this", and "these" with proper nouns if they can refer to more than one thing in the given context.
- Aim for one idea per sentence to improve readability.
- Stick to one main idea per paragraph. Each sentence in a paragraph should logically connect to the one before it. Imagine if each sentence in a paragraph was a link in a chain. If you pick up the first link, the other links in the chain should follow, forming a continuous sequence. This is how the sentences should connect to each other, ensuring a seamless flow of a single idea.

### [Conciseness](https://developer.mozilla.org#conciseness)

Keep sentences short. This automatically increases the readability and clarity of your document. It also helps in quick comprehension. Long sentences can be more challenging to understand quickly due to their complex structures.

**Callout:**
Based on common readability standards, aim for 15-20 words per sentence.


For additional insights on sentence length and readability strategies, see [Simple sentences](https://readabilityguidelines.co.uk/clear-language/simple-sentences/#1-make-your-average-sentence-15-words-long) (on [https://readabilityguidelines.co.uk](https://readabilityguidelines.co.uk)) and [Popular readability formulas](https://en.wikipedia.org/wiki/Readability#Popular_Readability_Formulas), including the Flesch-Kincaid index, on Wikipedia.

### [Consistency](https://developer.mozilla.org#consistency)

Use the same terminology throughout your documentation to ensure a seamless reader experience. For example, if you start referring to "user agents" as browsers, stick with that term consistently. This avoids confusion that can arise from using words interchangeably, even when they share the same meaning.

Additionally, maintain consistent word casing and follow a uniform formatting style throughout your documentation. These practices not only enhance readability but also contribute to a professional presentation of your documentation.

## [Organize your content for maximum impact](https://developer.mozilla.org#organize_your_content_for_maximum_impact)

Apply the same principles for organizing your content as you would for organizing your code: spend some time setting a clear goal and thinking about the desired structure for your documentation. Ensure that each subsection contributes to this goal incrementally.

### [Start with an introduction](https://developer.mozilla.org#start_with_an_introduction)

In the introduction, first describe the feature you're documenting. Next, set the context by explaining why learning about the feature would be beneficial to the readers. This can include describing real-life scenarios where the feature can be useful. The more relevance you add to the topic, the easier it will be for readers to understand and engage with the content.

### [Progress logically](https://developer.mozilla.org#progress_logically)

The following questions can help you ensure that your content is progressing logically:

- Is your document structured to guide readers from foundational concepts to more advanced ones? Are there sections to introduce the "**what**" to establish a base before delving into the "**why**" and "**how**"? Consider whether the document structure mirrors the natural learning path for the topic. Aligning the document's structure with the natural progression of learning helps readers build their knowledge step-by-step and also enhances the overall learning experience.
- Are there sufficient how-to guides or examples following the conceptual sections?
- Consider the flow of the content. Is it following a logical sequence â from one sentence to the next, from one paragraph to the next, and from one section to the next? Does each section logically build on the information presented previously, avoiding abrupt jumps or gaps in the content?

Additionally, as you work on the draft, always ask yourself:

- What reader questions am I addressing with this sentence?
- Can I add a simplistic or real-life use case to explain this concept?

### [Include examples](https://developer.mozilla.org#include_examples)

Imagine sitting next to someone as you explain the concepts to them. Preempt their questions and address them in your writing. Use this approach to add as many relevant examples as possible.

When adding examples, don't restrict yourself to only code; include non-code scenarios to demonstrate a feature's utility. This helps readers understand the concepts better and also caters to different learning styles. Consider providing real-world scenarios or use cases to illustrate how the feature or concept applies in practical situations.

### [Optimize the document structure and length](https://developer.mozilla.org#optimize_the_document_structure_and_length)

Evaluate your documentation's structure to ensure it maintains a logical and balanced hierarchy.

- Ensure that each section and subsection has a clear purpose and sufficient content.
- Look for instances where a main section contains only one subsection (orphan), such as a single `H3` section under an `H2` section. This indicates that you need to reorganize your content or make some additions.
- Check if there are lower-level headings such as `H4`. Too many subsections can be overwhelming for readers, making it difficult for them to grasp the information. In such cases, consider presenting the content as a bulleted list instead to help readers retain the key points more effectively. This approach helps to simplify the hierarchy and also contributes to easier navigation.
- While there should be sufficient content for each section, pay attention to the overall length. If any section becomes too extensive, it can be overwhelming for readers. Split large sections into multiple logical subsections or restructure the content into new sections and subsections. Grouping content into digestible pieces helps maintain focus and improve navigation for readers.

## [Proofread your writing](https://developer.mozilla.org#proofread_your_writing)

One aspect that cannot be stressed enough is the importance of **self-reviewing** and **proofreading** what you've written. Whether you're creating a large document or a short paragraph, this step is crucial.

Taking the time to fully review your work will help you identify sections that don't flow well or can be improved for clarity. During self-review, aim to spot and remove redundancy (repetition of ideas without adding value) and repetitiveness (overuse of words or phrases). These refinements will ensure your documentation is clear and coherent and conveys your ideas as intended.

Proofread and then take a break before you review again. Only then submit your work. While spell checkers can flag spelling errors, they might not flag incorrect use of words, such as an unintended use of "he" instead of "the". It's best to take a break and return with fresh eyes to catch any errors you might have missed. Pay close attention to identify inconsistencies in tone, style, tense, or formatting and make the necessary adjustments.

## [Additional tips](https://developer.mozilla.org#additional_tips)

To improve the clarity and accessibility of your documentation, also keep the following guidelines and tips in mind. To go in-depth into any of the topics, feel free to consult our [Writing style guide](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide).

- [Bulleted vs numbered lists](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide#lists): Lists, in general, make documentation easier to scan. Use bulleted lists when there is no specific order of the items. Use numbered lists when the steps need to be followed in the specific order. Always include a lead-sentence before beginning a list to provide context.
- [Commas](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide#commas): Use a comma after an introductory clause to improve readability and to clarify the sentence structure. Use a comma to separate items in a list to ensure clarity.
- [Alt text](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Howto/Images_media#adding_alternative_text_to_images): Always provide an alternative text for the images you add to content. This makes your documentation accessible to people using screen readers. In addition to images, ensure that video and audio files have accompanying descriptive texts.

- [Descriptive link text](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide#cross-references_linking): Make sure each link text is clear even out of context and clearly indicates where the link leads. Descriptive link texts also help people using screen readers understand the destination of links. For example, use "Read our [writing style guide](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide) to learn more" instead of "Click [here](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide) to learn more".

- [Inclusive language](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide#use_inclusive_language): Make your documentation welcoming to everyone. Strive to use words that respect and acknowledge the diversity of your audience.

## [Summary](https://developer.mozilla.org#summary)

That's it for this article. I hope you found these tips helpful as a quick refresher on technical writing best practices. Remember that learning how to create effective and easy-to-use documentation is an ongoing process. It starts with understanding your audience and the goals of your documentation. By applying these technical writing principles and tips, you'll certainly be able to enhance the clarity and overall quality of your documentation.

Let me know if you learned something new or if there's any idea that resonated with you. I'd also like to hear if there are any best practices you use in your technical documentation workflow. Share with us on [Mastodon](https://mastodon.social/@mdn) or [Discord](https://developer.mozilla.org/discord).