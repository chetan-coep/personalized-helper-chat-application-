---
id: "javascript_004"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 4
source_url: "https://developer.mozilla.org/en-US/blog/introduction-to-web-sustainability"
language: "en"
retrieved_at: "2026-11-01 21:52:48"
content_hash: "4dc9c4d98dec6f19edd4af5df1b8ff4917a226ca83516e908f643a364bad3af0"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/introduction-to-web-sustainability

---

# Introduction to web sustainability

As its impacts become more evident and frequent, climate change is quickly moving up the agenda for governments, communities, and companies worldwide. We know that reducing our greenhouse gas emissions is crucial to mitigate the worst effects of climate change and ensure a liveable and sustainable future.

Every industry has a part to play, including those of us in the web industry. In this article, we'll explore some of the environmental impacts of our digital lifestyles and discuss how web designers and developers can contribute to more sustainable practices.

## [How digital technology adds to carbon emissions](https://developer.mozilla.org#how_digital_technology_adds_to_carbon_emissions)

People often assume that digital technology is "clean" because digital activities don't produce visible pollution like factories or cars. In fact, the internet accounts for around 4% of global carbon emissions, a figure equivalent to the output of the entire aviation industry.

A large part of the environmental impact of the digital landscape stems from electricity use, often sourced from fossil fuels. Burning fossil fuels produces carbon dioxide (CO2), commonly referred to as carbon emissions. This electricity not only powers users' devices but also facilitates data storage and transfer across networks and supports the manufacturing of hardware for our digital infrastructure.
[Source](https://sustainablewebdesign.org/calculating-digital-emissions/)

## [Current challenges in digital sustainability](https://developer.mozilla.org#current_challenges_in_digital_sustainability)

Considering carbon emissions is merely one aspect of making our web applications more sustainable. There are many other interconnected factors that should be considered for making more sustainable choices when building for the web.

### [Water usage](https://developer.mozilla.org#water_usage)

An ever-expanding tech industry requires more data centers, which are not only energy-intensive but require a **lot** of water for cooling. Silicon chips also require a lot of water during the manufacturing process. Water scarcity is becoming an ever-increasing concern globally and will be exacerbated by climate change. Vital water supplies that communities rely on are [increasingly being diverted](https://www.washingtonpost.com/climate-environment/2023/04/25/data-centers-drought-water-use/) to support digital infrastructure.

### [E-waste management](https://developer.mozilla.org#e-waste_management)

Worldwide, we produce around 40 million tons of [electronic waste](https://earth.org/e-waste-pollution/) every each. Old devices such as laptops, smartphones, and tablets are frequently discarded without being properly recycled, often in the global south, where they cause pollution and harm fragile ecosystems. Where recycling does happen, it often occurs under exploitative conditions.

### [Material extraction](https://developer.mozilla.org#material_extraction)

Device manufacturing and battery technology (increasingly important for a transition to renewable energy) is dependent on the mining of precious metals. Extracting these natural resources is incredibly destructive, and it is decimating both landscapes and communities.

### [Chemical pollution](https://developer.mozilla.org#chemical_pollution)

Hazardous chemicals from the device manufacturing process can easily find their way into the natural environment, where they cause harm.

### [Social inequality and climate justice](https://developer.mozilla.org#social_inequality_and_climate_justice)

Disadvantaged people are most likely to suffer the environmental impacts of our digital lifestyles and least likely to benefit. We must ensure that the transition to increasingly sustainable practices doesn't inadvertently shift the burden onto those who are already bearing the greatest cost.

## [Actionable steps for web professionals to improve digital sustainability](https://developer.mozilla.org#actionable_steps_for_web_professionals_to_improve_digital_sustainability)

You might think that any individual effort to reduce the web's environmental impact is a drop in the ocean. But as tech workers, we are in a position of relative power compared to other industries. We build products that might be used by thousands, even millions of users. Any improvements we make have the potential for a vast impact when scaled up to that level.

Reducing carbon emissions caused by the products we build is an obvious place to start, while also continuing to think holistically and bearing in mind other aspects of digital sustainability.

## [Ways to improve web performance to lower carbon emissions](https://developer.mozilla.org#ways_to_improve_web_performance_to_lower_carbon_emissions)

Making our websites faster for our users has become an increasing focus in recent years. The good news is that there is a big overlap between web performance and sustainability: fast websites are **often** low-carbon websites!

Optimizing our sites can reduce the amount of data stored and transferred, and the amount of power consumed by the user's device. Building sustainably can also help extend the longevity of users' devices, reducing the need for upgrades and replacements.

### [Leveraging tools to assess performance and impact](https://developer.mozilla.org#leveraging_tools_to_assess_performance_and_impact)

Tools such as [WebPageTest](https://www.webpagetest.org/) and Google's [PageSpeedInsights](https://pagespeed.web.dev/) can help us measure web performance and prioritize improvements. WebPageTest also has a relatively new [Carbon Control](https://www.webpagetest.org/carbon-control/) feature to measure our websites' environmental impact. [Website Carbon](https://www.websitecarbon.com/) is another tool for getting a handle on your website's environmental impact.

While tools [can't measure everything](https://fershad.com/writing/is-data-the-best-proxy-for-website-carbon-emissions/), they provide a good starting point for understanding the impact of our websites and provide some ideas for improvements.

### [Cutting down image size](https://developer.mozilla.org#cutting_down_image_size)

Images are a big contributor to page weight, accounting for [nearly half](https://httparchive.org/reports/page-weight) of data transfer on the web. We can reduce this impact by using smaller and fewer images and by optimizing and compressing those we do use.

Using `srcset` and `<picture>`, we can serve the most appropriate image for a user's device â serving modern (smaller) image formats (such as WebP) to those whose devices support them, and ensuring that lower-resolution devices don't need to download huge, high-resolution images.

The `lazyload` HTML attribute is well-supported and prevents images from being downloaded before a user scrolls to the point they're required.

### [Optimizing fonts](https://developer.mozilla.org#optimizing_fonts)

Fonts are another resource that can significantly affect page weight, making them ripe for optimization. We can reduce this burden by limiting the number of web fonts we use. We could consider using a [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts) if multiple weights and styles of a particular typeface are needed.

Serving modern font formats, such as Web Open Font Format 2.0 (WOFF2), will generally reduce the payload compared to older TrueType Font (TTF) files. We could also consider [subsetting](https://the-sustainable.dev/a-guide-to-subsetting-fonts/) fonts â serving a limited collection of glyphs if, say, only one language is required on the website.

[Self-hosting your fonts](https://sia.codes/posts/making-google-fonts-faster/#self-host-your-web-fonts-for-full-control) will save on network requests and give you more control.

### [Handling third-party embeds](https://developer.mozilla.org#handling_third-party_embeds)

Third-party code such as chat widgets, analytics scripts, and social media embeds are often the worst offenders when it comes to page weight and data transfer. If you can't avoid these altogether, consider using the [import-on-interaction](https://www.patterns.dev/posts/import-on-interaction) pattern, where loading is deferred until a user interacts with the widget.

Paul Irish's [Lite YouTube Embed](https://github.com/paulirish/lite-youtube-embed) provides an easy way to defer loading of heavy YouTube embeds.

### [Reducing JavaScript usage](https://developer.mozilla.org#reducing_javascript_usage)

JavaScript is more resource-intensive than HTML and CSS, and most websites are over-reliant on it. Closely consider whether you really need a JavaScript framework for your project, and evaluate costly dependencies with tools like [Bundlephobia](https://bundlephobia.com/). You might be able to use a native API instead.

[Dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import#description) can help reduce the upfront JavaScript bundle size and prevent users from downloading code that won't be needed until much later.

For further insights, [Responsible JavaScript](https://abookapart.com/products/responsible-javascript) by Jeremy Wagner is a recommended reading resource.

### [General optimization tips](https://developer.mozilla.org#general_optimization_tips)

Minifying, compressing, and [tree-shaking](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking) your code, in addition to compressing images, will all contribute to reducing data transfer. Additionally, we can make sure we cache as much as possible. Harry Roberts provides a great guide to [cache-control for civilians](https://csswizardry.com/2019/03/cache-control-for-civilians/).

## [Choosing a green web host](https://developer.mozilla.org#choosing_a_green_web_host)

Ensuring that our web hosts use renewable energy is an important step towards reducing our sites' carbon emissions. Unfortunately, it's not always easy to distinguish genuine green credentials from greenwashing and marketing claims. The [Green Web Foundation's hosting directory](https://www.thegreenwebfoundation.org/directory/) lists companies that provide proof of their "green" credentials.

[Are my third parties green?](https://aremythirdpartiesgreen.com/) is a tool that checks the carbon impact of third-party dependencies, including whether they are green-hosted.

## [Optimizing energy use with carbon-aware computing](https://developer.mozilla.org#optimizing_energy_use_with_carbon-aware_computing)

We can reduce our reliance on electricity generated from fossil fuels by looking at where and when we run energy-intensive processes:

- By utilizing servers in locations where a higher proportion of electricity comes from renewable sources (spatial shifting).
- By running processes at times of the day when demand on the electrical grid is low, or when more electricity is being produced by intermittent solar or wind power (temporal shifting).

The [Green Software Foundation](https://learn.greensoftware.foundation/carbon-awareness) offers some great resources on this topic.

## [Making greener design choices](https://developer.mozilla.org#making_greener_design_choices)

By considering sustainability from the design stage, we are best-placed to minimize the environmental impact of our products. A greener design might involve using less energy-intensive colors. Blue colors use more energy than red or green do, and on Organic Light-Emitting Diode (OLED) screens, a dark color scheme can save energy because black pixels are "off".

Websites can be designed to minimize the use of video and large images, especially by avoiding autoplaying videos or by using SVGs instead of photos where possible.

The user journey also plays an important part: How much time are users spending clicking around on your site, loading more resources than they need because they can't find what they're looking for?

## [Using your power and privilege to build a sustainable web](https://developer.mozilla.org#using_your_power_and_privilege_to_build_a_sustainable_web)

Not only can we take steps to address the environmental impact of the products we build, but we can also make a wider impact by sharing our knowledge with the rest of the web community. This could include starting an environmental action group at your place of work, writing on your own blog, giving talks, or sharing tips on social networks.

The more we can normalise the conversation around web sustainability, the greater impact we can make.

## [Collaborating with the community for web sustainability](https://developer.mozilla.org#collaborating_with_the_community_for_web_sustainability)

As important as our individual efforts are, it's when we work together as part of a wider community that we can have the greatest impact.

- [ClimateAction.tech](https://climateaction.tech/) is a community of tech workers working together to seed climate action in companies, organizations and industries. It's a great place to have conversations with like-minded people and get inspired to take action.
- The [Sustainable Web Design Community Group](https://www.w3.org/community/sustyweb/) is working to define a set of guidelines for building sustainable websites. Join the group, or contribute via [GitHub](https://github.com/w3c/sustyweb/).

## [Summary](https://developer.mozilla.org#summary)

Although it can feel like an uphill battle, there are plenty of opportunities for those of us working on the web to build more sustainably and reduce the environmental impact of the products we build. The first step is becoming aware of the impact of our actions and choices, and then we can start to explore what actions we can take to reduce the burden on the planet. Every bit counts.

I trust you found the information and tips shared in this article valuable. Feel free to leave your feedback, thoughts, or questions on [Discord](https://developer.mozilla.org/discord) or on [GitHub](https://github.com/orgs/mdn/discussions/categories/the-mdn-web-docs-blog).

## [Resources](https://developer.mozilla.org#resources)

Beyond the tips here, there are many more resources to guide you in building a more sustainable web.

- [Green Web Foundation](https://www.thegreenwebfoundation.org/)
- [Green Software Foundation](https://greensoftware.foundation/)
- [Sustainable Web Design](https://sustainablewebdesign.org)
- [Sustainable Web Design (book)](https://abookapart.com/products/sustainable-web-design/) by Tom Greenwood
- [World Wide Waste (book)](https://gerrymcgovern.com/world-wide-waste/) by Gerry McGovern
- [Web Sustainability Guidelines (WSG) 1.0](https://w3c.github.io/sustyweb/) (Draft community group report)