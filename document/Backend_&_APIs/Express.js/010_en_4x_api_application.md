---
id: "express.js_010"
technology: "Express.js"
category: "Backend & APIs"
title: "Application Object · Express.js 4.x"
doc_order: 10
source_url: "https://expressjs.com/en/4x/api/application"
language: "en"
retrieved_at: "2026-11-03 17:40:15"
content_hash: "7651e7757f1bc9f14fa7c10af9ccbfc2f13ca16072669ac7369f044f980f96a5"
---

# Application Object · Express.js 4.x

Source: https://expressjs.com/en/4x/api/application

---

The `app` object conventionally denotes the Express application.
Create it by calling the top-level `express()` function exported by the Express module:

The `app` object has methods for

- Routing HTTP requests; see for example, [app.METHOD](https://expressjs.com#appmethod) and [app.param](https://expressjs.com#appparam).
- Configuring middleware; see [app.route](https://expressjs.com#approute).
- Rendering HTML views; see [app.render](https://expressjs.com#apprender).
- Registering a template engine; see [app.engine](https://expressjs.com#appengine).

It also has settings (properties) that affect how the application behaves;
for more information, see [Application Settings](https://expressjs.com#application-settings).

### Note

The `app.locals` object has properties that are local variables within the application,
and will be available in templates rendered with [res.render](https://expressjs.com/en/4x/api/response/#resrender).

### Warning

The `locals` object is used by view engines to render a response. The object keys may be
particularly sensitive and should not contain user-controlled input, as it may affect the
operation of the view engine or provide a path to cross-site scripting. Consult the documentation
for the used view engine for additional considerations.

Once set, the value of `app.locals` properties persist throughout the life of the application,
in contrast with [res.locals](https://expressjs.com/en/4x/api/response/#reslocals) properties that
are valid only for the lifetime of the request.

You can access local variables in templates rendered within the application.
This is useful for providing helper functions to templates, as well as application-level data.
Local variables are available in middleware via `req.app.locals` (see [req.app](https://expressjs.com/en/4x/api/request/#reqapp))

The `app.mountpath` property contains one or more path patterns on which a sub-app was mounted.

### Note

A sub-app is an instance of `express` that may be used for handling the request to a route.

It is similar to the [baseUrl](https://expressjs.com/en/4x/api/request/#reqbaseurl) property of the `req` object, except `req.baseUrl`
returns the matched URL path, instead of the matched patterns.

If a sub-app is mounted on multiple path patterns, `app.mountpath` returns the list of
patterns it is mounted on, as shown in the following example.

#### Arguments

`callback`
The listener called when the `mount` event fires. It receives the parent app as its only
argument: `callback(parent)`.

The `mount` event is fired on a sub-app, when it is mounted on a parent app. The parent app is passed to the callback function.

### Note

Sub-apps will:

- Not inherit the value of settings that have a default value. You must set the value in the sub-app.
- Inherit the value of settings with no default value.

For details, see [Application settings](https://expressjs.com#application-settings).

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

This method is like the standard [app.METHOD()](https://expressjs.com#appmethod) methods,
except it matches all HTTP verbs.

The following callback is executed for requests to `/secret` whether using
GET, POST, PUT, DELETE, or any other HTTP request method:

The `app.all()` method is useful for mapping “global” logic for specific path prefixes or arbitrary matches. For example, if you put the following at the top of all other
route definitions, it requires that all routes from that point on
require authentication, and automatically load a user. Keep in mind
that these callbacks do not have to act as end-points: `loadUser`
can perform a task, then call `next()` to continue matching subsequent
routes.

Or the equivalent:

Another example is white-listed “global” functionality. The example is similar to the ones above, but it only restricts paths that start with “/api”:

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Routes HTTP DELETE requests to the specified path with the specified callback functions.
For more information, see the [routing guide](https://expressjs.com/en/4x/guide/routing/).

### Caution

`app.del()` is the alias of [`app.delete()`](https://expressjs.com#appdelete), originally introduced because `delete` was a reserved word in older JavaScript engines. It has emitted a deprecation warning since Express v4.2.0. Use `app.delete()` instead.

You can update your code automatically with the following codemod:

Sets the Boolean setting `name` to `false`, where `name` is one of the properties from the [app settings table](https://expressjs.com#application-settings).
Calling `app.set('foo', false)` for a Boolean property is the same as calling `app.disable('foo')`.

For example:

Returns `true` if the Boolean setting `name` is disabled (`false`), where `name` is one of the properties from
the [app settings table](https://expressjs.com#application-settings).

Sets the Boolean setting `name` to `true`, where `name` is one of the properties from the [app settings table](https://expressjs.com#application-settings).
Calling `app.set('foo', true)` for a Boolean property is the same as calling `app.enable('foo')`.

Returns `true` if the setting `name` is enabled (`true`), where `name` is one of the
properties from the [app settings table](https://expressjs.com#application-settings).

#### Arguments

`ext`
The file extension the template engine is registered for (for example, `pug` or `html`).

`callback`
The template engine function used to render files with the given extension.

Registers the given template engine `callback` as `ext`.

By default, Express will `require()` the engine based on the file extension.
For example, if you try to render a “foo.pug” file, Express invokes the
following internally, and caches the `require()` on subsequent calls to increase
performance.

Use this method for engines that do not provide `.__express` out of the box,
or if you wish to “map” a different extension to the template engine.

For example, to map the EJS template engine to “.html” files:

In this case, EJS provides a `.renderFile()` method with
the same signature that Express expects: `(path, options, callback)`,
though note that it aliases this method as `ejs.__express` internally
so if you’re using “.ejs” extensions you don’t need to do anything.

Some template engines do not follow this convention. The
[consolidate.js](https://github.com/tj/consolidate.js) library maps Node template engines to follow this convention,
so they work seamlessly with Express.

Returns the value of `name` app setting, where `name` is one of the strings in the
[app settings table](https://expressjs.com#application-settings). For example:

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Routes HTTP GET requests to the specified path with the specified callback functions.

For more information, see the [routing guide](https://expressjs.com/en/4x/guide/routing/).

#### Arguments

`port`
The TCP port to listen on. If omitted or `0`, the OS assigns an arbitrary unused port.

`host`
The host on which to accept connections.

`backlog`
The maximum length of the queue of pending connections.

`path`
The path of a UNIX socket to listen on, as an alternative to host and port.

`callback`
A function to call once the server is listening.

Binds and listens for connections on the specified host and port, or starts a
UNIX socket and listens for connections on the given path. This method is
identical to Node’s [http.Server.listen()](https://nodejs.org/api/http.html#serverlisten).

If port is omitted or is 0, the operating system will assign an arbitrary unused port, which is useful for cases like automated tasks (tests, etc.).

The `app` returned by `express()` is in fact a JavaScript
`Function`, designed to be passed to Node’s HTTP servers as a callback
to handle requests. This makes it easy to provide both HTTP and HTTPS versions of
your app with the same code base, as the app does not inherit from these
(it is simply a callback):

The `app.listen()` method returns an [http.Server](https://nodejs.org/api/http.html#class-httpserver) object and (for HTTP) is a convenience method for the following:

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Routes an HTTP request, where METHOD is the HTTP method of the request, such as GET,
PUT, POST, and so on, in lowercase. Thus, the actual methods are `app.get()`,
`app.post()`, `app.put()`, and so on. See [Routing methods](https://expressjs.com#routing-methods) below for the complete list.

String route patterns match the whole request path. For example, `app.get('/apple', ...)` matches
`/apple`, but not `/apple/images`. With the same path, [app.use()](https://expressjs.com#appuse) matches both.

Regular expressions can match part of the path. `app.get(/apple/, ...)` matches `/apple/images`.
Use `^` and `$` for a full match: `app.get(/^\/apple$/, ...)` matches only `/apple`.

Express supports the following routing methods corresponding to the HTTP methods of the same names:

The API documentation has explicit entries only for the most popular HTTP methods `app.get()`,
`app.post()`, `app.put()`, `app.delete()`, and `app.query()`.
However, the other methods listed above work in exactly the same way.

To route methods that translate to invalid JavaScript variable names, use the bracket notation. For example, `app['m-search']('/', function ...`.

### Note

The `app.get()` function is automatically called for the HTTP `HEAD` method in addition to the
`GET` method if `app.head()` was not called for the path before `app.get()`.

The method, `app.all()`, is not derived from any HTTP method and loads middleware at
the specified path for *all* HTTP request methods.
For more information, see [app.all](https://expressjs.com#appall).

For more information on routing, see the [routing guide](https://expressjs.com/en/4x/guide/routing/).

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Routes HTTP QUERY requests to the specified path with the specified callback functions.
For more information, see the [routing guide](https://expressjs.com/en/4x/guide/routing/).

### Caution

The HTTP QUERY method was standardized on June 15, 2026 as [RFC 10008](https://www.rfc-editor.org/rfc/rfc10008.html).
Client and intermediary support is still limited. Verify that your target environments support the QUERY verb before relying on it in production.

The HTTP QUERY method ([RFC 10008](https://www.rfc-editor.org/rfc/rfc10008.html)) is designed for
queries whose input is too large or too sensitive to encode in the URL. Unlike `GET`, a QUERY
request carries a body containing the query input. Unlike `POST`, it is explicitly **safe and
idempotent**, intermediaries and caches can retry it automatically, and the response is cacheable
(with the request body included in the cache key).

Use `app.query()` when query parameters would exceed URL length limits, contain sensitive data that
should not appear in server logs or browser history, or are too complex to express cleanly as a URL
query string, such as deeply nested filters or structured criteria.

Because the query input travels in the request body, `req.body` is `undefined` until you mount a
body-parsing middleware such as [`express.json()`](https://expressjs.com/en/4x/api/express/#expressjson) or
[`express.urlencoded()`](https://expressjs.com/en/4x/api/express/#expressurlencoded) that matches the request’s `Content-Type`.

#### Arguments

`name`
The name of the route parameter, or an array of names.

`callback`
The trigger called as `callback(req, res, next, value, name)`: the request object, the
response object, the next middleware, the value of the parameter, and the name of the
parameter, in that order.

Add callback triggers to [route parameters](https://expressjs.com/en/4x/guide/routing/#route-parameters), where `name` is the name of the parameter or an array of them, and `callback` is the callback function. The parameters of the callback function are the request object, the response object, the next middleware, the value of the parameter and the name of the parameter, in that order.

If `name` is an array, the `callback` trigger is registered for each parameter declared in it, in the order in which they are declared. Furthermore, for each declared parameter except the last one, a call to `next` inside the callback will call the callback for the next declared parameter. For the last parameter, a call to `next` will call the next middleware in place for the route currently being processed, just like it would if `name` were just a string.

For example, when `:user` is present in a route path, you may map user loading logic to automatically provide `req.user` to the route, or perform validations on the parameter input.

Param callback functions are local to the router on which they are defined. They are not inherited by mounted apps or routers, nor are they triggered for route parameters inherited from parent routers. Hence, param callbacks defined on `app` will be triggered only by route parameters defined on `app` routes.

All param callbacks will be called before any handler of any route in which the param occurs, and they will each be called only once in a request-response cycle, even if the parameter is matched in multiple routes, as shown in the following examples.

On `GET /user/42`, the following is printed:

On `GET /user/42/3`, the following is printed:

### Caution

The following section describes `app.param(callback)`, which is deprecated as of v4.11.0.

The behavior of the `app.param(name, callback)` method can be altered entirely by passing only a function to `app.param()`. This function is a custom implementation of how `app.param(name, callback)` should behave - it accepts two parameters and must return a middleware.

The first parameter of this function is the name of the URL parameter that should be captured, the second parameter can be any JavaScript object which might be used for returning the middleware implementation.

The middleware returned by the function decides the behavior of what happens when a URL parameter is captured.

In this example, the `app.param(name, callback)` signature is modified to `app.param(name, accessId)`. Instead of accepting a name and a callback, `app.param()` will now accept a name and a number.

In this example, the `app.param(name, callback)` signature remains the same, but instead of a middleware callback, a custom data type checking function has been defined to validate the data type of the user id.

### Note

The ‘`.`’ character can’t be used to capture a character in your capturing regexp. For example you can’t use `'/user-.+/'` to capture `'users-gami'`, use `[\s\S]` or `[\w\W]` instead (as in `'/user-[\s\S]+/'`.

Examples:

Returns the canonical path of the app, a string.

The behavior of this method can become very complicated in complex cases of mounted apps:
it is usually better to use [req.baseUrl](https://expressjs.com/en/4x/api/request/#reqbaseurl) to get the canonical path of the app.

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Routes HTTP POST requests to the specified path with the specified callback functions.
For more information, see the [routing guide](https://expressjs.com/en/4x/guide/routing/).

#### Arguments

`path``callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Routes HTTP PUT requests to the specified path with the specified callback functions.

#### Arguments

`view`
The name of the view to render.

`locals`
An object whose properties define local variables for the view.

`callback`
The callback invoked as `callback(err, html)` with the rendered HTML.

Returns the rendered HTML of a view via the `callback` function. It accepts an optional parameter
that is an object containing local variables for the view. It is like [res.render()](https://expressjs.com/en/4x/api/response/#resrender),
except it cannot send the rendered view to the client on its own.

### Note

Think of `app.render()` as a utility function for generating rendered view strings. Internally
`res.render()` uses `app.render()` to render views.

### Warning

The `view` argument performs file system operations like reading a file from disk and evaluating
Node.js modules, and as so for security reasons should not contain input from the end-user.

### Warning

The `locals` object is used by view engines to render a response. The object keys may be
particularly sensitive and should not contain user-controlled input, as it may affect the
operation of the view engine or provide a path to cross-site scripting. Consult the documentation
for the used view engine for additional considerations.

### Caution

The local variable `cache` is reserved for enabling view cache. Set it to `true`, if you want to
cache view during development; view caching is enabled in production by default.

#### Arguments

`path`
The path of the route to create.

Returns an instance of a single route, which you can then use to handle HTTP verbs with optional middleware.
Use `app.route()` to avoid duplicate route names (and thus typo errors).

Assigns setting `name` to `value`. You may store any value that you want,
but certain names can be used to configure the behavior of the server. These
special names are listed in the [app settings table](https://expressjs.com#application-settings).

Calling `app.set('foo', true)` for a Boolean property is the same as calling
`app.enable('foo')`. Similarly, calling `app.set('foo', false)` for a Boolean
property is the same as calling `app.disable('foo')`.

Retrieve the value of a setting with [`app.get()`](https://expressjs.com#appgetname).

The following table lists application settings.

### Note

Sub-apps will:

- Not inherit the value of settings that have a default value. You must set the value in the sub-app.
- Inherit the value of settings with no default value; these are explicitly noted in the table below.

Exceptions: Sub-apps will inherit the value of `trust proxy` even though it has a default value (for backward-compatibility);
Sub-apps will not inherit the value of `view cache` in production (when `NODE_ENV` is “production”).

#### Settings

`case sensitive routing`
Enable case sensitivity. When enabled, “/Foo” and “/foo” are different routes. When disabled, “/Foo” and “/foo” are treated the same.

### Note

Sub-apps will inherit the value of this setting.

`env``etag``jsonp callback name`
Specifies the default JSONP callback name.

`json escape`
Enable escaping JSON responses from the `res.json`, `res.jsonp`, and `res.send` APIs. This will escape the characters `<`, `>`, and `&` as Unicode escape sequences in JSON. The purpose of this is to assist with [mitigating certain types of persistent XSS attacks](https://blog.mozilla.org/security/2017/07/18/web-service-audits-firefox-accounts/) when clients sniff responses for HTML.

### Note

Sub-apps will inherit the value of this setting.

`json replacer``json spaces``query parser`
Disable query parsing by setting the value to `false`, or set the query parser to use either “simple” or “extended” or a custom query string parsing function. The simple query parser is based on Node’s native query parser, [querystring](https://nodejs.org/api/querystring.html). The extended query parser is based on [qs](https://www.npmjs.com/package/qs). A custom query string parsing function will receive the complete query string, and must return an object of query keys and their values.

`strict routing`
Enable strict routing. When enabled, the router treats “/foo” and “/foo/” as different. Otherwise, the router treats “/foo” and “/foo/” as the same.

### Note

Sub-apps will inherit the value of this setting.

`subdomain offset`
The number of dot-separated parts of the host to remove to access subdomain.

`trust proxy`
Indicates the app is behind a front-facing proxy, and to use the `X-Forwarded-*` headers to determine the connection and the IP address of the client.

### Note

`X-Forwarded-*` headers are easily spoofed and the detected IP addresses are unreliable.

When enabled, Express attempts to determine the IP address of the client connected through the front-facing proxy, or series of proxies. The `req.ips` property, then contains an array of IP addresses the client is connected through. To enable it, use the values described in the trust proxy options table below. The `trust proxy` setting is implemented using the [proxy-addr](https://www.npmjs.com/package/proxy-addr) package. For more information, see its documentation.

### Note

Sub-apps *will* inherit the value of this setting, even though it has a default value.

`views`
A directory or an array of directories for the application’s views. If an array, the views are looked up in the order they occur in the array.

`view cache`
Enables view template compilation caching.

### Note

Sub-apps will not inherit the value of this setting in production (when `NODE_ENV` is “production”).

`view engine`
The default engine extension to use when omitted.

### Note

Sub-apps will inherit the value of this setting.

`x-powered-by`
Enables the “X-Powered-By: Express” HTTP header.

Read [Express behind proxies](https://expressjs.com/en/4x/guide/behind-proxies/) for more information.

**Boolean**: If `true`, the client’s IP address is understood as the left-most entry in the `X-Forwarded-*` header. If `false`, the app is understood as directly facing the Internet and the client’s IP address is derived from `req.connection.remoteAddress`. This is the default setting.

**String / String containing comma-separated values / Array of strings**: An IP address, subnet, or an array of IP addresses, and subnets to trust. Pre-configured subnet names are:

- loopback - `127.0.0.1/8`, `::1/128`
- linklocal - `169.254.0.0/16`, `fe80::/10`
- uniquelocal - `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `fc00::/7`

Set IP addresses in any of the following ways:

Specify a single subnet:

Specify a subnet and an address:

Specify multiple subnets as CSV:

Specify multiple subnets as an array:

When specified, the IP addresses or the subnets are excluded from the address determination process, and the untrusted IP address nearest to the application server is determined as the client’s IP address.

**Number**: Trust the *n*th hop from the front-facing proxy server as the client.

**Function**: Custom trust implementation. Use this only if you know what you are doing.

### Note

These settings apply only to dynamic files, not static files. The `express.static` middleware ignores these settings.

The ETag functionality is implemented using the [etag](https://www.npmjs.com/package/etag) package. For more information, see its documentation.

#### Values

`Boolean`
`true` enables weak ETag. This is the default setting. `false` disables ETag altogether.

`String``Function`
Custom ETag function implementation. Use this only if you know what you are doing.

#### Arguments

`path`
The path for which the middleware function is invoked; can be any of: a string representing a
path, a path pattern, a regular expression pattern to match paths, or an array of combinations
of any of the above. For examples, see [Path examples](https://expressjs.com#path-examples).

`callback`
Callback functions; can be: a middleware function, a series of middleware functions (separated
by commas), an array of middleware functions, or a combination of all of the above. You can
provide multiple callback functions that behave just like middleware, except that these
callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use
this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if
there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api/router/) and
[app](https://expressjs.com/en/4x/api/application/) implement the middleware interface, you can use them as you would any
other middleware function. For examples, see [Middleware callback function
examples](https://expressjs.com#middleware-callback-function-examples).

Mounts the specified [middleware](https://expressjs.com/en/4x/guide/using-middleware/) function or functions
at the specified path:
the middleware function is executed when the base of the requested path matches `path`.

With a string path, `app.use()` matches that path and its subpaths. For example,
`app.use('/apple', ...)` matches `/apple`, `/apple/images`, and `/apple/images/news`,
but not `/apples`.

Since `path` defaults to ”/”, middleware mounted without a path will be executed for every request to the app.
For example, this middleware function will be executed for *every* request to the app:

### Note

Sub-apps will:

- Not inherit the value of settings that have a default value. You must set the value in the sub-app.
- Inherit the value of settings with no default value.

For details, see [Application settings](https://expressjs.com#application-settings).

Middleware functions are executed sequentially, therefore the order of middleware inclusion is important.

**Error-handling middleware**

Error-handling middleware always takes *four* arguments. You must provide four arguments to identify it as an error-handling middleware function. Even if you don’t need to use the `next` object, you must specify it to maintain the signature. Otherwise, the `next` object will be interpreted as regular middleware and will fail to handle errors. For details about error-handling middleware, see: [Error handling](https://expressjs.com/en/4x/guide/error-handling/).

Define error-handling middleware functions in the same way as other middleware functions, except with four arguments instead of three, specifically with the signature `(err, req, res, next)`):

The following table provides some simple examples of valid `path` values for
mounting middleware.

**Path**: Matches the exact path `/abcd` and any sub-paths starting with `/abcd/` (for example, `/abcd/foo`):

**Path Pattern**: This will match paths starting with `/abcd` and `/abd`:

This will match paths starting with `/abcd`, `/abbcd`, `/abbbbbcd`, and so on:

This will match paths starting with `/abcd`, `/abxcd`, `/abFOOcd`, `/abbArcd`, and so on:

This will match paths starting with `/ad` and `/abcd`:

**Regular Expression**: This will match paths starting with `/abc` and `/xyz`:

**Array**: This will match paths starting with `/abcd`, `/xyza`, `/lmn`, and `/pqr`:

The following table provides some simple examples of middleware functions that
can be used as the `callback` argument to `app.use()`, `app.METHOD()`, and `app.all()`.

**Single Middleware**: You can define and mount a middleware function locally.

A router is valid middleware.

An Express app is valid middleware.

**Series of Middleware**: You can specify more than one middleware function at the same mount path.

**Array**: Use an array to group middleware logically.

**Combination**: You can combine all the above ways of mounting middleware.

Following are some examples of using the [express.static](https://expressjs.com/en/4x/guide/using-middleware/#built-in-middleware)
middleware in an Express app.

Serve static content for the app from the “public” directory in the application directory:

Mount the middleware at “/static” to serve static content only when their request path is prefixed with “/static”:

Disable logging for static content requests by loading the logger middleware after the static middleware:

Serve static files from multiple directories, but give precedence to ”./public” over the others: