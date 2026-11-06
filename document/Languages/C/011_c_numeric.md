---
id: "c_011"
technology: "C"
category: "Languages"
title: "Numerics - cppreference.com"
doc_order: 11
source_url: "https://en.cppreference.com/c/numeric"
language: "en"
retrieved_at: "2026-11-03 17:55:16"
content_hash: "c8fec366cfd1128b31301b430afac40b4ea4c720dba2e0ce1565bdd5702d4a36"
---

# Numerics - cppreference.com

Source: https://en.cppreference.com/c/numeric

---

# Numerics

The C numerics library includes common mathematical functions and types, as well as support for random number generation.

The header [`<math.h>`](https://en.cppreference.com/c/header/math) provides [standard C library mathematical functions](https://en.cppreference.com/c/numeric/math) such as [fabs](https://en.cppreference.com/c/numeric/math/fabs), [sqrt](https://en.cppreference.com/c/numeric/math/sqrt), and [sin](https://en.cppreference.com/c/numeric/math/sin).

The header [`<fenv.h>`](https://en.cppreference.com/c/header/fenv) defines [flags and functions related to exceptional floating-point state](https://en.cppreference.com/c/numeric/fenv), such as overflow and division by zero.

The header [`<stdlib.h>`](https://en.cppreference.com/c/header/stdlib) also includes C-style random number generation via [srand](https://en.cppreference.com/c/numeric/random/srand) and [rand](https://en.cppreference.com/c/numeric/random/rand).

The header [`<complex.h>`](https://en.cppreference.com/c/header/complex) provides types and functions to work with [complex numbers](https://en.cppreference.com/c/numeric/complex).

The header [`<tgmath.h>`](https://en.cppreference.com/c/header/tgmath) provides some macros for a function which names XXX:

- real function:

  - `float` variant `XXXf`
  - `double` variant `XXX`
  - `long double` variant `XXXl`

- complex function:

  - `float` variant `cXXXf`
  - `double` variant `cXXX`
  - `long double` variant `cXXXl`


### [Bit manipulation](https://en.cppreference.com/c/numeric/bit_manip) (since C23)

The header [`<stdbit.h>`](https://en.cppreference.com/c/header/stdbit) provides macros and functions to work with the [byte ordering](https://en.cppreference.com/c/numeric/bit_manip#Macros) and [byte and bit representation](https://en.cppreference.com/c/numeric/bit_manip#Functions) of C objects.


### Checked integer arithmetic (since C23)

Provides some [type-generic macros](https://en.cppreference.com/c/language/generic) for checked integer arithmetic:

|  | checked addition operation on two integers (type-generic function macro) | 
|  | checked subtraction operation on two integers (type-generic function macro) | 
|  | checked multiplication operation on two integers (type-generic function macro) |