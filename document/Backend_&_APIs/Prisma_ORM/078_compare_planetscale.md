---
id: "prisma_orm_078"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 78
source_url: "https://www.prisma.io/compare/planetscale"
language: "en"
retrieved_at: "2026-11-01 22:19:48"
content_hash: "70a462ffdc6744baeec57840c364c346d2e77264d21607ba992d0e24460ed7c8"
---

# Prisma ORM

Source: https://www.prisma.io/compare/planetscale

---

[Compare](https://www.prisma.io/compare)PlanetScale

# Prisma Postgres vs PlanetScale: TypeScript app hosting or database-first Postgres?

Pick [Prisma Postgres](https://www.prisma.io/docs/postgres) when you want managed PostgreSQL with [Prisma ORM](https://www.prisma.io/docs/orm) optional, and [Prisma Compute](https://www.prisma.io/docs/compute) hosting the TypeScript app as HTTP services in the same Prisma project. Pick [PlanetScale](https://planetscale.com/pricing) when you want database-first Postgres SKUs, Metal, high availability, or Neki, with application hosting on another provider.

[Get started with Prisma Postgres](https://console.prisma.io) [Create an instant database](https://create-db.prisma.io/web)

By [Martin Janse van Rensburg](https://www.prisma.io/blog/author/martin-janse-van-rensburg) · Updated  · 8 min read[X](https://x.com/vanrensbird)[LinkedIn](https://www.linkedin.com/in/martjvr/)[GitHub](https://github.com/vanrensbird)

Prisma makes Prisma Postgres. PlanetScale figures come from the pages listed under [Sources](https://www.prisma.io#sources), checked October 2026.

## When should I choose PlanetScale or Prisma Postgres?

| PlanetScale | Prisma Postgres | 
|---|---|
| You want a database-first Postgres SKU, with application hosting on another provider. | You want [Prisma ORM](https://www.prisma.io/docs/orm) available on the same platform as the database. Prisma ORM is optional; any Postgres client works. | 
| You want high-availability Postgres with one primary and two replicas across three availability zones, or Metal with local NVMe. | You want [Prisma Compute](https://www.prisma.io/docs/compute) to host the TypeScript app as HTTP services next to [Prisma Postgres](https://www.prisma.io/docs/postgres). | 
| You want PlanetScale database branches as isolated database deployments, billed as their own clusters. | You want a [preview branch](https://www.prisma.io/docs/compute/branching) that can own its app services and database. | 
| You want horizontally sharded Postgres with Neki, currently in platform preview, and you accept that PlanetScale says not to run production on it during the preview. | You want a [$0 free plan](https://www.prisma.io/postgres/free-postgresql-hosting) with no credit card, then operation-based pricing with spend limits on paid plans. | 

## How do PlanetScale and Prisma Postgres compare?

PlanetScale and Prisma Postgres are both managed PostgreSQL. PlanetScale sells database-first cluster SKUs, including Metal and Neki. Prisma Postgres sits next to an optional ORM and Prisma Compute. Columns are in alphabetical order.

| Feature | PlanetScale | Prisma Postgres | 
|---|---|---|
| Database | Managed PostgreSQL with branching and connection pooling. Single-node instances start at $5 a month. HA is one primary and two replicas. Metal uses local NVMe. | [Prisma Postgres](https://www.prisma.io/docs/postgres) is managed PostgreSQL that autoscales, with no instance to size or upgrade. Any Postgres client works with it, so Prisma ORM is optional. | 
| ORM on the same platform | No first-party ORM. Teams pick an external ORM or SQL client. | [Prisma ORM](https://www.prisma.io/docs/orm) is a first-party type-safe ORM on the same platform. It is optional. | 
| App hosting | Application hosting stays with another provider. PlanetScale is the database. | [Prisma Compute](https://www.prisma.io/docs/compute) hosts the TypeScript app as HTTP services. It is separate from Prisma Postgres. Compute has no built-in cron scheduler. WebSocket servers are not supported. | 
| Branches and previews | A PlanetScale Postgres branch is an isolated database deployment. There is no data replication between branches. Branches created from the Branches page start as PS-DEV at $5 a month and do not copy schema or data. Restore from a backup to include schema and data. | A Prisma [preview branch](https://www.prisma.io/docs/compute/branching) can own its Compute services and databases. Production data is not copied into that database. | 
| Free plan | No $0 Postgres plan. Single-node Postgres instances start at $5 a month. | Prisma Postgres Free is $0. No credit card required. 200,000 operations a month, 2 GB of storage, and 50 databases. | 
| Database pricing model | Resource-based SKUs: cluster size, storage, backups, and network usage. Prices on the pricing page are AWS us-east-1 and vary by region. | Operations plus storage, with spend limits on paid plans. Starter is $10 a month with 1 million operations and 10 GB included. | 
| Horizontal Postgres sharding | Neki is horizontally sharded Postgres, in platform preview as of September 2026. PlanetScale says not to run production workloads on Neki during the preview. Neki has no single-node configuration. | Standard PostgreSQL. No first-party horizontal sharding product. | 

## Where does each one fit?

### PlanetScale

PlanetScale is a database-first Postgres platform. Its [pricing page](https://planetscale.com/pricing) lists single-node, high-availability, and Metal SKUs, plus Neki for horizontally sharded Postgres. Application hosting stays with another provider.

- The database should be a PlanetScale Postgres SKU, with the app on another host.
- High availability should be one primary and two replicas, or Metal with local NVMe from $50 a month.
- Database branches should be isolated clusters, billed separately, without copying production data by default.
- Horizontally sharded Postgres with Neki is acceptable as a platform preview, not production.

### Prisma Postgres

Prisma Postgres fits a team that wants PostgreSQL next to the TypeScript app. [Prisma ORM](https://www.prisma.io/docs/orm) is optional. [Prisma Compute](https://www.prisma.io/docs/compute) is separate app hosting in the same Prisma project.

- The database should be PostgreSQL, with SQL and the Postgres ecosystem.
- Prisma ORM should be available, and optional, on that database.
- The TypeScript app should deploy as HTTP services on Prisma Compute, in the same Prisma project as the database.
- The database should have a $0 free plan, then operations and storage with spend limits on paid plans.

## What does Prisma Postgres do that PlanetScale doesn't?

### A first-party ORM, when you want one

Prisma ORM is a type-safe data layer on the same platform as Prisma Postgres. It is optional. You can skip it and use SQL or another Postgres client.

### Full TypeScript app hosting

Prisma Compute hosts the TypeScript app as HTTP services next to Prisma Postgres. The current release focuses on HTTP. WebSocket servers are not supported. Compute has no built-in cron scheduler.

### App and database on a preview branch

A Prisma preview branch can own its application services, deployments, and Prisma Postgres databases. Production data is not copied into that database. See [Compute branching](https://www.prisma.io/docs/compute/branching).

### A $0 free plan

Prisma Postgres Free is $0, with no credit card. PlanetScale Postgres single-node instances start at $5 a month. There is no $0 PlanetScale Postgres SKU on the pricing page checked October 2026.

## How much do PlanetScale and Prisma Postgres cost?

| Cost | PlanetScale | Prisma Postgres | 
|---|---|---|
| Lowest listed Postgres price | Single-node PS-5 is $5 a month on AWS us-east-1. There is no $0 Postgres plan. | Prisma Postgres Free is $0. No credit card required. 200,000 operations a month, 2 GB of storage, and 50 databases. | 
| High availability | HA Postgres is one primary and two replicas. PS-5 HA is $15 a month on AWS us-east-1. | Starter $10, Pro $49, Business $129 a month for Prisma Postgres and Prisma Compute. | 
| Metal | Postgres Metal starts at $50 a month for M-10 arm64 with 10 GiB included NVMe on AWS us-east-1. Storage is in the SKU rate. | No Metal SKU. Storage is billed by gigabyte on paid plans after the included amount. | 
| Neki | Horizontally sharded Postgres in platform preview. No single-node SKU. Network-attached Neki starts at $30 a month per shard (PS-10 arm64 HA) plus routers, storage, backups, and network. PlanetScale says not to run production on it during the preview. | Not offered. Prisma Postgres is standard PostgreSQL. | 

Prisma Postgres has a Free plan: $0 a month for 200,000 operations, 2 GB of storage, and 50 databases. No credit card required. The [pricing page](https://www.prisma.io/pricing) lists the paid plans. PlanetScale single-node Postgres starts at $5 a month on AWS us-east-1. There is no $0 Postgres SKU ([PlanetScale pricing](https://planetscale.com/pricing), October 2026). For health data, Business at $129 a month includes [HIPAA compliant Postgres](https://www.prisma.io/postgres/hipaa) with a signed BAA, plus SOC 2 Type II and ISO 27001.

## When is Prisma Postgres the wrong choice?

- You want database-first SKUs, Metal NVMe, or HA across three availability zones as the product. Prisma Postgres does not sell those cluster sizes. See [PlanetScale pricing](https://planetscale.com/pricing).
- You want horizontally sharded Postgres. Neki is PlanetScale's product for that, in platform preview. Prisma Postgres is standard PostgreSQL. PlanetScale says not to run production on Neki during the preview. See [Introducing Neki](https://planetscale.com/blog/introducing-neki).
- You want the database on PlanetScale and the app on another host, and a $5 cluster is acceptable because you do not need a $0 database plan.

## How do I switch from PlanetScale to Prisma Postgres?

1. Create an empty Prisma Postgres database. Prisma ORM is optional. The [import from an existing database](https://www.prisma.io/docs/postgres/import-from-existing-database) guide uses `pg_dump` and `pg_restore` over the direct connection.
2. Dump PlanetScale Postgres with a direct (non-PgBouncer) connection string, then restore into Prisma Postgres. The dump copies PostgreSQL schemas and data. It does not reproduce PlanetScale branch history, Metal SKUs, or a Neki shard topology.
3. Point the app at the Prisma Postgres connection string. Host the HTTP app on Prisma Compute, or keep the host you already use.

## How do I switch from Prisma Postgres to PlanetScale?

1. Create a PlanetScale Postgres cluster and dump Prisma Postgres with `pg_dump` over the direct connection, then restore into PlanetScale. Both sides are PostgreSQL.
2. Point the app at the PlanetScale connection string. Keep using SQL or an ORM; PlanetScale has no first-party ORM.
3. Keep application hosting on a separate provider. Prisma Postgres stays in place until you stop using it.

## What do teams say about Prisma Postgres?

Two teams on what Prisma ORM and Prisma Postgres do for them.

## Frequently asked questions

[PlanetScale pricing](https://planetscale.com/pricing)and

[Prisma pricing](https://www.prisma.io/pricing), October 2026.

[Prisma Postgres](https://www.prisma.io/docs/postgres), October 2026.

[PlanetScale pricing](https://planetscale.com/pricing)and

[Prisma Compute](https://www.prisma.io/docs/compute), October 2026.

[Introducing Neki](https://planetscale.com/blog/introducing-neki)and

[PlanetScale pricing](https://planetscale.com/pricing), October 2026.

[PlanetScale Postgres branching](https://planetscale.com/docs/postgres/branching), October 2026.

## Ready to build with Prisma?

Free to start, no credit card required.

Prisma ORM is free and open source, and always will be.

- Create a database and start building in minutes
- Read the docs for guides and API reference
- Trusted by 500K+ developers globally

Need a database? [Create an instant database](https://create-db.prisma.io/web).

## Sources

Every competitor figure on this page comes from these pages, checked October 2026.