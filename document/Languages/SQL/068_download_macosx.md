---
id: "sql_068"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 68
source_url: "https://www.postgresql.org/download/macosx"
language: "en"
retrieved_at: "2026-11-01 21:55:34"
content_hash: "45fdc6da5aad3baa2a787d35396bbb2633922cce77090f8ca90775a0f30a4f95"
---

# SQL

Source: https://www.postgresql.org/download/macosx

---

You can get macOS PostgreSQL packages from several sources.

 [Download the installer](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
certified by EDB for all supported Postgres versions.

**Note!** This installer is hosted by EDB and not on the PostgreSQL community servers.
  If you have issues with the website it's hosted on, please contact
  [webmaster@enterprisedb.com](mailto:webmaster@enterprisedb.com).

This installer includes:

This installer can run in graphical, command line, or silent install modes.

The macOS installer is designed to be a straightforward, fast way to get up and running with
PostgreSQL. In the unlikely event that you have issues with the installer,
please report them on the 
[installer Github page](https://github.com/EnterpriseDB/edb-installers/issues). Issues with the installed packages should be reported to the
appropriate project directly.

Advanced users can also download a
[zip archive](https://www.enterprisedb.com/download-postgresql-binaries)
of the binaries, without the installer.
This download is intended for users who wish to include Postgres as part of another application installer.

The installers are tested by EDB on the following platforms. They will generally work on newer versions of macOS as well:

| Postgres Version | 64-bit macOS Platforms | 
|---|---|
| 18 | 13+ (amd64), 13+ (arm64) | 
| 17 | 11.x (amd64), 12.x (arm64) | 
| 16 | 11.x (amd64), 12.x (arm64) | 
| 15 | 10.14 - 12.x (amd64), 12.x (arm64) | 
| 14 | 10.14 - 12.x (amd64), 12.x (arm64) | 
| 13 | 10.14 - 11.0 | 

[Postgres.app](https://postgresapp.com) is a simple, native macOS app that runs in the menubar without the need of an installer. Open the app, and you have a PostgreSQL server
ready and awaiting new connections. Close the app, and the server shuts down.

PostgreSQL can also be installed on macOS using
[Homebrew](https://brew.sh). For example, to install PostgreSQL 15,
you can use the following command:

```
    brew install postgresql@15
  
```

You can use [Homebrew Formulae](https://formulae.brew.sh) to
  search for PostgreSQL and other packages. To find a specific major version of
  PostgreSQL, search for `postgresql@NN`, where `NN`
  represents the major version. For example,
  [`postgresql@15`](https://formulae.brew.sh/formula/postgresql@15).

PostgreSQL packages are also available for macOS from the
[MacPorts Project](https://www.macports.org/). Please see the
MacPorts documentation for information on how to install ports.

A list of
[PostgreSQL packages](https://www.macports.org/ports.php?by=name&substr=postgresql)
can be found using the portfiles search tool on the MacPorts website.

PostgreSQL packages are available for macOS from the
[Fink Project](https://www.finkproject.org/).
Please see the Fink documentation for information on how to install packages.

A list of
[PostgreSQL packages](https://pdb.finkproject.org/pdb/browse.php?summary=postgresql)
can be found using the package search tool on the Fink website.