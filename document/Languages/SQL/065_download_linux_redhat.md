---
id: "sql_065"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 65
source_url: "https://www.postgresql.org/download/linux/redhat"
language: "en"
retrieved_at: "2026-11-01 21:55:50"
content_hash: "7897a433c27a5c2f9caf82beffbec5460789e3cd596283e8b1fb76a9aa26712b"
---

# SQL

Source: https://www.postgresql.org/download/linux/redhat

---

The Red Hat family of distributions includes:


and others.

PostgreSQL is available on these platforms by default. However,
each version of the platform normally "snapshots" a specific version of
PostgreSQL that is then supported throughout the lifetime of this platform.
Since this can often mean a different version than preferred, the PostgreSQL
project provides a [repository](https://www.postgresql.org#yum) of packages of all
supported versions for the most common distributions.

The [PostgreSQL Yum Repository](https://yum.postgresql.org) will integrate
with your normal systems and patch management, and provide automatic
updates for all supported versions of PostgreSQL throughout the support
[lifetime](https://www.postgresql.org/support/versioning/) of PostgreSQL.

The PostgreSQL Yum Repository currently supports:


**<sup>\*</sup>Note**: due to the shorter support cycle
on Fedora, all supported versions of PostgreSQL may not available on this platform. We do not recommend
using Fedora for server deployments.

The PostgreSQL Yum Repository recently [supports
the last two minor releases of RHEL and its derivatives](https://yum.postgresql.org/news/postgresql-rpms-multiple-rhel-minor-versions/), like RHEL 10.2
and 10.1.

To use the PostgreSQL Yum Repository, follow these steps:

These distributions all include PostgreSQL by default. To install
PostgreSQL from these repositories, use the `dnf` command on RHEL and Fedora:

```
dnf install postgresql-server
```

Which version of PostgreSQL you get will depend on the version of the distribution:

| Distribution | Version | 
|---|---|
| RHEL / Rocky Linux / AlmaLinux 10 | 16 | 
| RHEL / Rocky Linux / AlmaLinux 9 | 16, 15 and 13 (via modules) | 
| RHEL / Rocky Linux / AlmaLinux 8 | 15, 13, 12, 10 and 9.6 via modules | 
| Fedora 44 | 18 | 
| Fedora 43 | 18 | 

Other Red Hat family distributions may ship a different version of PostgreSQL by default, check with your distribution vendor to be sure.

The repository contains many different packages including third party addons. The most common and important packages are (substitute the version number as required):

| postgresql-client | libraries and client binaries | 
|---|---|
| postgresql-server | core database server | 
| postgresql-contrib | additional supplied modules | 
| postgresql-devel | libraries and headers for C language development | 

Due to policies for Red Hat family distributions, the PostgreSQL installation will not be enabled for automatic start or have the database initialized automatically. To make your database installation complete, you need to perform the following steps, based on your distribution:

postgresql-setup --initdb
  systemctl enable postgresql.service
  systemctl start postgresql.service

If you cannot, or do not want to, use the yum based installation method,
all the RPMs that are in the yum repository are available for
[direct download](https://yum.postgresql.org/rpmchart/)
and manual installation as well.