---
id: "prisma_orm_074"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 74
source_url: "https://www.prisma.io/compare/convex"
language: "en"
retrieved_at: "2026-11-01 22:19:42"
content_hash: "91cea5b65bca77efba66adac2f7139de2d673996ccd4703dde62721e5abc8af7"
---

# Prisma ORM

Source: https://www.prisma.io/compare/convex

---

[Compare](https://www.prisma.io/compare)Convex

# Prisma Postgres vs Convex: standard Postgres or a reactive database?

Pick [Prisma Postgres](https://www.prisma.io/docs/postgres) when you want a standard SQL database. It is PostgreSQL, [Prisma ORM](https://www.prisma.io/docs/orm) is optional, and [Prisma Compute](https://www.prisma.io/docs/compute) hosts the TypeScript app as HTTP services. Pick [Convex](https://docs.convex.dev/understanding/) when you want a reactive database and TypeScript query functions, with the frontend on a host such as Vercel or Netlify.

[Get started with Prisma Postgres](https://console.prisma.io) [Create an instant database](https://create-db.prisma.io/web)

By [Martin Janse van Rensburg](https://www.prisma.io/blog/author/martin-janse-van-rensburg) · Updated  · 7 min read[X](https://x.com/vanrensbird)[LinkedIn](https://www.linkedin.com/in/martjvr/)[GitHub](https://github.com/vanrensbird)

Prisma makes Prisma Postgres. Convex figures come from the pages listed under [Sources](https://www.prisma.io#sources), checked October 2026.

## When should I choose Convex or Prisma Postgres?

| Convex | Prisma Postgres | 
|---|---|
| You want queries written as TypeScript functions, with no SQL in the application. | You want a standard SQL database. Prisma Postgres is PostgreSQL. | 
| You want a query to rerun when the data it read changes, and the client to receive that result. | You want to query it with SQL, or with Prisma ORM. Prisma ORM is optional. | 
| You want the database and the server functions in Convex, and the frontend on a host such as Vercel or Netlify. | You want Prisma Compute to host the TypeScript app as HTTP services. | 
| You want file storage, text search, vector search, and auth on the same Convex plan as the database. | You want a pricing page that does not list a per-developer fee. | 

## How do Convex and Prisma Postgres compare?

Convex is a reactive database. Application queries are TypeScript functions. Convex cloud stores data in MySQL on PlanetScale. Prisma Postgres is managed PostgreSQL, with an optional ORM and separate app hosting. Columns are in alphabetical order.

| Feature | Convex | Prisma Postgres | 
|---|---|---|
| Database | The Convex database. Application queries are TypeScript. Convex cloud stores data in MySQL on PlanetScale. The open-source version can use SQLite, Postgres, or MySQL as the persistence layer. | [Prisma Postgres](https://www.prisma.io/docs/postgres) is PostgreSQL. Any Postgres client works with it, so Prisma ORM is optional. | 
| Queries | TypeScript query and mutation functions. The overview says there is no SQL to write and no ORM is required. A mutation runs as a transaction. | SQL against PostgreSQL, or [Prisma ORM](https://www.prisma.io/docs/orm). Prisma ORM 8 is a release candidate. Models live in contract.prisma. | 
| Realtime updates | A query reruns when the data it read changes. The client library receives the new result over a WebSocket. | No built-in reactive query sync. [Prisma Compute](https://www.prisma.io/docs/compute) does not currently support WebSocket servers. | 
| App hosting | Convex runs the database and the server functions. The hosting guide says to publish the frontend with a provider such as Vercel or Netlify. | Prisma Compute hosts the TypeScript app as HTTP services. It is separate from Prisma Postgres. Compute has no built-in cron scheduler. Scheduled jobs can come from Composer's cron building block. | 
| Developer fees | Professional is $25 per developer per month, for 1 to 20 developers. Free and Starter list 1 to 6 developers. Business and Enterprise list 50 or more developers and a $2,500 monthly minimum. | The pricing page does not list a per-developer fee. | 
| Free plan | Free, or $0 a month and pay as you go. The resource table includes 0.5 GB of database storage and 1 million function calls, then usage rates. | Prisma Postgres Free is $0, with 200,000 operations a month, 2 GB of storage, and 50 databases. Prisma Compute Free includes 1 million requests a month. The Free plan says no credit card is required. | 

## Where does each one fit?

### Convex

Convex is a reactive database. Its [overview](https://docs.convex.dev/understanding/) describes TypeScript queries that rerun when their data changes, and a client library that subscribes over a WebSocket.

- Subscribed queries should update the UI when the underlying documents change.
- Mutations should be transactions, and the client should apply subscribed results from one moment in the database.
- File storage, text search, vector search, and auth should sit on the Convex plan with the database.
- Application queries should be TypeScript functions in a convex/ folder.

### Prisma Postgres

Prisma Postgres fits a team that wants PostgreSQL. [Prisma ORM](https://www.prisma.io/docs/orm) is optional. [Prisma Compute](https://www.prisma.io/docs/compute) is separate app hosting.

- The database should be PostgreSQL, with SQL and the Postgres ecosystem.
- Prisma ORM should be available, and optional, on that database.
- The app should deploy as HTTP services on Prisma Compute.
- Adding a developer should not be a line on the pricing page.

## What does Prisma Postgres do that Convex doesn't?

### PostgreSQL

Prisma Postgres is PostgreSQL. You connect with a Postgres client. Prisma ORM is optional on that connection.

### A contract-based ORM, when you want one

Prisma ORM 8 is a release candidate. Models live in contract.prisma, and contract emit writes the types. You can skip it and use SQL.

### HTTP app hosting

Prisma Compute hosts the TypeScript app. The current release focuses on HTTP services. WebSocket servers are not supported. Compute has no built-in cron scheduler. Scheduled jobs can come from Composer's cron building block, which adds a scheduler service.

### Pricing without a per-developer fee

The pricing page lists Prisma Postgres by operations, storage, and databases, and Prisma Compute by requests, memory, CPU, and bandwidth. It does not list a per-developer fee. Starter, Pro, and Business list spend limits.

## How much do Convex and Prisma Postgres cost?

| Cost | Convex | Prisma Postgres | 
|---|---|---|
| Free plan | Free, or $0 a month and pay as you go. 1 to 6 developers. | Prisma Postgres Free is $0. No credit card required. | 
| Paid plans | Professional is $25 per developer per month. Business and Enterprise have a $2,500 monthly minimum. | Starter $10, Pro $49, Business $129 a month for Prisma Postgres and Prisma Compute. | 
| Developer seats | A line on Professional, Business, and Enterprise. | None. The pricing page does not list a per-developer fee. | 
| Database storage on free | 0.5 GB included, then $0.22 per additional GB. | 2 GB included, with 200,000 operations and 50 databases. | 

Prisma Postgres has a Free plan: $0 a month for 200,000 operations, 2 GB of storage, and 50 databases. The [pricing page](https://www.prisma.io/pricing) lists the paid plans. Convex Free includes 0.5 GB of database storage and 1 million function calls ([Convex pricing](https://www.convex.dev/pricing), October 2026).

## When is Prisma Postgres the wrong choice?

- You want query results pushed to the browser when data changes. Convex subscriptions use WebSockets. Prisma Postgres has no built-in reactive query sync, and Prisma Compute does not currently support WebSocket servers. See [Compute limitations](https://www.prisma.io/docs/compute/limitations).
- You want the database, server functions, file storage, and auth in one Convex deployment, and the application should not write SQL. The [Convex overview](https://docs.convex.dev/understanding/) describes that model.

## How do I switch from Convex to Prisma Postgres?

1. Create the PostgreSQL database. Prisma ORM is optional. When the tables already exist, the [existing-database guide](https://www.prisma.io/docs/prisma-orm/add-to-existing-project/postgresql) shows `contract infer`.
2. Export the data. Every Convex plan can download a snapshot export, a ZIP with one `documents.jsonl` file per table, from the dashboard or with `npx convex export`, as the [backup and export guide](https://docs.convex.dev/database/backup-restore) describes. Professional adds streaming data exports. Load the JSONL into PostgreSQL yourself. This page does not include a converter.
3. Point the app at the Postgres connection string. Host the HTTP app on Prisma Compute, or keep the frontend host you already use.

## How do I switch from Prisma Postgres to Convex?

1. Define Convex tables and write query and mutation functions. The [overview](https://docs.convex.dev/understanding/) shows `ctx.db.query` and `ctx.db.patch`.
2. Subscribe from the client with `useQuery`. The client library uses a WebSocket.
3. Publish the frontend with a provider such as Vercel or Netlify, as the [hosting guide](https://docs.convex.dev/production/hosting) describes. Prisma Postgres stays in place until you stop using it.

## What do teams say about Prisma Postgres?

Two teams on what Prisma ORM and Prisma Postgres do for them.

## Frequently asked questions

[Convex overview](https://docs.convex.dev/understanding/), October 2026.

[Convex pricing](https://www.convex.dev/pricing), October 2026.

[supported databases](https://www.prisma.io/docs/orm/supported-databases)and the

[Convex overview](https://docs.convex.dev/understanding/), October 2026.

[Convex overview](https://docs.convex.dev/understanding/)and

[Compute limitations](https://www.prisma.io/docs/compute/limitations), October 2026.

## Ready to build with Prisma?

Free to start, no credit card required.

Prisma ORM is free and open source, and always will be.

- Create a database and start building in minutes
- Read the docs for guides and API reference
- Trusted by 500K+ developers globally

Need a database? [Create an instant database](https://create-db.prisma.io/web).

## Sources

Every competitor figure on this page comes from these pages, checked October 2026.