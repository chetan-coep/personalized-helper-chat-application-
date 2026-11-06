---
id: "prisma_orm_001"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 1
source_url: "https://www.prisma.io"
language: "en"
retrieved_at: "2026-11-01 22:18:06"
content_hash: "01f30ad921262ccee133479b1a7691bf9e4e9222e6b00f09861e7dc2f16b1134"
---

# Prisma ORM

Source: https://www.prisma.io

---

# Your TypeScript app, from prompt to production

Give your coding agent a type-safe ORM, managed Postgres, and app hosting that work together natively. One shared context across your stack is all your agent needs to build, deploy, and iterate without coordinating between vendors.

- One platform, one stack, one bill
- A CLI and API your agent drives natively
- The ORM is free, always

Trusted by 500,000+ developers46,500+ GitHub stars

Trusted by leading companies

## The stack your agent has been waiting for

### Before

- A database from Neon, an ORM from Drizzle, hosting from Vercel
- Your agent writes the code, you wire it up
- Preview databases from one vendor, preview deployments from another
- Bandwidth bills that scale faster than your traffic
- Context-switching between a database dashboard, ORM CLI, hosting console, and data browser

### After

- Your agent runs the full loop: build, deploy, debug, fix, redeploy
- One platform: hosting, database, and ORM built to work together natively
- A preview database per feature branch, wired to its preview deployment
- App and database on one platform in the same region, so queries stay low-latency and never leave the region
- Spend limits on every paid tier, so your bill stops where you tell it to

## Ship a production TypeScript app in three steps

### Define

Write your data model once in `contract.prisma`, or have your agent write it for you. It's the shared contract your ORM, migrations, and data layer are all built around.

### Deploy

Add Prisma Postgres and Compute when you're ready to ship. Your app and database deploy together on one platform, in the same region, in one project.

### Iterate

Your agent reads logs, fixes what broke, and redeploys through one CLI. The loop runs for as long as you need it to.

## The TypeScript stack, integrated by design

ORM, database, and hosting designed to work together, so your agent can build, deploy, and iterate without coordinating between vendors.

Type-safe data layer

### Prisma ORM

A declarative, type-safe schema rebuilt in native TypeScript, the shared contract your whole stack and your agent are built around.

- Schema-as-LLM-context: small, dense, machine-readable
- Errors structured for agent consumption, not just human-readable
- Rebuilt in native TypeScript for the fastest type-checking at scale
- Free, open-source, the foundation 500K+ developers already trust

[Learn more about Prisma ORM](https://www.prisma.io/orm)

`contract.prisma`
*The shared contract across your stack*

Managed database

### Prisma Postgres

Managed Postgres already wired to your schema and co-located with your app hosting, on infrastructure built for single-digit ms boot times.

- Unikernel microVMs on bare metal, single-digit ms boot
- Operation-based pricing with spend limits, no bill shock
- A preview database per feature branch, integrated with hosting previews
- Works with any ORM if you're not using Prisma's
- Query Insights built in: spot slow queries and get an agent-ready prompt to fix them

[Learn more about Prisma Postgres](https://www.prisma.io/postgres)

`prisma.config.ts`
*One config, both products*

App hosting

### Prisma Compute

TypeScript app hosting on the same platform and in the same region as your database, so your agent can deploy, debug, and redeploy end-to-end.

- Bun runtime on bare metal
- Co-located with Prisma Postgres, single-digit ms query latency
- Long-running workloads: WebSockets, cron, background jobs *(coming soon)*
- Versioned deployments with preview URLs, [deploy by git push](https://www.prisma.io/docs/compute/deploy-on-push) or CLI

[Learn more about Prisma Compute](https://www.prisma.io/compute)

### Working across the stack

#### Prisma Studio

*to inspect your data*

Visual data browser and editor built into the Console. See what your agent did to your database, collaborate with teammates without SQL, embeddable in your own apps.

[Learn more about Prisma Studio](https://www.prisma.io/postgres)

#### CLI + Management API

*to stay in the loop*

The agent interface for the full platform. Structured output and `--json` modes everywhere, with full parity between CLI and API so anything your agent can run, it can also call programmatically.

[Learn more about the CLI and Management API](https://www.prisma.io/docs)

## What changes when your stack is built to work together

### Your agent handles the full loop

Build, deploy, debug, redeploy. No vendor coordination.

### One platform, not five glued together

Get your app live without wiring together a database, a host, and an ORM from separate vendors.

### Deploy your app, the database is already there

App and Postgres on one platform, in the same region, in one project.

## Pricing that scales with you

Start free with the ORM, which will always be free. Prisma Postgres has a [free tier](https://www.prisma.io/postgres/free-postgresql-hosting) with a hard cap, so you can build without a credit card. When you outgrow it, you're on operation-based pricing with spend limits, and database data transfer is always included.

- **Free Postgres tier** with a hard cap, no credit card required
- **Spend limits on every paid tier**, so your bill never surprises you
- **Unlimited database data transfer included**, no database egress bill-shock
- **Prisma ORM is free, always**
- **A preview database per feature branch**, no surcharge
- **SOC2, [HIPAA](https://www.prisma.io/postgres/hipaa), ISO 27001, and GDPR** at the Business tier

Typical stack (Neon + Vercel)

$20-35
per month

- Database and hosting from two vendors
- Database data transfer: 5 GB on Neon Free; 500 GB on Launch, then $0.10/GB
- Paid Vercel plan for commercial use

per month

- Free plan needs no credit card
- Database data transfer included
- Hard free-tier cap, no surprises

Typical stack (Neon + Vercel)

$110-270
per month

- Database and hosting from two vendors
- Database data transfer: 500 GB per project included, then $0.10/GB
- Spend controls: Neon notifications, Vercel budget with optional pause

per month

- One bill, one platform
- Database data transfer included
- Hard spend limits you set

## Real teams, real builds

## FAQ

`contract.prisma` is yours, your data sits in standard Postgres, and you can migrate away whenever you want. Migration paths from Prisma to other tools are documented.
## Ready to let your agent run the full loop?

The TypeScript stack 500K+ developers trust. Start with the free ORM, and add the rest of the platform when you need it.

- Built for how your agent ships now
- Postgres and hosting when you need them
- Type-safe ORM, free and always will be