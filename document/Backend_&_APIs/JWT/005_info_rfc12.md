---
id: "jwt_005"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 5
source_url: "https://www.rfc-editor.org/info/rfc12"
language: "en"
retrieved_at: "2026-11-01 22:15:36"
content_hash: "6f83b61e330afa3486722b4854dd4cb6cd30cdd9d335dd1da995d497d6e329e2"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc12

---

- [Home](https://www.rfc-editor.org/)
- **RFC 12**

View as:

# RFC 12: IMP-Host interface flow diagrams

- M. Wingfield

Unknown

- Added to 1 Set

```
Network Working Group                                       M. Wingfield
Request for Comments: 12  REVISED                         26 August 1969
                    IMP-HOST INTERFACE FLOW DIAGRAMS
   The following flow diagrams were extracted from the logic diagrams
   provided in 
```
[Appendix B](https://www.rfc-editor.org#appendix-B) of BBN Report No. 1822.  These diagrams
   indicate the logical sequence of hardware operations which occur
   within the IMP-HOST interface.  The logic names appearing in the
   blocks correspond to the logic elements found in [Appendix B](https://www.rfc-editor.org#appendix-B).
Wingfield                                                       [Page 1]
[RFC 12](https://www.rfc-editor.org/info/rfc12/)              IMP-HOST INTERFACE FLOW DIAGRAMS      26 August 1969
IMP to HOST Message
                       +----------+
                       |  Start   |
                       |  Input   |
                       +----------+
                             |
                             V
                 +------------------------+
                 | LAST \<--0; IMPERR \<--0 |
                 | PAD \<--0; IN REQST \<--0|
                 |  COUNTER \<--0          |
                 +------------------------+      +---+
                             |\<----------------- | B |
                             V                   +---+
                      +--------------+
                      | RFNIB \<-- 1  |
                      +--------------+
                             |\<--------------+
                             V               |
                            / \              |
                          /     \            |
                        / THERE'S \ N        |
                        \YOUR BIT /----------+
                          \=1 ? /
                            \ /
                             |
        +------------------->V
        |                   / \
   +----+------+    N     /     \
   | IMP ERROR |\<------ /   IMP   \
   | \<--- 1    |        \  READY  /
   +-----------+          \ ?   /
                            \ /
                             | Y
                             V
                            / \
                          /     \
   +-----------+   Y    /  LAST   \
   | PAD \<-- 1 |\<-------\ IMP BIT /
   +-----------+          \ =1? /
        |                   \ /                 +---+
        +------------------->|\<-----------------| C |
                             V                  +---+
                +-----------------------+
                |    PULSE SHIFT REG.   |       +---+
                |   INCREMENT COUNTER   |------>| A |
                |      RFNTR \<-- 0      |       +---+
                +-----------------------+
Wingfield                                                       \[Page 2\]

[RFC 12](https://www.rfc-editor.org/info/rfc12/)              IMP-HOST INTERFACE FLOW DIAGRAMS      26 August 1969
      +---+                +---+
      | C |                | A |
      +-+-+                +-+-+
        ^                    |
        | Y                  V
       / \                  / \
     /     \          N   /WORD \
   /  PAD=1  \ \<--------/ LENGTH  \
   \    ?    /          \   =1    /
     \     /              \  ?  /
       \ /                  \ /
        | N                  |
        V                    V
      +---+       +----------------------+
      | B |       |     INREQST \<--1     |
      +---+       +----------------------+
                             |\<-----------+
                             V            |
                            / \           |
                          /DATA \         |
                        /HAS BEEN \\\_N\_\_\_\_\_|
                        \ TAKEN   /
                          \ ?   /
                            \ /
                             V Y
                  +----------------------+
                  |    INREQST \<--0      |
                  +----------------------+
                             V
                            / \
                          /     \              +------------+
                        / LAST = 1\----------->|   END  OF  |
                        \    ?    /            |   MESSAGE  |
                          \     /              +------------+
                            \ /                       ^
                             | N                      |
                             V                        |
                            / \                       |
                          /     \                     |
                        / PAD = 1 \-------------------+
                        \     ?   /
                          \     /
                            \ /
                             | N
                             V
   +---+          +---------------------+
   | B |\<---------|    CLEAR COUNTER    |
   +---+          +---------------------+
Wingfield                                                       \[Page 3\]

[RFC 12](https://www.rfc-editor.org/info/rfc12/)              IMP-HOST INTERFACE FLOW DIAGRAMS      26 August 1969
HOST TO IMP MESSAGE
            +--------------+
            | START OUTPUT |
            +------+-------+
                   V
       +------------------------+
       | COUNTER \<-- 1          |
       | LSTWD \<--0; BTAVL \<--0 |
       +-----------+------------+        +---+
                   |\<--------------------| C |
                   V                     +---+
       +-----------+------------+
       |    OUT REQST \<-- 1     |
       |     CLEAR SHIFT REG.   |
       +-----------+------------+
     +------------>|
     |             V
     |            / \
     |      N   /     \
     |\_\_\_\_\_\_\_ / STROBE  \
              \DATA WORD/
                \ =1 ?/
                  \ /
                   V  Y
      +------------+------------+
      |  LOAD SHIFT  REGISTER   |
      |  OUTREQST \<-- 0         |
      |  COUNTER  \<-- 1         |
      +-------------------------+
      +---------->|
      |           V
      |          / \
      |        /     \
      |N     / RFNBIT  \
      +----- \   = 1   /
               \   ? /            +----------+
                 \ /              |          | N
                  V   Y           |         / \
         +--------+--------+      V       /     \
         |  THERE'S YOUR   |----------->/ RFNBIT  \
         | HOST BET \<-- 1  |            \  = 0    /
         +-----------------+              \  ?  /
                                            \ /
                                             | Y
                                           +-+-+
                                           | A |
                                           +---+
Wingfield                                                       \[Page 4\]

[RFC 12](https://www.rfc-editor.org/info/rfc12/)              IMP-HOST INTERFACE FLOW DIAGRAMS      26 August 1969
                               +---+
                               | A |
                               +---+
                                 V
                  +--------------+-------------+
                  | THERE'S YOUR HOST BIT \<--0 |
                  |      BTAVL \<-- 0           |
                  +----------------------------+
                                 V
                                / \                   / \
                              / WORD\   Y           /     \   Y
                            /LENGTH -1\---------->/  LSTWD  \---+
                            \   = 1   /           \   = 1   /   |
                              \  ?  /               \  ?  /     |
                                \ /                   \ /       |
                                 | N                   | N      |
                                 V                     |        |
                                / \                    |        |
                              / WORD\                  |        V
           \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ / LENGTH  \                |  +------------+
           |                \  = 1    /                |  | LIBIT \<- 1 |
           |                  \  ?  /                  |  +------------+
           |                    \ /                    V        |
           |                     |\<-----------------------\<------+
           |                     V
           |            +-----------------+
           |            | PUSH SHIFT REG. |
    +-------------+     |INCREMENT COUNTER|
    | LIBIT \<-- 0 |     +-----------------+
    +-------------+              V
           |                   +---+
           |                   | B |
           V                   +---+
          / \
        /     \
      /  LSTWD  \ Y                          +-------------+
      \   = 1   /--------------------------->|   END OF    |
        \  ?  /                              |   MESSAGE   |
          \ /                                +-------------+
           | N
           V
         +---+
         | C |
         +---+
         \[ This RFC was put into machine readable form for entry \]
             \[ into the online RFC archives by Lorrie Shiota\]
Wingfield                                                       \[Page 5\]

```
```
[RFC 12](https://www.rfc-editor.org/info/rfc12/)              IMP-HOST INTERFACE FLOW DIAGRAMS      26 August 1969
Wingfield                                                       [Page 6]