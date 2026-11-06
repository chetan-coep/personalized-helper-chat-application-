---
id: "sql_051"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 51
source_url: "https://www.postgresql.org/about/press/presskit96/en"
language: "en"
retrieved_at: "2026-11-01 21:57:59"
content_hash: "0585d0f2b88f4cb931407575f96737368895b00d17f6113e73d50c36e811f961"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit96/en

---

29 SEPTEMBER 2016: PostgreSQL 9.6, the latest version of the world's leading open source relational database, was released today by the PostgreSQL Global Development Group. This release will allow users to both scale up and scale out high performance database workloads. New features include parallel query, synchronous replication improvements, phrase search, and improvements to performance and usability.

Version 9.6 adds support for parallelizing some query operations, enabling utilization of several or all of the cores on a server to return query results faster. This release includes parallel sequential (table) scan, aggregation, and joins. Depending on details and available cores, parallelism can speed up big data queries by as much as 32 times faster.

"I migrated our entire genomics data platform — all 25 billion legacy MySQL rows of it — to a single Postgres database, leveraging the row compression abilities of the JSONB datatype, and the excellent GIN, BRIN, and B-tree indexing modes. Now with version 9.6, I expect to harness the parallel query functionality to allow even greater scalability for queries against our rather large tables," said Mike Sofen, Chief Database Architect, Synthetic Genomics.

Two new options have been added to PostgreSQL's synchronous replication feature which allow it to be used to maintain consistent reads across database clusters. First, it now allows configuring groups of synchronous replicas. Second, the "remote\_apply" mode creates a more consistent view of data across multiple nodes. These features support using built-in replication to maintain a set of "identical" nodes for load-balancing read workloads.

The PostgreSQL-to-PostgreSQL data federation driver, postgres\_fdw, has new capabilities to execute work on remote servers. By "pushing down" sorts, joins, and batch data updates, users can distribute workload across multiple PostgreSQL servers. These features should soon be added to other FDW drivers.

"With the capabilities of remote JOIN, UPDATE and DELETE, Foreign Data Wrappers are now a complete solution for sharing data between other databases and PostgreSQL. For example, PostgreSQL can be used to handle data input going to two or more different kinds of databases," said Julyanto Sutandang, Director of Business Solutions at Equnix.

PostgreSQL's full text search feature now supports "phrase search." This lets users search for exact phrases, or for words within a specified proximity to each other, using fast GIN indexes. Combined with new features for fine-tuning text search options, PostgreSQL is the superior option for "hybrid search" which puts together relational, JSON, and full text searching.

Thanks to feedback and testing by PostgreSQL users with high-volume production databases, the project has been able to improve many aspects of performance and usability in this release. Replication, aggregation, indexing, sorting, and stored procedures have all been made more efficient, and PostgreSQL now makes better use of resources with recent Linux kernels. Administration overhead for large tables and complex workloads was also reduced, especially through improvements to VACUUM.

For explanations of the above features and others, please see the following resources:

HTML documentation and man pages are installed with PostgreSQL, but feel free to browse, search and comment on our extensive, interactive [online documentation](https://www.postgresql.org/docs/9.6/).

PostgreSQL uses the [PostgreSQL License](https://www.postgresql.org/about/licence), a BSD-like "permissive" license. This
[OSI-certified license](http://www.opensource.org/licenses/postgresql) is widely appreciated as flexible and business-friendly, since it does not restrict the use of PostgreSQL with commercial and proprietary applications. Together with multi-company support and public ownership of the code, our license makes PostgreSQL very popular with vendors wanting to embed a database in their own products without fear of fees, vendor lock-in, or changes in licensing terms.

Web Pages

English-Language Press Inquiries

USA, Canada and General Inquiries

PostgreSQL Press Team

[press@postgresql.org](mailto:press@postgresql.org)

Phone: +1 (347) 674-7759

Ireland

Raymond O'Donnell

[ie@postgresql.org](mailto:ie@postgresql.org)

+353 (0)87 2241365

United Kingdom

Simon Riggs

[uk@postgresql.org](mailto:uk@postgresql.org)

+44-7900-255520

Finland

Jussi Mikkola

[fi@postgresql.org](mailto:fi@postgresql.org)

Cell: +46-708-969691

Sweden

Magnus Hagander

[se@postgresql.org](mailto:se@postgresql.org)

Cell: +46-708-969691

Malaysia

Chris Travers

[my@postgresql.org](mailto:my@postgresql.org)

Australia

Arul Shaji Arulappan and Richard Sayad

[au@postgresql.org](mailto:au@postgresql.org)

All logos are available for modification and redistribution under The PostgreSQL License. The PostgreSQL name and logo are trademarks of The PostgreSQL Community Association of Canada.

PostgreSQL is the world's most advanced database system, with a global community of thousands of users and contributors and dozens of companies and organizations.  The PostgreSQL Project builds on over 30 years of engineering, starting at the University of California, Berkeley, and has an unmatched pace of development today. PostgreSQL's mature feature set not only matches top proprietary database systems, but exceeds them in advanced database features, extensibility, security and stability.  Learn more about PostgreSQL and participate in our community at [PostgreSQL.org](https://www.postgresql.org).

"As the chief database architect for Synthetic Genomics, I was utterly amazed at the power, flexibility and richness of programming interfaces for Postgres 9.5x. I migrated our entire genomics data platform — all 25 billion legacy mysql rows of it — to a single Postgres database, leveraging the row compression abilities of the JSONB datatype, the excellent GIN, BRIN, and B-tree indexing modes, and the beautifully extended PL/pgSQL programming language for stored functions. Now with version 9.6, I expect to harness the parallel query functionality to allow even greater scalability for queries against our rather large tables. Postgres 9.5 has proven itself to be utterly stable, remarkably performant, and, in my opinion, the best mixed relational-document store data storage engine on the market at this time," said Mike Sofen, Chief Database Architect, Synthetic Genomics

[Synthetic Genomics, Inc.](https://www.syntheticgenomics.com/) (SGI) is a global leader in the fields of synthetic biology and synthetic genomics utilizing foundational intellectual property in these rapidly evolving disciplines to design and build biological systems to solve global sustainability challenges. SGI provides solutions in genomics research, bioproduction, and applied products. The research segment is focused on genomics solutions for academic and commercial research and development organizations. The commercial products and services include instrumentation, reagents, DNA synthesis services, and bioinformatics services and software.  Contact Synthetic Genomics at [media@syntheticgenomics.com](mailto:media@syntheticgenomics.com) (English)

[Equnix](http://www.equnix.co.id/) is an IT Solution Provider for Enterprises delivering comprehensive alternate solutions, based on research, development and Open Source. Equnix is a PostgreSQL Company. Contact us in English or Indonesian at: [Info@equnix.co.id](mailto:info@equnix.co.id) or call Johan D. at +6221-22866662.

PostgreSQL enjoys the support of numerous companies, who sponsor developers, provide hosting resources, and give us financial support.  See our [sponsors page](https://www.postgresql.org/about/sponsors/) for some of these project supporters.

There is also a large community of [companies offering PostgreSQL Support](https://www.postgresql.org/support/professional_support), from individual consultants to multinational companies.

[Donations](https://www.postgresql.org/about/donate) gladly accepted.

Or you can buy some of this fine merchandise from our [Zazzle PostgreSQL Store](http://www.zazzle.com/postgresql).