---
id: "express.js_006"
technology: "Express.js"
category: "Backend & APIs"
title: "Middleware · Express.js 3.x"
doc_order: 6
source_url: "https://expressjs.com/en/3x/api/middleware"
language: "en"
retrieved_at: "2026-11-03 17:40:05"
content_hash: "130e84d07404701e1dee34168c5e6c56131c2559185cc100a2bc0486711bac21"
---

# Middleware · Express.js 3.x

Source: https://expressjs.com/en/3x/api/middleware

---

Express 3.x includes a number of built-in middleware functions that can be used to handle common tasks such as parsing request bodies, handling cookies, and more. These middleware functions are available as properties on the Express module and can be added to your application using `app.use()`.

Basic Authentication middleware, populating `req.user`
with the username.

Simple username and password:

Callback verification:

Async callback verification, accepting `fn(err, user)`,
in this case `req.user` will be the user object passed.

Request body parsing middleware supporting JSON, urlencoded,
and multipart requests. This middleware is simply a wrapper
for the `json()`, `urlencoded()`, and
`multipart()` middleware.

For security sake, it’s better to disable file upload if your application
doesn’t need it. To do this, use only the needed middleware, i.e. don’t use
the `bodyParser` and `multipart()` middleware:

If your application needs file upload you should set up

[a strategy for dealing with those files](https://groups.google.com/d/msg/express-js/iP2VyhkypHo/5AXQiYN3RPcJ)

.

Compress response data with gzip / deflate. This middleware should be placed “high” within the stack to ensure all responses may be compressed.

Parses the Cookie header field and populates `req.cookies`
with an object keyed by the cookie names. Optionally you may enabled
signed cookie support by passing a `secret` string.

Provides cookie-based sessions, and populates `req.session`.
This middleware takes the following options:

- `key` cookie name defaulting to `connect.sess`
- `secret` prevents cookie tampering
- `cookie` session cookie settings, defaulting to `{ path: '/', httpOnly: true, maxAge: null }`
- `proxy` trust the reverse proxy when setting secure cookies (via “x-forwarded-proto”)

To clear a cookie simply assign the session to null before responding:

CSRF protection middleware.

By default this middleware generates a token named “\_csrf”
which should be added to requests which mutate
state, within a hidden form field, query-string etc. This
token is validated against `req.csrfToken()`.

The default `value` function checks `req.body` generated
by the `bodyParser()` middleware, `req.query` generated
by `query()`, and the “X-CSRF-Token” header field.

This middleware requires session support, thus should be added
somewhere below `session()`.

Directory serving middleware, serves the given `path`.
This middleware may be paired with `static()` to serve
files, providing a full-featured file browser.

This middleware accepts the following options:

- `hidden` display hidden (dot) files. Defaults to false.
- `icons` display icons. Defaults to false.
- `filter` Apply this filter function to files. Defaults to false.