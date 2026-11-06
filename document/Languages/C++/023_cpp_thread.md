---
id: "c++_023"
technology: "C++"
category: "Languages"
title: "Concurrency support library (since C++11) - cppreference.com"
doc_order: 23
source_url: "https://en.cppreference.com/cpp/thread"
language: "en"
retrieved_at: "2026-11-03 17:56:20"
content_hash: "433624b2d772025b2aca5d710fd34a474526bb8d15dba0f71fe7171d767d2166"
---

# Concurrency support library (since C++11) - cppreference.com

Source: https://en.cppreference.com/cpp/thread

---

# Concurrency support library (since C++11)

C++ includes built-in support for threads, atomic operations, mutual exclusion, condition variables, and futures.

### Threads

Threads enable programs to execute across several processor cores.

|  | manages a separate thread (class) | 
|  | [std::thread](https://en.cppreference.com/cpp/thread/thread) with support for auto-joining and cancellation (class) | 
| Functions managing the current thread |  | 
| Defined in  namespace `this_thread` |  | 
|  | suggests that the implementation reschedule execution of threads (function) | 
|  | returns the thread id of the current thread (function) | 
|  | stops the execution of the current thread for a specified time duration (function) | 
|  | stops the execution of the current thread until a specified time point (function) | 


### Cooperative cancellation (since C++20)

The components *stop source*, *stop token*, and *stop callback* can be used to asynchronously request that an operation stops execution in a timely manner, typically because the result is no longer required. Such a request is called a *stop request*.

These components specify the semantics of shared access to a *stop state*. Any object modeling any of these components that refer to the same stop state is an associated stop source, stop token, or stop callback, respectively.

| The concepts [`*stoppable-source*`](https://en.cppreference.com/index.php?title=cpp/thread/stoppable-source&action=edit&redlink=1), [`stoppable_token`](https://en.cppreference.com/cpp/thread/stoppable_token), and [`*stoppable-callback-for*`](https://en.cppreference.com/index.php?title=cpp/thread/stoppable-callback-for&action=edit&redlink=1) specify the required syntax and model semantics of stop source, stop token, and stop callback, respectively. | [(since C++26)](https://en.cppreference.com/cpp/compiler_support/26#P2300R10) | 

They are designed:

- to cooperatively cancel the execution such as for [std::jthread](https://en.cppreference.com/cpp/thread/jthread),
- to interrupt [std::condition\_variable\_any](https://en.cppreference.com/cpp/thread/condition_variable_any) waiting functions,

|  | [(since C++26)](https://en.cppreference.com/cpp/compiler_support/26#P2300R10) | 

- or for a custom execution management implementation.

In fact, they do not even need to be used to “stop” anything, but can instead be used for a thread-safe one-time function(s) invocation trigger, for example.

| Stop token types |  | 
|  | an interface for querying if a [std::jthread](https://en.cppreference.com/cpp/thread/jthread) cancellation request has been made (class) | 
|  | provides a stop token interface that a stop is never possible nor requested (class) | 
|  | a stop token that references stop state of its associated `std::inplace_stop_source` object (class) | 
| Stop source types |  | 
|  | class representing a request to stop one or more [std::jthread](https://en.cppreference.com/cpp/thread/jthread)s (class) | 
|  | a *stoppable source* that is the sole owner of its stop-state (class) | 
| Stop callback types |  | 
|  | an interface for registering callbacks on [std::jthread](https://en.cppreference.com/cpp/thread/jthread) cancellation (class template) | 
|  | a stop callback for `std::inplace_stop_token` (class template) | 
|  | obtains the callback type for a given stop token type (alias template) | 
| Concepts (since C++20) |  | 
|  | specifies the basic interface of stop tokens which allows queries for stop requests and whether the stop request is possible (concept) | 
|  | specifies a stop token that does not allow stopping (concept) | 
|  | specifies that a type is a factory for associated stop tokens and a stop request can be made upon it (exposition-only concept\*) | 
|  | specifies an interface for registering callbacks with a given stop token type (exposition-only concept\*) | 


### Cache size access (since C++17)

|  | min offset to avoid false sharing max offset to promote true sharing (constant) | 

### Atomic operations

These components are provided for fine-grained atomic operations allowing for lockless concurrent programming. Each atomic operation is indivisible with regards to any other atomic operation that involves the same object. Atomic objects are [free of data races](https://en.cppreference.com/cpp/language/memory_model#Threads_and_data_races).

| Atomic types |  | 
|  | atomic class template and specializations for bool, integral, floating-point,(since C++20) and pointer types (class template) | 
|  | provides atomic operations on non-atomic objects (class template) | 
| Operations on atomic types |  | 
|  | checks if the atomic type's operations are lock-free (function template) | 
|  | atomically replaces the value of the atomic object with a non-atomic argument (function template) | 
|  | atomically obtains the value stored in an atomic object (function template) | 
|  | atomically replaces the value of the atomic object with non-atomic argument and returns the old value of the atomic (function template) | 
|  | atomically compares the value of the atomic object with non-atomic argument and performs atomic exchange if equal or atomic load if not (function template) | 
|  | adds a non-atomic value to an atomic object and obtains the previous value of the atomic (function template) | 
|  | subtracts a non-atomic value from an atomic object and obtains the previous value of the atomic (function template) | 
|  | replaces the atomic object with the result of bitwise AND with a non-atomic argument and obtains the previous value of the atomic (function template) | 
|  | replaces the atomic object with the result of bitwise OR with a non-atomic argument and obtains the previous value of the atomic (function template) | 
|  | replaces the atomic object with the result of bitwise XOR with a non-atomic argument and obtains the previous value of the atomic (function template) | 
|  | replaces the atomic object with the result of [std::max](https://en.cppreference.com/cpp/algorithm/max) with a non-atomic argument and obtains the previous value of the atomic (function template) | 
|  | replaces the atomic object with the result of [std::min](https://en.cppreference.com/cpp/algorithm/min) with a non-atomic argument and obtains the previous value of the atomic (function template) | 
|  | blocks the thread until notified and the atomic value changes (function template) | 
|  | notifies a thread blocked in atomic\_wait (function template) | 
|  | notifies all threads blocked in atomic\_wait (function template) | 
| Flag type and operations |  | 
|  | the lock-free boolean atomic type (class) | 
|  | atomically sets the flag to `true` and returns its previous value (function) | 
|  | atomically sets the value of the flag to `false` (function) | 
|  | atomically returns the value of the flag (function) | 
|  | blocks the thread until notified and the flag changes (function) | 
|  | notifies a thread blocked in atomic\_flag\_wait (function) | 
|  | notifies all threads blocked in atomic\_flag\_wait (function) | 
| Initialization |  | 
|  | non-atomic initialization of a default-constructed atomic object (function template) | 
|  | constant initialization of an atomic variable of static storage duration (function macro) | 
|  | initializes an [std::atomic\_flag](https://en.cppreference.com/cpp/atomic/atomic_flag) to `false` (macro constant) | 
| Memory synchronization ordering |  | 
|  | defines memory ordering constraints for the given atomic operation (enum) | 
|  | removes the specified object from the [std::memory\_order\_consume](https://en.cppreference.com/cpp/atomic/memory_order) dependency tree (function template) | 
|  | generic memory order-dependent fence synchronization primitive (function) | 
|  | fence between a thread and a signal handler executed in the same thread (function) | 
| C compatibility macros (since C++23) |  | 
|  | compatibility macro such that `_Atomic(T)` is identical to `std::atomic<T>` (function macro) | 

Neither the `_Atomic` macro, nor any of the non-macro global namespace declarations are provided by any C++ standard library header other than `<stdatomic.h>`.

### Mutual exclusion

Mutual exclusion algorithms prevent multiple threads from simultaneously accessing shared resources. This prevents data races and provides support for synchronization between threads.

|  | provides basic mutual exclusion facility (class) | 
|  | provides mutual exclusion facility which implements locking with a timeout (class) | 
|  | provides mutual exclusion facility which can be locked recursively by the same thread (class) | 
|  | provides mutual exclusion facility which can be locked recursively by the same thread and implements locking with a timeout (class) | 
|  | provides shared mutual exclusion facility (class) | 
|  | provides shared mutual exclusion facility and implements locking with a timeout (class) | 
| Generic mutex management |  | 
|  | implements a strictly scope-based mutex ownership wrapper (class template) | 
|  | deadlock-avoiding RAII wrapper for multiple mutexes (class template) | 
|  | implements movable mutex ownership wrapper (class template) | 
|  | implements movable shared mutex ownership wrapper (class template) | 
|  | tags used to specify locking strategy (tag) | 
| Generic locking algorithms |  | 
|  | attempts to obtain ownership of mutexes via repeated calls to `try_lock` (function template) | 
|  | locks specified mutexes, blocks if any are unavailable (function template) | 
| Call once |  | 
|  | helper object to ensure that [`call_once`](https://en.cppreference.com/cpp/thread/call_once) invokes the function only once (class) | 
|  | invokes a function only once even if called from multiple threads (function template) | 

### Condition variables

A condition variable is a synchronization primitive that allows multiple threads to communicate with each other. It allows some number of threads to wait (possibly with a timeout) for notification from another thread that they may proceed. A condition variable is always associated with a mutex.

|  | provides a condition variable associated with a [std::unique\_lock](https://en.cppreference.com/cpp/thread/unique_lock) (class) | 
|  | provides a condition variable associated with any lock type (class) | 
|  | schedules a call to `notify_all` to be invoked when this thread is completely finished (function) | 
|  | lists the possible results of timed waits on condition variables (enum) | 


### Semaphores (since C++20)

A semaphore is a lightweight synchronization primitive used to constrain concurrent access to a shared resource. When either would suffice, a semaphore can be more efficient than a condition variable.

|  | semaphore that models a non-negative resource count (class template) | 
|  | semaphore that has only two states (typedef) | 


### Latches and Barriers (since C++20)

Latches and barriers are thread coordination mechanisms that allow any number of threads to block until an expected number of threads arrive. A latch cannot be reused, while a barrier can be used repeatedly.

|  | single-use thread barrier (class) | 
|  | reusable thread barrier (class template) | 

### Futures

The standard library provides facilities to obtain values that are returned and to catch exceptions that are thrown by asynchronous tasks (i.e. functions launched in separate threads). These values are communicated in a *shared state*, in which the asynchronous task may write its return value or store an exception, and which may be examined, waited for, and otherwise manipulated by other threads that hold instances of [std::future](https://en.cppreference.com/cpp/thread/future) or [std::shared\_future](https://en.cppreference.com/cpp/thread/shared_future) that reference that shared state.

|  | stores a value for asynchronous retrieval (class template) | 
|  | packages a function to store its return value for asynchronous retrieval (class template) | 
|  | waits for a value that is set asynchronously (class template) | 
|  | waits for a value (possibly referenced by other futures) that is set asynchronously (class template) | 
|  | runs a function asynchronously (potentially in a new thread) and returns a [std::future](https://en.cppreference.com/cpp/thread/future) that will hold the result (function template) | 
|  | specifies the launch policy for [std::async](https://en.cppreference.com/cpp/thread/async) (enum) | 
|  | specifies the results of timed waits performed on [std::future](https://en.cppreference.com/cpp/thread/future) and [std::shared\_future](https://en.cppreference.com/cpp/thread/shared_future) (enum) | 
| Future errors |  | 
|  | reports an error related to futures or promises (class) | 
|  | identifies the future error category (function) | 
|  | identifies the future error codes (enum) | 


### Safe Reclamation (since C++26)

Safe-reclamation techniques are most frequently used to straightforwardly resolve access-deletion races.

| Read-Copy-Update Mechanism |  | 
|  | allows an object to be protected by RCU (class template) | 
|  | provides regions of RCU protection (class) | 
|  | returns a reference to a static-duration object of type `std::rcu_domain` (function) | 
|  | blocks until a protection region unlocks on a RCU domain (function) | 
|  | may evaluate scheduled operations on a RCU domain and blocks until all preceding evaluations are complete (function) | 
|  | schedules the evaluation of a specified function on a RCU domain, potentially allocating memory, and invoking scheduled evaluations (function template) | 
| Hazard Pointers |  | 
|  | allows an object to be hazard-protectable (class template) | 
|  | single-writer multi-reader pointer that can be owned by at most one thread at any point of time (class) | 
|  | constructs a hazard pointer (function) |