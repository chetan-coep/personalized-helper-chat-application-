---
id: "prisma_orm_084"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 84
source_url: "https://www.prisma.io/compute/ai-usage-credits"
language: "en"
retrieved_at: "2026-11-01 22:19:57"
content_hash: "a65efdfd7a3914977bc17d1aaa5d180ae9e97365467450e7eba7c11fcd2289c9"
---

# Prisma ORM

Source: https://www.prisma.io/compute/ai-usage-credits

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# How should I host an AI API that charges credits?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)fits a small team that wants its API, saved usage and deployment configuration in one project. Vercel or Netlify with Prisma Postgres can also fit an existing app. The host runs the API; your application must define reservations, retries, settlement and customer-visible balances.

A customer with ten credits can send two requests at the same time. If both handlers read ten and each decides to spend seven, a check in application memory can approve work the balance cannot cover. Choose the hosting workflow you like, then enforce admission in the database.

We make Prisma Compute and Prisma Postgres. Provider and PostgreSQL sources linked here were checked on October 22, 2026.

## [What must the setup keep reliable?](https://www.prisma.io#what-must-the-setup-keep-reliable)

Keep an account balance, a history of credit changes and a record for each logical AI request. The history explains the balance; the request record explains whether work is reserved, running, completed or awaiting reconciliation. Keep model usage and the pricing rule used for the charge with that record.

Derive the account from verified authentication and calculate the charge on the server. A browser or model response must not choose the account balance or its own price. An AI assistant can write the implementation, but tests must prove its behavior with concurrent requests, retries and failures.

