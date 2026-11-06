---
id: "prisma_orm_097"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 97
source_url: "https://www.prisma.io/compute/multi-user-inventory-app"
language: "en"
retrieved_at: "2026-11-01 22:20:17"
content_hash: "f41df3149a51d6f86aa78e4510f4fc67765577dd10d8f33c84861ca5e58aa16d"
---

# Prisma ORM

Source: https://www.prisma.io/compute/multi-user-inventory-app

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# Where should I host a small inventory app used by several staff members?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)fits a small TypeScript team that wants the app and database in one project. Vercel or Netlify can also host the app while Prisma Postgres stores inventory. Keep stock in the database and make a failed or repeated request part of the workflow you test.

Two staff members can both see the last item in stock. Hosting the app makes it available to them, but it does not make a read-then-write stock calculation safe. Put the acceptance rule in the database update so the server can tell one person that the item is no longer available.

We make Prisma Compute and Prisma Postgres. The linked host and PostgreSQL documentation was checked on October 19, 2026. Prisma ORM is optional.

## [What does a shared inventory app need?](https://www.prisma.io#what-does-a-shared-inventory-app-need)

Use one authoritative stock record, individual staff logins and a server that checks which account or location each person may access. Record adjustments with a reason and staff identity when the business needs an audit trail. A shared platform login or a database password distributed to every browser is unnecessary.

Decide whether a click reserves stock, sells it or records a physical count. Those operations have different rules. Also decide what happens if the browser retries a request after losing the response. An app that decrements stock twice for the same sale can be wrong while every SQL statement succeeds.

## [Which app and database hosting setup fits?](https://www.prisma.io#which-app-and-database-hosting-setup-fits)

These options are ordered alphabetically by app host.

| App host | When to choose it | What remains your responsibility | 
|---|---|---|
| Netlify + Prisma Postgres | Your app already uses [Netlify's framework deployment workflow](https://docs.netlify.com/deploy/deploy-overview/). | Deploy server features, configure database access and implement staff permissions. | 
| Prisma Compute + Prisma Postgres | You want the TypeScript app and its database declared in one project. | Configure the module, authentication, migrations and inventory rules. | 
| Vercel + Prisma Postgres | Your Next.js app already uses [Vercel deployments](https://vercel.com/docs/deployments). | Configure the server's database URL and test the actual inventory endpoints. | 

For a new project, Prisma Compute and Prisma Postgres let the team keep deployment and database setup together. Follow the [Composer database guide](https://www.prisma.io/docs/composer/databases) for a declared dependency, or keep an existing PostgreSQL client and configure a separately managed database URL. Place the database-calling server [near the database](https://www.prisma.io/postgres/nodejs-database-regions).

## [How do I set up and verify inventory on Prisma?](https://www.prisma.io#how-do-i-set-up-and-verify-inventory-on-prisma)

### [1. Deploy the existing app with a development database](https://www.prisma.io#1-deploy-the-existing-app-with-a-development-database)

Follow the [framework deployment guide](https://www.prisma.io/docs/prisma-compute/deploy) to prepare the app's Composer module and build. A database dependency named `db` supplies `service.load().db.url`; an existing database URL belongs in a server-side input. Keep development and production separate.

Prisma Compute runs deployed TypeScript services on Bun. Check dependencies against the supported runtime, including any barcode or printer integrations. A staff browser can call HTTP endpoints without needing the database credentials itself.

### [2. Test an atomic stock change](https://www.prisma.io#2-test-an-atomic-stock-change)

In a fresh development database, run this example through its [direct connection](https://www.prisma.io/docs/postgres/database/connecting-to-your-database). Use migrations for the real schema.

The update returns `LAST-ITEM` with quantity `0`. A second staff request running the same update returns no rows. Under PostgreSQL's default Read Committed isolation, an update waiting for a concurrent writer rechecks its condition against the updated row. See the [transaction isolation documentation](https://www.postgresql.org/docs/17/transaction-iso.html).

In application code, derive the business account from the verified staff session. Bind the SKU and requested quantity as parameters, validate that the quantity is a positive integer, and handle a zero-row result explicitly. Do not read a number into the browser and later save a replacement number calculated from that stale value.

### [3. Make a sale more than a stock decrement](https://www.prisma.io#3-make-a-sale-more-than-a-stock-decrement)

If a sale also creates an order, adjustment record or reservation, group the required database changes in one [transaction](https://www.prisma.io/postgres/customer-order-transactions). Add a unique business request identifier so retries can return an existing result instead of decrementing stock twice. The single-statement example above demonstrates the stock boundary, not a complete retry-safe checkout.

Test concurrency using two sessions attempting the last item. Also test a double click, a lost response, a return and a staff account from another business. The UI should preserve the user's intent when a request fails and refresh the stock value after a successful operation.

Remove the demonstration table after those checks:

### [4. Verify the deployed workflow with the business owner](https://www.prisma.io#4-verify-the-deployed-workflow-with-the-business-owner)

Use a separate review environment with fictional products. Confirm that staff can sign in, perform an authorized stock adjustment and see it after refreshing. Verify that another business account cannot read the same SKU merely by knowing its name. Then rehearse the production migration and agree who may deploy changes.

Choose an appropriate [backup plan](https://www.prisma.io/docs/postgres/database/backups) and test recovery before inventory becomes operationally important. Keep exported reports and database recovery procedures with the business, rather than only on the contractor's laptop.

## [When should I choose another setup?](https://www.prisma.io#when-should-i-choose-another-setup)

Offline stock changes require synchronization and conflict rules; hosted Postgres alone does not make an app work without connectivity. Live multi-site inventory may also need reservation and reconciliation logic beyond a single counter.

Prisma Compute currently has no WebSocket server support or persistent writable filesystem. Choose another app host if those are requirements, or use HTTP updates and durable external storage. Prisma Postgres has plan-dependent snapshots and no point-in-time recovery yet (it is coming in November 2026); choose another database provider if your recovery requirement needs it today.

## Frequently asked questions

## Put the shared inventory behind one server

Deploy the TypeScript app on Prisma Compute with Prisma Postgres and verify concurrent staff updates before moving the business workflow.