---
id: "express.js_005"
technology: "Express.js"
category: "Backend & APIs"
title: "Application Object · Express.js 3.x"
doc_order: 5
source_url: "https://expressjs.com/en/3x/api/application"
language: "en"
retrieved_at: "2026-11-03 17:40:04"
content_hash: "9c3afc220647b5e06f81fcb6a6a0e0e952750e2072efc24d3756e6ab5d5a5079"
---

# Application Object · Express.js 3.x

Source: https://expressjs.com/en/3x/api/application

---

The `app` object conventionally denotes the Express application.
Create it by calling the top-level `express()` function exported by the Express module:

Application local variables are provided to all templates rendered within the application. This is useful for providing helper functions to templates, as well as app-level data.

The `app.locals` object is a JavaScript `Function`,
which when invoked with an object will merge properties into itself, providing
a simple way to expose existing objects as local variables.

A consequence of the `app.locals` Object being ultimately a Javascript Function Object is that you must not reuse existing (native) named properties for your own variable names, such as `name, apply, bind, call, arguments, length, constructor`.

The full list of native named properties can be found in many specifications. The [JavaScript specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) introduced original properties, some of which still recognized by modern engines, and the [EcmaScript specification](https://262.ecma-international.org/5.1/) then built on it and normalized the set of properties, adding new ones and removing deprecated ones. Check out properties for Functions and Objects if interested.

By default Express exposes only a single app-level local variable, `settings`.

The `app.routes` object houses all of the routes defined mapped
by the associated HTTP verb. This object may be used for introspection capabilities,
for example Express uses this internally not only for routing but to provide default

OPTIONS behavior unless `app.options()` is used. Your application or framework may
also remove routes by simply by removing them from this object.

The output of `console.log(app.routes)`:

The following settings are provided to alter how Express will behave:

- `env` Environment mode, defaults to process.env.NODE\_ENV or “development”
- `trust proxy` Enables reverse proxy support, disabled by default
- `jsonp callback name` Changes the default callback name of ?callback=
- `json replacer` JSON replacer callback, null by default
- `json spaces` JSON response spaces for formatting, defaults to 2 in development, 0 in production
- `case sensitive routing` Enable case sensitivity, disabled by default, treating “/Foo” and “/foo” as the same
- `strict routing` Enable strict routing, by default “/foo” and “/foo/” are treated the same by the router
- `view cache` Enables view template compilation caching, enabled in production by default
- `view engine` The default engine extension to use when omitted
- `views` The view directory path, defaulting to “process.cwd() + ‘/views‘“

Assigns setting `name` to `value`.

Get setting `name` value.

Set setting `name` to `true`.

Set setting `name` to `false`.

Check if setting `name` is enabled.

Check if setting `name` is disabled.

Conditionally invoke `callback` when `env` matches `app.get('env')`,
aka `process.env.NODE_ENV`. This method remains for legacy reasons, and is effectively
an `if` statement as illustrated in the following snippets. These functions are *not*
required in order to use `app.set()` and other configuration methods.

Is effectively sugar for:

Use the given middleware `function`, with optional mount `path`,
defaulting to ”/”.

The “mount” path is stripped and is **not** visible
to the middleware `function`. The main effect of this feature is that
mounted middleware may operate without code changes regardless of its “prefix”
pathname.

### Caution

A route will match any path that follows its path immediately with either a “`/`” or a “`.`”. For example: `app.use('/apple', ...)` will match */apple*, */apple/images*, */apple/images/news*, */apple.html*, */apple.html.txt*, and so on.

Here’s a concrete example, take the typical use-case of serving files in ./public
using the `express.static()` middleware:

Say for example you wanted to prefix all static files with “/static”, you could
use the “mounting” feature to support this. Mounted middleware functions are *not*
invoked unless the `req.url` contains this prefix, at which point
it is stripped when the function is invoked. This affects this function only,
subsequent middleware will see `req.url` with “/static” included
unless they are mounted as well.

The order of which middleware are “defined” using `app.use()` is
very important, they are invoked sequentially, thus this defines middleware
precedence. For example usually `express.logger()` is the very
first middleware you would use, logging every request:

Now suppose you wanted to ignore logging requests for static files, but to
continue logging routes and middleware defined after `logger()`,
you would simply move `static()` above:

Another concrete example would be serving files from multiple directories, giving precedence to ”./public” over the others:

Register the given template engine `callback` as `ext`

By default will `require()` the engine based on the
file extension. For example if you try to render
a “foo.jade” file Express will invoke the following internally,
and cache the `require()` on subsequent calls to increase
performance.

For engines that do not provide `.__express` out of the box -
or if you wish to “map” a different extension to the template engine
you may use this method. For example mapping the EJS template engine to
“.html” files:

In this case EJS provides a `.renderFile()` method with
the same signature that Express expects: `(path, options, callback)`,
though note that it aliases this method as `ejs.__express` internally
so if you’re using “.ejs” extensions you don’t need to do anything.

Some template engines do not follow this convention, the

[consolidate.js](https://github.com/visionmedia/consolidate.js)
library was created to map all of node’s popular template engines to follow this convention, thus
allowing them to work seamlessly within Express.

Map logic to route parameters. For example when `:user`
is present in a route path you may map user loading logic to automatically
provide `req.user` to the route, or perform validations
on the parameter input.

The following snippet illustrates how the `callback`
is much like middleware, thus supporting async operations, however
providing the additional value of the parameter, here named as `id`.
An attempt to load the user is then performed, assigning `req.user`,
otherwise passing an error to `next(err)`.

Alternatively you may pass only a `callback`, in which
case you have the opportunity to alter the `app.param()` API.
For example the [express-params](http://github.com/expressjs/express-params)
defines the following callback which allows you to restrict parameters to a given
regular expression.

This example is a bit more advanced, checking if the second argument is a regular expression, returning the callback which acts much like the “user” param example.

The method could now be used to effectively validate parameters, or also parse them to provide capture groups:

The `app.VERB()` methods provide the routing functionality
in Express, where **VERB** is one of the HTTP verbs, such
as `app.post()`. Multiple callbacks may be given, all are treated
equally, and behave just like middleware, with the one exception that
these callbacks may invoke `next('route')` to bypass the
remaining route callback(s). This mechanism can be used to perform pre-conditions
on a route then pass control to subsequent routes when there is no reason to proceed
with the route matched.

The following snippet illustrates the most simple route definition possible. Express
translates the path strings to regular expressions, used internally to match incoming requests.
Query strings are *not* considered when performing these matches, for example “GET /”
would match the following route, as would “GET /?name=tobi”.

Regular expressions may also be used, and can be useful if you have very specific restraints, for example the following would match “GET /commits/71dbb9c” as well as “GET /commits/71dbb9c..4c084f9”.

Several callbacks may also be passed, useful for re-using middleware that load resources, perform validations, etc.

These callbacks may be passed within arrays as well, these arrays are simply flattened when passed:

This method functions just like the `app.VERB()` methods,
however it matches all HTTP verbs.

This method is extremely useful for
mapping “global” logic for specific path prefixes or arbitrary matches.
For example if you placed the following route at the top of all other
route definitions, it would require that all routes from that point on
would require authentication, and automatically load a user. Keep in mind
that these callbacks do not have to act as end points, `loadUser`
can perform a task, then `next()` to continue matching subsequent
routes.

Or the equivalent:

Another great example of this is white-listed “global” functionality. Here the example is much like before, however only restricting paths prefixed with “/api”:

Render a `view` with a callback responding with
the rendered string. This is the app-level variant of `res.render()`,
and otherwise behaves the same way.

Bind and listen for connections on the given host and port,
this method is identical to node’s [http.Server#listen()](https://nodejs.org/api/http.html#serverlisten).

The `app` returned by `express()` is in fact a JavaScript
`Function`, designed to be passed to node’s http servers as a callback
to handle requests. This allows you to provide both HTTP and HTTPS versions of
your app with the same codebase easily, as the app does not inherit from these,
it is simply a callback:

The `app.listen()` method is simply a convenience method defined as,
if you wish to use HTTPS or provide both, use the technique above.