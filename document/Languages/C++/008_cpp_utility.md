---
id: "c++_008"
technology: "C++"
category: "Languages"
title: "Utility library - cppreference.com"
doc_order: 8
source_url: "https://en.cppreference.com/cpp/utility"
language: "en"
retrieved_at: "2026-11-03 17:55:56"
content_hash: "7053285b2b64636bc3805892212c1629973a4cab14666b835a817109b63472f5"
---

# Utility library - cppreference.com

Source: https://en.cppreference.com/cpp/utility

---

# Utility library

C++ includes a variety of utility libraries that provide functionality ranging from [bit-counting](https://en.cppreference.com/cpp/utility/bitset) to [partial function application](https://en.cppreference.com/cpp/utility/functional/bind). These libraries can be broadly divided into two groups:

- language support libraries, and
- general-purpose libraries.

## Language support

Language support libraries provide classes and functions that interact closely with language features and support common language idioms.


### [Implementation properties](https://en.cppreference.com/cpp/utility/feature_test) (since C++20)

The header [`<version>`](https://en.cppreference.com/cpp/header/version) supplies implementation-dependent information about the C++ standard library (such as the version number and release date). It also defines the [library feature-test macros](https://en.cppreference.com/cpp/utility/feature_test).

Basic types (e.g. [std::size\_t](https://en.cppreference.com/cpp/types/size_t), [std::nullptr\_t](https://en.cppreference.com/cpp/types/nullptr_t)), RTTI (e.g. [std::type\_info](https://en.cppreference.com/cpp/types/type_info))

Termination (e.g. [std::abort](https://en.cppreference.com/cpp/utility/program/abort), [std::atexit](https://en.cppreference.com/cpp/utility/program/atexit)), environment (e.g. [std::system](https://en.cppreference.com/cpp/utility/program/system)), signals (e.g. [std::raise](https://en.cppreference.com/cpp/utility/program/raise)).

Smart pointers (e.g. [std::shared\_ptr](https://en.cppreference.com/cpp/memory/shared_ptr)), allocators (e.g. [std::allocator](https://en.cppreference.com/cpp/memory/allocator) or [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource)), C-style memory management (e.g. [std::malloc](https://en.cppreference.com/cpp/memory/c/malloc)).

Exceptions (e.g. [std::exception](https://en.cppreference.com/cpp/error/exception), [std::terminate](https://en.cppreference.com/cpp/error/terminate)), assertions (e.g. [assert](https://en.cppreference.com/cpp/error/assert)).

Support for functions that take an arbitrary number of parameters (via e.g. [va\_start](https://en.cppreference.com/cpp/utility/variadic/va_start), [va\_arg](https://en.cppreference.com/cpp/utility/variadic/va_arg), [va\_end](https://en.cppreference.com/cpp/utility/variadic/va_end)).


### [Initializer lists](https://en.cppreference.com/cpp/utility/initializer_list) (since C++11)

|  | references a temporary array created in [list-initialization](https://en.cppreference.com/cpp/language/list_initialization) (class template) | 


### [Source code information capture](https://en.cppreference.com/cpp/utility/source_location) (since C++20)

|  | a class representing information about the source code, such as file names, line numbers, and function names (class) | 


### Three-way comparison (since C++20)

|  | specifies that operator `<=>` produces consistent result on given types (concept) | 
|  | the result type of 3-way comparison that supports all 6 operators, is not substitutable, and allows incomparable values (class) | 
|  | the result type of 3-way comparison that supports all 6 operators and is not substitutable (class) | 
|  | the result type of 3-way comparison that supports all 6 operators and is substitutable (class) | 
|  | named comparison functions (function) | 
|  | constrained function object implementing `x <=> y` (class) | 
|  | obtains the result type of the three-way comparison operator `<=>` on given types (class template) | 
|  | the strongest comparison category to which all of the given types can be converted (class template) | 
|  | performs 3-way comparison and produces a result of type `std::strong_ordering` (customization point object) | 
|  | performs 3-way comparison and produces a result of type `std::weak_ordering` (customization point object) | 
|  | performs 3-way comparison and produces a result of type `std::partial_ordering` (customization point object) | 
|  | performs 3-way comparison and produces a result of type `std::strong_ordering`, even if `operator<=>` is unavailable (customization point object) | 
|  | performs 3-way comparison and produces a result of type `std::weak_ordering`, even if `operator<=>` is unavailable (customization point object) | 
|  | performs 3-way comparison and produces a result of type `std::partial_ordering`, even if `operator<=>` is unavailable (customization point object) | 
|  | performs three-way comparison on types (class template) | 


### [Coroutine support](https://en.cppreference.com/cpp/coroutine) (since C++20)

Types for [coroutine](https://en.cppreference.com/cpp/language/coroutines) support (e.g. [std::coroutine\_traits](https://en.cppreference.com/cpp/coroutine/coroutine_traits), [std::coroutine\_handle](https://en.cppreference.com/cpp/coroutine/coroutine_handle)).


### [Contract support](https://en.cppreference.com/cpp/contract) (since C++26)

Types for [contract](https://en.cppreference.com/cpp/language/contracts) support (e.g. [`std::contracts::contract_violation`](https://en.cppreference.com/cpp/contract/contract_violation)).

## General-purpose utilities

### Swap

|  | swaps the values of two objects (function template) | 
|  | replaces the argument with a new value and returns its previous value (function template) | 
|  | swaps the values of two objects (customization point object) | 


### Type operations (since C++11)

|  | forwards a function argument and use the type template argument to preserve its value category (function template) | 
|  | forwards a function argument as if casting it to the value category and constness of the expression of specified type template argument (function template) | 
|  | converts the argument to an xvalue (function template) | 
|  | converts the argument to an xvalue if the move constructor does not throw (function template) | 
|  | obtains a reference to `const` to its argument (function template) | 
|  | obtains a reference to an object of the template type argument for use in an unevaluated context (function template) | 
|  | converts an enumeration to its underlying type (function template) | 


### Integer comparison functions (since C++20)

|  | compares two integer values, ensuring that signed negative numbers are less than unsigned numbers (function template) | 
|  | checks if an integer value is in the range of a given integer type (function template) | 


### Relational operators (until C++20)

| Defined in  namespace `std::rel_ops` |  | 
|  | automatically generates comparison operators based on user-defined `operator==` and `operator<` (function template) | 


|  | piecewise construction tag (tag) | 
|  | in-place construction tag (tag) | 
|  | value construction tag (tag) | 


### Undefined behavior utilities (since C++23)

|  | marks unreachable point of execution (function) | 
|  | establishes an observable checkpoint (function) | 

|  | implements binary tuple, i.e. a pair of values (class template) | 
|  | implements fixed size container, which holds elements of possibly different types (class template) | 
|  | calls a function with a tuple of arguments (function template) | 
|  | construct an object with a tuple of arguments (function template) | 
| [Tuple protocol](https://en.cppreference.com/cpp/utility/tuple/tuple-like) (since C++11) |  | 
|  | obtains the number of elements of a [tuple-like](https://en.cppreference.com/cpp/utility/tuple/tuple-like) type (class template) | 
|  | obtains the element types of a [tuple-like](https://en.cppreference.com/cpp/utility/tuple/tuple-like) type (class template) | 


### Sum types and type erased wrappers (since C++17)

|  | a wrapper that may or may not hold an object (class template) | 
|  | a wrapper that contains either an expected or error value (class template) | 
|  | a type-safe discriminated union (class template) | 
|  | objects that hold instances of any [CopyConstructible](https://en.cppreference.com/cpp/named_req/CopyConstructible) type (class) | 

|  | implements constant length bit array (class template) | 


### [Bit manipulation](https://en.cppreference.com/cpp/utility/bit) (since C++20)

The header [`<bit>`](https://en.cppreference.com/cpp/header/bit) provides several function templates to access, manipulate, and process individual bits and bit sequences. The byte ordering ([endianness](https://en.cppreference.com/cpp/types/endian)) of scalar types can be inspected via `std::endian` facility.


### [Function objects](https://en.cppreference.com/cpp/utility/functional) (since C++11)

Partial function application (e.g. [std::bind](https://en.cppreference.com/cpp/utility/functional/bind)) and related utilities: utilities for binding such as [std::ref](https://en.cppreference.com/cpp/utility/functional/ref)  and [std::placeholders](https://en.cppreference.com/cpp/utility/functional/placeholders), polymorphic function wrappers: [std::function](https://en.cppreference.com/cpp/utility/functional/function), predefined functors (e.g. [std::plus](https://en.cppreference.com/cpp/utility/functional/plus), [std::equal\_to](https://en.cppreference.com/cpp/utility/functional/equal_to)), pointer-to-member to function converters [std::mem\_fn](https://en.cppreference.com/cpp/utility/functional/mem_fn).


### [Hash support](https://en.cppreference.com/cpp/utility/hash) (since C++11)

|  | hash function object (class template) |