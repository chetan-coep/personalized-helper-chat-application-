---
id: "c++_010"
technology: "C++"
category: "Languages"
title: "Diagnostics library - cppreference.com"
doc_order: 10
source_url: "https://en.cppreference.com/cpp/error"
language: "en"
retrieved_at: "2026-11-03 17:55:58"
content_hash: "f14f8f7b8e52815a6b2f2dc67e05d58c6c336af62b99aaedf5cee74241732565"
---

# Diagnostics library - cppreference.com

Source: https://en.cppreference.com/cpp/error

---

# Diagnostics library

### Exception handling

The header [`<exception>`](https://en.cppreference.com/cpp/header/exception) provides several classes and functions related to exception handling in C++ programs.

|  | base class for exceptions thrown by the standard library components (class) | 
| Capture and storage of exception objects |  | 
|  | checks if exception handling is currently in progress (function) | 
|  | shared pointer type for handling exception objects (typedef) | 
|  | creates an [std::exception\_ptr](https://en.cppreference.com/cpp/error/exception_ptr) from an exception object (function template) | 
|  | obtains the exception object in an [std::exception\_ptr](https://en.cppreference.com/cpp/error/exception_ptr) (function template) | 
|  | captures the current exception in an [std::exception\_ptr](https://en.cppreference.com/cpp/error/exception_ptr) (function) | 
|  | throws the exception from an [std::exception\_ptr](https://en.cppreference.com/cpp/error/exception_ptr) (function) | 
|  | a mixin type to capture and store current exceptions (class) | 
|  | throws its argument with [std::nested\_exception](https://en.cppreference.com/cpp/error/nested_exception) mixed in (function template) | 
|  | throws the exception from a [std::nested\_exception](https://en.cppreference.com/cpp/error/nested_exception) (function template) | 
| Handling of failures in exception handling |  | 
|  | function called when exception handling fails (function) | 
|  | the type of the function called by [std::terminate](https://en.cppreference.com/cpp/error/terminate) (typedef) | 
|  | obtains the current terminate\_handler (function) | 
|  | changes the function to be called by [std::terminate](https://en.cppreference.com/cpp/error/terminate) (function) | 
|  | exception thrown when [std::current\_exception](https://en.cppreference.com/cpp/error/current_exception) fails to copy the exception object (class) | 
| Handling of exception specification violations (until C++17) |  | 
|  | function called when dynamic exception specification is violated (function) | 
|  | the type of the function called by [std::unexpected](https://en.cppreference.com/cpp/error/unexpected) (typedef) | 
|  | obtains the current `unexpected_handler` (function) | 
|  | changes the function to be called by [std::unexpected](https://en.cppreference.com/cpp/error/unexpected) (function) | 

### Exception categories

Several convenience classes are predefined in the header `<stdexcept>` to report particular error conditions. These classes can be divided into two categories: *logic* errors and *runtime* errors. Logic errors are a consequence of faulty logic within the program and may be preventable. Runtime errors are due to events beyond the scope of the program and cannot easily be predicted.

|  | exception class to indicate violations of logical preconditions or class invariants (class) | 
|  | exception class to report invalid arguments (class) | 
|  | exception class to report domain errors (class) | 
|  | exception class to report attempts to exceed maximum allowed size (class) | 
|  | exception class to report arguments outside of expected range (class) | 
|  | exception class to indicate conditions only detectable at run time (class) | 
|  | exception class to report range errors in internal computations (class) | 
|  | exception class to report arithmetic overflows (class) | 
|  | exception class to report arithmetic underflows (class) | 
|  | exception class to cancel atomic transactions (class template) | 

### Error numbers

|  | macro which expands to POSIX-compatible thread-local error number variable (macro variable) | 
|  | macros for standard POSIX-compatible error conditions (macro constant) | 


### System error (since C++11)

The header `<system_error>` defines types and functions used to report error conditions originating from the operating system, streams I/O, [std::future](https://en.cppreference.com/cpp/thread/future), or other low-level APIs.

|  | base class for error categories (class) | 
|  | identifies the generic error category (function) | 
|  | identifies the operating system error category (function) | 
|  | holds a portable error code (class) | 
|  | The portable error condition enumeration listing all standard [`<cerrno>`](https://en.cppreference.com/cpp/header/cerrno) macro constants (class) | 
|  | holds a platform-dependent error code (class) | 
|  | exception class used to report conditions that have an error\_code (class) | 

### Assertions

Assertions help to implement checking of preconditions in programs.

|  | aborts the program if the user-specified condition is not `true`. May be disabled for release builds. (function macro) | 


### [Stacktrace](https://en.cppreference.com/cpp/utility/basic_stacktrace) (since C++23)

|  | representation of an evaluation in a stacktrace (class) | 
|  | approximate representation of an invocation sequence consists of stacktrace entries (class template) | 


### Debugging support (since C++26)

|  | pauses the running program when called (function) | 
|  | calls std::breakpoint if std::is\_debugger\_present returns `true` (function) | 
|  | checks whether a program is running under the control of a debugger (function) | 

### See also

| [`static_assert` declaration](https://en.cppreference.com/cpp/language/static_assert) (C++11) | performs compile-time assertion checking |