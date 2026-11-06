---
id: "c_008"
technology: "C"
category: "Languages"
title: "Error handling - cppreference.com"
doc_order: 8
source_url: "https://en.cppreference.com/c/error"
language: "en"
retrieved_at: "2026-11-03 17:55:13"
content_hash: "596214cc1e9032e43fc2bbca2a30d2a5847f5c91a788339dec9673fe9158f3d5"
---

# Error handling - cppreference.com

Source: https://en.cppreference.com/c/error

---

# Error handling

### Error numbers

|  | macro which expands to POSIX-compatible thread-local error number variable (macro variable) | 
|  | macros for standard POSIX-compatible error conditions (macro constant) | 

### Assertions

|  | aborts the program if the user-specified condition is not `true`. May be disabled for release builds (function macro) | 
|  | issues a compile-time diagnostic if the value of a constant expression is false (keyword macro) | 

| Bounds checking The standard library provides bounds-checked versions of some existing functions ([gets\_s](https://en.cppreference.com/c/io/gets), [fopen\_s](https://en.cppreference.com/c/io/fopen), [printf\_s](https://en.cppreference.com/c/io/fprintf), [strcpy\_s](https://en.cppreference.com/c/string/byte/strcpy), [wcscpy\_s](https://en.cppreference.com/c/string/wide/wcscpy), [mbstowcs\_s](https://en.cppreference.com/c/string/multibyte/mbstowcs), [qsort\_s](https://en.cppreference.com/c/algorithm/qsort), [getenv\_s](https://en.cppreference.com/c/program/getenv), etc). This functionality is *optional* and is only available if `__STDC_LIB_EXT1__` is defined. The following macros and functions support this functionality. Note: implementations of bounds-checked functions are available as open-source libraries [Safe C](https://github.com/rurban/safeclib/) and [Slibc](https://code.google.com/archive/p/slibc/), and as part of Watcom C. There is also an incompatible set of bounds-checked functions available in Visual Studio. | (since C11) | 

| errno\_t (C11) | a typedef for the type `int`, used to self-document functions that return [errno](https://en.cppreference.com/c/error/errno) values (typedef) | 
| rsize\_t (C11) | a typedef for the same type as [size\_t](https://en.cppreference.com/c/types/size_t), used to self-document functions that range-check their parameters at runtime (typedef) | 
| RSIZE\_MAX (C11) | largest acceptable size for bounds-checked functions, expands to either constant or variable which may change at runtime (e.g. as the currently allocated memory size changes) (macro variable) | 
|  | set the error callback for bounds-checked functions (function) | 
|  | abort callback for the bounds-checked functions (function) | 
|  | ignore callback for the bounds-checked functions (function) | 

### Notes

Since C23, [`static_assert`](https://en.cppreference.com/c/language/_Static_assert) is itself a keyword, which may also be a predefined macro, so `<assert.h>` no longer provides it.

### References

| Extended content | 
|---|
|  | 

### See also

|  | defines the error handling mechanism used by the common mathematical functions (macro constant) |