Separate the prices you charge customers from the [infrastructure meters](https://www.prisma.io/compute/typescript-hosting-cost-visibility). A model request can cause several database queries and an app response. Those costs need their own budget even when the customer's credit price is fixed.

## [Which app host should I choose?](https://www.prisma.io#which-app-host-should-i-choose)

These options are alphabetical by app host and can use Prisma Postgres.

| Setup | Useful fit | Decision your application owns | 
|---|---|---|
| Netlify + Prisma Postgres | An app already using [Netlify's function workflow](https://docs.netlify.com/build/functions/overview/). | Credit admission, request state and recovery after a function stops. | 
| Prisma Compute + Prisma Postgres | A TypeScript API and its database described together through [Prisma Composer](https://www.prisma.io/docs/composer). | Transactions, model-call deadlines and settlement of unfinished requests. | 
| Vercel + Prisma Postgres | A Next.js app already using [Vercel's server functions](https://vercel.com/docs/functions). | Credential scope, concurrency and the same credit accounting rules. | 

For a new TypeScript API, Compute gives the team a deployment declaration its coding agent can inspect while Postgres keeps balances outside the running process. Keep a working app host when its deployment workflow already suits the product.

## [How do I build the Prisma setup?](https://www.prisma.io#how-do-i-build-the-prisma-setup)

### [1. Create a separate development ledger](https://www.prisma.io#1-create-a-separate-development-ledger)

Create a development Prisma Postgres database in [Console](https://console.prisma.io). Use fictional accounts and credits, separate from live customers. Prisma ORM is optional.

Apply schema migrations through the database's [direct connection](https://www.prisma.io/docs/postgres/database/connecting-to-your-database). Use its pooled URL for ordinary TCP application connections; the [Prisma Postgres serverless driver](https://www.prisma.io/docs/postgres/database/serverless-driver) requires the direct URL. Define constraints for nonnegative balances, valid request states and unique account/request identifiers.

### [2. Prove the conditional balance change](https://www.prisma.io#2-prove-the-conditional-balance-change)

With `psql` installed, open a direct connection to the development database. Paste this SQL into one session:

The first update returns `remaining = 3`; another seven-credit debit then returns no rows. PostgreSQL rechecks an update's condition after a competing writer commits under its [default isolation level](https://www.postgresql.org/docs/17/transaction-iso.html).

This demonstrates one admission rule, not a complete credit ledger. The second update is another debit attempt, not a deduplicated retry. Production code needs saved request identifiers, transaction boundaries and a policy for database errors. The temporary table disappears when the session ends.

### [3. Reserve, call the model and settle](https://www.prisma.io#3-reserve-call-the-model-and-settle)

For an implemented ledger, make the sequence explicit:

1. Authenticate the account and assign or reuse the logical request ID.
2. Start a transaction, lock the account's wallet row, and look up the request by account and request ID. If it exists, compare the validated inputs and any client-requested credit limit with its saved inputs or fingerprint; reject a mismatch. For a matching retry, end the transaction and return the saved state under its original pricing rules. For a new request, check the balance and persist the validated inputs and model/work limits, or an immutable durable reference to them. Save a canonical fingerprint and the server-decided credit amount and pricing version, reserve the credits, mark the request reserved and add its credit-history entry in that same transaction, then commit. Roll back a rejected request.
3. Atomically claim the reserved request by changing its state to running, and commit that change before submitting it to the model. Only the process that won this transition may submit the call. Make the call outside the transaction with a deadline, and save the provider request identifier when it becomes available.
4. In a new transaction, conditionally change the request from an allowed unfinished state to its final state. Only the transaction that wins this transition may apply the settlement or release to the wallet and add the corresponding credit-history entry; commit those changes together. A retry that finds a final request returns its saved result, while other invalid transitions are rejected.

When a model call times out, its outcome may be uncertain. Keep that request in a state your reconciliation process can inspect rather than immediately refunding and sending the same expensive work again. A database transaction cannot make an external API call happen exactly once.

Deploy a recovery worker that periodically finds reservations whose processing deadline has passed. A still-reserved request can be claimed through the same atomic transition. An expired running request is uncertain until the provider confirms its outcome, even when no provider identifier was saved: the process may have stopped after submission. Do not automatically release its credits or resubmit it. Check the provider's result or usage records when available; otherwise hold the reservation for an explicit review policy. The [Postgres worker guide](https://www.prisma.io/blog/you-dont-need-a-job-queue-postgres-already-has-skip-locked#where-to-run-the-worker) explains the always-on host needed for a polling process. Saving a reservation alone does not schedule its recovery.

For variable-cost work, reserve an explicit upper bound and enforce the corresponding model-output or work limit. Define what happens when a request reaches it. Fixed-price credits need a different settlement rule from pass-through token pricing.

### [4. Deploy and test the whole request lifecycle](https://www.prisma.io#4-deploy-and-test-the-whole-request-lifecycle)

Follow [Compute getting started](https://www.prisma.io/docs/compute/getting-started), or [port the existing API](https://www.prisma.io/docs/composer/porting-an-app), to configure the server and its inputs. Keep model keys in server-side secret configuration.

A database created by a Composer module is separate from a Console-created development database. Prepare every review and production target through the [migration workflow](https://www.prisma.io/postgres/production-database-migrations) before serving customer work. A configured `postgres()` data contract can apply migrations during deployment; `rawPostgres()` and manually supplied URLs require your own migration step.

Test simultaneous requests, repeated IDs, insufficient credits, a model failure, a timeout after success and a process restart between reservation and settlement. An API response and the customer's usage screen should agree with the saved request state.

## [When should I choose another setup?](https://www.prisma.io#when-should-i-choose-another-setup)

Choose a billing service if you need an existing product to own subscriptions, credit expiry or invoicing rules. If Stripe funds the wallet, verify payment events and deduplicate top-ups; the [Stripe hosting guide](https://www.prisma.io/compute/nextjs-stripe-subscriptions) covers that boundary.

Compute has [60 seconds to start a response](https://www.prisma.io/docs/compute/request-timeout). Long-running requests need a suitable durable worker design, not an in-memory promise treated as a queue. Check the runtime and recovery requirements before selecting the worker host. Prisma Postgres has [automatic snapshots on paid plans, created daily on days with database activity](https://www.prisma.io/docs/postgres/database/backups), with no point-in-time recovery yet (it is coming in November 2026); choose another database if you need that recovery window today.

## Frequently asked questions

## Keep usage decisions beside the API

Run the TypeScript API on Compute and save credit decisions in Prisma Postgres, with separate test balances before charging customers.