---
id: "c_004"
technology: "C"
category: "Languages"
title: "C Standard Library headers - cppreference.com"
doc_order: 4
source_url: "https://en.cppreference.com/c/header"
language: "en"
retrieved_at: "2026-11-03 17:55:11"
content_hash: "4dea8813c97c70e374ba243233437eb976f245309e8e33dda707c1f447424d8d"
---

# C Standard Library headers - cppreference.com

Source: https://en.cppreference.com/c/header

---

# C Standard Library headers

From cppreference.com

The interface of C standard library is defined by the following collection of headers.

### Feature test macros (since C23)

Feature test macros are defined in corresponding headers respectively since C23. Note that not all headers contain such a macro.

| # | Header | Macro name | Value | 
|---|---|---|---|
| 1 | [`<assert.h>`](https://en.cppreference.com/c/header/assert) | `__STDC_VERSION_ASSERT_H__` | `202311L` | 
| 2 | [`<complex.h>`](https://en.cppreference.com/c/header/complex) | `__STDC_VERSION_COMPLEX_H__` | `202311L` | 
| 3 | [`<ctype.h>`](https://en.cppreference.com/c/header/ctype) | N/A |  | 
| 4 | [`<errno.h>`](https://en.cppreference.com/c/header/errno) | N/A |  | 
| 5 | [`<fenv.h>`](https://en.cppreference.com/c/header/fenv) | `__STDC_VERSION_FENV_H__` | `202311L` | 
| 6 | [`<float.h>`](https://en.cppreference.com/c/header/float) | `__STDC_VERSION_FLOAT_H__` | `202311L` | 
| 7 | [`<inttypes.h>`](https://en.cppreference.com/c/header/inttypes) | `__STDC_VERSION_INTTYPES_H__` | `202311L` | 
| 8 | [`<iso646.h>`](https://en.cppreference.com/c/header/iso646) | N/A |  | 
| 9 | [`<limits.h>`](https://en.cppreference.com/c/header/limits) | `__STDC_VERSION_LIMITS_H__` | `202311L` | 
| 10 | [`<locale.h>`](https://en.cppreference.com/c/header/locale) | N/A |  | 
| 11 | [`<math.h>`](https://en.cppreference.com/c/header/math) | `__STDC_VERSION_MATH_H__` | `202311L` | 
| 12 | [`<setjmp.h>`](https://en.cppreference.com/c/header/setjmp) | `__STDC_VERSION_SETJMP_H__` | `202311L` | 
| 13 | [`<signal.h>`](https://en.cppreference.com/c/header/signal) | N/A |  | 
| 14 | [`<stdalign.h>`](https://en.cppreference.com/c/header/stdalign) | N/A |  | 
| 15 | [`<stdarg.h>`](https://en.cppreference.com/c/header/stdarg) | `__STDC_VERSION_STDARG_H__` | `202311L` | 
| 16 | [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) | `__STDC_VERSION_STDATOMIC_H__` | `202311L` | 
| 17 | [`<stdbit.h>`](https://en.cppreference.com/c/header/stdbit) | `__STDC_VERSION_STDBIT_H__` | `202311L` | 
| 18 | [`<stdbool.h>`](https://en.cppreference.com/c/header/stdbool) | N/A |  | 
| 19 | [`<stdckdint.h>`](https://en.cppreference.com/c/header/stdckdint) | `__STDC_VERSION_STDCKDINT_H__` | `202311L` | 
| 20 | [`<stddef.h>`](https://en.cppreference.com/c/header/stddef) | `__STDC_VERSION_STDDEF_H__` | `202311L` | 
| 21 | [`<stdint.h>`](https://en.cppreference.com/c/header/stdint) | `__STDC_VERSION_STDINT_H__` | `202311L` | 
| 22 | [`<stdio.h>`](https://en.cppreference.com/c/header/stdio) | `__STDC_VERSION_STDIO_H__` | `202311L` | 
| 23 | [`<stdlib.h>`](https://en.cppreference.com/c/header/stdlib) | `__STDC_VERSION_STDLIB_H__` | `202311L` | 
| 24 | [`<stdmchar.h>`](https://en.cppreference.com/c/header/stdmchar) | `__STDC_VERSION_STDMCHAR_H__` | `2029??L` | 
| 25 | [`<stdnoreturn.h>`](https://en.cppreference.com/c/header/stdnoreturn) | N/A |  | 
| 26 | [`<string.h>`](https://en.cppreference.com/c/header/string) | `__STDC_VERSION_STRING_H__` | `202311L` | 
| 27 | [`<tgmath.h>`](https://en.cppreference.com/c/header/tgmath) | `__STDC_VERSION_TGMATH_H__` | `202311L` | 
| 28 | [`<threads.h>`](https://en.cppreference.com/c/header/threads) | N/A |  | 
| 29 | [`<time.h>`](https://en.cppreference.com/c/header/time) | `__STDC_VERSION_TIME_H__` | `202311L` | 
| 30 | [`<uchar.h>`](https://en.cppreference.com/c/header/uchar) | `__STDC_VERSION_UCHAR_H__` | `202311L` | 
| 31 | [`<wchar.h>`](https://en.cppreference.com/c/header/wchar) | `__STDC_VERSION_WCHAR_H__` | `202311L` | 
| 32 | [`<wctype.h>`](https://en.cppreference.com/c/header/wctype) | N/A |  | 

### References

- C23 standard (ISO/IEC 9899:2024):

  - 7.1.2 Standard headers

- C17 standard (ISO/IEC 9899:2018):

  - 7.1.2 Standard headers (p: 131-132)

- C11 standard (ISO/IEC 9899:2011):

  - 7.1.2 Standard headers (p: 181-182)

- C99 standard (ISO/IEC 9899:1999):

  - 7.1.2 Standard headers (p: 165)

- C89/C90 standard (ISO/IEC 9899:1990):

  - 4.1.2 Standard headers