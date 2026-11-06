---
id: "prisma_orm_094"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 94
source_url: "https://www.prisma.io/compute/from-dev-server-to-production"
language: "en"
retrieved_at: "2026-11-01 22:20:11"
content_hash: "971dba9afd4e54dd1a3840c106f7175cf1a7f72b4838c6cfe19f52fec7cc93fd"
---

# Prisma ORM

Source: https://www.prisma.io/compute/from-dev-server-to-production

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# What does my TypeScript app need before I put it into public use?

[Prisma Compute](https://www.prisma.io/docs/compute)with

[Prisma Postgres](https://www.prisma.io/docs/postgres)fits a TypeScript app you want hosted with its database in one project. Vercel and Netlify are good choices when the app already follows their framework deployment workflow. Treat the move from

`npm run dev` as an application-readiness check as well as a hosting decision.
[Søren Bramer Schmidt](https://github.com/sorenbs)6 min read

`npm run dev` runs whatever your project's `dev` script defines. In many frameworks it starts a development server with fast rebuilds and development diagnostics. Opening that process to the internet does not establish a production deployment or prove that the application's data and access rules are ready.

We make Prisma Compute and Prisma Postgres. Provider and framework documentation linked here was checked on October 20, 2026. The steps apply to an existing app; use the framework's production instructions for its actual build and startup commands.

## [What changes between development and production?](https://www.prisma.io#what-changes-between-development-and-production)

The hosting provider needs an artifact it can reproduce and a supported way to run the server. Your users need the application to retain data, enforce access rules and fail in a way someone can diagnose. These are separate checks: a correct build can still point at the wrong database.

| Development assumption | Production question | 
|---|---|
| The app reads a local `.env` file. | Which server-side inputs does the deployed version receive? | 
| Test records live in memory or a local JSON file. | Which managed database stores records across instances and deploys? | 
| A developer opens the home page. | Can a real role sign in, complete the business action and see the saved result? | 
| An error appears in the terminal. | Where can the owner find a request error and the deployed version? | 
| The developer restarts the process. | How does the team recover code and data after a failed change? | 

## [Which host should I choose?](https://www.prisma.io#which-host-should-i-choose)

Choose around the framework and runtime you actually have. The options below are listed alphabetically.

| Host | Good fit | Preparation | 
|---|---|---|
| Netlify | Your framework's production integration fits Netlify's [deploy workflow](https://docs.netlify.com/deploy/deploy-overview/). | Configure its build, server functions and database environment. | 
| Prisma Compute | Your TypeScript server fits the deployed Bun runtime and you want managed Postgres in the same project. | Add a [Composer declaration](https://www.prisma.io/docs/composer), configure inputs and build before deploying. | 
| Vercel | Your app already follows its [framework and deployment workflow](https://vercel.com/docs/deployments). | Confirm dynamic routes, functions and the Preview/Production configuration. | 

A static export can suit an app with no server-side work. An application with private database queries or secret API calls needs those operations on a supported server runtime. Uploading a frontend folder alone does not deploy an arbitrary backend process.

## [How do I prepare the app for Prisma Compute?](https://www.prisma.io#how-do-i-prepare-the-app-for-prisma-compute)

### [1. Identify and run the production build](https://www.prisma.io#1-identify-and-run-the-production-build)

Read the scripts in `package.json` and the framework's deployment guide. For Next.js, review the [production checklist](https://nextjs.org/docs/app/guides/production-checklist). For a project that uses npm, commits `package-lock.json` and defines its production build as `build`, verify a clean installation and build:

A successful command exits with code `0`; its messages depend on the application. Fix missing configuration and type/build errors before deploying. Use your repository's actual package manager and lockfile rather than introducing npm into a pnpm or Bun project.

Follow the [framework deployment guide](https://www.prisma.io/docs/prisma-compute/deploy) to declare the service's build and entry point in Composer. Compute's `deploy` command does not run the build for you. Next.js needs its configured standalone artifact; a custom HTTP server must use the assigned service port and listen on `0.0.0.0`.

### [2. Configure durable data and secrets](https://www.prisma.io#2-configure-durable-data-and-secrets)

Create an account-owned Prisma Postgres database in [Console](https://console.prisma.io), then configure the existing client with the [pooled application URL](https://www.prisma.io/docs/postgres/database/connecting-to-your-database). Use a separate direct connection where your migration or administration workflow requires one. Prisma ORM is optional.

Move real records out of process memory and local files. Apply the schema with the migration workflow for your client, and verify which database the app connects to. A deployment does not prove that a manually managed schema has been applied.

Set [server-side inputs](https://www.prisma.io/compute/typescript-app-secrets) for database credentials, private API keys and the app's public origin or authentication callbacks. Give previews their own credentials and test database. Store customer uploads in [object storage](https://www.prisma.io/compute/file-uploads-disappear-after-redeploy).

### [3. Deploy a review version and exercise it](https://www.prisma.io#3-deploy-a-review-version-and-exercise-it)

Use [getting started](https://www.prisma.io/docs/compute/getting-started) to authenticate, then deploy the built Composer app to a [named test stage](https://www.prisma.io/docs/composer/deploying#production-and-stages): `npx prisma@latest deploy --stage review`. Verify the intended project and review stage in the deploy report. Open its actual URL from a second browser or device. Test both an allowed action and an action the current user must not be allowed to perform.

Create a fictional record, reload, then redeploy the same code and read the record again. Check login callbacks at the deployed origin, not just localhost. Confirm that invalid input produces a useful response and that logs exclude credentials and customer payloads.

### [4. Define the release and recovery procedure](https://www.prisma.io#4-define-the-release-and-recovery-procedure)

Record which source commit and live service version passed review. Keep the test steps with the repository and decide how schema changes reach production. With [deploy on push](https://www.prisma.io/docs/compute/deploy-on-push), the GitHub connection and the repository workflow are both required.

After review passes, check the intended production database and migration plan, then build and deploy the approved commit with production inputs. Verify the production URL and sign-in, and test a fictional save/read using an agreed test account with cleanup afterward.

Before customers depend on saved data, choose an appropriate [backup plan](https://www.prisma.io/docs/postgres/database/backups) and test restoration into a separate database. Keep code rollback and data recovery as separate procedures. Review [usage limits and spending controls](https://www.prisma.io/compute/typescript-hosting-spending-controls) before sharing the production URL.

Invite customers using the verified production URL.

## [When should I choose another setup?](https://www.prisma.io#when-should-i-choose-another-setup)

Prisma Compute runs deployed services on Bun and currently has no WebSocket server support, multi-region service deployment or persistent writable filesystem. Check the [runtime limitations](https://www.prisma.io/docs/compute/limitations) before committing to dependencies that require them. Prisma Postgres can still be the database from another app host.

If the remaining work is an unresolved authorization rule, missing recovery plan or unreliable business action, changing the host alone will not complete it. Resolve those application requirements in the review environment before inviting customers.

## Frequently asked questions

## Test a production deployment before inviting users

Prepare the app's build and inputs, then deploy a separate review environment with Prisma Compute and Prisma Postgres.