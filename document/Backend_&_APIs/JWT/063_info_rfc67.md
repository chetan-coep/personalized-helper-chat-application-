---
id: "jwt_063"
technology: "JWT"
category: "Backend & APIs"
title: "JWT"
doc_order: 63
source_url: "https://www.rfc-editor.org/info/rfc67"
language: "en"
retrieved_at: "2026-11-01 22:17:24"
content_hash: "fc5594b890888d89db38e411c44803d2d8d628a9322fcb5bc2d956d64f0f8e8e"
---

# JWT

Source: https://www.rfc-editor.org/info/rfc67

---

- [Home](https://www.rfc-editor.org/)
- **RFC 67**

View as:

# RFC 67: Proposed Change to Host/IMP Spec to Eliminate Marking

- W.R. Crowther

Unknown

```
Network Working Group                         W. Crowther
Request for Comments #67                      BBN
                                              [IMPORTANT]
         Proposed Change to Host/IMP Spec to Eliminate Marking
    Before he left for Norway, Dave Walden observed that there was a
simple change to the Host/IMP specifications which would eliminate all
"marking" problems.  The change is to separate the leader from the text
of regular messages, and then to send them as consecutive messages
instead of one packed message.  The text would then start on a word
boundary no matter what the word lengths of the machines involved.  The
process would take place on both IMP-to-Host and Host-to-IMP messages.
    We can see no disadvantages to this scheme, and a sampling of Host
reactions range from neutral to wildly enthusiastic.  Therefore, we
tentatively plan to implement this change.  We recognize that this
change will involve Host program changes, and that the new release must
be scheduled to coincide with those changes.  We propose providing
modified Host spec text along with a one week notice of the new release.
    If anyone sees a flaw in this scheme, or is unhappy about it, please
contact BBN quickly, since a new version of the IMP program is already
in the works.
       [ This RFC was put into machine readable form for entry ]
        [ into the online RFC archives by Kai Henningsen 5/97 ]
                                                                [Page 1]
```