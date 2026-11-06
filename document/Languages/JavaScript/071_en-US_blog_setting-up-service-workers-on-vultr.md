---
id: "javascript_071"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 71
source_url: "https://developer.mozilla.org/en-US/blog/setting-up-service-workers-on-vultr"
language: "en"
retrieved_at: "2026-11-01 21:53:43"
content_hash: "cc0110f1807ede7d77c0a376bd1c46d03adc18afd04bf0754f6ee423fbe93ebe"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/setting-up-service-workers-on-vultr

---

# Setting up service workers on Vultr

[Service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) provide a way to run scriptable network proxies in the web browser, allowing developers to control how web pages respond to network requests, manage resources, and build robust and performant web applications.
[Learning to use service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API#other_use_case_ideas) in your web application will help you build features like background data sync, pre-fetching resources your visitors will need next, processing data in one place instead of multiple pages, and other exciting functionalities.

In this article, we'll learn about the lifecycle of a service worker and why it's essential to understand how they work. We'll also create an example web application hosted on Vultr, including HTTPS via Nginx and Let's Encrypt, which we need to allow the service worker to run on visitors' browsers.

## [Service worker lifecycle](https://developer.mozilla.org#service_worker_lifecycle)

Service workers are event-driven JavaScript background tasks that run separately from the main thread of a web page. They act as intermediaries between the web page and the network to provide features like offline support, push notifications, and background synchronization.

Understanding the lifecycle of a service worker is crucial for effectively implementing and managing them in web projects. This lifecycle consists of three main phases:

- **Registration**: The initial step is the [registration phase](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register) where we check if the browser supports service workers.
- **Installation**: After registration, when the user visits the website the [service worker is immediately downloaded](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API#download_install_and_activate) for the service worker controlled URLs and a cache is created for the specified URLs. Whenever there's a new version of the website, installation will be triggered and the new version is installed in the background.
- **Activation**: During the activation phase, the service worker takes control of the web pages within its scope and begins intercepting network requests. This phase is typically an appropriate stage to clean up outdated caches and perform any necessary initialization tasks.

## [Setting up the project directory on Vultr](https://developer.mozilla.org#setting_up_the_project_directory_on_vultr)

To begin, deploy a server by following the steps in the [Deploying a server on Vultr](https://developer.mozilla.org/en-US/blog/deploying-node-js-applications-with-pm2-on-vultr/#deploying_a_server_on_vultr) section in our previous article.
No specific marketplace application is needed for this project.
Next, let's proceed to access the server terminal via SSH and set up a project for our web application.
We'll make a landing page with a CSS stylesheet and add a script to our main JavaScript file that will be used to check if the browser supports service workers and register the service worker.

We'll be using the [Nano](https://help.ubuntu.com/community/Nano) text editor to create and edit our project files on the server.
You can check the [shortcuts cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) for help using Nano.

1. Create a project directory, and navigate into it. bash```
mkdir sample
cd sample
```
2. Create an HTML file. bash```
nano index.html
```
3. Copy and paste the code below into the index.html file. html```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Service Worker App</title>
    <link rel="stylesheet" href="/main.css" />
  </head>
  <body>
    <h1>Welcome to My Service Worker App</h1>
    <p>This is a sample paragraph with <a href="#">a link</a>.</p>
    <script src="/app.js"></script>
  </body>
</html>
```
4. Save and exit the file.
5. Create a CSS file. bash```
nano main.css
```
6. Copy and paste the code below into the main.css file. css```
body,
h1 {
  margin: 0;
  padding: 0;
}
h1 {
  text-align: center;
  margin-top: 50px;
}
p {
  text-align: center;
}
body {
  background-color: #add8e6;
  font-family: Arial, sans-serif;
}
a {
  color: #00ff7b;
}
a:hover {
  text-decoration: underline;
}
```
7. Save and close the file.

## [Creating a service worker](https://developer.mozilla.org#creating_a_service_worker)

Now that you have set up a project directory, in this section you'll explore how a service worker is registered, installed, and activated.

### [Installing and activating a service worker](https://developer.mozilla.org#installing_and_activating_a_service_worker)

Let's add a basic service worker to our project that our main JavaScript app can interact with:

1. In the `sample` directory, create a JavaScript file:
bash```
nano sw.js
```
2. Copy and paste the code below into the `sw.js` file.
js```
const CACHE_NAME = "my-cache-v1";
const urlsToCache = ["/", "/index.html", "/main.css"];
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("Opened cache");
      return cache.addAll(urlsToCache);
    }),
  );
});
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((cacheName) => {
            return cacheName !== CACHE_NAME;
          })
          .map((cacheName) => {
            return caches.delete(cacheName);
          }),
      );
    }),
  );
});
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        return response;
      }
      return fetch(event.request);
    }),
  );
});
```
3. Save and exit the file.

In the code above, we are hooking into the three events we described earlier. When an install event is fired, we open a cache for URLs we're interested in controlling. We use the activate event to clear out any old caches we may have. Finally, we have a fetch event that checks if the resource requested by the user is cached; otherwise, it fetches the resource from the network and returns it.

### [Registering a service worker](https://developer.mozilla.org#registering_a_service_worker)

In this section, you'll learn how to check if a browser supports service workers, add an event listener to register the service worker, and give an alert once the service worker is registered.

1. Create a JavaScript file. bash```
nano app.js
```
2. Copy and paste the code below into the `app.js` file.
js```
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker
      .register("/sw.js")
      .then(function (registration) {
        alert(
          "Service Worker registration successful with scope: " +
            registration.scope,
        );
        if (registration.installing) {
          console.log("Service worker installing");
        } else if (registration.waiting) {
          console.log("Service worker installed");
        } else if (registration.active) {
          console.log("Service worker active");
        }
      })
      .catch(function (err) {
        alert("Service Worker registration failed: " + err);
      });
  });
}
```
3. Save and close the file.

In the code above, the `if ('serviceWorker' in navigator)` conditional checks if the browser supports service workers. If we have support for service workers, we can go ahead with registration using the `navigator.serviceWorker.register()` method given the script located at `/sw.js`. We're sending an alert that prints the scope URL and logging lifecycle status to the console.

## [Serving a web app on a Vultr server](https://developer.mozilla.org#serving_a_web_app_on_a_vultr_server)

In this section, you'll learn how to create a systemd service that starts automatically when the system boots up and runs a Python HTTP server that serves the web application.

1. Exit the `sample` directory.
bash```
cd ..
```
2. Create a Python file. bash```
nano http_server.py
```
3. Copy and paste the code below into the `http_server.py` file.
python```
import http.server
import socketserver
import os
PORT = 8000
DIRECTORY = "sample"
sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample")
mime_types = {
   ".html": "text/html",
   ".css": "text/css",
   ".js": "application/javascript",
}
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
   def guess_type(self, path):
      _, ext = os.path.splitext(path)
      return mime_types.get(ext.lower(), "application/octet-stream")
Handler = MyHTTPRequestHandler
os.chdir(sample_dir)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
   print("Serving at port", PORT)
   httpd.serve_forever()
```
4. The above code starts a Python HTTP server in our `sample` directory on port `8000`.
5. Save and exit the file.
6. Allow permission to execute the `http_server.py` as a script.
bash```
chmod +x http_server.py
```
7. Create a service worker service file. bash```
sudo nano /etc/systemd/system/pythonserver.service
```
8. Paste the following content into the service file. Make sure to replace the `User` and `Group` values with your actual values.
Also, replace `WorkingDirectory` with the actual `sample` directory path and `Execstart` with the actual `http_server.py` path.
\[Unit\] Description= Daemon for Sample Demo Application After=network.target \[Service\] User=example\_user Group=example\_user WorkingDirectory= /example\_user/sample ExecStart= /usr/bin/python3 /example\_user/http\_server.py \[Install\] WantedBy=multi-user.target
9. Start the service. bash```
sudo systemctl start pythonserver
```
10. Verify the status of the service. bash```
sudo systemctl status pythonserver
```
11. The output will look like this. ```
â pythonserver.service - Daemon for Sample Demo Application
   Loaded: loaded (/etc/systemd/system/pythonserver.service; disabled; preset: enabled)
   Active: active (running) since Fri 2024-04-05 10:29:31 UTC; 3s ago
Main PID: 10181 (python3)
   Tasks: 1 (limit: 1011)
   Memory: 8.6M
      CPU: 43ms
   CGroup: /system.slice/pythonserver.service
            ââ10181 /usr/bin/python3 /example_user/http_server.py
```
12. Enable the service to start automatically whenever the system boots up. bash```
sudo systemctl enable pythonserver
```

### [Securing a web app on Vultr using HTTPS](https://developer.mozilla.org#securing_a_web_app_on_vultr_using_https)

Service workers only work in HTTPS contexts due to security reasons. This prevents man-in-the-middle attacks and reduces the risk of data interception and tampering over the network.

The first step is configuring a reverse proxy for your web application. We can use Nginx for efficient request handling and load balancing.
Next, you need to request a free SSL certificate from [Let's Encrypt](https://letsencrypt.org/) to add HTTPS.
The steps to perform this are described in our previous article [Configuring Nginx as a reverse proxy server and Installing an SSL certificate using Certbot](https://developer.mozilla.org/en-US/blog/build-ai-powered-apps-openllm-vultr-gpu/#configuring_nginx_as_a_reverse_proxy_server).

Once you have applied HTTPS, visit your application's URL, and if everything's working, you'll see an alert with the service worker scope. You can also check your browser's developer console to see lifecycle events. The first time you visit the page, the cache will be opened and the service worker will be installed. You can refresh the page to see the service worker is activated and the webpage can be accessed by the user while being offline. To test this you can turn off your internet connection and refresh the page again.

## [Conclusion](https://developer.mozilla.org#conclusion)

In this article, we learned what service workers are and the different phases of their lifecycle. We also learned how to create a web application with a service worker that adds offline functionality to specific pages and resources. Using service workers can significantly improve the user experience by allowing users to access content even when they're offline.

*This is a sponsored article by Vultr. Vultr is the world's largest privately-held cloud computing platform. A favorite with developers, Vultr has served over 1.5 million customers across 185 countries with flexible, scalable, global Cloud Compute, Cloud GPU, Bare Metal, and Cloud Storage solutions. Learn more about [Vultr](https://www.vultr.com/campaign/compute/)*