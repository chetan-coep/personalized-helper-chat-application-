---
id: "c_012"
technology: "C"
category: "Languages"
title: "Date and time utilities - cppreference.com"
doc_order: 12
source_url: "https://en.cppreference.com/c/chrono"
language: "en"
retrieved_at: "2026-11-03 17:55:16"
content_hash: "3d3e39ed0f0515aa1f9dc71d21cc11325f266e0d502e46e7833407f15649da61"
---

# Date and time utilities - cppreference.com

Source: https://en.cppreference.com/c/chrono

---

# Date and time utilities

From cppreference.com

### Functions

| Time manipulation |  | 
|  | computes the difference between times (function) | 
|  | returns the current calendar time of the system as time since epoch (function) | 
|  | returns raw processor clock time since the program is started (function) | 
|  | returns the calendar time in seconds and nanoseconds based on a given time base (function) | 
|  | returns the resolution of calendar time based on a given time base (function) | 
| Format conversions |  | 
|  | converts a [tm](https://en.cppreference.com/c/chrono/tm) object to a textual representation (function) | 
|  | converts a [time\_t](https://en.cppreference.com/c/chrono/time_t) object to a textual representation (function) | 
|  | converts a [tm](https://en.cppreference.com/c/chrono/tm) object to custom textual representation (function) | 
|  | converts a [tm](https://en.cppreference.com/c/chrono/tm) object to custom wide string textual representation (function) | 
|  | converts time since epoch to calendar time expressed as Coordinated Universal Time (UTC) (function) | 
|  | converts time since epoch to calendar time expressed as local time (function) | 
|  | converts calendar time to time since epoch (function) | 
|  | converts calendar time to time since epoch, ignoring the Daylight Saving Time flag (function) | 

### Constants

|  | number of processor clock ticks per second (macro constant) | 

### Types

|  | calendar time type (struct) | 
|  | calendar time since epoch type (typedef) | 
|  | processor time since era type (typedef) | 
|  | time in seconds and nanoseconds (struct) | 

### References

- C23 standard (ISO/IEC 9899:2024):

  - 7.27 Date and time \<time.h> (p: TBD)

  - 7.29.5.1 The wcsftime function (p: TBD)

  - 7.31.14 Date and time \<time.h> (p: TBD)

- C17 standard (ISO/IEC 9899:2018):

  - 7.27 Date and time \<time.h> (p: 284-291)

  - 7.29.5.1 The wcsftime function (p: 320-321)

  - 7.31.14 Date and time \<time.h> (p: 333)

- C11 standard (ISO/IEC 9899:2011):

  - 7.27 Date and time \<time.h> (p: 388-397)

  - 7.29.5.1 The wcsftime function (p: 439-440)

  - 7.31.14 Date and time \<time.h> (p: 456)

- C99 standard (ISO/IEC 9899:1999):

  - 7.23 Date and time \<time.h> (p: 338-347)

  - 7.24.5.1 The wcsftime function (p: 385-386)

- C89/C90 standard (ISO/IEC 9899:1990):

  - 4.12 DATE AND TIME \<time.h>