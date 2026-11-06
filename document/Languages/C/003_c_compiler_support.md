---
id: "c_003"
technology: "C"
category: "Languages"
title: "C compiler support - cppreference.com"
doc_order: 3
source_url: "https://en.cppreference.com/c/compiler_support"
language: "en"
retrieved_at: "2026-11-03 17:55:09"
content_hash: "094d04aa48c10693694bf22374a5f5b311fdecc5ae45db52e2c0a8d90acb7618"
---

# C compiler support - cppreference.com

Source: https://en.cppreference.com/c/compiler_support

---

# C compiler support

From cppreference.com

|  | This page is maintained as best-effort and may lag behind most recent compiler releases. If you see something is out-of-date, please help us by updating it! | 


## C23 features

Note that this list may change, as the draft C23/2x standard evolves.

### C23 core language features

|  | This section is incomplete Reason: status for other compilers supporting C2x | 

| C23 feature | Paper(s) | GCC | Clang | MSVC | Apple Clang | EDG eccp | Intel C++ | Nvidia HPC C++ (ex PGI)\* | Nvidia nvcc | Cray |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|
| [`static_assert`](https://en.cppreference.com/c/language/_Static_assert) with no message | [N2265](https://open-std.org/JTC1/SC22/WG14/www/docs/n2265.pdf) | 9 | 9 | Yes | Yes | 6.5 | 2021.1.2 (clang based) |  |  |  |  | 
| `[[`[nodiscard](https://en.cppreference.com/c/language/attributes/nodiscard)]] | [N2267](https://open-std.org/JTC1/SC22/WG14/www/docs/n2267.pdf) | 10 | 9 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| `[[`[maybe_unused](https://en.cppreference.com/c/language/attributes/maybe_unused)]] | [N2270](https://open-std.org/JTC1/SC22/WG14/www/docs/n2270.pdf) | 10 | 9 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| `[[`[deprecated](https://en.cppreference.com/c/language/attributes/deprecated)]] | [N2334](https://open-std.org/JTC1/SC22/WG14/www/docs/n2334.pdf) | 10 | 9 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| [Attributes](https://en.cppreference.com/c/language/attributes) | [N2335](https://open-std.org/JTC1/SC22/WG14/www/docs/n2335.pdf) [N2554](https://open-std.org/JTC1/SC22/WG14/www/docs/n2554.pdf) | 10 | 9 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| IEEE 754 decimal floating-point types | [N2341](https://open-std.org/JTC1/SC22/WG14/www/docs/n2341.pdf) | 4.2 (partial)\* 12 |  |  |  |  | 13.0 (partial)\* |  |  |  |  | 
| `[[`[fallthrough](https://en.cppreference.com/c/language/attributes/fallthrough)]] | [N2408](https://open-std.org/JTC1/SC22/WG14/www/docs/n2408.pdf) | 10 | 9 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| [`u8` character constants](https://en.cppreference.com/c/language/character_constant) | [N2418](https://open-std.org/JTC1/SC22/WG14/www/docs/n2418.pdf) | 10 | 15 |  |  | 6.5 | 2022.2 |  |  |  |  | 
| Removal of [function definitions](https://en.cppreference.com/c/language/function_definition) without prototype | [N2432](https://open-std.org/JTC1/SC22/WG14/www/docs/n2432.pdf) | 10 | 15 |  |  | 6.9 | 2022.2 |  |  |  |  | 
| `[[`[nodiscard](https://en.cppreference.com/c/language/attributes/nodiscard)]] with message | [N2448](https://open-std.org/JTC1/SC22/WG14/www/docs/n2448.pdf) | 11 | 10 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| Unnamed parameters in function definitions | [N2480](https://open-std.org/JTC1/SC22/WG14/www/docs/n2480.pdf) | 11 | 11 |  | Yes | 6.4 | 2021.1.2 (clang based) |  |  |  |  | 
| [Labels](https://en.cppreference.com/c/language/statements#Labels) before declarations and end of blocks | [N2508](https://open-std.org/JTC1/SC22/WG14/www/docs/n2508.pdf) | 11 | 16 | Partial\* |  | 6.5 | 17.0\* |  |  |  |  | 
| [Binary integer constants](https://en.cppreference.com/c/language/integer_constant) | [N2549](https://open-std.org/JTC1/SC22/WG14/www/docs/n2549.pdf) | 4.3\* 11 | 2.9\* 9 | 19.0 (2015)\*\* | Yes | 6.5 | 11.0\* |  |  |  |  | 
| [`__has_c_attribute`](https://en.cppreference.com/c/language/attributes#Attribute_testing) in preprocessor conditionals | [N2553](https://open-std.org/JTC1/SC22/WG14/www/docs/n2553.pdf) | 11 | 9 |  | Yes | 6.5 | 2021.1.2 (clang based) |  |  |  |  | 
| Allow duplicate attributes | [N2557](https://open-std.org/JTC1/SC22/WG14/www/docs/n2557.pdf) | 11 | 13 |  | Yes | 6.5 | 2021.4 (clang-based |  |  |  |  | 
| IEEE 754 interchange and extended types | [N2601](https://open-std.org/JTC1/SC22/WG14/www/docs/n2601.pdf) | 7 (partial)\* 14 | 6 (partial)\* |  | Partial\* |  |  |  |  |  |  | 
| Digit separators | [N2626](https://open-std.org/JTC1/SC22/WG14/www/docs/n2626.pdf) | 12 | 13 | 19.0 (2015)\*\* | Yes | 6.5 | 18.0\* |  |  |  |  | 
| [`#elifdef` and `#elifndef`](https://en.cppreference.com/c/preprocessor/conditional) | [N2645](https://open-std.org/JTC1/SC22/WG14/www/docs/n2645.pdf) | 12 | 13 | 19.40\* | 13.1.6\* | 6.5 | 2021.4 |  |  |  |  | 
| Type change of [`u8` string literals](https://en.cppreference.com/c/language/string_literal) | [N2653](https://open-std.org/JTC1/SC22/WG14/www/docs/n2653.htm) | 13 |  |  |  |  |  |  |  |  |  | 
| `[[`[maybe_unused](https://en.cppreference.com/c/language/attributes/maybe_unused)]] for labels | [N2662](https://open-std.org/JTC1/SC22/WG14/www/docs/n2662.pdf) | 11 | 16 |  |  | 6.5 | 2022.2 |  |  |  |  | 
|  [`#warning`](https://en.cppreference.com/c/preprocessor/error) | [N2686](https://open-std.org/JTC1/SC22/WG14/www/docs/n2686.pdf) | Yes | Yes |  | Yes | 6.5 | Yes |  |  |  |  | 
| Bit-precise integer types ( `_BitInt`) | [N2763](https://open-std.org/JTC1/SC22/WG14/www/docs/n2763.pdf) | 14 (partial)\* | 15 |  |  | 6.5 | 2022.2 |  |  |  |  | 
| `[[`[noreturn](https://en.cppreference.com/c/language/attributes/noreturn)]] | [N2764](https://open-std.org/JTC1/SC22/WG14/www/docs/n2764.pdf) | 13 | 15 |  |  | 6.5 | 2022.2 |  |  |  |  | 
| Suffixes for bit-precise integer constants | [N2775](https://open-std.org/JTC1/SC22/WG14/www/docs/n2775.pdf) | 14 | 15 |  |  | 6.9 | 2022.2 |  |  |  |  | 
| [`__has_include`](https://en.cppreference.com/c/preprocessor/include) in preprocessor conditionals | [N2799](https://open-std.org/JTC1/SC22/WG14/www/docs/n2799.pdf) | 5 | Yes | 19.11\* | Yes | 6.5 | 18.0 |  |  |  |  | 
| Identifier Syntax using Unicode Standard Annex 31 | [N2836](https://open-std.org/JTC1/SC22/WG14/www/docs/n2836.pdf) | 13 | 15 |  |  | 6.5 | 2022.2 |  |  |  |  | 
| Removal of [function declarations](https://en.cppreference.com/c/language/function_declaration) without prototype | [N2841](https://open-std.org/JTC1/SC22/WG14/www/docs/n2841.htm) | 13 | 15 |  |  | 6.9 | 2022.2 |  |  |  |  | 
| [Empty initializers](https://en.cppreference.com/c/language/initialization#Empty_initialization) | [N2900](https://open-std.org/JTC1/SC22/WG14/www/docs/n2900.htm) | Partial\* 13 | Partial\* |  | Partial\* | Partial\* | Partial\* |  |  |  |  | 
| [`typeof`](https://en.cppreference.com/c/language/typeof) and [`typeof_unqual`](https://en.cppreference.com/c/language/typeof) | [N2927](https://open-std.org/JTC1/SC22/WG14/www/docs/n2927.htm) [N2930](https://open-std.org/JTC1/SC22/WG14/www/docs/n2930.pdf) | Partial\* 13 | Partial\* 16 | 19.39\* | Partial\* | Partial\* | Partial\* |  |  | Partial\* |  | 
| New spelling of keywords | [N2934](https://open-std.org/JTC1/SC22/WG14/www/docs/n2934.pdf) | 13 | 16 |  |  | 6.5 |  |  |  |  |  | 
| Predefined [`true` and `false`](https://en.cppreference.com/c/language/bool_constant) | [N2935](https://open-std.org/JTC1/SC22/WG14/www/docs/n2935.pdf) | 13 | 15 |  |  | 6.8 | 2022.2 |  |  |  |  | 
| `[[`[unsequenced](https://en.cppreference.com/c/language/attributes/unsequenced)]] and `[[`[reproducible](https://en.cppreference.com/c/language/attributes/reproducible)]] | [N2956](https://open-std.org/JTC1/SC22/WG14/www/docs/n2956.htm) | 15 |  |  |  |  |  |  |  |  |  | 
| Relax requirements for [variadic parameter list](https://en.cppreference.com/c/language/variadic) | [N2975](https://open-std.org/JTC1/SC22/WG14/www/docs/n2975.pdf) | 13 | 16 |  |  | 6.5 | 2023.1 |  |  |  |  | 
| Type inference in object definitions | [N3007](https://open-std.org/JTC1/SC22/WG14/www/docs/n3007.htm) | 13 | 18 |  |  |  |  |  |  |  |  | 
|  [`#embed`](https://en.cppreference.com/c/preprocessor/embed) | [N3017](https://open-std.org/JTC1/SC22/WG14/www/docs/n3017.htm) | 15 | 19 |  |  | 6.8 |  |  |  |  |  | 
| [`constexpr`](https://en.cppreference.com/c/language/constexpr) objects | [N3018](https://open-std.org/JTC1/SC22/WG14/www/docs/n3018.htm) | 13 | 19 |  |  |  |  |  |  |  |  | 
| Improved Normal Enumerations | [N3029](https://open-std.org/JTC1/SC22/WG14/www/docs/n3029.htm) | 13 | 20\* |  |  |  |  |  |  |  |  | 
| Enumerations with fixed underlying types | [N3030](https://open-std.org/JTC1/SC22/WG14/www/docs/n3030.htm) | 13 | 20\* |  |  | 6.8 |  |  |  |  |  | 
| [`__VA_OPT__`](https://en.cppreference.com/c/preprocessor/replace#Function-like_macros) | [N3033](https://open-std.org/JTC1/SC22/WG14/www/docs/n3033.htm) | 8 13 | 12 | 19.39\* |  | 6.5 |  |  |  |  |  | 
| Storage-class specifiers for compound literals | [N3038](https://open-std.org/JTC1/SC22/WG14/www/docs/n3038.htm) | 13 |  |  |  |  |  |  |  |  |  | 
| [`nullptr`](https://en.cppreference.com/c/language/nullptr) | [N3042](https://open-std.org/JTC1/SC22/WG14/www/docs/n3042.htm) | 13 | 16 |  |  | 6.7 |  |  |  |  |  | 
| C23 feature | Paper(s) | GCC | Clang | MSVC | Apple Clang | EDG eccp | Intel C++ | Nvidia HPC C++ (ex PGI)\* | Nvidia nvcc | Cray |  | 

### C23 library features

|  | This section is incomplete Reason: a different list for C standard libraries | 


## C99 features

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