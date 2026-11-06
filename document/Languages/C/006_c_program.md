---
id: "c_006"
technology: "C"
category: "Languages"
title: "Program support utilities - cppreference.com"
doc_order: 6
source_url: "https://en.cppreference.com/c/program"
language: "en"
retrieved_at: "2026-11-03 17:55:12"
content_hash: "adac0c717b8bb4dbcf770f6a4d636f8ee1e413997a5bfd659ac4c2b34fe9f316"
---

# Program support utilities - cppreference.com

Source: https://en.cppreference.com/c/program

---

# Program support utilities

From cppreference.com

### Program termination

The following functions manage program termination and resources cleanup.

|  | causes abnormal program termination (without cleaning up) (function) | 
|  | causes normal program termination with cleaning up (function) | 
|  | causes normal program termination without completely cleaning up (function) | 
|  | causes normal program termination without cleaning up (function) | 
|  | registers a function to be called on [exit()](https://en.cppreference.com/c/program/exit) invocation (function) | 
|  | registers a function to be called on [`quick_exit`](https://en.cppreference.com/c/program/quick_exit) invocation (function) | 
|  | indicates program execution execution status (macro constant) | 

### Unreachable control flow

|  | marks unreachable point of execution (function macro) | 

### Communicating with the environment

|  | calls the host environment's command processor (function) | 
|  | access to the list of environment variables (function) | 

### Memory alignment query

|  | queries the alignment of a pointer value (function) | 

### Signals

Several functions and macro constants for signal management are provided.

|  | sets a signal handler for particular signal (function) | 
|  | runs the signal handler for particular signal (function) | 
|  | the integer type that can be accessed as an atomic entity from an asynchronous signal handler (typedef) | 
|  | defines signal handling strategies (macro constant) | 
|  | error was encountered (macro constant) | 
| Signal types |  | 
|  | defines signal types (macro constant) | 

### Non-local jumps

|  | saves the context (function macro) | 
|  | jumps to specified location (function) | 
| Types |  | 
|  | execution context type (typedef) | 

### References

- C23 standard (ISO/IEC 9899:2024):

  - 7.13 Non-local jumps \<setjmp.h> (p: 283-284)

  - 7.14 Signal handling \<signal.h> (p: 285-287)

  - 7.24 General utilities \<stdlib.h> (p: 356-374)

  - 7.33.9 Signal handling \<signal.h> (p: 458)

  - 7.33.16 General utilities \<stdlib.h> (p: 458)

- C17 standard (ISO/IEC 9899:2018):

  - 7.13 Nonlocal jumps \<setjmp.h> (p: 191-192)

  - 7.14 Signal handling \<signal.h> (p: 193-195)

  - 7.22 General utilities \<stdlib.h> (p: 248-262)

  - 7.31.7 Signal handling \<signal.h> (p: 332)

  - 7.31.12 General utilities \<stdlib.h> (p: 333)

- C11 standard (ISO/IEC 9899:2011):

  - 7.13 Nonlocal jumps \<setjmp.h> (p: 262-264)

  - 7.14 Signal handling \<signal.h> (p: 265-267)

  - 7.22 General utilities \<stdlib.h> (p: 340-360)

  - 7.31.7 Signal handling \<signal.h> (p: 455)

  - 7.31.12 General utilities \<stdlib.h> (p: 456)

- C99 standard (ISO/IEC 9899:1999):

  - 7.13 Nonlocal jumps \<setjmp.h> (p: 243-245)

  - 7.14 Signal handling \<signal.h> (p: 246-248)

  - 7.20 General utilities \<stdlib.h> (p: 306-324)

  - 7.26.6 Signal handling \<signal.h> (p: 401)

  - 7.26.10 General utilities \<stdlib.h> (p: 402)

- C89/C90 standard (ISO/IEC 9899:1990):

  - 4.6 NON-LOCAL JUMPS \<setjmp.h>

  - 4.7 SIGNAL HANDLING \<signal.h>

  - 4.10 GENERAL UTILITIES \<stdlib.h>

  - 4.13.5 Signal handling \<signal.h>

  - 7.13.7 General utilities \<stdlib.h>