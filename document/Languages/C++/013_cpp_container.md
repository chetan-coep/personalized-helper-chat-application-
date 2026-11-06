---
id: "c++_013"
technology: "C++"
category: "Languages"
title: "Containers library - cppreference.com"
doc_order: 13
source_url: "https://en.cppreference.com/cpp/container"
language: "en"
retrieved_at: "2026-11-03 17:56:04"
content_hash: "e09d049483b2f8aee252bc6f58c3824e1265293e4cf19355253c93fefe0dd03d"
---

# Containers library - cppreference.com

Source: https://en.cppreference.com/cpp/container

---

# Containers library

The Containers library is a generic collection of class templates and algorithms that allow programmers to easily implement common data structures like queues, lists and stacks. There are two(until C++11)three(since C++11) classes of containers:

- sequence containers,
- associative containers,

|  | (since C++11) | 

each of which is designed to support a different set of operations.

The container manages the storage space that is allocated for its elements and provides member functions to access them, either directly or through iterators (objects with properties similar to pointers).

Most containers have at least several member functions in common, and share functionalities. Which container is the best for the particular application depends not only on the offered functionality, but also on its efficiency for different workloads.

### Sequence containers

Sequence containers implement data structures which can be accessed sequentially.

|  | fixed-sized inplace contiguous array (class template) | 
|  | resizable contiguous array (class template) | 
|  | resizable, fixed capacity, inplace contiguous array (class template) | 
|  | collection that reuses erased elements' memory (class template) | 
|  | double-ended queue (class template) | 
|  | singly-linked list (class template) | 
|  | doubly-linked list (class template) | 

### Associative containers

Associative containers implement sorted data structures that can be quickly searched (O(log n) complexity).

|  | collection of unique keys, sorted by keys (class template) | 
|  | collection of key-value pairs, sorted by keys, keys are unique (class template) | 
|  | collection of keys, sorted by keys (class template) | 
|  | collection of key-value pairs, sorted by keys (class template) | 


### Unordered associative containers (since C++11)

Unordered associative containers implement unsorted (hashed) data structures that can be quickly searched (O(1) average, O(n) worst-case complexity).

|  | collection of unique keys, hashed by keys (class template) | 
|  | collection of key-value pairs, hashed by keys, keys are unique (class template) | 
|  | collection of keys, hashed by keys (class template) | 
|  | collection of key-value pairs, hashed by keys (class template) | 

### Container adaptors

Container adaptors provide a different interface for sequential containers.

|  | adapts a container to provide stack (LIFO data structure) (class template) | 
|  | adapts a container to provide queue (FIFO data structure) (class template) | 
|  | adapts a container to provide priority queue (class template) | 
|  | adapts a container to provide a collection of unique keys, sorted by keys (class template) | 
|  | adapts two containers to provide a collection of key-value pairs, sorted by unique keys (class template) | 
|  | adapts a container to provide a collection of keys, sorted by keys (class template) | 
|  | adapts two containers to provide a collection of key-value pairs, sorted by keys (class template) | 


### Views (since C++20)

Views provide flexible facilities for interacting with one- or multi-dimensional views over a non-owning array of elements.

|  | a non-owning view over a contiguous sequence of objects (class template) | 
|  | a multi-dimensional non-owning array view (class template) | 

### Iterator invalidation

