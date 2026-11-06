---
id: "sql_045"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 45
source_url: "https://www.postgresql.org/about/press/presskit18/en"
language: "en"
retrieved_at: "2026-11-01 21:57:30"
content_hash: "184afe3bcc8b809ba885a34720b8a50bd788d6f70c1361b2617884e87d6d91f9"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit18/en

---

**September 25, 2025** - The
  [PostgreSQL Global Development Group](https://www.postgresql.org)
  today announced the release of [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html),
  the latest version of the world's most advanced open source database.

PostgreSQL 18 improves performance for workloads of all sizes through a new
  I/O subsystem that has demonstrated up to 3× performance improvements when
  reading from storage, and also increases the number of queries that can use
  indexes. This release makes major-version upgrades less disruptive,
  accelerating upgrade times and reducing the time required to reach expected
  performance after an upgrade completes. Developers also benefit from
  PostgreSQL 18 features, including virtual generated columns that compute
  values at query time, and the database-friendly `uuidv7()`
  function that provides better indexing and read performance for UUIDs.
  PostgreSQL 18 makes it easier to integrate with single-sign on (SSO) systems
  with support for OAuth 2.0 authentication.

"The efforts of the global open source community shape every PostgreSQL release and help deliver features that meet users where their data resides," said Jonathan Katz, a member of the PostgreSQL core team. "PostgreSQL 18 builds on the project's long, rich history of delivering a reliable and robust data management experience, while continuing to expand the workloads it can support."

PostgreSQL, an innovative data management system known for its reliability, robustness, and extensibility, benefits from nearly 30 years of open source development from a global developer community and has become the preferred open source relational database for organizations of all sizes.

PostgreSQL previously relied on operating system readahead mechanisms to accelerate data retrieval. However, because operating systems lack insight into database-specific access patterns, they cannot always anticipate what data will be required, leading to suboptimal performance in many workloads.

PostgreSQL 18 introduces a new asynchronous I/O (AIO) subsystem designed to address this limitation. AIO lets PostgreSQL issue multiple I/O requests concurrently instead of waiting for each to finish in sequence. This expands existing readahead and improves overall throughput. AIO operations supported in PostgreSQL 18 include sequential scans, bitmap heap scans, and vacuum. Benchmarking has demonstrated performance gains of up to 3x in certain scenarios.

The new [`io_method`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-IO-METHOD)
  setting lets you toggle between the AIO methods, including `worker` and `io_uring`,
  or you can choose to maintain the current PostgreSQL behavior with the `sync`
  setting. There are now more parameters to consider tuning with AIO, which you
  can [learn more about in the documentation](https://www.postgresql.org/docs/18/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-IO).

A key PostgreSQL feature is the generation and storage of
[statistics](https://www.postgresql.org/docs/18/planner-stats.html) that help
PostgreSQL select the most efficient query plan. Before PostgreSQL 18, these
statistics didn't carry over on a [major version upgrade](https://www.postgresql.org/docs/18/pgupgrade.html),
which could cause significant query performance degradations on busy systems
until the [`ANALYZE`](https://www.postgresql.org/docs/18/sql-analyze.html)
finished running. PostgreSQL 18 introduces the ability to keep planner
statistics through a major version upgrade, which helps an upgraded cluster
reach expected performance more quickly after the upgrade.

Additionally, [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html),
a utility that performs major version upgrades, includes several enhancements in
PostgreSQL 18, such as faster upgrades when a database contains many objects
like tables and sequences. This release also lets `pg_upgrade` process its
checks in parallel based on the settings of the `--jobs` flag, and adds the
`--swap` flag that swaps upgrade directories instead of copying, cloning, or
linking files.

PostgreSQL 18 further accelerates query performance with features that
  automatically make your workloads faster. This release introduces "skip scan"
  lookups on [multicolumn B-tree indexes](https://www.postgresql.org/docs/18/indexes-multicolumn.html)
  that improve execution time for queries that omit an `=` condition on one or
  more prefix index columns. It can also optimize queries that use `OR` conditions
  in a `WHERE` to use an index, leading to significantly faster execution. There
  are also numerous improvements for how PostgreSQL plans and executes table joins,
  from boosting the performance of hash joins to allowing merge joins to use
  incremental sorts. PostgreSQL 18 also supports parallel builds for
  [GIN indexes](https://www.postgresql.org/docs/18/gin.html), joining B-tree and
  [BRIN indexes](https://www.postgresql.org/docs/current/brin.html) in supporting
  this capability.

This release also builds on PostgreSQL support for hardware acceleration,
  including support for ARM NEON and SVE CPU intrinsics for the `popcount`
  function, which is used by the [`bit_count`](https://www.postgresql.org/docs/18/functions-bitstring.html)
  and other internal capabilities.

PostgreSQL 18 introduces [virtual generated columns](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-STORED)
  that compute values at query time instead of storing them. This is now the
  default option for generated columns. Additionally, stored generated columns
  can now be logically replicated.

This release adds the capability to access both the previous (`OLD`)
  and current (`NEW`) values in the
  [`RETURNING` clause](https://www.postgresql.org/docs/18/dml-returning.html)
  for `INSERT`, `UPDATE`, `DELETE` and `MERGE`
  commands. PostgreSQL 18 also adds UUIDv7 generation through the
  [`uuidv7()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE)
  function, letting you generate random UUIDs that are timestamp-ordered to
  support better caching strategies. PostgreSQL 18 includes
  [`uuidv4()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE)
  as an alias for `gen_random_uuid()`.

PostgreSQL 18 adds [temporal constraints](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-UNIQUE)
  -- constraints over ranges -- for both `PRIMARY KEY` and `UNIQUE`
  constraints using the `WITHOUT OVERLAPS` clause, and on
  `FOREIGN KEY` constraints using the `PERIOD` clause.

Finally, PostgreSQL 18 makes it easier to create the schema definition of a
  foreign table using the definition of a local table with the
  [`CREATE FOREIGN TABLE ... LIKE`](https://www.postgresql.org/docs/18/sql-createforeigntable.html)
  command.

PostgreSQL 18 makes text processing easier and faster with several new
  enhancements. This release adds the [`PG_UNICODE_FAST`](https://www.postgresql.org/docs/18/collation.html#COLLATION-MANAGING-STANDARD)
  collation, which provides full Unicode semantics for case transformations while
  helping to accelerate many comparisons. This includes the `upper` and `lower`
  string comparison functions and the new [`casefold`](https://www.postgresql.org/docs/18/functions-string.html#FUNCTIONS-STRING-OTHER)
  function for case-insensitive comparisons. Additionally, PostgreSQL 18 now
  supports making `LIKE` comparisons over text that uses a
  [nondeterministic collation](https://www.postgresql.org/docs/18/collation.html#COLLATION-NONDETERMINISTIC),
  simplifying how you can perform more complex pattern matching. This release also
  changes [full text search](https://www.postgresql.org/docs/18/textsearch.html)
  to use the default collation provider of a cluster instead of always using libc,
  which may require you to reindex all
  [full text search](https://www.postgresql.org/docs/18/textsearch-tables.html#TEXTSEARCH-TABLES-INDEX)
  and [`pg_trgm`](https://www.postgresql.org/docs/18/pgtrgm.html#PGTRGM-INDEX)
  indexes after running [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html).

PostgreSQL 18 introduces [`oauth` authentication](https://www.postgresql.org/docs/18/auth-oauth.html),
  which lets users authenticate using OAuth 2.0 mechanisms supported through
  PostgreSQL extensions. Additionally, PostgreSQL 18 includes validation for
  [FIPS mode](https://www.postgresql.org/docs/18/pgcrypto.html#PGCRYPTO-OPENSSL-SUPPORT-FUNCS),
  and adds the [`ssl_tls13_ciphers`](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-SSL-TLS13-CIPHERS)
  parameter for configuring server-side TLS v1.3 cipher suites.

This release deprecates `md5` password authentication, which will
  be removed in a future release. If you require PostgreSQL password-based
  authentication, use [SCRAM authentication](https://www.postgresql.org/docs/18/auth-password.html).
  PostgreSQL 18 also supports SCRAM passthrough authentication with both
  [`postgres_fdw`](https://www.postgresql.org/docs/18/postgres-fdw.html)
  and [`dblink`](https://www.postgresql.org/docs/18/dblink.html)
  for authenticating to remote PostgreSQL instances. Additionally,
  [`pgcrypto`](https://www.postgresql.org/docs/18/pgcrypto.html)
  now supports [SHA-2 encryption for password hashing](https://www.postgresql.org/docs/18/pgcrypto.html#PGCRYPTO-CRYPT-ALGORITHMS).

PostgreSQL 18 supports reporting logical replication write conflicts in logs and
  in the [`pg_stat_subscription_stats`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-SUBSCRIPTION-STATS) view. Additionally,
  [`CREATE SUBSCRIPTION`](https://www.postgresql.org/docs/18/sql-createsubscription.html)
  now defaults to using parallel streaming for applying transactions, which can
  help improve performance. The
  [`pg_createsubscriber`](https://www.postgresql.org/docs/18/app-pgcreatesubscriber.html)
  utility now has an `--all` flag so you can create logical replicas for all
  databases in an instance with a single command. PostgreSQL 18 also lets you
  automatically [drop idle replication slots](https://www.postgresql.org/docs/18/runtime-config-replication.html#GUC-IDLE-REPLICATION-SLOT-TIMEOUT) to help prevent storing too many
  write-ahead log files on a publisher.

PostgreSQL 18 improves its [vacuum](https://www.postgresql.org/docs/18/routine-vacuuming.html)
  strategy by proactively freezing more pages during regular vacuums, reducing
  overhead and helping in situations that require aggressive vacuums.

PostgreSQL 18 adds more details to [`EXPLAIN`](https://www.postgresql.org/docs/18/using-explain.html),
  which provides information about query plan execution, and as of this release
  now automatically shows how many buffers (the fundamental unit of data storage)
  are accessed when executing `EXPLAIN ANALYZE`. Additionally, `EXPLAIN ANALYZE`
  now shows how many index lookups occur during an index scan, and `EXPLAIN ANALYZE VERBOSE`
  includes CPU, WAL, and average read statistics. PostgreSQL 18 includes more info
  in [`pg_stat_all_tables`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW)
  on time spent on vacuum and related operations, as well as per-connection
  statistics on I/O and WAL utilization.

Databases initialized with PostgreSQL 18 [`initdb`](https://www.postgresql.org/docs/18/app-initdb.html)
  now have page checksums enabled by default. This can affect upgrades from
  non-checksum enabled clusters, which would require you to create a new
  PostgreSQL 18 cluster with the `--no-data-checksums` option when using
  [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html).

PostgreSQL 18 also introduces a new version (3.2) of the PostgreSQL wire
  protocol, the first new protocol version since PostgreSQL 7.4 (2003).
  [`libpq`](https://www.postgresql.org/docs/18/libpq-connect.html) still uses
  version 3.0 by default while clients (e.g., drivers, poolers, proxies) add
  support for the new protocol version.

Many other new features and improvements have been added to PostgreSQL 18 that
  may also be helpful for your use cases. Please see the
  [release notes](https://www.postgresql.org/docs/18/release-18.html) for a
  complete list of new and changed features.

[PostgreSQL](https://www.postgresql.org) is the world's most
  advanced open source database, with a global community of thousands of users,
  contributors, companies and organizations. Since its beginnings at the
  University of California, Berkeley over 40 years ago, PostgreSQL has continued
  with an unmatched pace of development. PostgreSQL's mature feature set not
  only matches top proprietary database systems, but exceeds them in advanced
  database features, extensibility, security, and stability.

[PostgreSQL](https://www.postgresql.org) is the world's most
  advanced open source database, with a global community of thousands of users,
  contributors, companies and organizations. Built on over 35 years of
  engineering, starting at the University of California, Berkeley, PostgreSQL
  has continued with an unmatched pace of development. PostgreSQL's mature
  feature set not only matches top proprietary database systems, but exceeds
  them in advanced database features, extensibility, security, and stability.

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

For explanations of the above features and others, please see the following resources:

There are several ways you can download PostgreSQL 18, including:

Other tools and extensions are available on the
  [PostgreSQL Extension Network](http://pgxn.org).

PostgreSQL 18 comes with HTML documentation as well as man
  pages, and you can also browse the documentation online in both
  [HTML](https://www.postgresql.org/docs/18/) and [PDF](https://www.postgresql.org/files/documentation/pdf/18/postgresql-18-US.pdf) formats.

PostgreSQL uses the [PostgreSQL License](https://www.postgresql.org/about/licence/), a
  BSD-like "permissive" license. This [OSI-certified license](http://www.opensource.org/licenses/postgresql/)
  is widely appreciated as flexible and business-friendly, since it does not
  restrict the use of PostgreSQL with commercial and proprietary applications.
  Together with multi-company support and public ownership of the code, our
  license makes PostgreSQL very popular with vendors wanting to embed a database
  in their own products without fear of fees, vendor lock-in, or changes in
  licensing terms.

Website

Postgres and PostgreSQL and the Elephant Logo (Slonik) are all registered
  trademarks of the [PostgreSQL Community Association](https://www.postgres.ca).
  If you wish to use these marks, you must comply with the [trademark policy](https://www.postgresql.org/about/policies/trademarks/).

PostgreSQL enjoys the support of numerous companies, who sponsor developers,
  provide hosting resources, and give us financial support. See our
  [sponsors](https://www.postgresql.org/about/sponsors/) page for
  some of these project supporters.

There is also a large community of
  [companies offering PostgreSQL Support](https://www.postgresql.org/support/professional_support/),
  from individual consultants to multinational companies.

If you wish to make a financial contribution to the PostgreSQL Global
  Development Group or one of the recognized community non-profit organizations,
  please visit our [donations](https://www.postgresql.org/about/donate/)
  page.