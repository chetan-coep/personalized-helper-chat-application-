---
id: "javascript_013"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 13
source_url: "https://developer.mozilla.org/en-US/blog/securing-apis-express-rate-limit-and-slow-down"
language: "en"
retrieved_at: "2026-11-01 21:53:39"
content_hash: "a1336adea2f48e9ad8e682a1ee5dba17c4a71cefbf2babd8be2c1f0a7a7e4198"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/securing-apis-express-rate-limit-and-slow-down

---

# Securing APIs: Express rate limit and slow down

Rate limiting and slow-down mechanisms help maintain the stability, security, and performance of web applications.
These controls prevent overloading systems and offer a level of protection against brute force and [Distributed Denial of Service](https://developer.mozilla.org/en-US/docs/Glossary/Distributed_Denial_of_Service) (DDoS) attacks.
Rate limiting also improves the scalability of your application and enhances user experience by maintaining service quality and reliability.

[Content delivery networks (CDNs)](https://developer.mozilla.org/en-US/docs/Glossary/CDN) and network-level solutions are popular and convenient ways to secure projects from these problems, but you can also implement controls and slow-down logic directly in your applications.
This approach gives you more control of your server's behavior and provides an additional fallback if a CDN or a DDoS protection fails.
Additionally, scripts or app integrations that are not malicious can misbehave because of bugs or network issues.
Rate limiting and slow-down mechanisms can stop programs from performing actions excessively and unintentionally using system or network resources.

In this article, we will create an Express application and incorporate rate limit and slow-down logic to make it more scalable and secure. There are many aspects to securing an application, but by using the methods described in this post, you should be comfortable with configuring one additional means of ensuring your Express apps are more resilient and secure.

## [Setting up an Express app on Vultr](https://developer.mozilla.org#setting_up_an_express_app_on_vultr)

To begin, deploy a server by following the steps in [Deploying a server on Vultr](https://developer.mozilla.org/en-US/blog/deploying-node-js-applications-with-pm2-on-vultr/#deploying_a_server_on_vultr) section in our previous article.
Next, let's proceed to access the server terminal via SSH and set up a project for our web application.

We'll be using the [Nano](https://help.ubuntu.com/community/Nano) text editor to create and edit our project files on the server.
You can check the [shortcuts cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) for help using Nano.
We'll also be using [Uncomplicated Firewall (UFW)](https://help.ubuntu.com/community/UFW) to control the traffic that is allowed in and out of the server.
Our Express app uses port `3000`, so we can enable incoming traffic via only this port using UFW.

1. Create a project directory, and navigate into it. bash```
mkdir express-api-security
cd express-api-security
```
2. Initialize a Node.js project. bash```
npm init -y
```
3. Install the Express dependency. bash```
npm install express
```
4. Create another directory for the landing page, and navigate into it. bash```
mkdir public
cd public
```
5. Create an HTML file. bash```
nano index.html
```
6. Copy and paste the code below into the `index.html` file.
html```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Express Rate Limit & Slow Down</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f0f0;
      }
      .container {
        text-align: center;
      }
      h1 {
        color: #333;
      }
      p {
        color: #666;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Express Rate Limit & Slow Down Applied</h1>
      <p>Rate limiting and speed limiting are applied to this page.</p>
    </div>
  </body>
</html>
```
7. Save and exit the file.
8. Exit the public directory, and create a JavaScript file. bash```
cd ..
nano app.js
```
9. Copy and paste the code below into the `app.js` file.
js```
const express = require("express");
const app = express();
const port = 3000;
app.use(express.static("public"));
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```
10. Allow incoming connections to port `3000`.
bash```
ufw allow 3000
```
11. Reload the firewall. bash```
ufw reload
```
12. Run the Node.js application. bash```
node app.js
```

You should see "Server is running on port 3000" logged to the console if your app is running, and you can access the application at the server IP and port `3000`:

http://\<server-ip>:3000

You can reload the webpage as many times as you want, the reload speed is not affected as no rate limit and slow-down mechanisms are applied.
You can stop the application by pressing `Ctrl` + `C`.

## [Understanding Express rate limit middleware](https://developer.mozilla.org#understanding_express_rate_limit_middleware)

The [express-rate-limit](https://www.npmjs.com/package/express-rate-limit) middleware is used to control the rate of incoming requests to an Express application.

- `windowMs`: Defines the time in milliseconds during which the rate limit applies. For example, `windowMs: 15 * 60 * 1000` sets a 15-minute window.
- `max`: Specifies the maximum number of requests allowed from a single IP address within the time window.
If requests exceed this defined limit then the rate limit will be triggered.

### [Implementing rate limiting in Express applications](https://developer.mozilla.org#implementing_rate_limiting_in_express_applications)

In this section, we are going to apply the [express-rate-limit](https://www.npmjs.com/package/express-rate-limit) middleware to the Express application.

1. Install the `express-rate-limit` dependency.
bash```
npm install express-rate-limit
```
2. Open the `app.js` file in the `express-api-security` directory.
bash```
nano app.js
```
3. Add the middleware. Your JavaScript file should look like this: js```
const express = require("express");
const rateLimit = require("express-rate-limit");
const app = express();
const port = 3000;
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
});
app.use(limiter);
app.use(express.static("public"));
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```
4. Save and exit the file.
5. Run the application using `node app.js`.

Let's look at the changes we've made in `app.js`. We're importing `express-rate-limit` and creating a rate limiter as a const `limiter` and configuring it at a maximum of 5 requests per IP address within a 15-minute window.

If a client exceeds the defined limit, subsequent requests will receive a [429 (Too Many Requests)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/429) status code until the time window resets. You can enable the middleware using `app.use(limiter)`.

When you visit the application URL, refresh the page a few times.
When you refresh the page 6 times, you will see a browser error screen that says "Too many requests, please try again later".
When you're finished testing rate limiting, stop the application by pressing `Ctrl` + `C`.

## [Understanding Express slow-down middleware](https://developer.mozilla.org#understanding_express_slow-down_middleware)

The [express-slow-down](https://www.npmjs.com/package/express-slow-down) middleware introduces delays in responding to requests. This delay helps to spread out the incoming requests over time, reducing the load on the server.
Unlike rate limiting, it doesn't immediately reject requests when the limit is exceeded.

- `delayAfter`: Specifies the number of requests after which the slow-down effect takes place.
For example, setting `delayAfter: 1` means the slowdown applies after the first request.
- `delayMs`: Specifies the delay in milliseconds added to each request once the limit defined by `delayAfter` is exceeded.

### [Implementing slow-down mechanism into Express applications](https://developer.mozilla.org#implementing_slow-down_mechanism_into_express_applications)

In this section, we are going to apply the Express slow down-middleware to the Express application.

1. Install the `express-slow-down` dependency.
bash```
npm install express-slow-down
```
2. Open the `app.js` file in the `express-api-security` directory.
bash```
nano app.js
```
3. Add the middleware. Your JavaScript file should look like this: js```
const express = require("express");
const rateLimit = require("express-rate-limit");
const slowDown = require("express-slow-down");
const app = express();
const port = 3000;
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
});
const speedLimiter = slowDown({
  windowMs: 15 * 60 * 1000,
  delayAfter: 1,
  delayMs: () => 2000,
});
app.use(speedLimiter);
app.use(limiter);
app.use(express.static("public"));
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```
4. Save and exit the file.
5. Run the application using `node app.js`.

We've made similar changes to `app.js` that we've done before for rate limiting.
We're importing `express-slow-down` and creating the speed limiting middleware as a const `speedLimiter`.
The configuration we've added slows down the request rate after 1 request by adding a delay of 2000 milliseconds (2 seconds) to each subsequent request within a 15-minute window.
Again, you apply the middleware with `app.use(speedLimiter)`.

When you visit the application URL, try refreshing the page repeatedly. You will see that the time it takes to load the page upon refresh increases each time. This is an overeager use of slowdown for illustration, so you can enable speed limiting after a much higher number of requests in your actual application. The benefit is that this is configurable depending on how your app is really used.

## [Practical uses and examples](https://developer.mozilla.org#practical_uses_and_examples)

Let's look at how rate limiting and slow-down can be used in real-world applications. Here are two common use cases:

- Social media platforms provide APIs that allow developers to access their data. However, to prevent abuse and ensure fair usage, these platforms integrate rate limiting. 
  - The API endpoints have rate limits defined specifying the number of requests that can be made per user within a certain timeframe.
  - They also integrate a slow-down mechanism to prevent sudden bursts of requests.
- E-commerce websites experience spikes in traffic in the holiday seasons. To prevent server overload, ensure smooth checkout processes, and protect against fraud, these platforms integrate rate limit and slow-down mechanisms during the checkout and order processing workflows. 
  - Checkout and order processing endpoints are rate limited to restrict the number of requests, such as adding items to the cart or submitting orders, within a certain timeframe.
  - After exceeding the initial rate limit, additional requests may be subjected to delays, ensuring that the server can process incoming orders without being overwhelmed by sudden surges in traffic.

## [Conclusion](https://developer.mozilla.org#conclusion)

In this article, we created an Express app and learned how to include rate-limiting and slow-down mechanisms. By learning how to incorporate and configure these features in your projects, you will be able to create scalable server-side Node.js apps that have more robust request handling for better security and resilience.

*This is a sponsored article by Vultr. Vultr is the world's largest privately-held cloud computing platform. A favorite with developers, Vultr has served over 1.5 million customers across 185 countries with flexible, scalable, global Cloud Compute, Cloud GPU, Bare Metal, and Cloud Storage solutions. Learn more about [Vultr](https://www.vultr.com/campaign/compute/).*