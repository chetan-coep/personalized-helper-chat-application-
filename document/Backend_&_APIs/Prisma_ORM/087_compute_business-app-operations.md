---
id: "prisma_orm_087"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 87
source_url: "https://www.prisma.io/compute/business-app-operations"
language: "en"
retrieved_at: "2026-11-01 22:20:01"
content_hash: "135210851d8ee8ef01fa4d5c4157078b94e3c63b1ed8b63d4282638ef356674d"
---

# Prisma ORM

Source: https://www.prisma.io/compute/business-app-operations

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# What hosting can I manage for an AI-built business app without a full-time developer?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)is a practical fit for an AI-built TypeScript business app because its services and database live in one project, with a Console and CLI your assistant can help inspect. You can manage routine operations as the owner, but the application still needs someone responsible for authentication, code changes and recovery.

The first question is what you expect to manage. Checking a live URL, reviewing a bill and approving a tested release are reasonable owner tasks. Diagnosing an authorization flaw or recovering corrupted business records may need experienced technical help. A managed platform removes server administration from that list, while application ownership stays with the business.

We make Prisma Compute and Prisma Postgres. The vendor sources linked below were checked on October 20, 2026. This guide is for an existing TypeScript app; it does not assume that hosting turns custom software into a maintained business product.

## [What should the platform take care of?](https://www.prisma.io#what-should-the-platform-take-care-of)

Look for a repeatable deployment process, an identifiable live version, accessible logs and a managed database. Keep the hosting account, source repository, domain and billing under business-controlled ownership. A contractor's personal account should not be the only route to your customer records.

Your assistant should be able to explain how the app is built, where data is saved and how a release is checked. Put the deployment declaration and migrations in the repository so future help can inspect them. Store credentials in a password manager and server-side secret configuration, with a recovery path that survives someone's departure.

## [Which hosting approach fits this situation?](https://www.prisma.io#which-hosting-approach-fits-this-situation)

These app hosts are ordered alphabetically. All require you to maintain your own application code.

| Approach | Good fit | Owner's next check | 
|---|---|---|
| Netlify + managed Postgres | An existing app already uses its [Git deployments and framework integration](https://docs.netlify.com/deploy/deploy-overview/). | Confirm who owns the database account and how server functions receive its credentials. | 
| Prisma Compute + Prisma Postgres | A TypeScript app whose server and database you want in one project, inspectable through [Console and CLI](https://www.prisma.io/docs/compute/getting-started). | Have the app's Composer declaration, environment inputs and recovery procedure explained at handoff. | 
| Vercel + managed Postgres | A Next.js app already built around [Vercel's deployment workflow](https://vercel.com/docs/deployments). | Verify access to production deployments and the separate database's backups and billing. | 

Prisma Compute gives a small team a concrete TypeScript deployment definition for its agent to read and change. Prisma Postgres accepts ordinary PostgreSQL clients, so an existing app can keep its database library. For an owner who wants a finished tool maintained by its vendor, compare a hosted business application or a supported app builder instead of starting with a custom repository.

## [How do I make the Prisma setup manageable?](https://www.prisma.io#how-do-i-make-the-prisma-setup-manageable)

### [1. Establish ownership and a release boundary](https://www.prisma.io#1-establish-ownership-and-a-release-boundary)

Use [getting started](https://www.prisma.io/docs/compute/getting-started) to prepare a Composer app and a managed database. Ask whoever prepares the app to demonstrate the build, an [isolated review deployment](https://www.prisma.io/docs/composer/deploying#production-and-stages) using a named stage such as `--stage review`, and a separate production release. Define which changes you can approve yourself and who handles failures you cannot diagnose.

Keep reviews on [separate test data](https://www.prisma.io/postgres/typescript-test-environment). If the app receives a manually supplied database URL, configure the test and production values separately. A test deployment connected to the production database can still change customer records.

### [2. Keep a short operations record](https://www.prisma.io#2-keep-a-short-operations-record)

Record the project, production branch, service name, live URL, database identity and the repository commit for the current release. Add a representative business test, such as signing in and saving a fictional booking, plus its cleanup procedure. Record where errors go and who can help; do not paste secret values into this document.

After CLI login using the current [supported runtime](https://www.prisma.io/docs/compute/limitations#cli), the owner or assistant can inspect an existing project:

Here `business-portal`, `main` and `web` stand for your actual project, confirmed production branch and service name returned by the list. These commands inspect resources; they do not deploy or write customer data. The [service reference](https://www.prisma.io/docs/cli/service) explains the returned live-version details. Use `@latest` deliberately for the hosting CLI; it does not require upgrading the app's installed ORM.

### [3. Decide what recovery means](https://www.prisma.io#3-decide-what-recovery-means)

Set a tolerable amount of lost work and a tolerable recovery time. A database snapshot from yesterday may be unacceptable if today's orders cannot be reconstructed. Prisma Postgres [backups](https://www.prisma.io/docs/postgres/database/backups) depend on the plan, and point-in-time recovery is not available until November 2026. Choose the provider and plan around the business requirement.

Rehearse restoration into a separate database and check that the application can read it. Keep exports where appropriate, and verify that the business can reach the credentials needed to recover. A backup entry in a dashboard is less useful than a restoration procedure someone has tested.

### [4. Review usage and changes regularly](https://www.prisma.io#4-review-usage-and-changes-regularly)

Use the current [pricing and plan limits](https://www.prisma.io/pricing) to set a budget, and understand what happens when a limit stops service. Paid-plan spending controls and free-plan quotas protect different things; neither proves that the app will stay available under every workload.

Review failed requests, dependency updates and access changes as part of operating the app. Test updates before release and retain the previous working version and its compatible schema. The [deployment handoff guide](https://www.prisma.io/compute/deployment-handoff-checks) gives a practical acceptance check.

For checks that distinguish a running process from a working customer flow, use the [app and database health guide](https://www.prisma.io/compute/app-database-health-checks). It connects service inspection, bounded database checks and an external test of the public app.

## [When is this the wrong setup?](https://www.prisma.io#when-is-this-the-wrong-setup)

Choose a maintained business product if you need someone else to own both hosting and the application's ongoing behavior. An AI assistant can help with the work, but it does not create an accountable maintainer or guarantee that a proposed fix is correct.

Also check the [Compute runtime limits](https://www.prisma.io/docs/compute/limitations). Deployed services run on Bun; WebSocket servers and a persistent writable filesystem are unsupported, and each service runs in one region. Keep Prisma Postgres with another app host when that host better fits a required runtime or operating workflow.

Before relying on the backup policy, [practice restoring a hosted Postgres database](https://www.prisma.io/postgres/practice-database-recovery) into an isolated target and verify the application against the recovered records.

## Frequently asked questions

## Keep the app understandable after launch

Use one project for your TypeScript app and Postgres, then record the ownership, release and recovery steps the business needs.