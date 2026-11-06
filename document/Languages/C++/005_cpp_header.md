---
id: "c++_005"
technology: "C++"
category: "Languages"
title: "C++ Standard Library headers - cppreference.com"
doc_order: 5
source_url: "https://en.cppreference.com/cpp/header"
language: "en"
retrieved_at: "2026-11-03 17:55:47"
content_hash: "a2cdc48d12c8b09a9602bfc21a934b114d20554d63485ac491896460de25d107"
---

# C++ Standard Library headers - cppreference.com

Source: https://en.cppreference.com/cpp/header

---

# C++ Standard Library headers

The interface of C++ standard library is defined by the following collection of headers.

### C compatibility headers

For some of the C standard library headers of the form *xxx*.h`c` (all meaningful *xxx*`c` headers are listed above). The intended use of headers of form *xxx**xxx*.h

With the exception of [`complex.h`](https://en.cppreference.com/cpp/header/ccomplex), each *xxx*.h`c` header would have placed in the *xxx*`std` namespace.

These headers are allowed to also declare the same names in the `std` namespace, and the corresponding `c` headers are allowed to also declare the same names in the global namespace: including *xxx*[`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) definitely provides [std::malloc](https://en.cppreference.com/cpp/memory/c/malloc) and may also provide `::malloc`. Including [`<stdlib.h>`](https://en.cppreference.com/c/header/stdlib) definitely provides `::malloc` and may also provide [std::malloc](https://en.cppreference.com/cpp/memory/c/malloc). This applies even to functions and function overloads that are not part of C standard library.

Notes: *xxx*.h

|  | Behaves same as [`<cassert>`](https://en.cppreference.com/cpp/header/cassert) | 
|  | Behaves as if each name from [`<cctype>`](https://en.cppreference.com/cpp/header/cctype) is placed in global namespace | 
|  | Behaves same as [`<cerrno>`](https://en.cppreference.com/cpp/header/cerrno) | 
|  | Behaves as if each name from [`<cfenv>`](https://en.cppreference.com/cpp/header/cfenv) is placed in global namespace | 
|  | Behaves same as [`<cfloat>`](https://en.cppreference.com/cpp/header/cfloat) | 
|  | Behaves as if each name from [`<cinttypes>`](https://en.cppreference.com/cpp/header/cinttypes) is placed in global namespace | 
|  | Behaves same as [`<climits>`](https://en.cppreference.com/cpp/header/climits) | 
|  | Behaves as if each name from [`<clocale>`](https://en.cppreference.com/cpp/header/clocale) is placed in global namespace | 
|  | Behaves as if each name from [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) is placed in global namespace, except for names of [mathematical special functions](https://en.cppreference.com/cpp/numeric/special_functions) | 
|  | Behaves as if each name from [`<csetjmp>`](https://en.cppreference.com/cpp/header/csetjmp) is placed in global namespace | 
|  | Behaves as if each name from [`<csignal>`](https://en.cppreference.com/cpp/header/csignal) is placed in global namespace | 
|  | Behaves as if each name from [`<cstdarg>`](https://en.cppreference.com/cpp/header/cstdarg) is placed in global namespace | 
|  | Behaves as if each name from [`<cstddef>`](https://en.cppreference.com/cpp/header/cstddef) is placed in global namespace, except for names of [`std::byte` and related functions](https://en.cppreference.com/cpp/types/byte) | 
|  | Behaves as if each name from [`<cstdint>`](https://en.cppreference.com/cpp/header/cstdint) is placed in global namespace | 
|  | Behaves as if each name from [`<cstdio>`](https://en.cppreference.com/cpp/header/cstdio) is placed in global namespace | 
|  | Behaves as if each name from [`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) is placed in global namespace | 
|  | Behaves as if each name from [`<cstring>`](https://en.cppreference.com/cpp/header/cstring) is placed in global namespace | 
|  | Behaves as if each name from [`<ctime>`](https://en.cppreference.com/cpp/header/ctime) is placed in global namespace | 
|  | Behaves as if each name from [`<cuchar>`](https://en.cppreference.com/cpp/header/cuchar) is placed in global namespace | 
|  | Behaves as if each name from [`<cwchar>`](https://en.cppreference.com/cpp/header/cwchar) is placed in global namespace | 
|  | Behaves as if each name from [`<cwctype>`](https://en.cppreference.com/cpp/header/cwctype) is placed in global namespace | 

#### Special C compatibility headers

The headers [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic), [`<stdbit.h>`](https://en.cppreference.com/c/header/stdbit), and [`<stdckdint.h>`](https://en.cppreference.com/c/header/stdckdint) declare names which are also provided in the C standard library. The header [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) also defines the [`_Atomic`](https://en.cppreference.com/c/keyword/_Atomic) macro which is a [keyword](https://en.cppreference.com/c/keyword) in C. Unlike other `<` headers, corresponding *xxx*.h>`<cstdatomic>`, `<cstdbit>`, and `<cstdckdint>` are not provided.

|  | Defines `_Atomic` and provides corresponding components in the C standard library | 
|  | Provides corresponding components in the C standard library | 
|  | Provides corresponding components in the C standard library | 

#### Empty C headers

The headers [`<complex.h>`](https://en.cppreference.com/c/header/complex), [`<ccomplex>`](https://en.cppreference.com/cpp/header/ccomplex), [`<tgmath.h>`](https://en.cppreference.com/c/header/tgmath), and [`<ctgmath>`](https://en.cppreference.com/cpp/header/ctgmath) do not contain any content from the C standard library and instead merely include other headers from the C++ standard library.

|  | Simply includes the header [`<complex>`](https://en.cppreference.com/cpp/header/complex) | 
|  | Simply includes the header [`<complex>`](https://en.cppreference.com/cpp/header/complex) | 
|  | Simply includes the headers [`<complex>`](https://en.cppreference.com/cpp/header/complex) and [`<cmath>`](https://en.cppreference.com/cpp/header/cmath): the overloads equivalent to the contents of the C header [`<tgmath.h>`](https://en.cppreference.com/c/header/tgmath) are already provided by those headers | 
|  | Simply includes the headers [`<complex>`](https://en.cppreference.com/cpp/header/complex) and [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) | 

#### Meaningless C headers

The headers [`<ciso646>`](https://en.cppreference.com/cpp/header/ciso646), [`<cstdalign>`](https://en.cppreference.com/cpp/header/cstdalign), and [`<cstdbool>`](https://en.cppreference.com/cpp/header/cstdbool) are meaningless in C++ because the macros they provide in C are language keywords in C++.

|  | Empty header. [The macros that appear in `iso646.h` in C](https://en.cppreference.com/c/language/operator_alternative) are [keywords in C++](https://en.cppreference.com/cpp/language/operator_alternative) | 
|  | Defines one [compatibility macro constant](https://en.cppreference.com/cpp/types) | 
|  | Defines one [compatibility macro constant](https://en.cppreference.com/cpp/types) | 
|  | Has no effect | 
|  | Defines one [compatibility macro constant](https://en.cppreference.com/cpp/types) | 
|  | Defines one [compatibility macro constant](https://en.cppreference.com/cpp/types) | 

#### Unsupported C headers

The C headers [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic),(until C++23) [`<stdnoreturn.h>`](https://en.cppreference.com/c/header/stdnoreturn), and [`<threads.h>`](https://en.cppreference.com/c/header/threads) are not included in C++ and have no `c` equivalents.
*xxx*

[C++ TR's/TS's](https://en.cppreference.com/cpp/experimental) also define several collections of headers.