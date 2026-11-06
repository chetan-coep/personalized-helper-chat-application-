---
id: "prisma_orm_090"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 90
source_url: "https://www.prisma.io/compute/customer-report-hosting"
language: "en"
retrieved_at: "2026-11-01 22:20:05"
content_hash: "a3715b8d1404d14e9a7d977b27da7db0b592e8cbae78db74fb2dafd64c71dc03"
---

# Prisma ORM

Source: https://www.prisma.io/compute/customer-report-hosting

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# What hosting should I use for customer reports?

[Prisma Compute](https://www.prisma.io/docs/compute),

[Prisma Postgres](https://www.prisma.io/docs/postgres)and an Object Store bucket keep those resources in one project. That is a practical fit for a TypeScript business app with bounded report requests. Keep Vercel or Netlify when their existing workflow fits, and choose a suitable worker runtime for generation that must finish independently of a request.

[Søren Bramer Schmidt](https://github.com/sorenbs)6 min read

The report is useful only if the right customer can obtain the right result. That includes a saved filter choice, a defined view of the data, a generation status and a file that still exists after the next deployment.

We make Prisma Compute and Prisma Postgres. The linked hosting, storage and PostgreSQL documentation was checked on October 22, 2026.

## [What determines the hosting setup?](https://www.prisma.io#what-determines-the-hosting-setup)

Start with the actual report engine and workload. A small CSV can come from a bounded database query. A large PDF may need a rendering library, substantial memory or a browser process. Test that dependency in the intended runtime before choosing a host.

Decide whether the result must be generated during the request or can arrive later. Measure query time, rendering time, output size and concurrent requests with a representative dataset. A successful two-row demo does not establish how a customer's largest report behaves.

## [Which app host fits the report endpoint?](https://www.prisma.io#which-app-host-fits-the-report-endpoint)

These app hosts are listed alphabetically. Each can connect to managed Postgres and an appropriate object store.

| Setup | Useful fit | Verify before launch | 
|---|---|---|
| Netlify + Prisma Postgres | An existing app built around [Netlify functions](https://docs.netlify.com/build/functions/overview/). | The chosen runtime supports the renderer and the report fits the function's documented limits. | 
| Prisma Compute + Prisma Postgres + Object Store | A TypeScript app that wants its server, database and [private files](https://www.prisma.io/docs/compute/object-storage) in one project. | The deployed Bun runtime supports the report engine, and longer work has a durable execution plan. | 
| Vercel + Prisma Postgres | A Next.js app already using [Vercel functions](https://vercel.com/docs/functions). | Renderer dependencies, request duration and how unfinished work is recovered. | 

For a new TypeScript app serving small customer-scoped reports, Compute keeps the endpoint and saved data together. You can also use Prisma Postgres while keeping the report API on an existing host.

## [How do I build the Prisma workflow?](https://www.prisma.io#how-do-i-build-the-prisma-workflow)

### [1. Define the report and its customer boundary](https://www.prisma.io#1-define-the-report-and-its-customer-boundary)

Create a development Prisma Postgres database and a private [Object Store bucket](https://www.prisma.io/docs/compute/object-storage) in the intended project. Use fictional customer data and separate storage from production while testing.

Store a report identifier, owning account, requested filters, generation state, creation time and eventual object key. The server derives the account from verified authentication. A request's account field or an unguessable report identifier is not sufficient permission to query or download another customer's data.

### [2. Check the query before adding a renderer](https://www.prisma.io#2-check-the-query-before-adding-a-renderer)

With `psql` installed, open a development database connection and run this self-contained example. It reads fictional values and creates no tables:

The result is `order_count = 2` and `total_cents = 17500`. The other account is excluded. In application code, bind the authorized account as a parameter and validate report filters. The constant in this demonstration is not an authentication implementation.

Define whether a report describes current data or a saved state at a particular time. For a small report that needs several queries to agree, begin a short read-only transaction at PostgreSQL's [Repeatable Read isolation level](https://www.postgresql.org/docs/17/transaction-iso.html#XACT-REPEATABLE-READ) before the first query. Collect the authorized inputs and commit before rendering or uploading. For large exports, design a saved or versioned input dataset rather than holding an open transaction through a long rendering job. Pagination alone does not freeze records that are being updated.

### [3. Choose synchronous or queued generation](https://www.prisma.io#3-choose-synchronous-or-queued-generation)

For a bounded report, query authorized data, render it and return the result within the host's limits. Handle client disconnects and errors without reporting a completed download that never existed.

Compute has [60 seconds to start responding](https://www.prisma.io/docs/compute/request-timeout). Streaming can continue after the first response bytes, but it does not make a generation task durable. If work must finish independently of the request, save a report job and give it a deployed worker with a reliable trigger, retry policy and recovery after interruption.

The [Postgres job-queue guide](https://www.prisma.io/blog/you-dont-need-a-job-queue-postgres-already-has-skip-locked#where-to-run-the-worker) covers worker hosting. A process that must poll while there are no visitors belongs on a suitable always-on worker host. `waitUntil` can keep a Compute instance awake for best-effort work, but it does not supply durable retries or survive every redeploy.

### [4. Publish the file only after it exists](https://www.prisma.io#4-publish-the-file-only-after-it-exists)

Upload the finished result to a private object key for that job attempt, then mark the report ready in Postgres with that reference. An object upload and a database transaction are separate operations. If the state update fails, retry or reconcile the saved job and object; clean up abandoned attempt files through a defined procedure.

Before issuing a download, check that the authenticated account owns the ready report. The [object storage guide](https://www.prisma.io/docs/compute/object-storage) shows presigned URLs; set a short lifetime and keep the bucket private, with credentials available only to the server.

When generating CSV from customer-entered text, handle both CSV quoting and spreadsheet interpretation of formulas. Follow [CSV injection guidance](https://community.owasp.org/attacks/CSV_Injection) for values that spreadsheet software may execute; quoting a cell does not by itself make it inert.

### [5. Deploy and test recovery](https://www.prisma.io#5-deploy-and-test-recovery)

Configure the server with [Compute getting started](https://www.prisma.io/docs/compute/getting-started) or [Port an existing app](https://www.prisma.io/docs/composer/porting-an-app). Build before deploying and prepare each database with its [migrations](https://www.prisma.io/postgres/production-database-migrations). A newly declared deployment database does not inherit the Console development database's records.

Test a large report, two accounts requesting the same type, a failed upload, a worker restart and a repeated generation request. Verify that an unauthorized account cannot obtain the report and that the ready file survives an app redeploy. Put report progress and failure information in an authenticated status view.

## [When should I choose another setup?](https://www.prisma.io#when-should-i-choose-another-setup)

Choose a worker runtime that supports the renderer when it needs dependencies outside [Compute's runtime limits](https://www.prisma.io/docs/compute/limitations), or when generation must run as an always-on process. Compute can remain the customer-facing app while the worker uses the same managed Postgres database.

For internal analysis, an existing reporting or BI product may be more appropriate than a custom download service. For saved business data, choose the [backup and restore plan](https://www.prisma.io/docs/postgres/database/backups) separately from file delivery; a downloadable report is not a backup of the underlying database.

## Frequently asked questions

## Keep report data and delivery under control

Use Compute for the customer endpoint, Prisma Postgres for saved state and a private bucket for downloadable results.