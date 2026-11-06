---
id: "c++_015"
technology: "C++"
category: "Languages"
title: "Ranges library (since C++20) - cppreference.com"
doc_order: 15
source_url: "https://en.cppreference.com/cpp/ranges"
language: "en"
retrieved_at: "2026-11-03 17:56:09"
content_hash: "3e38859c8fad1e6f364f695dd8994dc600ebacc01910dab40abd00e00bd2e1b1"
---

# Ranges library (since C++20) - cppreference.com

Source: https://en.cppreference.com/cpp/ranges

---

# Ranges library (since C++20)

The ranges library is an extension and generalization of the algorithms and iterator libraries that makes them more powerful by making them composable and less error-prone.

The library creates and manipulates range *views*, lightweight objects that indirectly represent iterable sequences (*ranges*). Ranges are an abstraction on top of

- `[`begin`,` end`)` – iterator pairs, e.g. ranges made by implicit conversion from containers. All algorithms that take iterator pairs now have overloads that accept ranges (e.g. [`ranges::sort`](https://en.cppreference.com/cpp/algorithm/ranges/sort))
- begin `+` `[``0``,` size`)` – counted sequences, e.g. range returned by [`views::counted`](https://en.cppreference.com/cpp/ranges/view_counted)
- `[`begin`,` *predicate*`)` – conditionally-terminated sequences, e.g. range returned by [`views::take_while`](https://en.cppreference.com/cpp/ranges/take_while_view)
- `[`begin`,` ..`)` – unbounded sequences, e.g. range returned by [`views::iota`](https://en.cppreference.com/cpp/ranges/iota_view)

The ranges library includes [range algorithms](https://en.cppreference.com/cpp/algorithm/ranges), which are applied to ranges eagerly, and [range adaptors](https://en.cppreference.com#Range_adaptors), which are applied to views lazily. Adaptors can be composed into pipelines, so that their actions take place as the view is iterated.

| ``` namespace std {     namespace views = ranges::views; }  ```  |  | (since C++20) | 

The namespace alias `std::views` is provided as a shorthand for `std::ranges::views`.

| Defined in  namespace `std::ranges` |  | 
| Range access |  | 
|  | returns an iterator to the beginning of a range (customization point object) | 
|  | returns a sentinel indicating the end of a range (customization point object) | 
|  | returns an iterator to the beginning of a read-only range (customization point object) | 
|  | returns a sentinel indicating the end of a read-only range (customization point object) | 
|  | returns a reverse iterator to a range (customization point object) | 
|  | returns a reverse end iterator to a range (customization point object) | 
|  | returns a reverse iterator to a read-only range (customization point object) | 
|  | returns a reverse end iterator to a read-only range (customization point object) | 
|  | returns an integer equal to the reserve hint given by a range (customization point object) | 
|  | returns an integer equal to the size of a range (customization point object) | 
|  | returns a signed integer equal to the size of a range (customization point object) | 
|  | checks whether a range is empty (customization point object) | 
|  | obtains a pointer to the beginning of a contiguous range (customization point object) | 
|  | obtains a pointer to the beginning of a read-only contiguous range (customization point object) | 
| Range primitives |  | 
|  | obtains iterator and sentinel types of a range (alias template) | 
|  | obtains size, difference, and value types of a range (alias template) | 
|  | obtains reference types of a range (alias template) | 
| Dangling iterator handling |  | 
|  | a placeholder type indicating that an iterator or a `subrange` should not be returned since it would be dangling (class) | 
|  | obtains iterator type or `subrange` type of a [`borrowed_range`](https://en.cppreference.com/cpp/ranges/borrowed_range) (alias template) | 
| Other utilities |  | 
|  | tags a range to be treated as a sequence rather than a single value (class template) | 
| Range concepts |  | 
|  | specifies that a type is a range, that is, it provides a `begin` iterator and an `end` sentinel (concept) | 
|  | specifies that a type is a [`range`](https://en.cppreference.com/cpp/ranges/range) and iterators obtained from an expression of it can be safely returned without danger of dangling (concept) | 
|  | specifies that a range can estimate its size in constant time (concept) | 
|  | specifies that a range knows its size in constant time (concept) | 
|  | specifies that a range is a view, that is, it has constant time copy/move/assignment (concept) | 
|  | specifies a range whose iterator type satisfies [`input_iterator`](https://en.cppreference.com/cpp/iterator/input_iterator) (concept) | 
|  | specifies a range whose iterator type satisfies [`output_iterator`](https://en.cppreference.com/cpp/iterator/output_iterator) (concept) | 
|  | specifies a range whose iterator type satisfies [`forward_iterator`](https://en.cppreference.com/cpp/iterator/forward_iterator) (concept) | 
|  | specifies a range whose iterator type satisfies [`bidirectional_iterator`](https://en.cppreference.com/cpp/iterator/bidirectional_iterator) (concept) | 
|  | specifies a range whose iterator type satisfies [`random_access_iterator`](https://en.cppreference.com/cpp/iterator/random_access_iterator) (concept) | 
|  | specifies a range whose iterator type satisfies [`contiguous_iterator`](https://en.cppreference.com/cpp/iterator/contiguous_iterator) (concept) | 
|  | specifies that a range has identical iterator and sentinel types (concept) | 
|  | specifies the requirements for a [`range`](https://en.cppreference.com/cpp/ranges/range) to be safely convertible to a [`view`](https://en.cppreference.com/cpp/ranges/view) (concept) | 
|  | specifies that a range has read-only elements (concept) | 
|  | specifies that a range knows its size in constant time and allows random access to its elements (exposition-only concept\*) | 
| Range conversions |  | 
|  | constructs a new non-view object from an input range (function template) | 
| Views |  | 
|  | helper class template for defining a [`view`](https://en.cppreference.com/cpp/ranges/view), using the [curiously recurring template pattern](https://en.cppreference.com/cpp/language/crtp) (class template) | 
|  | combines an iterator-sentinel pair into a [`view`](https://en.cppreference.com/cpp/ranges/view) (class template) | 

### Range factories

| Defined in  namespace `std::ranges` |  | 
|  | an empty [`view`](https://en.cppreference.com/cpp/ranges/view) with no elements (class template) (variable template) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that contains a single element of a specified value (class template) (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of a sequence generated by repeatedly incrementing an initial value (class template) (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that generates a sequence of increasing values from `0` up to `n` (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of a generated sequence by repeatedly producing the same value (class template) (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of the elements obtained by successive application of `operator>>` on the associated input stream (class template) (customization point object) | 

### Range adaptors

| Defined in  namespace `std::ranges` |  | 
|  | helper base class template for defining a range adaptor closure object (class template) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that includes all elements of a [`range`](https://en.cppreference.com/cpp/ranges/range) (alias template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) of the elements of some other [`range`](https://en.cppreference.com/cpp/ranges/range) (class template) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) with unique ownership of some [`range`](https://en.cppreference.com/cpp/ranges/range) (class template) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) of a sequence that casts each element to an rvalue (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that consists of the elements of a [`range`](https://en.cppreference.com/cpp/ranges/range) that satisfy a predicate (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) of a sequence that applies a transformation function to each element (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of the first N elements of another [`view`](https://en.cppreference.com/cpp/ranges/view) (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of the initial elements of another [`view`](https://en.cppreference.com/cpp/ranges/view), until the first element on which a predicate returns `false` (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of elements of another [`view`](https://en.cppreference.com/cpp/ranges/view), skipping the first N elements (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of the elements of another [`view`](https://en.cppreference.com/cpp/ranges/view), skipping the initial subsequence of elements until the first element where the predicate returns `false` (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of the sequence obtained from flattening a [`view`](https://en.cppreference.com/cpp/ranges/view) of [`range`s](https://en.cppreference.com/cpp/ranges/range) (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of the sequence obtained from flattening a view of ranges, with the delimiter in between elements (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) over the subranges obtained from splitting another [`view`](https://en.cppreference.com/cpp/ranges/view) using a delimiter (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) over the subranges obtained from splitting another [`view`](https://en.cppreference.com/cpp/ranges/view) using a delimiter (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of concatenation of the adapted views (class template) (customization point object) | 
|  | creates a subrange from an iterator and a count (customization point object) | 
|  | converts a [`view`](https://en.cppreference.com/cpp/ranges/view) into a [`common_range`](https://en.cppreference.com/cpp/ranges/common_range) (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that iterates over the elements of another bidirectional view in reverse order (class template) (range adaptor object) | 
|  | converts a [`view`](https://en.cppreference.com/cpp/ranges/view) into a [`constant_range`](https://en.cppreference.com/cpp/ranges/constant_range) (class template) (range adaptor object) | 
|  | takes a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of [`*tuple-like*`](https://en.cppreference.com/cpp/utility/tuple/tuple-like) values and a number N and produces a [`view`](https://en.cppreference.com/cpp/ranges/view) of N<sup>th</sup> element of each tuple (class template) (range adaptor object) | 
|  | takes a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of pair-like values and produces a [`view`](https://en.cppreference.com/cpp/ranges/view) of the first elements of each pair (class template) (range adaptor object) | 
|  | takes a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of pair-like values and produces a [`view`](https://en.cppreference.com/cpp/ranges/view) of the second elements of each pair (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that maps each element of adapted sequence to a tuple of both the element's position and its value (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of tuples of references to corresponding elements of the adapted views (class template) (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of results of application of a transformation function to corresponding elements of the adapted views (class template) (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of tuples of references to adjacent elements of the adapted view (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of pairs of references to adjacent elements of the adapted view (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of results of application of a transformation function to adjacent elements of the adapted view (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of results of application of a transformation function to each pair of adjacent elements of the adapted view (customization point object) | 
|  | a range of [`view`s](https://en.cppreference.com/cpp/ranges/view) that are `N`-sized non-overlapping successive chunks of the elements of another [`view`](https://en.cppreference.com/cpp/ranges/view) (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) whose M<sup>th</sup> element is a [`view`](https://en.cppreference.com/cpp/ranges/view) over the M<sup>th</sup> through (M + N - 1)<sup>th</sup> elements of another [`view`](https://en.cppreference.com/cpp/ranges/view) (class template) (range adaptor object) | 
|  | splits the [`view`](https://en.cppreference.com/cpp/ranges/view) into subranges between each pair of adjacent elements for which the given predicate returns `false` (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of elements of another [`view`](https://en.cppreference.com/cpp/ranges/view), advancing over N elements at a time (class template) (range adaptor object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) consisting of tuples of results calculated by the n-ary cartesian product of the adapted views (class template) (customization point object) | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that caches the last-accessed element of its underlying sequence (class template) (range adaptor object) | 
|  | converts a [`view`](https://en.cppreference.com/cpp/ranges/view) into a range that is [`input_range`](https://en.cppreference.com/cpp/ranges/input_range)-only and non-[`common_range`](https://en.cppreference.com/cpp/ranges/common_range) (class template) (range adaptor object) | 


### Range generators (since C++23)

| Defined in  namespace `std` |  | 
|  | a [`view`](https://en.cppreference.com/cpp/ranges/view) that represents synchronous [coroutine](https://en.cppreference.com/cpp/language/coroutines) generator (class template) | 

### Helper items

#### Range adaptor objects

See [RangeAdaptorObject](https://en.cppreference.com/cpp/named_req/RangeAdaptorObject) (RAO).

#### Range adaptor closure objects

See [RangeAdaptorClosureObject](https://en.cppreference.com/cpp/named_req/RangeAdaptorClosureObject) (RACO).

#### Customization point objects

See [Customization point object](https://en.cppreference.com/cpp/ranges/cpo) (CPO).

#### Assignable wrapper

Some range adaptors wrap their elements or function objects with the (until C++23)(since C++23). The wrapper augments the wrapped object with assignability when needed.

#### Non-propagating cache

Some range adaptors are specified in terms of an exposition-only class template , which behaves almost like `std::optional<T>` (see description for differences).

#### Conditionally-`const` type

| ``` template< bool Const, class T > using /*maybe-const*/ = std::conditional_t<Const, const T, T>;  ```  |  | (exposition only\*) | 

The alias template `/*maybe-const*/` is a shorthand used to conditionally apply a `const` qualifier to the type `T`.

#### Integer-like type helper templates

| ``` template< /*is-integer-like*/ T > using /*make-signed-like-t*/<T> = /* see description */;  ```  | (1) | (exposition only\*) | 
| ``` template< /*is-integer-like*/ T > using /*make-unsigned-like-t*/<T> = /* see description */;  ```  | (2) | (exposition only\*) | 
| ``` template< /*is-integer-like*/ T > /*make-unsigned-like-t*/<T> /*to-unsigned-like*/( T t ) {     return static_cast</*make-unsigned-like-t*/<T>>(t); }  ```  | (3) | (exposition only\*) | 

[integer-like type](https://en.cppreference.com/cpp/iterator/is-integer-like)

`T`:
- If `T` is an integer type, `/*make-signed-like-t*/<T>` is `std::make_signed_t<T>`.
- Otherwise, `/*make-signed-like-t*/<T>` is a corresponding unspecified signed-integer-like type of the same width as `T`.

`T`:
- If `T` is an integer type, `/*make-unsigned-like-t*/<T>` is `std::make_unsigned_t<T>`.
- Otherwise, `/*make-signed-like-t*/<T>` is a corresponding unspecified unsigned-integer-like type of the same width as `T`.

`t` to `/*make-unsigned-like-t*/<T>`.
#### Customization point object helpers

| ``` template< ranges::input_range R > constexpr auto& /*possibly-const-range*/(R& r) noexcept {     if constexpr (ranges::input_range<const R>)         return const_cast<const R&>(r);     else         return r; }  ```  | (1) | (exposition only\*) | 
| ``` template< class T > constexpr auto /*as-const-pointer*/( const T* p ) noexcept {     return p; }  ```  | (2) | (exposition only\*) | 

Some range access customization point objects are specified in terms of these exposition-only function templates.

`/*possibly-const-range*/` returns the const-qualified version of `r` if `const R` models [`input_range`](https://en.cppreference.com/cpp/ranges/input_range); otherwise, returns

`r` without any casting.`/*as-const-pointer*/` returns a pointer to object of constant type.
#### Range adaptor helpers

| ``` template< class F, class Tuple > constexpr auto /*tuple-transform*/( F&& f, Tuple&& tuple ) {     return std::apply([&]<class... Ts>(Ts&&... args)     {         return std::tuple<std::invoke_result_t<F&, Ts>...>             (std::invoke(f, std::forward<Ts>(args))...);     }, std::forward<Tuple>(tuple)); }  ```  | (1) | (exposition only\*) | 
| ``` template< class F, class Tuple > constexpr void /*tuple-for-each*/( F&& f, Tuple&& tuple ) {     std::apply([&]<class... Ts>(Ts&&... args)     {         (static_cast<void>(std::invoke(f, std::forward<Ts>(args))), ...);     }, std::forward<Tuple>(tuple)); }  ```  | (2) | (exposition only\*) | 
| ``` template< class T > constexpr T& /*as-lvalue*/( T&& t ) {     return static_cast<T&>(t); }  ```  | (3) | (exposition only\*) | 

Some range adaptors are specified in terms of these exposition-only function templates.

`/*tuple-transform*/` returns a new tuple constructed by applying `f` to each element of `tuple`.`/*tuple-for-each*/` applies `f` to each element of `tuple` and returns nothing.`/*as-lvalue*/` forwards rvalue `t` as lvalue.
#### Helper concepts

Following exposition-only concepts are used for several types, but they are not parts of the interface of standard library.

| ``` template< class R > concept /*simple-view*/ =     ranges::view<R> && ranges::range<const R> &&     std::same_as<ranges::iterator_t<R>, ranges::iterator_t<const R>> &&     std::same_as<ranges::sentinel_t<R>, ranges::sentinel_t<const R>>;  ```  | (1) | (exposition only\*) | 
| ``` template< class I > concept /*has-arrow*/ =     ranges::input_iterator<I> &&     (std::is_pointer_v<I> \|\| requires(const I i) { i.operator->(); });  ```  | (2) | (exposition only\*) | 
| ``` template< class T, class U > concept /*different-from*/ =     !std::same_as<std::remove_cvref_t<T>, std::remove_cvref_t<U>>;  ```  | (3) | (exposition only\*) | 
| ``` template< class R > concept /*range-with-movable-references*/ =     ranges::input_range<R> &&     std::move_constructible<ranges::range_reference_t<R>> &&     std::move_constructible<ranges::range_rvalue_reference_t<R>>;  ```  | (4) | (exposition only\*) | 
| ``` template< bool C, class... Views > concept /*all-random-access*/ =     (ranges::random_access_range          <std::conditional_t<C, const Views, Views>> && ...);  ```  | (5) | (exposition only\*) | 
| ``` template< bool C, class... Views > concept /*all-bidirectional*/ =     (ranges::bidirectional_range          <std::conditional_t<C, const Views, Views>> && ...);  ```  | (6) | (exposition only\*) | 
| ``` template< bool C, class... Views > concept /*all-forward*/ =     (ranges::forward_range          <std::conditional_t<C, const Views, Views>> && ...);  ```  | (7) | (exposition only\*) | 

### Notes

| [Feature-test](https://en.cppreference.com/cpp/utility/feature_test) macro | Value | Std | Feature | 
|---|---|---|---|
| [`__cpp_lib_generator`](https://en.cppreference.com/cpp/feature_test#cpp_lib_generator) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_generator_202207L) | (C++23) | `std::generator` – synchronous coroutine generator for ranges | 
| [`__cpp_lib_ranges`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges) | [`201911L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_ranges_201911L) | (C++20) | Ranges library and [constrained algorithms](https://en.cppreference.com/cpp/algorithm/ranges) | 
|  | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202106L) | (C++23) (DR20) | Non- [default-initializable](https://en.cppreference.com/cpp/concepts/default_initializable) [views](https://en.cppreference.com/cpp/ranges/view) | 
|  | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202110L) | (C++23) (DR20) | [Views](https://en.cppreference.com/cpp/ranges/view) with [ownership](https://en.cppreference.com/cpp/ranges/owning_view) | 
|  | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202202L) | (C++23) | `ranges::range_adaptor_closure` | 
|  | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202207L) | (C++23) | Relaxing [range adaptors](https://en.cppreference.com#Range_adaptors) to allow for move-only types | 
|  | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202211L) | (C++23) | Removing "poison pills" [(P2602)](https://wg21.link/p2602) overloads in `ranges::begin` etc | 
|  | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202302L) | (C++23) | Relaxing ranges to allow certain projections | 
|  | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_202406L) | (C++26) (DR20) | Removing the common reference requirement from the indirectly invocable concepts | 
| [`__cpp_lib_ranges_as_const`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_as_const) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_as_const_202207L) | (C++23) | `std::const_iterator`, `ranges::as_const_view` | 
| [`__cpp_lib_ranges_as_rvalue`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_as_rvalue) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_as_rvalue_202207L) | (C++23) | `ranges::as_rvalue_view` | 
| [`__cpp_lib_ranges_cache_latest`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_cache_latest) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_cache_latest_202411L) | (C++26) | `ranges::cache_latest_view` | 
| [`__cpp_lib_ranges_cartesian_product`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_cartesian_product) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_cartesian_product_202207L) | (C++23) | `ranges::cartesian_product_view` | 
| [`__cpp_lib_ranges_chunk`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_chunk) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_chunk_202202L) | (C++23) | `ranges::chunk_view` | 
| [`__cpp_lib_ranges_chunk_by`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_chunk_by) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_chunk_by_202202L) | (C++23) | `ranges::chunk_by_view` | 
| [`__cpp_lib_ranges_concat`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_concat) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_concat_202403L) | (C++26) | `ranges::concat_view` | 
| [`__cpp_lib_ranges_enumerate`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_enumerate) | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_enumerate_202302L) | (C++23) | `ranges::enumerate_view` | 
| [`__cpp_lib_ranges_indices`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_indices) | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_indices_202506L) | (C++26) | `ranges::views::indices` | 
| [`__cpp_lib_ranges_join_with`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_join_with) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_join_with_202202L) | (C++23) | `ranges::join_with_view` | 
| [`__cpp_lib_ranges_repeat`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_repeat) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_repeat_202207L) | (C++23) | `ranges::repeat_view` | 
| [`__cpp_lib_ranges_reserve_hint`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_reserve_hint) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_reserve_hint_202502L) | (C++26) | `ranges::reserve_hint` and `ranges::approximately_sized_range` | 
| [`__cpp_lib_ranges_slide`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_slide) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_slide_202202L) | (C++23) | `ranges::slide_view` | 
| [`__cpp_lib_ranges_stride`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_stride) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_stride_202207L) | (C++23) | `ranges::stride_view` | 
| [`__cpp_lib_ranges_to_container`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_to_container) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_to_container_202202L) | (C++23) | `ranges::to` | 
| [`__cpp_lib_ranges_as_input`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_as_input) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_as_input_202502L) | (C++26) | `ranges::as_input_view` | 
| [`__cpp_lib_ranges_zip`](https://en.cppreference.com/cpp/feature_test#cpp_lib_ranges_zip) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_zip_202110L) | (C++23) | `ranges::zip_view`, `ranges::zip_transform_view`, `ranges::adjacent_view`, `ranges::adjacent_transform_view` | 

### Example

```
#include <iostream>
#include <ranges>
int main()
{
    auto const ints = {0, 1, 2, 3, 4, 5};
    auto even = [](int i) { return 0 == i % 2; };
    auto square = [](int i) { return i * i; };
    
    // the "pipe" syntax of composing the views:
    for (int i : ints | std::views::filter(even) | std::views::transform(square))
        std::cout << i << ' ';
    
    std::cout << '\n';
    
    // a traditional "functional" composing syntax:
    for (int i : std::views::transform(std::views::filter(ints, even), square))
        std::cout << i << ' ';
}
```
Output:

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [LWG 3509](https://cplusplus.github.io/LWG/issue3509) ( [P2281R1](https://wg21.link/P2281R1)) | C++20 | it was unclear how range adaptor objects bound trailing arguments | they are bound by value | 
| [LWG 3948](https://cplusplus.github.io/LWG/issue3948) | C++23 | *possibly-const-range* and *as-const-pointer* were not declared `noexcept` | declared `noexcept` | 
| [LWG 4027](https://cplusplus.github.io/LWG/issue4027) | C++23 | *possibly-const-range* would not add const-qualification for ranges that has already modeled [`constant_range`](https://en.cppreference.com/cpp/ranges/constant_range) | adds const-qualification for such ranges | 
| [LWG 4112](https://cplusplus.github.io/LWG/issue4112) | C++20 | *has-arrow* did not require `i` to be const-qualified | requires |