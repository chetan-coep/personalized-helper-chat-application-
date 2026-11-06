---
id: "express.js_012"
technology: "Express.js"
category: "Backend & APIs"
title: "Request Object · Express.js 4.x"
doc_order: 12
source_url: "https://expressjs.com/en/4x/api/request"
language: "en"
retrieved_at: "2026-11-03 17:40:18"
content_hash: "f40b50ce388d9db4106921cb0cbf843dc25a8efd09121223a279bb4130a66335"
---

# Request Object · Express.js 4.x

Source: https://expressjs.com/en/4x/api/request

---

The `req` object represents the HTTP request and has properties for the
request query string, parameters, body, HTTP headers, and so on. In this documentation and by convention,
the object is always referred to as `req` (and the HTTP response is `res`) but its actual name is determined
by the parameters to the callback function in which you’re working.

For example:

But you could just as well have:

The `req` object is an enhanced version of Node’s own request object
and supports all [built-in fields and methods](https://nodejs.org/api/http.html#class-httpincomingmessage).

The `req` object contains a number of properties that provide information about the HTTP request, such as headers, query parameters, and more.

### Caution

In Express 4, `req.files` is no longer available on the `req` object by default. To access uploaded files
on the `req.files` object, use multipart-handling middleware like [multer](https://www.npmjs.com/package/multer), [multiparty](https://www.npmjs.com/package/multiparty), [busboy](https://www.npmjs.com/package/busboy),
[formidable](https://www.npmjs.com/package/formidable),
or [pez](https://www.npmjs.com/package/pez).

This property holds a reference to the instance of the Express application that is using the middleware.

If you follow the pattern in which you create a module that just exports a middleware function
and `require()` it in your main file, then the middleware can access the Express instance via `req.app`

For example:

And the middleware module itself:

The URL path on which a router instance was mounted.

The `req.baseUrl` property is similar to the [mountpath](https://expressjs.com/en/4x/api/application/#appmountpath) property of the `app` object,
except `app.mountpath` returns the matched path pattern(s).

For example:

Even if you use a path pattern or a set of path patterns to load the router,
the `baseUrl` property returns the matched string, not the pattern(s). In the
following example, the `greet` router is loaded on two path patterns.

When a request is made to `/greet/jp`, `req.baseUrl` is “/greet”. When a request is
made to `/hello/jp`, `req.baseUrl` is “/hello”.

Contains key-value pairs of data submitted in the request body.
By default, it is `undefined`, and is populated when you use body-parsing middleware such
as [`express.json()`](https://expressjs.com/en/4x/api/express/#expressjson) or [`express.urlencoded()`](https://expressjs.com/en/4x/api/express/#expressurlencoded).

### Warning

As `req.body`’s shape is based on user-controlled input, all properties and values in this object
are untrusted and should be validated before trusting. For example, `req.body.foo.toString()` may
fail in multiple ways, for example `foo` may not be there or may not be a string, and `toString`
may not be a function and instead a string or other user-input.

The following example shows how to use body-parsing middleware to populate `req.body`.

When using [cookie-parser](https://www.npmjs.com/package/cookie-parser) middleware, this property is an object that
contains cookies sent by the request. If the request contains no cookies, it defaults to `{}`.

If the cookie has been signed, you have to use [req.signedCookies](https://expressjs.com#reqsignedcookies).

For more information, issues, or concerns, see [cookie-parser](https://github.com/expressjs/cookie-parser).

When the response is still “fresh” in the client’s cache `true` is returned, otherwise `false` is returned to indicate that the client cache is now stale and the full response should be sent.

When a client sends the `Cache-Control: no-cache` request header to indicate an end-to-end reload request, this module will return `false` to make handling these requests transparent.

Further details for how cache validation works can be found in the
[HTTP/1.1 Caching Specification](https://tools.ietf.org/html/rfc7234).

Contains the hostname derived from the `Host` HTTP header.

When the [`trust proxy` setting](https://expressjs.com/en/4x/api/application/#options-for-trust-proxy-setting)
does not evaluate to `false`, this property will instead get the value
from the `X-Forwarded-Host` header field. This header can be set by
the client or by the proxy.

If there is more than one `X-Forwarded-Host` header in the request, the
value of the first header is used. This includes a single header with
comma-separated values, in which the first value is used.

### Note

Prior to Express v4.17.0, the `X-Forwarded-Host` could not contain multiple values or be present
more than once.

### Caution

`req.host` is a deprecated alias of [`req.hostname`](https://expressjs.com#reqhostname) and returns the same value — the hostname with the port number stripped off. It has emitted a deprecation warning since Express v4.5.0. Use `req.hostname` instead.

Contains the remote IP address of the request.

When the [`trust proxy` setting](https://expressjs.com/en/4x/api/application/#options-for-trust-proxy-setting) does not evaluate to `false`,
the value of this property is derived from the left-most entry in the
`X-Forwarded-For` header. This header can be set by the client or by the proxy.

When the [`trust proxy` setting](https://expressjs.com/en/4x/api/application/#options-for-trust-proxy-setting) does not evaluate to `false`,
this property contains an array of IP addresses
specified in the `X-Forwarded-For` request header. Otherwise, it contains an
empty array. This header can be set by the client or by the proxy.

For example, if `X-Forwarded-For` is `client, proxy1, proxy2`, `req.ips` would be
`["client", "proxy1", "proxy2"]`, where `proxy2` is the furthest downstream.

Contains a string corresponding to the HTTP method of the request:
`GET`, `POST`, `PUT`, and so on.

This property is much like `req.url`; however, it retains the original request URL,
allowing you to rewrite `req.url` freely for internal routing purposes. For example,
the “mounting” feature of [app.use()](https://expressjs.com/en/4x/api/application/#appuse) will rewrite `req.url` to strip the mount point.

`req.originalUrl` is available both in middleware and router objects, and is a
combination of `req.baseUrl` and `req.url`. Consider following example:

This property is an object containing properties mapped to the [named route “parameters”](https://expressjs.com/en/4x/guide/routing/#route-parameters). For example, if you have the route `/user/:name`, then the “name” property is available as `req.params.name`. This object defaults to `{}`.

When you use a regular expression for the route definition, capture groups are provided as integer keys using `req.params[n]`, where `n` is the n<sup>th</sup> capture group. This rule is applied to unnamed wild card matches with string routes such as `/file/*`:

Named capturing groups in regular expressions behave like named route parameters. For example the group from `/^\/file\/(?<path>.*)$/` expression is available as `req.params.path`.

If you need to make changes to a key in `req.params`, use the [app.param](https://expressjs.com/en/4x/api/application/#appparam) handler. Changes are applicable only to [parameters](https://expressjs.com/en/4x/guide/routing/#route-parameters) already defined in the route path.

Any changes made to the `req.params` object in a middleware or route handler will be reset.

### Note

Express automatically decodes the values in `req.params` (using `decodeURIComponent`).

Contains the path part of the request URL.

### Note

Contains the request protocol string: either `http` or (for TLS requests) `https`.

When the [`trust proxy` setting](https://expressjs.com/en/4x/api/application/#options-for-trust-proxy-setting) does not evaluate to `false`,
this property will use the value of the `X-Forwarded-Proto` header field if present.
This header can be set by the client or by the proxy.

This property is an object containing a property for each query string parameter in the route.
When [query parser](https://expressjs.com/en/4x/api/application/#application-settings) is set to disabled, it is an empty object `{}`, otherwise it is the result of the configured query parser.

### Warning

As `req.query`’s shape is based on user-controlled input, all properties and values in this object
are untrusted and should be validated before trusting. For example, `req.query.foo.toString()` may
fail in multiple ways, for example `foo` may not be there or may not be a string, and `toString`
may not be a function and instead a string or other user-input.

The value of this property can be configured with the [query parser application setting](https://expressjs.com/en/4x/api/application/#application-settings) to work how your application needs it. A very popular query string parser is the [`qs` module](https://www.npmjs.com/package/qs), and this is used by default. The `qs` module is very configurable with many settings, and it may be desirable to use different settings than the default to populate `req.query`:

Check out the [query parser application setting](https://expressjs.com/en/4x/api/application/#application-settings) documentation for other customization options.

This property holds a reference to the [response object](https://expressjs.com/en/4x/api/response/)
that relates to this request object.

Contains the currently-matched route (a `Route` object). For example:

Example output from the previous snippet:

A Boolean property that is true if a TLS connection is established. Equivalent to:

When using [cookie-parser](https://www.npmjs.com/package/cookie-parser) middleware, this property
contains signed cookies sent by the request, unsigned and ready for use. Signed cookies reside
in a different object to show developer intent; otherwise, a malicious attack could be placed on
`req.cookie` values (which are easy to spoof). Note that signing a cookie does not make it “hidden”
or encrypted; but simply prevents tampering (because the secret used to sign is private).

If no signed cookies are sent, the property defaults to `{}`.

For more information, issues, or concerns, see [cookie-parser](https://github.com/expressjs/cookie-parser).

Indicates whether the request is “stale,” and is the opposite of `req.fresh`.
For more information, see [req.fresh](https://expressjs.com#reqfresh).

An array of subdomains in the domain name of the request.

The application property `subdomain offset`, which defaults to 2, is used for determining the
beginning of the subdomain segments. To change this behavior, change its value
using [app.set](https://expressjs.com/en/4x/api/application/#appset).

A Boolean property that is `true` if the request’s `X-Requested-With` header field is
“XMLHttpRequest”, indicating that the request was issued by a client library such as jQuery.

The `req` object also contains a number of methods that can be used to perform various tasks related to the HTTP request, such as checking the content type, retrieving header values, and more.

#### Arguments

`types`
The content type(s) to check: a MIME type (such as `application/json`), an extension name
(such as `json`), a comma-delimited list, or an array.

Checks if the specified content types are acceptable, based on the request’s `Accept` HTTP header field.
The method returns the best match, or if none of the specified content types is acceptable, returns
`false` (in which case, the application should respond with `406 "Not Acceptable"`).

The `type` value may be a single MIME type string (such as “application/json”),
an extension name such as “json”, a comma-delimited list, or an array. For a
list or array, the method returns the *best* match (if any).

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

#### Arguments

`charset`
One or more character sets to test against the request’s `Accept-Charset` header.

Returns the first accepted charset of the specified character sets,
based on the request’s `Accept-Charset` HTTP header field.
If none of the specified charsets is accepted, returns `false`.

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

#### Arguments

`charset`
One or more character sets to test against the request’s `Accept-Charset` header.

### Caution

`req.acceptsCharset()` is the singular alias of [`req.acceptsCharsets()`](https://expressjs.com#reqacceptscharsets) and behaves identically. It has emitted a deprecation warning since Express v4.5.0. Use `req.acceptsCharsets()` instead.

You can update your code automatically with the following codemod:

#### Arguments

`encoding`
One or more encodings to test against the request’s `Accept-Encoding` header.

Returns the first accepted encoding of the specified encodings,
based on the request’s `Accept-Encoding` HTTP header field.
If none of the specified encodings is accepted, returns `false`.

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

#### Arguments

`encoding`
One or more encodings to test against the request’s `Accept-Encoding` header.

### Caution

`req.acceptsEncoding()` is the singular alias of [`req.acceptsEncodings()`](https://expressjs.com#reqacceptsencodings) and behaves identically. It has emitted a deprecation warning since Express v4.5.0. Use `req.acceptsEncodings()` instead.

You can update your code automatically with the following codemod:

#### Arguments

`lang`
One or more languages to test against the request’s `Accept-Language` header. If omitted, all
accepted languages are returned as an array.

Returns the first accepted language of the specified languages,
based on the request’s `Accept-Language` HTTP header field.
If none of the specified languages is accepted, returns `false`.

If no `lang` argument is given, then `req.acceptsLanguages()`
returns all languages from the HTTP `Accept-Language` header
as an `Array`.

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

#### Arguments

`lang`
One or more languages to test against the request’s `Accept-Language` header. If omitted, all
accepted languages are returned as an array.

### Caution

`req.acceptsLanguage()` is the singular alias of [`req.acceptsLanguages()`](https://expressjs.com#reqacceptslanguages) and behaves identically. It has emitted a deprecation warning since Express v4.5.0. Use `req.acceptsLanguages()` instead.

You can update your code automatically with the following codemod:

Express (4.x) source: [request.js line 179](https://github.com/expressjs/express/blob/4.x/lib/request.js#L179)

Accepts (1.3) source: [index.js line 195](https://github.com/jshttp/accepts/blob/f69c19e459bd501e59fb0b1a40b7471bb578113a/index.js#L195)

#### Arguments

`field`
The name of the HTTP request header to read (case-insensitive). `Referrer` and `Referer` are
interchangeable.

Returns the specified HTTP request header field (case-insensitive match).
The `Referrer` and `Referer` fields are interchangeable.

Aliased as `req.header(field)`.

#### Arguments

`type`
The MIME type(s) or extension name(s) to match against the request’s `Content-Type` header.

Returns the matching content type if the incoming request’s “Content-Type” HTTP header field
matches the MIME type specified by the `type` parameter. If the request has no body, returns `null`.
Returns `false` otherwise.

For more information, or if you have issues or concerns, see [type-is](https://github.com/expressjs/type-is).

#### Arguments

`name`
The name of the parameter to look up, searched in `req.params`, then `req.body`, then
`req.query`.

`defaultValue`
A value to return when the parameter is not found in any of the request objects.

### Caution

Deprecated. Use either `req.params`, `req.body` or `req.query`, as applicable.

Returns the value of param `name` when present.

Lookup is performed in the following order:

- `req.params`
- `req.body`
- `req.query`

Optionally, you can specify `defaultValue` to set a default value if the parameter is not found in any of the request objects.

### Warning

Direct access to `req.body`, `req.params`, and `req.query` should be favoured for clarity - unless you truly accept input from each object.

Body-parsing middleware must be loaded for `req.param()` to work predictably. Refer [req.body](https://expressjs.com#reqbody) for details.

#### Arguments

`size`
The maximum size of the resource.

`options`
Options for parsing the `Range` header.

`combine`
Specify if overlapping and adjacent ranges should be combined. When `true`, ranges are
combined and returned as if they were specified that way in the header.

`Range` header parser.

An array of ranges will be returned or negative numbers indicating an error parsing.

- `-2` signals a malformed header string
- `-1` signals an unsatisfiable range