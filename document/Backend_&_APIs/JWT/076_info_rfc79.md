---
id: "jwt_076"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 76
source_url: "https://www.rfc-editor.org/info/rfc79"
language: "en"
retrieved_at: "2026-11-01 22:17:48"
content_hash: "b5ec889597cbdfbcd2962d09668409a0010964364aea05de7461f0ba15a22ab7"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc79

---

- [Home](https://www.rfc-editor.org/)
- **RFC 79**

View as:

# RFC 79: Logger Protocol error

- E. Meyer

Unknown

```
Network Working Group                                Edwin W. Meyer, Jr.
Request for Comments: 79                                 MIT Project MAC
NIC 5601                                               November 16, 1970
                         Logger Protocol Error
   A conflict was recently discovered between the official NCP protocol
   as described in protocol document 1 and the logger protocol as
   described in 
```
[RFC 66](https://www.rfc-editor.org/info/rfc66/) by Steve Crocker.  Steve suggested that we put
   out an RFC to alert the network community to this point.
   In [RFC 66](https://www.rfc-editor.org/info/rfc66/), it is proposed that an ALL allocate command be sent
   immediately following an RTS or STR request for connection.  This
   conflicts with the restriction stated in Protocol Document 1 that an
   ALL command can be given only for an "open" connection.
   To not be required to handle an ALL command before a connection is
   established is a simplifying restriction that an NCP implementation
   may take advantage of.  For example, the Multics NCP is currently
   designed this way.  For this reason, and also because we believe that
   the NCP protocol should not be changed now except for critical
   reasons it is felt that the proposed logger protocol should be
   modified to agree with the existing NCP protocol.
         [ This RFC was put into machine readable form for entry ]
       [ into the online RFC archives by Alison De La Cruz  11/00  ]
Meyer                                                           [Page 1]