---
id: "express.js_008"
technology: "Express.js"
category: "Backend & APIs"
title: "API Response Overview · Express.js 3.x"
doc_order: 8
source_url: "https://expressjs.com/en/3x/api/response"
language: "en"
retrieved_at: "2026-11-03 17:40:08"
content_hash: "5d53ee07330a3d2e35ce073d1a4531d93d00a3cfcc16a6c48a24bf0dfe94cdfb"
---

# API Response Overview · Express.js 3.x

Source: https://expressjs.com/en/3x/api/response

---

The `res` object is an enhanced version of Node’s own response object
and supports all [built-in fields and methods](https://nodejs.org/api/http.html#class-httpserverresponse).

The `res` object contains a number of properties that provide information about the HTTP response.

Assign the charset. Defaults to “utf-8”.

Response local variables are scoped to the request, thus only
available to the view(s) rendered during that request / response
cycle, if any. Otherwise this API is identical to [app.locals](https://expressjs.com/en/3x/api/application/#applocals).

This object is useful for exposing request-level information such as the request pathname, authenticated user, user settings etcetera.

This property holds a reference to the [request object](https://expressjs.com/en/3x/api/request/)
that relates to this response object.

The `res` object contains a number of methods that can be used to send responses, set headers, and more.

Sets the Content-Disposition header field to “attachment”. If
a `filename` is given then the Content-Type will be
automatically set based on the extname via `res.type()`,
and the Content-Disposition’s “filename=” parameter will be set.

Clear cookie `name`. The `path` option defaults to ”/“.

Set cookie `name` to `value`, which may be a string or object converted to JSON. The `path`
option defaults to ”/”.

The `maxAge` option is a convenience option for setting “expires”
relative to the current time in milliseconds. The following is equivalent to
the previous example.

An object may be passed which is then serialized as JSON, which is
automatically parsed by the `bodyParser()` middleware.

Signed cookies are also supported through this method. Simply
pass the `signed` option. When given `res.cookie()`
will use the secret passed to `express.cookieParser(secret)`
to sign the value.

Later you may access this value through the [req.signedCookie](https://expressjs.com/en/3x/api/request/#reqsignedcookies)
object.

Transfer the file at `path` as an “attachment”,
typically browsers will prompt the user for download. The
Content-Disposition “filename=” parameter, aka the one
that will appear in the browser dialog is set to `path`
by default, however you may provide an override `filename`.

When an error has occurred or transfer is complete the optional
callback `fn` is invoked. This method uses [res.sendfile()](https://expressjs.com#ressendfilepath-options-fn)
to transfer the file.

Performs content-negotiation on the request Accept header
field when present. This method uses `req.accepted`, an array of
acceptable types ordered by their quality values, otherwise the
first callback is invoked. When no match is performed the server
responds with 406 “Not Acceptable”, or invokes the `default`
callback.

The Content-Type is set for you when a callback is selected,
however you may alter this within the callback using `res.set()`
or `res.type()` etcetera.

The following example would respond with `{ "message": "hey" }`
when the Accept header field is set to “application/json” or “*/json”,
however if ”*/\*” is given then “hey” will be the response.

In addition to canonicalized MIME types you may also use extnames mapped to these types, providing a slightly less verbose implementation:

Get the case-insensitive response header `field`.

Send a JSON response. This method is identical
to `res.send()` when an object or
array is passed, however it may be used for
explicit JSON conversion of non-objects (null, undefined, etc),
though these are technically not valid JSON.

Send a JSON response with JSONP support. This method is identical
to `res.json()` however opts-in to JSONP callback
support.

By default the JSONP callback name is simply `callback`,
however you may alter this with the [jsonp callback name](https://expressjs.com/en/3x/api/application/#settings)
setting. The following are some examples of JSONP responses using the same
code:

Join the given `links` to populate the “Link” response header field.

p yields:

Set the location header.

You can use the same kind of `urls` as in `res.redirect()`.

For example, if your application is mounted at `/blog`,
the following would set the `location` header to
`/blog/admin`:

Redirect to the given `url` with optional `status` code
defaulting to 302 “Found”.

Express supports a few forms of redirection, first being a fully qualified URI for redirecting to a different site:

The second form is the pathname-relative redirect, for example
if you were on `http://example.com/admin/post/new`, the
following redirect to `/admin` would land you at `http://example.com/admin`:

This next redirect is relative to the `mount` point of the application. For example
if you have a blog application mounted at `/blog`, ideally it has no knowledge of
where it was mounted, so where a redirect of `/admin/post/new` would simply give you
`http://example.com/admin/post/new`, the following mount-relative redirect would give
you `http://example.com/blog/admin/post/new`:

Pathname relative redirects are also possible. If you were
on `http://example.com/admin/post/new`, the following redirect
would land you at `http//example.com/admin/post`:

The final special-case is a `back` redirect, redirecting back to
the Referer (or Referrer), defaulting to `/` when missing.

Render a `view` with a callback responding with
the rendered string. When an error occurs `next(err)`
is invoked internally. When a callback is provided both the possible error
and rendered string are passed, and no automated response is performed.

Send a response.

This method performs a myriad of
useful tasks for simple non-streaming responses such
as automatically assigning the Content-Length unless
previously defined and providing automatic *HEAD* and
HTTP cache freshness support.

When a `Buffer` is given
the Content-Type is set to “application/octet-stream”
unless previously defined as shown below:

When a `String` is given the
Content-Type is set defaulted to “text/html”:

When an `Array` or `Object` is
given Express will respond with the JSON representation:

Finally when a `Number` is given without
any of the previously mentioned bodies, then a response
body string is assigned for you. For example 200 will
respond will the text “OK”, and 404 “Not Found” and so on.

Transfer the file at the given `path`.

Automatically defaults the Content-Type response header field based
on the filename’s extension. The callback `fn(err)` is
invoked when the transfer is complete or when an error occurs.

Options:

- `maxAge` in milliseconds defaulting to 0
- `root` root directory for relative filenames

This method provides fine-grained support for file serving as illustrated in the following example:

Set header `field` to `value`, or pass an object to set multiple fields at once.

Aliased as `res.header(field, [value])`.

Chainable alias of node’s `res.statusCode=`.

Sets the Content-Type to the mime lookup of `type`,
or when ”/” is present the Content-Type is simply set to this
literal value.

p Aliased as `res.contentType(type)`.