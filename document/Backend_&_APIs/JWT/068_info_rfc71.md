---
id: "jwt_068"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 68
source_url: "https://www.rfc-editor.org/info/rfc71"
language: "en"
retrieved_at: "2026-11-01 22:17:32"
content_hash: "8e936e3de9525dab2cb06075d1d85bc390118ad4b4466f9b424d3c72a0fa4487"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc71

---

- [Home](https://www.rfc-editor.org/)
- **RFC 71**

View as:

# RFC 71: Reallocation in Case of Input Error

- T. Schipper

Unknown

```
Network Working Group                                   Tjaart Schipper
Request for Comments #71                                25 September 1970
                                                        UCLA-CCN
            Reallocation in Case of Input Error
In case of reading a message from the IMP, it may be impossible for the
receiving NCP to determine the length of the message if an input error
occurs. The following protocol will be used at the CCN-Host at UCLA to
resynchronize flow control.
If an input error is detected and the NCP can find the intended link
number, it will send a GVB with frac = O to the sending Host and disregard
further incoming messages on that link. When the RET has been received, a
new ALL will be sent.
If the sending Host is not waiting for a RFNM when the GVB arrives, it will
send the RET immediately. If it is waiting for a RFNM corresponding to the
message with the error or a RFNM corresponding to a following message, it
will send the RET after the RFNM has been received.
In this way, the receiving Host will know that the link is clear before it
issues a new ALL.
TS/rb.
     [ This RFC was put into machine readable form for entry ]
     [ into the online RFC archives by Alexandra Weikert 7/97]
```