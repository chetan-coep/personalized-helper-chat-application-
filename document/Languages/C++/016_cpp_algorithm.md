---
id: "c++_016"
technology: "C++"
category: "Languages"
title: "Algorithms library - cppreference.com"
doc_order: 16
source_url: "https://en.cppreference.com/cpp/algorithm"
language: "en"
retrieved_at: "2026-11-03 17:56:12"
content_hash: "e735800f3f5db98c966880e3eeb10c8749445574e39e2f0f2dab5f40b1652d48"
---

# Algorithms library - cppreference.com

Source: https://en.cppreference.com/cpp/algorithm

---

# Algorithms library

The algorithms library defines functions for a variety of purposes (e.g., searching, sorting, counting, manipulating) that operate on [ranges](https://en.cppreference.com/cpp/iterator#Ranges) of elements.


C++20 provides [constrained](https://en.cppreference.com/cpp/language/constraints) versions of most algorithms in the namespace `std::ranges`. In these algorithms, a range can be specified as either an [iterator](https://en.cppreference.com/cpp/iterator/input_or_output_iterator)-[sentinel](https://en.cppreference.com/cpp/iterator/sentinel_for) pair or as a single [`range`](https://en.cppreference.com/cpp/ranges/range) argument, and projections and pointer-to-member callables are supported. Additionally, the [return types](https://en.cppreference.com/cpp/algorithm/ranges#Return_types) of most algorithms have been changed to return all potentially useful information computed during the execution of the algorithm.

```
std::vector<int> v{7, 1, 4, 0, -1};
std::ranges::sort(v); // constrained algorithm
```

### Parallel algorithms [(since C++17)](https://en.cppreference.com/cpp/compiler_support/17#P0024R2)

A *parallel algorithm* is a function template in the algorithms library with a template parameter named `ExecutionPolicy` or constrained by  [(since C++26)](https://en.cppreference.com/cpp/compiler_support/26#P3179R9). Such a template parameter is termed an *execution policy template parameter* , it describes the manner in which the execution of a parallel algorithm may be parallelized.

Unless otherwise stated, parallel algorithms are allowed to make arbitrary copies of elements from ranges, as long as both `std::is_trivially_copy_constructible_v<T>` and `std::is_trivially_destructible_v<T>` are `true`, where `T` is the type of elements.

#### Execution policies

The standard library algorithms support several [execution policies](https://en.cppreference.com/cpp/algorithm/execution_policy_tag_t), and the library provides corresponding execution policy types and objects. Users may select an execution policy statically by invoking a parallel algorithm with an [execution policy object](https://en.cppreference.com/cpp/algorithm/execution_policy_tag) of the corresponding type.

Standard library implementations (but not the users) may define additional execution policies as an extension. The semantics of parallel algorithms invoked with an execution policy object of implementation-defined type is implementation-defined.

| Defined in  namespace `std::execution` |  | 
|  | execution policy types (class) | 
|  | global execution policy objects (constant) | 
| Defined in  namespace `std` |  | 
|  | test whether a class represents an execution policy (class template) | 
|  | specifies that a type represents an execution policy (exposition-only concept\*) | 

### Non-modifying sequence operations

#### Batch operations

|  | applies a unary [function object](https://en.cppreference.com/cpp/named_req/FunctionObject) to elements from a [range](https://en.cppreference.com/cpp/iterator#Ranges) (function template & algorithm function object) | 
|  | applies a function object to the first N elements of a sequence (function template & algorithm function object) | 

#### Search operations

|  | checks if a predicate is `true` for all, any or none of the elements in a range (function template & algorithm function object) | 
|  | checks if the range contains the given element or subrange (algorithm function object) | 
|  | finds the first element satisfying specific criteria (function template & algorithm function object) | 
|  | finds the last element satisfying specific criteria (algorithm function object) | 
|  | finds the last sequence of elements in a certain range (function template & algorithm function object) | 
|  | searches for any one of a set of elements (function template & algorithm function object) | 
|  | finds the first two adjacent items that are equal (or satisfy a given predicate) (function template & algorithm function object) | 
|  | returns the number of elements satisfying specific criteria (function template & algorithm function object) | 
|  | finds the first position where two ranges differ (function template & algorithm function object) | 
|  | determines if two sets of elements are the same (function template & algorithm function object) | 
|  | searches for the first occurrence of a range of elements (function template & algorithm function object) | 
|  | searches for the first occurrence of a number consecutive copies of an element in a range (function template & algorithm function object) | 
|  | checks whether a range starts with another range (algorithm function object) | 
|  | checks whether a range ends with another range (algorithm function object) | 


#### Fold operations [(since C++23)](https://en.cppreference.com/cpp/compiler_support/23#P2322R6)

|  | specifies that a callable type can be used in fold algorithms (exposition-only concept\*) | 
|  | left-folds a range of elements (algorithm function object) | 
|  | left-folds a range of elements using the first element as an initial value (algorithm function object) | 
|  | right-folds a range of elements (algorithm function object) | 
|  | right-folds a range of elements using the last element as an initial value (algorithm function object) | 
|  | left-folds a range of elements, and returns a [pair](https://en.cppreference.com/cpp/algorithm/ranges/return_types/in_value_result) (iterator, value) (algorithm function object) | 
|  | left-folds a range of elements using the first element as an initial value, and returns a [pair](https://en.cppreference.com/cpp/algorithm/ranges/return_types/in_value_result) (iterator, [optional](https://en.cppreference.com/cpp/utility/optional)) (algorithm function object) | 

### Modifying sequence operations

#### Copy operations

|  | copies a range of elements to a new location (function template & algorithm function object) | 
|  | copies a number of elements to a new location (function template & algorithm function object) | 
|  | copies a range of elements in backwards order (function template & algorithm function object) | 
|  | moves a range of elements to a new location (function template & algorithm function object) | 
|  | moves a range of elements to a new location in backwards order (function template & algorithm function object) | 

#### Swap operations

|  | swaps the values of two objects (function template) | 
|  | swaps two ranges of elements (function template & algorithm function object) | 
|  | swaps the elements pointed to by two iterators (function template) | 

#### Transformation operations

|  | applies a function to a range of elements, storing results in a destination range (function template & algorithm function object) | 
|  | replaces all values satisfying specific criteria with another value (function template & algorithm function object) | 
|  | copies a range, replacing elements satisfying specific criteria with another value (function template & algorithm function object) | 

#### Generation operations

|  | copy-assigns the given value to every element in a range (function template & algorithm function object) | 
|  | copy-assigns the given value to N elements in a range (function template & algorithm function object) | 
|  | assigns the results of successive function calls to every element in a range (function template & algorithm function object) | 
|  | assigns the results of successive function calls to N elements in a range (function template & algorithm function object) | 

#### Removing operations

|  | removes elements satisfying specific criteria (function template & algorithm function object) | 
|  | copies a range of elements omitting those that satisfy specific criteria (function template & algorithm function object) | 
|  | removes consecutive duplicate elements in a range (function template & algorithm function object) | 
|  | creates a copy of some range of elements that contains no consecutive duplicates (function template & algorithm function object) | 

#### Order-changing operations

|  | reverses the order of elements in a range (function template & algorithm function object) | 
|  | creates a copy of a range that is reversed (function template & algorithm function object) | 
|  | rotates the order of elements in a range (function template & algorithm function object) | 
|  | copies and rotate a range of elements (function template & algorithm function object) | 
|  | shifts elements in a range (function template & algorithm function object) | 
|  | randomly re-orders elements in a range (function template & algorithm function object) | 

#### Sampling operations

|  | selects N random elements from a sequence (function template & algorithm function object) | 

#### Requirements

Some algorithms require the sequence represented by the arguments to be “sorted” or “partitioned”. The behavior is undefined if the requirement is not met.

| A sequence is *sorted with respect to a comparator `comp`* if for every iterator `iter` pointing to the sequence and every non-negative integer `n` such that `iter + n`<sup>[\[1\]](https://en.cppreference.com#cite_note-plus-1)</sup> is a [valid iterator](https://en.cppreference.com/cpp/iterator#Dereferenceability_and_validity) pointing to an element of the sequence, `comp(*(iter + n), *iter) == false`<sup>[\[1\]](https://en.cppreference.com#cite_note-plus-1)</sup>. | [(until C++20)](https://en.cppreference.com/cpp/compiler_support/20#P0896R4) | 
| A sequence is *sorted with respect to `comp` and `proj`* for a comparator `comp` and projection `proj` if for every iterator `iter` pointing to the sequence and every non-negative integer `n` such that `iter + n`<sup>[\[1\]](https://en.cppreference.com#cite_note-plus-1)</sup> is a valid iterator pointing to an element of the sequence, `bool(std::invoke(comp, std::invoke(proj, *(iter + n)),`                        `std::invoke(proj, *iter)))` <sup>[\[1\]](https://en.cppreference.com#cite_note-plus-1)</sup> is `false`. A sequence is *sorted with respect to a comparator `comp`* if the sequence is sorted with respect to `comp` and `std::identity{}` (the identity projection). | [(since C++20)](https://en.cppreference.com/cpp/compiler_support/20#P0896R4) | 

A sequence `[``start``,` `finish``)` is *partitioned with respect to an expression `f(e)`* if there exists an integer `n` such that for all `i` in `[``0``,` `std::distance(start, finish)``)`, `f(*(start + i))`<sup>[\[1\]](https://en.cppreference.com#cite_note-plus-1)</sup> is `true` if and only if `i < n`.

#### Partitioning operations

|  | determines if the range is partitioned by the given predicate (function template & algorithm function object) | 
|  | divides a range of elements into two groups (function template & algorithm function object) | 
|  | copies a range dividing the elements into two groups (function template & algorithm function object) | 
|  | divides elements into two groups while preserving their relative order within each group (function template & algorithm function object) | 
|  | locates the partition point of a partitioned range (function template & algorithm function object) | 

#### Sorting operations

|  | sorts a range of elements (function template & algorithm function object) | 
|  | sorts a range of elements while preserving relative order between equivalent elements (function template & algorithm function object) | 
|  | sorts the first N elements of a range (function template & algorithm function object) | 
|  | copies and partially sorts a range of elements (function template & algorithm function object) | 
|  | checks whether a range is sorted (function template & algorithm function object) | 
|  | finds the largest sorted subrange (function template & algorithm function object) | 
|  | finds the N <sup>th</sup> element if the range were sorted (function template & algorithm function object) | 

#### Binary search operations (on partitioned ranges)

|  | finds the first element not less than the given value using binary search (function template & algorithm function object) | 
|  | finds the first element greater than the given value using binary search (function template & algorithm function object) | 
|  | finds the range of elements matching the given value using binary search (function template & algorithm function object) | 
|  | determines if an element exists in a range using binary search (function template & algorithm function object) | 

#### Set operations (on sorted ranges)

|  | determines if one sequence is a subsequence of another (function template & algorithm function object) | 
|  | computes the union of two sets (function template & algorithm function object) | 
|  | computes the intersection of two sets (function template & algorithm function object) | 
|  | computes the difference between two sets (function template & algorithm function object) | 
|  | computes the symmetric difference between two sets (function template & algorithm function object) | 

#### Merge operations (on sorted ranges)

|  | merges two sorted ranges (function template & algorithm function object) | 
|  | merges two ordered ranges in-place (function template & algorithm function object) | 

#### Heap operations

| A random access [range](https://en.cppreference.com/cpp/iterator#Ranges) `[``first``,` `last``)` is a *heap with respect to a comparator `comp`* if `bool(comp(first[(i - 1) / 2], first[i]))` is `false` for all integer `i` in `(``0``,` `last - first``)`. | [(until C++20)](https://en.cppreference.com/cpp/compiler_support/20#P0896R4) | 
| A random access [range](https://en.cppreference.com/cpp/iterator#Ranges) `[``first``,` `last``)` is a *heap with respect to `comp` and `proj`* for a comparator `comp` and projection `proj` if `bool(std::invoke(comp, std::invoke(proj, first[(i - 1) / 2]),`                        `std::invoke(proj, first[i]))` is `false` for all integer `i` in `(``0``,` `last - first``)`. A random access range `[``first``,` `last``)` is a *heap with respect to a comparator `comp`* if the range is a heap with respect to `comp` and `std::identity{}` (the identity projection). | [(since C++20)](https://en.cppreference.com/cpp/compiler_support/20#P0896R4) | 

A heap can be created by [std::make\_heap](https://en.cppreference.com/cpp/algorithm/make_heap) and [ranges::make\_heap](https://en.cppreference.com/cpp/algorithm/ranges/make_heap)[(since C++20)](https://en.cppreference.com/cpp/compiler_support/20#P0896R4).

For more properties of heap, see [max heap](https://en.wikipedia.org/wiki/Binary_heap).



|  | adds an element to a max heap (function template & algorithm function object) | 
|  | removes the largest element from a max heap (function template & algorithm function object) | 
|  | creates a max heap out of a range of elements (function template & algorithm function object) | 
|  | turns a max heap into a range of elements sorted in ascending order (function template & algorithm function object) | 
|  | checks if the given range is a max heap (function template & algorithm function object) | 
|  | finds the largest subrange that is a max heap (function template & algorithm function object) | 

#### Minimum/maximum operations

|  | returns the greater of the given values (function template & algorithm function object) | 
|  | returns the largest element in a range (function template & algorithm function object) | 
|  | returns the smaller of the given values (function template & algorithm function object) | 
|  | returns the smallest element in a range (function template & algorithm function object) | 
|  | returns the smaller and larger of two elements (function template & algorithm function object) | 
|  | returns the smallest and the largest elements in a range (function template & algorithm function object) | 
|  | clamps a value between a pair of boundary values (function template & algorithm function object) | 

#### Lexicographical comparison operations

|  | compares two ranges lexicographically (function template & algorithm function object) | 
|  | compares two ranges using three-way comparison (function template) | 

#### Permutation operations

|  | generates the next greater lexicographic permutation of a range of elements (function template & algorithm function object) | 
|  | generates the next smaller lexicographic permutation of a range of elements (function template & algorithm function object) | 
|  | determines if a sequence is a permutation of another sequence (function template & algorithm function object) | 

### Numeric operations

|  | fills a range with successive increments of the starting value (function template & algorithm function object) | 
|  | sums up or folds a range of elements (function template) | 
|  | computes the inner product of two ranges of elements (function template) | 
|  | computes the differences between adjacent elements in a range (function template) | 
|  | computes the partial sum of a range of elements (function template) | 
|  | similar to [std::accumulate](https://en.cppreference.com/cpp/algorithm/accumulate), except out of order (function template) | 
|  | similar to [std::partial\_sum](https://en.cppreference.com/cpp/algorithm/partial_sum), excludes the i<sup>th</sup> input element from the i<sup>th</sup> sum (function template) | 
|  | similar to [std::partial\_sum](https://en.cppreference.com/cpp/algorithm/partial_sum), includes the i<sup>th</sup> input element in the i<sup>th</sup> sum (function template) | 
|  | applies an invocable, then reduces out of order (function template) | 
|  | applies an invocable, then calculates exclusive scan (function template) | 
|  | applies an invocable, then calculates inclusive scan (function template) | 


### Specialized `<random>` algorithms [(since C++26)](https://en.cppreference.com/cpp/compiler_support/26#P1068R11)

|  | fills a range with random numbers from a uniform random bit generator (algorithm function object) | 

### Notes

| [Feature-test](https://en.cppreference.com/cpp/utility/feature_test) macro | Value | Std | Feature | 
|---|---|---|---|
| [`__cpp_lib_algorithm_default_value_type`](https://en.cppreference.com/cpp/feature_test#cpp_lib_algorithm_default_value_type) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_algorithm_default_value_type_202403L) | (C++26) | [List-initialization](https://en.cppreference.com/cpp/language/list_initialization) for algorithms | 
| [`__cpp_lib_algorithm_iterator_requirements`](https://en.cppreference.com/cpp/feature_test#cpp_lib_algorithm_iterator_requirements) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_algorithm_iterator_requirements_202207L) | (C++23) | Ranges iterators as inputs to non-Ranges algorithms | 
| [`__cpp_lib_clamp`](https://en.cppreference.com/cpp/feature_test#cpp_lib_clamp) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_clamp_201603L) | (C++17) | [std::clamp](https://en.cppreference.com/cpp/algorithm/clamp) | 
| [`__cpp_lib_constexpr_algorithms`](https://en.cppreference.com/cpp/feature_test#cpp_lib_constexpr_algorithms) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_algorithms_201806L) | (C++20) | Constexpr for algorithms | 
|  | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_algorithms_202306L) | (C++26) | Constexpr stable sorting | 
| [`__cpp_lib_execution`](https://en.cppreference.com/cpp/feature_test#cpp_lib_execution) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_execution_201603L) | (C++17) | Execution policies | 
|  | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_execution_201902L) | (C++20) | [std::execution::unsequenced\_policy](https://en.cppreference.com/cpp/algorithm/execution_policy_tag_t) | 
| [`__cpp_lib_freestanding_algorithm`](https://en.cppreference.com/cpp/feature_test#cpp_lib_freestanding_algorithm) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_algorithm_202311L) | (C++26) | Freestanding facilities in [`<algorithm>`](https://en.cppreference.com/cpp/header/algorithm) | 
| [`__cpp_lib_parallel_algorithm`](https://en.cppreference.com/cpp/feature_test#cpp_lib_parallel_algorithm) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_parallel_algorithm_201603L) | (C++17) | Parallel algorithms | 
|  | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_parallel_algorithm_202506L) | (C++26) | Parallel range algorithms | 
| [`__cpp_lib_robust_nonmodifying_seq_ops`](https://en.cppreference.com/cpp/feature_test#cpp_lib_robust_nonmodifying_seq_ops) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_robust_nonmodifying_seq_ops_201304L) | (C++14) | Making non-modifying sequence operations more robust (two-range overloads for [std::mismatch](https://en.cppreference.com/cpp/algorithm/mismatch), [std::equal](https://en.cppreference.com/cpp/algorithm/equal) and std::is\_permutation) | 
| [`__cpp_lib_sample`](https://en.cppreference.com/cpp/feature_test#cpp_lib_sample) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_sample_201603L) | (C++17) | [std::sample](https://en.cppreference.com/cpp/algorithm/sample) | 
| [`__cpp_lib_shift`](https://en.cppreference.com/cpp/feature_test#cpp_lib_shift) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_shift_201806L) | (C++20) | std::shift\_left and std::shift\_right | 

### C library

|  | sorts a range of elements with unspecified type (function) | 
|  | searches an array for an element of unspecified type (function) | 

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [LWG 193](https://cplusplus.github.io/LWG/issue193) | C++98 | heap required `*first` to be the largest element | there can be elements equal to `*first` | 
| [LWG 2150](https://cplusplus.github.io/LWG/issue2150) | C++98 | the definition of a sorted sequence was incorrect | corrected | 
| [LWG 2166](https://cplusplus.github.io/LWG/issue2166) | C++98 | the heap requirement did not match the definition of [max heap](https://en.wikipedia.org/wiki/Binary_heap) closely enough | requirement improved |