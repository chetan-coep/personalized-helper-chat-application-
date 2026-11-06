---
id: "javascript_072"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 72
source_url: "https://developer.mozilla.org/en-US/blog/static-site-generation-with-nextjs"
language: "en"
retrieved_at: "2026-11-01 21:53:45"
content_hash: "8742b8cb2039d7fbc76f9f723912a499acb04850d32bd608473818cb467c6812"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/static-site-generation-with-nextjs

---

# Static Site Generation (SSG) with Next.js

[Static Site Generators (SSGs)](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation) are tools for producing HTML in advance so a server can efficiently send the same content to all visitors without creating it first.
Unlike dynamic web pages, where a server may query a database on page load and populate templates, an SSG pre-builds the files so that when you deploy them, the server has less work to do when your website is visited.

SSGs have several benefits, such as faster loading time and better visitor user experience.
For developers, scalability is also convenient with static sites as you can cache and serve entire websites in [Content Delivery Networks (CDNs)](https://developer.mozilla.org/en-US/docs/Glossary/CDN) instead of deploying more servers.
With no server-side processing or database interactions, static sites are more resilient to security vulnerabilities like SQL injection or cross-site scripting (XSS) attacks.

In this article, we will create a Next.js application and use the default rendering mode to create a static site that is performant and efficient.

## [Setting up a Next.js app on Vultr](https://developer.mozilla.org#setting_up_a_next.js_app_on_vultr)

To begin, deploy a server using the [NodeJS](https://www.vultr.com/marketplace/apps/nodejs) image by following the steps in [Deploying a server on Vultr](https://developer.mozilla.org/en-US/blog/deploying-node-js-applications-with-pm2-on-vultr/#deploying_a_server_on_vultr) section in our previous article. Next, let's proceed to access the server terminal via SSH and set up a project for our web application.

To get us started, we'll use [create-next-app](https://nextjs.org/docs/pages/api-reference/create-next-app), a starter template for quickly bootstrapping Next.js applications.
For illustration, we'll use static generation in our app but fetch some data at build time.
This way, we will build a flexible website while still benefiting from deploying static pages.

We'll be using the [Nano](https://help.ubuntu.com/community/Nano) text editor to create and edit our project files on the server.
You can check the [shortcuts cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) for help using Nano.
We'll also be using [Uncomplicated Firewall (UFW)](https://help.ubuntu.com/community/UFW) to control the traffic that is allowed in and out of the server. Our Next app uses port `3000`, so we can enable incoming traffic via only this port using UFW.

1. Allow incoming connections to port `3000`, and reload the firewall.
bash```
sudo ufw allow 3000
sudo ufw reload
```
2. Create a Next.js application `sample-app`.
bash```
npx create-next-app@latest sample-app
```
3. In the setup wizard, enter the following responses: â Would you like to use TypeScript? â¦ No â Would you like to use ESLint? â¦ Yes â Would you like to use Tailwind CSS? â¦ No â Would you like to use \`src/\` directory? â¦ Yes â Would you like to use App Router? (recommended) â¦ Yes â Would you like to customize the default import alias (@/\*)? â¦ No
4. Navigate into the project directory, and open the `package.json` file:
bash```
cd sample-app
nano package.json
```
5. Change the `start` value, to access the application via server IP.
json```
"scripts": {
    "start": "next start -H 0.0.0.0",
},
```
6. Save and exit the file.
7. Navigate into the `src/app` directory.
bash```
cd src/app
```
8. Create a new directory `posts` within the `src/app` directory, and navigate into it.
bash```
mkdir posts
cd posts
```
9. Create a JavaScript file called `page.js`
bash```
nano page.js
```
10. Copy and paste the below code into the `page.js` file.
jsx```
import React from "react";
import styles from "../page.module.css";
async function getPosts() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  return res.json();
}
const posts = await getPosts();
export default async function PostsPage() {
  return (
    <main className={styles.main}>
      <h1>Posts archive</h1>
      <ol>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ol>
    </main>
  );
}
```
11. Save and exit the file
12. From the project root, create a production build and start the Next.js application in production mode: bash```
npm run build && npm run start
```

You should see something like this:

Creating an optimized production build ...
â Compiled successfully
â Linting and checking validity of types
â Collecting page data
â Generating static pages (6/6)
â Collecting build traces
â Finalizing page optimization
Route (app)                              Size     First Load JS
â â /                                    5.42 kB        92.4 kB
â â /\_not-found                          871 B          87.9 kB
â â /posts                               137 B          87.2 kB
+ First Load JS shared by all            87 kB
 â chunks/23-ef3c75ca91144cad.js        31.5 kB
 â chunks/fd9d1056-2821b0f0cabcd8bd.js  53.6 kB
 â other shared chunks (total)          1.87 kB
â  (Static)  prerendered as static content

You can view the application at `http://<server-ip>:3000/posts` to see what we're generating at this point.

Let's look at the code we used to get this far.
For fetching data, `getPosts()` sends a `GET` request to a URL that serves placeholder data.
You might not make fetch requests in your application; you might instead get some information from data files on disk on the server or even query a local database.
This example is helpful because we see what happens when we need external data from our website.

We're storing the request result as a variable `posts` that we can iterate over in the page template.
The `PostsPage` function is the default export of the component, and it returns a JSX element that will be rendered as the component's output.
We're iterating over each post returned from the endpoint and creating an ordered list of post titles.

You can stop the application by pressing `Ctrl` + `C`.

## [Understanding SSG in Next.js apps](https://developer.mozilla.org#understanding_ssg_in_next.js_apps)

Here are the key concepts you should understand when using SSG in Next.js apps, including the benefits they bring.

- **Pre-rendering**
  - During the build process, all the pages of a website are pre-rendered into static HTML files. The content is generated once and stored as static files.
- **Content sources**
  - You can source content from various places, such as a headless CMS, databases, or REST APIs.
  - The content is fetched and processed to create HTML files during the build process.
- **Deployment**
  - You can cache and efficiently serve the built files using a web server or [Content Delivery Network (CDN)](https://docs.vultr.com/vultr-content-delivery-network).
If you know the files do not change, you can be more aggressive with caching, which is more efficient for visitors and your server costs.
  - You don't have to consider provisioning and maintaining an environment for server-side logic.

### [Adding dynamic routes to a static Next.js site](https://developer.mozilla.org#adding_dynamic_routes_to_a_static_next.js_site)

Now that we know how to fetch data from a public API at build time and populate a page template with the response for static pages, we might need to do something more complex.

We have a post archive at `/posts` that lists all the post titles, but we want to create individual pages for each post.
We will use the numeric post `id` for this (e.g., `/posts/12`), but you can imagine it might also be interesting to use the `title`, for example, `/posts/my-cool-post`.

This poses an interesting problem because we might not know the IDs of the posts we're fetching at build time. How do we create template pages for every post? We can use dynamic routes to handle this case, which lets us add special handling to the routing but keeps static site generation as the preferred output.

To add dynamic routes for numeric blog IDs, make a directory with the special Next.js format `[segmentName]` (in this case `[id]`).
If you're following these steps on a different machine using a shell like zsh, you will have to quote the square brackets like `'[id]'`:

1. Create a new directory `[id]` within the `src/app/posts` directory, and navigate into it.
bash```
mkdir "[id]"
cd "[id]"
```
2. Create a new JavaScript file. bash```
nano page.js
```
3. Copy and paste the below code into the `page.js` file.
jsx```
import React from "react";
import { notFound } from "next/navigation";
import styles from "../../page.module.css";
async function getPost(id) {
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${id}`,
  );
  if (!res.ok) {
    return null;
  }
  return res.json();
}
export async function generateStaticParams() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = await res.json();
  return posts.map((post) => ({
    id: post.id.toString(),
  }));
}
export default async function PostPage({ params }) {
  const post = await getPost(params.id);
  if (!post) {
    notFound();
  }
  return (
    <main className={styles.main}>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </main>
  );
}
```
4. Save and close the file.
5. Recreate the production build and restart the application: bash```
# in the project root:
npm run build && npm run start
```

You should see the following:

Creating an optimized production build ...
â Compiled successfully
â Linting and checking validity of types
â Collecting page data
â Generating static pages (106/106)
â Collecting build traces
â Finalizing page optimization
Route (app)                              Size     First Load JS
â â /                                    5.42 kB        92.4 kB
â â /\_not-found                          871 B          87.9 kB
â â /posts                               338 B          87.4 kB
â â /posts/\[id\]                          338 B          87.4 kB
   â /posts/1
   â /posts/2
   â /posts/3
   â \[+97 more paths\]

Note that we've generated 106 pages this time, so the additional 100 posts are created at build time, and the page paths are pre-rendered depending on external data.
If you want to explore other options, you can also look at [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#when-should-i-use-getstaticpaths) and the [Next.js examples repository](https://github.com/vercel/next.js/tree/canary/examples) for other ways to add dynamic routes to an SSG build.

You can now visit the server at `http://<server-ip>:3000/posts` and explore each post at the numeric ID, like `http://<server-ip>:3000/posts/2`.

## [Practical uses and examples](https://developer.mozilla.org#practical_uses_and_examples)

Here are some examples where SSGs using Next.js work well:

- **Content-heavy websites**: Blogs, documentation, and marketing sites where the content is relatively static and doesn't change much.
- **E-commerce**: You can pre-render product pages so that you have fast-loading pages where conversions matter.
- **Jamstack architecture**: Jamstack websites usually use JavaScript functionality on the client side while keeping the server-side static. If you're making a lot of network requests client-side, be aware that you might shift the performance cost to your visitors, so weigh this option carefully.

## [Conclusion](https://developer.mozilla.org#conclusion)

In this article, we created a Next.js application and deployed it to a Vultr NodeJS image. We learned how to use SSG to make a fast, scalable, and reasonably secure application. By learning how to use SSGs, you can create more resilient web applications with modern tooling and architecture.

*This is a sponsored article by Vultr. Vultr is the world's largest privately-held cloud computing platform. A favorite with developers, Vultr has served over 1.5 million customers across 185 countries with flexible, scalable, global Cloud Compute, Cloud GPU, Bare Metal, and Cloud Storage solutions. Learn more about [Vultr](https://www.vultr.com/campaign/compute/)*