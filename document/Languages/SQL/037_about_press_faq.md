---
id: "sql_037"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 37
source_url: "https://www.postgresql.org/about/press/faq"
language: "en"
retrieved_at: "2026-11-01 21:57:04"
content_hash: "218117f34913cb9f04bf3ecb2fc8bbf8d100c8189206d2e28efd9c593969c32b"
---

# SQL

Source: https://www.postgresql.org/about/press/faq

---

**Q: What is the current version of PostgreSQL?**

A: 18, which was released on September 25, 2025. This is our 35th major release in over 39 years of development. We release a new version of PostgreSQL every year, which is unique among SQL databases.

**Q: Does the PostgreSQL Project have a Code of Conduct?**

A: The PostgreSQL Project prides itself on the quality of our code and our work, and the technical and professional accomplishments of our community. We expect everyone who participates to conduct themselves in a professional manner, acting with common courtesy and in the common interest, with respect for all users and developers. To that end, we established a [Code of Conduct](https://www.postgresql.org/about/policies/coc/) for community interaction and participation in the project's work and the community at large.

**Q: How does versioning work?**

A: PostgreSQL [versioning](https://www.postgresql.org/support/versioning/) has a two-part number scheme. The first number (e.g. 18) represents the major version, which is a new feature release. The second number represents a patch version, which is a bug / security fix release. For example, "18.1" is the first patch release of PostgreSQL 18. For more information, please see the  [PostgreSQL versioning](https://www.postgresql.org/support/versioning/) page.

**Q: When do releases happen?**

A: Major version releases happen roughly once-a-year around September. Patch releases are scheduled once-a-quarter (February, May, August, November). You can read more about the release schedule on the [roadmap](https://www.postgresql.org/developer/roadmap/) page.

**Q: Why are older versions that are labeled 9.6.6 or 9.5.9?**

A: Because of the long history of our project the first two decimals are major releases.  Thus 9.6, 9.5 etc. were all major releases.  Minor releases have numbers like 9.6.6. Since version 10, the project has adopted a two-part version numbering scheme.

**Q: How is PostgreSQL licenced? How much does it cost?**

A: PostgreSQL is released under the [OSI-approved PostgreSQL Licence](https://opensource.org/licenses/PostgreSQL). There is no fee, even for use in commercial software products.  Please see [the PostgreSQL Licence](https://www.postgresql.org/about/licence/).

**Q: What is the PostgreSQL trademark policy?**

A: This is covered in details on the [PostgreSQL trademark policy](https://www.postgresql.org/about/policies/trademarks/) page.

**Q: How many developers work on PostgreSQL?**

A: There are thousands of people contributing to the PostgreSQL ecosystem at any one time! Over 700 on the core database software. As with other open source projects, of course, we depend on hundreds of community members for documentation, translations, advocacy, conferences, website development, infrastructure, and peer-to-peer support. There are also many other projects associated with PostgreSQL, including drivers, libraries, extensions and more.

**Q: How many PostgreSQL users are there, worldwide?**

A: Our wide distribution through the open source world and liberal licensing make that a difficult question to answer with any accuracy. Most users get PostgreSQL with a Linux distribution, or with some of the many other products, OSS software, and hardware devices that include PostgreSQL. Many indexes, such as the [DB-Engines Ranking](https://db-engines.com/en/ranking), demonstrate that PostgreSQL adoption continues to grow at a rapid pace, including DB-Engines recognition of PostgreSQL as the [DBMS of the Year in 2017](https://db-engines.com/en/blog_post/76), [2018](https://db-engines.com/en/blog_post/79), [2020](https://db-engines.com/en/blog_post/85), and [2023](https://db-engines.com/en/blog_post/106). What we do know is that PostgreSQL is more popular than ever, with the number of downloads and installations increasing year-over-year.

**Q: Can we talk to some of your users?**

A: Please contact [press@postgresql.org](mailto:press@postgresql.org) and our press volunteers will try to arrange a contact.

**Q: What company owns PostgreSQL?**

A: None.  We are an unincorporated association of volunteers and companies who share code under the PostgreSQL Licence. The PostgreSQL project involves a couple dozen companies who either support PostgreSQL contributors or directly contribute corporate projects to our repository.  Some of our major corporate sponsors are on the [sponsors page,](https://www.postgresql.org/about/sponsors/) and there are many more companies who contribute to the project in other ways.

**Q: Where can people get support for PostgreSQL?**

A: There are many companies that provide paid support for PostgreSQL. You can find support vendors by regional from the [professional services list](https://www.postgresql.org/support/professional_support/). Please note that this list is strictly informational and is not an endorsement of any of these vendors.

**Q: What's the relationship between the PostgreSQL Project and the companies listed on the "Sponsors" page?**

A: The PostgreSQL project enjoys the support of multiple companies who sell products or services built with PostgreSQL, and in turn contribute code, money and staff time to the project.  None of them "own" PostgreSQL, nor is any individual company responsible for PostgreSQL code development. This is the same as Linux, Apache and FreeBSD.

**Q: How does PostgreSQL compare to MySQL?**

A: This is a topic that can start several hours of discussion. PostgreSQL is liberally licenced and owned by its community; MySQL is GPL-licenced and owned by Oracle. Beyond that, each database user should make his own evaluation; open source software makes doing comparisons very easy. We encourage you to look at a high-level summary of PostgreSQL features and functionality on the [about PostgreSQL](https://www.postgresql.org/about/) page.

**Q: How does PostgreSQL compare to Oracle/DB2/SQL Server/Informix?**

A: Our feature set is generally considered to be very competitive with other leading SQL RDBMSes. There are features some of them have that PostgreSQL does not, and the reverse is also true. We have had many users migrate from other database systems and they are completely satisfied with their PostgreSQL systems.

**Q: How does PostgreSQL compare to "NoSQL"?**

A: The term "NoSQL" covers such a diverse array of non-relational database implementations, from tiny embedded databases like BerkeleyDB to massive clustered data processing platforms like Hadoop, that it's impossible to comment on them as a general class.  Non-relational databases preceded relational databases and have existed alongside them for forty years, so choosing between relational and nonrelational databases is nothing new.  Users should choose the database whose features, implementation, and community support their current application needs. Further, using multiple different databases for large projects is fast becoming the norm, and PostgreSQL users are no exception.

Additionally, PostgreSQL has supported storing "unstructured" data types such as JSON and XML for many years.

**Q: Is PostgreSQL a "vector database"?**

A: PostgreSQL supports storing and searching over many data types, including vectors. PostgreSQL has an [array](https://www.postgresql.org/docs/current/arrays.html) data type that can store multi-dimensional data. PostgreSQL's extension framework lets developers add additional vector functionality into PostgreSQL, including custom indexes that interface into PostgreSQL's memory and storage management systems. There are several extensions that augment PostgreSQL's vector search capabilities.

**Q: When will PostgreSQL 19 come out?**

A: The PostgreSQL project begins work on the next version of PostgreSQL in July of each year, and releases the GA in September of the following year. So expect version 19 around September 2026.

**Q: How do you pronounce PostgreSQL**

A: post-GRES-que-ell, per this [audio file](https://www.postgresql.org/files/postgresql.mp3).  However, many people find it easier to just say "post-GRES".