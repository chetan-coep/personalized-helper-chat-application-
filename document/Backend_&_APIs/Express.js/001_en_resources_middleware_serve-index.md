---
id: "express.js_001"
technology: "Express.js"
category: "Backend & APIs"
title: "serve-index middleware · Express.js"
doc_order: 1
source_url: "https://expressjs.com/en/resources/middleware/serve-index"
language: "en"
retrieved_at: "2026-11-03 17:40:01"
content_hash: "7228fc0df0786624e2cba0d527d81ba31146cc47af1d210799a7937b07360419"
---

# serve-index middleware · Express.js

Source: https://expressjs.com/en/resources/middleware/serve-index

---

Serves pages that contain directory listings for a given path.

This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):

### Note

Returns middleware that serves an index of the directory in the given `path`.

The `path` is based off the `req.url` value, so a `req.url` of `'/some/dir`
with a `path` of `'public'` will look at `'public/some/dir'`. If you are using
something like `express`, you can change the URL “base” with `app.use` (see
the express example).

Serve index accepts these properties in the options object.

Apply this filter function to files. Defaults to `false`. The `filter` function
is called for each file, with the signature `filter(filename, index, files, dir)`
where `filename` is the name of the file, `index` is the array index, `files` is
the array of files and `dir` is the absolute path the file is located (and thus,
the directory the listing is for).

Display hidden (dot) files. Defaults to `false`.

Display icons. Defaults to `false`.

Optional path to a CSS stylesheet. Defaults to a built-in stylesheet.

Optional path to an HTML template or a function that will render a HTML string. Defaults to a built-in template.

When given a string, the string is used as a file path to load and then the following tokens are replaced in templates:

- `{directory}` with the name of the directory.
- `{files}` with the HTML of an unordered list of file links.
- `{linked-path}` with the HTML of a link to the directory.
- `{style}` with the specified stylesheet and embedded images.

When given as a function, the function is called as `template(locals, callback)`
and it needs to invoke `callback(error, htmlString)`. The following are the
provided locals:

- `directory` is the directory being displayed (where `/` is the root).
- `displayIcons` is a Boolean for if icons should be rendered or not.
- `fileList` is a sorted array of files in the directory. The array contains
objects with the following properties:
  - `name` is the relative name for the file.
  - `stat` is a `fs.Stats` object for the file.
- `path` is the full filesystem path to `directory`.
- `style` is the default stylesheet or the contents of the `stylesheet` option.
- `viewName` is the view name provided by the `view` option.

Display mode. `tiles` and `details` are available. Defaults to `tiles`.