---
id: "prisma_orm_075"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 75
source_url: "https://www.prisma.io/compare/kysely"
language: "en"
retrieved_at: "2026-11-01 22:19:44"
content_hash: "e41088d37e7ff8509454f9a3cda55e935da948d6860797e74d5ced0571e2434e"
---

# Prisma ORM

Source: https://www.prisma.io/compare/kysely

---

[Compare](https://www.prisma.io/compare)Kysely

# Prisma ORM vs Kysely: contract file or SQL query builder?

Both give you type-safe database access in TypeScript, from opposite ends. [Prisma ORM](https://www.prisma.io/docs/orm) starts from a contract file: you describe your models once, and typed queries and migrations follow from it. [Kysely](https://kysely.dev) starts from SQL: you write each query as a fluent TypeScript builder over table types you keep yourself.

[Get started with Prisma ORM](https://www.prisma.io/docs/prisma-orm/quickstart/postgresql) [Create an instant database](https://create-db.prisma.io/web)

By [Martin Janse van Rensburg](https://www.prisma.io/blog/author/martin-janse-van-rensburg) · Updated  · 12 min read[X](https://x.com/vanrensbird)[LinkedIn](https://www.linkedin.com/in/martjvr/)[GitHub](https://github.com/vanrensbird)

Prisma makes Prisma ORM. Kysely figures come from the pages listed under [Sources](https://www.prisma.io#sources), checked October 2026.

## When should I choose Kysely or Prisma ORM?

| Kysely | Prisma ORM | 
|---|---|
| You want the library itself to be the SQL query builder, with no contract file — a contract is the `contract.prisma` file that describes your models. | You want models and relations in a contract file, `contract.prisma`. | 
| You want table types as TypeScript interfaces, written by hand or produced by a generator. | You want typed model queries and a SQL query builder from the same database client. | 
| You want up and down migrations as TypeScript functions you write. An optional CLI lives in `kysely-ctl`. | You want `migration plan` to write a TypeScript migration from that contract. `db sign` records that the database already matches the contract. | 
| You need a built-in dialect — Kysely's adapter for one database — for MySQL, Microsoft SQL Server, or PGlite, which Prisma ORM 8 does not ship. | You want related records as part of the model API, as in `db.orm.public.User.include`. | 

## What does the same query look like in each?

Each snippet reads one user by email with their posts: Kysely nests the posts with its `jsonArrayFrom` helper, and Prisma ORM loads them with `include`. The SQL tab is representative of the statements both send, not captured from a live run.

posts includeemail filterTinted lines match across the open tab. Hover one to emphasize its pair.

## How do Prisma ORM and Kysely compare feature by feature?

Kysely is a SQL query builder. Prisma ORM is a contract-based ORM that also includes a SQL query builder on PostgreSQL and SQLite. Columns are in alphabetical order.

| Feature | Kysely | Prisma ORM | 
|---|---|---|
| Library price | Free. MIT license. | Free. Apache License 2.0. | 
| Release status | Version 0.29.7 on npm, so not yet a 1.0 release. The getting started guide requires TypeScript 5.4 or newer, and strict mode. | Prisma ORM 8 is a release candidate, and it is what `npm install prisma` gives you. The final release is still to come. | 
| Data model | TypeScript interfaces you provide. A dialect also needs its driver, such as `pg` for PostgreSQL. | A contract file, `contract.prisma`. `contract emit` writes the types. `contract infer` writes a starter contract from PostgreSQL tables you already have. There is no `@prisma/client` package. | 
| Queries | A fluent SQL builder: `selectFrom`, `where`, and the other clauses in the guide. | An ORM client for model queries, a SQL query builder on PostgreSQL and SQLite, and raw SQL for a statement neither API expresses. | 
| Migrations | up and down functions you write. Pending migrations run in alphanumeric order, with an option for unordered migrations. | `migration plan` writes `migration.ts` from the contract. On PostgreSQL, `migration show` prints the SQL. `db migrate` runs `ops.json`, not the TypeScript file. | 
| Databases | Built-in dialects for PostgreSQL, MySQL, Microsoft SQL Server, SQLite, and PGlite. See [database support](https://www.prisma.io#databases). | PostgreSQL, MongoDB, and SQLite in Prisma ORM 8. The rest stay on Prisma ORM 7. See [database support](https://www.prisma.io#databases). | 
| Hosted database | None. Kysely is a library. | [Prisma Postgres](https://www.prisma.io/docs/postgres) is a separate product. Any Postgres client works with it, so Prisma ORM is optional. [Prisma Compute](https://www.prisma.io/docs/compute) is separate app hosting. | 

## Which databases do Prisma ORM and Kysely support?

Kysely's dialects next to the two Prisma ORM lines. Prisma ORM 7 is the generally available release, and it supports every database here except PGlite. No means no support.

| Database | Kysely | Prisma ORM 8 | Prisma ORM 7 | 
|---|---|---|---|
| PostgreSQL | Built-in | Release candidate | Supported | 
| MySQL | Built-in | ORM 7 only | Supported | 
| MariaDB | Community dialect | ORM 7 only | Supported | 
| Microsoft SQL Server | Built-in | ORM 7 only | Supported | 
| SQLite | Built-in | Experimental | Supported | 
| CockroachDB | No | ORM 7 only | Supported | 
| MongoDB | No | Early access | Supported | 
| PGlite | Built-in | No | No | 

MariaDB on Kysely is the community [kysely-mariadb](https://github.com/awaludinar/kysely-mariadb) dialect. Sources: [Kysely dialects](https://kysely.dev/docs/dialects), [Prisma ORM 8 supported databases](https://www.prisma.io/docs/orm/supported-databases), and [Prisma ORM 7 supported databases](https://www.prisma.io/docs/orm/v7/reference/supported-databases), October 2026.

## What does Prisma ORM do that Kysely doesn't?

### A model API and a SQL query builder

The ORM client answers model queries. The SQL query builder, on PostgreSQL and SQLite, takes joins and aggregates the client does not expose. Raw SQL covers a statement neither API expresses.

### A migration plan that does not need the database

`migration plan` reads the contract and writes the migration. Planning does not connect to a database, so it can run without database credentials.

## How much do Prisma ORM and Kysely cost?

| Cost | Kysely | Prisma ORM | 
|---|---|---|
| Library license and cost | Free, MIT | Free, Apache 2.0 | 
| Paid plans | None | None for the ORM | 
| Hosted database | None. You bring your own. | [Prisma Postgres](https://www.prisma.io/docs/postgres), optional. It works with any Postgres client, Kysely included. | 

Prisma Postgres has a Free plan: $0 a month for 200,000 operations, 2 GB of storage, and 50 databases. The [pricing page](https://www.prisma.io/pricing) lists the paid plans.

## When is Prisma ORM the wrong choice?

- You want a SQL query builder and no contract file. Kysely takes a TypeScript `Database` interface, a dialect, and that dialect's driver.
- You need MySQL, MariaDB, SQL Server, or CockroachDB from the current Prisma ORM 8 packages. Those databases are not in ORM 8 yet. [Prisma ORM 7](https://www.prisma.io/docs/orm/v7) still supports them, and Kysely has built-in dialects for MySQL, SQL Server, and SQLite. See [supported databases](https://www.prisma.io/docs/orm/supported-databases).

## How does each task look in Kysely and Prisma ORM?

What each step of the usual workflow looks like on each side, for a team moving in either direction.

| Task | Kysely | Prisma ORM | 
|---|---|---|
| Define tables | A TypeScript `Database` interface, with one property per table. | Models in `contract.prisma`. | 
| Generate types | Nothing to generate if you write the interface by hand. Community generators such as `kysely-codegen` write it for you. | `contract emit` writes the types from the contract. | 
| Read an existing database | `kysely-codegen` connects to PostgreSQL, MySQL, SQLite, or SQL Server and writes the `Database` interface. | Inspects a live database and writes a starter `contract.prisma`. | 
| Write a migration | `up` and `down` functions you write with `db.schema`. `kysely migrate make` from `kysely-ctl` creates the file. | `migration plan` writes `migration.ts` from the contract. | 
| Preview query SQL | `.compile()` on a query returns its SQL and parameters without running it. | `.build()` on the SQL query builder returns the query without running it. | 
| Preview migration SQL | You read the SQL you wrote in the `up` function. There is no separate preview command. | A CLI preview prints a migration's operations and statement preview, without connecting to the database. | 
| Run migrations | `Migrator` from `kysely/migration`, with `migrateToLatest()`. `kysely-ctl` wraps it as `kysely migrate latest`. | `db migrate` applies the pending migrations on disk. | 

## How do I switch from Kysely to Prisma ORM?

For PostgreSQL, these four commands from the [existing-database guide](https://www.prisma.io/docs/prisma-orm/add-to-existing-project/postgresql) add Prisma ORM beside the tables you already have. The Node.js versions that guide expects still apply. Signing records that the database already matches the contract, so the first `migration plan` starts from your tables instead of an empty database. The rows stay where they are.

Representative types for the User and Post tables in the query above, then the four commands.

1. Later changes go through [contract emit and migration plan](https://www.prisma.io/docs/orm/migrations/generating-a-migration). On PostgreSQL, `migration show` prints the SQL.

## How do I switch from Prisma ORM to Kysely?

1. Keep the database and the connection string.
2. Add a TypeScript `Database` interface that matches the tables. A community generator can emit those types from a Prisma schema. Prisma documents it on the [Prisma ORM 7 generators](https://www.prisma.io/docs/orm/v7/prisma-schema/overview/generators) page. It is not part of Prisma ORM.
3. Create one Kysely instance with the dialect that matches the database, plus that dialect's driver. On PostgreSQL that is `PostgresDialect` and `pg`. On Prisma Postgres, follow the [Kysely quickstart](https://www.prisma.io/docs/prisma-postgres/quickstart/kysely). Prisma ORM is optional there.

## What do teams say about Prisma ORM?

Two teams on what type safety in Prisma ORM does for them.

## Frequently asked questions

Yes. Kysely ships a migrator that runs the `up` and `down` functions you write by hand, so many teams add a separate tool to generate them. Prisma writes the migration for you from your schema. In Prisma 7, `prisma migrate dev` compares your schema with the database, writes a plain SQL file you can edit, and applies it, while `prisma migrate deploy` applies migrations in production. Prisma 8 (release candidate) keeps the idea with new commands: `prisma migration plan` writes a TypeScript migration you can review, and `prisma db migrate` applies it. To try it, [Prisma Postgres](https://www.prisma.io/postgres) has a free plan with 50 databases, 2 GB and 200k operations a month, no card needed.

```
# Prisma 7
npx prisma migrate dev --name add_user_phone
# Prisma 8 (release candidate)
npx prisma migration plan --name add_user_phone
npx prisma db migrate
```
Kysely's own docs are upfront that it has no concept of relations, so you nest rows with SQL JSON helpers such as `jsonArrayFrom`. Prisma knows your relations from the schema, so you just ask for them. In Prisma 7 you use `include` or `select`, nest as deep as you like, and filter parents by their children with `some`, `every` and `none`. Prisma 7 can load it all in one SQL query with `relationLoadStrategy: "join"`, which is still in Preview. Prisma 8 (release candidate) uses a chained `.include()` that reads the relation in the same SQL statement as the parent, with a callback to filter, sort or limit it.

```
// Prisma 7
const users = await prisma.user.findMany({
  include: { posts: { where: { published: true }, take: 5 } },
});
// Prisma 8 (release candidate)
const users = await db.orm.public.User
  .include("posts", (p) => p.where({ published: true }).limit(5))
  .all();
```
Yes. With a query builder you usually write each insert yourself and wrap them in a transaction. Prisma 7 has nested writes: inside one `create` or `update` you can create, connect, update or delete related records, and Prisma runs it all as a single transaction, rolling everything back if any part fails. Prisma 8 (release candidate) supports nested `create`, `connect` and `disconnect`. Nested update, upsert, delete and `connectOrCreate` are not in Prisma 8 yet, so for those you change the related rows through their own model inside `db.transaction(...)`.

```
// Prisma 7: one query, one transaction
await prisma.user.create({
  data: {
    email: "elsa@prisma.io",
    posts: { create: [{ title: "Hello" }, { title: "Second post" }] },
  },
});
// Prisma 8 (release candidate)
await db.orm.public.User.create({
  email: "elsa@prisma.io",
  posts: (p) => p.create([{ title: "Hello", published: false }]),
});
```
Kysely has no built-in way to do it, so you set the column in every update, add a database trigger, or write your own plugin. In Prisma you mark the field once in the schema and Prisma fills it in on every write. In Prisma 7 that is the `@updatedAt` attribute. In Prisma 8 (release candidate) it is `temporal.updatedAt()`, which sets the time on every create and update from your application's clock. One thing to know: because the value comes from the app, a row you insert with raw SQL has to supply it.

```
// Prisma 7: schema.prisma
model Post {
  id        Int      @id @default(autoincrement())
  updatedAt DateTime @updatedAt
}
// Prisma 8 (release candidate): contract.prisma
// use prisma-8
model Post {
  id        Int @id @default(autoincrement())
  updatedAt temporal.updatedAt()
}
```
For everyday reads and writes, usually yes, because Prisma gives you methods for each model. Kysely asks you to spell out each step, which is great for complex SQL but adds up for simple CRUD. In Prisma 7, a create returns the new record by default. Prisma 8 (release candidate) trims it further: no `data` wrapper, and an update or delete without a `.where(...)` does not type-check, so you can't wipe a table by accident. When you do want SQL, Prisma 7 has `$queryRaw` and TypedSQL (Preview), and Prisma 8 has a typed SQL query builder.

```
// Kysely
await db.insertInto("user").values({ email, name }).returningAll().executeTakeFirstOrThrow();
// Prisma 7
await prisma.user.create({ data: { email, name } });
// Prisma 8 (release candidate)
await db.orm.public.User.create({ email, name });
```
If you need something stable today, use Prisma 7. It is the current stable release, it supports PostgreSQL, MySQL, SQLite, SQL Server, CockroachDB and MongoDB, and it will keep getting bug fixes and security updates for 18 months after Prisma 8 reaches general availability. Prisma 8 is a release candidate: PostgreSQL is the most complete, MongoDB is in early access, SQLite is experimental, and MySQL is not supported yet. Note that a plain `npm install prisma` now installs the Prisma 8 release candidate, so pin `prisma@7` if you want version 7.

```
# Prisma 7 (stable)
npm install --save-dev prisma@7
# Prisma 8 (release candidate)
npm install --save-dev prisma
npm install @prisma/orm-postgres
```
## Add Prisma ORM to an existing project

Prisma ORM is free and open source, and always will be.

- Add the library
- Read the ORM docs
- Trusted by 500K+ developers globally

Need a database? [Create an instant database](https://create-db.prisma.io/web).

[Get started with Prisma ORM](https://www.prisma.io/docs/prisma-orm/quickstart/postgresql) [Get started with Prisma Postgres](https://console.prisma.io)

## Sources

Every competitor figure on this page comes from these pages, checked October 2026.