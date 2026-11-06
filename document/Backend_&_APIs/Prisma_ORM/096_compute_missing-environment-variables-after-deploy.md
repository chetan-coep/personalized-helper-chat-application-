---
id: "prisma_orm_096"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 96
source_url: "https://www.prisma.io/compute/missing-environment-variables-after-deploy"
language: "en"
retrieved_at: "2026-11-01 22:20:15"
content_hash: "07ff330c5331629f32080cfbf5487348c38eded1a8204e747f69b5acad83b7b1"
---

# Prisma ORM

Source: https://www.prisma.io/compute/missing-environment-variables-after-deploy

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# API key works locally but is missing after deployment: where do production secrets go?

`.env` file that Git ignores, so the deployed app never receives it. Production secrets go in your host's environment variable settings (a dashboard page or a CLI command) under the exact name your code reads, set for the environment you deployed (many hosts, such as Vercel and Netlify, hold separate values for production and previews). Then deploy again, because on Vercel, Netlify and many other hosts a changed variable applies only to new deployments. Keep the key out of variables with a public prefix such as `NEXT_PUBLIC_` or `VITE_`, which are copied into browser JavaScript at build time. On [Prisma Compute](https://www.prisma.io/docs/compute), the app reads the key through its service input, and

`npx prisma@latest project env add PAYMENTS_API_KEY --role production` stores the value for the next deploy.
[Gregory Boch](https://github.com/gregory-boch-prisma)10 min read

Your app reads the key from the environment (`process.env`, or `import.meta.env` in Vite), and on your machine something fills that in from a `.env` file: Next.js loads it into `process.env`, Vite loads it into `import.meta.env` (and exposes only `VITE_` values to browser code), and plain Node.js apps use `dotenv` or `node --env-file`. That file is in `.gitignore`, so it isn't in the repository your host deploys from. The deployed app starts with only the variables the host gives it, and the key isn't one of them until you add it in the host's settings and deploy again.

We make Prisma Compute and Prisma Postgres. The fix below works on any host. Every host and framework behavior on this page links to its documentation, checked on October 22, 2026.

## [Why the key is there locally and missing in production](https://www.prisma.io#why-the-key-is-there-locally-and-missing-in-production)

A `.env` file is a convenience for development. Git doesn't commit it, so a host that builds from your repository never sees it. In production, variables come from the platform: [Vercel](https://vercel.com/docs/environment-variables), [Netlify](https://docs.netlify.com/build/environment-variables/overview/), [Render](https://render.com/docs/configure-environment-variables), [Railway](https://docs.railway.com/variables) and [Fly.io](https://fly.io/docs/apps/secrets/) each store them per project, service or app and pass them to your code as environment variables.

TypeScript doesn't catch the gap. With `@types/node`, `process.env.PAYMENTS_API_KEY` has the type `string | undefined` ([process.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/node/process.d.ts)), and a non-null assertion such as `process.env.PAYMENTS_API_KEY!` satisfies the compiler without supplying a value. The first sign is often a `401` from the API you call, or a client library that throws because its key is `undefined`.

## [Find which check fails](https://www.prisma.io#find-which-check-fails)

What you see points to the cause. Run the check before you change anything.

| What you see | Likely cause | Check | 
|---|---|---|
| `undefined` in server code on every request | The variable isn't set on the host, or is set under a different name | The host's variable list for that project or service. Names are case-sensitive. | 
| Works in a preview deployment but not in production, or the reverse | The variable is set for one environment only | The environments or deploy contexts the variable applies to | 
| Still `undefined` after you added it | The running deployment is older than the change | Whether a deployment finished after you saved the variable | 
| `undefined` in browser code | The code runs in the browser, where server-only variables don't exist | Whether the code runs in a client component or a Vite client module | 
| The build fails, or a public value is empty in the browser | The variable isn't available to the build | The variable's scope (build or runtime) and where the build runs | 
| A public value is empty only in deploys built by CI | The CI job doesn't pass the secret to the build step | The workflow's `env:` block for the build step | 
| The app exits at startup with an error about a missing `.env` file | The start script runs `node --env-file=.env` and the file isn't on the server | The `start` script in `package.json` | 

The last row has a specific cause: [Node.js throws](https://nodejs.org/api/cli.html#--env-filefile) when the file passed to `--env-file` doesn't exist. Use `--env-file-if-exists=.env` (Node.js 22.9 or newer, no longer experimental since 22.21 and 24.10) in a script that also runs in production, or drop the flag there. When both the environment and the file set a variable, Node.js keeps the environment's value.

## [How to fix it](https://www.prisma.io#how-to-fix-it)

These steps work on any host. Replace `PAYMENTS_API_KEY` with your variable names.

### [1. List every variable the code reads](https://www.prisma.io#1-list-every-variable-the-code-reads)

Search the code for environment reads and compare the list with your `.env` file:

Without a path, `git grep` searches every tracked file, so it finds reads in `app/`, `src/` or anywhere else. The pattern also matches bracket access (`process.env["PAYMENTS_API_KEY"]`) and destructuring (`const { PAYMENTS_API_KEY } = process.env`), so read each match for the names it uses.

Check the exact spelling, including case and prefix. `PAYMENTS_API_KEY` and `PAYMENT_API_KEY` are different variables, and a host integration can add a variable under a name of its own choosing.

### [2. Add the variables on the host, for the right environment](https://www.prisma.io#2-add-the-variables-on-the-host-for-the-right-environment)

Set each variable where the host expects it, for the environment the failing deployment belongs to. Hosts with preview or staging environments (Vercel, Netlify, [Railway](https://docs.railway.com/environments) and Prisma Compute, for example) keep separate values per environment, so a key saved only for previews is missing in production.

These hosts are ordered alphabetically:

| Host | Where to set it | When a change takes effect | 
|---|---|---|
| Fly.io | `fly secrets set PAYMENTS_API_KEY=...` | [Immediately](https://fly.io/docs/apps/secrets/): the command updates and restarts each Machine. With `--stage`, when Machines are next started or updated, for example by `fly deploy`. Runtime secrets aren't available while Fly.io builds the image, which has separate build secrets. | 
| Netlify | Project configuration, Environment variables, or `netlify env:set` | [After a new build and deploy](https://docs.netlify.com/build/environment-variables/get-started/). On Pro and Enterprise plans, a variable can be [limited to scopes](https://docs.netlify.com/build/environment-variables/overview/) (Builds, Functions, Runtime, Post processing), so a Functions-only key isn't available to the build. | 
| Prisma Compute | `npx prisma@latest project env add PAYMENTS_API_KEY=... --role production`, with the app reading the key through its service input ([details below](https://www.prisma.io#setting-production-secrets-on-prisma-compute)) | [On the next deploy](https://www.prisma.io/docs/compute/environment-variables). Saving a variable doesn't change existing deployments or start a deploy. | 
| Railway | The service's Variables tab | [After you review and deploy](https://docs.railway.com/variables) the staged changes. Variables are available to the build and to the running service. | 
| Render | The service's Environment page in the dashboard | [Your choice when saving](https://render.com/docs/configure-environment-variables): rebuild and deploy, redeploy the existing build, or save only and apply on the next deploy. | 
| Vercel | Project settings, Environment Variables, or `vercel env add` | [Only on new deployments](https://vercel.com/docs/environment-variables/managing-environment-variables). Choose Production, Preview (all branches or one) or Development for each variable. | 

Other hosts and setups follow the same pattern:

- Heroku: `heroku config:set PAYMENTS_API_KEY=...`. Setting a config var [restarts the app and creates a new release](https://devcenter.heroku.com/articles/config-vars).
- Docker: pass variables when the container starts, with `docker run --env` or `--env-file` ([docker run reference](https://docs.docker.com/reference/cli/docker/container/run/)). Don't set secrets with `ENV` or `ARG` in the Dockerfile: Docker's docs say [they persist in the final image](https://docs.docker.com/build/building/secrets/).
- Kubernetes: store the key in a Secret and reference it from the container's `env` with `secretKeyRef` ([Kubernetes docs](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/)).
- Amazon ECS: reference the Secrets Manager secret in the task definition's `secrets` list and give the task execution role permission to read it. The container receives the value when it starts, so after rotating the secret, launch a new task or force a new deployment ([Amazon ECS docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.html)).
- A VM with systemd: `EnvironmentFile=` reads variables from a file outside the app directory. For secrets, [systemd's documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) recommends `LoadCredential=`, which passes them as files, because environment variables are inherited by child processes.

### [3. Keep the key in server code](https://www.prisma.io#3-keep-the-key-in-server-code)

A public prefix publishes the value. [Next.js](https://nextjs.org/docs/app/guides/environment-variables) replaces `process.env.NEXT_PUBLIC_*` references with their values during `next build` and includes them in the JavaScript sent to the browser. [Vite](https://vite.dev/guide/env-and-mode) does the same for `VITE_*` variables and says they shouldn't contain API keys. If browser code needs the result of an API call, call the API from a route handler, server action or backend endpoint that reads the unprefixed variable, and return only the data the page needs.

Build-time inlining also explains a public value that stays empty or old in the browser. Next.js reads `NEXT_PUBLIC_` values from the environment where `next build` runs and doesn't pick up later changes, so the build needs them and you have to rebuild after changing one. Server-only variables are read when the code runs: in Next.js, a page that renders per request reads `process.env` at that point.

If a CI job runs the build, map each value the build needs into the build step. In GitHub Actions, a step gets a secret only through the [`secrets` context](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets), and a secret that isn't set evaluates to an empty string instead of failing the job:

### [4. Redeploy and check the deployment, not the dashboard](https://www.prisma.io#4-redeploy-and-check-the-deployment-not-the-dashboard)

Start a new deployment after saving the variables, then confirm the running code sees them without printing the value. Log whether the variable is set, or call the code path that uses it and check for a successful response:

A variable that appears in the host's list only proves the name exists in that environment. It doesn't prove the deployment you're testing was created after you saved it, or that the value is the right key.

### [5. Fail at startup instead of on the first request](https://www.prisma.io#5-fail-at-startup-instead-of-on-the-first-request)

Read required variables once, in a module that server code imports, and stop with the variable's name when one is missing:

The error names the variable and never prints its value. In Next.js, a module imported by a page that is prerendered during `next build` runs this check during the build, so set the variable for the build as well or import the module only from code that runs per request.

## [Setting production secrets on Prisma Compute](https://www.prisma.io#setting-production-secrets-on-prisma-compute)

[Prisma Compute](https://www.prisma.io/docs/compute) hosts TypeScript apps built for Node.js, Bun or Next.js; deployed apps run on Bun. Prisma Compute fits when you want a missing key to stop the deploy instead of reaching production as `undefined`: in a [Prisma Composer](https://www.prisma.io/docs/composer) app, the deploy fails and names any variable bound with `envSecret` that is set neither on the platform nor in the deploying shell ([Deploying](https://www.prisma.io/docs/composer/deploying#ci)). Compute doesn't require Prisma ORM or Prisma Postgres, so the rest of this section applies to any app you deploy there.

On Compute, the fix has two parts, because the code reads the key differently. The CLI's `deploy` command, [deploy on push](https://www.prisma.io/docs/compute/deploy-on-push) and the Deploy Button all deploy a [Prisma Composer](https://www.prisma.io/docs/composer) app; only the REST API, whose endpoint is marked experimental, deploys without one ([Deployments](https://www.prisma.io/docs/compute/deployments)). In a Composer app, application code doesn't read `process.env`, so when you move an existing app over, its `process.env` reads become service input ([Compute FAQ](https://www.prisma.io/docs/compute/faq)).

First, declare the key as a `secretString()` field of the service's input, bind it in `module.ts` with `envSecret("PAYMENTS_API_KEY")`, and read it with `service.input()` ([Service input](https://www.prisma.io/docs/composer/service-input)). Your code receives a box that redacts the value in logs and JSON, and `.expose()` returns it where you pass it to the API client.

Then store the value that binding names, as a [project environment variable](https://www.prisma.io/docs/compute/environment-variables). Variables come in three layers: production, preview for every preview deploy, and overrides for a single preview branch. With only the name, the CLI reads the value from a variable of the same name in your shell, so export it first (for example from your secret manager's CLI) and the key doesn't appear in the command. With the production key exported as `PAYMENTS_API_KEY`, run:

Every preview deploy receives the preview value, so give previews a separate test or restricted key, not the production one. Export that key as `PAYMENTS_API_KEY` in the same shell, then run:

`project env` commands target the project the directory is linked to; in CI, pass `--project <id-or-name>` on each command instead ([Known limitations](https://www.prisma.io/docs/compute/limitations#cli)). `add` fails if the key already exists in that scope; use `update` to replace a value. `--branch <name>` sets an override for one preview branch, and `--file .env.production` imports a dotenv file instead of a single key. `list` shows names and metadata, never values ([project command reference](https://www.prisma.io/docs/cli/project)). Running the CLI with `npx` needs Node.js 22.18 or newer on the 22 line, 24.11 or newer on the 24 line, or 26 or newer.

A deploy can also seed the value: when a stage lacks the variable, the deploy copies it from the deploying shell ([Deploying](https://www.prisma.io/docs/composer/deploying)). So a deploy from your laptop can succeed while a fresh CI stage needs the value exported in the CI job.

Values resolve at deploy time, so deploy again after any change: run `deploy`, push to the default branch if deploy on push is set up, or promote a version, which rebuilds it with the production variables ([Compute FAQ](https://www.prisma.io/docs/compute/faq#how-do-i-rotate-a-secret)).

Two details matter for Next.js. `deploy` doesn't build for you: you run the build before `deploy`, locally or in CI, and deploy on push runs your build command in GitHub Actions ([Known limitations](https://www.prisma.io/docs/compute/limitations)). So `NEXT_PUBLIC_` values come from the environment where `next build` ran. And pages that read runtime configuration need `export const dynamic = "force-dynamic"` ([Compute FAQ](https://www.prisma.io/docs/compute/faq)).

Know the limits before you rely on it:

- Values are write-only. The CLI, the API and the Console never return them, and there is no command to pull them into a local `.env`, so keep the source copy in a secret manager.
- You set values with the CLI, or a deploy copies missing ones from the deploying shell. The Console lists variable names, never values.
- Keys must match `[A-Z_][A-Z0-9_]*`, and each value can be up to 8 KB. A larger credential, such as a long certificate chain, needs another delivery method, such as fetching it from a secret manager at startup.
- A changed value needs a new deployment. Prisma Compute has no documented integration that reads values from an external secret manager while the app runs.

If your app already runs on Vercel, Netlify, Render, Railway or Fly.io, moving hosts doesn't fix a missing variable. Set it where the app runs and redeploy there.

## [How to prevent it](https://www.prisma.io#how-to-prevent-it)

Commit a `.env.example` that lists every variable name with a placeholder value, and update it in the same change that adds a new `process.env` read. Keep the startup check from step 5, so a deploy with a missing key fails in the logs with the variable's name. Store the real values in one place you control, such as a password manager or a secret manager, and copy them to each host and CI system from there.

Never log a whole `process.env` object or a request that includes an `Authorization` header. If a key ends up in a commit or a log, rotate it with the provider before you clean up: [GitHub's guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) puts revoking or rotating the secret first.

## [When this fix doesn't apply](https://www.prisma.io#when-this-fix-doesnt-apply)

If the variable is set and the app still gets a `401` or `403`, the key arrives but is wrong: a test key in production, a revoked key, or a key from another account. Compare the key's prefix or last characters with the provider's dashboard instead of printing it.

If the missing value is `DATABASE_URL` and you don't have a database yet, follow the [DATABASE\_URL guide](https://www.prisma.io/postgres/database-url-missing). For how to separate production and preview credentials, rotate them and hand them over to a contractor, see [where database passwords and API keys go when you deploy](https://www.prisma.io/compute/typescript-app-secrets).

## Frequently asked questions

`create-next-app` adds `.env` files to `.gitignore` for that reason. Set the value in the host's environment settings, and keep the source copy in a password manager or secret manager. A `.env.example` file with names and placeholder values is the part to commit.`NEXT_PUBLIC_` or `VITE_` is readable by anyone who loads the page, so move the call that needs it to server code.`DATABASE_URL` on the host and redeploy. The [DATABASE\_URL guide](https://www.prisma.io/postgres/database-url-missing)walks through that case, including pooled and direct connection strings. On Prisma Compute, a database declared in the Composer module is created by the deploy and reaches the app as

`db.url` from `service.load()`, so there is no `DATABASE_URL` to set (
[Databases](https://www.prisma.io/docs/composer/databases)).

## Set production and preview secrets on Prisma Compute

Store each key per environment with the Prisma CLI, keep values write-only, and deploy to apply them.