---
id: "tailwindcss_003"
technology: "TailwindCSS"
category: "Frontend"
title: "Installing Tailwind CSS with Vite - Tailwind CSS"
doc_order: 3
source_url: "https://tailwindcss.com/docs/installation"
language: "en"
retrieved_at: "2026-11-03 17:59:22"
content_hash: "5ad8eb86bd9a583812e2921158697a94ab9106576eeb627cd432e0d5892c6c1b"
---

# Installing Tailwind CSS with Vite - Tailwind CSS

Source: https://tailwindcss.com/docs/installation

---

Installation

Tailwind CSS works by scanning all of your HTML files, JavaScript components, and any other templates for class names, generating the corresponding styles and then writing them to a static CSS file.

It's fast, flexible, and reliable — with zero-runtime.

Installing Tailwind CSS as a Vite plugin is the most seamless way to integrate it with frameworks like Laravel, SvelteKit, React Router, Nuxt, and SolidJS.

`npm create vite@latest my-projectcd my-project`
Install `tailwindcss` and `@tailwindcss/vite` via npm.

`npm install tailwindcss @tailwindcss/vite`
Add the `@tailwindcss/vite` plugin to your Vite configuration.

`import { defineConfig } from 'vite'import tailwindcss from '@tailwindcss/vite'export default defineConfig({  plugins: [    tailwindcss(),  ],})`
Add an `@import` to your CSS file that imports Tailwind CSS.

`@import "tailwindcss";`
Run your build process with `npm run dev` or whatever command is configured in your `package.json` file.

`npm run dev`
Make sure your compiled CSS is included in the `<head>` *(your framework might handle this for you)*, then start using Tailwind’s utility classes to style your content.

`<!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="/src/style.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>`