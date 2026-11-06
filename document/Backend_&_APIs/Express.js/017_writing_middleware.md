---
id: "express.js_017"
technology: "Express.js"
category: "Backend & APIs"
title: "Writing and Using Custom Middleware in Express.js"
doc_order: 17
source_url: "https://expressjs.com/en/guide/writing-middleware.html"
language: "en"
retrieved_at: "2026-11-03 20:58:00"
content_hash: "express_custom_middleware_017"
---

# Writing Middleware in Express.js

Source: https://expressjs.com/en/guide/writing-middleware.html

---

## What is Middleware in Express.js

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the `next` middleware function in the application’s request-response cycle.

Middleware functions can:
- Execute any code.
- Make changes to the request and the response objects.
- End the request-response cycle.
- Call the next middleware function in the stack by invoking `next()`.

If the current middleware function does not end the request-response cycle, it MUST call `next()` to pass control to the next middleware function. Otherwise, the request will be left hanging.

---

## How to Create a Custom Logging Middleware

Here is a complete, copy-pasteable example of creating a custom request logging middleware function:

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

// Custom logging middleware function
const requestLogger = (req, res, next) => {
    const timestamp = new Date().toISOString();
    const method = req.method;
    const url = req.originalUrl || req.url;
    
    console.log(`[${timestamp}] ${method} request to ${url}`);
    
    // Pass control to the next middleware function
    next();
};

// Mount middleware globally for all incoming requests
app.use(requestLogger);

// Parse JSON bodies
app.use(express.json());

// Sample route
app.get('/api/users', (req, res) => {
    res.json({ message: "List of users" });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

---

## Error-Handling Middleware

Error-handling middleware functions are defined with four arguments instead of three: `(err, req, res, next)`:

```javascript
app.use((err, req, res, next) => {
    console.error("Unhandled Error:", err.stack);
    res.status(500).json({
        error: "Internal Server Error",
        message: err.message
    });
});
```

