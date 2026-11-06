---
id: "c++_011"
technology: "C++"
category: "Languages"
title: "Memory management library - cppreference.com"
doc_order: 11
source_url: "https://en.cppreference.com/cpp/memory"
language: "en"
retrieved_at: "2026-11-03 17:55:59"
content_hash: "7736b44014f44e5b7186fdba0eed78f010ec662034ea4d93dea38d9ca51d1ec2"
---

# Memory management library - cppreference.com

Source: https://en.cppreference.com/cpp/memory

---

# Memory management library


### Smart pointers (since C++11)

Smart pointers enable automatic, exception-safe, object lifetime management.

| Pointer categories |  | 
|  | smart pointer with unique object ownership semantics (class template) | 
|  | smart pointer with shared object ownership semantics (class template) | 
|  | weak reference to an object managed by [std::shared\_ptr](https://en.cppreference.com/cpp/memory/shared_ptr) (class template) | 
|  | smart pointer with strict object ownership semantics (class template) | 
| Helper classes |  | 
|  | provides mixed-type owner-based ordering of shared and weak pointers (class template) | 
|  | provides owner-based hashing for shared and weak pointers (class) | 
|  | provides mixed-type owner-based equal comparisons of shared and weak pointers (class) | 
|  | allows an object to create a `shared_ptr` referring to itself (class template) | 
|  | exception thrown when accessing a `weak_ptr` which refers to already destroyed object (class) | 
|  | default deleter for [unique\_ptr](https://en.cppreference.com/cpp/memory/unique_ptr) (class template) | 
| Smart pointer adaptors (since C++23) |  | 
|  | interoperates with foreign pointer setters and resets a smart pointer on destruction (class template) | 
|  | creates an `out_ptr_t` with an associated smart pointer and resetting arguments (function template) | 
|  | interoperates with foreign pointer setters, obtains the initial pointer value from a smart pointer, and resets it on destruction (class template) | 
|  | creates an `inout_ptr_t` with an associated smart pointer and resetting arguments (function template) | 

### Allocators

Allocators are class templates encapsulating memory allocation strategy. This allows generic containers to decouple memory management from the data itself.

|  | the default allocator (class template) | 
|  | provides information about allocator types (class template) | 
|  | records the address and the actual size of storage allocated by `allocate_at_least` (class template) | 
|  | a tag used to select allocator-aware constructors (tag) | 
|  | checks if the specified type supports uses-allocator construction (class template) | 
|  | prepares the argument list matching the flavor of uses-allocator construction required by the given type (function template) | 
|  | creates an object of the given type by means of uses-allocator construction (function template) | 
|  | creates an object of the given type at specified memory location by means of uses-allocator construction (function template) | 
|  | implements multi-level allocator for multi-level containers (class template) | 
| Defined in  namespace `std::pmr` |  | 
|  | an allocator that supports run-time polymorphism based on the [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) it is constructed with (class template) | 


### Memory resources (since C++17)

Memory resources implement memory allocation strategies that can be used by [std::pmr::polymorphic\_allocator](https://en.cppreference.com/cpp/memory/polymorphic_allocator).

| Defined in  namespace `std::pmr` |  | 
|  | an abstract interface for classes that encapsulate memory resources (class) | 
|  | returns a static program-wide [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) that uses the global [operator new](https://en.cppreference.com/cpp/memory/new/operator_new) and [operator delete](https://en.cppreference.com/cpp/memory/new/operator_delete) to allocate and deallocate memory (function) | 
|  | returns a static [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) that performs no allocation (function) | 
|  | gets the default [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) (function) | 
|  | sets the default [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) (function) | 
|  | a set of constructor options for pool resources (class) | 
|  | a thread-safe [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) for managing allocations in pools of different block sizes (class) | 
|  | a thread-unsafe [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) for managing allocations in pools of different block sizes (class) | 
|  | a special-purpose [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) that releases the allocated memory only when the resource is destroyed (class) | 


### Explicit lifetime management (since C++23)

|  | implicitly creates objects in given storage with the object representation reused (function template) | 


### Types for composite class design (since C++26)

|  | a wrapper containing dynamically-allocated object with value-like semantics (class template) | 
|  | a polymorphic wrapper containing dynamically-allocated object with value-like semantics (class template) | 

### Miscellaneous

|  | provides information about pointer-like types (class template) | 
|  | obtains a raw pointer from a pointer-like type (function template) | 
|  | obtains actual address of an object, even if the **&** operator is overloaded (function template) | 
|  | aligns a pointer in a buffer (function) | 
|  | informs the compiler that a pointer is aligned (function template) | 
|  | checks whether the pointer points to an object whose alignment has at least the given value (function template) | 

Includes e.g. [operator new](https://en.cppreference.com/cpp/memory/new/operator_new), [operator delete](https://en.cppreference.com/cpp/memory/new/operator_delete), [std::set\_new\_handler](https://en.cppreference.com/cpp/memory/new/set_new_handler).

Includes e.g. [std::malloc](https://en.cppreference.com/cpp/memory/c/malloc), [std::free](https://en.cppreference.com/cpp/memory/c/free).


### Uninitialized storage (until C++20)

Several utilities are provided to create and access raw storage.

|  | an iterator that allows standard algorithms to store results in uninitialized memory (class template) | 
|  | obtains uninitialized storage (function template) | 
|  | frees uninitialized storage (function template) | 


### Garbage collector support (until C++23)

|  | declares that an object can not be recycled (function) | 
|  | declares that an object can be recycled (function template) | 
|  | declares that a memory area does not contain traceable pointers (function) | 
|  | cancels the effect of [std::declare\_no\_pointers](https://en.cppreference.com/cpp/memory/gc/declare_no_pointers) (function) | 
|  | lists pointer safety models (enum) | 
|  | returns the current pointer safety model (function) |