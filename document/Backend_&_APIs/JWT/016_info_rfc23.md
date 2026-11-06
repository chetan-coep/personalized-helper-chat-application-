---
id: "jwt_016"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 16
source_url: "https://www.rfc-editor.org/info/rfc23"
language: "en"
retrieved_at: "2026-11-01 22:15:56"
content_hash: "6ae0c609695c2a87f325461fc31eb079e1dfe34b6aa1ba9d15bcd8b5e9b0ff57"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc23

---

- [Home](https://www.rfc-editor.org/)
- **RFC 23**

View as:

# RFC 23: Transmission of Multiple Control Messages

- G. Gregg

Unknown

```
Network Working Group                                           G. Gregg
Request for Comments: 23                                            UCSB
                                                         16 October 1969
                TRANSMISSION OF MULTIPLE CONTROL MESSAGES
The network program at a site must be prepared to send or receive more
than one control message in a single control communication.
During the time that the control link is blocked awaiting RFNM, it is
possible that a number of control messages to a particular remote host
will accumulate.  When the link is unblocked, these should all be sent
in a single communication for greatest efficiency.
For receiving, it will be necessary to have a loop which returns to
decode and take action on successive control messages until the control
communication is exhausted.
```