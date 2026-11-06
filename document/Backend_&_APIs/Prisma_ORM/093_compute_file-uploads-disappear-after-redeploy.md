---
id: "prisma_orm_093"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 93
source_url: "https://www.prisma.io/compute/file-uploads-disappear-after-redeploy"
language: "en"
retrieved_at: "2026-11-01 22:20:10"
content_hash: "51ac5ea7effa840089574a4be8b3929e71138b6e4d9b400bf3a8fd14122bb789"
---

# Prisma ORM

Source: https://www.prisma.io/compute/file-uploads-disappear-after-redeploy

---

[Prisma Compute](https://www.prisma.io/compute)

[Guides](https://www.prisma.io/compute/guides)

# Files uploaded to my Node app disappear after a redeploy. Where should I store them?

`uploads/` folder, is gone after the next deploy or restart. Store customer uploads in S3-compatible object storage (AWS S3, Cloudflare R2, or the bucket service your host offers) and save each file's key, owner and type in your database. A persistent disk or volume also works, but each one belongs to a single instance, so the app either runs as one instance or ends up with files split across instances. On [Prisma Compute](https://www.prisma.io/docs/compute), which has no persistent filesystem, uploads go to an

[Object Store bucket](https://www.prisma.io/docs/compute/object-storage)in the same Prisma project as your database.

[Gregory Boch](https://github.com/gregory-boch-prisma)8 min read

If customer uploads were there yesterday and are missing after a deploy, your app is almost certainly writing them to the server's local disk. On most hosting platforms that disk belongs to one running copy of your build, and the next deploy replaces it with a new one.

We make Prisma Compute and Prisma Postgres. Every host behavior on this page links to that host's documentation, checked on October 19, 2026. The fix works for any Node.js app, whichever framework, host or database client you use.

## [Why uploaded files disappear](https://www.prisma.io#why-uploaded-files-disappear)

A deploy builds your code into an image, starts new instances from it and stops the old ones. Each new instance starts with the files from the build and nothing else, so a file your app saved at runtime, for example with multer's `diskStorage` or `fs.writeFile("./uploads/...")`, is not in it.

Hosts document this in their own words:

| Host | What happens to files your app writes at runtime | 
|---|---|
| Fly.io | A Machine's root filesystem is ephemeral, meant for data that can be rebuilt on deploys and restarts. A Fly Volume keeps files, attached to one Machine. [Docs](https://docs.fly.io/volumes/overview) | 
| Heroku | Each dyno gets a fresh copy of the latest deploy, and files it writes are discarded when it stops or restarts. Dynos restart daily. [Docs](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), [S3 guide](https://devcenter.heroku.com/articles/s3) | 
| Prisma Compute | No persistent filesystem. Files you keep go to an Object Store bucket or the database. [Docs](https://www.prisma.io/docs/compute/limitations#runtime), [FAQ](https://www.prisma.io/docs/compute/faq) | 
| Railway | Files persist inside a mounted volume, one volume per service. Data written to the volume path at build time is not kept. [Docs](https://docs.railway.com/volumes/reference), [guide](https://docs.railway.com/volumes) | 
| Render | Changes to a service's local files are lost on every redeploy or restart, unless they are on a persistent disk. [Docs](https://render.com/docs/disks) | 
| Vercel | Functions have a read-only filesystem with a writable `/tmp` of up to 500 MB, for scratch space only. [Docs](https://vercel.com/docs/functions/runtimes#file-system-support) | 

Two related symptoms have the same cause. If you run more than one instance, an upload saved by one instance is missing when a request lands on another. And if uploads work on your laptop but not after deploying, that is because your laptop keeps the same disk between runs and a deployed instance doesn't.

## [Fix: move uploads to object storage](https://www.prisma.io#fix-move-uploads-to-object-storage)

Object storage keeps files outside your app's instances, so deploys, restarts and extra instances no longer affect them. Use any S3-compatible service: [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Cloudflare R2](https://developers.cloudflare.com/r2/api/s3/api/), [Railway Buckets](https://docs.railway.com/storage-buckets), a [Prisma Object Store bucket](https://www.prisma.io/docs/storage), or the one your host recommends. Your database then keeps one row per file, so the app can list a customer's files, check who owns a file and find it in the bucket.

### [1. Create a bucket and an access key](https://www.prisma.io#1-create-a-bucket-and-an-access-key)

Create a private bucket with your provider and an access key that can read and write it. Save four values as environment variables on your host, never in Git: `S3_ENDPOINT`, `S3_BUCKET`, `S3_ACCESS_KEY_ID` and `S3_SECRET_ACCESS_KEY`. Leave `S3_ENDPOINT` unset for AWS S3, and set `S3_REGION` to the region your provider's documentation gives for its S3 API (on AWS S3, the bucket's region).

### [2. Add a table for file references](https://www.prisma.io#2-add-a-table-for-file-references)

The bucket holds the bytes. Postgres holds what your app needs to know about them:

Store the object key, not a full URL. A key keeps working when you move the files to another provider or switch from public to presigned links, and a stored URL doesn't.

### [3. Write uploads to the bucket instead of the disk](https://www.prisma.io#3-write-uploads-to-the-bucket-instead-of-the-disk)

Install the packages the example uses:

This Express example keeps the upload in memory with multer, writes it to the bucket, records it in Postgres and serves it back through a presigned URL. It uses ES modules, so save it as `server.mjs` or set `"type": "module"` in `package.json`. Replace the `ownerId` lines with your own authentication.

Generate the key yourself instead of using the customer's file name, so two files called `invoice.pdf` don't overwrite each other and nobody can write outside their own prefix. If your provider's documentation asks for path-style URLs, add `forcePathStyle: true` to the client options. If it rejects the checksum headers that recent AWS SDK versions send by default, add `requestChecksumCalculation: "WHEN_REQUIRED"`.

For large files such as videos, you can skip the app server: your app creates a presigned PUT URL and the browser uploads straight to the bucket. [AWS documents this flow](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html), and other S3-compatible services support it to different degrees, so check yours.

### [4. Copy the files that are still on disk](https://www.prisma.io#4-copy-the-files-that-are-still-on-disk)

Files written since the last deploy or restart exist only on the running instance. Before you deploy the fix, copy them into the bucket if your host gives you a shell on that instance or a volume to read from, then insert a row for each one. Run an S3 tool or a short script on that instance, not on a fresh one: on Heroku, for example, `heroku run` starts a new one-off dyno that doesn't have the web dyno's files. With the AWS CLI installed there and the bucket's key set as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`:

Leave out `--endpoint-url` for AWS S3.

### [5. Deploy and check that files survive](https://www.prisma.io#5-deploy-and-check-that-files-survive)

Deploy, upload a test file, deploy again without changes, and open the file. If it still loads, uploads now live outside the instance. Search your code for any other runtime writes to local paths, such as generated PDFs or exported CSVs, and move them the same way.

For generated files, the [customer-report hosting guide](https://www.prisma.io/compute/customer-report-hosting) connects private downloads with customer-scoped queries, report status and a durable generation workflow.

## [Storing uploads with Prisma Compute and Prisma Postgres](https://www.prisma.io#storing-uploads-with-prisma-compute-and-prisma-postgres)

[Prisma Compute](https://www.prisma.io/docs/compute) has no persistent filesystem, so the local `uploads/` folder from the start of this page doesn't work there either. Its storage option is an Object Store bucket: S3-compatible storage that lives in the same Prisma project as your [Prisma Postgres](https://www.prisma.io/docs/postgres) database, managed from the Console, the CLI or the REST API.

To run the Express example above on Compute, deploy it as a [Prisma Composer](https://www.prisma.io/docs/composer) service, which is how apps deploy to Compute. Declare the service with `compute()` and two dependencies from `@prisma/composer-prisma-cloud`, `store: bucket()` and `db: rawPostgres()`, then provision both in your `module.ts`:

Provisioning the bucket also mints its access key, so there are no storage credentials to copy. The server code changes in three places, following [porting an app](https://www.prisma.io/docs/composer/porting-an-app) and [object storage in Composer](https://www.prisma.io/docs/composer/object-storage):

Your build has to produce a self-contained entry file, and `npx prisma dev` runs the app locally against a stand-in bucket and database; [porting an app](https://www.prisma.io/docs/composer/porting-an-app) covers the build and the `service.ts` declaration. The `uploads` table goes in the provisioned Prisma Postgres database. To keep an existing Postgres database instead, pass its connection string as a secret [service input](https://www.prisma.io/docs/composer/service-input) rather than declaring `rawPostgres()`. Prisma ORM is optional either way: the example uses the `pg` driver.

The [object storage guide](https://www.prisma.io/docs/compute/object-storage) shows the other route: create the bucket and a key yourself, store the four values as environment variables, and read them with Bun's built-in S3 client (`Bun.s3`), which picks up these names without configuration:

`bucket key create` mints a `read_write` key unless you pass `--role read`. Its secret is shown once, so copy it right away. A deployment that only serves files can hold a `read` key, but a write with a `read` key fails with `AccessDenied`. Values resolve at deploy time, so set them before you deploy.

Things to know before you rely on it:

- **Object Store pricing and plan limits are not published yet.** The Free plan's 2 GB is Prisma Postgres database storage, which holds the `uploads` table, not the files; [pricing](https://www.prisma.io/pricing) has the other plans.
- **Deleting a bucket deletes its files and keys in one step**, even when it isn't empty, and can't be undone.
- **Requests have 60 seconds to start responding.** An upload that passes through your app has to finish arriving before your handler can respond, so it has to fit in that window; see [request timeout](https://www.prisma.io/docs/compute/request-timeout).

## [How to prevent it, and when the fix doesn't apply](https://www.prisma.io#how-to-prevent-it-and-when-the-fix-doesnt-apply)

Treat every instance's disk as temporary from the start. Write uploads, generated files and anything else customers expect to find again to object storage or the database, and keep local disk for scratch files that a single request creates and deletes. A test that deploys twice and checks an uploaded file between deploys catches a regression before customers do.

Object storage is the wrong fit when your app or a tool it depends on needs a real filesystem that persists: a SQLite database file, a CMS that writes its media folder to disk, or software that expects POSIX file locking. Use a host with persistent disks or volumes for those, accept that the app runs as a single instance, and back the disk up. Prisma Compute doesn't offer persistent disks, so it is the wrong host for that kind of app. [Moving SQLite data to Postgres](https://www.prisma.io/postgres/app-data-lost-after-restart) solves the database part of the problem, because the data then lives outside the instance.

## Frequently asked questions

`bytea` column, which keeps everything in one place, but every upload then makes the database and its backups larger and every download goes through a database query. For customer uploads such as photos, PDFs and CSVs, put the file in object storage and keep a row in Postgres with its key, owner, name, type and size.
[Render disks](https://render.com/docs/disks),

[Railway volumes](https://docs.railway.com/volumes/reference)and

[Fly Volumes](https://docs.fly.io/volumes/overview)keep files across deploys, but each is attached to a single instance: Render can't scale a service with a disk to more instances, Railway can't use replicas with a volume, and a Fly Volume attaches to one Machine. Render and Railway also note a short downtime on each deploy of a service with a disk or volume. Object storage isn't tied to an instance, so it avoids these trade-offs.

[Heroku](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), for example, discards files a dyno wrote as soon as it stops or restarts. Check whether copies exist elsewhere: a CDN cache, an email attachment, a backup job or the customer's own device. Files written since the last deploy or restart may still be on the running instance, so copy them to the bucket before you deploy again.

## Keep uploads next to your database

Create an Object Store bucket in your Prisma project, give your app a key, and read and write files with any S3 client.