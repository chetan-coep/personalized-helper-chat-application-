---
id: "c++_019"
technology: "C++"
category: "Languages"
title: "Numerics library - cppreference.com"
doc_order: 19
source_url: "https://en.cppreference.com/cpp/numeric"
language: "en"
retrieved_at: "2026-11-03 17:56:15"
content_hash: "f6cae548b30ca18334666d48a5183f7d96753a7cf14bf577f086436c12ef9d8a"
---

# Numerics library - cppreference.com

Source: https://en.cppreference.com/cpp/numeric

---

# Numerics library

The C++ numerics library includes common mathematical functions and types, as well as optimized numeric arrays and support for random number generation.

## Mathematical functions and types

The header [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) provides [standard C library mathematical functions](https://en.cppreference.com/cpp/numeric/math) such as [std::fabs](https://en.cppreference.com/cpp/numeric/math/fabs), [std::sqrt](https://en.cppreference.com/cpp/numeric/math/sqrt), and [std::sin](https://en.cppreference.com/cpp/numeric/math/sin).


### [Mathematical special functions](https://en.cppreference.com/cpp/numeric/special_functions) (since C++17)

The header [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) also provides several mathematical special functions such as [std::beta](https://en.cppreference.com/cpp/numeric/special_functions/beta), [std::hermite](https://en.cppreference.com/cpp/numeric/special_functions/hermite), and [std::cyl\_bessel\_i](https://en.cppreference.com/cpp/numeric/special_functions/cyl_bessel_i).


### [Mathematical constants](https://en.cppreference.com/cpp/numeric/constants) (since C++20)

The header [`<numbers>`](https://en.cppreference.com/cpp/header/numbers) provides several mathematical constants, such as [std::numbers::pi](https://en.cppreference.com/cpp/numeric/constants) or [std::numbers::sqrt2](https://en.cppreference.com/cpp/numeric/constants)


### [Basic linear algebra algorithms](https://en.cppreference.com/cpp/numeric/linalg) (since C++26)

The header [`<linalg>`](https://en.cppreference.com/cpp/header/linalg) provides basic linear algebra algorithms which are based on BLAS.


### [Data-parallel types](https://en.cppreference.com/cpp/numeric/simd) (since C++26)

The header [`<simd>`](https://en.cppreference.com/cpp/header/simd) provides portable types for explicitly stating data-parallelism and structuring data for more efficient SIMD access.

### Complex number arithmetic

|  | a complex number type (class template) | 

### Numeric arrays

|  | numeric arrays, array masks and array slices (class template) | 

## Numeric algorithms

The header [`<numeric>`](https://en.cppreference.com/cpp/header/numeric) provides numeric algorithms below:


### Factor operations (since C++17)

|  | computes the greatest common divisor of two integers (function template) | 
|  | computes the least common multiple of two integers (function template) | 


### Interpolation operations (C++20)

|  | midpoint between two numbers or pointers (function template) | 
|  | linear interpolation function (function) | 


### Saturation arithmetic (since C++26)

|  | saturating addition operation on two integers (function template) | 
|  | saturating subtraction operation on two integers (function template) | 
|  | saturating multiplication operation on two integers (function template) | 
|  | saturating division operation on two integers (function template) | 
|  | returns an integer value clamped to the range of another integer type (function template) | 

### Numeric operations

|  | fills a range with successive increments of the starting value (function template & algorithm function object) | 
|  | sums up or folds a range of elements (function template) | 
|  | similar to [std::accumulate](https://en.cppreference.com/cpp/algorithm/accumulate), except out of order (function template) | 
|  | applies an invocable, then reduces out of order (function template) | 
|  | computes the inner product of two ranges of elements (function template) | 
|  | computes the differences between adjacent elements in a range (function template) | 
|  | computes the partial sum of a range of elements (function template) | 
|  | similar to [std::partial\_sum](https://en.cppreference.com/cpp/algorithm/partial_sum), includes the i<sup>th</sup> input element in the i<sup>th</sup> sum (function template) | 
|  | similar to [std::partial\_sum](https://en.cppreference.com/cpp/algorithm/partial_sum), excludes the i<sup>th</sup> input element from the i<sup>th</sup> sum (function template) | 
|  | applies an invocable, then calculates inclusive scan (function template) | 
|  | applies an invocable, then calculates exclusive scan (function template) | 

## Miscellaneous

The header [`<random>`](https://en.cppreference.com/cpp/header/random) defines [pseudo-random number generators and numerical distributions](https://en.cppreference.com/cpp/numeric/random). The header [`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) also includes C-style random number generation via [std::srand](https://en.cppreference.com/cpp/numeric/random/srand) and [std::rand](https://en.cppreference.com/cpp/numeric/random/rand).


### [Floating-point environment](https://en.cppreference.com/cpp/numeric/fenv) (since C++11)

The header [`<cfenv>`](https://en.cppreference.com/cpp/header/cfenv) defines [flags and functions related to exceptional floating-point state](https://en.cppreference.com/cpp/numeric/fenv), such as overflow and division by zero.


### [Bit manipulation](https://en.cppreference.com/cpp/utility/bit) (since C++20)

The header [`<bit>`](https://en.cppreference.com/cpp/header/bit) provides several function templates to access, manipulate, and process individual bits and bit sequences. The byte ordering ([endianness](https://en.cppreference.com/cpp/types/endian)) of scalar types can be inspected via `std::endian` facility.


### Checked integer arithmetic (since C++26)

The C compatibility header [`<stdckdint.h>`](https://en.cppreference.com/cpp/header/stdckdint.h) provides several function templates for checked integer arithmetic.

|  | checked addition operation on two integers (function template) | 
|  | checked subtraction operation on two integers (function template) | 
|  | checked multiplication operation on two integers (function template) |