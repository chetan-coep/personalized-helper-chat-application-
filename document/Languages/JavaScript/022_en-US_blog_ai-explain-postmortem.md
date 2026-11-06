---
id: "javascript_022"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 22
source_url: "https://developer.mozilla.org/en-US/blog/ai-explain-postmortem"
language: "en"
retrieved_at: "2026-11-01 21:51:50"
content_hash: "46485b9f1088d6e43d1647740419711e5f3aa3bdda159272b03dd32643408912"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/ai-explain-postmortem

---

# Reflections on AI Explain: A postmortem

We recently launched two new AI experiences â AI Explain and AI Help. Thanks to feedback from our community, we realized that AI Explain needs more work. We have disabled it and will be working on it to make it a better experience.

In this blog post, we look into the story behind AI Explain: its development, launch, and the reasons that led us to press the pause button. We greatly value our community's input, which has played a significant part in this decision. Looking forward, we aim to resume our work on this feature in 2024, giving us ample time to address the feedback received and improve the feature in a way that helps everyone who wants to use it.

## [Launching AI-powered features](https://developer.mozilla.org#launching_ai-powered_features)

In preparation for the launch of MDN Plus in March 2022, we spent the majority of 2021 doing user research to try to understand the main pain points people have on MDN. A topic that came up a lot was the discoverability of content for people who are newer to software development. Experienced developers can be more productive by effectively searching for the information they need, but new developers often still need to build this skill.

A recurring complaint we heard from our readers was that MDN is excellent when you know what to look for. If you don't, it's not easy to discover the information you need and extract meaningful knowledge from the appropriate documentation. Developers with less experience find it harder to navigate through MDN and often turn to other places to find the information they need. Even more, we have a high dependency on search engines, with more than 90% of our traffic coming from them. We knew improving site search would help discoverability and saw an opportunity to combine search improvements with novel ways of interacting with the site.

We've noted that it's not always trivial to understand code examples on MDN, because they often combine features, not all of which are explained in the current article. However, fully explaining every detailâlike defining what a CSS selector is on every page containing a CSS exampleâwould be impractical. Through AI Explain we could enable readers to better understand embedded code examples in MDN documentation, without overwhelming the core content.

### [Interacting with documentation using generative AI](https://developer.mozilla.org#interacting_with_documentation_using_generative_ai)

In January 2023, we began experimenting with OpenAI's GPT-3.5 API to determine how we could enhance our documentation platform and make our website more user-friendly. We saw potential for uses such as summarizing documentation pages, explaining existing code samples, generating examples for pages lacking them, and generating unique code examples that combined different technologies according to user queries.

We also saw that other developer-focused companies were investing significantly in and building products on top of the technology. With MDN's documentation being publicly available under an open Creative Commons license, and considered best-in-class, it's reasonable to assume most models have been trained on our content, and products started to be announced which explicitly allowed the consumption of our documentation. This led us to understand that, irrespective of our personal feelings, our users already access our content through generative AI. With the support of our community, we are uniquely positioned to learn how AI can augment documentation and how developers use it. Our extensive experience, a willingness to learn, and our network of contributors and subject matter experts place us in a great position to refine this functionality through iteration and feedback.

In March 2023, we focused development on two features that were the most promising given the current state of the technology:

- **AI Explain** - A way for readers to explore and understand code examples embedded in MDN documentation pages, describing the purpose and behavior of the code or parts of the example.
- **AI Help** - A conversational interface that offers concise answers using MDN articles related to the user's questions for contextual help and provides the MDN pages it used to answer the questions as sources.
This prototype was built in collaboration with Supabase for the purpose of getting responses tailored to MDN content.
We decided to keep this feature behind a login which would require readers to have an MDN Plus account.

We recognized an opportunity with these features to better assist less experienced developers with the intent to be helpful rather than matching our reference documentation's exact quality and precision. Beginners are new to navigating reference documentation and often turn to other, potentially less accurate, information sources. Learning isn't an immediate jump to a correct conclusion but an iterative process where we consider incorrect information and discard it as our understanding solidifies. Just as a human might (as an expert or a peer in a learning community) give an incorrect response, it is still ultimately useful as it unblocks, gives our users ideas, and points them to something relevant.

## [Launching AI Explain](https://developer.mozilla.org#launching_ai_explain)

Let's zoom in on the AI Explain launch.

### [Testing the accuracy of explanations](https://developer.mozilla.org#testing_the_accuracy_of_explanations)

We first tested AI Explain with the OpenAI models `gpt-3.5-turbo-0301`, followed by `gpt-3.5-turbo-0613`, as this was the default model from June 27, 2023 onwards.
Due to the reduced capacity for the new model, we reverted to `gpt-3.5-turbo-0301`.
We ran all 25,820 unique code examples on MDN against `gpt-3.5-turbo-0301` and used a combination of automated and manual testing to validate the explained responses.

As beginners are the most likely audience to use this feature, we took common programming concepts and examples that readers would run against AI Explain and corroborated responses individually. Contrasting this audience, we also chose edge cases and new web technologies that we thought the model might struggle to explain.

With regard to automated testing, a test suite is a challenge to build for a feature of this type due to the non-deterministic output of an LLM.
Therefore, one method we tried was to run explanations created by `gpt-3.5-turbo-0301` for each of the 25,820 unique code examples on MDN and validate the output against GPT-4.
The summary of the responses from this experiment tagged generated explanations as either accurate, somewhat inaccurate, or incorrect.
We randomly sampled responses that were not considered high-quality and manually inspected and evaluated them.

Our conclusion from testing in these ways was that the responses were helpful in enough cases that it would be beneficial for users to try out in beta. In addition to testing, starting March 2023, we conducted Mozilla-internal demos and communicated that work was in progress on these features to stakeholders and our partners.

