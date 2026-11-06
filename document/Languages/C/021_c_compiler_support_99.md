---
id: "c_021"
technology: "C"
category: "Languages"
title: "Compiler support for C99 - cppreference.com"
doc_order: 21
source_url: "https://en.cppreference.com/c/compiler_support/99"
language: "en"
retrieved_at: "2026-11-03 17:55:25"
content_hash: "644dff5b8c5e2136cdfb729bc1202df552b5748f157dc996828cab92491424c4"
---

# Compiler support for C99 - cppreference.com

Source: https://en.cppreference.com/c/compiler_support/99

---

# Compiler support for C99

From cppreference.com

### C99 core language features

|  | This section is incomplete Reason: needs to list C compilers, verification | 

| C99 feature | Paper(s) | GCC | Clang | MSVC | Apple Clang | EDG eccp | Intel C++ | Nvidia HPC C++ (ex PGI)\* | Nvidia nvcc | Cray |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|
| Universal-character-names in [identifiers](https://en.cppreference.com/c/language/identifier) |  | 3.1 | Yes | Yes |  |  |  |  |  |  |  | 
| Increased [translation limits](https://en.cppreference.com/c/language/identifier#Translation_limits) | [N590](https://open-std.org/JTC1/SC22/WG14/www/docs/n590.pdf) | 0.9 | N/A |  |  |  |  |  |  |  |  | 
| `//` [comments](https://en.cppreference.com/c/comment) | [N644](https://open-std.org/JTC1/SC22/WG14/www/docs/n644.htm) | 2.7 | Yes | Yes |  |  |  |  |  |  |  | 
| [`restrict`](https://en.cppreference.com/c/language/restrict) pointers | [N448](https://open-std.org/JTC1/SC22/WG14/www/docs/n448.pdf) | 2.95 | Yes | partial\* |  |  |  |  |  |  |  | 
| Enhanced [arithmetic types](https://en.cppreference.com/c/language/arithmetic_types) | [N815](https://open-std.org/JTC1/SC22/WG14/www/docs/n815.htm) [N601](https://open-std.org/JTC1/SC22/WG14/www/docs/n601.ps) [N620](https://open-std.org/JTC1/SC22/WG14/www/docs/n620.ps) [N638](https://open-std.org/JTC1/SC22/WG14/www/docs/n638.ps) [N657](https://open-std.org/JTC1/SC22/WG14/www/docs/n657.ps) [N694](https://open-std.org/JTC1/SC22/WG14/www/docs/n694.ps) [N809](https://open-std.org/JTC1/SC22/WG14/www/docs/n809.ps) | Yes | partial | Maybe |  |  |  |  |  |  |  | 
| Flexible array members |  | 3.0 | Yes | Yes |  |  |  |  |  |  |  | 
| [Variable-length array](https://en.cppreference.com/c/language/array#Variable-length_arrays) (VLA) types | [N683](https://open-std.org/JTC1/SC22/WG14/www/docs/n683.htm) | 0.9 | Yes |  |  |  |  |  |  |  |  | 
| Variably-modified (VM) types | [N2778](https://open-std.org/JTC1/SC22/WG14/www/docs/n2778.pdf) | N/A | Yes |  |  |  |  |  |  |  |  | 
| Designated initializers | [N494](https://open-std.org/JTC1/SC22/WG14/www/docs/n494.pdf) | 3.0 | Yes | Yes |  |  |  |  |  |  |  | 
| Non-constant initializers |  | 1.21 | N/A |  |  |  |  |  |  |  |  | 
| Idempotent cvr-qualifiers | [N505](https://open-std.org/JTC1/SC22/WG14/www/docs/n505.pdf) | 3.0 | N/A |  |  |  |  |  |  |  |  | 
| Trailing comma in [enumerator-list](https://en.cppreference.com/c/language/enum) |  | 0.9 | Yes | Yes |  |  |  |  |  |  |  | 
| Hexadecimal [floating constants](https://en.cppreference.com/c/language/floating_constant) | [N308](https://open-std.org/JTC1/SC22/WG14/www/docs/n308.pdf) | 2.8 | Yes | Yes |  |  |  |  |  |  |  | 
| [Compound literals](https://en.cppreference.com/c/language/compound_literal) | [N716](https://open-std.org/JTC1/SC22/WG14/www/docs/n716.htm) | 3.1 | Yes | Yes |  |  |  |  |  |  |  | 
| Floating-point environment |  | partial | partial |  |  |  |  |  |  |  |  | 
| Requiring truncation for divisions of signed integer types | [N617](https://open-std.org/JTC1/SC22/WG14/www/docs/n617.htm) | 0.9 | N/A |  |  |  |  |  |  |  |  | 
| Implicit `return 0;` in the [`main()` function](https://en.cppreference.com/c/language/main_function) |  | Yes | Yes | Yes |  |  |  |  |  |  |  | 
| Declarations and statements in mixed order | [N740](https://open-std.org/JTC1/SC22/WG14/www/docs/n740.htm) | 3.0 | Yes | Yes |  |  |  |  |  |  |  | 
| init-statement in [`for`](https://en.cppreference.com/c/language/for) loops |  | Yes | Yes | Yes |  |  |  |  |  |  |  | 
| [`inline`](https://en.cppreference.com/c/language/inline) functions | [N741](https://open-std.org/JTC1/SC22/WG14/www/docs/n741.htm) | 4.3 | Yes | Yes |  |  |  |  |  |  |  | 
| Predefined variable [`__func__`](https://en.cppreference.com/c/language/function_definition) | [N611](https://open-std.org/JTC1/SC22/WG14/www/docs/n611.ps) | 2.95 | Yes | Yes |  |  |  |  |  |  |  | 
| Cvr-qualifiers and `static` in `[]` within function declarations |  | 3.1 | Yes |  |  |  |  |  |  |  |  | 
| [Variadic macros](https://en.cppreference.com/c/preprocessor/replace) | [N707](https://open-std.org/JTC1/SC22/WG14/www/docs/n707.htm) | 2.95 | Yes | Yes |  |  |  |  |  |  |  | 
| [`_Pragma`](https://en.cppreference.com/c/preprocessor/impl) preprocessor operator | [N634](https://open-std.org/JTC1/SC22/WG14/www/docs/n634.ps) | 3.0 | Yes | partial\* |  |  |  |  |  |  |  | 
| Standard pragmas for floating-point evaluation | [N631](https://open-std.org/JTC1/SC22/WG14/www/docs/n631.htm) [N696](https://open-std.org/JTC1/SC22/WG14/www/docs/n696.ps) | No | No |  |  |  |  |  |  |  |  | 
| C99 feature | Paper(s) | GCC | Clang | MSVC | Apple Clang | EDG eccp | Intel C++ | Nvidia HPC C++ (ex PGI)\* | Nvidia nvcc | Cray |  |