---
id: "jwt_059"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 59
source_url: "https://www.rfc-editor.org/info/rfc63"
language: "en"
retrieved_at: "2026-11-01 22:17:16"
content_hash: "00c04212a08f72dee996645d712c2963aff4fe2ae58652ff09f84254a9eebb1e"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc63

---

- [Home](https://www.rfc-editor.org/)
- **RFC 63**

View as:

# RFC 63: Belated Network Meeting Report

- V.G. Cerf

Unknown

```
Network Working Group                                          V. Cerf
Request for Comments #63                                       31 July 70
                     Belated Network Meeting Report
On 8 May 1970, a Network Working Group meeting was hosted at Lincoln Labs.
The topics under discussion were:
   1)   Lincoln Lab's Local Interaction Language (LIL)
   2)   Records, Messages, and Format in HOST-HOST information exchange.
   3)   Miscellaneous gripes
The first topic is thoroughly summarized in Lincoln Lab's Semi annual
Technical Summary titled "Graphics", dated May 31, 1970 (document id.
ESD-TR-70-151).
The second topic involved considerable  discussion of NWG/RFC #42 in which
it was proposed that all messages be preceded by an 8-bit type byte which
would declare the format of the message which followed.
The following decisions were reached:
   a)   Records may begin anywhere within a message.
   b)   The first 8 bits of a record are reserved for type information.
   c)   The first transmission on a connection starts a record.
Type 0 is agreed to mean that the transmission that follows consists of an
arbitrarily long record, and that no further type bytes will be present.
The notions of messages and records are independent of the flow-control
protocol.  Thus the receipt of a message does not carry any semantic
importance.  The receipt of a record, however, may initiate some interpre-
tation process.
After some discussion, the proposals in NWG/RFC #42 were permuted as follows:
   type 0 = bit string of arbitrary length follows
   type 1 = 8-bit ASCII follows
   type 2 = EBCDIC follows
   type 3 = MOD 33 TTY 7-bit ASCII
                                                                [Page 1]
```
Network Working Group                                         V. Cerf
Request for Comments #63                                      31 July 70
   type 4 = YOUR Local
            followed by another type byte
   type 5 = MY Local
            followed by another type byte
The praise or blame for the preceding decisions rests on the attendees at
the meeting, to wit:
[E](https://www.rfc-editor.org#appendix-E). Ancona (LL)
[T](https://www.rfc-editor.org#appendix-T). J. Barkalow (LL)
[D](https://www.rfc-editor.org#appendix-D). B. Black (Harvard)
Jack Bouknight (UI)
Howard Brodie (MAC)
Vint Cerf (UCLA)
Steve Crocker (UCLA)
Jim Curry (UTAH)
[A](https://www.rfc-editor.org#appendix-A). Evans (LL, MAC)
Robert Flegal (UTAH)
Jim Frogie (LL)
[J](https://www.rfc-editor.org#appendix-J). D. Fry (MITRE)
John Heafner (RAND)
Bob Hoffman (RAND)
Richard Kalin (LL)
William Kantrowitz (LL)
Peggy Karp (MITRE)
Abe Landsberg (SDC)
Robert Long (SDC)
James Madden (UI)
John Melvin (SRI)
Alan Nemeth (LL)
John Newkirk (Harvard)
Jon Postel (UCLA)
Tom O'Sullivan (Raytheon)
Ari Shoshani (SDC)
Joel Winett (LL)
Instead of sending NWG/RFC's to Chuck Rose at Case University, Jim Torson
will be receiving them.
       \[ This RFC was put into machine readable form for entry \]
     \[ into the online RFC archives by Tammy and Ofer Porat 1/97 \]
                                                                \[Page 2\]