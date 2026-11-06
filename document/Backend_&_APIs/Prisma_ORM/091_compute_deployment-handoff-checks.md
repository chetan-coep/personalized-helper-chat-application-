---
id: "prisma_orm_091"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 91
source_url: "https://www.prisma.io/compute/deployment-handoff-checks"
language: "en"
retrieved_at: "2026-11-01 22:20:07"
content_hash: "a6d476a5ecb1523b2a79398bad8ce6d08cbc567f133e3e6bbe78f97ca11e42fc"
---

# Prisma ORM

Source: https://www.prisma.io/compute/deployment-handoff-checks

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# Which hosting setup helps me verify a contractor's Next.js deployment?

[Prisma Compute](https://www.prisma.io/docs/compute)is a good fit for a TypeScript handoff because its CLI exposes services, live versions and logs, with

[Prisma Postgres](https://www.prisma.io/docs/postgres)available in the same project. Netlify and Vercel also expose deployment details. A successful build is one check; sign-in, database writes and the correct live version need their own checks.

[Søren Bramer Schmidt](https://github.com/sorenbs)7 min read

A handoff should leave the owner able to answer three questions: which version is live, whether its server can do the business task, and where to look when that task fails. The contractor's working laptop and a green build indicator do not answer all three.

We make Prisma Compute and Prisma Postgres. Provider sources linked here were checked on October 19, 2026. The service commands below inspect existing resources without deploying code or changing configuration. The acceptance test in step 3 writes a fictional record in production; use an agreed test account and clean up afterward.

## [What evidence should the owner be able to see?](https://www.prisma.io#what-evidence-should-the-owner-be-able-to-see)

Ask for the repository commit, platform project, production URL and service or deployment identifier. Keep the hosting account, domain and database ownership with the business. Give the contractor the platform access their work needs, then review access at handoff.

Separate build output from runtime evidence. Build logs explain compilation and packaging; runtime logs explain requests to the running server. Neither proves by itself that a customer can log in and save the right record. Agree on an acceptance test that covers the workflow the business bought.

## [Which host exposes useful deployment evidence?](https://www.prisma.io#which-host-exposes-useful-deployment-evidence)

These hosts are listed alphabetically. Each needs an application-level acceptance test.

| Host | What the owner can inspect | When it fits | 
|---|---|---|
| Netlify | [Deploy summaries and deploy logs](https://docs.netlify.com/deploy/deploy-overview/), plus [function logs](https://docs.netlify.com/manage/monitoring/logs/). | The app already uses Netlify's framework and function workflow. | 
| Prisma Compute | [Service details, live versions and version logs](https://www.prisma.io/docs/cli/service); build output is available in Console. | You want TypeScript hosting and managed Postgres in one project, with CLI inspection for the owner or their assistant. | 
| Vercel | [Deployment details and build output](https://vercel.com/docs/deployments), plus [runtime logs](https://vercel.com/docs/logs). | The Next.js app already follows Vercel's deployment workflow. | 

Keep an existing host if it already gives the owner the access and evidence they need. Prisma Postgres can remain the database from another app host; moving the frontend is optional.

## [How do I inspect a Next.js handoff on Prisma Compute?](https://www.prisma.io#how-do-i-inspect-a-nextjs-handoff-on-prisma-compute)

### [1. Confirm the account, project and service](https://www.prisma.io#1-confirm-the-account-project-and-service)

Use a supported CLI runtime from the [getting-started guide](https://www.prisma.io/docs/compute/getting-started). The commands use `prisma@latest` so an older project-local CLI is not selected. The current Prisma 8 CLI is a [release candidate](https://www.prisma.io/docs/orm/release-status); inspecting hosting resources does not require upgrading the app's ORM.

Authenticate as the intended account, then inspect an existing project named `customer-portal`. Here `main` is the project's confirmed production branch; replace it if your project uses another branch:

Use the service name actually returned by the list. The next commands assume it is `web` and keep the same explicit branch so a similarly named preview does not confuse the handoff:

The [service reference](https://www.prisma.io/docs/cli/service) describes these outputs. `service show` identifies the live version; the version list gives history. Keep that identifier with the agreed source commit and deployment report. The commands show real account-specific values, so there is no universal successful output to paste into a checklist.

### [2. Check the intended URL and version](https://www.prisma.io#2-check-the-intended-url-and-version)

Open the live service URL from its details, then the production custom domain if one is configured. Verify the expected release marker or feature and compare it with the handoff's commit and version record. A preview can work while a production domain still serves an earlier release.

For a deployment created by an assistant or CI, retain the [deploy report](https://www.prisma.io/docs/cli/deploy) with its resource results and URLs. Verify its outcome and the actual live version. A process starting successfully is not the same as a completed acceptance test.

### [3. Run an authenticated business action](https://www.prisma.io#3-run-an-authenticated-business-action)

This test writes to production through the live URL. Use the agreed test account to sign in, create or update a fictional record, reload the page and confirm the saved state. Verify that an unauthorized account cannot read it. Clean up the fictional record afterward through the application's normal workflow.

For Prisma Postgres, confirm the resource the app actually connects to and that its migrations are applied. A service can deploy while pointing to an empty test database or to credentials for the wrong environment. [Secret scopes](https://www.prisma.io/compute/typescript-app-secrets) and database identity belong in the handoff notes without recording secret values.

### [4. Check failures and the recovery path](https://www.prisma.io#4-check-failures-and-the-recovery-path)

Read runtime logs around the acceptance request. `service logs` defaults to the live version; use `--version-id` when investigating an older one. If runtime logs are unavailable for that version, retain its ID and consult Console build output or application monitoring. Avoid writing passwords, tokens or customer payloads to logs.

Agree who handles failed deploys and how to use the [rollback procedure](https://www.prisma.io/compute/roll-back-deployment). Test recovery on a review environment and check schema compatibility. Also confirm that billing, backups and the domain can be managed by someone the business retains.

When the business operates several independent apps, keep the handoff record per app. The [multiple-app hosting guide](https://www.prisma.io/compute/multiple-business-apps) covers separate projects, databases, credentials and release boundaries under shared administration.

## [When should I choose another setup?](https://www.prisma.io#when-should-i-choose-another-setup)

Choose the host whose runtime and operating workflow fit the app. Prisma Compute runs deployed services on Bun and currently lacks WebSocket server support and a persistent writable filesystem. Check the [runtime limits](https://www.prisma.io/docs/compute/limitations) before accepting dependencies that require those features.

If the owner requires a particular monitoring integration or log retention period, verify that separately. A short deploy log and a permanent application audit record serve different needs, and the handoff should state where each lives.

After accepting the release, keep an [owner operations record](https://www.prisma.io/compute/business-app-operations) with routine checks, recovery steps and a route to technical help.

## Frequently asked questions

## Make the handoff verifiable

Keep the project under business ownership and use live service details, version logs and an acceptance test to check the deployed app.