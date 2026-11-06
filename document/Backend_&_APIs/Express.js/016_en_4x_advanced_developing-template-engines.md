---
id: "express.js_016"
technology: "Express.js"
category: "Backend & APIs"
title: "Developing template engines for Express · Express.js 4.x"
doc_order: 16
source_url: "https://expressjs.com/en/4x/advanced/developing-template-engines"
language: "en"
retrieved_at: "2026-11-03 17:40:12"
content_hash: "cae62020fff3dc6e14cb10caa4b68a094335909be63a83404108c08e49a7224c"
---

# Developing template engines for Express · Express.js 4.x

Source: https://expressjs.com/en/4x/advanced/developing-template-engines

---

Use the app.engine(ext, callback) method to create your own template engine. ext refers to the file extension, and callback is the template engine function, which accepts the following items as parameters: the location of the file, the options object, and the callback function.

The following code is an example of implementing a very simple template engine for rendering .ntl files.

Your app will now be able to render .ntl files. Create a file named index.ntl in the views directory with the following content.

Then, create the following route in your app.

When you make a request to the home page, index.ntl will be rendered as HTML.