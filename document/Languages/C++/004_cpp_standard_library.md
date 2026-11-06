---
id: "c++_004"
technology: "C++"
category: "Languages"
title: "C++ Standard Library - cppreference.com"
doc_order: 4
source_url: "https://en.cppreference.com/cpp/standard_library"
language: "en"
retrieved_at: "2026-11-03 17:55:45"
content_hash: "784aad71a19828693a8c17d09a9e654ddb55a0461100a72b611f0c71204ba948"
---

# C++ Standard Library - cppreference.com

Source: https://en.cppreference.com/cpp/standard_library

---

# C++ Standard Library

The C++ standard library provides a wide range of facilities that are usable in standard C++.

### Category

The [language support library](https://en.cppreference.com/cpp/utility#Language_support) provides components that are required by certain parts of the C++ language, such as memory allocation ([new](https://en.cppreference.com/cpp/language/new)/[delete](https://en.cppreference.com/cpp/language/delete)) and [exception processing](https://en.cppreference.com/cpp/language/exceptions).

| The [concepts library](https://en.cppreference.com/cpp/concepts) describes library components that C++ programs may use to perform compile-time validation of [template arguments](https://en.cppreference.com/cpp/language/template_parameters) and perform function dispatch based on properties of types. | (since C++20) | 

The [diagnostics library](https://en.cppreference.com/cpp/error) provides a consistent framework for reporting errors in a C++ program, including [predefined exception classes](https://en.cppreference.com/cpp/error#Exception_categories).

The [memory management library](https://en.cppreference.com/cpp/memory) provides components for memory management, including [smart pointers](https://en.cppreference.com/cpp/memory#Smart_pointers) and [scoped allocator](https://en.cppreference.com/cpp/memory/scoped_allocator_adaptor)(since C++11).

| The [metaprogramming library](https://en.cppreference.com/cpp/meta) describes facilities for use in [templates](https://en.cppreference.com/cpp/language/templates) and during constant evaluation, including [type traits](https://en.cppreference.com/cpp/meta#Type_traits), [integer sequence](https://en.cppreference.com/cpp/utility/integer_sequence),(since C++14) and [rational arithmetic](https://en.cppreference.com/cpp/numeric/ratio). | (since C++11) | 

The [general utilities library](https://en.cppreference.com/cpp/utility#General-purpose_utilities) includes components used by other library elements, such as a [predefined storage allocator](https://en.cppreference.com/cpp/memory#Allocators) for dynamic storage management, and components used as infrastructure in C++ programs, such as [tuples](https://en.cppreference.com/cpp/utility/tuple) and(since C++11) [function wrappers](https://en.cppreference.com/cpp/utility/functional).

The [containers](https://en.cppreference.com/cpp/container), [iterators](https://en.cppreference.com/cpp/iterator), [ranges](https://en.cppreference.com/cpp/ranges)(since C++20), and [algorithms](https://en.cppreference.com/cpp/algorithm) libraries provide a C++ program with access to a subset of the most widely used algorithms and data structures.

The [strings library](https://en.cppreference.com/cpp/string) provides support for manipulating text represented as homogeneous sequences of following types: `char`, `char8_t`(since C++20), `char16_t`, `char32_t`(since C++11), `wchar_t`, and any other character-like types.

The [text processing library](https://en.cppreference.com/cpp/text) provides [regular expression](https://en.cppreference.com/cpp/regex) matching and searching(since C++11), utilities for [text formatting](https://en.cppreference.com/cpp/utility/format)(since C++20) and [identifying text encodings](https://en.cppreference.com/cpp/text/text_encoding)(since C++26), and [localization facilities](https://en.cppreference.com/cpp/locale).

The [numerics library](https://en.cppreference.com/cpp/numeric) provides [numeric algorithms](https://en.cppreference.com/cpp/numeric#Numeric_algorithms) and [complex number](https://en.cppreference.com/cpp/numeric/complex) components that extend support for numeric processing. The [valarray](https://en.cppreference.com/cpp/numeric/valarray) component provides support for n-at-a-time processing, potentially implemented as parallel operations on platforms that support such processing. The [random number component](https://en.cppreference.com/cpp/numeric/random) provides facilities for generating pseudo-random numbers.(since C++11)

The [time library](https://en.cppreference.com/cpp/chrono) provides generally useful time utilities.

The [input/output library](https://en.cppreference.com/cpp/io) provides the [iostream components](https://en.cppreference.com/cpp/io#Stream-based_I/O) that are the primary mechanism for C++ program input and output. They can be used with other elements of the library, particularly strings, locales, and iterators.

| The [thread support library](https://en.cppreference.com/cpp/thread) provides components to create and manage threads, including [atomic operations](https://en.cppreference.com/cpp/atomic/atomic), [mutual exclusion](https://en.cppreference.com/cpp/thread/mutex), and inter-thread communication. | (since C++11) | 


| The [execution support](https://en.cppreference.com/cpp/execution) library provides a framework for managing asynchronous execution on generic execution resources. | (since C++26) | 

### Library contents

The C++ standard library provides definitions for the [entities](https://en.cppreference.com/cpp/language/basic_concepts) and [macros](https://en.cppreference.com/cpp/preprocessor/replace) described in the synopses of the [C++ standard library headers](https://en.cppreference.com/cpp/headers), unless otherwise specified.

All library entities except [operator new](https://en.cppreference.com/cpp/memory/new/operator_new) and [operator delete](https://en.cppreference.com/cpp/memory/new/operator_delete) are defined within the namespace `std` or [namespaces](https://en.cppreference.com/cpp/language/namespace) nested within namespace `std` (except the entities for the C standard library facilities, see below). It is unspecified whether names declared in a specific namespace are declared directly in that namespace or in an [inline namespace](https://en.cppreference.com/cpp/language/namespace#Inline_namespaces) inside that namespace.(since C++11)

#### Headers

Each element of the C++ standard library is declared or defined (as appropriate) in a *header*. A header is not necessarily a source file, nor are the sequences delimited by **\<****>**

The C++ standard library provides the *C++ library headers* and *additional C++ headers for C library facilities* (see “[headers](https://en.cppreference.com/cpp/headers)” page for descriptions):

| C++ headers for C library facilities |  |  |  |  | 
|---|---|---|---|---|
| [`<cassert>`](https://en.cppreference.com/cpp/header/cassert) | [`<clocale>`](https://en.cppreference.com/cpp/header/clocale) | [`<cstdarg>`](https://en.cppreference.com/cpp/header/cstdarg) | [`<cstring>`](https://en.cppreference.com/cpp/header/cstring) |  | 
| [`<cctype>`](https://en.cppreference.com/cpp/header/cctype) | [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) | [`<cstddef>`](https://en.cppreference.com/cpp/header/cstddef) | [`<ctime>`](https://en.cppreference.com/cpp/header/ctime) |  | 
| [`<cerrno>`](https://en.cppreference.com/cpp/header/cerrno) | [`<csetjmp>`](https://en.cppreference.com/cpp/header/csetjmp) | [`<cstdio>`](https://en.cppreference.com/cpp/header/cstdio) | [`<cwchar>`](https://en.cppreference.com/cpp/header/cwchar) |  | 
| [`<cfloat>`](https://en.cppreference.com/cpp/header/cfloat) | [`<csignal>`](https://en.cppreference.com/cpp/header/csignal) | [`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) | [`<cwctype>`](https://en.cppreference.com/cpp/header/cwctype) |  | 
| [`<climits>`](https://en.cppreference.com/cpp/header/climits) |  |  |  |  | 
| Headers added in C++11 |  |  |  |  | 
| [`<cfenv>`](https://en.cppreference.com/cpp/header/cfenv) | [`<cinttypes>`](https://en.cppreference.com/cpp/header/cinttypes) | [`<cstdint>`](https://en.cppreference.com/cpp/header/cstdint) | [`<cuchar>`](https://en.cppreference.com/cpp/header/cuchar) |  | 
| Removed headers |  |  |  |  | 
| [`<ccomplex>`](https://en.cppreference.com/cpp/header/ccomplex) | (since C++11)(deprecated in C++17)(removed in C++20) |  |  |  | 
| [`<ciso646>`](https://en.cppreference.com/cpp/header/ciso646) | (removed in C++20) |  |  |  | 
| [`<cstdalign>`](https://en.cppreference.com/cpp/header/cstdalign) | (since C++11)(deprecated in C++17)(removed in C++20) |  |  |  | 
| [`<cstdbool>`](https://en.cppreference.com/cpp/header/cstdbool) | (since C++11)(deprecated in C++17)(removed in C++20) |  |  |  | 
| [`<ctgmath>`](https://en.cppreference.com/cpp/header/ctgmath) | (since C++11)(deprecated in C++17)(removed in C++20) |  |  |  | 

A [freestanding implementation](https://en.cppreference.com/cpp/freestanding) has an implementation-defined set of headers, see [here](https://en.cppreference.com/cpp/freestanding#header_requirements) for the minimal requirement on the set of headers.

### C standard library

The C++ standard library also makes available the facilities of the C standard library, suitably adjusted to ensure static type safety. The descriptions of many library functions rely on the C standard library for the semantics of those functions.

In some cases, the signatures specified in standard C++ may be different from the signatures in the C standard library, and additional overloads may be declared, but the behavior and the preconditions (including those implied by C's [`restrict`](https://en.cppreference.com/c/language/restrict))(since C++17) are the same unless otherwise stated.

For compatibility with the C standard library, the C++ standard library provides the C headers listed below. The intended use of these headers is for interoperability only. It is possible that C++ source files need to include one of these headers in order to be valid ISO C. Source files that are not intended to also be valid ISO C should not use any of the C headers. See [here](https://en.cppreference.com/cpp/headers#C_compatibility_headers) for descriptions.

| C headers |  |  |  | 
|---|---|---|---|
| [`<assert.h>`](https://en.cppreference.com/cpp/header/cassert) | [`<limits.h>`](https://en.cppreference.com/cpp/header/climits) | [`<stdarg.h>`](https://en.cppreference.com/cpp/header/cstdarg) | [`<string.h>`](https://en.cppreference.com/cpp/header/cstring) | 
| [`<ctype.h>`](https://en.cppreference.com/cpp/header/cctype) | [`<locale.h>`](https://en.cppreference.com/cpp/header/clocale) | [`<stddef.h>`](https://en.cppreference.com/cpp/header/cstddef) | [`<time.h>`](https://en.cppreference.com/cpp/header/ctime) | 
| [`<errno.h>`](https://en.cppreference.com/cpp/header/cerrno) | [`<math.h>`](https://en.cppreference.com/cpp/header/cmath) | [`<stdio.h>`](https://en.cppreference.com/cpp/header/cstdio) | [`<wchar.h>`](https://en.cppreference.com/cpp/header/cwchar) | 
| [`<float.h>`](https://en.cppreference.com/cpp/header/cfloat) | [`<setjmp.h>`](https://en.cppreference.com/cpp/header/csetjmp) | [`<stdlib.h>`](https://en.cppreference.com/cpp/header/cstdlib) | [`<wctype.h>`](https://en.cppreference.com/cpp/header/cwctype) | 
| [`<iso646.h>`](https://en.cppreference.com/cpp/header/ciso646) | [`<signal.h>`](https://en.cppreference.com/cpp/header/csignal) |  |  | 
| Headers added in C++11 |  |  |  | 
| [`<complex.h>`](https://en.cppreference.com/cpp/header/ccomplex) | [`<inttypes.h>`](https://en.cppreference.com/cpp/header/cinttypes) | [`<stdbool.h>`](https://en.cppreference.com/cpp/header/cstdbool) | [`<tgmath.h>`](https://en.cppreference.com/cpp/header/ctgmath) | 
| [`<fenv.h>`](https://en.cppreference.com/cpp/header/cfenv) | [`<stdalign.h>`](https://en.cppreference.com/cpp/header/cstdalign) | [`<stdint.h>`](https://en.cppreference.com/cpp/header/cstdint) | [`<uchar.h>`](https://en.cppreference.com/cpp/header/cuchar) | 
| Headers added in C++23 |  |  |  | 
| [`<stdatomic.h>`](https://en.cppreference.com/cpp/header/stdatomic.h) |  |  |  | 
| Headers added in C++26 |  |  |  | 
| [`<stdbit.h>`](https://en.cppreference.com/cpp/header/stdbit.h) | [`<stdckdint.h>`](https://en.cppreference.com/cpp/header/stdckdint.h) |  |  | 

Except otherwise noted, the contents of each header `c` is the same as that of the corresponding header *xxx**xxx*.h[C standard library](https://en.cppreference.com/c/header). In the C++ standard library, however, the declarations (except for names which are defined as macros in C) are within namespace scope of the namespace `std`. It is unspecified whether these names (including any overloads added) are first declared within the global namespace scope and are then injected into namespace `std` by explicit [using-declarations](https://en.cppreference.com/cpp/language/namespace#Using-declarations).

Names which are defined as macros in C ([`assert`](https://en.cppreference.com/cpp/error/assert), [`offsetof`](https://en.cppreference.com/cpp/types/offsetof), [`setjmp`](https://en.cppreference.com/cpp/utility/program/setjmp), [`va_arg`](https://en.cppreference.com/cpp/utility/variadic/va_arg), [`va_end`](https://en.cppreference.com/cpp/utility/variadic/va_end) and [`va_start`](https://en.cppreference.com/cpp/utility/variadic/va_start)) must be defined as macros in the C++ standard library, even if C grants license for implementation as functions.

Names that are defined as functions in C must be defined as functions in the C++ standard library. This disallows the practice, allowed in C, of providing a masking macro in addition to the function prototype. The only way to achieve equivalent inline behavior in C++ is to provide a definition as an extern [inline function](https://en.cppreference.com/cpp/language/inline).

Identifiers that are keywords or operators in C++ cannot be defined as macros in C++ standard library headers. In particular, including the standard header [`<iso646.h>`](https://en.cppreference.com/cpp/header/ciso646) has no effect.

#### Names associated with safe functions in standard C (since C++17)

If any C++ header is included, it is implementation-defined whether any of the following C standard Annex K names is declared in the global namespace (none of them is declared in namespace `std`):

### Using the library

#### Including headers

The entities in the C++ standard library are defined in headers, whose contents are made available to a translation unit when it contains the appropriate 
[`#include`](https://en.cppreference.com/cpp/preprocessor/include) preprocessing directive.

A translation unit may include library headers in any order. Each may be included more than once, with no effect different from being included exactly once, except that the effect of including either [`<cassert>`](https://en.cppreference.com/cpp/header/cassert) or [`<assert.h>`](https://en.cppreference.com/cpp/header/cassert) depends each time on the lexically current definition of `NDEBUG`.

A translation unit can only include a header outside of any declaration or definition, and lexically before the first reference in that translation unit to any of the entities declared in that header. No diagnostic is required.

| In [module units](https://en.cppreference.com/cpp/language/modules), headers can only be included in [global module fragments](https://en.cppreference.com/cpp/language/modules#Global_module_fragment). | (since C++20) | 

| Importing headers The [C++ library headers](https://en.cppreference.com#Headers), or, for a freestanding implementation, the subset of such headers that are provided by the implementation, are collectively known as the *importable C++ library headers*. The contents of importable C++ library headers are made available to a translation unit when it contains the appropriate [import declaration](https://en.cppreference.com/cpp/language/modules#Importing_modules_and_headers). | (since C++20) | 
| Importing modules The C++ standard library provides the following *C++ library modules*: For each declaration in the standard library, | (since C++23) | 

#### Linkage

Entities in the C++ standard library have [storage duration#external linkage](https://en.cppreference.com/cpp/language/storage_duration#external_linkage). Unless otherwise specified, objects and functions have the default `extern "C++"` [linkage](https://en.cppreference.com/cpp/language/language_linkage).

Whether a name from the C standard library declared with external linkage has `extern "C"` or `extern "C++"` linkage is implementation-defined. The C++ standard recommends using `extern "C++"` in this case.

Objects and functions defined in the library and required by a C++ program are included in the program prior to program startup.

### Requirements on standard library implementations

#### Guarantees

A C++ header must provide [declarations](https://en.cppreference.com/cpp/language/declarations) and [definitions](https://en.cppreference.com/cpp/language/definition) that appear in

- the synopsis of that header, or
- the synopsis of another header which is appeared to be included in the synopsis of that header.

For types and macros defined in multiple headers (such as [`NULL`](https://en.cppreference.com/cpp/types/NULL)), including any number of these headers in any order never violates the [one definition rule](https://en.cppreference.com/cpp/language/definition#One_Definition_Rule).

Unless otherwise specified, all [object-like macros](https://en.cppreference.com/cpp/preprocessor/replace#Object-like_macros) defined by the C standard library that expand to integral [constant expressions](https://en.cppreference.com/cpp/language/constant_expression) can be used in [`#if`](https://en.cppreference.com/cpp/preprocessor/conditional) preprocessing directives.

Calling a standard library non-member function signature always results in actually calling that function. Therefore a conforming standard library implementation cannot define additional non-member functions that may be called by a valid C++ program.

Non-member function signatures are never declared with additional [default arguments](https://en.cppreference.com/cpp/language/default_arguments).

Unless otherwise specified, calls made by functions in the standard library to non-operator, non-member functions do not use functions from another [namespace](https://en.cppreference.com/cpp/language/namespace) which are found through [argument-dependent name lookup](https://en.cppreference.com/cpp/language/adl).

For each [friend declaration](https://en.cppreference.com/cpp/language/friend) of a function (template) within a class (template) definition, no other declaration is provided for that function (template).

| Standard library function signatures can only be declared as `constexpr` if they are required to be [constexpr](https://en.cppreference.com/cpp/language/constexpr) (libstdc++ cmath [is notably non-conforming](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=102916) here). If a header provides any non-defining declarations of constexpr functions or constructors, the corresponding definitions should also be provided within that header. Unless otherwise specified, each standard library function should meet each of the following requirements to prevent [data races](https://en.cppreference.com/cpp/language/memory_model#Threads_and_data_races): | (since C++11) | 

For each class defined in the C++ standard library required to be [derived](https://en.cppreference.com/cpp/language/derived_class) from another class defined in the C++ standard library,

- the base class must be [virtual](https://en.cppreference.com/cpp/language/derived_class#Virtual_base_classes) if it is specified as `virtual`,
- the base class cannot be virtual if it is not specified as `virtual`, and
- unless otherwise specified, types with distinct names shall be distinct types.

| Unless otherwise specified, all types specified in the C++ standard library are non-[final](https://en.cppreference.com/cpp/language/final) types. | (since C++11) | 

If a function defined in the C++ standard library is specified to throw an [exception](https://en.cppreference.com/cpp/language/exceptions) (in a particular situation) of a given type, the exception thrown can only have that type or a type derived from that type so that an exception handler for the base type can catch it.

Functions from the C standard library can only throw exceptions when such a function calls a program-supplied function that throws an exception ([`qsort()`](https://en.cppreference.com/cpp/algorithm/qsort) and [`bsearch()`](https://en.cppreference.com/cpp/algorithm/bsearch) meet this condition).

Destructor operations defined in the C++ standard library never throw exceptions. Every destructor in the C++ standard library behaves as if it had a [non-throwing exception specification](https://en.cppreference.com/cpp/language/noexcept_spec).

| If a function in the C++ standard library report errors via a [std::error\_code](https://en.cppreference.com/cpp/error/error_code) object, that object's [`category()`](https://en.cppreference.com/cpp/error/error_code/category) member must return [std::system\_category()](https://en.cppreference.com/cpp/error/system_category) for errors originating from the operating system, or a reference to an implementation-defined [std::error\_category](https://en.cppreference.com/cpp/error/error_category) object for errors originating elsewhere. The possible values of [`value()`](https://en.cppreference.com/cpp/error/error_code/value) for each of these error categories should be defined. Objects of types defined in the C++ standard library may be [moved from](https://en.cppreference.com/cpp/language/move_constructor). Move operations can either be explicitly specified or implicitly generated. Unless otherwise specified, such moved-from objects will be placed in a valid but unspecified state. An object of a type defined in the C++ standard library may be [move-assigned](https://en.cppreference.com/cpp/language/move_assignment) to itself. Unless otherwise specified, such an assignment places the object in a valid but unspecified state. | (since C++11) | 

#### Implementation freedom

It is unspecified whether any member or non-member functions in the C++ standard library are defined as [inline](https://en.cppreference.com/cpp/language/inline).

For a non-[virtual](https://en.cppreference.com/cpp/language/virtual) C++ standard library member function, a different set of member function signatures can be declared, provided that any call to that member function that would select an overload from the given set of declarations behaves as if that overload was selected. This allows, for instance:

- adding parameters with default arguments,
- replacing a member function with default arguments with two or more member functions with equivalent behavior, or
- adding additional signatures for a member function name.

Unless otherwise specified, it is implementation-defined which functions in the C++ standard library may be recursively reentered.

| C++ standard library implementations can share their own internal objects between threads if the objects are not visible to users and are protected against data races. | (since C++11) | 

It is unspecified whether any function signature or class in the C++ standard library is a friend of another class in the C++ standard library.

The names and global function signatures described [here](https://en.cppreference.com#Library_contents) are reserved to the implementation.

Any class in the C++ standard library can be derived from a class with a name reserved to the implementation. If a class defined in the C++ standard library is required to be derived from other classes in the C++ standard library, that class can be derived directly from the required base or indirectly through a hierarchy of base classes with names reserved to the implementation.

If a function defined in the C++ standard library is not specified to throw an exception but does not have a non-throwing exception specification, the exception thrown is implementation-defined, but its type should be [std::exception](https://en.cppreference.com/cpp/error/exception) or any type derived from [std::exception](https://en.cppreference.com/cpp/error/exception).

The exception specification for a non-virtual function can be strengthened by adding a non-throwing exception specification.

| ===Standard library hardening=== An implementation can be a *hardened implementation *, whether the implementation is hardened is implementation-defined. Some standard library functions (and function templates) have *hardened precondition *. When such a function is invoked: Functions with hardened preconditions  | (since C++26) | 

|  | - all overloads have hardened preconditions | 
|  | - some overloads have hardened preconditions | 

### Notes

### Example

```
import std;
struct Str : std::string // OK, std::string cannot be final
{
    ~Str(); // Guaranteed to be noexcept
};
int main()
{
    std::puts("Hello stdlib!");
    // ::puts("Hello stdlib!"); // Requires std.compat module or stdio.h header
    // constexpr auto& void_info = std::any().type(); // any::type cannot be constexpr
    std::string p, q;
    q = std::move(p); // OK, p is left in a valid (but unspecified) state
                      // This includes self move assignment q = std::move(q)
    // return EXIT_SUCCESS; // Macro EXIT_SUCCESS is not provided by either stdlib module
}
```
Output:

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [LWG 1](https://cplusplus.github.io/LWG/issue1) | C++98 | the language linkages of the names from the C standard library were unspecified | they are implementation-defined | 
| [LWG 119](https://cplusplus.github.io/LWG/issue119) | C++98 | the exception specifications of virtual functions could be strengthened | only allowed for non-virtual functions | 
| [LWG 147](https://cplusplus.github.io/LWG/issue147) | C++98 | the specification on non-member functions only considered global functions | also considers non-global functions | 
| [LWG 225](https://cplusplus.github.io/LWG/issue225) | C++98 | standard library functions might call non-member functions from other namespaces due to argument-dependent lookup | prohibited unless otherwise specified | 
| [LWG 336](https://cplusplus.github.io/LWG/issue336) | C++98 | [`<strstream>`](https://en.cppreference.com/cpp/header/strstream) was not a C++ library header | it is a C++ library header | 
| [LWG 343](https://cplusplus.github.io/LWG/issue343) | C++98 | library header dependencies were not specified | specified (listed in synopses) | 
| [LWG 456](https://cplusplus.github.io/LWG/issue456) | C++98 | C++ headers for C library facilities could only provide definitions in namespace `std` | allowed to define in global namespace and then inject into namespace `std` | 
| [LWG 465](https://cplusplus.github.io/LWG/issue465) | C++98 | identifiers that are keywords or operators in C++ could be defined as macros in C++ standard library headers (only [`<ciso646>`](https://en.cppreference.com/cpp/header/ciso646) is required not to define them as macros) | all C++ standard library headers cannot define them as macros | 
| [LWG 1178](https://cplusplus.github.io/LWG/issue1178) | C++98 | C++ headers must include a C++ header that contains any needed definition | C++ headers must provide declarations and definitions that are directly or indirectly included in its synopsis | 
| [LWG 2013](https://cplusplus.github.io/LWG/issue2013) | C++11 | it was unspecified whether the functions not required by the standard to be constexpr can be declared `constexpr` by the standard library | prohibited | 
| [LWG 2225](https://cplusplus.github.io/LWG/issue2225) | C++98 | a diagnostic was required if a header is included at an incorrect position | no diagnostic is required in this case |