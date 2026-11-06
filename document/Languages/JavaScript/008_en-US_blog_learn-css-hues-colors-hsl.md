---
id: "javascript_008"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 8
source_url: "https://developer.mozilla.org/en-US/blog/learn-css-hues-colors-hsl"
language: "en"
retrieved_at: "2026-11-01 21:52:58"
content_hash: "0aba1163834b1e643706b6a5ad31328c6ebe84dfc5f8375df12b4cec8414bcad"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/learn-css-hues-colors-hsl

---

# Learn how to use hue in CSS colors with HSL

Out with the old, in with the `<hue>`! Hues are a great way to define colors in CSS.

We covered CSS color functions in [a previous post](https://developer.mozilla.org/en-US/blog/css-color-module-level-4/) including all of the new functions and ways to describe colors including a dip into color spaces. If you're feeling overwhelmed by all of the details about color spaces and the science behind it, this post is for you.

In this post, we'll take a look at what hues are and how you can take your first steps using hues in CSS using the `hsl()` function.

## [What is a hue?](https://developer.mozilla.org#what_is_a_hue)

Hue is the property that allows us to tell the difference (or similarity) between colors like red, orange, yellow, green, blue, etc. There's more to what makes up a color than hue, and we'll cover that in a bit, but for now, let's see what it means to define a color using hue.

The key concept for you to understand hue is that you can specify a hue in an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle) (or a number that represents an angle in degrees).
The reason behind using an `<angle>` is that most of the color models describe hues using a color wheel that looks something like this:

There's a complete circle from 0 to 360 degrees, and we can use any number in between that range to describe a color.
Not all color functions use the same color wheel, so 180 degrees in one function might be a different color than 180 degrees in another function.
You can see some examples of this on the [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue) page.

## [Why are hues useful?](https://developer.mozilla.org#why_are_hues_useful)

CSS has an amazing variety of ways to choose colors for styling your pages - and this is already without hues. You're probably using one of these ways to define a color in your CSS:

```
/* A named color */
hotpink
/* A # hexadecimal value */
#ff0099
/* An RGB function with 256 values for red, green, and blue */
rgb(255 0 153)
```
That gives us hexadecimal values like `#ff0000` and named colors like `aliceblue` or `rebeccapurple`.
You might be using the [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb) function (or "functional notation"), which lets you set red, green, and blue values independently.

These common ways to set colors give us a great amount of flexibility through literally millions of colors (`256 x 256 x 256`). But what if you want variations of a certain color?
Maybe you'd like to use `aliceblue` but a little less vibrant, or a color like `#008000` but 50% darker.
How can you get a color that's 10% brighter than `rgb(255 0 153)`?

The great thing about hues is that you can choose a color and create variations of it using the other properties like saturation (how vibrant a color is), lightness (how light or dark a color is), and chroma (how intense a color is).

Another benefit of hues as angles is that you can find related colors based on where they are in the color wheel (e.g., three colors, each 10 degrees apart) or make a color palette based on related colors. We'll see exactly how to do this later.

## [How do you use the `hsl()` function?](https://developer.mozilla.org#how_do_you_use_the_hsl_function)

If you want to try hues in CSS, I believe you should start with the [hsl()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl) function that lets you define **hue**, **saturation**, and **lightness**, in that order, as `hsl(hue, saturation, lightness)`.
Let's take a look at some colors defined using the `hsl()` function in the following sections.

### [Defining red, green, and blue using `hsl()`](https://developer.mozilla.org#defining_red_green_and_blue_using_hsl)

