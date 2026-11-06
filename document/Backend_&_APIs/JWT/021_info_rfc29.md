---
id: "jwt_021"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 21
source_url: "https://www.rfc-editor.org/info/rfc29"
language: "en"
retrieved_at: "2026-11-01 22:16:07"
content_hash: "6f38e1acf796c9d2b75e757b1b21ad6806f2f7601d22c03efb7594df7ed3357a"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc29

---

- [Home](https://www.rfc-editor.org/)
- **RFC 29**

View as:

# RFC 29: Response to RFC 28

- R.E. Kahn

Unknown

Network Working Group                                   Robert Kahn
[RFC-29](https://www.rfc-editor.org/info/rfc29/)                                                  BBN
                                                        19 January 1970
This note is in response to Bill English's Request for Comments:  28.
A "millisecond" clock should be satisfactory for most network measurements.
Round-trip message transit times typically should be at least on the
order of tens to hundreds of milliseconds.  The IMP contains a 16-bit
hardware clock which is incremented every 100 microseconds to allow for
timing of internal events within the IMP, as for example, during tracing.
However, most measurements are made using a 25.6 ms. software clock.
DISTRIBUTION:
[A](https://www.rfc-editor.org#appendix-A). Bhushan, MIT
[S](https://www.rfc-editor.org#appendix-S). Carr. Utah
[G](https://www.rfc-editor.org#appendix-G). Cole, SDS
[S](https://www.rfc-editor.org#appendix-S). Crocker, UCLA
[K](https://www.rfc-editor.org#appendix-K). Fry, MITRE
[J](https://www.rfc-editor.org#appendix-J). Heafner, RAND
[B](https://www.rfc-editor.org#appendix-B). Kahn, BBN
[T](https://www.rfc-editor.org#appendix-T). O'Sullivan, Raytheon
[L](https://www.rfc-editor.org#appendix-L). Roberts, ARPA
[P](https://www.rfc-editor.org#appendix-P). Rovner, LL
[R](https://www.rfc-editor.org#appendix-R). Stoughton, UCSB