---
id: "prisma_orm_095"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 95
source_url: "https://www.prisma.io/compute/long-running-background-jobs"
language: "en"
retrieved_at: "2026-11-01 22:20:14"
content_hash: "4730ae154953d285367536179b75ed0a424820f398fa7bd61924e047dadc19fb"
---

# Prisma ORM

Source: https://www.prisma.io/compute/long-running-background-jobs

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# My background job stops when my serverless function times out. Where should long-running tasks run?

`waitUntil` or Next.js `after()` on Vercel. That limit is 5 minutes by default on Vercel and at most 15 minutes for a standard AWS Lambda function. Move the job out of the request: the handler saves the job and returns `202`, and something without that limit runs it. That is either a worker process on a host that keeps it running (Railway, Render or Fly.io) reading from a queue such as pg-boss or Graphile Worker on Postgres or BullMQ on Redis, or a durable workflow service such as Inngest, Trigger.dev, Vercel Workflows or Upstash Workflow that runs the job as retried steps. Whichever you pick, make every step safe to run twice. On [Prisma Compute](https://www.prisma.io/docs/compute),

`waitUntil` keeps the instance awake after the response until the job's promise settles, on a best-effort basis, so the job belongs in the database as well.
Every serverless function invocation has a time limit. When the invocation reaches it, the platform stops it, and everything it started stops with it: the promise you didn't await, the loop over 10,000 rows, the call to a model API that was halfway through. Often nothing is logged except the timeout, and the work has to start over from the beginning, if anything starts it again at all. The fix is to stop running the job inside the request: save it, return `202`, and run it in a worker process on a host that keeps it running, or in a durable workflow service that retries each step.

We make Prisma Compute and Prisma Postgres. The fix below works on any host. Platform and library behaviors on this page link to their documentation, checked on October 22, 2026.

## [Why the job stops at the time limit](https://www.prisma.io#why-the-job-stops-at-the-time-limit)

Each platform sets a hard limit on how long one invocation can run. On AWS Lambda and Vercel, work you start after sending the response is bound by that same invocation.

| Platform | Time limit per invocation | Work after the response | 
|---|---|---|
| AWS Lambda | 3 seconds by default, configurable up to 900 seconds (15 minutes). Lambda Managed Instances allow up to 90 minutes for asynchronous and event-source invocations. [Docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html) | Background work that hasn't finished when the handler returns is frozen with the execution environment, and resumes only if Lambda reuses that environment. [Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) | 
| Netlify | 60 seconds for synchronous functions, not configurable. Background functions run up to 15 minutes. [Configuration](https://docs.netlify.com/build/functions/configuration/), [background functions](https://docs.netlify.com/build/functions/background-functions/) | `context.waitUntil()` extends the function's execution until the promise completes, so the work still has to finish within the function's limit. [Functions API](https://docs.netlify.com/build/functions/api/#waituntil). A background function that returns an error is retried after 1 minute, then after 2 more. | 
| Prisma Compute | 60 seconds to start responding. A response that has started streaming isn't cut off. [Docs](https://www.prisma.io/docs/compute/request-timeout) | `waitUntil` keeps the instance awake until the promise settles, best effort: no retry, and no continuity through a restart or deployment. [Docs](https://www.prisma.io/docs/compute/keeping-instances-awake) | 
| Vercel | 300 seconds by default with Fluid compute. Pro and Enterprise can raise it to 800 seconds, and to 1,800 seconds per function in a beta for Node.js, Bun and Python. Hobby stays at 300. [Limits](https://vercel.com/docs/functions/limitations#max-duration), [configuring duration](https://vercel.com/docs/functions/configuring-functions/duration) | Promises passed to `waitUntil` have the same timeout as the function, and are cancelled when it times out. [Docs](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package) | 

Raising the limit helps when a job has a known upper bound below the platform's maximum. It doesn't help when the job's length depends on the data (an import that grows with the customer's file), and it doesn't add retries. The fix is to stop tying the job to a request at all.

## [Fix: save the job, return, and run it somewhere else](https://www.prisma.io#fix-save-the-job-return-and-run-it-somewhere-else)

The pattern is the same on every platform. The request handler checks the input, saves a job that describes the work, and returns `202 Accepted` with the job's id. A separate process picks the job up, runs it, retries it when it fails, and records its progress where your app can read it.

### [1. Pick where the job runs](https://www.prisma.io#1-pick-where-the-job-runs)

The choice is mostly about what you are willing to host and how long one job runs.

| Option | Examples | How it gets past the time limit | Choose it when | 
|---|---|---|---|
| Durable workflow service | [Inngest](https://www.inngest.com/docs/usage-limits/inngest), [Trigger.dev](https://trigger.dev/docs/runs/max-duration), [Upstash Workflow](https://upstash.com/docs/workflow/getstarted), [Vercel Workflows](https://vercel.com/docs/workflows) | Trigger.dev builds and deploys your task code to its own infrastructure and runs it there, so your host's time limit doesn't apply ( [how it works](https://trigger.dev/docs/how-it-works)). Runs have no maximum duration: you set a project default `maxDuration`, which caps each attempt's CPU time, and `timeout.None` removes the cap. Inngest, Upstash Workflow and Vercel Workflows call your own functions for each step and save each finished step, so a failed step is retried without rerunning the others, but every step must still fit your host's limit ([Inngest retries](https://www.inngest.com/docs/features/inngest-functions/error-retries/retries)). Upstash runs each step as a separate request to your app, and an Inngest step can run up to 2 hours, but no longer than your host's own timeout. | You don't want to host a worker, or the job waits on webhooks, approvals or sleeps. | 
| Durable functions on your cloud | [AWS Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html) | Lambda checkpoints each step and resumes from the last checkpoint, and a durable function can run for up to one year. A Step Functions Standard workflow execution can also run up to 1 year; an Express workflow is capped at 5 minutes. | You are already on AWS. | 
| Queue in Postgres, plus a worker process | [pg-boss](https://github.com/timgit/pg-boss), [Graphile Worker](https://worker.graphile.org/docs/requirements) | Jobs are rows in your database. A long-running worker claims them with `SKIP LOCKED`, so the job runs in a process with no request attached. | You already use Postgres and want jobs to commit in the same transaction as the data they belong to. | 
| Queue in Redis, plus a worker process | [BullMQ](https://docs.bullmq.io/) | The same pattern, with Redis as the queue store. | You already run Redis, or you want BullMQ's rate limiting and priorities. | 
| Workflow engine with your own workers | [Temporal](https://docs.temporal.io/workers) | The Temporal Service keeps each workflow's state and hands out tasks. Your code runs in worker processes that you operate. | The job is a long, multi-step workflow and you are prepared to operate the workers. | 
| Batch job | [Cloud Run jobs](https://docs.cloud.google.com/run/docs/configuring/task-timeout), [Amazon ECS standalone tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-tasks.html) | Each task runs in a container that does the work and then stops. A Cloud Run task has its own timeout: 10 minutes by default, configurable up to 168 hours. On AWS, an ECS task on Fargate or your own EC2 instances fits a batch process the same way. | The job is heavy computation that needs a container image or runs for hours. | 

A worker process needs a host that keeps it running. On [Railway](https://docs.railway.com/guides/bullmq-jobs-retry-dlq), that is an always-on service in the same project, with serverless left off. On [Render](https://render.com/docs/background-workers), it is a background worker, which runs continuously and receives no network traffic; background workers don't have a free instance type ([Render free tier](https://render.com/docs/free)). On [Fly.io](https://docs.fly.io/launch/processes), it is a `worker` process group in the same app. List only the `web` group in the `processes` of your `http_service` (or `[[services]]`) section, so Fly Proxy sends requests only to the web process.

If you can't add any of these yet, split the job into chunks that each finish inside one invocation, record where each chunk ended, and have each one queue the next. It needs no new infrastructure, but every chunk is still bound by the time limit.

### [2. Save the job and return](https://www.prisma.io#2-save-the-job-and-return)

The rest of this guide uses [pg-boss](https://github.com/timgit/pg-boss) on Postgres, because it needs no service besides the database you already have. It requires Node.js 22.12 or newer (or Bun) and PostgreSQL 13 or newer. The example uses ES modules, so set `"type": "module"` in `package.json`.

Create the queue in one shared module. Each process (your web app and the worker) gets its own pg-boss instance, created once and reused:

The request handler only sends the job. This one is a Next.js route handler in a project with a `src` directory, and the same three lines work in any framework:

The route queues work on the caller's behalf, so check who is calling first, the same way your other routes do: authenticate the request and confirm the caller can access `reportId`. The example leaves that check out because it depends on your auth setup.

pg-boss creates its tables in a `pgboss` schema the first time `start()` runs. Because the job is a row in your database, you can also send it inside the transaction that creates the report, so the job exists only if the report does ([pg-boss adapters](https://github.com/timgit/pg-boss/blob/master/docs/api/adapters.md)).

### [3. Run the worker as its own process](https://www.prisma.io#3-run-the-worker-as-its-own-process)

The worker is a long-running script, not a route. It polls the queue (every 2 seconds by default), runs each job and marks it done or failed:

Run it with `npx tsx src/worker.ts` locally, and deploy it as a second service from the same repository with that start command. On a deploy, the host sends `SIGTERM` and then kills the process after a grace period. `boss.stop()` waits up to 30 seconds by default for active jobs, then fails them so they retry ([pg-boss stop](https://github.com/timgit/pg-boss/blob/master/docs/api/ops.md)). Set its `timeout` just under your host's grace period: Railway gives 0 seconds unless you set a draining time ([Railway guide](https://docs.railway.com/guides/bullmq-jobs-retry-dlq)), Render 30 seconds by default and up to 300 ([Render deploys](https://render.com/docs/deploys)), and Fly.io's `kill_timeout` 5 seconds by default and up to 300 ([Fly.io configuration](https://fly.io/docs/reference/configuration/)). A job longer than that is interrupted on every deploy, so it depends on the recorded steps in step 4. A process killed before `stop()` fails its jobs leaves them active until `expireInSeconds` passes (or the heartbeat check below notices), then pg-boss retries them.

`expireInSeconds` defaults to 15 minutes and can be at most 24 hours. Set it above the longest a job should ever take. For long jobs, also set `heartbeatSeconds` on the queue: the worker then reports that it is alive, and pg-boss notices a dead worker within `heartbeatSeconds` plus up to 60 seconds and retries its job, instead of waiting out the expiration ([pg-boss queues](https://github.com/timgit/pg-boss/blob/master/docs/api/queues.md)).

### [4. Make each job safe to run twice](https://www.prisma.io#4-make-each-job-safe-to-run-twice)

Plan for every job to run more than once. A worker can finish the work and crash before recording it, and a step can time out after its side effect happened. BullMQ documents at-least-once delivery as the worst case ([BullMQ](https://docs.bullmq.io/)), Upstash Workflow promises at-least-once delivery ([Upstash Workflow](https://upstash.com/docs/workflow/getstarted)), and pg-boss warns that a job that expired may already be running again elsewhere ([pg-boss workers](https://github.com/timgit/pg-boss/blob/master/docs/api/workers.md)). Design for it:

- Give each side effect a key and check it before acting: a row in a `sent_emails` table, or an idempotency key passed to the payment or email API.
- Split the job into steps and record each finished step, for example the last row offset of an import. A retry starts from the last recorded step, and only the interrupted step runs again.
- Put a timeout on every network call inside the job, shorter than the job's own expiration, so one stuck request doesn't hold the whole job until it expires.

### [5. Show progress to the user](https://www.prisma.io#5-show-progress-to-the-user)

The request returned a job id, so the page can ask for the job's state instead of holding a request open. Store status and progress in your own table (`reports.status`, `reports.progress`) and update it from the worker. The page then polls an endpoint that reads that row, or listens on a stream you send from it. pg-boss also keeps its own record of each job, which `getJobById` returns, but your table is the one your app's permissions already cover.

## [Where does Prisma Compute fit?](https://www.prisma.io#where-does-prisma-compute-fit)

[Prisma Compute](https://www.prisma.io/docs/compute) hosts TypeScript apps built for Node.js, Bun or Next.js; deployed apps run on Bun. Prisma Compute fits when the job is bounded and a lost run can be started again: the request saves the job in Postgres and returns within the 60-second response limit, and `waitUntil` from `@prisma/compute` keeps the instance awake until the work's promise settles ([Request timeout](https://www.prisma.io/docs/compute/request-timeout)). The docs describe this as bounded, best-effort background work, and an idle app scales to zero again once it finishes ([Keeping instances awake](https://www.prisma.io/docs/compute/keeping-instances-awake)).

Keep the job in [Prisma Postgres](https://www.prisma.io/docs/postgres), in the same project as the app. If a deploy or restart interrupts the work, the job is still there, and the next trigger picks it up from its last recorded step: a request from an external scheduler that calls your service, or a worker you run on another host. If a worker on another host also processes these jobs, have `runJob` claim the row first, for example `UPDATE jobs SET status = 'running', claimed_at = now() WHERE id = $1 AND status = 'queued' RETURNING id`, and skip the job when no row comes back, so the two never run it at once. pg-boss polls by default, so it runs over the pooled connection string (`pooled.db.prisma.io`). Graphile Worker listens with `LISTEN`/`NOTIFY` by default, and so does pg-boss when you turn on `useListenNotify`; give those connections the direct connection string (`db.prisma.io`), because the pooler runs in transaction mode ([Connection pooling](https://www.prisma.io/docs/postgres/database/connection-pooling), [pg-boss constructor](https://github.com/timgit/pg-boss/blob/master/docs/api/constructor.md), [Graphile Worker FAQ](https://worker.graphile.org/docs/faq)). Compute doesn't require Prisma ORM or Prisma Postgres; the examples on this page use pg-boss and its own `pg` pool.

Know the limits before you rely on it:

- `waitUntil` and `KeepAwakeGuard` are best effort ([Keeping instances awake](https://www.prisma.io/docs/compute/keeping-instances-awake)). They keep the current instance from scaling to zero, but they don't make work durable, retry failures, or carry work through a restart or a new deployment.
- Compute focuses on HTTP services and has no built-in cron scheduler today ([Known limitations](https://www.prisma.io/docs/compute/limitations#runtime)); native cron is planned for early 2027. A job that has to run when no request arrives needs an external scheduler that calls your service, or a worker on another host.
- An instance kept awake is running, so it bills provisioned memory for the whole time, even while the job mostly waits ([Compute pricing](https://www.prisma.io/docs/compute/pricing)).
- Compute runs TypeScript on Bun and doesn't run Python, Go or Docker images ([Compute FAQ](https://www.prisma.io/docs/compute/faq)). A job that needs one of those belongs on a container host or in Cloud Run jobs.
- Pooled Prisma Postgres connections end any single query after 10 minutes. Long queries and `LISTEN` go over the direct connection, which allows 10 connections on Free and Starter, 50 on Pro and 100 on Business, with 5 reserved for platform operations ([Connection pooling](https://www.prisma.io/docs/postgres/database/connection-pooling)).

If the job must not be lost and runs for an hour or more, or must start at fixed times, keep the queue in Prisma Postgres if you like, and run the worker on Railway, Render or Fly.io, or hand the job to a durable workflow service.

## [How to prevent it](https://www.prisma.io#how-to-prevent-it)

Treat any work that can take longer than a few seconds as a job from the start: the handler validates the input, saves the job and returns its id. Test with production-sized data, because a job that takes 20 seconds on a sample file can take 20 minutes on a real customer's file.

Log the job id at each stage, and alert on jobs that have been active or retrying for longer than you expect. pg-boss's `getQueue()` returns a queue's queued, active and failed counts; for your own table, a query on `status` and `updated_at` does it.

## [When this fix doesn't apply](https://www.prisma.io#when-this-fix-doesnt-apply)

If the work is a response the user is waiting for, such as a streamed AI answer, a queue adds a round trip the user doesn't need. Start streaming the response early instead: on Prisma Compute, a response that has started streaming isn't cut off at 60 seconds. [AI chat responses cut off by a timeout](https://www.prisma.io/compute/ai-chat-timeout-streaming) covers that case.

If the job should run on a schedule, every night or every 5 minutes, the question is what starts it, not where it runs. See [scheduled jobs that don't run](https://www.prisma.io/compute/scheduled-jobs-not-running).

If the job fails on the first attempt every time, more time or retries won't fix it. Run it locally against a copy of the data, with the same input, and find the error first.

## Frequently asked questions

[limits](https://vercel.com/docs/functions/limitations#max-duration),

[duration docs](https://vercel.com/docs/functions/configuring-functions/duration)). AWS Lambda allows up to 900 seconds (

[timeout docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)). A longer limit doesn't add retries, though: if the function crashes at minute 12, the job is lost unless it was saved somewhere first, and the user still waits on an open request.

`SKIP LOCKED`, so concurrent workers don't block each other or get the same job, and a job can commit in the same transaction as the row it belongs to (
[pg-boss](https://github.com/timgit/pg-boss)). BullMQ needs Redis, and it is a good choice when you already run Redis or want its rate limiting and job priorities.

[You don't need a job queue, Postgres already has SKIP LOCKED](https://www.prisma.io/blog/you-dont-need-a-job-queue-postgres-already-has-skip-locked)builds a queue on a plain table and covers when a dedicated queue is worth it.

`waitUntil` have the same timeout as the function, and Vercel recommends `after()` on Next.js 15.1 and later for the same purpose, with `maxDuration` setting how long it may run (
[Vercel docs](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package)). Both suit short follow-up work such as logging. On Prisma Compute,

`waitUntil` keeps the instance awake until the promise settles, but it doesn't retry the work or carry it through a restart or deployment (
[Keeping instances awake](https://www.prisma.io/docs/compute/keeping-instances-awake)).

## Return fast, finish the work after the response

See how a Prisma Compute service answers within 60 seconds, keeps working with waitUntil, and stores jobs that must not be lost.