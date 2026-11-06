---
id: "prisma_orm_081"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 81
source_url: "https://www.prisma.io/compute"
language: "en"
retrieved_at: "2026-11-01 22:19:52"
content_hash: "6f4bc690a6a3e2ffb22a03c5432c84f17fa7667af9da8a90b13dde4b1469093b"
---

# Prisma ORM

Source: https://www.prisma.io/compute

---

Prisma Compute

# One platform for your app and its database

Prisma Compute hosts TypeScript apps (Node.js, Bun or Next.js) next to Prisma Postgres in one project.

Generally available since August 2026. Free plan, no credit card.

- Set up deploy on push, and every feature branch gets a preview with its own declared databases
- Your app runs next to Prisma Postgres, in one of six regions
- Streams responses and scales to zero when idle, for agents as well as apps

## One platform can ship features two never could

When your hosting provider and your database provider are separate companies, the things that depend on them being aware of each other (per-branch previews with their own database, end-to-end test data) depend on an integration between the two that you set up and maintain.

Prisma Compute exists to change that.

A preview or staging environment per Git branch

Ship app and database in one deploy

Host streaming agents natively

One module.ts for app and database

## What one platform unlocks

Compute and Prisma Postgres run as a single platform. The features below are only possible because of that.

streamopen

### Built for hosting AI agents

Agents stream their answers and spend most of their time waiting on a model API. Compute streams a response as your service sends it, bills memory and active CPU separately, and scales to zero between tasks.

its own app and database

### A preview per feature branch

Once deploy on push is set up, every feature branch (any branch except the default) gets its own services and a new database for each one the Composer module declares, and deleting the branch tears them down. A database typed by a Prisma ORM contract gets your migrations applied on deploy; one declared with rawPostgres() keeps your own migration step. No shared test DB that passes tests production fails.

[Learn more about A preview per feature branch](https://www.prisma.io/docs/compute/deploy-on-push)

two dashboards, two bills

one project

### App and database on one platform

Your app runs next to Prisma Postgres, in the same project, with PgBouncer pooling included. Any Postgres client works, and Prisma ORM is optional.

POST /v1/buckets

### S3-compatible file storage built in

Object Store buckets live inside your project, next to its databases, managed from the same Console and API. Any S3 client works, with per-bucket keys scoped to read or read-write.

[Learn more about S3-compatible file storage built in](https://www.prisma.io/docs/compute/object-storage)

## Built to work with the rest of Prisma

Prisma Compute is where the stack comes together: your app, your database, and your data model on one platform. Standard Postgres underneath: leave with pg\_dump; the Composer module is a TypeScript file in your repo, not a runtime.

Best together. Swappable when needed.

Swap any layer. It still works.

Everything wired for you: one config, a preview with its own declared databases for each feature branch, and the app next to its database.

## Compare Prisma

How Prisma Compute and Prisma Postgres compare with the other hosting and Postgres options, and where each one fits.

- [App hosting platforms with managed Postgres compared (2026)Prisma Compute, Railway, Render, Fly.io, Supabase, Neon and Vercel compared for an app next to managed Postgres.](https://www.prisma.io/blog/app-hosting-platforms-with-managed-postgres-2026)
- [Where to host a TypeScript frontend, a Node API and PostgresHosting a TypeScript frontend, a Node API and their Postgres database from one GitHub repository.](https://www.prisma.io/blog/where-to-host-typescript-frontend-node-api-postgres)
- [Choosing hosting and Postgres after your first 100 paying usersWhat to run the app and the database on once real users arrive.](https://www.prisma.io/blog/choosing-hosting-and-postgres-after-your-first-100-users)
- [Prisma Postgres vs NeonManaged PostgreSQL compared: optional Prisma ORM and Prisma Compute in one project, or Neon Functions, Auth, Object Storage, and AI Gateway.](https://www.prisma.io/compare/neon)
- [Prisma Postgres vs PlanetScaleManaged PostgreSQL compared: optional Prisma ORM and Prisma Compute in one project, or database-first SKUs, Metal, and Neki.](https://www.prisma.io/compare/planetscale)
- [Prisma Postgres vs SupabaseManaged PostgreSQL compared: optional Prisma ORM and Prisma Compute in one project, or Auth, Storage, Realtime, and Edge Functions.](https://www.prisma.io/compare/supabase)
- [Prisma vs Vercel + Neon + DrizzleOne TypeScript platform compared with a host, a database, and an ORM from three providers.](https://www.prisma.io/compare/vercel-neon-drizzle)
- [Neon vs Prisma Postgres for hosting and the database in one placeNeon alternatives when the app and its database should live in one project.](https://www.prisma.io/blog/neon-vs-prisma-postgres-app-hosting-in-one-place)
- [Netlify alternatives for a full-stack TypeScript app with PostgresWhere to move a TypeScript app with Postgres when Netlify stops fitting.](https://www.prisma.io/blog/prisma-vs-netlify)
- [Move a local Postgres database online (2026)Prisma Postgres, Neon, Render, Railway and Supabase compared for taking a laptop Postgres database online with pg\_dump and pg\_restore.](https://www.prisma.io/blog/from-local-to-production-with-prisma-postgres)
- [Migrate a local Postgres database to Prisma PostgresThe docs guide for copying a local PostgreSQL database into Prisma Postgres with pg\_dump and pg\_restore over the direct connection.](https://www.prisma.io/docs/postgres/import-from-existing-database)

## FAQ

[how to host a test version of your app without replacing production](https://www.prisma.io/blog/host-a-test-version-without-replacing-production).

[hosting spending controls](https://www.prisma.io/compute/typescript-hosting-spending-controls)and

[understanding app hosting costs](https://www.prisma.io/compute/typescript-hosting-cost-visibility).

## One platform. Both layers. Features only possible because of it.

Compute is part of a TypeScript stack where hosting and the database travel as a unit: preview them together, deploy them together, debug them together.

- Built to host the agents you're building, not just the apps
- A preview per feature branch, app and database together
- App next to its database, in one project
- Trusted by 500,000+ developers · 46,500+ GitHub stars