Read-only methods never [invalidate](https://en.cppreference.com/cpp/iterator#Dereferceability_and_validity) iterators or references. Methods which modify the contents of a container may invalidate iterators and/or references, as summarized in this table.

| Category | Container | After **insertion**, are... |  | After **erasure**, are... |  | Conditionally | 
|---|---|---|---|---|---|---|
|  |  | **iterators** valid? | **references** valid? | **iterators** valid? | **references** valid? |  | 
| Sequence containers | [`array`](https://en.cppreference.com/cpp/container/array) | N/A |  | N/A |  |  | 
|  | [`vector`](https://en.cppreference.com/cpp/container/vector) | No |  | N/A |  | Insertion changed capacity | 
|  |  | Yes |  | Yes |  | Before modified element(s) (for insertion only if capacity didn't change) | 
|  |  | No |  | No |  | At or after modified element(s) | 
|  | [`deque`](https://en.cppreference.com/cpp/container/deque) | No | Yes | Yes, except erased element(s) |  | Modified first or last element | 
|  |  |  | No | No |  | Modified middle only | 
|  | [`list`](https://en.cppreference.com/cpp/container/list) | Yes |  | Yes, except erased element(s) |  |  | 
|  | [`forward_list`](https://en.cppreference.com/cpp/container/forward_list) | Yes |  | Yes, except erased element(s) |  |  | 
| Associative containers | [`set`](https://en.cppreference.com/cpp/container/set) [`multiset`](https://en.cppreference.com/cpp/container/multiset) [`map`](https://en.cppreference.com/cpp/container/map) [`multimap`](https://en.cppreference.com/cpp/container/multimap) | Yes |  | Yes, except erased element(s) |  |  | 
| Unordered associative containers | [`unordered_set`](https://en.cppreference.com/cpp/container/unordered_set) [`unordered_multiset`](https://en.cppreference.com/cpp/container/unordered_multiset) [`unordered_map`](https://en.cppreference.com/cpp/container/unordered_map) [`unordered_multimap`](https://en.cppreference.com/cpp/container/unordered_multimap) | No | Yes | N/A |  | Insertion caused rehash | 
|  |  | Yes |  | Yes, except erased element(s) |  | No rehash | 

|  | This section is incomplete Reason: add iterator invalidation for C++23 "flat" adaptors (std::flat\_set etc) | 

|  | This section is incomplete Reason: add iterator invalidation for C++26 std::inplace\_vector | 

Here, **insertion** refers to any method which adds one or more elements to the container and **erasure** refers to any method which removes one or more elements from the container.

- Examples of insertion methods are [std::set::insert](https://en.cppreference.com/cpp/container/set/insert), [std::map::emplace](https://en.cppreference.com/cpp/container/map/emplace), [std::vector::push\_back](https://en.cppreference.com/cpp/container/vector/push_back), and [std::deque::push\_front](https://en.cppreference.com/cpp/container/deque/push_front).

|  | (since C++11) | 

- Examples of erasure methods are [std::set::erase](https://en.cppreference.com/cpp/container/set/erase), [std::vector::pop\_back](https://en.cppreference.com/cpp/container/vector/pop_back), [std::deque::pop\_front](https://en.cppreference.com/cpp/container/deque/pop_front), and [std::map::clear](https://en.cppreference.com/cpp/container/map/clear).
  - `clear` invalidates all iterators and references. Because it erases all elements, this technically complies with the rules above.

Unless otherwise specified (either explicitly or by defining a function in terms of other functions), passing a container as an argument to a library function never invalidate iterators to, or change the values of, objects within that container.

The past-the-end iterator deserves particular mention. In general this iterator is invalidated as though it were a normal iterator to a non-erased element. So [std::set::end](https://en.cppreference.com/cpp/container/set/end) is never invalidated, [std::unordered\_set::end](https://en.cppreference.com/cpp/container/unordered_set/end) is invalidated only on rehash(since C++11), [std::vector::end](https://en.cppreference.com/cpp/container/vector/end) is always invalidated (since it is always after the modified elements), and so on.

There is one exception: an erasure which deletes the last element of a [std::deque](https://en.cppreference.com/cpp/container/deque) *does* invalidate the past-the-end iterator, even though it is not an erased element of the container (or an element at all). Combined with the general rules for [std::deque](https://en.cppreference.com/cpp/container/deque) iterators, the net result is that the only modifying operation which does *not* invalidate [std::deque::end](https://en.cppreference.com/cpp/container/deque/end) is an erasure which deletes the first element, but not the last.

| Thread safety | (since C++11) | 

### Function table

Note: [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string) is not treated as a container by the standard but behaves much like one due to its similarity. It is listed as 'Pseudo container' here for convenience.

|  | - functions present in C++03 | 
|  | - functions present since C++11 | 
|  | - functions present since C++17 | 
|  | - functions present since C++20 | 
|  | - functions present since C++23 | 

|  | This section is incomplete Reason: Add C++26 "color" and fill member/non-member function table for std::inplace\_vector | 

#### Member function table

- Note: functions in two different `extract` lines have different meanings and syntax:

#### Non-member function table

| The `<`, `<=`, `>`, `>=`, and `!=` operators are [synthesized](https://en.cppreference.com/cpp/language/operators#Comparison_operators) from `operator<=>` and `operator==` respectively. | [(since C++20)](https://en.cppreference.com/cpp/compiler_support/20#P1185R2) | 

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [LWG 51](https://cplusplus.github.io/LWG/issue51) | C++98 | container iterators might be invalidated by arbitrary library operation | they are only invalidated when specified | 

### See also

C++ named requirements:

|  | numeric arrays, array masks and array slices (class template) | 
|  | stores and manipulates sequences of characters (class template) | 
|  | read-only string view (class template) |