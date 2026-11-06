---
id: "sql_039"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 39
source_url: "https://www.postgresql.org/about/press/presskit13/en"
language: "en"
retrieved_at: "2026-11-01 21:57:06"
content_hash: "023dee653ab09ccd3428f7c79969329ddf9f349ec057c22a1a41b092c3a17530"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit13/en

---

**SEPTEMBER 24, 2020** - The PostgreSQL Global Development Group
  today announced the release of [PostgreSQL 13](https://www.postgresql.org/docs/13/release-13.html),
  the latest version of the world’s [most advanced open source database](https://www.postgresql.org/).

PostgreSQL 13 includes significant improvements to its indexing and lookup system that benefit large databases, including space savings and performance gains for indexes, faster response times for queries that use aggregates or partitions, better query planning when using enhanced statistics, and more.

Along with highly requested features like [parallelized vacuuming](https://www.postgresql.org/docs/13/sql-vacuum.html)
  and [incremental sorting](https://www.postgresql.org/docs/13/runtime-config-query.html#GUC-ENABLE-INCREMENTAL-SORT),
  PostgreSQL 13 provides a better data management experience for workloads big
  and small, with optimizations for daily administration, more conveniences for
  application developers, and security enhancements.

"PostgreSQL 13 showcases the collaboration and dedication of our global community in furthering the abilities of the world's most advanced open source relational database," said Peter Eisentraut, a PostgreSQL Core Team member. "The innovations that each release brings along with its reputation for reliability and stability is the reason why more people choose to use PostgreSQL for their applications."

[PostgreSQL](https://www.postgresql.org), an innovative data
  management system known for its reliability and robustness, benefits from over
  25 years of open source development from a [global developer community](https://www.postgresql.org/community/)
  and has become the preferred open source relational database for organizations
  of all sizes.

Building on work from the previous PostgreSQL release, PostgreSQL 13 can
  efficiently handle [duplicate data in B-tree indexes](https://www.postgresql.org/docs/13/btree-implementation.html#BTREE-DEDUPLICATION),
  the standard database index. This lowers the overall space usage that B-tree
  indexes require while improving overall query performance.

PostgreSQL 13 introduces incremental sorting, where sorted data from an
  earlier step in a query can accelerate sorting at a later step. Additionally,
  PostgreSQL can now use the [extended statistics](https://www.postgresql.org/docs/13/planner-stats.html#PLANNER-STATS-EXTENDED)
  system (accessed via [`CREATE STATISTICS`](https://www.postgresql.org/docs/13/sql-createstatistics.html))
  to create improved plans for queries with `OR` clauses and `IN`/`ANY` lookups
  over lists.

In PostgreSQL 13, more types of [aggregate](https://www.postgresql.org/docs/13/functions-aggregate.html)
  and [grouping set](https://www.postgresql.org/docs/13/queries-table-expressions.html#QUERIES-GROUPING-SETS)
  queries can leverage PostgreSQL’s efficient hash aggregation functionality, as
  queries with large aggregates do not have to fit entirely into memory. Queries
  with [partitioned tables](https://www.postgresql.org/docs/13/ddl-partitioning.html)
  have received a performance boost, as there are now more cases where partitions
  can be pruned and where partitions can be directly joined.

[Vacuuming](https://www.postgresql.org/docs/13/routine-vacuuming.html) is an essential part
  of PostgreSQL administration, enabling the database to reclaim storage space
  after rows are updated and deleted. This process can also present
  administrative challenges, though prior PostgreSQL releases have done work to
  ease the overhead of vacuuming.

PostgreSQL 13 continues to improve the vacuuming system with the introduction
  of [parallelized vacuum for indexes](https://www.postgresql.org/docs/13/sql-vacuum.html).
  In addition to the vacuuming performance benefits it offers, the use of this
  new feature can be tuned to specific workloads as administrators can select
  the number of parallel workers to run. In addition to these performance
  benefits, data inserts can now trigger the autovacuum process.

[Replication slots](https://www.postgresql.org/docs/13/warm-standby.html#STREAMING-REPLICATION-SLOTS),
  which are used to prevent write-ahead logs (WAL) from being removed before
  they are received by a replica, can be tuned in PostgreSQL 13 to specify the
  [max number of WAL files to retain](https://www.postgresql.org/docs/13/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE)
  and help avoid out-of-disk errors.

PostgreSQL 13 also adds more ways an administrator can monitor database
  activity, including referencing WAL usage statistics from `EXPLAIN`,
  the progress of streaming base backups, and the progress of the `ANALYZE`
  commands. Additionally, the integrity of the output of the
  [`pg_basebackup`](https://www.postgresql.org/docs/13/app-pgbasebackup.html)
  command can be checked using the new [`pg_verifybackup`](https://www.postgresql.org/docs/13/app-pgverifybackup.html)
  command.

PostgreSQL 13 makes it even easier to work with PostgreSQL data types coming
  from different data sources. This release adds the
  [`datetime()`](https://www.postgresql.org/docs/13/functions-json.html#FUNCTIONS-SQLJSON-OP-TABLE)
  function to its SQL/JSON path support, which converts valid time formats (e.g.
  ISO 8601 strings) to PostgreSQL-native types. Additionally, the UUID v4
  generation function, [`gen_random_uuid()`](https://www.postgresql.org/docs/13/functions-uuid.html),
  is now available without having to install any extensions.

PostgreSQL’s partitioning system is more flexible, as partitioned tables fully support logical replication and BEFORE row-level triggers.

The [`FETCH FIRST`](https://www.postgresql.org/docs/13/sql-select.html#SQL-LIMIT)
  syntax in PostgreSQL 13 is now expanded to include the `WITH TIES`
  clause. When specified, `WITH TIES` includes any rows that, based
  on the `ORDER BY` clause, "tie" with the last row in the result set.

PostgreSQL’s extension system is a key component of its robustness as it allows
  developers to expand its functionality. In previous releases, new extensions
  could only be installed by a database superuser. To make it easier to take
  advantage of PostgreSQL’s extensibility, PostgreSQL 13 adds the concept of a
  "[trusted extension](https://www.postgresql.org/docs/13/sql-createextension.html),"
  which allows database users to install extensions that a superuser marks as
  "trusted." Certain built-in extensions are marked as trusted by default,
  including [`pgcrypto`](https://www.postgresql.org/docs/13/pgcrypto.html),
  [`tablefunc`](https://www.postgresql.org/docs/13/tablefunc.html),
  [`hstore`](https://www.postgresql.org/docs/13/hstore.html), and more.

For applications that require secure authentication methods, PostgreSQL 13
  allows for clients to [require channel binding](https://www.postgresql.org/docs/13/libpq-connect.html#LIBPQ-CONNECT-CHANNEL-BINDING)
  when using [SCRAM authentication](https://www.postgresql.org/docs/13/sasl-authentication.html#SASL-SCRAM-SHA-256),
  and the PostgreSQL foreign data wrapper ([`postgres_fdw`](https://www.postgresql.org/docs/13/postgres-fdw.html))
  can now use certificate-based authentication.

[PostgreSQL](https://www.postgresql.org) is the world's most
  advanced open source database, with a global community of thousands of users,
  contributors, companies and organizations. Built on over 30 years of
  engineering, starting at the University of California, Berkeley, PostgreSQL
  has continued with an unmatched pace of development. PostgreSQL's mature
  feature set not only matches top proprietary database systems, but exceeds
  them in advanced database features, extensibility, security, and stability.

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

For explanations of the above features and others, please see the following resources:

There are several ways you can download PostgreSQL 13, including:

Other tools and extensions are available on the
  [PostgreSQL Extension Network](http://pgxn.org).

PostgreSQL 13 comes with HTML documentation HTML documentation as well as man
  pages, and you can also browse the documentation online in both
  [HTML](https://www.postgresql.org/docs/13/) and [PDF](https://www.postgresql.org/files/documentation/pdf/13/postgresql-13-US.pdf) formats.

PostgreSQL uses the [PostgreSQL License](https://www.postgresql.org/about/licence/), a
  BSD-like "permissive" license. This [OSI-certified license](http://www.opensource.org/licenses/postgresql/)
  is widely appreciated as flexible and business-friendly, since it does not
  restrict the use of PostgreSQL with commercial and proprietary applications.
  Together with multi-company support and public ownership of the code, our
  license makes PostgreSQL very popular with vendors wanting to embed a database
  in their own products without fear of fees, vendor lock-in, or changes in
  licensing terms.

Website

All logos are available for modification and redistribution under The
  [PostgreSQL Licence](https://www.postgresql.org/about/licence/).  The PostgreSQL name and
  logo are trademarks of The PostgreSQL Community Association of Canada.

PostgreSQL enjoys the support of numerous companies, who sponsor developers,
  provide hosting resources, and give us financial support.  See our
  [sponsors page](https://www.postgresql.org/about/sponsors/) for
  some of these project supporters.

There is also a large community of
  [companies offering PostgreSQL Support](https://www.postgresql.org/support/professional_support/)
  , from individual consultants to multinational companies.

If you wish to make a financial contribution to the PostgreSQL Global
  Development Group or one of the recognized community non-profit organizations,
  please visit our [donations](https://www.postgresql.org/about/donate/) page.