This is a pretty basic example to illustrate how the `hsl()` function works.
You will see that it matches up with the [color wheel above](https://developer.mozilla.org#what_is_a_hue) when you check the angles at 0, 120, and 240 degrees:

```
#red {
  background-color: hsl(0 100% 50%);
}
#green {
  background-color: hsl(120 100% 50%);
}
#blue {
  background-color: hsl(240 100% 50%);
}
```
```
<div id="red">Red</div>
<div id="green">Green</div>
<div id="blue">Blue</div>
```
### [Making a variation of a hue](https://developer.mozilla.org#making_a_variation_of_a_hue)

To see how saturation values work, let's take a look at a red color with decreasing saturation values from 100% to 0%:

```
<div id="red-hsl">sat. 100%</div>
<div id="red-hsl-80">sat. 80%</div>
<div id="red-hsl-60">sat. 60%</div>
<div id="red-hsl-40">sat. 40%</div>
<div id="red-hsl-20">sat. 20%</div>
<div id="red-hsl-0">sat. 0%</div>
```
```
#red-hsl {
  background-color: hsl(0 100% 50%);
}
#red-hsl-80 {
  background-color: hsl(0 80% 50%);
}
#red-hsl-60 {
  background-color: hsl(0 60% 50%);
}
/* Continue with saturation values 40%, 20%, and 0% */
```
In the end, we have a gray color and any `hsl()` value with 0% saturation will be a shade of gray depending on the lightness value.
The `hue` value won't have any effect on the color when saturation is 0%.
Let's experiment with this in the next section to see what that looks like.

### [Exploring hue saturation and lightness using hsl()](https://developer.mozilla.org#exploring_hue_saturation_and_lightness_using_hsl)

On the [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#changing_the_hue_of_a_color_using_a_slider) page, there's an example where you can change the hue of an element using a slider like `hsl(<slider-value> 100% 50%)`.
We can use this as a starting point and build on it here by adding more inputs, so that we can also control the saturation and lightness:

```
<div id="box"></div>
<input type="range" min="0" max="360" value="0" step="0.1" id="h-slider" />
<input type="range" min="0" max="100" value="100" step="0.1" id="s-slider" />
<input type="range" min="0" max="100" value="50" step="0.1" id="l-slider" />
<p>Hue: <span id="h-value">0deg</span></p>
<p>Saturation: <span id="s-value">100%</span></p>
<p>Lightness: <span id="l-value">50%</span></p>
<br />
<button>Reset</button>
```
To make this interactive, we can grab the values of the sliders and replace the arguments in the function like `hsl(slider1 slider2 slider3)`.
Instead of [repeating the code](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#changing_the_hue_of_a_color_using_a_slider) to update a value for each slider, we call one function to update the box when any slider changes:

```
const box = document.querySelector("#box");
const hue = document.querySelector("#h-slider");
const saturation = document.querySelector("#s-slider");
const lightness = document.querySelector("#l-slider");
const updateBox = () => {
  // Set hsl(<hue>deg, <saturation>%, <lightness>%)
  box.style.backgroundColor = `hsl(${hue.value} ${saturation.value}% ${lightness.value}%)`;
  // Some feedback so we can see the values changing
  document.querySelector("#h-value").textContent = `${hue.value}deg`;
  document.querySelector("#s-value").textContent = `${saturation.value}%`;
  document.querySelector("#l-value").textContent = `${lightness.value}%`;
};
hue.addEventListener("input", updateBox);
saturation.addEventListener("input", updateBox);
lightness.addEventListener("input", updateBox);
```
Notice that when the saturation is 0%, the hue value doesn't have any effect on the color. The same is true when the lightness is 0% (black) or 100% (white), the hue and saturation values don't have any effect.

### [Using a variable to change hues in multiple places](https://developer.mozilla.org#using_a_variable_to_change_hues_in_multiple_places)

Let's say we want to use the same hue value in multiple places.
We can use a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) to do this:

```
:root {
  --hue: 0;
}
#red-hsl {
  background-color: hsl(var(--hue) 100% 50%);
}
#red-hsl-80 {
  background-color: hsl(var(--hue) 80% 50%);
}
/* Continue for saturation values 60%, 40%, 20%, and 0% */
```
```
<div id="red-hsl">100%</div>
<div id="red-hsl-80">80%</div>
<div id="red-hsl-60">60%</div>
<div id="red-hsl-40">40%</div>
<div id="red-hsl-20">20%</div>
<!-- We don't need a 0% saturation div because it's always gray -->
<input type="range" min="0" max="360" value="0" step="0.1" id="hue" />
```
```
const hue = document.querySelector("#hue");
const updateHue = () => {
  document.documentElement.style.setProperty("--hue", hue.value);
};
hue.addEventListener("input", updateHue);
```
The great thing about putting these pieces together is that we can choose a color for our project and then use the same hue value in multiple places. We can use this as a color scheme for elements that need to stand out or to show a state like a button that's disabled, while using the same hue value for each.

### [Picking related colors based on hue angles](https://developer.mozilla.org#picking_related_colors_based_on_hue_angles)

I mentioned earlier that you can find related colors based on where they are in the color wheel. Let's give this a go by building on the general idea of the previous example, but with some more variations of the same color. We won't change the saturation or lightness values, but we'll change the hue value by 10 degrees for each box:

```
<div id="color-1"></div>
<div id="color-2"></div>
<div id="color-3"></div>
<div id="color-4"></div>
<div id="color-5"></div>
<div id="color-6"></div>
<div id="color-7"></div>
<input type="range" min="0" max="360" value="0" step="0.1" id="hue" />
```
We're building on the example in the previous section, but adding a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc) function so that we can calculate different colors based on the hue value of the first box.
For each box, we're adding 10 degrees to the hue value of the previous box:

```
:root {
  --hue: 0;
}
#color-1 {
  background-color: hsl(var(--hue) 100% 50%);
}
#color-2 {
  background-color: hsl(calc(var(--hue) + 10) 100% 50%);
}
#color-3 {
  background-color: hsl(calc(var(--hue) + 20) 100% 50%);
}
#color-4 {
  background-color: hsl(calc(var(--hue) + 30) 100% 50%);
}
#color-5 {
  background-color: hsl(calc(var(--hue) + 40) 100% 50%);
}
#color-6 {
  background-color: hsl(calc(var(--hue) + 50) 100% 50%);
}
#color-7 {
  background-color: hsl(calc(var(--hue) + 60) 100% 50%);
}
```
```
const hue = document.querySelector("#hue");
const updateHue = () => {
  document.documentElement.style.setProperty("--hue", hue.value);
};
hue.addEventListener("input", updateHue);
```
Now we're starting to get colorful! We can cycle 360 degrees through the color wheel and see how the colors change by hue angle, with each box being 10 degrees apart.

## [Summary](https://developer.mozilla.org#summary)

Let's have a recap of what we've learned in this article. We've covered:

- Common ways to specify colors: [named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color), the [`rgb()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb), and [hexadecimal values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
- What [hues](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue) are and why the [`hsl()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl) is a good starting point for hues in CSS
- How to calculate variations of a color using [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) and the [`calc()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)

## [Next steps](https://developer.mozilla.org#next_steps)

Now that you know how to use the `hsl()` function, it would be interesting to extend the examples in this post or try out [alpha values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#syntax) to make colors transparent.
Can you build on the last example and control other values like saturation and lightness?
What about building a color picker or try converting `rgb()` to `hsl()` values?

If you want to learn more, be sure to check out the [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue) reference page for details on hue angles and other color functions.
Be sure to have a look at the [hue interpolation methods](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method) page, which is an interesting read if you want to know more about calculating colors between two hues, especially if you want to create gradients or mix colors.
The previous article [New functions, gradients, and hues in CSS colors (Level 4)](https://developer.mozilla.org/en-US/blog/css-color-module-level-4/) has a comprehensive overview of the different color functions and what they look like.

I hope you enjoyed the post. Feel free to get in touch with us on our [Discord server](https://developer.mozilla.org/discord) or [on GitHub](https://github.com/orgs/mdn/discussions/categories/the-mdn-web-docs-blog) to share your thoughts, ask questions, or to show us what you've built.
I want to send a big thanks to [Yarusome](https://www.github.com/yarusome) for making improvements to the hue and interpolation documentation and adding brilliant diagrams to help explain the concepts.
Until next time, and happy hacking! ð¨