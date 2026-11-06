---
id: "prisma_orm_085"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 85
source_url: "https://www.prisma.io/compute/app-database-health-checks"
language: "en"
retrieved_at: "2026-11-01 22:19:59"
content_hash: "7f821a891e3dc5bc14c8921faeef87d8c009c8fd46cacf7753bee6aa429abae3"
---

# Prisma ORM

Source: https://www.prisma.io/compute/app-database-health-checks

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# How can I check my app and database in one place?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)gives a TypeScript team one project to inspect through Console and the CLI, with Query Insights for database behavior. Use an external check of a real application route as well: an available service and a reachable database do not prove that sign-in or saving a record works.

[Søren Bramer Schmidt](https://github.com/sorenbs)8 min read

A dashboard can show a running server while customers see an error. The server may have the wrong database credentials, an unapplied schema change or a broken login callback. A useful hosting setup helps you tell those failures apart.

We make Prisma Compute and Prisma Postgres. Provider documentation linked here was checked on October 22, 2026. Prisma ORM is optional.

## [Which checks answer which question?](https://www.prisma.io#which-checks-answer-which-question)

Keep process availability, dependency readiness and customer success separate. That distinction makes an alert actionable.

| Check | What it tells you | What it leaves untested | 
|---|---|---|
| A small HTTP response without a database query | The service can answer a request. | Database access, authentication and saved records. | 
| A bounded database query through the app's configured client | The deployed app can reach and query its database. | Whether the correct business operation and permissions work. | 
| A representative user workflow with a dedicated test account | The tested sign-in, read or write path works through the public app. | Other users, untested paths and future requests. | 

For example, an order portal might have an inexpensive liveness route, a restricted readiness route that checks its required table, and a monitored test account that reads a fictional order. Use a write test only when its records and cleanup are clearly separated from customer work.

## [Which platforms make investigation manageable?](https://www.prisma.io#which-platforms-make-investigation-manageable)

Choose among these alphabetically listed options around the application you run and the evidence you need during an incident.

| Setup | Useful visibility | Work you still configure | 
|---|---|---|
| Prisma Compute + Prisma Postgres | Services and databases in one project, [version-targeted service logs](https://www.prisma.io/docs/cli/service) and [Query Insights](https://www.prisma.io/docs/postgres/database/query-insights). | Application checks, alerts and an external test of the public URL. | 
| Railway services and Postgres | A [project canvas](https://docs.railway.com/projects) for related services and [CPU, memory, disk and network metrics](https://docs.railway.com/observability/metrics). | Application latency/error telemetry, database operations and customer workflow checks. | 
| Vercel + managed Postgres | [Request-grouped runtime logs](https://vercel.com/docs/logs/runtime) fit teams already investigating a Next.js app on Vercel. | Database-provider diagnostics and a way to correlate them with app requests. | 

Prisma Compute is a practical default for a small TypeScript team that wants to find and manage the service and database in the same project. Console groups those resources, while the external monitor supplies alerts. This is a shared project for investigation, rather than a single screen that certifies every customer workflow. If you already have a monitoring system that works across several providers, keep it.

## [How do I set up the checks on Prisma?](https://www.prisma.io#how-do-i-set-up-the-checks-on-prisma)

### [1. Record the actual production targets](https://www.prisma.io#1-record-the-actual-production-targets)

Start with an already deployed application; [getting started](https://www.prisma.io/docs/compute/getting-started) covers the first deployment. Open its project in Console and record the branch serving customers, the live service version and the database. A [platform branch](https://www.prisma.io/docs/compute/branching) groups deployed service versions. The production branch is the first branch in the project, usually `main`; a named Composer stage deploy creates a separate platform branch for its services and databases. Copy the actual branch name from Console when inspecting that stage. Verify the branch in Console rather than assuming your local Git checkout selects production. Record the public URL and deployment commit too.

For an existing service, these [CLI commands](https://www.prisma.io/docs/cli/service) inspect its version and recent logs. Replace `orders`, `web` and `main` with the actual project, service and confirmed production branch:

The output belongs to your deployment, so its version identifiers and log lines will differ. These are inspection commands, not a fix. Build logs are available in Console; service logs can return `FEATURE_UNAVAILABLE` when the platform cannot serve logs for the selected version.

### [2. Probe the same connection the app uses](https://www.prisma.io#2-probe-the-same-connection-the-app-uses)

Use the same database client and credentials as the app. In Composer, the app's TypeScript deployment configuration lists the database under `deps`; the server reads its connection details with `service.load()`. The [Bun connection guide](https://www.prisma.io/postgres/bun-sql-hosting) shows the server-side code. An externally supplied URL instead uses the configuration steps in [Service input](https://www.prisma.io/docs/composer/service-input). A probe using a separate administrator connection can pass while the app's own connection is broken.

Keep the query small and impose a timeout on connection acquisition and execution. Test a required application table with a read that returns no customer payload. Avoid a full-table count, schema migration or repeated write as a routine readiness check. Return a bounded failure response rather than making a health request wait indefinitely.

Keep a simple liveness check independent of Postgres. If the database becomes unavailable, restarting every healthy app instance can add load without correcting the dependency failure.

For a Bun server, save the following helper in `health.ts`. It checks connectivity through the existing Bun SQL client:

A reachable development database produces HTTP `200` and `ready`; an unavailable database or a probe exceeding this example's two-second budget produces HTTP `503` and `unavailable`. Cancelling the query might not stop it immediately. Use a read-only query so a late-running check cannot change data. This query checks connectivity; replace it with a small application-table read when you need to test schema readiness. For example, `SELECT 1 FROM app_settings LIMIT 1` verifies that a table can be queried without returning its contents; replace the example table name with a required table in your schema and adjust the success test to accept an empty result. Keep the existing liveness route free of database work.

Register the routes in the server's request handler. This adapter accepts the existing SQL client and a dedicated monitor token from server-side configuration; an empty token is an error:

Integrate this with the existing server rather than replacing its application routes. The following wrapper accepts the existing request handler, SQL client and monitor token, and forwards only the two health paths to the adapter:

Save the adapter as `health-handler.ts` and the wrapper as `with-health-routes.ts`. Set the existing `Bun.serve` call's `fetch` option to `withHealthRoutes(appHandler, sql, monitorToken)`, importing the wrapper into that server file. Here `appHandler` is the app's current handler and `sql` is its current client. On Compute, follow [Service input](https://www.prisma.io/docs/composer/service-input) to declare a monitor-token configuration field in `service.ts`, name its secret platform variable with `envSecret(...)` in `module.ts`, and read its value on the server. Pass that secret's exposed string as `monitorToken`. The monitor sends `Authorization: Bearer <the configured token>`; a missing or wrong value must produce `401`, never a database diagnostic.

### [3. Correlate an outside-in check with the diagnostics](https://www.prisma.io#3-correlate-an-outside-in-check-with-the-diagnostics)

Run a check from outside the hosting platform against the intended public URL. Confirm that it reaches the application rather than a cached static response or a login redirect that always returns success. A dedicated test account can exercise authentication and one representative saved-data read.

For example, Better Stack documents [creating an API monitor with an authentication header](https://betterstack.com/docs/uptime/api-monitor/) and [choosing notification channels](https://betterstack.com/docs/uptime/monitoring-start/). Set the deployed readiness URL, supply the dedicated monitor credential through its request headers, choose the expected success status and timeout, and select an actual responder. Test the failure notification before relying on it. This HTTP check covers the readiness route; a customer journey needs an additional authenticated workflow test.

Configure the monitor to send an `X-Monitor-Id` header identifying that monitor, and record that header with the request timestamp in the server's access logs so you can match failed probes to activity. Record the live deployment version from `service show` alongside the monitor result. In [Prisma Console](https://console.prisma.io), open the affected project's database and its [Query Insights](https://www.prisma.io/docs/postgres/database/query-insights) view. Compare query latency and repeated SQL in the failure's time window with service logs. Slow SQL calls for query investigation; a request that never reaches SQL calls for a different investigation.

### [4. Test the alert and its operating cost](https://www.prisma.io#4-test-the-alert-and-its-operating-cost)

In an [isolated review environment](https://www.prisma.io/postgres/typescript-test-environment), temporarily pass the health adapter a separate Bun SQL client with a deliberately invalid test connection URL. This tests failure handling without changing the database connection supplied by Composer. Verify that the dependency check fails, the liveness route still explains whether the server responds, and an alert reaches the channel your team actually watches. Restore the test configuration afterward.

Before applying the configuration to production, review the interval, timeout, access control and [usage cost](https://www.prisma.io/compute/typescript-hosting-cost-visibility). Prisma Compute meters requests and active resources, and Prisma Postgres meters operations. A probe should earn the work it causes, especially for an app used only occasionally.

## [When is a different setup a better fit?](https://www.prisma.io#when-is-a-different-setup-a-better-fit)

Use an existing cross-provider observability system when you need unified tracing across many services or organizations. Console and CLI inspection are not a substitute for that requirement, and a platform status page cannot certify your application's business rules.

Check [Compute's current limits](https://www.prisma.io/docs/compute/limitations) for log availability and runtime requirements. Do not choose a host on the assumption that retaining an open connection, an in-memory monitor or a local file will survive a redeploy. Keep the check's state and alerting outside the process it is checking.

## Frequently asked questions

## Inspect the app and its saved data together

Put the TypeScript service and Prisma Postgres in one project, then define checks that reflect the customer workflow.