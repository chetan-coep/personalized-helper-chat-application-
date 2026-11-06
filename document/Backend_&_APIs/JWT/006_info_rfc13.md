---
id: "jwt_006"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 6
source_url: "https://www.rfc-editor.org/info/rfc13"
language: "en"
retrieved_at: "2026-11-01 22:15:38"
content_hash: "c8a64fabba17050294b67d3432f12a89d14ce1ddc30bd7a578f5eb39ce3b5691"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc13

---

- [Home](https://www.rfc-editor.org/)
- **RFC 13**

View as:

# RFC 13: Zero Text Length EOF Message

- V. Cerf

Unknown

- Added to 1 Set

```
Network Working Group                                          Vint Cerf
Request for Comments: 13                                       UCLA
                                                          20 August 1969
Referring to NWG/RFC: 11, it appears that file transmissions over
auxiliary connections will require some mechanism to specify "END-OF-
FILE."  It is proposed that a length 0 (zero) message be used for this
purpose.  Figure 1 shows the format:
|<---32 bits--->|<---32 bits--->|<----16 bits---->|<------?------>|
+---------------+---------------+-----------------+---------------+
|    leader     |    marking    |    checksum     |    padding    |
+---------------+---------------+-----------------+---------------+
                                Figure 1
                      Zero Text Length EOF Message
       [ This RFC was put into machine readable form for entry ]
      [ into the online RFC archives by Michael Brunnbauer 1/97 ]
                                                                [Page 1]
```