### [Launch and feedback](https://developer.mozilla.org#launch_and_feedback)

On June 28th, we launched AI Explain on MDN. The feature was accessible to all users via a button labeled 'AI Explain' on the top right corner of embedded code examples. AI Explain was live for 65 hours with a total of 24,132 unique visitors who used the functionality to generate 44,229 responses. 3.34% of the responses were voted on via a thumbs up/down UI beside answers. Of these responses, 68.9% votes marked the answers as helpful and 31.1% marked them as unhelpful. For some perspective on this feedback relative to other site functionality, we typically see around 70%-75% positive sentiment from our audience who rate their experience (eg: 72% positive sentiment for the recently-launched sidebar filter).

On June 30th, [a GitHub issue](https://github.com/mdn/yari/issues/9208) was opened by a community member who was concerned about the output generated by AI Explain being incorrect and misleading.
This GitHub issue received 1,287 upvotes and 115 comments.

We also saw feedback from the community on Mastodon, Discord, Twitter, and Matrix sharing their concerns about the feature. We received a total of 11 unique examples shared across social channels that demonstrated output from AI Explain that was either inaccurate or misleading:

- In four cases, the code examples contained newer web features that GPT-3.5 doesn't know about due to its limitation to information until 2021.
- In three cases (including one duplicate), we found the code examples to be sufficiently complex that many developers would have a hard time explaining them.
- In two cases the explanations ignored important syntax details (slashes, short-hand notation).
- In one case the explanation was mostly correct, but falsely flagged a missing closing tag that was actually present in the code example.
- In one case, no screenshot or text was posted of the response, so we were unable to analyze it.

The overall sentiment of the negative feedback was that AI Explain was not ready to be launched, and that adding generative AI to MDN was not a good addition to the platform.

### [Rollback and response](https://developer.mozilla.org#rollback_and_response)

We acknowledge a misstep in fully launching the AI Explain feature, rather than limiting access to logged-in users as originally intended. This error was amplified by a GitHub issue being reported over a long weekend. To address this, we promptly deactivated the feature, initiating a comprehensive internal review and thoroughly analyzing user feedback (as detailed above). The GitHub issue was opened on June 30 at 22:00 CEST, and we disabled AI Explain on July 1 at 09:40 CEST with the changes deployed at 10:20 CEST. This was the earliest point we could take action considering time zone differences between the issue reporter and the team. The AI Explain button was removed from code blocks on MDN and AI Explain is no longer accessible to any users.

## [What we can improve](https://developer.mozilla.org#what_we_can_improve)

There are three important aspects to take away from this launch:

1. AI Explain was originally intended as an experimental feature for logged-in users, akin to AI Help. Launching it publicly to all users, and without a clear indication of its experimental nature, was a mistake. 
  - This error has been acknowledged and addressed within our team. We've also updated our development processes to prevent similar oversights in the future.
2. Prompting GPT-3.5 to explain code samples without context is not sufficient given its 2021 limitation. We should have used a similar approach for AI Explain as we did with AI Help, using relevant MDN content as context.
3. Just before the launch, OpenAI updated their API to use `gpt-3.5-turbo-0613`.
While our random sample testing did not identify any issues, 4 out of the 11 inaccurate examples pointed out by the community were due to these changes.
  - Going forward, we need to thoroughly validate any differences between models, as these variations can significantly affect output. This is crucial, especially considering that the majority of our testing and development were done using a model that differed from the one deployed in production.

## [Next steps](https://developer.mozilla.org#next_steps)

Here are the actions we're implementing:

1. AI Explain will not be reintroduced to MDN until we are confident that it delivers reliable information that both readers and contributors can trust. We do not anticipate this happening within 2023, and we will provide updates as soon as we believe it's ready for community review.
2. We will work with our community of contributors to test and improve AI-powered features during the development process going forward. This will include thorough testing with community members from different backgrounds, skill levels, and perspectives.
3. Future platform experiments of this nature will be restricted to logged-in users or those who have voluntarily joined a user experience cohort.
4. We commit to clearly marking new features as experimental, explaining any potential for unexpected behavior, and providing reasons for their trial status.
5. For AI Help specifically, we added a "Report an issue with this answer on GitHub" link to all answers, making it easy for users to raise issues in a dedicated ai-feedback repository with all necessary context for us to expedite bug fixes and enhancements of the feature.

## [The right path for open source maintenance](https://developer.mozilla.org#the_right_path_for_open_source_maintenance)

We know that technical accuracy is why our readers come to MDN, and we understand that many of our community members are disappointed with the quality of the feature we launched and that we have chosen to include generative AI functionality in the platform.

While there are definitely learnings we took from how this launch went, we reaffirm our commitment to enhancing the reading experience of MDN. Improving how people interact with MDN includes developing new platform features that may use novel technologies, including generative AI, to help explore, understand, and enrich the substantial collection of human-written and curated content. We want to continue to help our readers understand web technologies wherever they are in their learning journey. We hope that with your input, we will keep improving the platform many of you depend on.

We're following the discussions on social platforms closely, and we're taking the feedback from every contributor into account while we work on steps to improve transparency about adding features to MDN.

Managing open-source software is not easy, and there are so many contributors and users with different perspectives and expectations that we need to serve. We acknowledge the feedback we received on GitHub from our users directly through the 115 comments and indirectly through the 1287 upvotes. We acted on it and that's why AI Explain has been disabled. We have 17 million unique readers that come monthly to MDN to find answers and learn about the web, and we would like to serve all of them as best as we can as well. We are committed to continue as stewards of open web documentation and work with our community to improve the experience for all of our readers responsibly.