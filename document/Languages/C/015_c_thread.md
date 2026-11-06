---
id: "c_015"
technology: "C"
category: "Languages"
title: "Concurrency support library - cppreference.com"
doc_order: 15
source_url: "https://en.cppreference.com/c/thread"
language: "en"
retrieved_at: "2026-11-03 17:55:18"
content_hash: "a0c0c8f4923ed541666c29cec0ae241a508a35b36324dfcb39c6ecb00040d2d2"
---

# Concurrency support library - cppreference.com

Source: https://en.cppreference.com/c/thread

---

# Concurrency support library

C includes built-in support for threads, atomic operations, mutual exclusion, condition variables, and thread-specific storages.

These features are optionally provided:

- if the macro constant `__STDC_NO_THREADS__` is defined by the compiler, the header [`<threads.h>`](https://en.cppreference.com/c/header/threads) and all of the names provided in it are not provided;
- if the macro constant `__STDC_NO_ATOMICS__` is defined by the compiler, the header [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) and all of the names provided in it are not provided.

See also  [type specifier and qualifier](https://en.cppreference.com/c/language/atomic).

### Threads

| **thrd_t** | implementation-defined complete object type identifying a thread | 
|  | creates a thread (function) | 
|  | checks if two identifiers refer to the same thread (function) | 
|  | obtains the current thread identifier (function) | 
|  | suspends execution of the calling thread for the given period of time (function) | 
|  | yields the current time slice (function) | 
|  | terminates the calling thread (function) | 
|  | detaches a thread (function) | 
|  | blocks until a thread terminates (function) | 
|  | indicates a thread error status (constant) | 
| thrd\_start\_t (C11) | a typedef of the function pointer type `int(*)(void*)`, used by `thrd_create` (typedef) | 

### Atomic operations

| Operations on atomic types |  | 
| (C11)(C11)(C23)(C11)(C11)(C11)(C11)(C11)(C11)(C11)(C11) | indicates that the given atomic type is lock-free (macro constant) | 
|  | indicates whether the atomic object is lock-free (function) | 
|  | stores a value in an atomic object (function) | 
|  | reads a value from an atomic object (function) | 
|  | swaps a value with the value of an atomic object (function) | 
|  | swaps a value with an atomic object if the old value is what is expected, otherwise reads the old value (function) | 
|  | atomic addition (function) | 
|  | atomic subtraction (function) | 
|  | atomic bitwise OR (function) | 
|  | atomic bitwise exclusive OR (function) | 
|  | atomic bitwise AND (function) | 
| Flag type and operations |  | 
|  | lock-free atomic boolean flag (struct) | 
|  | sets an atomic\_flag to true and returns the old value (function) | 
|  | sets an atomic\_flag to false (function) | 
| Initialization |  | 
|  | initializes an existing atomic object (function) | 
|  | initializes a new atomic object (function macro) | 
|  | initializes a new `atomic_flag` (macro constant) | 
| Memory synchronization ordering |  | 
|  | defines memory ordering constraints (enum) | 
|  | breaks a dependency chain for `memory_order_consume` (function macro) | 
|  | generic memory order-dependent fence synchronization primitive (function) | 
|  | fence between a thread and a signal handler executed in the same thread (function) | 

| Convenience type aliases |  | 
| Typedef name | Full type name | 
| `atomic_bool` (C11) | `_Atomic _Bool`(until C23)`_Atomic bool`(since C23) | 
| `atomic_char` (C11) | `_Atomic char` | 
| `atomic_schar` (C11) | `_Atomic signed char` | 
| `atomic_uchar` (C11) | `_Atomic unsigned char` | 
| `atomic_short` (C11) | `_Atomic short` | 
| `atomic_ushort` (C11) | `_Atomic unsigned short` | 
| `atomic_int` (C11) | `_Atomic int` | 
| `atomic_uint` (C11) | `_Atomic unsigned int` | 
| `atomic_long` (C11) | `_Atomic long` | 
| `atomic_ulong` (C11) | `_Atomic unsigned long` | 
| `atomic_llong` (C11) | `_Atomic long long` | 
| `atomic_ullong` (C11) | `_Atomic unsigned long long` | 
| `atomic_char8_t` (C23) | `_Atomic char8_t` | 
| `atomic_char16_t` (C11) | `_Atomic char16_t` | 
| `atomic_char32_t` (C11) | `_Atomic char32_t` | 
| `atomic_wchar_t` (C11) | `_Atomic wchar_t` | 
| `atomic_int_least8_t` (C11) | `_Atomic int_least8_t` | 
| `atomic_uint_least8_t` (C11) | `_Atomic uint_least8_t` | 
| `atomic_int_least16_t` (C11) | `_Atomic int_least16_t` | 
| `atomic_uint_least16_t` (C11) | `_Atomic uint_least16_t` | 
| `atomic_int_least32_t` (C11) | `_Atomic int_least32_t` | 
| `atomic_uint_least32_t` (C11) | `_Atomic uint_least32_t` | 
| `atomic_int_least64_t` (C11) | `_Atomic int_least64_t` | 
| `atomic_uint_least64_t` (C11) | `_Atomic uint_least64_t` | 
| `atomic_int_fast8_t` (C11) | `_Atomic int_fast8_t` | 
| `atomic_uint_fast8_t` (C11) | `_Atomic uint_fast8_t` | 
| `atomic_int_fast16_t` (C11) | `_Atomic int_fast16_t` | 
| `atomic_uint_fast16_t` (C11) | `_Atomic uint_fast16_t` | 
| `atomic_int_fast32_t` (C11) | `_Atomic int_fast32_t` | 
| `atomic_uint_fast32_t` (C11) | `_Atomic uint_fast32_t` | 
| `atomic_int_fast64_t` (C11) | `_Atomic int_fast64_t` | 
| `atomic_uint_fast64_t` (C11) | `_Atomic uint_fast64_t` | 
| `atomic_intptr_t` (C11) | `_Atomic intptr_t` | 
| `atomic_uintptr_t` (C11) | `_Atomic uintptr_t` | 
| `atomic_size_t` (C11) | `_Atomic size_t` | 
| `atomic_ptrdiff_t` (C11) | `_Atomic ptrdiff_t` | 
| `atomic_intmax_t` (C11) | `_Atomic intmax_t` | 
| `atomic_uintmax_t` (C11) | `_Atomic uintmax_t` | 

### Mutual exclusion

| **mtx_t** | mutex identifier | 
|  | creates a mutex (function) | 
|  | blocks until locks a mutex (function) | 
|  | blocks until locks a mutex or times out (function) | 
|  | locks a mutex or returns without blocking if already locked (function) | 
|  | unlocks a mutex (function) | 
|  | destroys a mutex (function) | 
|  | defines the type of a mutex (enum) | 
| Call once |  | 
|  | calls a function exactly once (function) | 

### Condition variables

| **cnd_t** | condition variable identifier | 
|  | creates a condition variable (function) | 
|  | unblocks one thread blocked on a condition variable (function) | 
|  | unblocks all threads blocked on a condition variable (function) | 
|  | blocks on a condition variable (function) | 
|  | blocks on a condition variable, with a timeout (function) | 
|  | destroys a condition variable (function) | 

### Thread-local storage

|  | convenience macro for storage-class specifier `_Thread_local` (keyword macro) | 
| **tss_t** | thread-specific storage pointer | 
|  | maximum number of times destructors are called (macro constant) | 
| **tss_dtor_t** (C11) | function pointer type `void(*)(void*)`, used for TSS destructor (typedef) | 
|  | creates thread-specific storage pointer with a given destructor (function) | 
|  | reads from thread-specific storage (function) | 
|  | write to thread-specific storage (function) | 
|  | releases the resources held by a given thread-specific pointer (function) | 

### Reserved identifiers

In future revisions of the C standard:

- function names, type names, and enumeration constants that begin with either `cnd_`, `mtx_`, `thrd_`, or `tss_`, and a lowercase letter may be added to the declarations in the `<threads.h>` header;
- macros that begin with `ATOMIC_` and an uppercase letter may be added to the macros defined in the [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) header;
- typedef names that begin with either `atomic_` or `memory_`, and a lowercase letter may be added to the declarations in the [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) header;
- enumeration constants that begin with `memory_order_` and a lowercase letter may be added to the definition of the [memory\_order](https://en.cppreference.com/c/atomic/memory_order) type in the [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) header;
- function names that begin with `atomic_` and a lowercase letter may be added to the declarations in the [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) header.

Identifiers reserved for functions names are always potentially(since C23) reserved for use as identifiers with external linkage, while other identifiers list here are potentially(since C23) reserved when [`<stdatomic.h>`](https://en.cppreference.com/c/header/stdatomic) is included.

Declaring, defining, or `#undef`ing such an identifier results in undefined behavior if it is provided by the standard or implementation(since C23). Portable programs should not use those identifiers.

### References

- C23 standard (ISO/IEC 9899:2024):

  - 7.17 Atomics \<stdatomic.h> (p: TBD)

  - 7.26 Threads \<threads.h> (p: TBD)

  - 7.31.8 Atomics \<stdatomic.h> (p: TBD)

  - 7.31.15 Threads \<threads.h> (p: TBD)

- C17 standard (ISO/IEC 9899:2018):

  - 7.17 Atomics \<stdatomic.h> (p: 200-209)

  - 7.26 Threads \<threads.h> (p: 274-283)

  - 7.31.8 Atomics \<stdatomic.h> (p: 332)

  - 7.31.15 Threads \<threads.h> (p: 333)

- C11 standard (ISO/IEC 9899:2011):

  - 7.17 Atomics \<stdatomic.h> (p: 273-286)

  - 7.26 Threads \<threads.h> (p: 376-387)

  - 7.31.8 Atomics \<stdatomic.h> (p: 455-456)

  - 7.31.15 Threads \<threads.h> (p: 456)

### See also

### External links

| [GNU GCC Libc Manual: ISO C Mutexes](https://www.gnu.org/software/libc/manual/html_node/ISO-C-Mutexes.html) |