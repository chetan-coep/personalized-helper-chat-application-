---
id: "express.js_011"
technology: "Express.js"
category: "Backend & APIs"
title: "Express Object · Express.js 4.x"
doc_order: 11
source_url: "https://expressjs.com/en/4x/api/express"
language: "en"
retrieved_at: "2026-11-03 17:40:16"
content_hash: "1743bbe9fa33f39428da8f2391083d53a1e69518190b7aa25527ff588dc50d12"
---

# Express Object · Express.js 4.x

Source: https://expressjs.com/en/4x/api/express

---

Creates an Express application. The `express()` function is a top-level function exported by the `express` module.

#### Arguments

`options`
Configures how the JSON body is parsed; it accepts the properties below.

`inflate`
Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected.

`limit``reviver``strict`
Enables or disables only accepting arrays and objects; when disabled will accept anything
`JSON.parse` accepts.

`type`
This is used to determine what media type the middleware will parse. This option can be a
string, array of strings, or a function. If not a function, `type` option is passed
directly to the [type-is](https://www.npmjs.com/package/type-is#readme) library and this
can be an extension name (like `json`), a mime type (like `application/json`), or a mime
type with a wildcard (like `*/*` or `*/json`). If a function, the `type` option is called
as `fn(req)` and the request is parsed if it returns a truthy value.

`verify`
This option, if supplied, is called as `verify(req, res, buf, encoding)`, where `buf` is a
`Buffer` of the raw request body and `encoding` is the encoding of the request. The
parsing can be aborted by throwing an error.

This is a built-in middleware function in Express. It parses incoming requests
with JSON payloads and is based on
[body-parser](https://expressjs.com/en/resources/middleware/body-parser/).

Returns middleware that only parses JSON and only looks at requests where
the `Content-Type` header matches the `type` option. This parser accepts any
Unicode encoding of the body and supports automatic inflation of `gzip` and
`deflate` encodings.

A new `body` object containing the parsed data is populated on the `request`
object after the middleware (i.e. `req.body`), or an empty object (`{}`) if
there was no body to parse, the `Content-Type` was not matched, or an error
occurred.

### Warning

As `req.body`’s shape is based on user-controlled input, all properties and values in this object
are untrusted and should be validated before trusting. For example, `req.body.foo.toString()` may
fail in multiple ways, for example `foo` may not be there or may not be a string, and `toString`
may not be a function and instead a string or other user-input.

#### Arguments

`options`
Configures how the request body is parsed; it accepts the properties below.

`inflate`
Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected.

`limit``type`
This is used to determine what media type the middleware will parse. This option can be a
string, array of strings, or a function. If not a function, `type` option is passed
directly to the [type-is](https://www.npmjs.com/package/type-is#readme) library and this
can be an extension name (like `bin`), a mime type (like `application/octet-stream`), or a
mime type with a wildcard (like `*/*` or `application/*`). If a function, the `type`
option is called as `fn(req)` and the request is parsed if it returns a truthy value.

`verify`
This option, if supplied, is called as `verify(req, res, buf, encoding)`, where `buf` is a
`Buffer` of the raw request body and `encoding` is the encoding of the request. The
parsing can be aborted by throwing an error.

This is a built-in middleware function in Express. It parses incoming request
payloads into a `Buffer` and is based on
[body-parser](https://expressjs.com/en/resources/middleware/body-parser/).

Returns middleware that parses all bodies as a `Buffer` and only looks at requests
where the `Content-Type` header matches the `type` option. This parser accepts
any Unicode encoding of the body and supports automatic inflation of `gzip` and
`deflate` encodings.

A new `body` `Buffer` containing the parsed data is populated on the `request`
object after the middleware (i.e. `req.body`), or an empty object (`{}`) if
there was no body to parse, the `Content-Type` was not matched, or an error
occurred.

### Warning

As `req.body`’s shape is based on user-controlled input, all properties and values in this object
are untrusted and should be validated before trusting. For example, `req.body.toString()` may fail
in multiple ways, for example stacking multiple parsers `req.body` may be from a different parser.
Testing that `req.body` is a `Buffer` before calling buffer methods is recommended.

#### Arguments

`caseSensitive`
Enable case sensitivity. Disabled by default, treating `/Foo` and `/foo` as the same.

`mergeParams`
Preserve the `req.params` values from the parent router. If the parent and the child have
conflicting param names, the child’s value take precedence.

`strict`
Enable strict routing. Disabled by default, `/foo` and `/foo/` are treated the same by the
router.

Creates a new [router](https://expressjs.com/en/4x/api/router/) object.

You can add middleware and HTTP method routes (such as `get`, `put`, `post`, and
so on) to `router` just like an application.

For more information, see [Router](https://expressjs.com/en/4x/api/router/).

#### Arguments

`root`
The root directory from which to serve static assets.

`options``dotfiles``etag`
Enable or disable etag generation.

### Note

`express.static` always sends weak ETags.

`extensions`
Sets file extension fallbacks: If a file is not found, search for files with the specified
extensions and serve the first one found. Example: `['html', 'htm']`.

`fallthrough``immutable`
Enable or disable the `immutable` directive in the `Cache-Control` response header. If
enabled, the `maxAge` option should also be specified to enable caching. The `immutable`
directive will prevent supported clients from making conditional requests during the life
of the `maxAge` option to check if the file has changed.

`index`
Sends the specified directory index file. Set to `false` to disable directory indexing.

`lastModified`
Set the `Last-Modified` header to the last modified date of the file on the OS.

`maxAge``redirect`
Redirect to trailing ”/” when the pathname is a directory.

`acceptRanges`
Enable or disable accepting ranged requests. Disabling this will not send the
`Accept-Ranges` header and will ignore the contents of the Range request header.

`cacheControl`
Enable or disable setting the `Cache-Control` response header. Disabling this will ignore
the immutable and maxAge options.

This is a built-in middleware function in Express.
It serves static files and is based on [serve-static](https://expressjs.com/en/resources/middleware/serve-static/).

The `root` argument specifies the root directory from which to serve static assets.
The function determines the file to serve by combining `req.url` with the provided `root` directory.
When a file is not found, instead of sending a 404 response, it calls `next()`
to move on to the next middleware, allowing for stacking and fall-backs.

For more information, see [Serving static files in Express](https://expressjs.com/en/4x/starter/static-files/).
and [Using middleware - Built-in middleware](https://expressjs.com/en/4x/guide/using-middleware/#built-in-middleware).

Possible values for this option are:

- “allow” - No special treatment for dotfiles.
- “deny” - Deny a request for a dotfile, respond with `403`, then call `next()`.
- “ignore” - Act as if the dotfile does not exist, respond with `404`, then call `next()`.
- `undefined` - Act as ignore, except that files in a directory that begins with a dot are **NOT** ignored.

When this option is `true`, client errors such as a bad request or a request to a non-existent
file will cause this middleware to simply call `next()` to invoke the next middleware in the stack.
When false, these errors (even 404s), will invoke `next(err)`.

Set this option to `true` so you can map multiple physical directories
to the same web address or for routes to fill in non-existent files.

Use `false` if you have mounted this middleware at a path designed
to be strictly a single file system directory, which allows for short-circuiting 404s
for less overhead. This middleware will also reply to all methods.

For this option, specify a function to set custom response headers. Alterations to the headers must occur synchronously.

The signature of the function is:

Arguments:

- `res`, the [response object](https://expressjs.com/en/4x/api/response/).
- `path`, the file path that is being sent.
- `stat`, the `stat` object of the file that is being sent.

Here is an example of using the `express.static` middleware function with an elaborate options object:

#### Arguments

`options`
Configures how the text body is parsed; it accepts the properties below.

`defaultCharset`
Specify the default character set for the text content if the charset is not specified in
the `Content-Type` header of the request.

`inflate`
Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected.

`limit``type`
This is used to determine what media type the middleware will parse. This option can be a
string, array of strings, or a function. If not a function, `type` option is passed
directly to the [type-is](https://www.npmjs.com/package/type-is#readme) library and this
can be an extension name (like `txt`), a mime type (like `text/plain`), or a mime type
with a wildcard (like `*/*` or `text/*`). If a function, the `type` option is called as
`fn(req)` and the request is parsed if it returns a truthy value.

`verify`
This option, if supplied, is called as `verify(req, res, buf, encoding)`, where `buf` is a
`Buffer` of the raw request body and `encoding` is the encoding of the request. The
parsing can be aborted by throwing an error.

This is a built-in middleware function in Express. It parses incoming request
payloads into a string and is based on
[body-parser](https://expressjs.com/en/resources/middleware/body-parser/).

Returns middleware that parses all bodies as a string and only looks at requests
where the `Content-Type` header matches the `type` option. This parser accepts
any Unicode encoding of the body and supports automatic inflation of `gzip` and
`deflate` encodings.

A new `body` string containing the parsed data is populated on the `request`
object after the middleware (i.e. `req.body`), or an empty object (`{}`) if
there was no body to parse, the `Content-Type` was not matched, or an error
occurred.

### Warning

As `req.body`’s shape is based on user-controlled input, all properties and values in this object
are untrusted and should be validated before trusting. For example, `req.body.trim()` may fail in
multiple ways, for example stacking multiple parsers `req.body` may be from a different parser.
Testing that `req.body` is a string before calling string methods is recommended.

#### Arguments

`options`
Configures how the URL-encoded body is parsed; it accepts the properties below.

`extended`
This option allows you to choose between parsing the URL-encoded data with the `querystring`
library (when `false`) or the `qs` library (when `true`). The “extended” syntax allows for
rich objects and arrays to be encoded into the URL-encoded format, allowing for a
JSON-like experience with URL-encoded. For more information, please [see the qs
library](https://www.npmjs.com/package/qs#readme).

`inflate`
Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected.

`limit``parameterLimit`
This option controls the maximum number of parameters that are allowed in the URL-encoded data. If a request contains more parameters than this value, an error will be raised.

`type`
This is used to determine what media type the middleware will parse. This option can be a
string, array of strings, or a function. If not a function, `type` option is passed
directly to the [type-is](https://www.npmjs.com/package/type-is#readme) library and this
can be an extension name (like `urlencoded`), a mime type (like
`application/x-www-form-urlencoded`), or a mime type with a wildcard (like
`*/x-www-form-urlencoded`). If a function, the `type` option is called as `fn(req)` and
the request is parsed if it returns a truthy value.

`verify`
This option, if supplied, is called as `verify(req, res, buf, encoding)`, where `buf` is a
`Buffer` of the raw request body and `encoding` is the encoding of the request. The
parsing can be aborted by throwing an error.

`depth`
Configure the maximum depth of the `qs` library when `extended` is `true`. This allows you
to limit the amount of keys that are parsed and can be useful to prevent certain types of
abuse. It is recommended to keep this value as low as possible.

This is a built-in middleware function in Express. It parses incoming requests
with urlencoded payloads and is based on [body-parser](https://expressjs.com/en/resources/middleware/body-parser/).

Returns middleware that only parses urlencoded bodies and only looks at
requests where the `Content-Type` header matches the `type` option. This
parser accepts only UTF-8 encoding of the body and supports automatic
inflation of `gzip` and `deflate` encodings.

A new `body` object containing the parsed data is populated on the `request`
object after the middleware (i.e. `req.body`), or an empty object (`{}`) if
there was no body to parse, the `Content-Type` was not matched, or an error
occurred. This object will contain key-value pairs, where the value can be
a string or array (when `extended` is `false`), or any type (when `extended`
is `true`).

### Warning

As `req.body`’s shape is based on user-controlled input, all properties and values in this object
are untrusted and should be validated before trusting. For example, `req.body.foo.toString()` may
fail in multiple ways, for example `foo` may not be there or may not be a string, and `toString`
may not be a function and instead a string or other user-input.