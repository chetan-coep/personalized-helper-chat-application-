---
id: "express.js_013"
technology: "Express.js"
category: "Backend & APIs"
title: "Response · Express.js 4.x"
doc_order: 13
source_url: "https://expressjs.com/en/4x/api/response"
language: "en"
retrieved_at: "2026-11-03 17:40:19"
content_hash: "2c531416c24b74f455b261f4a1b20aca37b930d87c704aab3fc258e7b8b1f662"
---

# Response · Express.js 4.x

Source: https://expressjs.com/en/4x/api/response

---

The `res` object represents the HTTP response that an Express app sends when it gets an HTTP request.

In this documentation and by convention,
the object is always referred to as `res` (and the HTTP request is `req`) but its actual name is determined
by the parameters to the callback function in which you’re working.

For example:

But you could just as well have:

The `res` object is an enhanced version of Node’s own response object
and supports all [built-in fields and methods](https://nodejs.org/api/http.html#class-httpserverresponse).

This property holds a reference to the instance of the Express application that is using the middleware.

`res.app` is identical to the [req.app](https://expressjs.com/en/4x/api/request/#reqapp) property in the request object.

Boolean property that indicates if the app sent HTTP headers for the response.

Use this property to set variables accessible in templates rendered with [res.render](https://expressjs.com#resrender).
The variables set on `res.locals` are available within a single request-response cycle, and will not
be shared between requests.

### Warning

The `locals` object is used by view engines to render a response. The object keys may be
particularly sensitive and should not contain user-controlled input, as it may affect the
operation of the view engine or provide a path to cross-site scripting. Consult the documentation
for the used view engine for additional considerations.

In order to keep local variables for use in template rendering between requests, use
[app.locals](https://expressjs.com/en/4x/api/application/#applocals) instead.

This property is useful for exposing request-level information such as the request path name, authenticated user, user settings, and so on to templates rendered within the application.

This property holds a reference to the [request object](https://expressjs.com/en/4x/api/request/)
that relates to this response object.

#### Arguments

`field`
The name of the HTTP response header to append to.

`value`
The value(s) to append to the header.

Appends the specified `value` to the HTTP response header `field`. If the header is not already set,
it creates the header with the specified value. The `value` parameter can be a string or an array.

### Note

calling `res.set()` after `res.append()` will reset the previously-set header value.

#### Arguments

`filename`
The file name used to set the `Content-Disposition` “filename=” parameter and the
`Content-Type` (from its extension).

Sets the HTTP response `Content-Disposition` header field to “attachment”. If a `filename` is given,
then it sets the Content-Type based on the extension name via `res.type()`,
and sets the `Content-Disposition` “filename=” parameter.

Clears the cookie with the specified `name` by sending a `Set-Cookie` header that sets its expiration date in the past.
This instructs the client that the cookie has expired and is no longer valid. For more information
about available `options`, see [res.cookie()](https://expressjs.com#rescookie).

### Caution

If the `maxAge` or `expires` options are set, the cookie may not be cleared depending on the time
values provided, as Express does not ignore these options. It is therefore recommended to omit
these options when calling this method. Passing these two options has been deprecated since
Express v4.20.0.

### Caution

#### Arguments

`name`
The name of the cookie.

`value`
The cookie value; an object is serialized as JSON.

`options`
Options for the `Set-Cookie` header.

`domain`
Domain name for the cookie. Defaults to the domain name of the app.

`encode`
A synchronous function used for cookie value encoding. Defaults to `encodeURIComponent`.

`expires`
Expiry date of the cookie in GMT. If not specified or set to `0`, creates a session cookie.

`httpOnly`
Flags the cookie to be accessible only by the web server.

`maxAge`
Convenient option for setting the expiry time relative to the current time in milliseconds.

`path`
Path for the cookie. Defaults to ”/”.

`partitioned``priority`
Value of the “Priority” **Set-Cookie** attribute.

`secure`
Marks the cookie to be used with HTTPS only.

`signed`
Indicates if the cookie should be signed.

`sameSite`
Value of the “SameSite” **Set-Cookie** attribute.

Sets cookie `name` to `value`. The `value` parameter may be a string or object converted to JSON.

### Caution

For example:

You can set multiple cookies in a single response by calling `res.cookie` multiple times, for example:

The `encode` option allows you to choose the function used for cookie value encoding.
Does not support asynchronous functions.

Example use case: You need to set a domain-wide cookie for another site in your organization. This other site (not under your administrative control) does not use URI-encoded cookie values.

The `maxAge` option is a convenience option for setting “expires” relative to the current time in milliseconds.
The following is equivalent to the second example above.

You can pass an object as the `value` parameter; it is then serialized as JSON and parsed by `bodyParser()` middleware.

When using [cookie-parser](https://www.npmjs.com/package/cookie-parser) middleware, this method also
supports signed cookies. Simply include the `signed` option set to `true`.
Then `res.cookie()` will use the secret passed to `cookieParser(secret)` to sign the value.

Later you may access this value through the [req.signedCookie](https://expressjs.com/en/4x/api/request/#reqsignedcookies) object.

#### Arguments

`path`
The path to the file to transfer. If relative, it is resolved against the current working directory or the `root` option.

`filename`
The file name for the `Content-Disposition` “filename=” parameter; overrides the name derived from `path`.

`options``maxAge``root`
Root directory for relative file names.

`lastModified`
Sets the `Last-Modified` header to the last modified date of the file on the OS. Set `false` to disable it.

`headers`
Object containing HTTP headers to serve with the file.

`dotfiles`
Option for serving dotfiles. Possible values are `"allow"`, `"deny"`, and `"ignore"`.

`acceptRanges`
Enable or disable accepting ranged requests.

`cacheControl`
Enable or disable setting the `Cache-Control` response header.

`immutable`
Enable or disable the `immutable` directive in the `Cache-Control` response header. If enabled, the `maxAge` option should also be specified to enable caching.

`fn`
Callback `fn(err)` invoked when the transfer completes or an error occurs.

Transfers the file at `path` as an “attachment”. Typically, browsers will prompt the user for download.
By default, the `Content-Disposition` header “filename=” parameter is derived from the `path` argument, but can be overridden with the `filename` parameter.
If `path` is relative, then it will be based on the current working directory of the process or
the `root` option, if provided.

### Warning

This API provides access to data on the running file system. Ensure that either (a) the way in
which the `path` argument was constructed is secure if it contains user input or (b) set the `root`
option to the absolute path of a directory to contain access within.

When the `root` option is provided, Express will validate that the relative path provided as
`path` will resolve within the given `root` option.

The method invokes the callback function `fn(err)` when the transfer is complete
or when an error occurs. If the callback function is specified and an error occurs,
the callback function must explicitly handle the response process either by
ending the request-response cycle, or by passing control to the next route.

#### Arguments

`data`
Data to write before ending the response.

`encoding`
The encoding for `data` when it is a string.

`callback`
Called once the response has finished.

Ends the response process. This method actually comes from Node core, specifically the [response.end() method of http.ServerResponse](https://nodejs.org/api/http.html#responseenddata-encoding-callback).

Use to quickly end the response without any data. If you need to respond with data, instead use methods such as [res.send()](https://expressjs.com#ressend) and [res.json()](https://expressjs.com#resjson).

#### Arguments

`object`
An object whose keys are MIME types (or extension names) mapped to handler functions,
optionally with a `default` handler.

Performs content-negotiation on the `Accept` HTTP header on the request object, when present.
It uses [req.accepts()](https://expressjs.com/en/4x/api/request/#reqaccepts) to select a handler for the request, based on the acceptable
types ordered by their quality values. If the header is not specified, the first callback is invoked.
When no match is found, the server responds with 406 “Not Acceptable”, or invokes the `default` callback.

The `Content-Type` response header is set when a callback is selected. However, you may alter
this within the callback using methods such as `res.set()` or `res.type()`.

The following example would respond with `{ "message": "hey" }` when the `Accept` header field is set
to “application/json” or ”\*/json” (however if it is ”\*/\*”, then the response will be “hey”).

In addition to canonicalized MIME types, you may also use extension names mapped to these types for a slightly less verbose implementation:

#### Arguments

`field`
The name of the response header to read (case-insensitive).

Returns the HTTP response header specified by `field`.
The match is case-insensitive.

#### Arguments

`body`
The value to send as JSON. Can be any JSON type: object, array, string, Boolean, number, or null.

Sends a JSON response. This method sends a response (with the correct content-type) that is the parameter converted to a
JSON string using [JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

The parameter can be any JSON type, including object, array, string, Boolean, number, or null, and you can also use it to convert other values to JSON.

### Caution

The signature `res.json(obj, status)` has been deprecated since Express v4.2.0 (and the reversed `res.json(status, obj)` since v4.7.0). Set the status separately and chain the call instead: `res.status(status).json(obj)`.

You can update your code automatically with the following codemod:

#### Arguments

`body`
The value to send as a JSONP response. Can be any JSON type.

Sends a JSON response with JSONP support. This method is identical to `res.json()`,
except that it opts-in to JSONP callback support.

By default, the JSONP callback name is simply `callback`. Override this with the

[jsonp callback name](https://expressjs.com/en/4x/api/application/#application-settings) setting.

The following are some examples of JSONP responses using the same code:

### Caution

The signature `res.jsonp(obj, status)` has been deprecated since Express v4.2.0 (and the reversed `res.jsonp(status, obj)` since v4.7.0). Set the status separately and chain the call instead: `res.status(status).jsonp(obj)`.

You can update your code automatically with the following codemod:

#### Arguments

`links`
An object whose properties (such as `next` and `last`) populate the `Link` response header.

Joins the `links` provided as properties of the parameter to populate the response’s
`Link` HTTP header field.

For example, the following call:

Yields the following results:

#### Arguments

`path`
The URL to set in the `Location` header.

Sets the response `Location` HTTP header to the specified `path` parameter.

### Caution

`'back'` was deprecated in 4.21.0, use `req.get('Referrer') || '/'` as an argument instead.

A `path` value of “back” has a special meaning, it refers to the URL specified in the `Referer` header of the request. If the `Referer` header was not specified, it refers to ”/”.

See also [Security best practices: Prevent open redirect
vulnerabilities](https://expressjs.com/en/advanced/best-practice-security/#prevent-open-redirects).

### Warning

After encoding the URL, if not encoded already, Express passes the specified URL to the browser in the `Location` header,
without any validation.

Browsers take the responsibility of deriving the intended URL from the current URL
or the referring URL, and the URL specified in the `Location` header; and redirect the user accordingly.

#### Arguments

`status`
The HTTP status code to use. Defaults to `302` (Found).

`path`
The URL to redirect to.

Redirects to the URL derived from the specified `path`, with specified `status`, a positive integer
that corresponds to an [HTTP status code](https://www.rfc-editor.org/rfc/rfc9110#name-status-codes) .
If not specified, `status` defaults to 302 “Found”.

### Caution

The reversed signature `res.redirect(path, status)` (status as the second argument) has been deprecated since Express v4.6.0. Use `res.redirect(status, path)` instead.

You can update your code automatically with the following codemod:

Redirects can be a fully-qualified URL for redirecting to a different site:

Redirects can be relative to the root of the host name. For example, if the
application is on `http://example.com/admin/post/new`, the following
would redirect to the URL `http://example.com/admin`:

Redirects can be relative to the current URL. For example,
from `http://example.com/blog/admin/` (notice the trailing slash), the following
would redirect to the URL `http://example.com/blog/admin/post/new`.

Redirecting to `post/new` from `http://example.com/blog/admin` (no trailing slash),
will redirect to `http://example.com/blog/post/new`.

If you found the above behavior confusing, think of path segments as directories (with trailing slashes) and files, it will start to make sense.

Path-relative redirects are also possible. If you were on
`http://example.com/admin/post/new`, the following would redirect to
`http://example.com/admin/post`:

A `back` redirection redirects the request back to the [referer](https://en.wikipedia.org/wiki/HTTP_referer),
defaulting to `/` when the referer is missing.

### Caution

`back` redirect was deprecated in 4.21.0, use `req.get('Referrer') || '/'` as an argument instead.

See also [Security best practices: Prevent open redirect
vulnerabilities](https://expressjs.com/en/advanced/best-practice-security/#prevent-open-redirects).

#### Arguments

`view`
The file path of the view to render (absolute or relative to the `views` setting).

`locals`
An object whose properties define local variables for the view.

`callback`
Called as `callback(err, html)`. When provided, the rendered HTML is not sent automatically.

Renders a `view` and sends the rendered HTML string to the client.
Optional parameters:

- `locals`, an object whose properties define local variables for the view.
- `callback`, a callback function. If provided, the method returns both the possible error and rendered string, but does not perform an automated response. When an error occurs, the method invokes `next(err)` internally.

The `view` argument is a string that is the file path of the view file to render. This can be an absolute path, or a path relative to the `views` setting. If the path does not contain a file extension, then the `view engine` setting determines the file extension. If the path does contain a file extension, then Express will load the module for the specified template engine (via `require()`) and render it using the loaded module’s `__express` function.

For more information, see [Using template engines with Express](https://expressjs.com/en/4x/guide/using-template-engines/).

### Warning

The `view` argument performs file system operations like reading a file from disk and evaluating
Node.js modules, and as so for security reasons should not contain input from the end-user.

### Warning

The `locals` object is used by view engines to render a response. The object keys may be
particularly sensitive and should not contain user-controlled input, as it may affect the
operation of the view engine or provide a path to cross-site scripting. Consult the documentation
for the used view engine for additional considerations.

### Caution

The local variable `cache` enables view caching. Set it to `true`, to cache the view during
development; view caching is enabled in production by default.

#### Arguments

`body`
The response body. Strings are sent as HTML; objects and arrays as JSON; Buffers as binary.

Sends the HTTP response.

The `body` parameter can be a `Buffer` object, a `String`, an object, `Boolean`, or an `Array`.
For example:

This method performs many useful tasks for simple non-streaming responses:
For example, it automatically assigns the `Content-Length` HTTP response header field
(unless previously defined) and provides automatic HEAD and HTTP cache freshness support.

When the parameter is a `Buffer` object, the method sets the `Content-Type`
response header field to “application/octet-stream”, unless previously defined as shown below:

When the parameter is a `String`, the method sets the `Content-Type` to “text/html”:

When the parameter is an `Array` or `Object`, Express responds with the JSON representation:

### Caution

The signatures `res.send(body, status)` and `res.send(status)` have been deprecated since Express v4.5.0 (the reversed `res.send(status, body)` since v4.7.0). To set the status, chain the call: `res.status(status).send(body)`. To send only a status code, use [`res.sendStatus()`](https://expressjs.com#ressendstatus). If you need to send a number as the body, convert it to a string first (for example, `res.send(String(123))`) so it is not interpreted as a status code.

You can update your code automatically with the following codemod:

#### Arguments

`path`
The path to the file to transfer. Must be absolute unless the `root` option is set.

`options`
Options for serving the file.

`maxAge``root`
Root directory for relative file names.

`lastModified`
Sets the `Last-Modified` header to the last modified date of the file on the OS. Set `false` to disable it.

`headers`
Object containing HTTP headers to serve with the file.

`dotfiles`
Option for serving dotfiles. Possible values are `"allow"`, `"deny"`, and `"ignore"`.

`acceptRanges`
Enable or disable accepting ranged requests.

`cacheControl`
Enable or disable setting the `Cache-Control` response header.

`immutable`
Enable or disable the `immutable` directive in the `Cache-Control` response header. If enabled, the `maxAge` option should also be specified to enable caching.

`fn`
Callback `fn(err)` invoked when the transfer completes or an error occurs.

Transfers the file at the given `path`. Sets the `Content-Type` response HTTP header field
based on the filename’s extension. Unless the `root` option is set in
the options object, `path` must be an absolute path to the file.

### Warning

This API provides access to data on the running file system. Ensure that either (a) the way in
which the `path` argument was constructed into an absolute path is secure if it contains user
input or (b) set the `root` option to the absolute path of a directory to contain access within.

When the `root` option is provided, the `path` argument is allowed to be a relative path,
including containing `..`. Express will validate that the relative path provided as `path` will
resolve within the given `root` option.

The method invokes the callback function `fn(err)` when the transfer is complete
or when an error occurs. If the callback function is specified and an error occurs,
the callback function must explicitly handle the response process either by
ending the request-response cycle, or by passing control to the next route.

Here is an example of using `res.sendFile` with all its arguments.

The following example illustrates using
`res.sendFile` to provide fine-grained support for serving files:

For more information, or if you have issues or concerns, see [send](https://github.com/pillarjs/send).

#### Arguments

`path`
The path to the file to transfer.

`options``fn`
Callback `fn(err)` invoked when the transfer completes or an error occurs.

### Caution

`res.sendfile()` (lower-cased) is the legacy version of [`res.sendFile()`](https://expressjs.com#ressendfile) and behaves identically. The camel-cased `res.sendFile()` was introduced in Express v4.8.0, and `res.sendfile()` has emitted a deprecation warning since that release. Use `res.sendFile()` instead.

You can update your code automatically with the following codemod:

Transfers the file at the given `path`. This is the legacy, lower-cased version of [`res.sendFile()`](https://expressjs.com#ressendfile) and behaves the same way. Prefer `res.sendFile()` in new code.

#### Arguments

`statusCode`
The HTTP status code to set; its registered status message becomes the response body.

Sets the response HTTP status code to `statusCode` and sends the registered status message as the text response body. If an unknown status code is specified, the response body will just be the code number.

### Caution

Some versions of Node.js will throw when `res.statusCode` is set to an invalid HTTP status code
(outside of the range `100` to `599`). Consult the HTTP server documentation for the Node.js
version being used.

#### Arguments

`field`
The header name, or an object of header name/value pairs to set multiple headers at once.

`value`
The header value (when `field` is a string).

Sets the response’s HTTP header `field` to `value`.
To set multiple fields at once, pass an object as the parameter.

Aliased as `res.header(field [, value])`.

#### Arguments

`code`
The HTTP status code for the response.

Sets the HTTP status for the response.
It is a chainable alias of Node’s [response.statusCode](https://nodejs.org/api/http.html#responsestatuscode).

#### Arguments

`type`
The MIME type, or a file extension that is looked up to a MIME type. If it contains `/`, it is
used as-is.

Sets the `Content-Type` HTTP header to the MIME type as determined by the specified `type`. If `type` contains the ”/” character, then it sets the `Content-Type` to the exact value of `type`, otherwise it is assumed to be a file extension and the MIME type is looked up in a mapping using the `express.static.mime.lookup()` method.

Aliased as `res.contentType(type)`.

#### Arguments

`field`
The header field name to add to the `Vary` response header.

Adds the field to the `Vary` response header, if it is not there already.