---
id: "prisma_orm_092"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 92
source_url: "https://www.prisma.io/compute/discord-slack-bot-postgres"
language: "en"
retrieved_at: "2026-11-01 22:20:08"
content_hash: "d0aa082315ce84a796d86c0d405e0eb192ff5e5e2e5d68815f0b126fcb7dd9f6"
---

# Prisma ORM

Source: https://www.prisma.io/compute/discord-slack-bot-postgres

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# Where can I host a TypeScript bot with Postgres?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)is a useful starting point: declare the TypeScript service and database together, then deploy and inspect them from the same project. For a Discord Gateway bot or a Slack Socket Mode app, choose a host with a documented continuously running process, such as Render's background workers. The database can still be Prisma Postgres.

[Søren Bramer Schmidt](https://github.com/sorenbs)7 min read

A support bot might receive a slash command, save a ticket and return a reference number. A moderation bot might need a continuous stream of server events. Both can use TypeScript and Postgres, but their hosting requirements differ.

We make Prisma Compute and Prisma Postgres. The official sources linked here were checked on October 29, 2026. This guide compares hosting models; it does not assume that every library called a bot runs the same way.

## [Does your bot receive HTTP requests or maintain a connection?](https://www.prisma.io#does-your-bot-receive-http-requests-or-maintain-a-connection)

Start with the bot's event delivery. [Discord interactions](https://docs.discord.com/developers/interactions/receiving-and-responding) can arrive through an HTTP endpoint or the Gateway. Those are alternative delivery methods for interactions. Receiving application commands over HTTP does not provide every Gateway event.

Slack's [HTTP Events API](https://docs.slack.dev/apis/events-api/) sends requests to your server, while [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode/) establishes an outbound WebSocket connection. Socket Mode needs connection refresh and reconnect handling, even when no user is issuing a command.

Inspect the library configuration with your coding assistant. A public request URL and an HTTP handler point toward a web service. Gateway login, heartbeats or a Socket Mode client point toward a continuously running process. A TypeScript runtime match by itself does not establish that the host will keep that process connected.

## [Which hosting setup fits that model?](https://www.prisma.io#which-hosting-setup-fits-that-model)

These options are ordered alphabetically by app host. Each can be paired with an external managed Postgres database; choose the service type before comparing its price.

| App host | When it fits | What to check | 
|---|---|---|
| Prisma Compute | A TypeScript HTTP bot whose service and database should be declared and deployed in one project. | The deployed runtime is Bun. Compute focuses on HTTP services; keep-awake work is best effort, and there is no persistent writable filesystem or WebSocket server support. See [limitations](https://www.prisma.io/docs/compute/limitations). | 
| [Render](https://render.com/docs/background-workers) | A Gateway or Socket Mode bot that needs a continuously running background worker, or a separate HTTP web service. | Select the worker or web-service type deliberately. Configure reconnects, shutdown behavior, server-side database access and the service's region. | 
| [Vercel](https://vercel.com/docs/functions) | HTTP commands that belong in an existing supported web app. | Function execution and connection lifetimes apply. For a continuous process, evaluate its separate [Daemons](https://vercel.com/docs/daemons) offering and current availability rather than assuming a Function is a permanent worker. | 

Prisma Compute fits the HTTP case especially well when a small team wants its assistant to see the service, database dependency and deployment configuration together. [Composer's plain Postgres dependency](https://www.prisma.io/docs/composer/databases) supplies connection configuration for the client you choose; adopting Prisma ORM is optional.

For a connected bot, Render's [outbound WebSocket support](https://render.com/docs/websocket) and continuously running worker model are directly relevant. Keep important state in Postgres there too: a worker restart still replaces the process.

## [How should I set up the HTTP bot on Prisma?](https://www.prisma.io#how-should-i-set-up-the-http-bot-on-prisma)

### [1. Create a separate development application](https://www.prisma.io#1-create-a-separate-development-application)

Use a development Discord application or Slack app installation and a test channel. Store its tokens and signing configuration as [server-side environment variables](https://www.prisma.io/docs/compute/environment-variables). Keep production credentials out of preview environments and build output.

Deploy a TypeScript HTTP service using [Composer getting started](https://www.prisma.io/docs/composer/getting-started) or [porting an existing app](https://www.prisma.io/docs/composer/porting-an-app). Verify the bot SDK and its HTTP adapter under Bun before connecting a live workspace.

### [2. Declare one database provisioning path](https://www.prisma.io#2-declare-one-database-provisioning-path)

Declare a [plain Postgres dependency](https://www.prisma.io/docs/composer/databases) if Composer should provision the database with the service. If you already created a database separately, configure that existing connection instead. Creating both does not make them the same database.

For a separately hosted bot, obtain Prisma Postgres's [pooled connection string](https://www.prisma.io/docs/postgres/database/connecting-to-your-database) for application traffic and keep it on the server. Use the direct connection for migrations and administrative tools. Place the bot near its database; the [region-selection guide](https://www.prisma.io/postgres/nodejs-database-regions) explains how extra round trips affect request time.

Store installation identifiers, application records and processing state in tables. Include the workspace or server boundary in queries, so a command from one customer cannot read another customer's records.

### [3. Verify the sender before accepting work](https://www.prisma.io#3-verify-the-sender-before-accepting-work)

Use the platform's documented verification procedure. Discord requires verification of the request signature and a valid response to its endpoint check. Slack's [request verification](https://docs.slack.dev/authentication/verifying-requests-from-slack/) uses its signing secret and timestamp. Preserve the raw request body where the verifier requires it.

For Slack's HTTP Events API, implement the [URL-verification handshake](https://docs.slack.dev/apis/events-api/using-http-request-urls/) too. For a `url_verification` setup request, verify the request and return HTTP 200 with its `challenge` value so Slack accepts the Request URL. This handshake applies to Events API URLs, not slash-command URLs.

A valid signature establishes the sender; your handler must still check whether the installation and user may perform the requested action. Avoid logging tokens, request signatures or private message bodies merely to prove that a request arrived.

### [4. Acknowledge promptly and persist work that must finish](https://www.prisma.io#4-acknowledge-promptly-and-persist-work-that-must-finish)

Discord requires an initial interaction response within three seconds. Slack [interactive requests](https://docs.slack.dev/interactivity/handling-user-interaction/) also require acknowledgment within three seconds. Implement the appropriate response or deferral before waiting for a slow model call or report generation; do not copy a generic HTTP acknowledgment across different interaction types.

For work that must finish, commit a job or queue message before acknowledging receipt, and ensure that storage step fits the platform's deadline. For a database inbox, use a stable delivery identifier where the platform provides one, such as a Discord interaction ID or a Slack Events API event ID. Namespace it by platform and installation, require every part of that key, and enforce a [database uniqueness constraint](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-UNIQUE-CONSTRAINTS). Accept the delivery and create its pending job in one transaction, handling a uniqueness conflict atomically so concurrent retries cannot both create a job. Different command types can require a different deduplication strategy.

Arrange an explicit processor that resumes pending work. On Compute, [persisting work and processing it in steps](https://www.prisma.io/docs/compute/request-timeout) needs a separate trigger, such as an external scheduler, Composer's cron building block or a worker elsewhere. `waitUntil` can keep an instance awake after a response; it does not supply retries or guarantee completion through a restart.

Plan how a resumed job delivers its result. [Discord interaction tokens](https://docs.discord.com/developers/interactions/receiving-and-responding) are valid for 15 minutes, while Slack's [`response_url` replies](https://docs.slack.dev/interactivity/handling-user-interaction/#message_responses) are limited to 30 minutes after receipt. If work can outlast that window, including after an outage, use an authenticated status page or a new bot message where the app has permission. Preserve the original recipient and privacy requirements rather than posting a private result to a public channel.

That uniqueness constraint prevents duplicate acceptance, but it cannot by itself make an external message send happen exactly once. Save progress, use downstream idempotency facilities where available, and decide how to reconcile a crash between sending a message and recording success.

### [5. Test through the real platform](https://www.prisma.io#5-test-through-the-real-platform)

Send a command from the development installation and confirm the expected database change. Then repeat the delivery, restart the service during processing, and verify that pending work resumes without creating a second ticket. Check that an invalid signature is rejected and that one customer's command cannot access another customer's records.

With [deploy on push](https://www.prisma.io/docs/compute/deploy-on-push), declared databases receive separate resources on preview branches. Check the bot installation and platform callback configuration separately: database isolation does not redirect production Slack or Discord traffic to a test workspace.

## [What should I budget for?](https://www.prisma.io#what-should-i-budget-for)

Account for the HTTP service or continuously running worker, Postgres usage and storage, and any external queue or AI API. A connected bot can consume resources while waiting for events. Repeated deliveries and retries can also add database and model calls.

Use the current [Prisma pricing](https://www.prisma.io/pricing), [Render pricing](https://render.com/pricing) or [Vercel pricing](https://vercel.com/pricing) for the service type you selected. Measure a representative command and its retry path before estimating from the number of chat users.

## [When is Prisma the wrong choice?](https://www.prisma.io#when-is-prisma-the-wrong-choice)

Choose a documented continuous-worker service for a Gateway or Socket Mode bot rather than relying on an HTTP instance remaining connected indefinitely. Prisma Compute has [no WebSocket server support or persistent filesystem](https://www.prisma.io/docs/compute/limitations), and its keep-awake primitives do not guarantee continuity through deployments. Keep bot state outside the process regardless of the host.

Prisma Postgres credentials have [full access to their database](https://www.prisma.io/docs/postgres/database/connecting-to-your-database#access-and-permissions); a separate password does not restrict a bot to one table or customer. Enforce application authorization, or choose a database setup with the restricted roles your design needs. For recovery, [paid-plan daily snapshots](https://www.prisma.io/docs/postgres/database/backups) are not point-in-time recovery. Include that distinction when choosing how to protect valuable bot records.

## Frequently asked questions

## Deploy the HTTP bot and its database together

Start with a TypeScript service and a Postgres dependency, then test a real command through a separate development installation.