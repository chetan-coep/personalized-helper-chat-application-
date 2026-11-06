---
id: "express.js_014"
technology: "Express.js"
category: "Backend & APIs"
title: "Router · Express.js 4.x"
doc_order: 14
source_url: "https://expressjs.com/en/4x/api/router"
language: "en"
retrieved_at: "2026-11-03 17:40:20"
content_hash: "5808cc59dcbfab980b4d84ca013e9e6c7f2dfca91a088c80199c190f05fb1350"
---

# Router · Express.js 4.x

Source: https://expressjs.com/en/4x/api/router

---

A router object is an instance of middleware and routes. You can think of it
as a “mini-application,” capable only of performing middleware and routing
functions. Every Express application has a built-in app router.

A router behaves like middleware itself, so you can use it as an argument to
app.use() or as the argument to another router’s use() method.

The top-level express object has a Router() method that creates a new router object.

Once you’ve created a router object, you can add middleware and HTTP method routes (such as get, put, post,
and so on) to it just like an application. For example:

You can then use a router for a particular root URL in this way separating your routes into files or even mini-apps.

The path for which the route callbacks are invoked.

callback

Type:Function | Function\[\]

One or more middleware/handler functions. Each may call next('route') to skip the remaining
callbacks.

This method is just like the router.METHOD() methods, except that it matches all HTTP methods (verbs).

This method is extremely useful for
mapping “global” logic for specific path prefixes or arbitrary matches.
For example, if you placed the following route at the top of all other
route definitions, it would require that all routes from that point on
would require authentication, and automatically load a user. Keep in mind
that these callbacks do not have to act as end points; loadUser
can perform a task, then call next() to continue matching subsequent
routes.

Or the equivalent:

Another example of this is white-listed “global” functionality. Here
the example is much like before, but it only restricts paths prefixed with
“/api”:

The path for which the route callbacks are invoked.

callback

Type:Function | Function\[\]

One or more middleware/handler functions. Each may call next('route') to skip the remaining
callbacks.

The router.METHOD() methods provide the routing functionality in Express,
where METHOD is one of the HTTP methods, such as GET, PUT, POST, and so on,
in lowercase. Thus, the actual methods are router.get(), router.post(),
router.put(), and so on.

Note

The router.get() function is automatically called for the HTTP HEAD method in addition to the
GET method if router.head() was not called for the path before router.get().

Note

router.query() routes HTTP QUERY requests, mirroring app.query(). The QUERY method is gated by the runtime and requires Node.js >=20.19.3 \<21 || >=22.2.0.

You can provide multiple callbacks, and all are treated equally, and behave just
like middleware, except that these callbacks may invoke next('route')
to bypass the remaining route callback(s). You can use this mechanism to perform
pre-conditions on a route then pass control to subsequent routes when there is no
reason to proceed with the route matched.

The following snippet illustrates the most simple route definition possible.
Express translates the path strings to regular expressions, used internally
to match incoming requests. Query strings are not considered when performing
these matches, for example “GET /” would match the following route, as would
“GET /?name=tobi”.

You can also use regular expressions—useful if you have very specific
constraints, for example the following would match “GET /commits/71dbb9c” as well
as “GET /commits/71dbb9c..4c084f9”.

The name of the route parameter to attach the trigger to. Unlike app.param(), this does not
accept an array.

callback

Type:Function

The trigger called as callback(req, res, next, value, name).

Adds callback triggers to route parameters, where name is the name of the parameter and callback is the callback function. Although name is technically optional, using this method without it is deprecated starting with Express v4.11.0 (see below).

The parameters of the callback function are:

req, the request object.

res, the response object.

next, indicating the next middleware function.

The value of the name parameter.

The name of the parameter.

Note

Unlike app.param(), router.param() does not accept an array of route parameters.

For example, when :user is present in a route path, you may map user loading logic to automatically provide req.user to the route, or perform validations on the parameter input.

Param callback functions are local to the router on which they are defined. They are not inherited by mounted apps or routers, nor are they triggered for route parameters inherited from parent routers. Hence, param callbacks defined on router will be triggered only by route parameters defined on router routes.

A param callback will be called only once in a request-response cycle, even if the parameter is matched in multiple routes, as shown in the following examples.

On GET /user/42, the following is printed:

Caution

The following section describes router.param(callback), which is deprecated as of v4.11.0.

The behavior of the router.param(name, callback) method can be altered entirely by passing only a function to router.param(). This function is a custom implementation of how router.param(name, callback) should behave - it accepts two parameters and must return a middleware.

The first parameter of this function is the name of the URL parameter that should be captured, the second parameter can be any JavaScript object which might be used for returning the middleware implementation.

The middleware returned by the function decides the behavior of what happens when a URL parameter is captured.

In this example, the router.param(name, callback) signature is modified to router.param(name, accessId). Instead of accepting a name and a callback, router.param() will now accept a name and a number.

In this example, the router.param(name, callback) signature remains the same, but instead of a middleware callback, a custom data type checking function has been defined to validate the data type of the user id.

Returns an instance of a single route which you can then use to handle HTTP verbs
with optional middleware. Use router.route() to avoid duplicate route naming and
thus typing errors.

Building on the router.param() example above, the following code shows how to use
router.route() to specify various HTTP method handlers.

This approach re-uses the single /users/:user\_id path and adds handlers for
various HTTP methods.

Note

When you use router.route(), middleware ordering is based on when the route is created, not
when method handlers are added to the route. For this purpose, you can consider method handlers to
belong to the route to which they were added.

Uses the specified middleware function or functions, with optional mount path path, that defaults to ”/”.

This method is similar to app.use(). A simple example and use case is described below.
See app.use() for more information.

Middleware is like a plumbing pipe: requests start at the first middleware function defined
and work their way “down” the middleware stack processing for each path they match.

The “mount” path is stripped and is not visible to the middleware function.
The main effect of this feature is that a mounted middleware function may operate without
code changes regardless of its “prefix” pathname.

The order in which you define middleware with router.use() is very important.
They are invoked sequentially, thus the order defines middleware precedence. For example,
usually a logger is the very first middleware you would use, so that every request gets logged.

Now suppose you wanted to ignore logging requests for static files, but to continue
logging routes and middleware defined after logger(). You would simply move the call to express.static() to the top,
before adding the logger middleware:

Another example is serving files from multiple directories,
giving precedence to ”./public” over the others:

The router.use() method also supports named parameters so that your mount points
for other routers can benefit from preloading using named parameters.

Note

Although these middleware functions are added via a particular router, when
they run is defined by the path they are attached to (not the router). Therefore,
middleware added via one router may run for other routers if its routes
match.

For example, this code shows two different routers mounted on the same path:

Even though the authentication middleware was added via the authRouter it will run on the routes defined by the openRouter as well since both routers were mounted on /users. To avoid this behavior, use different paths for each router.