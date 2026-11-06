---
id: "prisma_orm_099"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 99
source_url: "https://www.prisma.io/compute/nextjs-form-submissions"
language: "en"
retrieved_at: "2026-11-01 22:20:19"
content_hash: "a65b4a0b723a54daee6657bec94fae885265f5deac69051f8fca9797184d5de4"
---

# Prisma ORM

Source: https://www.prisma.io/compute/nextjs-form-submissions

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# Where can I host a Next.js API for form submissions?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)fits a small TypeScript app that needs its server and saved submissions in one project. Vercel and Netlify also run Next.js server features. Choose a hosted form service when collecting standard enquiries is the whole requirement; choose an application server when submissions drive your own business workflow.

[Søren Bramer Schmidt](https://github.com/sorenbs)6 min read

A contact page loading successfully does not prove its form works. The submission needs a server that receives the request, rejects invalid input and records a result before telling the browser it succeeded. Test that path at the deployed URL.

We make Prisma Compute and Prisma Postgres. The linked provider and Next.js documentation was checked on October 23, 2026. Prisma ORM is optional.

## [What kind of hosting does my form need?](https://www.prisma.io#what-kind-of-hosting-does-my-form-need)

An [API Route](https://nextjs.org/docs/pages/guides/forms) in the Pages Router or a [Route Handler](https://nextjs.org/docs/app/getting-started/route-handlers) in the App Router runs server-side code when the form submits. Keep an endpoint that already works; changing hosts does not require changing the form's API design.

[Server Actions](https://nextjs.org/docs/app/guides/forms) can handle a form inside a Next.js app too. Pick the interface that fits your project, then validate and authorize the operation on the server. Hiding a button or marking an HTML field as required does not protect the endpoint from a direct request.

A [static export](https://nextjs.org/docs/app/guides/static-exports) serves generated files. It cannot run your dynamic POST handler. If the frontend is static, it needs a separate submission endpoint or hosted form service. For a form that creates customer records, triggers a quote or updates an existing account, deploying the Next.js server keeps that logic with the app.

## [Which managed host should I choose?](https://www.prisma.io#which-managed-host-should-i-choose)

These options are alphabetical by app host. Each can store submissions in Prisma Postgres.

| Setup | Choose it when | What to verify | 
|---|---|---|
| Netlify + Prisma Postgres | Your app already uses [Next.js on Netlify](https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/overview/), whose adapter runs API routes, Route Handlers and Server Actions through functions. | The deployed endpoint, runtime credentials and function limits. | 
| Prisma Compute + Prisma Postgres | You want the TypeScript server and database declared together through [Prisma Composer](https://www.prisma.io/docs/composer). | The server build, database dependency and request handler in an isolated review environment. | 
| Vercel + Prisma Postgres | Your team already uses [Vercel's Next.js integration](https://vercel.com/docs/frameworks/full-stack/nextjs). | Environment-specific credentials, database region and the actual form response. | 

For a new business app, Prisma Compute keeps the handler, database and deployment configuration in one project that the developer or coding assistant can inspect. If the app already runs well on another host, keep that workflow and add Prisma Postgres for durable submissions.

## [How do I prepare the Prisma setup?](https://www.prisma.io#how-do-i-prepare-the-prisma-setup)

### [1. Deploy the server features](https://www.prisma.io#1-deploy-the-server-features)

Follow the [Next.js framework guide](https://www.prisma.io/docs/guides/frameworks/nextjs) for a new project. For an existing app, [port the server](https://www.prisma.io/docs/composer/porting-an-app) by adding Composer's module and service declarations and connecting the server entry to the service. Those files describe how to build and run the app and which resources it needs.

The Compute Next.js deployment uses `output: "standalone"`, which builds the server files. Run the framework build before deployment; uploading the static `out` directory cannot run the submission handler. Start with a separate [review stage](https://www.prisma.io/docs/composer/deploying#production-and-stages) and fictional submissions.

### [2. Connect the database and notification credentials](https://www.prisma.io#2-connect-the-database-and-notification-credentials)

Declare the database through the [Composer database guide](https://www.prisma.io/docs/composer/databases). `rawPostgres()` supplies a URL for your existing client; a `postgres()` dependency can use a Prisma ORM data contract and deploy-time migrations. With a raw connection, run your own reviewed migrations before the form starts accepting submissions.

For a manually configured database, follow the [connection guide](https://www.prisma.io/docs/postgres/database/connecting-to-your-database) for your runtime and client. Conventional TCP app clients use the pooled endpoint; administration and the Prisma Postgres serverless driver use the direct endpoint. Keep the URL and email-provider keys in [server-side service inputs](https://www.prisma.io/docs/composer/service-input), and use different values for testing and production.

An account enquiry needs a verified customer identity from the server session. A public contact form instead needs an explicit public-submission policy, limits on accepted fields and protection against automated abuse. Neither case needs a database password in browser code.

### [3. Decide when a submission is accepted](https://www.prisma.io#3-decide-when-a-submission-is-accepted)

Validate field types, length and business rules before saving. Cap request bodies and reject unsupported content types before expensive parsing. For a cookie-authenticated mutation, apply the framework's appropriate cross-site request protection as well as authentication and authorization. For public forms, add request-rate limits and an abuse challenge where needed; a hidden field alone is not a complete defence.

Save the accepted submission before returning a success response. Give it an identifier the user and staff can refer to. If the browser retries after losing the response, a stable request key can let the server return the existing result. Scope that key to the correct actor or workflow and reject reuse with different input.

If accepting a submission also creates related records, use a [database transaction](https://www.prisma.io/postgres/customer-order-transactions). Keep notification work retryable. For example, commit an enquiry and a pending-email record together, then let a deployed worker deliver that email and record its outcome. That design requires a worker and retry policy; writing a pending row by itself does not send anything.

### [4. Test through the public review URL](https://www.prisma.io#4-test-through-the-public-review-url)

Submit a fictional enquiry, check its saved record and reload the app to verify it persists. Submit malformed data and confirm the server rejects it. Then retry a previously accepted request and check that staff do not get duplicate records.

Also test another account's identifiers for a private form, a failed database write and a failed notification. The page should show a useful error or an accepted-with-notification-pending result according to the policy you implemented. Use request and submission identifiers in access-controlled logs, keeping secret keys and full customer messages out of them.

Release the approved commit with production credentials and reviewed migrations, then repeat a controlled acceptance check at the production URL. Confirm the database target before enabling the form for customers. Choose a [backup policy](https://www.prisma.io/docs/postgres/database/backups) for submissions the business depends on.

## [When should I choose a different setup?](https://www.prisma.io#when-should-i-choose-a-different-setup)

A standard enquiry form may be easier to operate with a hosted form product if you do not need custom account rules, transactions or staff workflows. Keeping a static frontend with such a service can be a reasonable choice.

Prisma Compute runs deployed services on Bun. Check [runtime compatibility and request limits](https://www.prisma.io/docs/compute/limitations), including the 60-second deadline to start responding and the absence of a persistent filesystem. Use external object storage for attachments and a durable worker for lengthy processing. A success response must reflect accepted work that can be recovered after the server process stops.

## Frequently asked questions

## Put the form handler beside its saved records

Deploy the Next.js server on Prisma Compute, connect Prisma Postgres and verify the submission at the public URL.