---
id: "c_005"
technology: "C"
category: "Languages"
title: "Type support - cppreference.com"
doc_order: 5
source_url: "https://en.cppreference.com/c/types"
language: "en"
retrieved_at: "2026-11-03 17:55:11"
content_hash: "df5421cb75bef69c5487d7e5e4c017a43972ef9f7cdae79de7483722c998f02e"
---

# Type support - cppreference.com

Source: https://en.cppreference.com/c/types

---

# Type support

See also [type system overview](https://en.cppreference.com/c/language/types) and [arithmetic types defined by the language](https://en.cppreference.com/c/language/arithmetic_types).

### Basic types

#### Additional basic types and convenience macros

|  | unsigned integer type returned by the [`sizeof`](https://en.cppreference.com/c/language/sizeof) operator (typedef) | 
|  | signed integer type returned when subtracting two pointers (typedef) | 
|  | the type of the predefined null pointer constant [`nullptr`](https://en.cppreference.com/c/language/nullptr) (typedef) | 
|  | implementation-defined null pointer constant (macro constant) | 
|  | a type with alignment requirement as great as any other scalar type (typedef) | 
|  | byte offset from the beginning of a struct type to specified member (function macro) | 
| bool (C99)(removed in C23) | convenience macro, expands to [`_Bool`](https://en.cppreference.com/c/keyword/_Bool) (keyword macro) | 
| true (C99)(removed in C23) | expands to integer constant `1` (macro constant) | 
| false (C99)(removed in C23) | expands to integer constant `0` (macro constant) | 
| \_\_bool\_true\_false\_are\_defined (C99)(deprecated in C23) | expands to integer constant `1` (macro constant) | 
| alignas (C11)(removed in C23) | convenience macro, expands to keyword [`_Alignas`](https://en.cppreference.com/c/keyword/_Alignas) (keyword macro) | 
| alignof (C11)(removed in C23) | convenience macro, expands to keyword [`_Alignof`](https://en.cppreference.com/c/keyword/_Alignof) (keyword macro) | 
| \_\_alignas\_is\_defined (C11)(removed in C23) | expands to integer constant `1` (macro constant) | 
| \_\_alignof\_is\_defined (C11)(removed in C23) | expands to integer constant `1` (macro constant) | 
| noreturn (C11)(deprecated in C23) | convenience macro, expands to [`_Noreturn`](https://en.cppreference.com/c/keyword/_Noreturn) (keyword macro) | 

#### [Fixed width integer types](https://en.cppreference.com/c/types/integer) (since C99)

### Notes

| The type of `true` and `false` is `int` rather than `_Bool`. A program may undefine and perhaps then redefine the macros `bool`, `true` and `false`. However, such ability is a deprecated feature. | (since C99) (until C23) | 
| The type of `true` and `false` is `bool`. It is unspecified whether any of `bool`, `_Bool`, `true`, or `false` is implemented as a predefined macro. If `bool`, `true`, or `false` (but not `_Bool`) is defined as a predefined macro, a program may undefine and perhaps redefine it. | (since C23) | 

### Example

```
#include <stdalign.h>
#include <stdbool.h>
#include <stdio.h>
int main(void)
{
    printf("%d %d %d\n", true && false, true || false, !false);
    printf("%d %d\n", true ^ true, true + true);
    printf("%zu\n", alignof(short));
}
```
Possible output:

### References

- C23 standard (ISO/IEC 9899:2024):

  - 7.15 Alignment \<stdalign.h> (p: TBD)

  - 7.18 Boolean type and values \<stdbool.h> (p: TBD)

  - 7.19 Common definitions \<stddef.h> (p: TBD)

  - 7.23 \_Noreturn \<stdnoreturn.h> (p: TBD)

  - 7.31.9 Boolean type and values \<stdbool.h> (p: TBD)

- C17 standard (ISO/IEC 9899:2018):

  - 7.15 Alignment \<stdalign.h> (p: 196)

  - 7.18 Boolean type and values \<stdbool.h> (p: 210)

  - 7.19 Common definitions \<stddef.h> (p: 211)

  - 7.23 \_Noreturn \<stdnoreturn.h> (p: 263)

  - 7.31.9 Boolean type and values \<stdbool.h> (p: 332)

- C11 standard (ISO/IEC 9899:2011):

  - 7.15 Alignment \<stdalign.h> (p: 268)

  - 7.18 Boolean type and values \<stdbool.h> (p: 287)

  - 7.19 Common definitions \<stddef.h> (p: 288)

  - 7.23 \_Noreturn \<stdnoreturn.h> (p: 361)

  - 7.31.9 Boolean type and values \<stdbool.h> (p: 456)

- C99 standard (ISO/IEC 9899:1999):

  - 7.18 Boolean type and values \<stdbool.h> (p: 253)

  - 7.19 Common definitions \<stddef.h> (p: 254)

  - 7.26.7 Boolean type and values \<stdbool.h> (p: 401)

- C89/C90 standard (ISO/IEC 9899:1990):

  - 4.1.5 Common definitions \<stddef.h>