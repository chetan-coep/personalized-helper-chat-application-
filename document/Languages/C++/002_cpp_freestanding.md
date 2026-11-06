---
id: "c++_002"
technology: "C++"
category: "Languages"
title: "Freestanding and hosted implementations - cppreference.com"
doc_order: 2
source_url: "https://en.cppreference.com/cpp/freestanding"
language: "en"
retrieved_at: "2026-11-03 17:55:42"
content_hash: "828d6516a8509bcfb56f930a158666eaa1191e31d2c9177565639d3c9b215060"
---

# Freestanding and hosted implementations - cppreference.com

Source: https://en.cppreference.com/cpp/freestanding

---

# Freestanding and hosted implementations

There are two kinds of implementations defined by the C++ standard: ***hosted*** and ***freestanding*** implementations. For *hosted* implementations, the set of standard library headers required by the C++ standard is much larger than for *freestanding* ones. In a *freestanding* implementation, execution may happen without an operating system.

The kind of the implementation is implementation-defined. The predefined macro `__STDC_HOSTED__` is expanded to `1` for hosted implementations and `0` for freestanding implementations.(since C++11)

| Requirements on [multi-threaded executions and data races](https://en.cppreference.com/cpp/language/memory_model) | (since C++11) | 

| *freestanding* | *hosted* | 
|---|---|
| Under a *freestanding* implementation, it is implementation-defined whether a program can have more than one [thread of execution](https://en.cppreference.com/cpp/thread). | Under a *hosted* implementation, a C++ program can have more than one [thread](https://en.cppreference.com/cpp/thread) running concurrently. | 

### Requirements on the [`main`](https://en.cppreference.com/cpp/language/main_function) function

| *freestanding* | *hosted* | 
|---|---|
| In a *freestanding* implementation, it is implementation-defined whether a program is required to define a [`main`](https://en.cppreference.com/cpp/language/main_function) function. Start-up and termination is implementation-defined; start-up contains the execution of [constructors](https://en.cppreference.com/cpp/language/constructor) for objects of [namespace scope](https://en.cppreference.com/cpp/language/scope#Namespace_scope) with static storage duration; termination contains the execution of [destructors](https://en.cppreference.com/cpp/language/destructor) for objects with static [storage duration](https://en.cppreference.com/cpp/language/storage_duration). | In a *hosted* implementation, a program must contain a global function called [`main`](https://en.cppreference.com/cpp/language/main_function). Executing a program starts a main [thread of execution](https://en.cppreference.com/cpp/thread) in which the `main` function is invoked, and in which variables of static [storage duration](https://en.cppreference.com/cpp/language/storage_duration) might be initialized and destroyed. | 


### Requirements on [standard library headers](https://en.cppreference.com/cpp/header)

A *freestanding* implementation has an implementation-defined set of headers. This set includes at least the headers in the following table.

For partially freestanding headers, freestanding implementations only needs to provide part of the entities in the corresponding synopsis:

- If an entity is commented `// freestanding`, it is guaranteed to be provided.

|  | (since C++26) | 

- If an entity is declared in a header whose synopsis begins with `all freestanding` or `// mostly freestanding`, it is guaranteed to be provided if the entity itself is not commented.

#### Headers required for a freestanding implementation

| Library | Component | Headers | Freestanding | 
|---|---|---|---|
| [Language support](https://en.cppreference.com/cpp/utility#Language_support) | Common definitions | [`<cstddef>`](https://en.cppreference.com/cpp/header/cstddef) | All | 
|  | C standard library | [`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) | Partial | 
|  | Implementation properties | [`<cfloat>`](https://en.cppreference.com/cpp/header/cfloat) [`<climits>`](https://en.cppreference.com/cpp/header/climits) (since C++11) [`<limits>`](https://en.cppreference.com/cpp/header/limits) [`<version>`](https://en.cppreference.com/cpp/header/version) (since C++20) | All | 
|  | Integer types | [`<cstdint>`](https://en.cppreference.com/cpp/header/cstdint) (since C++11) | All | 
|  | Dynamic memory management | [`<new>`](https://en.cppreference.com/cpp/header/new) | All | 
|  | Type identification | [`<typeinfo>`](https://en.cppreference.com/cpp/header/typeinfo) | All | 
|  | Source location | [`<source_location>`](https://en.cppreference.com/cpp/header/source_location) (since C++20) | All | 
|  | Exception handling | [`<exception>`](https://en.cppreference.com/cpp/header/exception) | All | 
|  | Initializer lists | [`<initializer_list>`](https://en.cppreference.com/cpp/header/initializer_list) (since C++11) | All | 
|  | Comparisons | [`<compare>`](https://en.cppreference.com/cpp/header/compare) (since C++20) | All | 
|  | Coroutines support | [`<coroutine>`](https://en.cppreference.com/cpp/header/coroutine) (since C++20) | All | 
|  | Other runtime support | [`<cstdarg>`](https://en.cppreference.com/cpp/header/cstdarg) | All | 
|  | Debugging support | [`<debugging>`](https://en.cppreference.com/cpp/header/debugging) (since C++26) | All | 
| [Concepts](https://en.cppreference.com/cpp/concepts) |  | [`<concepts>`](https://en.cppreference.com/cpp/header/concepts) (since C++20) | All | 
| [Diagnostics](https://en.cppreference.com/cpp/error) | Error numbers | [`<cerrno>`](https://en.cppreference.com/cpp/header/cerrno) (since C++26) | Partial | 
|  | System error support | [`<system_error>`](https://en.cppreference.com/cpp/header/system_error) (since C++26) | Partial | 
| [Memory management](https://en.cppreference.com/cpp/memory) | Memory | [`<memory>`](https://en.cppreference.com/cpp/header/memory) (since C++23) | Partial | 
| [Metaprogramming](https://en.cppreference.com/cpp/meta) | Type traits | [`<type_traits>`](https://en.cppreference.com/cpp/header/type_traits) (since C++11) | All | 
|  | Compile-time rational arithmetic | [`<ratio>`](https://en.cppreference.com/cpp/header/ratio) (since C++23) | All | 
| [General utilities](https://en.cppreference.com/cpp/utility#General-purpose_utilities) | Utility components | [`<utility>`](https://en.cppreference.com/cpp/header/utility) (since C++23) | All | 
|  | Tuples | [`<tuple>`](https://en.cppreference.com/cpp/header/tuple) (since C++23) | All | 
|  | Function objects | [`<functional>`](https://en.cppreference.com/cpp/header/functional) (since C++20) | Partial | 
|  | Primitive numeric conversions | [`<charconv>`](https://en.cppreference.com/cpp/header/charconv) (since C++26) | Partial | 
|  | Bit manipulation | [`<bit>`](https://en.cppreference.com/cpp/header/bit) (since C++20) [`<stdbit.h>`](https://en.cppreference.com/cpp/header/stdbit.h) (since C++26) | All | 
| [Strings](https://en.cppreference.com/cpp/string) | String classes | [`<string>`](https://en.cppreference.com/cpp/header/string) (since C++26) | Partial | 
|  | Null-terminated sequence utilities | [`<cstring>`](https://en.cppreference.com/cpp/header/cstring) (since C++26) | Partial | 
| [Text processing](https://en.cppreference.com/cpp/text) | Null-terminated sequence utilities | [`<cwchar>`](https://en.cppreference.com/cpp/header/cwchar) (since C++26) | Partial | 
| [Iterators](https://en.cppreference.com/cpp/iterator) |  | [`<iterator>`](https://en.cppreference.com/cpp/header/iterator) (since C++23) | Partial | 
| [Ranges](https://en.cppreference.com/cpp/ranges) |  | [`<ranges>`](https://en.cppreference.com/cpp/header/ranges) (since C++23) | Partial | 
| [Numerics](https://en.cppreference.com/cpp/numeric) | Mathematical functions for floating-point types | [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) (since C++26) | Partial | 
|  | Random number generation | [`<random>`](https://en.cppreference.com/cpp/header/random) (since C++26) | Partial | 
| [Concurrency support](https://en.cppreference.com/cpp/thread) | Atomics | [`<atomic>`](https://en.cppreference.com/cpp/header/atomic) (since C++11) | All <sup>[\[1\]](https://en.cppreference.com#cite_note-1)</sup> | 
| [Execution control](https://en.cppreference.com/cpp/execution) |  | [`<execution>`](https://en.cppreference.com/cpp/header/execution) (since C++26) | Partial | 
| **Deprecated** headers |  | [`<ciso646>`](https://en.cppreference.com/cpp/header/ciso646) (until C++20) [`<cstdalign>`](https://en.cppreference.com/cpp/header/cstdalign) (since C++11)(until C++20) [`<cstdbool>`](https://en.cppreference.com/cpp/header/cstdbool) (since C++11)(until C++20) | All | 

1. [↑](https://en.cppreference.com#cite_ref-1) Support for always lock-free integral atomic types and presence of type aliases [std::atomic\_signed\_lock\_free](https://en.cppreference.com/cpp/atomic/atomic) and [std::atomic\_unsigned\_lock\_free](https://en.cppreference.com/cpp/atomic/atomic) are implementation-defined in a freestanding implementation.(since C++20)

### Notes

Some compiler vendors may not fully support freestanding implementation. For example, GCC libstdc++ has had implementation and build issues before version 13, while LLVM libcxx and MSVC STL do not support freestanding.

In C++23, many features are made freestanding with partial headers. However, it is still up for discussion in WG21 whether some headers will be made freestanding in the future standards. Regardless, containers like [vector](https://en.cppreference.com/cpp/container/vector), [list](https://en.cppreference.com/cpp/container/list), [deque](https://en.cppreference.com/cpp/container/deque), and [map](https://en.cppreference.com/cpp/container/map) will never be freestanding due to their dependencies on exceptions and heap.

GCC 13 provides more headers, such as [`<optional>`](https://en.cppreference.com/cpp/header/optional), [`<span>`](https://en.cppreference.com/cpp/header/span), [`<array>`](https://en.cppreference.com/cpp/header/array), and [`<bitset>`](https://en.cppreference.com/cpp/header/bitset), for freestanding, although these headers may not be portable or provide the same capabilities as a hosted implementation. It is better to avoid using them in a freestanding environment, even if the toolchain provides them.

### References

- C++23 standard (ISO/IEC 14882:2024):

  - 4.1 Implementation compliance \[intro.compliance\] (p: 10)

  - 6.9.2 Multi-threaded executions and data races \[intro.multithread\] (p: 84)

  - 6.9.3.1 main function \[basic.start.main\] (p: 89)

  - 16.4.2.5 Freestanding implementations \[compliance\] (p: 483)

- C++20 standard (ISO/IEC 14882:2020):

  - 4.1 Implementation compliance \[intro.compliance\] (p: 7)

  - 6.9.2 Multi-threaded executions and data races \[intro.multithread\] (p: 77)

  - 6.9.3.1 main function \[basic.start.main\] (p: 82)

  - 16.5.1.3 Freestanding implementations \[compliance\] (p: 470)

- C++17 standard (ISO/IEC 14882:2017):

  - 4.1 Implementation compliance \[intro.compliance\] (p: 5)

  - 4.7 Multi-threaded executions and data races \[intro.multithread\] (p: 15)

  - 6.6.1 main function \[basic.start.main\] (p: 66)

  - 20.5.1.3 Freestanding implementations \[compliance\] (p: 458)

- C++14 standard (ISO/IEC 14882:2014):

  - 1.4 Implementation compliance \[intro.compliance\] (p: 5)

  - 1.10 Multi-threaded executions and data races \[intro.multithread\] (p: 11)

  - 3.6.1 Main function \[basic.start.main\] (p: 62)

  - 17.6.1.3 Freestanding implementations \[compliance\] (p: 441)

- C++11 standard (ISO/IEC 14882:2011):

  - 1.4 Implementation compliance \[intro.compliance\] (p: 5)

  - 1.10 Multi-threaded executions and data races \[intro.multithread\] (p: 11)

  - 3.6.1 Main function \[basic.start.main\] (p: 58)

  - 17.6.1.3 Freestanding implementations \[compliance\] (p: 408)

- C++03 standard (ISO/IEC 14882:2003):

  - 1.4 Implementation compliance \[intro.compliance\] (p: 3)

  - 3.6.1 Main function \[basic.start.main\] (p: 43)

  - 17.4.1.3 Freestanding implementations \[lib.compliance\] (p: 326)

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [CWG 1938](https://cplusplus.github.io/CWG/issues/1938.html) | C++98 | an implementation did not need to document whether it is hosted | made the implementation kind implementation- defined (thus requires a documentation) | 
| [LWG 3653](https://cplusplus.github.io/LWG/issue3653) ( [P1642R11](https://wg21.link/P1642R11)) | C++20 | [`<coroutine>`](https://en.cppreference.com/cpp/header/coroutine) is freestanding, but uses [std::hash](https://en.cppreference.com/cpp/utility/hash) which was not | made [`<functional>`](https://en.cppreference.com/cpp/header/functional) being partially freestanding |