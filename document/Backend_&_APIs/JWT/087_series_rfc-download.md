---
id: "jwt_087"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 87
source_url: "https://www.rfc-editor.org/series/rfc-download"
language: "en"
retrieved_at: "2026-11-01 22:14:59"
content_hash: "7447a241bab374b643cee9bfba3b4da0baf91464b0ecc7859de2041bb9eaaaf5"
---

# JWT

Source: https://www.rfc-editor.org/series/rfc-download

---

- [Home](https://www.rfc-editor.org/)
- **Download RFCs**

# Download RFCs

## In this section

## [Feed of recently published RFCs](https://www.rfc-editor.org#feed-of-recently-published-rfcs)

To be notified of newly published RFCs, use the [RSS feed](https://www.rfc-editor.org/rfcrss.xml) or [Atom feed](https://www.rfc-editor.org/rfcatom.xml).

## [Download RFCs Using rsync](https://www.rfc-editor.org#download-rfcs-using-rsync)

To download RFCs and keep them up to date locally, use [rsync](https://rsync.samba.org).

### [To get the list of modules](https://www.rfc-editor.org#to-get-the-list-of-modules)

Type `rsync rsync.rfc-editor.org::`

This will return the following results:

| Module Names | Comments | 
|---|---|
| everything-ftp | Everything FTP | 
| rfcs | Contents of in-notes/ and subdirectories `bcp/`, `fyi/`, `ien/`, and `std/` | 
| rfcs-text-only | Text files from `[rfcs]` | 
| rfc-ed-all | Entire repository (excluding Internet-Drafts) | 
| rfcs-pdf-only | PDF versions of ASCII RFCs to ensure correct page breaks, etc. | 
| rfcs-exclude-json | Contents of `[rfcs]` excluding JSON files | 
| rfcs-json-only | Only the JSON files from the directories in `[rfcs]` | 
| rfcs-pdf-all | All PDFs | 

### [To create a mirror using a module](https://www.rfc-editor.org#to-create-a-mirror-using-a-module)

Type `rsync -avz --delete rsync.rfc-editor.org::Module-Name Target-Directory`

For example: To create a mirror of the text versions of all the RFCs, i.e.,

```
in-notes/*.txt
in-notes/bcp/*.txt
in-notes/fyi/*.txt
in-notes/ien/*.txt
in-notes/std/*.txt
```
type `rsync -avz --delete rsync.rfc-editor.org::rfcs-text-only my-rfc-mirror`

(The `--delete` option is useful for removing local copies of files that have been deleted from the repository as well as expired Internet-Drafts.)

Last updated .