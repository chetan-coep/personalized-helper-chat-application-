---
id: "sql_064"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 64
source_url: "https://www.postgresql.org/download/linux/debian"
language: "en"
retrieved_at: "2026-11-01 21:55:45"
content_hash: "f4e0904185204b3e5ae218f2797d6fc479a85ecfae6f36fd26362b8945a5a0c7"
---

# SQL

Source: https://www.postgresql.org/download/linux/debian

---

PostgreSQL is available in all Debian versions by default. However, Debian
"snapshots" a specific version of PostgreSQL that is then supported throughout
the lifetime of that Debian version.
The PostgreSQL project maintains an [Apt repository](https://www.postgresql.org#apt) with all supported
of PostgreSQL available.

Debian includes PostgreSQL by default. To install PostgreSQL on Debian,
use the `apt` (or other apt-driving) command:

apt install postgresql

If the version included in your version of Debian is not the one you want,
you can use the [PostgreSQL Apt Repository](https://apt.postgresql.org). This repository will integrate
with your normal systems and patch management, and provide automatic
updates for all supported versions of PostgreSQL throughout the support
[lifetime](https://www.postgresql.org/support/versioning/) of PostgreSQL.

The PostgreSQL Apt repository supports the current versions of Debian:

on the following architectures:

sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

Import the [repository key](https://www.postgresql.org/media/keys/ACCC4CF8.asc):

sudo apt install curl ca-certificates gpg
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

Verify the key:

```
gpg --show-key /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc
pub   rsa4096 2011-10-13 [SC]
      B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
uid                      PostgreSQL Debian Repository
```
Create **/etc/apt/sources.list.d/pgdg.sources**. The distributions are called *codename***-pgdg**. In the example, replace *trixie* with the actual distribution you are using. File contents:

Types: deb deb-src
URIs: https://apt.postgresql.org/pub/repos/apt
Suites: trixie-pgdg
Architectures: amd64
Components: main
Signed-By: /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc

sudo apt update
sudo apt install postgresql-18

For more information about the apt repository, including answers to frequent
questions, please see the
[PostgreSQL Apt Repository wiki page](https://wiki.postgresql.org/wiki/Apt).

The repository contains many different packages including third party addons. The most common and important packages are (substitute the version number as required):

| postgresql-client-18 | client libraries and client binaries | 
|---|---|
| postgresql-18 | core database server | 
| postgresql-doc-18 | documentation | 
| libpq-dev | libraries and headers for C language frontend development | 
| postgresql-server-dev-18 | libraries and headers for C language backend development |