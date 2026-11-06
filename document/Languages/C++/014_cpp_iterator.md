---
id: "c++_014"
technology: "C++"
category: "Languages"
title: "Iterator library - cppreference.com"
doc_order: 14
source_url: "https://en.cppreference.com/cpp/iterator"
language: "en"
retrieved_at: "2026-11-03 17:56:06"
content_hash: "3b949f7e3ba02b10f6e64b432039afa366625c24cf2619a4723454817b95c209"
---

# Iterator library - cppreference.com

Source: https://en.cppreference.com/cpp/iterator

---

# Iterator library

Iterators are a generalization of [pointers](https://en.cppreference.com/cpp/language/pointer) that allow a C++ program to work with different data structures (for example, [containers](https://en.cppreference.com/cpp/container) and [ranges](https://en.cppreference.com/cpp/ranges)(since C++20)) in a uniform manner. The iterator library provides definitions for iterators, as well as iterator traits, adaptors, and utility functions.

Since iterators are an abstraction of pointers, their semantics are a generalization of most of the semantics of pointers in C++. This ensures that every [function template](https://en.cppreference.com/cpp/language/function_template) that takes iterators works as well with regular pointers.

### Iterator categories

There are five(until C++17)six(since C++17) kinds of iterators: [LegacyInputIterator](https://en.cppreference.com/cpp/named_req/InputIterator), [LegacyOutputIterator](https://en.cppreference.com/cpp/named_req/OutputIterator), [LegacyForwardIterator](https://en.cppreference.com/cpp/named_req/ForwardIterator), [LegacyBidirectionalIterator](https://en.cppreference.com/cpp/named_req/BidirectionalIterator), [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator), and [LegacyContiguousIterator](https://en.cppreference.com/cpp/named_req/ContiguousIterator)(since C++17). (See also [LegacyIterator](https://en.cppreference.com/cpp/named_req/Iterator) for the most basic kind of iterator.)

Instead of being defined by specific types, each category of iterator is defined by the operations that can be performed on it. This definition means that any type that supports the necessary operations can be used as an iterator -- for example, a pointer supports all of the operations required by [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator), so a pointer can be used anywhere a [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator) is expected.

All of the iterator categories (except [LegacyOutputIterator](https://en.cppreference.com/cpp/named_req/OutputIterator)) can be organized into a hierarchy, where more powerful iterator categories (e.g. [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator)) support the operations of less powerful categories (e.g. [LegacyInputIterator](https://en.cppreference.com/cpp/named_req/InputIterator)). If an iterator falls into one of these categories and also satisfies the requirements of [LegacyOutputIterator](https://en.cppreference.com/cpp/named_req/OutputIterator), then it is called a *mutable* iterator and supports *both* input and output. Non-mutable iterators are called *constant* iterators.

| Iterators are called *constexpr* iterators if all operations provided to meet iterator category requirements are [constexpr functions](https://en.cppreference.com/cpp/language/constexpr#constexpr_function). | (since C++20) | 

| Iterator category | Operations and storage requirement |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|
|  | write | read | increment |  | decrement | random access | contiguous storage | 
|  |  |  | without multiple passes | with multiple passes |  |  |  | 
| [LegacyIterator](https://en.cppreference.com/cpp/named_req/Iterator) |  |  | Required |  |  |  |  | 
| [LegacyOutputIterator](https://en.cppreference.com/cpp/named_req/OutputIterator) | Required |  | Required |  |  |  |  | 
| [LegacyInputIterator](https://en.cppreference.com/cpp/named_req/InputIterator) (mutable if supports write operation) |  | Required | Required |  |  |  |  | 
| [LegacyForwardIterator](https://en.cppreference.com/cpp/named_req/ForwardIterator) (also satisfies [LegacyInputIterator](https://en.cppreference.com/cpp/named_req/InputIterator)) |  | Required | Required | Required |  |  |  | 
| [LegacyBidirectionalIterator](https://en.cppreference.com/cpp/named_req/BidirectionalIterator) (also satisfies [LegacyForwardIterator](https://en.cppreference.com/cpp/named_req/ForwardIterator)) |  | Required | Required | Required | Required |  |  | 
| [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator) (also satisfies [LegacyBidirectionalIterator](https://en.cppreference.com/cpp/named_req/BidirectionalIterator)) |  | Required | Required | Required | Required | Required |  | 
| [LegacyContiguousIterator](https://en.cppreference.com/cpp/named_req/ContiguousIterator)<sup>[\[1\]](https://en.cppreference.com#cite_note-1)</sup> (also satisfies [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator)) |  | Required | Required | Required | Required | Required | Required | 

1. [↑](https://en.cppreference.com#cite_ref-1) [LegacyContiguousIterator](https://en.cppreference.com/cpp/named_req/ContiguousIterator) category was only formally specified in C++17, but the iterators of [std::vector](https://en.cppreference.com/cpp/container/vector), [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string), [std::array](https://en.cppreference.com/cpp/container/array), and [std::valarray](https://en.cppreference.com/cpp/numeric/valarray), as well as pointers into C arrays are often treated as a separate category in pre-C++17 code.

Note: A type supporting the required operations in a row of the table above does not necessarily fall into the corresponding category, see the category page for the complete list of requirements.

### Definitions

#### Types and writability

An input iterator `i` supports the expression `*i`, resulting in a value of some [object type](https://en.cppreference.com/cpp/language/type) `T`, called the *value type* of the iterator.

An output iterator `i` has a non-empty set of types that are *writable*(until C++20)[`indirectly_writable`](https://en.cppreference.com/cpp/iterator/indirectly_writable)(since C++20) to the iterator; for each such type `T`, the expression `*i = o` is valid where `o` is a value of type `T`.

For every iterator type `X` for which equality is defined(until C++20), there is a corresponding signed [integer](https://en.cppreference.com/cpp/language/types#Signed_and_unsigned_integer_types)(until C++20)[integer-like](https://en.cppreference.com/cpp/iterator/is-integer-like)(since C++20) type called the *difference type* of the iterator.

#### Dereferenceability and validity

Just as a regular pointer to an [array](https://en.cppreference.com/cpp/language/array) guarantees that there is a pointer value pointing past the last element of the array, so for any iterator type there is an iterator value that points past the last element of a corresponding sequence. Such a value is called a *past-the-end* value.

Values of an iterator `i` for which the expression `*i` is defined are called *dereferenceable*. The [standard library](https://en.cppreference.com/cpp/standard_library) never assumes that past-the-end values are dereferenceable.

Iterators can also have *singular* values that are not associated with any sequence. Results of most expressions are undefined for singular values; the only exceptions are

- the assignment of a non-singular value to an iterator that holds a singular value,
- destroying an iterator that holds a singular value, and,
- for iterators that meet the [DefaultConstructible](https://en.cppreference.com/cpp/named_req/DefaultConstructible) requirements, using a [value-initialized](https://en.cppreference.com/cpp/language/value_initialization) iterator as the source of a copy or move(since C++11) operation.

In these cases the singular value is overwritten the same way as any other value. Dereferenceable values are always non-singular.

An *invalid* iterator is an iterator that may be singular.

#### Ranges

Most of the standard library’s algorithmic templates that operate on data structures have interfaces that use ranges.

| An iterator `j` is called *reachable* from an iterator `i` if and only if there is a finite sequence of applications of the expression `++i` that makes `i == j`. If `j` is reachable from `i`, they refer to elements of the same sequence. A *range* is a pair of iterators that designate the beginning and end of the computation. A range `[``i``,` `i``)` is an empty range; in general, a range `[``i``,` `j``)` refers to the elements in the data structure starting with the element pointed to by `i` and up to but not including the element pointed to by `j`. Range `[``i``,` `j``)` is *valid* if and only if `j` is reachable from `i`. | (until C++20) | 
| A *range* can be denoted by either Iterator-sentinel range An iterator and a sentinel denoting a range are comparable. `[``i``,` `s``)` is empty if `i == s`; otherwise, `[``i``,` `s``)` refers to the elements in the data structure starting with the element pointed to by `i` and up to but not including the element, if any, pointed to by the first iterator `j` such that `j == s`. A sentinel `s` is called *reachable* from an iterator `i` if and only if there is a finite sequence of applications of the expression `++i` that makes `i == s`. If `s` is reachable from `i`, `[``i``,` `s``)` denotes a *valid* range. Counted range A *counted range* `i` `+` `[``0``,` `n``)` is empty if `n == 0`; otherwise, `i` `+` `[``0``,` `n``)` refers to the `n` elements in the data structure starting with the element pointed to by `i` and up to but not including the element, if any, pointed to by the result of `n` applications of `++i`. A counted range `i` `+` `[``0``,` `n``)` is *valid* if and only if | (since C++20) | 

The result of the application of functions in the standard library to invalid ranges is undefined.


### Iterator concepts (since C++20)

A new system of iterators based on [concepts](https://en.cppreference.com/cpp/language/constraints) that are different from C++17 iterators. While the basic taxonomy remains similar, the requirements for individual iterator categories are somewhat different.

| Defined in  namespace `std` |  | 
|  | specifies that a type is indirectly readable by applying operator `*` (concept) | 
|  | specifies that a value can be written to an iterator's referenced object (concept) | 
|  | specifies that a [`semiregular`](https://en.cppreference.com/cpp/concepts/semiregular) type can be incremented with pre- and post-increment operators (concept) | 
|  | specifies that the increment operation on a [`weakly_incrementable`](https://en.cppreference.com/cpp/iterator/weakly_incrementable) type is [equality-preserving](https://en.cppreference.com/cpp/concepts#Equality_preservation) and that the type is [`equality_comparable`](https://en.cppreference.com/cpp/concepts/equality_comparable) (concept) | 
|  | specifies that a type behaves as a (signed) integer type (exposition-only concept\*) | 
|  | specifies that objects of a type can be incremented and dereferenced (concept) | 
|  | specifies a type is a sentinel for an [`input_or_output_iterator`](https://en.cppreference.com/cpp/iterator/input_or_output_iterator) type (concept) | 
|  | specifies that the `-` operator can be applied to an iterator and a sentinel to calculate their difference in constant time (concept) | 
|  | specifies that a type is an input iterator, that is, its referenced values can be read and it can be both pre- and post-incremented (concept) | 
|  | specifies that a type is an output iterator for a given value type, that is, values of that type can be written to it and it can be both pre- and post-incremented (concept) | 
|  | specifies that an [`input_iterator`](https://en.cppreference.com/cpp/iterator/input_iterator) is a forward iterator, supporting equality comparison and multi-pass (concept) | 
|  | specifies that a [`forward_iterator`](https://en.cppreference.com/cpp/iterator/forward_iterator) is a bidirectional iterator, supporting movement backwards (concept) | 
|  | specifies that a [`bidirectional_iterator`](https://en.cppreference.com/cpp/iterator/bidirectional_iterator) is a random-access iterator, supporting advancement in constant time and subscripting (concept) | 
|  | specifies that a [`random_access_iterator`](https://en.cppreference.com/cpp/iterator/random_access_iterator) is a contiguous iterator, referring to elements that are contiguous in memory (concept) | 


### Iterator associated types (since C++20)

| Defined in  namespace `std` |  | 
|  | computes the difference type of a [`weakly_incrementable`](https://en.cppreference.com/cpp/iterator/weakly_incrementable) type (class template) | 
|  | computes the value type of an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type (class template) | 
|  | computes the associated types of an iterator (alias template) | 

### Iterator primitives

|  | provides uniform interface to the properties of an iterator (class template) | 
|  | empty class types used to indicate iterator categories (class) | 
|  | base class to ease the definition of required types for simple iterators (class template) | 


### Iterator customization points (since C++20)

| Defined in  namespace `std::ranges` |  | 
|  | casts the result of dereferencing an object to its associated rvalue reference type (customization point object) | 
|  | swaps the values referenced by two dereferenceable objects (customization point object) | 


### Algorithm concepts and utilities (since C++20)

A set of concepts and related utility templates designed to ease constraining common algorithm operations.

| Defined in  namespace `std` |  | 
| Indirect callable concepts |  | 
|  | specifies that a callable type can be invoked with the result of dereferencing an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type (concept) | 
|  | specifies that a callable type, when invoked with the result of dereferencing an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type, satisfies [`predicate`](https://en.cppreference.com/cpp/concepts/predicate) (concept) | 
|  | specifies that a callable type, when invoked with the result of dereferencing two [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) types, satisfies [`predicate`](https://en.cppreference.com/cpp/concepts/predicate) (concept) | 
|  | specifies that a callable type, when invoked with the result of dereferencing two [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) types, satisfies [`equivalence_relation`](https://en.cppreference.com/cpp/concepts/equivalence_relation) (concept) | 
|  | specifies that a callable type, when invoked with the result of dereferencing two [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) types, satisfies [`strict_weak_order`](https://en.cppreference.com/cpp/concepts/strict_weak_order) (concept) | 
| Common algorithm requirements |  | 
|  | specifies that values may be moved from an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type to an [`indirectly_writable`](https://en.cppreference.com/cpp/iterator/indirectly_writable) type (concept) | 
|  | specifies that values may be moved from an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type to an [`indirectly_writable`](https://en.cppreference.com/cpp/iterator/indirectly_writable) type and that the move may be performed via an intermediate object (concept) | 
|  | specifies that values may be copied from an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type to an [`indirectly_writable`](https://en.cppreference.com/cpp/iterator/indirectly_writable) type (concept) | 
|  | specifies that values may be copied from an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type to an [`indirectly_writable`](https://en.cppreference.com/cpp/iterator/indirectly_writable) type and that the copy may be performed via an intermediate object (concept) | 
|  | specifies that the values referenced by two [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) types can be swapped (concept) | 
|  | specifies that the values referenced by two [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) types can be compared (concept) | 
|  | specifies the common requirements of algorithms that reorder elements in place (concept) | 
|  | specifies the requirements of algorithms that merge sorted sequences into an output sequence by copying elements (concept) | 
|  | specifies the common requirements of algorithms that permute sequences into ordered sequences (concept) | 
| Utilities |  | 
|  | computes the result of invoking a callable object on the result of dereferencing some set of [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) types (alias template) | 
|  | helper template for specifying the constraints on algorithms that accept projections (class template) | 
|  | computes the value type of an [`indirectly_readable`](https://en.cppreference.com/cpp/iterator/indirectly_readable) type by projection (alias template) | 

### Iterator adaptors

|  | iterator adaptor for reverse-order traversal (class template) | 
|  | creates a [std::reverse\_iterator](https://en.cppreference.com/cpp/iterator/reverse_iterator) of type inferred from the argument (function template) | 
|  | iterator adaptor for insertion at the end of a container (class template) | 
|  | creates a [std::back\_insert\_iterator](https://en.cppreference.com/cpp/iterator/back_insert_iterator) of type inferred from the argument (function template) | 
|  | iterator adaptor for insertion at the front of a container (class template) | 
|  | creates a [std::front\_insert\_iterator](https://en.cppreference.com/cpp/iterator/front_insert_iterator) of type inferred from the argument (function template) | 
|  | iterator adaptor for insertion into a container (class template) | 
|  | creates a [std::insert\_iterator](https://en.cppreference.com/cpp/iterator/insert_iterator) of type inferred from the argument (function template) | 
|  | iterator adaptor that converts an iterator into a constant iterator (class template) | 
|  | computes a constant iterator type for a given type (alias template) | 
|  | computes a sentinel type to be used with constant iterators (alias template) | 
|  | creates a std::const\_iterator of type inferred from the argument (function template) | 
|  | creates a std::const\_sentinel of type inferred from the argument (function template) | 
|  | iterator adaptor which dereferences to an rvalue (class template) | 
|  | sentinel adaptor for [std::move\_iterator](https://en.cppreference.com/cpp/iterator/move_iterator) (class template) | 
|  | creates a [std::move\_iterator](https://en.cppreference.com/cpp/iterator/move_iterator) of type inferred from the argument (function template) | 
|  | adapts an iterator type and its sentinel into a common iterator type (class template) | 
|  | default sentinel for use with iterators that know the bound of their range (class) | 
|  | iterator adaptor that tracks the distance to the end of the range (class template) | 
|  | sentinel that always compares unequal to any [`weakly_incrementable`](https://en.cppreference.com/cpp/iterator/weakly_incrementable) type (class) | 

### Stream iterators

|  | input iterator that reads from [std::basic\_istream](https://en.cppreference.com/cpp/io/basic_istream) (class template) | 
|  | output iterator that writes to [std::basic\_ostream](https://en.cppreference.com/cpp/io/basic_ostream) (class template) | 
|  | input iterator that reads from [std::basic\_streambuf](https://en.cppreference.com/cpp/io/basic_streambuf) (class template) | 
|  | output iterator that writes to [std::basic\_streambuf](https://en.cppreference.com/cpp/io/basic_streambuf) (class template) | 

### Iterator operations

|  | advances an iterator by given distance (function template) | 
|  | returns the distance between two iterators (function template) | 
|  | increment an iterator (function template) | 
|  | decrement an iterator (function template) | 
|  | advances an iterator by given distance or to a given bound (algorithm function object) | 
|  | returns the distance between an iterator and a sentinel, or between the beginning and end of a range (algorithm function object) | 
|  | increment an iterator by a given distance or to a bound (algorithm function object) | 
|  | decrement an iterator by a given distance or to a bound (algorithm function object) | 


### Range access (since C++11)

These non-member function templates provide a generic interface for containers, plain arrays, and [std::initializer\_list](https://en.cppreference.com/cpp/utility/initializer_list).

|  |  | (since C++23) | 
|  |  | (since C++23) | 
|  |  | (since C++26) | 
|  |  | (since C++26) | 
|  |  | (since C++26) | 
|  |  | (since C++20) | 
|  |  | (since C++23) | 
|  |  | (since C++17) | 

| Defined in  namespace `std` |  | 
|  | returns an iterator to the beginning of a container or array (function template) | 
|  | returns an iterator to the end of a container or array (function template) | 
|  | returns a reverse iterator to the beginning of a container or array (function template) | 
|  | returns a reverse end iterator for a container or array (function template) | 
|  | returns the size of a container or array (function template) | 
|  | checks whether the container is empty (function template) | 
|  | obtains the pointer to the underlying array (function template) | 

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [CWG 1181](https://cplusplus.github.io/CWG/issues/1181.html) | C++98 | array types could not be value types | they can | 
| [LWG 208](https://cplusplus.github.io/LWG/issue208) | C++98 | past-the-end iterators were always non-singular | they can be singular | 
| [LWG 278](https://cplusplus.github.io/LWG/issue278) | C++98 | the validity of an iterator was not defined | defined to be always non-singular | 
| [LWG 324](https://cplusplus.github.io/LWG/issue324) | C++98 | output iterators had value types | output iterators have writable types instead | 
| [LWG 407](https://cplusplus.github.io/LWG/issue407) | C++98 | singular iterators could not be destroyed | allowed | 
| [LWG 408](https://cplusplus.github.io/LWG/issue408) ( [N3066](https://wg21.link/N3066)) | C++98 | singular iterators could not be copied | allowed if they are value-initialized | 
| [LWG 1185](https://cplusplus.github.io/LWG/issue1185) ( [N3066](https://wg21.link/N3066)) | C++98 | [LegacyForwardIterator](https://en.cppreference.com/cpp/named_req/ForwardIterator), [LegacyBidirectionalIterator](https://en.cppreference.com/cpp/named_req/BidirectionalIterator) and [LegacyRandomAccessIterator](https://en.cppreference.com/cpp/named_req/RandomAccessIterator) always satisfy [LegacyOutputIterator](https://en.cppreference.com/cpp/named_req/OutputIterator) | they might not satisfy [LegacyOutputIterator](https://en.cppreference.com/cpp/named_req/OutputIterator) | 
| [LWG 1210](https://cplusplus.github.io/LWG/issue1210) ( [N3066](https://wg21.link/N3066)) | C++98 | the definition of iterator singularity and reachability depended on containers | depend on sequences instead | 
| [LWG 3009](https://cplusplus.github.io/LWG/issue3009) | C++17 | [`<string_view>`](https://en.cppreference.com/cpp/header/string_view) did not provide the range access function templates | provides these templates | 
| [LWG 3987](https://cplusplus.github.io/LWG/issue3987) | C++23 | [`<flat_map>`](https://en.cppreference.com/cpp/header/flat_map) and [`<flat_set>`](https://en.cppreference.com/cpp/header/flat_set) did not provide the range access function templates | provides these templates |