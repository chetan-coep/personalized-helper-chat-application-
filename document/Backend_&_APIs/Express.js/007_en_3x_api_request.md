---
id: "express.js_007"
technology: "Express.js"
category: "Backend & APIs"
title: "Request · Express.js 3.x"
doc_order: 7
source_url: "https://expressjs.com/en/3x/api/request"
language: "en"
retrieved_at: "2026-11-03 17:40:07"
content_hash: "3546d07395b819761a0fd464119361b7740c022f2331b5fbbb47ced3a81112ff"
---

# Request · Express.js 3.x

Source: https://expressjs.com/en/3x/api/request

---

The `req` object is an enhanced version of Node’s own request object
and supports all [built-in fields and methods](https://nodejs.org/api/http.html#class-httpincomingmessage).

The `req` object contains a number of properties that provide information about the HTTP request, such as headers, query parameters, and more.

Return an array of Accepted media types ordered from highest quality to lowest.

Return an array of Accepted charsets ordered from highest quality to lowest.

Return an array of Accepted languages ordered from highest quality to lowest.

This property is an object containing the parsed request body. This feature
is provided by the `bodyParser()` middleware, though other body
parsing middleware may follow this convention as well. This property
defaults to `{}` when `bodyParser()` is used.

This object requires the `cookieParser()` middleware for use.
It contains cookies sent by the user-agent. If no cookies are sent, it
defaults to `{}`.

This property is an object of the files uploaded. This feature
is provided by the `bodyParser()` middleware, though other body
parsing middleware may follow this convention as well. This property
defaults to `{}` when `bodyParser()` is used.

For example if a **file** field was named “image”,
and a file was uploaded, `req.files.image` would contain
the following `File` object:

The `bodyParser()` middleware utilizes the

[node-formidable](https://github.com/felixge/node-formidable)
module internally, and accepts the same options. An example of this is the `keepExtensions`
formidable option, defaulting to **false**
which in this case gives you the filename “/tmp/8ef9c52abe857867fd0a4e9a819d1876” void of the “.png”
extension. To enable this, and others you may pass them to `bodyParser()`:

Check if the request is fresh - aka Last-Modified and/or the ETag still match, indicating that the resource is “fresh”.

Returns the hostname from the “Host” header field (void of port number).

Return the remote address, or when “trust proxy” is enabled - the upstream address.

When “trust proxy” is `true`, parse
the “X-Forwarded-For” ip address list
and return an array, otherwise an empty
array is returned.

For example if the value were “client, proxy1, proxy2”
you would receive the array `["client", "proxy1", "proxy2"]`
where “proxy2” is the furthest down-stream.

This property is much like `req.url`, however it retains
the original request url, allowing you to rewrite `req.url`
freely for internal routing purposes. For example the “mounting” feature
of [app.use()](https://expressjs.com/en/3x/api/application/#appusepath-function) will rewrite `req.url` to
strip the mount point.

This property is an array containing properties mapped to the named route “parameters”.
For example if you have the route `/user/:name`, then the “name” property
is available to you as `req.params.name`. This object defaults to `{}`.

When a regular expression is used for the route definition, capture groups
are provided in the array using `req.params[N]`, where `N`
is the nth capture group. This rule is applied to unnamed wild-card matches
with string routes such as `/file/*`:

Returns the request URL pathname.

Return the protocol string “http” or “https” when requested with TLS. When the “trust proxy” setting is enabled the “X-Forwarded-Proto” header field will be trusted. If you’re running behind a reverse proxy that supplies https for you this may be enabled.

This property is an object containing the parsed query-string,
defaulting to `{}`.

This property holds a reference to the [response object](https://expressjs.com/en/3x/api/response/)
that relates to this request object.

The currently matched `Route` containing
several properties such as the route’s original path
string, the regexp generated, and so on.

Example output from the previous snippet:

Check if a TLS connection is established. This is a short-hand for:

This object requires the `cookieParser(secret)` middleware for use.
It contains signed cookies sent by the user-agent, unsigned and ready for use.
Signed cookies reside in a different object to show developer intent; otherwise,
a malicious attack could be placed on `req.cookie` values (which are easy to spoof).
Note that signing a cookie does not make it “hidden” or encrypted; this simply
prevents tampering (because the secret used to sign is private). If no signed
cookies are sent, it defaults to `{}`.

Check if the request is stale - aka Last-Modified and/or the ETag do not match, indicating that the resource is “stale”.

Return subdomains as an array.

Check if the request was issued with the “X-Requested-With” header field set to “XMLHttpRequest” (jQuery etc).

The `req` object also contains a number of methods that can be used to perform various tasks related to the HTTP request, such as checking the content type, retrieving header values, and more.

Check if the given `types` are acceptable, returning
the best match when true, otherwise `undefined` - in which
case you should respond with 406 “Not Acceptable”.

The `type` value may be a single mime type string
such as “application/json”, the extension name
such as “json”, a comma-delimited list or an array. When a list
or array is given the best match, if any is returned.

Check if the given `charset` are acceptable.

Check if the given `lang` are acceptable.

Get the case-insensitive request header `field`. The “Referrer” and “Referer” fields are interchangeable.

Aliased as `req.header(field)`.

Check if the incoming request contains the “Content-Type”
header field, and it matches the give mime `type`.

Return the value of param `name` when present.

Lookup is performed in the following order:

- `req.params`
- `req.body`
- `req.query`

Direct access to `req.body`, `req.params`,
and `req.query` should be favoured for clarity - unless
you truly accept input from each object.