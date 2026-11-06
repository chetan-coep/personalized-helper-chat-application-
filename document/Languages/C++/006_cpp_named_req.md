---
id: "c++_006"
technology: "C++"
category: "Languages"
title: "Named Requirements - cppreference.com"
doc_order: 6
source_url: "https://en.cppreference.com/cpp/named_req"
language: "en"
retrieved_at: "2026-11-03 17:55:48"
content_hash: "a9b34a2397a7e03eb11debc134da4be7813f5504257ecbc6d5044bcdf40274e2"
---

# Named Requirements - cppreference.com

Source: https://en.cppreference.com/cpp/named_req

---

# Named Requirements

The *named requirements* listed on this page are the named requirements used in the normative text of the C++ standard to define the expectations of the standard library.

The burden to ensure that library templates are instantiated with template arguments that satisfy these requirements is on the programmer. Failure to do so may result in very complex compiler diagnostics.

Some of these requirements are formalized in C++20 using the [concepts](https://en.cppreference.com/cpp/language/constraints) language feature.

| Basic |  | 
|  | specifies that an object of the type can be default constructed (named requirement) | 
|  | specifies that an object of the type can be constructed from rvalue (named requirement) | 
|  | specifies that an object of the type can be constructed from lvalue (named requirement) | 
|  | specifies that an object of the type can be assigned from rvalue (named requirement) | 
|  | specifies that an object of the type can be assigned from lvalue (named requirement) | 
|  | specifies that an object of the type can be destroyed (named requirement) | 
| Type properties |  | 
| Note: the standard does not define named requirements with names specified in this subcategory. These are type categories defined by the core language. They are included here as named requirements only for consistency. |  | 
|  | object types that are not array types or class types (named requirement) | 
|  | POD (Plain Old Data) types, compatible with C `struct` (named requirement) | 
|  | objects of these types can maintain their values after copying their underlying bytes (named requirement) | 
|  | objects of these types can be trivially constructed and copied (named requirement) | 
|  | these types are useful for communicating with code written in other programming languages (named requirement) | 
|  | objects of these types can be implicitly created, and their lifetimes can be implicitly started (named requirement) | 
| Library-wide |  | 
|  | boolean operations ( `operator&&`, `operator\|\|`, and `operator!`) have usual semantics (named requirement) | 
|  | `operator==` is an equivalence relation (named requirement) | 
|  | `operator<` is a strict weak ordering relation (named requirement) | 
|  | can be swapped with an unqualified non-member function call `swap()` (named requirement) | 
|  | a [LegacyIterator](https://en.cppreference.com/cpp/named_req/Iterator) that dereferences to a [Swappable](https://en.cppreference.com/cpp/named_req/Swappable) type (named requirement) | 
|  | a pointer-like type supporting a null value (named requirement) | 
|  | a [FunctionObject](https://en.cppreference.com/cpp/named_req/FunctionObject) that for inputs with different values has a low probability of giving the same output (named requirement) | 
|  | a class type that contains allocation information (named requirement) | 
|  | an object that can be called with the function call syntax (named requirement) | 
|  | a type for which the invoke operation is defined (named requirement) | 
|  | a [FunctionObject](https://en.cppreference.com/cpp/named_req/FunctionObject) that returns a value convertible to `bool` for one argument without modifying it (named requirement) | 
|  | a [FunctionObject](https://en.cppreference.com/cpp/named_req/FunctionObject) that returns a value convertible to `bool` for two arguments without modifying them (named requirement) | 
|  | a [BinaryPredicate](https://en.cppreference.com/cpp/named_req/BinaryPredicate) that establishes an ordering relation (named requirement) | 

| Container |  | 
|  | data structure that allows element access using iterators (named requirement) | 
|  | container using bidirectional iterators (named requirement) | 
|  | container using an allocator (named requirement) | 
|  | container with elements stored linearly (named requirement) | 
|  | container with elements stored at adjacent memory addresses (named requirement) | 
|  | container that stores elements by associating them to keys (named requirement) | 
|  | container that stores elements stored in buckets by associating them to keys (named requirement) | 
| Container element |  | 
|  | element can be default-constructed in uninitialized storage (named requirement) | 
|  | element can be copy-constructed in uninitialized storage (named requirement) | 
|  | element can be move-constructed in uninitialized storage (named requirement) | 
|  | element can be constructed in uninitialized storage (named requirement) | 
|  | element can be destroyed using an allocator (named requirement) | 
| Iterator |  | 
|  | general concept to access data within some data structure (named requirement) | 
|  | iterator that can be used to read data (named requirement) | 
|  | iterator that can be used to write data (named requirement) | 
|  | iterator that can be used to read data multiple times (named requirement) | 
|  | iterator that can be both incremented and decremented (named requirement) | 
|  | iterator that can be advanced in constant time (named requirement) | 
|  | iterator to contiguously-allocated elements (named requirement) | 
|  | iterator that can be used during constant expression evaluation (named requirement) | 
| Stream I/O functions |  | 
|  | a stream input function that does not skip leading whitespace and counts the processed characters (named requirement) | 
|  | a stream input function that skips leading whitespace (named requirement) | 
|  | a basic stream output function (named requirement) | 
|  | a stream output function that sets failbit on errors and returns a reference to the stream (named requirement) | 
| Formatters |  | 
|  | abstracts formatting operations for a given formatting argument type and character type (named requirement) | 
|  | defines functions used by the [formatting library](https://en.cppreference.com/cpp/utility/format) (named requirement) | 
| Random Number Generation |  | 
|  | consumes a sequence of integers and produces a sequence of 32-bit unsigned values (named requirement) | 
|  | returns uniformly distributed random unsigned integers (named requirement) | 
|  | a deterministic [UniformRandomBitGenerator](https://en.cppreference.com/cpp/named_req/UniformRandomBitGenerator), defined by the seed (named requirement) | 
|  | a [RandomNumberEngine](https://en.cppreference.com/cpp/named_req/RandomNumberEngine) that transforms the output of another [RandomNumberEngine](https://en.cppreference.com/cpp/named_req/RandomNumberEngine) (named requirement) | 
|  | returns random numbers distributed according to a given mathematical probability density function (named requirement) | 
| Concurrency |  | 
|  | provides exclusive ownership semantics for execution agents (i.e. threads) (named requirement) | 
|  | a [BasicLockable](https://en.cppreference.com/cpp/named_req/BasicLockable) that supports attempted lock acquisition (named requirement) | 
|  | a [Lockable](https://en.cppreference.com/cpp/named_req/Lockable) that supports timed lock acquisition (named requirement) | 
|  | provides shared ownership semantics for execution agents (i.e. threads) (named requirement) | 
|  | a [SharedLockable](https://en.cppreference.com/cpp/named_req/SharedLockable) that supports timed lock acquisition (named requirement) | 
|  | a [Lockable](https://en.cppreference.com/cpp/named_req/Lockable) that protects against data races and sequentially consistent synchronization (named requirement) | 
|  | a [TimedLockable](https://en.cppreference.com/cpp/named_req/TimedLockable) that protects against data races and sequentially consistent synchronization (named requirement) | 
|  | a [Mutex](https://en.cppreference.com/cpp/named_req/Mutex) that supports shared ownership semantics (named requirement) | 
|  | a [TimedMutex](https://en.cppreference.com/cpp/named_req/TimedMutex) that supports shared ownership semantics (named requirement) | 
| Ranges |  | 
|  | a [FunctionObject](https://en.cppreference.com/cpp/named_req/FunctionObject) that creates a [range adaptor](https://en.cppreference.com/cpp/ranges#Range_adaptors) from a [`viewable_range`](https://en.cppreference.com/cpp/ranges/viewable_range) and additional arguments (named requirement) | 
|  | a [FunctionObject](https://en.cppreference.com/cpp/named_req/FunctionObject) that supports the pipe operator (named requirement) | 
| Multidimensional View Customization |  | 
|  | controls the mapping of multidimensional index in mdspan (named requirement) | 
|  | a policy that holds [LayoutMapping](https://en.cppreference.com/cpp/named_req/LayoutMapping) requirements (named requirement) | 
|  | a policy that controls access to data handle in mdspan (named requirement) | 
| Other |  | 
|  | describes a property of a type (named requirement) | 
|  | describes a relationship between two types (named requirement) | 
|  | modifies a property of a type (named requirement) | 
|  | aggregates a duration, a time point, and a function to get the current time point (named requirement) | 
|  | a [Clock](https://en.cppreference.com/cpp/named_req/Clock) that does not throw exceptions (named requirement) | 
|  | defines types and functions for a character type (named requirement) | 
|  | bitset, integer, or enumeration (named requirement) | 
|  | a type for which initialization is effectively equal to assignment (named requirement) | 
|  | defines types and functions used by the [regular expressions library](https://en.cppreference.com/cpp/regex) (named requirement) | 
|  | a type with constexpr constructor (named requirement) | 

|  | This section is incomplete Reason: Any other missing requirement? |