---
id: "c++_007"
technology: "C++"
category: "Languages"
title: "Feature testing (since C++20) - cppreference.com"
doc_order: 7
source_url: "https://en.cppreference.com/cpp/feature_test"
language: "en"
retrieved_at: "2026-11-03 17:55:54"
content_hash: "477267c0de7cc79f7806529dfc1a9861f5519e27d2040f6b5a575beec3c6cf98"
---

# Feature testing (since C++20) - cppreference.com

Source: https://en.cppreference.com/cpp/feature_test

---

# Feature testing (since C++20)

The standard defines a set of [preprocessor macros](https://en.cppreference.com/cpp/preprocessor/replace) corresponding to C++ language and library features introduced in C++11 or later. They are intended as a simple and portable way to detect the presence of said features.

### Attributes

| **__has_cpp_attribute(** attribute-token **)** |  |  |  |  |  |  |  |  |  | 

Checks for the support of an [attribute](https://en.cppreference.com/cpp/language/attributes) named by attribute-token (after macro expansion).

For each standard attribute, it is implementation-defined whether `__has_cpp_attribute` expands to the value given in the table below (which is the year and month in which the attribute was added to the working draft) or `0`. It will expand to given value in the table if and only if the standard attribute causes the implementation to behave as recommended (issuing diagnostic messages, affecting class layout, etc.).

The presence of vendor-specific attributes is determined by a non-zero value.

`__has_cpp_attribute` can be expanded in the expression of 


It is treated as a defined macro by 


| attribute-token | Attribute | Value | Std | Paper(s) | 
|---|---|---|---|---|
| `assume` | `[[`[assume](https://en.cppreference.com/cpp/language/attributes/assume)]] | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#assume) | (C++23) | [P1774R8](https://wg21.link/P1774R8) | 
| `carries_dependency` | `[[`[carries_dependency](https://en.cppreference.com/cpp/language/attributes/carries_dependency)]] | [`200809L`](https://en.cppreference.com/cpp/compiler_support/11#carries_dependency) | (C++11) (until C++26) | [N2556](https://wg21.link/N2556) [N2643](https://wg21.link/N2643) [P3475R2](https://wg21.link/P3475R2) | 
| `deprecated` | `[[`[deprecated](https://en.cppreference.com/cpp/language/attributes/deprecated)]] | [`201309L`](https://en.cppreference.com/cpp/compiler_support/14#deprecated) | (C++14) | [N3760](https://wg21.link/N3760) | 
| `fallthrough` | `[[`[fallthrough](https://en.cppreference.com/cpp/language/attributes/fallthrough)]] | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#fallthrough) | (C++17) | [P0188R1](https://wg21.link/P0188R1) | 
| `indeterminate` | `[[`[indeterminate](https://en.cppreference.com/cpp/language/attributes/indeterminate)]] | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#indeterminate) | (C++26) | [P2795R5](https://wg21.link/P2795R5) | 
| `likely` | `[[`[likely](https://en.cppreference.com/cpp/language/attributes/likely)]] | [`201803L`](https://en.cppreference.com/cpp/compiler_support/20#likely) | (C++20) | [P0479R5](https://wg21.link/P0479R5) | 
| `maybe_unused` | `[[`[maybe_unused](https://en.cppreference.com/cpp/language/attributes/maybe_unused)]] | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#maybe_unused) | (C++17) | [P0212R1](https://wg21.link/P0212R1) | 
| `no_unique_address` | `[[`[no_unique_address](https://en.cppreference.com/cpp/language/attributes/no_unique_address)]] | [`201803L`](https://en.cppreference.com/cpp/compiler_support/20#no_unique_address) | (C++20) | [P0840R2](https://wg21.link/P0840R2) | 
| `nodiscard` | `[[`[nodiscard](https://en.cppreference.com/cpp/language/attributes/nodiscard)]] | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#nodiscard) | (C++17) | [P0189R1](https://wg21.link/P0189R1) | 
|  | `[[`[nodiscard](https://en.cppreference.com/cpp/language/attributes/nodiscard)]] with reason | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#nodiscard) | (C++20) | [P1301R4](https://wg21.link/P1301R4) | 
| `noreturn` | `[[`[noreturn](https://en.cppreference.com/cpp/language/attributes/noreturn)]] | [`200809L`](https://en.cppreference.com/cpp/compiler_support/11#noreturn) | (C++11) | [N2761](https://wg21.link/N2761) | 
| `unlikely` | `[[`[unlikely](https://en.cppreference.com/cpp/language/attributes/likely)]] | [`201803L`](https://en.cppreference.com/cpp/compiler_support/20#likely) | (C++20) | [P0479R5](https://wg21.link/P0479R5) | 
| Total number of attributes: 11 |  |  |  |  | 

### Language features

The following macros can be used to detect whether a language feature is implemented by the current implementation. They are [predefined](https://en.cppreference.com/cpp/preprocessor/replace#Predefined_macros) in every translation unit.

Each macro expands to an integer literal corresponding to the year and month when the corresponding feature has been included in the working draft. When a feature changes significantly, the macro will be updated accordingly.

| Macro name | Feature | Value | Std | Paper(s) | 
|---|---|---|---|---|
| `__cpp_aggregate_bases` | [Aggregate classes](https://en.cppreference.com/cpp/language/aggregate_initialization) with base classes | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_aggregate_bases_201603L) | (C++17) | [P0017R1](https://wg21.link/P0017R1) | 
| `__cpp_aggregate_nsdmi` | [Aggregate classes](https://en.cppreference.com/cpp/language/aggregate_initialization) with [default member initializers](https://en.cppreference.com/cpp/language/data_members#Member_initialization) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_aggregate_nsdmi_201304L) | (C++14) | [N3653](https://wg21.link/N3653) | 
| `__cpp_aggregate_paren_init` | [Aggregate initialization](https://en.cppreference.com/cpp/language/aggregate_initialization) in the form of [direct initialization](https://en.cppreference.com/cpp/language/direct_initialization) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_aggregate_paren_init_201902L) | (C++20) | [P0960R3](https://wg21.link/P0960R3) | 
| `__cpp_alias_templates` | [Alias templates](https://en.cppreference.com/cpp/language/type_alias) | [`200704L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_alias_templates_200704L) | (C++11) | [N2258](https://wg21.link/N2258) | 
| `__cpp_aligned_new` | [Dynamic memory allocation for over-aligned data](https://en.cppreference.com/cpp/memory/new/align_val_t) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_aligned_new_201606L) | (C++17) | [P0035R4](https://wg21.link/P0035R4) | 
| `__cpp_attributes` | [Attributes](https://en.cppreference.com/cpp/language/attributes) | [`200809L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_attributes_200809L) | (C++11) | [N2761](https://wg21.link/N2761) | 
| `__cpp_auto_cast` | [Casting an expression to a prvalue](https://en.cppreference.com/cpp/language/explicit_cast) (`auto(x)`) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_auto_cast_202110L) | (C++23) | [P0849R8](https://wg21.link/P0849R8) | 
| `__cpp_binary_literals` | [Binary literals](https://en.cppreference.com/cpp/language/integer_literal) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_binary_literals_201304L) | (C++14) | [N3472](https://wg21.link/N3472) | 
| `__cpp_capture_star_this` | [Lambda capture of `*this` by value as `[=,*this]`](https://en.cppreference.com/cpp/language/lambda#Lambda_capture) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_capture_star_this_201603L) | (C++17) | [P0018R3](https://wg21.link/P0018R3) | 
| `__cpp_char8_t` | [`char8_t`](https://en.cppreference.com/cpp/keyword/char8_t) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_char8_t_201811L) | (C++20) | [P0482R6](https://wg21.link/P0482R6) | 
|  | char8\_t compatibility and portability fix (allow [initialization of (unsigned) char arrays](https://en.cppreference.com/cpp/language/aggregate_initialization#Character_arrays) from [UTF-8 string literals](https://en.cppreference.com/cpp/language/string_literal)) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_char8_t_202207L) | (C++23) (DR20) | [P2513R4](https://wg21.link/P2513R4) | 
| `__cpp_concepts` | [Concepts](https://en.cppreference.com/cpp/language/constraints) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_concepts_201907L) | (C++20) | [P0734R0](https://wg21.link/P0734R0) [P1084R2](https://wg21.link/P1084R2) [P1452R2](https://wg21.link/P1452R2) | 
|  | Conditional trivial special member functions | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_concepts_202002L) |  | [P0848R3](https://wg21.link/P0848R3) [P2493R0](https://wg21.link/P2493R0) | 
|  | Conditional noexcept specifiers in [compound requirements](https://en.cppreference.com/cpp/language/requires#Compound_requirements) | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_concepts_202606L) | (C++29) | [P3822R2](https://wg21.link/P3822R2) | 
| `__cpp_conditional_explicit` | [Conditional `explicit` specifier](https://en.cppreference.com/cpp/language/explicit) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_conditional_explicit_201806L) | (C++20) | [P0892R2](https://wg21.link/P0892R2) | 
| `__cpp_consteval` | [Immediate functions](https://en.cppreference.com/cpp/language/consteval) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_consteval_201811L) | (C++20) | [P1073R3](https://wg21.link/P1073R3) | 
|  | Making [`consteval`](https://en.cppreference.com/cpp/language/consteval) propagate up | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_consteval_202211L) | (C++23) (DR20) | [P2564R3](https://wg21.link/P2564R3) | 
|  | consteval-only values | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_consteval_202606L) | (C++29) (DR20) | [P4101R1](https://wg21.link/P4101R1) | 
| `__cpp_constexpr` | [`constexpr`](https://en.cppreference.com/cpp/language/constexpr) | [`200704L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_constexpr_200704L) | (C++11) | [N2235](https://wg21.link/N2235) | 
|  | [Relaxed `constexpr`](https://en.cppreference.com/cpp/language/constexpr#relaxed-constexpr), [non-`const` `constexpr` methods](https://en.cppreference.com/cpp/language/constexpr#constexpr-method-is-const) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_constexpr_201304L) | (C++14) | [N3652](https://wg21.link/N3652) | 
|  | [Constexpr lambda](https://en.cppreference.com/cpp/language/lambda) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_constexpr_201603L) | (C++17) | [P0170R1](https://wg21.link/P0170R1) | 
|  | [Virtual function](https://en.cppreference.com/cpp/language/virtual) calls in constant expressions; [`try` blocks](https://en.cppreference.com/cpp/language/try) in constexpr functions, [`dynamic_cast`](https://en.cppreference.com/cpp/language/dynamic_cast) and polymorphic [`typeid`](https://en.cppreference.com/cpp/language/typeid) in constant expressions; trivial [default initialization](https://en.cppreference.com/cpp/language/default_initialization) and [asm-declaration](https://en.cppreference.com/cpp/language/asm) in constexpr functions | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_constexpr_201907L) | (C++20) | [P1064R0](https://wg21.link/P1064R0) [P1002R1](https://wg21.link/P1002R1) [P1327R1](https://wg21.link/P1327R1) [P1331R2](https://wg21.link/P1331R2) [P1668R1](https://wg21.link/P1668R1) | 
|  | Changing the active member of a union in constant evaluation | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_constexpr_202002L) |  | [P1330R0](https://wg21.link/P1330R0) [P2493R0](https://wg21.link/P2493R0) | 
|  | Non- [literal](https://en.cppreference.com/cpp/named_req/LiteralType) variables, labels, and [`goto`](https://en.cppreference.com/cpp/language) statements in constexpr functions | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_constexpr_202110L) | (C++23) | [P2242R3](https://wg21.link/P2242R3) | 
|  | Relaxing some restrictions on [constexpr](https://en.cppreference.com/cpp/language/constexpr) functions and function templates | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_constexpr_202207L) |  | [P2448R2](https://wg21.link/P2448R2) | 
|  | Permitting static constexpr variables in constexpr functions | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_constexpr_202211L) |  | [P2647R1](https://wg21.link/P2647R1) | 
|  | Constexpr cast from `void*`: towards constexpr type-erasure | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_constexpr_202306L) | (C++26) | [P2738R1](https://wg21.link/P2738R1) | 
|  | Constexpr [placement new](https://en.cppreference.com/cpp/language/new#Placement_new) | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_constexpr_202406L) |  | [P2747R2](https://wg21.link/P2747R2) | 
| `__cpp_constexpr_dynamic_alloc` | Operations for dynamic storage duration in constexpr functions | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_constexpr_dynamic_alloc_201907L) | (C++20) | [P0784R7](https://wg21.link/P0784R7) | 
| `__cpp_constexpr_exceptions` | Constexpr [exceptions](https://en.cppreference.com/cpp/language/exceptions) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_constexpr_exceptions_202411L) | (C++26) | [P3068R6](https://wg21.link/P3068R6) | 
| `__cpp_constexpr_in_decltype` | Generation of function and variable definitions when [needed for constant evaluation](https://en.cppreference.com/cpp/language/constant_expression#Functions_and_variables_needed_for_constant_evaluation) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_constexpr_in_decltype_201711L) | (C++20) (DR11) | [P0859R0](https://wg21.link/P0859R0) | 
| `__cpp_constexpr_virtual_inheritance` | Constexpr virtual inheritance | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_constexpr_virtual_inheritance_202506L) | (C++26) | [P3533R2](https://wg21.link/P3533R2) | 
| `__cpp_constinit` | [`constinit`](https://en.cppreference.com/cpp/language/constinit) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_constinit_201907L) | (C++20) | [P1143R2](https://wg21.link/P1143R2) | 
| `__cpp_contracts` | [Contracts](https://en.cppreference.com/cpp/language/contracts) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_contracts_202502L) | (C++26) | [P2900R14](https://wg21.link/P2900R14) | 
|  | [Contracts](https://en.cppreference.com/cpp/language/contracts) for [virtual functions](https://en.cppreference.com/cpp/language/virtual) | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_contracts_202606L) | (C++29) | [P3097R3](https://wg21.link/P3097R3) | 
| `__cpp_decltype` | [`decltype`](https://en.cppreference.com/cpp/language/decltype) | [`200707L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_decltype_200707L) | (C++11) | [N2343](https://wg21.link/N2343) | 
| `__cpp_decltype_auto` | [Return type deduction for normal functions](https://en.cppreference.com/cpp/language/auto) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_decltype_auto_201304L) | (C++14) | [N3638](https://wg21.link/N3638) | 
| `__cpp_deduction_guides` | [Template argument deduction for class templates](https://en.cppreference.com/cpp/language/class_template_argument_deduction) (CTAD) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_deduction_guides_201703L) | (C++17) | [P0091R3](https://wg21.link/P0091R3) [P0512R0](https://wg21.link/P0512R0) [P0620R0](https://wg21.link/P0620R0) | 
|  | CTAD for aggregates and aliases | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_deduction_guides_201907L) | (C++20) | [P1814R0](https://wg21.link/P1814R0) [P1816R0](https://wg21.link/P1816R0) | 
| `__cpp_delegating_constructors` | [Delegating constructors](https://en.cppreference.com/cpp/language/constructor#Delegating_constructor) | [`200604L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_delegating_constructors_200604L) | (C++11) | [N1986](https://wg21.link/N1986) | 
| `__cpp_deleted_function` | Deleted [function definitions](https://en.cppreference.com/cpp/language/function) with messages (`= delete("should have a reason");`) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_deleted_function_202403L) | (C++26) | [P2573R2](https://wg21.link/P2573R2) | 
| `__cpp_designated_initializers` | [Designated initializers](https://en.cppreference.com/cpp/language/aggregate_initialization#Designated_initializer) | [`201707L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_designated_initializers_201707L) | (C++20) | [P0329R4](https://wg21.link/P0329R4) | 
|  | [Designated initializers](https://en.cppreference.com/cpp/language/initialization) for base classes | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_designated_initializers_202606L) | (C++29) | [P2287R6](https://wg21.link/P2287R6) | 
| `__cpp_enumerator_attributes` | Attributes for [enumerators](https://en.cppreference.com/cpp/language/enum) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_enumerator_attributes_201411L) | (C++17) | [N4266](https://wg21.link/N4266) | 
| `__cpp_expansion_statements` | [Expansion statements (`template for`)](https://en.cppreference.com/cpp/language/template_for) | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_expansion_statements_202506L) | (C++26) | [P1306R5](https://wg21.link/P1306R5) | 
| `__cpp_explicit_this_parameter` | [Explicit object parameter](https://en.cppreference.com/cpp/language/member_functions#Explicit_object_member_functions) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_explicit_this_parameter_202110L) | (C++23) | [P0847R7](https://wg21.link/P0847R7) | 
| `__cpp_fold_expressions` | [Fold expressions](https://en.cppreference.com/cpp/language/fold) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_fold_expressions_201603L) | (C++17) | [N4295](https://wg21.link/N4295) [P0036R0](https://wg21.link/P0036R0) | 
|  | Ordering of [constraints](https://en.cppreference.com/cpp/language/constraints) involving [fold expressions](https://en.cppreference.com/cpp/language/fold) | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_fold_expressions_202406L) | (C++26) | [P2963R3](https://wg21.link/P2963R3) | 
| `__cpp_generic_lambdas` | [Generic lambda expressions](https://en.cppreference.com/cpp/language/lambda) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_generic_lambdas_201304L) | (C++14) | [N3649](https://wg21.link/N3649) | 
|  | Explicit template parameter list for [generic lambdas](https://en.cppreference.com/cpp/language/lambda) | [`201707L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_generic_lambdas_201707L) | (C++20) | [P0428R2](https://wg21.link/P0428R2) | 
| `__cpp_guaranteed_copy_elision` | Guaranteed [copy elision](https://en.cppreference.com/cpp/language/copy_elision) through simplified [value categories](https://en.cppreference.com/cpp/language/value_category) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_guaranteed_copy_elision_201606L) | (C++17) | [P0135R1](https://wg21.link/P0135R1) | 
| `__cpp_hex_float` | [Hexadecimal floating literals](https://en.cppreference.com/cpp/language/floating_literal) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_hex_float_201603L) | (C++17) | [P0245R1](https://wg21.link/P0245R1) | 
| `__cpp_if_consteval` | [`if consteval`](https://en.cppreference.com/cpp/language/if) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_if_consteval_202106L) | (C++23) | [P1938R3](https://wg21.link/P1938R3) | 
| `__cpp_if_constexpr` | [`if constexpr`](https://en.cppreference.com/cpp/language/if) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_if_constexpr_201606L) | (C++17) | [P0292R2](https://wg21.link/P0292R2) | 
| `__cpp_impl_coroutine` | [Coroutines](https://en.cppreference.com/cpp/language/coroutines) (compiler support) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_impl_coroutine_201902L) | (C++20) | [P0912R5](https://wg21.link/P0912R5) [LWG3393](https://wg21.link/LWG3393) | 
|  | Removing mutual exclusivity for [coroutine promise return functions](https://en.cppreference.com/cpp/language/coroutines) | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_impl_coroutine_202606L) | (C++29) (DR20) | [P3950R1](https://wg21.link/P3950R1) | 
| `__cpp_impl_destroying_delete` | Destroying [`operator delete`](https://en.cppreference.com/cpp/memory/new/operator_delete) (compiler support) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_impl_destroying_delete_201806L) | (C++20) | [P0722R3](https://wg21.link/P0722R3) | 
| `__cpp_impl_reflection` | [Reflection](https://en.cppreference.com/cpp/meta/reflection) | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_impl_reflection_202506L) | (C++26) | [P2996R13](https://wg21.link/P2996R13) [P3096R12](https://wg21.link/P3096R12) [P3293R3](https://wg21.link/P3293R3) [P3394R4](https://wg21.link/P3394R4) [P3795R2](https://wg21.link/P3795R2) | 
| `__cpp_impl_three_way_comparison` | [Three-way comparison](https://en.cppreference.com/cpp/language/operator_comparison#Three-way_comparison) (compiler support) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_impl_three_way_comparison_201907L) | (C++20) | [P0515R3](https://wg21.link/P0515R3) [P0768R1](https://wg21.link/P0768R1) [P1185R2](https://wg21.link/P1185R2) [P1630R1](https://wg21.link/P1630R1) | 
| `__cpp_implicit_move` | Simpler [implicit move](https://en.cppreference.com/cpp/language/return#Automatic_move_from_local_variables_and_parameters) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_implicit_move_202207L) | (C++23) | [P2266R3](https://wg21.link/P2266R3) | 
| `__cpp_inheriting_constructors` | [Inheriting constructors](https://en.cppreference.com/cpp/language/using_declaration#Inheriting_constructors) | [`200802L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_inheriting_constructors_200802L) | (C++11) | [N2540](https://wg21.link/N2540) | 
|  | New specification for [inheriting constructors](https://en.cppreference.com/cpp/language/using_declaration#Inheriting_constructors) | [`201511L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_inheriting_constructors_201511L) | (C++17) (DR11) | [P0136R1](https://wg21.link/P0136R1) | 
| `__cpp_init_captures` | [Lambda init-capture](https://en.cppreference.com/cpp/language/lambda) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_init_captures_201304L) | (C++14) | [N3648](https://wg21.link/N3648) | 
|  | Allow pack expansion in [lambda](https://en.cppreference.com/cpp/language/lambda) init-capture | [`201803L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_init_captures_201803L) | (C++20) | [P0780R2](https://wg21.link/P0780R2) | 
| `__cpp_initializer_lists` | [List-initialization](https://en.cppreference.com/cpp/language/list_initialization) and [std::initializer\_list](https://en.cppreference.com/cpp/utility/initializer_list) | [`200806L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_initializer_lists_200806L) | (C++11) | [N2672](https://wg21.link/N2672) | 
| `__cpp_inline_variables` | [Inline variables](https://en.cppreference.com/cpp/language/inline) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_inline_variables_201606L) | (C++17) | [P0386R2](https://wg21.link/P0386R2) | 
| `__cpp_lambdas` | [Lambda expressions](https://en.cppreference.com/cpp/language/lambda) | [`200907L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_lambdas_200907L) | (C++11) | [N2927](https://wg21.link/N2927) | 
| `__cpp_modules` | [Modules](https://en.cppreference.com/cpp/language/modules) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_modules_201907L) | (C++20) | [P1103R3](https://wg21.link/P1103R3) [P1811R0](https://wg21.link/P1811R0) | 
| `__cpp_multidimensional_subscript` | Multidimensional [subscript operator](https://en.cppreference.com/cpp/language/operator_member_access) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_multidimensional_subscript_202110L) | (C++23) | [P2128R6](https://wg21.link/P2128R6) | 
|  | Static [`operator[]`](https://en.cppreference.com/cpp/language/operators) | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_multidimensional_subscript_202211L) |  | [P2589R1](https://wg21.link/P2589R1) | 
| `__cpp_named_character_escapes` | Named [universal character escapes](https://en.cppreference.com/cpp/language/escape) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_named_character_escapes_202207L) | (C++23) | [P2071R2](https://wg21.link/P2071R2) | 
| `__cpp_namespace_attributes` | [Attributes](https://en.cppreference.com/cpp/language/attributes) for [namespaces](https://en.cppreference.com/cpp/language/namespace) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_namespace_attributes_201411L) | (C++17) | [N4266](https://wg21.link/N4266) | 
| `__cpp_noexcept_function_type` | Make [exception specifications](https://en.cppreference.com/cpp/language/noexcept_spec) be part of the type system | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_noexcept_function_type_201510L) | (C++17) | [P0012R1](https://wg21.link/P0012R1) | 
| `__cpp_nontype_template_args` | Allow constant evaluation for all [non-type template arguments](https://en.cppreference.com/cpp/language/template_parameters#Template_non-type_arguments) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_nontype_template_args_201411L) | (C++17) | [N4268](https://wg21.link/N4268) | 
|  | Class types and floating-point types in [non-type template parameters](https://en.cppreference.com/cpp/language/template_parameters#Non-type_template_parameter) | [`201911L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_nontype_template_args_201911L) | (C++20) | [P1907R1](https://wg21.link/P1907R1) | 
| `__cpp_nontype_template_parameter_auto` | Declaring [non-type template parameter](https://en.cppreference.com/cpp/language/template_parameters#Non-type_template_parameter) with `auto` | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_nontype_template_parameter_auto_201606L) | (C++17) | [P0127R2](https://wg21.link/P0127R2) | 
| `__cpp_nsdmi` | [Non-static data member initializers](https://en.cppreference.com/cpp/language/data_members#Member_initialization) | [`200809L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_nsdmi_200809L) | (C++11) | [N2756](https://wg21.link/N2756) | 
| `__cpp_pack_indexing` | [Pack indexing](https://en.cppreference.com/cpp/language/pack_indexing) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_pack_indexing_202311L) | (C++26) | [P2662R3](https://wg21.link/P2662R3) | 
|  | [Pack indexing](https://en.cppreference.com/cpp/language/pack_indexing) for templates | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_pack_indexing_202606L) | (C++29) | [P3670R4](https://wg21.link/P3670R4) | 
| `__cpp_placeholder_variables` | [A nice placeholder with no name](https://en.cppreference.com/cpp/language/conflicting_declarations#Multiple_declarations_of_the_same_entity) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_placeholder_variables_202306L) | (C++26) | [P2169R4](https://wg21.link/P2169R4) | 
| `__cpp_pp_embed` | [`#embed`](https://en.cppreference.com/cpp/preprocessor/embed) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_pp_embed_202502L) | (C++26) | [P1967R14](https://wg21.link/P1967R14) | 
|  | [`#embed`](https://en.cppreference.com/cpp/preprocessor/embed) [`offset`](https://en.cppreference.com/cpp/preprocessor/embed#offset_parameter) parameter | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_pp_embed_202606L) | (C++29) | [P3540R3](https://wg21.link/P3540R3) | 
| `__cpp_range_based_for` | [Range-based `for` loop](https://en.cppreference.com/cpp/language/range-for) | [`200907L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_range_based_for_200907L) | (C++11) | [N2930](https://wg21.link/N2930) | 
|  | [Range-based `for` loop](https://en.cppreference.com/cpp/language/range-for#Explanation) with different `begin`/`end` types | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_range_based_for_201603L) | (C++17) | [P0184R0](https://wg21.link/P0184R0) | 
|  | [Lifetime extension in range-based `for`](https://en.cppreference.com/cpp/language/range-for#Temporary_range_initializer) | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_range_based_for_202211L) | (C++23) | [P2644R1](https://wg21.link/P2644R1) [P2718R0](https://wg21.link/P2718R0) [CWG2659](https://wg21.link/CWG2659) | 
| `__cpp_raw_strings` | [Raw string literals](https://en.cppreference.com/cpp/language/string_literal) | [`200710L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_raw_strings_200710L) | (C++11) | [N2442](https://wg21.link/N2442) | 
| `__cpp_ref_qualifiers` | [ref-qualifiers](https://en.cppreference.com/cpp/language/member_functions) | [`200710L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_ref_qualifiers_200710L) | (C++11) | [N2439](https://wg21.link/N2439) | 
| `__cpp_return_type_deduction` | [Return type deduction for normal functions](https://en.cppreference.com/cpp/language/auto) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_return_type_deduction_201304L) | (C++14) | [N3638](https://wg21.link/N3638) | 
| `__cpp_rvalue_references` | [Rvalue reference](https://en.cppreference.com/cpp/language/reference) | [`200610L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_rvalue_references_200610L) | (C++11) | [N2118](https://wg21.link/N2118) | 
| `__cpp_size_t_suffix` | [Literal suffixes for `std::size_t` and its signed version](https://en.cppreference.com/cpp/language/integer_literal) | [`202011L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_size_t_suffix_202011L) | (C++23) | [P0330R8](https://wg21.link/P0330R8) | 
| `__cpp_sized_deallocation` | [Sized deallocation](https://en.cppreference.com/cpp/memory/new/operator_delete) | [`201309L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_sized_deallocation_201309L) | (C++14) | [N3778](https://wg21.link/N3778) | 
| `__cpp_static_assert` | [`static_assert`](https://en.cppreference.com/cpp/language/static_assert) | [`200410L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_static_assert_200410L) | (C++11) | [N1720](https://wg21.link/N1720) | 
|  | [Single-argument `static_assert`](https://en.cppreference.com/cpp/language/static_assert) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_static_assert_201411L) | (C++17) | [N3928](https://wg21.link/N3928) | 
|  | [User-generated `static_assert` messages](https://en.cppreference.com/cpp/language/static_assert) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_static_assert_202306L) | (C++26) | [P2741R3](https://wg21.link/P2741R3) | 
| `__cpp_static_call_operator` | Static [`operator()`](https://en.cppreference.com/cpp/language/operators) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_static_call_operator_202207L) | (C++23) | [P1169R4](https://wg21.link/P1169R4) | 
| `__cpp_structured_bindings` | [Structured bindings](https://en.cppreference.com/cpp/language/structured_binding) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_structured_bindings_201606L) | (C++17) | [P0217R3](https://wg21.link/P0217R3) | 
|  | [Attributes](https://en.cppreference.com/cpp/language/attributes) for [structured binding](https://en.cppreference.com/cpp/language/structured_binding) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_structured_bindings_202403L) | (C++26) | [P0609R3](https://wg21.link/P0609R3) | 
|  | [Structured binding](https://en.cppreference.com/cpp/language/structured_binding) declaration as a condition | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_structured_bindings_202406L) |  | [P0963R3](https://wg21.link/P0963R3) | 
|  | [Structured bindings](https://en.cppreference.com/cpp/language/structured_binding) can introduce a [pack](https://en.cppreference.com/cpp/language/pack) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_structured_bindings_202411L) |  | [P1061R10](https://wg21.link/P1061R10) | 
| `__cpp_template_parameters` | Concept and variable-template template-parameters | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_template_parameters_202502L) | (C++26) | [P2841R7](https://wg21.link/P2841R7) | 
| `__cpp_template_template_args` | Matching of [template template arguments](https://en.cppreference.com/cpp/language/template_parameters#Template_template_arguments) | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_template_template_args_201611L) | (C++17) | [P0522R0](https://wg21.link/P0522R0) | 
| `__cpp_threadsafe_static_init` | [Dynamic initialization and destruction with concurrency](https://en.cppreference.com/cpp/language/storage_duration#Static_local_variables) | [`200806L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_threadsafe_static_init_200806L) | (C++11) | [N2660](https://wg21.link/N2660) | 
| `__cpp_trivial_union` | Trivial unions | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_trivial_union_202603L) | (C++26) | [P3074R7](https://wg21.link/P3074R7) [P3726R2](https://wg21.link/P3726R2) | 
| `__cpp_unicode_characters` | [New character types](https://en.cppreference.com/cpp/language/types) (char16\_t and char32\_t) | [`200704L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_unicode_characters_200704L) | (C++11) | [N2249](https://wg21.link/N2249) | 
| `__cpp_unicode_literals` | [Unicode string literals](https://en.cppreference.com/cpp/language/string_literal) | [`200710L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_unicode_literals_200710L) | (C++11) | [N2442](https://wg21.link/N2442) | 
| `__cpp_user_defined_literals` | [User-defined literals](https://en.cppreference.com/cpp/language/user_literal) | [`200809L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_user_defined_literals_200809L) | (C++11) | [N2765](https://wg21.link/N2765) | 
| `__cpp_using_enum` | [`using enum`](https://en.cppreference.com/cpp/language/enum#Using-enum-declaration) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_using_enum_201907L) | (C++20) | [P1099R5](https://wg21.link/P1099R5) | 
| `__cpp_variable_templates` | [Variable templates](https://en.cppreference.com/cpp/language/variable_template) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_variable_templates_201304L) | (C++14) | [N3651](https://wg21.link/N3651) | 
| `__cpp_variadic_friend` | Variadic [friend declarations](https://en.cppreference.com/cpp/language/friend) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_variadic_friend_202403L) | (C++26) | [P2893R3](https://wg21.link/P2893R3) | 
| `__cpp_variadic_templates` | [Variadic templates](https://en.cppreference.com/cpp/language/parameter_pack) | [`200704L`](https://en.cppreference.com/cpp/compiler_support/11#cpp_variadic_templates_200704L) | (C++11) | [N2242](https://wg21.link/N2242) | 
| `__cpp_variadic_using` | Pack expansions in [`using`-declarations](https://en.cppreference.com/cpp/language/using_declaration) | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_variadic_using_201611L) | (C++17) | [P0195R2](https://wg21.link/P0195R2) | 
| Total number of macros: 78 |  |  |  |  | 

### Library features

The following macros can be used to detect whether a standard library feature is implemented by the current implementation. Unlike the language feature test macros, they are not predefined. Instead, they are provided by the header [`<version>`](https://en.cppreference.com/cpp/header/version).

For each library feature test macro, it is also provided by the headers that provide the relevant standard library components. See [library feature test macros](https://en.cppreference.com/cpp/utility/feature_test) for a complete list of headers providing these macros.

Each macro expands to an integer literal corresponding to the year and month when the corresponding feature has been included in the working draft. When a feature changes significantly, the macro will be updated accordingly.

| Macro name | Feature | Value | Std | Paper(s) | 
|---|---|---|---|---|
| `__cpp_lib_adaptor_iterator_pair_constructor` | Iterator pair constructors for [std::stack](https://en.cppreference.com/cpp/container/stack) and [std::queue](https://en.cppreference.com/cpp/container/queue) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_adaptor_iterator_pair_constructor_202106L) | (C++23) | [P1425R4](https://wg21.link/P1425R4) | 
| `__cpp_lib_addressof_constexpr` | Constexpr [std::addressof](https://en.cppreference.com/cpp/memory/addressof) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_addressof_constexpr_201603L) | (C++17) | [LWG2296](https://wg21.link/LWG2296) | 
| `__cpp_lib_algorithm_default_value_type` | Enabling [list-initialization](https://en.cppreference.com/cpp/language/list_initialization) for [algorithms](https://en.cppreference.com/cpp/algorithm) | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_algorithm_default_value_type_202603L) | (C++26) | [P2248R8](https://wg21.link/P2248R8) [P3217R0](https://wg21.link/P3217R0) [P3787R2](https://wg21.link/P3787R2) | 
| `__cpp_lib_algorithm_iterator_requirements` | Ranges iterators as inputs to non-Ranges [algorithms](https://en.cppreference.com/cpp/algorithm) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_algorithm_iterator_requirements_202207L) | (C++23) | [P2408R5](https://wg21.link/P2408R5) | 
| `__cpp_lib_aligned_accessor` | std::aligned\_accessor: an std::mdspan accessor expressing pointer over-alignment | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_aligned_accessor_202411L) | (C++26) | [P2897R7](https://wg21.link/P2897R7) | 
| `__cpp_lib_allocate_at_least` | Size-feedback in the allocator interface, e.g.: [`std::allocator::allocate_at_least`](https://en.cppreference.com/cpp/memory/allocator/allocate_at_least), [`std::allocator_traits::allocate_at_least`](https://en.cppreference.com/cpp/memory/allocator_traits/allocate_at_least) | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_allocate_at_least_202302L) | (C++23) | [P0401R6](https://wg21.link/P0401R6) [P2652R2](https://wg21.link/P2652R2) [LWG3887](https://wg21.link/LWG3887) | 
| `__cpp_lib_allocator_traits_is_always_equal` | [`std::allocator_traits::is_always_equal`](https://en.cppreference.com/cpp/memory/allocator_traits), `noexcept` cleanups | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_allocator_traits_is_always_equal_201411L) | (C++17) | [N4258](https://wg21.link/N4258) | 
| `__cpp_lib_any` | [std::any](https://en.cppreference.com/cpp/utility/any) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_any_201606L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) [P0032R3](https://wg21.link/P0032R3) | 
| `__cpp_lib_apply` | [std::apply](https://en.cppreference.com/cpp/utility/apply) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_apply_201603L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) | 
|  | [std::apply](https://en.cppreference.com/cpp/utility/apply) changes: std::apply\_result, std::is\_applicable and std::is\_nothrow\_applicable | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_apply_202506L) | (C++26) | [P1317R2](https://wg21.link/P1317R2) | 
| `__cpp_lib_array_constexpr` | Constexpr for [std::reverse\_iterator](https://en.cppreference.com/cpp/iterator/reverse_iterator), [std::move\_iterator](https://en.cppreference.com/cpp/iterator/move_iterator), [std::array](https://en.cppreference.com/cpp/container/array) and [range access](https://en.cppreference.com/cpp/iterator#Range_access) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_array_constexpr_201603L) | (C++17) | [P0031R0](https://wg21.link/P0031R0) | 
|  | [ConstexprIterator](https://en.cppreference.com/cpp/named_req/ConstexprIterator); constexpr comparison for [std::array](https://en.cppreference.com/cpp/container/array); misc constexpr bits ([std::array::fill](https://en.cppreference.com/cpp/container/array/fill) et al.) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_array_constexpr_201811L) | (C++20) | [P0858R0](https://wg21.link/P0858R0) [LWG3257](https://wg21.link/LWG3257) [P1023R0](https://wg21.link/P1023R0) [P1032R1](https://wg21.link/P1032R1) | 
| `__cpp_lib_as_const` | [std::as\_const](https://en.cppreference.com/cpp/utility/as_const) | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_as_const_201510L) | (C++17) | [P0007R1](https://wg21.link/P0007R1) | 
| `__cpp_lib_associative_heterogeneous_erasure` | Heterogeneous erasure in [associative containers](https://en.cppreference.com/cpp/container#Associative_containers) and [unordered associative containers](https://en.cppreference.com/cpp/container#Unordered_associative_containers) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_associative_heterogeneous_erasure_202110L) | (C++23) | [P2077R3](https://wg21.link/P2077R3) | 
| `__cpp_lib_associative_heterogeneous_insertion` | Heterogeneous overloads for the remaining member functions in [ordered](https://en.cppreference.com/cpp/container#Associative_containers) and [unordered associative containers](https://en.cppreference.com/cpp/container#Unordered_associative_containers) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_associative_heterogeneous_insertion_202306L) | (C++26) | [P2363R5](https://wg21.link/P2363R5) | 
| `__cpp_lib_assume_aligned` | [std::assume\_aligned](https://en.cppreference.com/cpp/memory/assume_aligned) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_assume_aligned_201811L) | (C++20) | [P1007R3](https://wg21.link/P1007R3) | 
| `__cpp_lib_atomic_flag_test` | std::atomic\_flag::test | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_flag_test_201907L) | (C++20) | [P1135R6](https://wg21.link/P1135R6) | 
| `__cpp_lib_atomic_float` | [Floating-point atomic](https://en.cppreference.com/cpp/atomic/atomic) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_float_201711L) | (C++20) | [P0020R6](https://wg21.link/P0020R6) | 
| `__cpp_lib_atomic_is_always_lock_free` | Constexpr [`std::atomic<T>::is_always_lock_free`](https://en.cppreference.com/cpp/atomic/atomic/is_always_lock_free) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_atomic_is_always_lock_free_201603L) | (C++17) | [P0152R1](https://wg21.link/P0152R1) | 
| `__cpp_lib_atomic_lock_free_type_aliases` | Atomic lockfree integral types ( [std::atomic\_signed\_lock\_free](https://en.cppreference.com/cpp/atomic/atomic), [std::atomic\_unsigned\_lock\_free](https://en.cppreference.com/cpp/atomic/atomic)) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_lock_free_type_aliases_201907L) | (C++20) | [P1135R6](https://wg21.link/P1135R6) | 
| `__cpp_lib_atomic_min_max` | Atomic minimum/maximum ( [`std::atomic::fetch_min`](https://en.cppreference.com/cpp/atomic/atomic/fetch_min), [`std::atomic::fetch_max`](https://en.cppreference.com/cpp/atomic/atomic/fetch_max), etc) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_atomic_min_max_202403L) | (C++26) | [P0493R5](https://wg21.link/P0493R5) | 
|  | Atomic floating-point min/max | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_atomic_min_max_202506L) |  | [P3008R6](https://wg21.link/P3008R6) | 
| `__cpp_lib_atomic_reductions` | Atomic reduction operations | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_atomic_reductions_202506L) | (C++26) | [P3111R8](https://wg21.link/P3111R8) | 
| `__cpp_lib_atomic_ref` | [`std::atomic_ref`](https://en.cppreference.com/cpp/atomic/atomic_ref) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_ref_201806L) | (C++20) | [P0019R8](https://wg21.link/P0019R8) | 
|  | [`std::atomic_ref::address()`](https://en.cppreference.com/cpp/atomic/atomic_ref/address) | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_atomic_ref_202603L) | (C++26) | [P2835R7](https://wg21.link/P2835R7) [P3936R1](https://wg21.link/P3936R1) | 
| `__cpp_lib_atomic_shared_ptr` | [`std::atomic<std::shared_ptr>`](https://en.cppreference.com/cpp/memory/shared_ptr/atomic2) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_shared_ptr_201711L) | (C++20) | [P0718R2](https://wg21.link/P0718R2) | 
| `__cpp_lib_atomic_value_initialization` | Fixing atomic initialization (value-initialize [std::atomic](https://en.cppreference.com/cpp/atomic/atomic) by default) | [`201911L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_value_initialization_201911L) | (C++20) | [P0883R2](https://wg21.link/P0883R2) | 
| `__cpp_lib_atomic_wait` | Efficient [std::atomic](https://en.cppreference.com/cpp/atomic/atomic) waiting | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_atomic_wait_201907L) | (C++20) | [P1135R6](https://wg21.link/P1135R6) | 
| `__cpp_lib_barrier` | [`std::barrier`](https://en.cppreference.com/cpp/thread/barrier) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_barrier_201907L) | (C++20) | [P1135R6](https://wg21.link/P1135R6) | 
|  | [`std::barrier`](https://en.cppreference.com/cpp/thread/barrier)'s phase completion guarantees | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_barrier_202302L) | (C++23) | [P2588R3](https://wg21.link/P2588R3) | 
| `__cpp_lib_bind_back` | std::bind\_back | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_bind_back_202202L) | (C++23) | [P2387R3](https://wg21.link/P2387R3) | 
|  | Allow passing callable objects as non-type template arguments to std::bind\_back | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_bind_back_202306L) | (C++26) | [P2714R1](https://wg21.link/P2714R1) | 
| `__cpp_lib_bind_front` | [`std::bind_front`](https://en.cppreference.com/cpp/utility/functional/bind_front) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_bind_front_201907L) | (C++20) | [P0356R5](https://wg21.link/P0356R5) [P1651R0](https://wg21.link/P1651R0) | 
|  | Allow passing callable objects as non-type template arguments to [std::bind\_front](https://en.cppreference.com/cpp/utility/functional/bind_front) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_bind_front_202306L) | (C++26) | [P2714R1](https://wg21.link/P2714R1) | 
| `__cpp_lib_bit_cast` | [`std::bit_cast`](https://en.cppreference.com/cpp/numeric/bit_cast) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_bit_cast_201806L) | (C++20) | [P0476R2](https://wg21.link/P0476R2) | 
| `__cpp_lib_bitops` | [Bit operations](https://en.cppreference.com/cpp/utility/bit) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_bitops_201907L) | (C++20) | [P0553R4](https://wg21.link/P0553R4) | 
|  | [`<bit>`](https://en.cppreference.com/cpp/header/bit): bit permutations, std::shl and std::shr | [`202607L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_bitops_202607L) | (C++29) | [P3104R6](https://wg21.link/P3104R6) [P3793R2](https://wg21.link/P3793R2) | 
| `__cpp_lib_bitset` | Interfacing [std::bitset](https://en.cppreference.com/cpp/utility/bitset) with [std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_bitset_202306L) | (C++26) | [P2697R1](https://wg21.link/P2697R1) | 
| `__cpp_lib_bool_constant` | [std::bool\_constant](https://en.cppreference.com/cpp/types/integral_constant) | [`201505L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_bool_constant_201505L) | (C++17) | [N4389](https://wg21.link/N4389) | 
| `__cpp_lib_bounded_array_traits` | [`std::is_bounded_array`](https://en.cppreference.com/cpp/types/is_bounded_array), [`std::is_unbounded_array`](https://en.cppreference.com/cpp/types/is_unbounded_array) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_bounded_array_traits_201902L) | (C++20) | [P1357R1](https://wg21.link/P1357R1) | 
| `__cpp_lib_boyer_moore_searcher` | [Searchers](https://en.cppreference.com/cpp/utility/functional#Searchers) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_boyer_moore_searcher_201603L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) | 
| `__cpp_lib_byte` | [`std::byte`](https://en.cppreference.com/cpp/types/byte) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_byte_201603L) | (C++17) | [P0298R3](https://wg21.link/P0298R3) | 
| `__cpp_lib_byteswap` | [`std::byteswap`](https://en.cppreference.com/cpp/numeric/byteswap) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_byteswap_202110L) | (C++23) | [P1272R4](https://wg21.link/P1272R4) | 
| `__cpp_lib_char8_t` | Library support for [char8_t](https://en.cppreference.com/cpp/language/types#char8_t) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_char8_t_201907L) | (C++20) | [P0482R6](https://wg21.link/P0482R6) [P1423R3](https://wg21.link/P1423R3) | 
| `__cpp_lib_chrono` | Rounding functions for [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) and [std::chrono::time\_point](https://en.cppreference.com/cpp/chrono/time_point) | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_chrono_201510L) | (C++17) | [P0092R1](https://wg21.link/P0092R1) | 
|  | Constexpr for all the member functions of [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) and [std::chrono::time\_point](https://en.cppreference.com/cpp/chrono/time_point) | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_chrono_201611L) |  | [P0505R0](https://wg21.link/P0505R0) | 
|  | [Calendars](https://en.cppreference.com/cpp/chrono#Calendar) and [Time zones](https://en.cppreference.com/cpp/chrono#Time_zone) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_chrono_201907L) | (C++20) | [P0355R7](https://wg21.link/P0355R7) [P1466R3](https://wg21.link/P1466R3) | 
|  | [Hashing](https://en.cppreference.com/cpp/utility/hash) support for [`std::chrono`](https://en.cppreference.com/cpp/chrono) value classes | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_chrono_202306L) | (C++26) | [P2592R3](https://wg21.link/P2592R3) | 
| `__cpp_lib_chrono_udls` | [User-defined literals for time types](https://en.cppreference.com/cpp/chrono/duration#Literals) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_chrono_udls_201304L) | (C++14) | [N3642](https://wg21.link/N3642) | 
| `__cpp_lib_clamp` | [std::clamp](https://en.cppreference.com/cpp/algorithm/clamp) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_clamp_201603L) | (C++17) | [P0025R1](https://wg21.link/P0025R1) | 
| `__cpp_lib_common_reference` | Make std::common\_reference\_t of [std::reference\_wrapper](https://en.cppreference.com/cpp/utility/functional/reference_wrapper) a reference type | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_common_reference_202302L) | (C++23) | [P2655R3](https://wg21.link/P2655R3) | 
| `__cpp_lib_common_reference_wrapper` | Make std::common\_reference\_t of [std::reference\_wrapper](https://en.cppreference.com/cpp/utility/functional/reference_wrapper) a reference type | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_common_reference_wrapper_202302L) | (C++23) | [P2655R3](https://wg21.link/P2655R3) | 
| `__cpp_lib_complex_udls` | [User-defined Literals for `std::complex`](https://en.cppreference.com/cpp/numeric/complex/operator%22%22i) | [`201309L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_complex_udls_201309L) | (C++14) | [N3779](https://wg21.link/N3779) | 
| `__cpp_lib_concepts` | [Standard library concepts](https://en.cppreference.com/cpp/concepts) | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_concepts_202002L) | (C++20) | [P0898R3](https://wg21.link/P0898R3) [P1754R1](https://wg21.link/P1754R1) [P1964R2](https://wg21.link/P1964R2) | 
|  | Move-only types for [`equality_comparable_with`](https://en.cppreference.com/cpp/concepts/equality_comparable), [`totally_ordered_with`](https://en.cppreference.com/cpp/concepts/totally_ordered), and [`three_way_comparable_with`](https://en.cppreference.com/cpp/utility/compare/three_way_comparable) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_concepts_202207L) | (C++23) | [P2404R3](https://wg21.link/P2404R3) | 
| `__cpp_lib_constant_wrapper` | std::constant\_wrapper | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constant_wrapper_202603L) | (C++26) | [P2781R9](https://wg21.link/P2781R9) [P3978R3](https://wg21.link/P3978R3) | 
|  | Reverting string literal support in std::constant\_wrapper | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_constant_wrapper_202606L) | (C++29) (DR26) | [P4206R0](https://wg21.link/P4206R0) | 
| `__cpp_lib_constexpr_algorithms` | Constexpr for [algorithms](https://en.cppreference.com/cpp/algorithm) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_algorithms_201806L) | (C++20) | [P0202R3](https://wg21.link/P0202R3) [P0879R0](https://wg21.link/P0879R0) [LWG3256](https://wg21.link/LWG3256) [LWG3792](https://wg21.link/LWG3792) | 
|  | Constexpr stable sorting | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_algorithms_202306L) | (C++26) | [P2562R1](https://wg21.link/P2562R1) | 
| `__cpp_lib_constexpr_atomic` | Constexpr [std::atomic](https://en.cppreference.com/cpp/atomic/atomic) and std::atomic\_ref | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_atomic_202411L) | (C++26) | [P3309R3](https://wg21.link/P3309R3) | 
| `__cpp_lib_constexpr_bitset` | A more constexpr [std::bitset](https://en.cppreference.com/cpp/utility/bitset) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_constexpr_bitset_202207L) | (C++23) | [P2417R2](https://wg21.link/P2417R2) | 
| `__cpp_lib_constexpr_charconv` | Constexpr for std::to\_chars and std::from\_chars for integral types | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_constexpr_charconv_202207L) | (C++23) | [P2291R3](https://wg21.link/P2291R3) | 
| `__cpp_lib_constexpr_cmath` | Constexpr for mathematical functions in [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) and [`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_constexpr_cmath_202202L) | (C++23) | [P0533R9](https://wg21.link/P0533R9) | 
|  | More constexpr for [`<cmath>`](https://en.cppreference.com/cpp/header/cmath) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_cmath_202306L) | (C++26) | [P1383R2](https://wg21.link/P1383R2) | 
| `__cpp_lib_constexpr_complex` | Constexpr for [std::complex](https://en.cppreference.com/cpp/numeric/complex) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_complex_201711L) | (C++20) | [P0415R1](https://wg21.link/P0415R1) | 
|  | More constexpr for [`<complex>`](https://en.cppreference.com/cpp/header/complex) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_complex_202306L) | (C++26) | [P1383R2](https://wg21.link/P1383R2) | 
| `__cpp_lib_constexpr_deque` | Constexpr [std::deque](https://en.cppreference.com/cpp/container/deque) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_deque_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_dynamic_alloc` | Constexpr for [std::allocator](https://en.cppreference.com/cpp/memory/allocator) and related utilities | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_dynamic_alloc_201907L) | (C++20) | [P0784R7](https://wg21.link/P0784R7) | 
| `__cpp_lib_constexpr_exceptions` | Constexpr for exception types, e.g. [std::bad\_alloc](https://en.cppreference.com/cpp/memory/new/bad_alloc), [std::bad\_cast](https://en.cppreference.com/cpp/types/bad_cast) etc. | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_exceptions_202411L) | (C++26) | [P3068R6](https://wg21.link/P3068R6) | 
|  | Constexpr for more exception types | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_exceptions_202502L) |  | [P3378R2](https://wg21.link/P3378R2) | 
| `__cpp_lib_constexpr_flat_map` | Constexpr std::flat\_map and std::flat\_multimap | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_flat_map_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_flat_set` | Constexpr std::flat\_set and std::flat\_multiset | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_flat_set_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_format` | Constexpr text formatting | [`202511L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_format_202511L) | (C++26) | [P3391R2](https://wg21.link/P3391R2) | 
| `__cpp_lib_constexpr_forward_list` | Constexpr [std::forward\_list](https://en.cppreference.com/cpp/container/forward_list) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_forward_list_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_functional` | Misc constexpr bits ( [std::default\_searcher](https://en.cppreference.com/cpp/utility/functional/default_searcher)); constexpr `INVOKE` | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_functional_201907L) | (C++20) | [P1032R1](https://wg21.link/P1032R1) [P1065R2](https://wg21.link/P1065R2) | 
| `__cpp_lib_constexpr_inplace_vector` | Constexpr std::inplace\_vector for non-trivial types | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_inplace_vector_202502L) | (C++26) | [P3074R7](https://wg21.link/P3074R7) | 
| `__cpp_lib_constexpr_iterator` | Misc constexpr bits ( [std::insert\_iterator](https://en.cppreference.com/cpp/iterator/insert_iterator) et al.) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_iterator_201811L) | (C++20) | [P1032R1](https://wg21.link/P1032R1) | 
| `__cpp_lib_constexpr_list` | Constexpr [std::list](https://en.cppreference.com/cpp/container/list) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_list_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_map` | Constexpr [std::map](https://en.cppreference.com/cpp/container/map) and [std::multimap](https://en.cppreference.com/cpp/container/multimap) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_map_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_memory` | Constexpr in [std::pointer\_traits](https://en.cppreference.com/cpp/memory/pointer_traits) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_memory_201811L) | (C++20) | [P1006R1](https://wg21.link/P1006R1) | 
|  | Constexpr [std::unique\_ptr](https://en.cppreference.com/cpp/memory/unique_ptr) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_constexpr_memory_202202L) | (C++23) | [P2273R3](https://wg21.link/P2273R3) | 
|  | Constexpr [std::shared\_ptr](https://en.cppreference.com/cpp/memory/shared_ptr) and friends | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_memory_202506L) | (C++26) | [P3037R6](https://wg21.link/P3037R6) | 
| `__cpp_lib_constexpr_new` | Constexpr [placement `new`](https://en.cppreference.com/cpp/language/new#Placement_new) | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_new_202406L) | (C++26) | [P2747R2](https://wg21.link/P2747R2) | 
| `__cpp_lib_constexpr_numeric` | Constexpr for [algorithms](https://en.cppreference.com/cpp/algorithm#Numeric_operations) in [`<numeric>`](https://en.cppreference.com/cpp/header/numeric) | [`201911L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_numeric_201911L) | (C++20) | [P1645R1](https://wg21.link/P1645R1) | 
| `__cpp_lib_constexpr_queue` | Constexpr [std::queue](https://en.cppreference.com/cpp/container/queue) and [std::priority\_queue](https://en.cppreference.com/cpp/container/priority_queue) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_queue_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_set` | Constexpr [std::set](https://en.cppreference.com/cpp/container/set) and [std::multiset](https://en.cppreference.com/cpp/container/multiset) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_set_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_stack` | Constexpr [std::stack](https://en.cppreference.com/cpp/container/stack) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_stack_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_string` | More constexpr [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits) | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_constexpr_string_201611L) | (C++17) | [P0426R1](https://wg21.link/P0426R1) | 
|  | Fully constexpr [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_string_201811L) | (C++20) | [P1032R1](https://wg21.link/P1032R1) | 
|  | Constexpr [std::string](https://en.cppreference.com/cpp/string/basic_string) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_string_201907L) |  | [P0980R1](https://wg21.link/P0980R1) | 
| `__cpp_lib_constexpr_string_view` | Misc constexpr bits ( [std::string\_view::copy](https://en.cppreference.com/cpp/string/basic_string_view/copy)) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_string_view_201811L) | (C++20) | [P1032R1](https://wg21.link/P1032R1) | 
| `__cpp_lib_constexpr_tuple` | Misc constexpr bits ( [std::tuple::operator=](https://en.cppreference.com/cpp/utility/tuple/operator%3D) et al.) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_tuple_201811L) | (C++20) | [P1032R1](https://wg21.link/P1032R1) | 
| `__cpp_lib_constexpr_typeinfo` | Constexpr for [std::type\_info::operator==](https://en.cppreference.com/cpp/types/type_info/operator_cmp) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_constexpr_typeinfo_202106L) | (C++23) | [P1328R1](https://wg21.link/P1328R1) | 
| `__cpp_lib_constexpr_unordered_map` | Constexpr [std::unordered\_map](https://en.cppreference.com/cpp/container/unordered_map) and [std::unordered\_multimap](https://en.cppreference.com/cpp/container/unordered_multimap) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_unordered_map_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_unordered_set` | Constexpr [std::unordered\_set](https://en.cppreference.com/cpp/container/unordered_set) and [std::unordered\_multiset](https://en.cppreference.com/cpp/container/unordered_multiset) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constexpr_unordered_set_202502L) | (C++26) | [P3372R3](https://wg21.link/P3372R3) | 
| `__cpp_lib_constexpr_utility` | Misc constexpr bits ( [std::pair::operator=](https://en.cppreference.com/cpp/utility/pair/operator%3D) et al.) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_utility_201811L) | (C++20) | [P1032R1](https://wg21.link/P1032R1) | 
| `__cpp_lib_constexpr_vector` | Constexpr for [std::vector](https://en.cppreference.com/cpp/container/vector) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_constexpr_vector_201907L) | (C++20) | [P1004R2](https://wg21.link/P1004R2) | 
| `__cpp_lib_constrained_equality` | Constrained relational operators for [`std::pair`](https://en.cppreference.com/cpp/utility/pair/operator_cmp), [`std::tuple`](https://en.cppreference.com/cpp/utility/tuple/operator_cmp), [`std::optional`](https://en.cppreference.com/cpp/utility/optional/operator_cmp), and [`std::variant`](https://en.cppreference.com/cpp/utility/variant/operator_cmp) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constrained_equality_202403L) | (C++26) | [P2944R3](https://wg21.link/P2944R3) | 
|  | Constraining std::expected [equality operators](https://en.cppreference.com/cpp/utility/expected/operator_cmp) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_constrained_equality_202411L) |  | [P3379R0](https://wg21.link/P3379R0) | 
| `__cpp_lib_containers_ranges` | [Ranges-aware](https://en.cppreference.com/cpp/ranges/to#container_compatible_range) construction and insertion for containers and strings | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_containers_ranges_202202L) | (C++23) | [P1206R7](https://wg21.link/P1206R7) | 
| `__cpp_lib_contracts` | [`<contracts>`](https://en.cppreference.com/cpp/header/contracts): Contracts support | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_contracts_202502L) | (C++26) | [P2900R14](https://wg21.link/P2900R14) | 
| `__cpp_lib_copyable_function` | std::copyable\_function | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_copyable_function_202306L) | (C++26) | [P2548R6](https://wg21.link/P2548R6) | 
| `__cpp_lib_coroutine` | [Coroutines](https://en.cppreference.com/cpp/language/coroutines) (library support) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_coroutine_201902L) | (C++20) | [P0912R5](https://wg21.link/P0912R5) [LWG3393](https://wg21.link/LWG3393) | 
| `__cpp_lib_counting_scope` | Async scopes: creating scopes for non-sequential concurrency | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_counting_scope_202506L) | (C++26) | [P3149R11](https://wg21.link/P3149R11) [P3815R1](https://wg21.link/P3815R1) | 
| `__cpp_lib_debugging` | [`<debugging>`](https://en.cppreference.com/cpp/header/debugging): [Debugging support](https://en.cppreference.com/cpp/utility#Debugging_support) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_debugging_202311L) | (C++26) | [P2546R5](https://wg21.link/P2546R5) | 
|  | Replaceable [`std::is_debugger_present`](https://en.cppreference.com/cpp/utility/is_debugger_present) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_debugging_202403L) |  | [P2810R4](https://wg21.link/P2810R4) | 
| `__cpp_lib_define_static` | std::define\_static\_object, std::define\_static\_array, std::define\_static\_string | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_define_static_202506L) | (C++26) | [P3491R3](https://wg21.link/P3491R3) | 
| `__cpp_lib_destroying_delete` | Destroying [`operator delete`](https://en.cppreference.com/cpp/memory/new/operator_delete) (library support) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_destroying_delete_201806L) | (C++20) | [P0722R3](https://wg21.link/P0722R3) | 
| `__cpp_lib_enable_shared_from_this` | [std::enable\_shared\_from\_this::weak\_from\_this](https://en.cppreference.com/cpp/memory/enable_shared_from_this/weak_from_this) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_enable_shared_from_this_201603L) | (C++17) | [P0033R1](https://wg21.link/P0033R1) | 
| `__cpp_lib_endian` | std::endian | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_endian_201907L) | (C++20) | [P0463R1](https://wg21.link/P0463R1) [P1612R1](https://wg21.link/P1612R1) | 
| `__cpp_lib_erase_if` | Uniform container erasure | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_erase_if_202002L) | (C++20) | [P1209R0](https://wg21.link/P1209R0) [P1115R3](https://wg21.link/P1115R3) | 
| `__cpp_lib_exception_ptr_cast` | std::exception\_ptr\_cast() | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_exception_ptr_cast_202603L) | (C++26) | [P2927R3](https://wg21.link/P2927R3) [P3748R0](https://wg21.link/P3748R0) [P3981R2](https://wg21.link/P3981R2) | 
| `__cpp_lib_exchange_function` | [std::exchange](https://en.cppreference.com/cpp/utility/exchange) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_exchange_function_201304L) | (C++14) | [N3668](https://wg21.link/N3668) | 
| `__cpp_lib_execution` | [Execution policies](https://en.cppreference.com/cpp/algorithm#Execution_policies) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_execution_201603L) | (C++17) | [P0024R2](https://wg21.link/P0024R2) | 
|  | [`std::execution::unsequenced_policy`](https://en.cppreference.com/cpp/algorithm/execution_policy_tag_t) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_execution_201902L) | (C++20) | [P1001R2](https://wg21.link/P1001R2) | 
| `__cpp_lib_expected` | class template std::expected | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_expected_202202L) | (C++23) | [P0323R12](https://wg21.link/P0323R12) | 
|  | Monadic functions for std::expected | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_expected_202211L) |  | [P2505R5](https://wg21.link/P2505R5) | 
|  | std::expected::has\_error() | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_expected_202606L) | (C++29) | [P3798R1](https://wg21.link/P3798R1) | 
| `__cpp_lib_filesystem` | [Filesystem library](https://en.cppreference.com/cpp/filesystem) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_filesystem_201703L) | (C++17) | [P0218R1](https://wg21.link/P0218R1) [P0219R1](https://wg21.link/P0219R1) [P0392R0](https://wg21.link/P0392R0) [P0317R1](https://wg21.link/P0317R1) | 
| `__cpp_lib_flat_map` | [`std::flat_map`](https://en.cppreference.com/cpp/container/flat_map) and [`std::flat_multimap`](https://en.cppreference.com/cpp/container/flat_multimap) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_flat_map_202207L) | (C++23) | [P0429R9](https://wg21.link/P0429R9) | 
|  | [`std::flat_map`](https://en.cppreference.com/cpp/container/flat_map) and [`std::flat_multimap`](https://en.cppreference.com/cpp/container/flat_multimap) fixes | [`202511L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_flat_map_202511L) | (C++26) | [P3567R2](https://wg21.link/P3567R2) | 
| `__cpp_lib_flat_set` | [`std::flat_set`](https://en.cppreference.com/cpp/container/flat_set) and [`std::flat_multiset`](https://en.cppreference.com/cpp/container/flat_multiset) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_flat_set_202207L) | (C++23) | [P1222R4](https://wg21.link/P1222R4) [LWG3751](https://wg21.link/LWG3751) | 
|  | [`std::flat_set`](https://en.cppreference.com/cpp/container/flat_set) and [`std::flat_multiset`](https://en.cppreference.com/cpp/container/flat_multiset) fixes | [`202511L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_flat_set_202511L) | (C++26) | [P3567R2](https://wg21.link/P3567R2) | 
| `__cpp_lib_format` | [Text formatting](https://en.cppreference.com/cpp/utility/format) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_format_201907L) | (C++20) | [P0645R10](https://wg21.link/P0645R10) [P1361R2](https://wg21.link/P1361R2) [P1652R1](https://wg21.link/P1652R1) | 
|  | Compile-time format string checks; Reducing parameterization of [std::vformat\_to](https://en.cppreference.com/cpp/utility/format/vformat_to) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_format_202106L) | (C++23) (DR20) | [P2216R3](https://wg21.link/P2216R3) | 
|  | Fixing locale handling in chrono formatters; Supporting non-const-formattable types | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_format_202110L) |  | [P2372R3](https://wg21.link/P2372R3) [P2418R2](https://wg21.link/P2418R2) | 
|  | Exposing [`std::basic_format_string`](https://en.cppreference.com/cpp/utility/format/basic_format_string); clarify handling of encodings in localized formatting of chrono types | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_format_202207L) | (C++23) | [P2419R2](https://wg21.link/P2419R2) [P2508R1](https://wg21.link/P2508R1) | 
|  | Formatting pointers | [`202304L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_202304L) | (C++26) | [P2510R3](https://wg21.link/P2510R3) | 
|  | Type-checking format args | [`202305L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_202305L) |  | [P2757R3](https://wg21.link/P2757R3) | 
|  | Member [`visit`](https://en.cppreference.com/cpp/utility/format/basic_format_arg) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_202306L) |  | [P2637R3](https://wg21.link/P2637R3) | 
|  | [Runtime format strings](https://en.cppreference.com/cpp/utility/format/dynamic_format) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_202311L) |  | [P2918R2](https://wg21.link/P2918R2) | 
|  | Renaming `std::runtime_format` to std::dynamic\_format | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_202603L) |  | [P2918R2](https://wg21.link/P2918R2) | 
| `__cpp_lib_format_path` | Formatting of [std::filesystem::path](https://en.cppreference.com/cpp/filesystem/path) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_path_202403L) | (C++26) | [P2845R8](https://wg21.link/P2845R8) | 
|  | std::filesystem::path::display\_string() and std::filesystem::path::native\_encoded\_string() | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_path_202506L) |  | [P2319R5](https://wg21.link/P2319R5) | 
| `__cpp_lib_format_ranges` | Formatting ranges | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_format_ranges_202207L) | (C++23) | [P2286R8](https://wg21.link/P2286R8) [P2585R1](https://wg21.link/P2585R1) [LWG3750](https://wg21.link/LWG3750) | 
| `__cpp_lib_format_uchar` | Fix formatting of code units as integers | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_format_uchar_202311L) | (C++26) | [P2909R4](https://wg21.link/P2909R4) | 
| `__cpp_lib_formatters` | Formatting [std::thread::id](https://en.cppreference.com/cpp/thread/thread/id) and [`std::stacktrace`](https://en.cppreference.com/cpp/utility/basic_stacktrace) | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_formatters_202302L) | (C++23) | [P2693R1](https://wg21.link/P2693R1) | 
| `__cpp_lib_forward_like` | [`std::forward_like`](https://en.cppreference.com/cpp/utility/forward_like) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_forward_like_202207L) | (C++23) | [P2445R1](https://wg21.link/P2445R1) | 
| `__cpp_lib_freestanding_algorithm` | Freestanding facilities in [`<algorithm>`](https://en.cppreference.com/cpp/header/algorithm) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_algorithm_202311L) | (C++26) | [P2407R5](https://wg21.link/P2407R5) | 
|  | Freestanding library: [`<algorithm>`](https://en.cppreference.com/cpp/header/algorithm) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_algorithm_202502L) |  | [P2976R1](https://wg21.link/P2976R1) | 
| `__cpp_lib_freestanding_array` | Make parts of [std::array](https://en.cppreference.com/cpp/container/array) freestanding | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_array_202311L) | (C++26) | [P2407R5](https://wg21.link/P2407R5) | 
| `__cpp_lib_freestanding_char_traits` | Freestanding [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_char_traits_202306L) | (C++26) | [P2338R4](https://wg21.link/P2338R4) | 
| `__cpp_lib_freestanding_charconv` | Freestanding facilities in [`<charconv>`](https://en.cppreference.com/cpp/header/charconv) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_charconv_202306L) | (C++26) | [P2338R4](https://wg21.link/P2338R4) | 
| `__cpp_lib_freestanding_cstdlib` | Freestanding facilities in [`<cstdlib>`](https://en.cppreference.com/cpp/header/cstdlib) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_cstdlib_202306L) | (C++26) | [P2338R4](https://wg21.link/P2338R4) | 
| `__cpp_lib_freestanding_cstring` | Freestanding facilities in [`<cstring>`](https://en.cppreference.com/cpp/header/cstring) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_cstring_202306L) | (C++26) | [P2338R4](https://wg21.link/P2338R4) | 
|  | Removing [std::strtok](https://en.cppreference.com/cpp/string/byte/strtok) from freestanding facilities | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_cstring_202311L) |  | [P2937R0](https://wg21.link/P2937R0) | 
| `__cpp_lib_freestanding_cwchar` | Freestanding facilities in [`<cwchar>`](https://en.cppreference.com/cpp/header/cwchar) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_cwchar_202306L) | (C++26) | [P2338R4](https://wg21.link/P2338R4) | 
| `__cpp_lib_freestanding_errc` | Freestanding [std::errc](https://en.cppreference.com/cpp/error/errc) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_errc_202306L) | (C++26) | [P2338R4](https://wg21.link/P2338R4) | 
| `__cpp_lib_freestanding_execution` | Freestanding library: [`<execution>`](https://en.cppreference.com/cpp/header/execution) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_execution_202502L) | (C++26) | [P2976R1](https://wg21.link/P2976R1) | 
| `__cpp_lib_freestanding_expected` | Make parts of std::expected freestanding | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_expected_202311L) | (C++26) | [P2833R2](https://wg21.link/P2833R2) | 
| `__cpp_lib_freestanding_feature_test_macros` | Support for freestanding feature-test macros | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_feature_test_macros_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_functional` | Freestanding facilities in [`<functional>`](https://en.cppreference.com/cpp/header/functional) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_functional_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_iterator` | Freestanding facilities in [`<iterator>`](https://en.cppreference.com/cpp/header/iterator) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_iterator_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_mdspan` | Freestanding std::mdspan | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_mdspan_202311L) | (C++26) | [P2833R2](https://wg21.link/P2833R2) | 
| `__cpp_lib_freestanding_memory` | Freestanding facilities in [`<memory>`](https://en.cppreference.com/cpp/header/memory) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_memory_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
|  | Freestanding library: [`<memory>`](https://en.cppreference.com/cpp/header/memory) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_memory_202502L) |  | [P2976R1](https://wg21.link/P2976R1) | 
| `__cpp_lib_freestanding_numeric` | Freestanding facilities in [`<numeric>`](https://en.cppreference.com/cpp/header/numeric) (saturation arithmetic) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_numeric_202311L) | (C++26) | [P0543R3](https://wg21.link/P0543R3) | 
|  | Freestanding library: [`<numeric>`](https://en.cppreference.com/cpp/header/numeric) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_numeric_202502L) |  | [P2976R1](https://wg21.link/P2976R1) | 
| `__cpp_lib_freestanding_operator_new` | Definition of [operator new](https://en.cppreference.com/cpp/memory/new/operator_new) (optional in freestanding implementations) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_operator_new_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_optional` | Making parts of [std::optional](https://en.cppreference.com/cpp/utility/optional) freestanding | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_optional_202311L) | (C++26) | [P2407R5](https://wg21.link/P2407R5) | 
|  | Freestanding std::optional\<T&> | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_optional_202506L) |  | [P3836R2](https://wg21.link/P3836R2) | 
| `__cpp_lib_freestanding_random` | Freestanding library: [`<random>`](https://en.cppreference.com/cpp/header/random) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_random_202502L) | (C++26) | [P2976R1](https://wg21.link/P2976R1) | 
| `__cpp_lib_freestanding_ranges` | Freestanding facilities in [`<ranges>`](https://en.cppreference.com/cpp/header/ranges) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_ranges_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_ratio` | Freestanding facilities in [`<ratio>`](https://en.cppreference.com/cpp/header/ratio) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_ratio_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_string_view` | Making parts of [std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view) freestanding | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_string_view_202311L) | (C++26) | [P2407R5](https://wg21.link/P2407R5) | 
| `__cpp_lib_freestanding_tuple` | Freestanding facilities in [`<tuple>`](https://en.cppreference.com/cpp/header/tuple) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_tuple_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_utility` | Freestanding facilities in [`<utility>`](https://en.cppreference.com/cpp/header/utility) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_utility_202306L) | (C++26) | [P2198R7](https://wg21.link/P2198R7) | 
| `__cpp_lib_freestanding_variant` | Making parts of [std::variant](https://en.cppreference.com/cpp/utility/variant) freestanding | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_freestanding_variant_202311L) | (C++26) | [P2407R5](https://wg21.link/P2407R5) | 
| `__cpp_lib_fstream_native_handle` | Obtaining native handles from file streams | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_fstream_native_handle_202306L) | (C++26) | [P1759R6](https://wg21.link/P1759R6) | 
| `__cpp_lib_function_ref` | std::function\_ref: A type-erased callable reference | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_function_ref_202306L) | (C++26) | [P0792R14](https://wg21.link/P0792R14) | 
| `__cpp_lib_gcd_lcm` | [std::gcd](https://en.cppreference.com/cpp/numeric/gcd), [std::lcm](https://en.cppreference.com/cpp/numeric/lcm) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_gcd_lcm_201606L) | (C++17) | [P0295R0](https://wg21.link/P0295R0) | 
| `__cpp_lib_generator` | std::generator: Synchronous coroutine generator for ranges | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_generator_202207L) | (C++23) | [P2502R2](https://wg21.link/P2502R2) | 
| `__cpp_lib_generic_associative_lookup` | Heterogeneous comparison lookup in [associative containers](https://en.cppreference.com/cpp/container#Associative_containers) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_generic_associative_lookup_201304L) | (C++14) | [N3657](https://wg21.link/N3657) | 
| `__cpp_lib_generic_unordered_lookup` | Heterogeneous comparison lookup in [unordered associative containers](https://en.cppreference.com/cpp/container#Unordered_associative_containers) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_generic_unordered_lookup_201811L) | (C++20) | [P0919R3](https://wg21.link/P0919R3) | 
| `__cpp_lib_hardware_interference_size` | [`std::hardware_{constructive, destructive}_interference_size`](https://en.cppreference.com/cpp/thread/hardware_destructive_interference_size) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_hardware_interference_size_201703L) | (C++17) | [P0154R1](https://wg21.link/P0154R1) | 
| `__cpp_lib_has_unique_object_representations` | [std::has\_unique\_object\_representations](https://en.cppreference.com/cpp/types/has_unique_object_representations) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_has_unique_object_representations_201606L) | (C++17) | [P0258R2](https://wg21.link/P0258R2) | 
| `__cpp_lib_hazard_pointer` | [`<hazard_pointer>`](https://en.cppreference.com/cpp/header/hazard_pointer): Hazard pointers | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_hazard_pointer_202306L) | (C++26) | [P2530R3](https://wg21.link/P2530R3) | 
|  | Hazard pointer batches | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_hazard_pointer_202606L) | (C++29) | [P3428R4](https://wg21.link/P3428R4) | 
| `__cpp_lib_hive` | [`<hive>`](https://en.cppreference.com/cpp/header/hive): a bucket-based container that re-uses memory locations from erased elements | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_hive_202502L) | (C++26) | [P0447R28](https://wg21.link/P0447R28) | 
| `__cpp_lib_hypot` | 3-argument overload of [std::hypot](https://en.cppreference.com/cpp/numeric/math/hypot) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_hypot_201603L) | (C++17) | [P0030R1](https://wg21.link/P0030R1) | 
| `__cpp_lib_incomplete_container_elements` | Minimal incomplete type support for [`std::forward_list`](https://en.cppreference.com/cpp/container/forward_list#Template_parameters), [`std::list`](https://en.cppreference.com/cpp/container/list#Template_parameters), and [`std::vector`](https://en.cppreference.com/cpp/container/vector#Template_parameters) | [`201505L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_incomplete_container_elements_201505L) | (C++17) | [N4510](https://wg21.link/N4510) | 
| `__cpp_lib_indirect` | std::indirect | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_indirect_202502L) | (C++26) | [P3019R14](https://wg21.link/P3019R14) | 
| `__cpp_lib_initializer_list` | Resolved inconsistencies in `begin`/`end` for [std::initializer\_list](https://en.cppreference.com/cpp/utility/initializer_list) | [`202511L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_initializer_list_202511L) | (C++26) (DR11) | [P3016R6](https://wg21.link/P3016R6) | 
| `__cpp_lib_inplace_vector` | std::inplace\_vector: Dynamically-resizable vector with fixed capacity | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_inplace_vector_202406L) | (C++26) | [P0843R14](https://wg21.link/P0843R14) | 
|  | Better return types. Removed `try_append_range` member function | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_inplace_vector_202603L) |  | [P3981R2](https://wg21.link/P3981R2) [P4022R0](https://wg21.link/P4022R0) | 
| `__cpp_lib_int_pow2` | [Integral power-of-2 operations](https://en.cppreference.com/cpp/utility/bit) (std::has\_single\_bit, std::bit\_ceil, std::bit\_floor, std::bit\_width) | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_int_pow2_202002L) | (C++20) | [P0556R3](https://wg21.link/P0556R3) [P1956R1](https://wg21.link/P1956R1) | 
| `__cpp_lib_integer_comparison_functions` | [Integer comparison functions](https://en.cppreference.com/cpp/utility#Integer_comparison_functions) | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_integer_comparison_functions_202002L) | (C++20) | [P0586R2](https://wg21.link/P0586R2) | 
| `__cpp_lib_integer_sequence` | [Compile-time integer sequences](https://en.cppreference.com/cpp/utility/integer_sequence) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_integer_sequence_201304L) | (C++14) | [N3658](https://wg21.link/N3658) | 
|  | Making [std::integer\_sequence](https://en.cppreference.com/cpp/utility/integer_sequence) usable in structured bindings and expansion statements | [`202511L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_integer_sequence_202511L) | (C++26) | [P1789R3](https://wg21.link/P1789R3) | 
| `__cpp_lib_integral_constant_callable` | [std::integral\_constant::operator()](https://en.cppreference.com/cpp/types/integral_constant) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_integral_constant_callable_201304L) | (C++14) | [N3545](https://wg21.link/N3545) | 
| `__cpp_lib_interpolate` | [`std::lerp`](https://en.cppreference.com/cpp/numeric/lerp), [`std::midpoint`](https://en.cppreference.com/cpp/numeric/midpoint) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_interpolate_201902L) | (C++20) | [P0811R3](https://wg21.link/P0811R3) | 
| `__cpp_lib_invoke` | [std::invoke](https://en.cppreference.com/cpp/utility/functional/invoke) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_invoke_201411L) | (C++17) | [N4169](https://wg21.link/N4169) | 
| `__cpp_lib_invoke_r` | [`std::invoke_r`](https://en.cppreference.com/cpp/utility/functional/invoke) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_invoke_r_202106L) | (C++23) | [P2136R3](https://wg21.link/P2136R3) | 
| `__cpp_lib_ios_noreplace` | Support [exclusive mode](https://en.cppreference.com/cpp/io/ios_base/openmode) for fstreams | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ios_noreplace_202207L) | (C++23) | [P2467R1](https://wg21.link/P2467R1) | 
| `__cpp_lib_is_aggregate` | [`std::is_aggregate`](https://en.cppreference.com/cpp/types/is_aggregate) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_is_aggregate_201703L) | (C++17) | [LWG2911](https://wg21.link/LWG2911) | 
| `__cpp_lib_is_constant_evaluated` | [`std::is_constant_evaluated`](https://en.cppreference.com/cpp/types/is_constant_evaluated) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_is_constant_evaluated_201811L) | (C++20) | [P0595R2](https://wg21.link/P0595R2) | 
| `__cpp_lib_is_final` | [std::is\_final](https://en.cppreference.com/cpp/types/is_final) | [`201402L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_is_final_201402L) | (C++14) | [LWG2112](https://wg21.link/LWG2112) | 
| `__cpp_lib_is_implicit_lifetime` | [`std::is_implicit_lifetime`](https://en.cppreference.com/cpp/types/is_implicit_lifetime) | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_is_implicit_lifetime_202302L) | (C++23) | [P2674R1](https://wg21.link/P2674R1) | 
| `__cpp_lib_is_invocable` | std::is\_invocable, [std::invoke\_result](https://en.cppreference.com/cpp/types/result_of) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_is_invocable_201703L) | (C++17) | [P0604R0](https://wg21.link/P0604R0) | 
| `__cpp_lib_is_layout_compatible` | [`std::is_layout_compatible`](https://en.cppreference.com/cpp/types/is_layout_compatible) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_is_layout_compatible_201907L) | (C++20) | [P0466R5](https://wg21.link/P0466R5) | 
| `__cpp_lib_is_nothrow_convertible` | [`std::is_nothrow_convertible`](https://en.cppreference.com/cpp/types/is_convertible) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_is_nothrow_convertible_201806L) | (C++20) | [P0758R1](https://wg21.link/P0758R1) [LWG3356](https://wg21.link/LWG3356) | 
| `__cpp_lib_is_null_pointer` | [std::is\_null\_pointer](https://en.cppreference.com/cpp/types/is_null_pointer) | [`201309L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_is_null_pointer_201309L) | (C++14) (DR11) | [LWG2247](https://wg21.link/LWG2247) | 
| `__cpp_lib_is_pointer_interconvertible` | Pointer-interconvertibility traits: [`std::is_pointer_interconvertible_with_class`](https://en.cppreference.com/cpp/types/is_pointer_interconvertible_with_class), [`std::is_pointer_interconvertible_base_of`](https://en.cppreference.com/cpp/types/is_pointer_interconvertible_base_of) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_is_pointer_interconvertible_201907L) | (C++20) | [P0466R5](https://wg21.link/P0466R5) | 
| `__cpp_lib_is_scoped_enum` | [`std::is_scoped_enum`](https://en.cppreference.com/cpp/types/is_scoped_enum) | [`202011L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_is_scoped_enum_202011L) | (C++23) | [P1048R1](https://wg21.link/P1048R1) | 
| `__cpp_lib_is_structural` | std::is\_structural: type trait for detecting [structural types](https://en.cppreference.com/cpp/language/template_parameters) | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_is_structural_202603L) | (C++26) | [P3856R8](https://wg21.link/P3856R8) | 
| `__cpp_lib_is_sufficiently_aligned` | std::is\_sufficiently\_aligned: checks a pointer’s alignment precondition | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_is_sufficiently_aligned_202411L) | (C++26) | [P2897R7](https://wg21.link/P2897R7) | 
| `__cpp_lib_is_swappable` | [(nothrow-)swappable traits](https://en.cppreference.com/cpp/types/is_swappable) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_is_swappable_201603L) | (C++17) | [P0185R1](https://wg21.link/P0185R1) | 
| `__cpp_lib_is_virtual_base_of` | std::is\_virtual\_base\_of: Type trait for detecting virtual base classes | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_is_virtual_base_of_202406L) | (C++26) | [P2985R0](https://wg21.link/P2985R0) | 
| `__cpp_lib_is_within_lifetime` | Checking if a union alternative is active ( [`std::is_within_lifetime`](https://en.cppreference.com/cpp/types/is_within_lifetime)) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_is_within_lifetime_202306L) | (C++26) | [P2641R4](https://wg21.link/P2641R4) | 
|  | Extension of [`std::is_within_lifetime`](https://en.cppreference.com/cpp/types/is_within_lifetime) | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_is_within_lifetime_202603L) |  | [P3450R1](https://wg21.link/P3450R1) | 
| `__cpp_lib_jthread` | [Stop token](https://en.cppreference.com/cpp/thread/stop_token) and [joining thread](https://en.cppreference.com/cpp/thread/jthread) | [`201911L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_jthread_201911L) | (C++20) | [P0660R10](https://wg21.link/P0660R10) [P1869R1](https://wg21.link/P1869R1) | 
| `__cpp_lib_latch` | [`std::latch`](https://en.cppreference.com/cpp/thread/latch) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_latch_201907L) | (C++20) | [P1135R6](https://wg21.link/P1135R6) | 
| `__cpp_lib_launder` | [CWG issue 1776](https://cplusplus.github.io/CWG/issues/1776.html): Replacement of class objects containing reference members ([std::launder](https://en.cppreference.com/cpp/utility/launder)) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_launder_201606L) | (C++17) | [P0137R1](https://wg21.link/P0137R1) | 
| `__cpp_lib_linalg` | [A free function linear algebra interface based on the BLAS](https://en.cppreference.com/cpp/numeric/linalg) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_linalg_202311L) | (C++26) | [P1673R13](https://wg21.link/P1673R13) | 
| `__cpp_lib_list_remove_return_type` | Change the return type of the `remove()`, `remove_if()` and `unique()` of [std::forward\_list](https://en.cppreference.com/cpp/container/forward_list) and [std::list](https://en.cppreference.com/cpp/container/list) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_list_remove_return_type_201806L) | (C++20) | [P0646R1](https://wg21.link/P0646R1) | 
| `__cpp_lib_logical_traits` | [Logical operations on type traits](https://en.cppreference.com/cpp/meta#Operations_on_traits) | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_logical_traits_201510L) | (C++17) | [P0013R1](https://wg21.link/P0013R1) | 
| `__cpp_lib_make_from_tuple` | [std::make\_from\_tuple](https://en.cppreference.com/cpp/utility/make_from_tuple) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_make_from_tuple_201606L) | (C++17) | [P0209R2](https://wg21.link/P0209R2) | 
| `__cpp_lib_make_reverse_iterator` | [`std::make_reverse_iterator`](https://en.cppreference.com/cpp/iterator/make_reverse_iterator) | [`201402L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_make_reverse_iterator_201402L) | (C++14) | [LWG2285](https://wg21.link/LWG2285) | 
| `__cpp_lib_make_unique` | [std::make\_unique](https://en.cppreference.com/cpp/memory/unique_ptr/make_unique) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_make_unique_201304L) | (C++14) | [N3656](https://wg21.link/N3656) | 
| `__cpp_lib_map_lookup` | Better lookup function for map containers | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_map_lookup_202606L) | (C++29) | [P3091R6](https://wg21.link/P3091R6) | 
| `__cpp_lib_map_try_emplace` | [std::map::try\_emplace](https://en.cppreference.com/cpp/container/map/try_emplace), [std::map::insert\_or\_assign](https://en.cppreference.com/cpp/container/map/insert_or_assign) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_map_try_emplace_201411L) | (C++17) | [N4279](https://wg21.link/N4279) | 
| `__cpp_lib_math_constants` | [Mathematical constants](https://en.cppreference.com/cpp/numeric/constants) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_math_constants_201907L) | (C++20) | [P0631R8](https://wg21.link/P0631R8) | 
| `__cpp_lib_math_special_functions` | [Mathematical special functions](https://en.cppreference.com/cpp/numeric/special_functions) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_math_special_functions_201603L) | (C++17) | [P0226R1](https://wg21.link/P0226R1) | 
| `__cpp_lib_mdspan` | [`std::mdspan`](https://en.cppreference.com/cpp/container/mdspan) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_mdspan_202207L) | (C++23) | [P0009R18](https://wg21.link/P0009R18) [P2599R2](https://wg21.link/P2599R2) [P2604R0](https://wg21.link/P2604R0) [P2613R1](https://wg21.link/P2613R1) | 
|  | std::dims for std::mdspan | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_mdspan_202406L) | (C++26) | [P2389R2](https://wg21.link/P2389R2) | 
| `__cpp_lib_mdspan_copy` | std::mdspan copy and fill operations | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_mdspan_copy_202606L) | (C++29) | [P3242R4](https://wg21.link/P3242R4) | 
| `__cpp_lib_memory_resource` | [std::pmr::memory\_resource](https://en.cppreference.com/cpp/memory/memory_resource) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_memory_resource_201603L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) | 
| `__cpp_lib_modules` | [Standard library modules](https://en.cppreference.com/cpp/standard_library#Importing_modules) `std` and `std.compat` | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_modules_202207L) | (C++23) | [P2465R3](https://wg21.link/P2465R3) | 
| `__cpp_lib_move_iterator_concept` | Make [std::move\_iterator\<T\*>](https://en.cppreference.com/cpp/iterator/move_iterator) a random access iterator | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_move_iterator_concept_202207L) | (C++23) | [P2520R0](https://wg21.link/P2520R0) | 
| `__cpp_lib_move_only_function` | std::move\_only\_function | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_move_only_function_202110L) | (C++23) | [P0288R9](https://wg21.link/P0288R9) | 
| `__cpp_lib_node_extract` | Splicing maps and sets ( [std::map::extract](https://en.cppreference.com/cpp/container/map/extract), [std::map::merge](https://en.cppreference.com/cpp/container/map/merge), [`insert(node_type)`](https://en.cppreference.com/cpp/container/map/insert), etc) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_node_extract_201606L) | (C++17) | [P0083R3](https://wg21.link/P0083R3) | 
| `__cpp_lib_nonmember_container_access` | [std::size](https://en.cppreference.com/cpp/iterator/size), [std::data](https://en.cppreference.com/cpp/iterator/data) and [std::empty](https://en.cppreference.com/cpp/iterator/empty) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_nonmember_container_access_201411L) | (C++17) | [N4280](https://wg21.link/N4280) | 
| `__cpp_lib_not_fn` | [std::not\_fn](https://en.cppreference.com/cpp/utility/functional/not_fn) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_not_fn_201603L) | (C++17) | [P0005R4](https://wg21.link/P0005R4) | 
|  | Allow passing callable objects as non-type template arguments to [std::not\_fn](https://en.cppreference.com/cpp/utility/functional/not_fn) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_not_fn_202306L) | (C++26) | [P2714R1](https://wg21.link/P2714R1) | 
| `__cpp_lib_null_iterators` | Null [LegacyForwardIterators](https://en.cppreference.com/cpp/named_req/ForwardIterator) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_null_iterators_201304L) | (C++14) | [N3644](https://wg21.link/N3644) | 
| `__cpp_lib_observable_checkpoint` | Library support for observable checkpoints | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_observable_checkpoint_202506L) | (C++26) | [P1494R5](https://wg21.link/P1494R5) [P3641R0](https://wg21.link/P3641R0) | 
| `__cpp_lib_optional` | [std::optional](https://en.cppreference.com/cpp/utility/optional) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_optional_201606L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) [P0032R3](https://wg21.link/P0032R3) [P0307R2](https://wg21.link/P0307R2) | 
|  | Fully constexpr [std::optional](https://en.cppreference.com/cpp/utility/optional) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_optional_202106L) | (C++23) (DR20) | [P2231R1](https://wg21.link/P2231R1) | 
|  | [Monadic operations](https://en.cppreference.com/cpp/utility/optional#Monadic_operations) in [std::optional](https://en.cppreference.com/cpp/utility/optional) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_optional_202110L) | (C++23) | [P0798R8](https://wg21.link/P0798R8) [LWG3621](https://wg21.link/LWG3621) | 
|  | std::optional\<T&> | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_optional_202506L) | (C++26) | [P2988R12](https://wg21.link/P2988R12) | 
| `__cpp_lib_optional_range_support` | [std::optional](https://en.cppreference.com/cpp/utility/optional) range support | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_optional_range_support_202406L) | (C++26) | [P3168R2](https://wg21.link/P3168R2) | 
| `__cpp_lib_out_ptr` | std::out\_ptr, std::inout\_ptr | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_out_ptr_202106L) | (C++23) | [P1132R8](https://wg21.link/P1132R8) | 
|  | Freestanding std::out\_ptr, std::inout\_ptr | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_out_ptr_202311L) | (C++26) | [P2833R2](https://wg21.link/P2833R2) | 
| `__cpp_lib_parallel_algorithm` | [Parallel algorithms](https://en.cppreference.com/cpp/algorithm#Execution_policies) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_parallel_algorithm_201603L) | (C++17) | [P0024R2](https://wg21.link/P0024R2) | 
|  | Parallel range algorithms | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_parallel_algorithm_202506L) | (C++26) | [P3179R9](https://wg21.link/P3179R9) [P3709R2](https://wg21.link/P3709R2) | 
| `__cpp_lib_parallel_scheduler` | Parallel scheduler | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_parallel_scheduler_202506L) | (C++26) | [P2079R10](https://wg21.link/P2079R10) [P3804R2](https://wg21.link/P3804R2) | 
| `__cpp_lib_philox_engine` | std::philox\_engine: Counter-based random number engine | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_philox_engine_202406L) | (C++26) | [P2075R6](https://wg21.link/P2075R6) | 
| `__cpp_lib_pointer_tag_pair` | Pointer tagging | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_pointer_tag_pair_202606L) | (C++29) | [P3125R6](https://wg21.link/P3125R6) | 
| `__cpp_lib_polymorphic` | std::polymorphic | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_polymorphic_202502L) | (C++26) | [P3019R14](https://wg21.link/P3019R14) | 
| `__cpp_lib_polymorphic_allocator` | [std::pmr::polymorphic\_allocator\<>](https://en.cppreference.com/cpp/memory/polymorphic_allocator) as a vocabulary type | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_polymorphic_allocator_201902L) | (C++20) | [P0339R6](https://wg21.link/P0339R6) [LWG3437](https://wg21.link/LWG3437) | 
| `__cpp_lib_print` | Formatted output | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_print_202207L) | (C++23) | [P2093R14](https://wg21.link/P2093R14) | 
|  | Permit an efficient implementation of std::print | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_print_202403L) | (C++26) (DR23) | [P3107R5](https://wg21.link/P3107R5) | 
|  | std::print more types faster with less memory | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_print_202406L) |  | [P3235R3](https://wg21.link/P3235R3) | 
| `__cpp_lib_quoted_string_io` | [std::quoted](https://en.cppreference.com/cpp/io/manip/quoted) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_quoted_string_io_201304L) | (C++14) | [N3654](https://wg21.link/N3654) | 
| `__cpp_lib_ranges` | [Ranges library](https://en.cppreference.com/cpp/ranges) and [constrained algorithms](https://en.cppreference.com/cpp/algorithm/ranges) | [`201911L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_ranges_201911L) | (C++20) | [P0896R4](https://wg21.link/P0896R4) [P1035R7](https://wg21.link/P1035R7) [P1716R3](https://wg21.link/P1716R3) | 
|  | Non- [default-initializable](https://en.cppreference.com/cpp/concepts/default_initializable) [views](https://en.cppreference.com/cpp/ranges/view) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202106L) | (C++23) (DR20) | [P2325R3](https://wg21.link/P2325R3) | 
|  | [Views](https://en.cppreference.com/cpp/ranges/view) with [ownership](https://en.cppreference.com/cpp/ranges/owning_view) | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202110L) |  | [P2415R2](https://wg21.link/P2415R2) | 
|  | [`std::ranges::range_adaptor_closure`](https://en.cppreference.com/cpp/ranges/range_adaptor_closure) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202202L) | (C++23) | [P2387R3](https://wg21.link/P2387R3) | 
|  | Relaxing [range adaptors](https://en.cppreference.com/cpp/ranges) to allow for move-only types | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202207L) |  | [P2494R2](https://wg21.link/P2494R2) | 
|  | Removing “poison pill” overloads in ranges::begin, ranges::end, [ranges::rbegin](https://en.cppreference.com/cpp/ranges/rbegin), [ranges::rend](https://en.cppreference.com/cpp/ranges/rend), and [ranges::size](https://en.cppreference.com/cpp/ranges/size) | [`202211L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202211L) |  | [P2602R2](https://wg21.link/P2602R2) | 
|  | Relaxing ranges to allow certain projections | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_202302L) |  | [P2609R3](https://wg21.link/P2609R3) | 
|  | Removing the common reference requirement from the indirectly invocable concepts | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_202406L) | (C++26) (DR20) | [P2997R1](https://wg21.link/P2997R1) | 
| `__cpp_lib_ranges_as_const` | std::const\_iterator, [`std::ranges::as_const_view`](https://en.cppreference.com/cpp/ranges/as_const_view) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_as_const_202207L) | (C++23) | [P2278R4](https://wg21.link/P2278R4) | 
|  | Making std::basic\_const\_iterator follow its underlying type's convertibility | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_as_const_202311L) | (C++26) | [P2836R1](https://wg21.link/P2836R1) | 
| `__cpp_lib_ranges_as_input` | [`std::ranges::as_input_view`](https://en.cppreference.com/cpp/ranges/as_input_view) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_as_input_202502L) | (C++26) | [P3137R3](https://wg21.link/P3137R3) [P3828R1](https://wg21.link/P3828R1) | 
| `__cpp_lib_ranges_as_rvalue` | [`std::ranges::as_rvalue_view`](https://en.cppreference.com/cpp/ranges/as_rvalue_view) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_as_rvalue_202207L) | (C++23) | [P2446R2](https://wg21.link/P2446R2) | 
| `__cpp_lib_ranges_cache_latest` | [`std::ranges::cache_latest_view`](https://en.cppreference.com/cpp/ranges/cache_latest_view) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_cache_latest_202411L) | (C++26) | [P3138R5](https://wg21.link/P3138R5) | 
| `__cpp_lib_ranges_cartesian_product` | [`std::ranges::cartesian_product_view`](https://en.cppreference.com/cpp/ranges/cartesian_product_view) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_cartesian_product_202207L) | (C++23) | [P2374R4](https://wg21.link/P2374R4) [P2540R1](https://wg21.link/P2540R1) | 
| `__cpp_lib_ranges_chunk` | [`std::ranges::chunk_view`](https://en.cppreference.com/cpp/ranges/chunk_view) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_chunk_202202L) | (C++23) | [P2442R1](https://wg21.link/P2442R1) | 
| `__cpp_lib_ranges_chunk_by` | [`std::ranges::chunk_by_view`](https://en.cppreference.com/cpp/ranges/chunk_by_view) | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_chunk_by_202202L) | (C++23) | [P2443R1](https://wg21.link/P2443R1) | 
| `__cpp_lib_ranges_concat` | [`std::ranges::concat_view`](https://en.cppreference.com/cpp/ranges/concat_view) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_concat_202403L) | (C++26) | [P2542R8](https://wg21.link/P2542R8) | 
| `__cpp_lib_ranges_contains` | [`std::ranges::contains`](https://en.cppreference.com/cpp/algorithm/ranges/contains) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_contains_202207L) | (C++23) | [P2302R4](https://wg21.link/P2302R4) | 
| `__cpp_lib_ranges_enumerate` | std::ranges::enumerate\_view | [`202302L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_enumerate_202302L) | (C++23) | [P2164R9](https://wg21.link/P2164R9) | 
| `__cpp_lib_ranges_filter` | Filter view extensions for safer use | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_filter_202603L) | (C++26) (DR20) | [P3725R3](https://wg21.link/P3725R3) | 
| `__cpp_lib_ranges_find_last` | [`std::ranges::find_last`](https://en.cppreference.com/cpp/algorithm/ranges/find_last), [`std::ranges::find_last_if`](https://en.cppreference.com/cpp/algorithm/ranges/find_last), and [`std::ranges::find_last_if_not`](https://en.cppreference.com/cpp/algorithm/ranges/find_last) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_find_last_202207L) | (C++23) | [P1223R5](https://wg21.link/P1223R5) [LWG3807](https://wg21.link/LWG3807) | 
| `__cpp_lib_ranges_fold` | `std::ranges` [fold algorithms](https://en.cppreference.com/cpp/algorithm/ranges#Constrained_fold_operations) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_fold_202207L) | (C++23) | [P2322R6](https://wg21.link/P2322R6) | 
| `__cpp_lib_ranges_generate_random` | Vector API for random number generation ( [`std::ranges::generate_random`](https://en.cppreference.com/cpp/algorithm/ranges/generate_random)) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_generate_random_202403L) | (C++26) | [P1068R11](https://wg21.link/P1068R11) | 
| `__cpp_lib_ranges_indices` | std::views::indices | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_indices_202506L) | (C++26) | [P3060R3](https://wg21.link/P3060R3) | 
| `__cpp_lib_ranges_iota` | std::ranges::iota | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_iota_202202L) | (C++23) | [P2440R1](https://wg21.link/P2440R1) | 
| `__cpp_lib_ranges_join_with` | std::ranges::join\_with\_view | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_join_with_202202L) | (C++23) | [P2441R2](https://wg21.link/P2441R2) | 
| `__cpp_lib_ranges_repeat` | [`std::ranges::repeat_view`](https://en.cppreference.com/cpp/ranges/repeat_view) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_repeat_202207L) | (C++23) | [P2474R2](https://wg21.link/P2474R2) | 
| `__cpp_lib_ranges_reserve_hint` | [`std::ranges::approximately_sized_range`](https://en.cppreference.com/cpp/ranges/approximately_sized_range) and [`std::ranges::reserve_hint`](https://en.cppreference.com/cpp/ranges/reserve_hint) | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ranges_reserve_hint_202502L) | (C++26) | [P2846R6](https://wg21.link/P2846R6) | 
| `__cpp_lib_ranges_slide` | std::ranges::slide\_view | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_slide_202202L) | (C++23) | [P2442R1](https://wg21.link/P2442R1) | 
| `__cpp_lib_ranges_starts_ends_with` | std::ranges::starts\_with, std::ranges::ends\_with | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_starts_ends_with_202106L) | (C++23) | [P1659R3](https://wg21.link/P1659R3) | 
| `__cpp_lib_ranges_stride` | [`std::ranges::stride_view`](https://en.cppreference.com/cpp/ranges/stride_view) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_stride_202207L) | (C++23) | [P1899R3](https://wg21.link/P1899R3) | 
| `__cpp_lib_ranges_to_container` | std::ranges::to | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_to_container_202202L) | (C++23) | [P1206R7](https://wg21.link/P1206R7) | 
| `__cpp_lib_ranges_zip` | std::ranges::zip\_view, std::ranges::zip\_transform\_view, std::ranges::adjacent\_view, std::ranges::adjacent\_transform\_view | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_ranges_zip_202110L) | (C++23) | [P2321R2](https://wg21.link/P2321R2) | 
| `__cpp_lib_ratio` | Adding the new 2022 SI prefixes | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_ratio_202306L) | (C++26) | [P2734R0](https://wg21.link/P2734R0) | 
| `__cpp_lib_raw_memory_algorithms` | [Extending memory management tools](https://en.cppreference.com/cpp/memory#Uninitialized_storage) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_raw_memory_algorithms_201606L) | (C++17) | [P0040R3](https://wg21.link/P0040R3) | 
|  | Constexpr for [specialized memory algorithms](https://en.cppreference.com/cpp/memory#Uninitialized_memory_algorithms) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_raw_memory_algorithms_202411L) | (C++26) | [P3369R0](https://wg21.link/P3369R0) [P3508R0](https://wg21.link/P3508R0) | 
| `__cpp_lib_rcu` | [`<rcu>`](https://en.cppreference.com/cpp/header/rcu): Read-Copy Update (RCU) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_rcu_202306L) | (C++26) | [P2545R4](https://wg21.link/P2545R4) | 
| `__cpp_lib_reference_from_temporary` | std::reference\_constructs\_from\_temporary and std::reference\_converts\_from\_temporary | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_reference_from_temporary_202202L) | (C++23) | [P2255R2](https://wg21.link/P2255R2) | 
| `__cpp_lib_reference_wrapper` | Comparisons for [`std::reference_wrapper`](https://en.cppreference.com/cpp/utility/functional/reference_wrapper/operator_cmp) | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_reference_wrapper_202403L) | (C++26) | [P2944R3](https://wg21.link/P2944R3) | 
| `__cpp_lib_reflection` | [`<meta>`](https://en.cppreference.com/cpp/header/meta): Reflection | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_reflection_202506L) | (C++26) | [P2996R13](https://wg21.link/P2996R13) [P3394R4](https://wg21.link/P3394R4) [P3293R3](https://wg21.link/P3293R3) [P3096R12](https://wg21.link/P3096R12) [P3560R2](https://wg21.link/P3560R2) [P3795R2](https://wg21.link/P3795R2) [P4156R0](https://wg21.link/P4156R0) | 
| `__cpp_lib_remove_cvref` | [`std::remove_cvref`](https://en.cppreference.com/cpp/types/remove_cvref) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_remove_cvref_201711L) | (C++20) | [P0550R2](https://wg21.link/P0550R2) | 
| `__cpp_lib_replaceable_contract_violation_handler` | Implementation-defined support of replaceable contract-violation handler | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_replaceable_contract_violation_handler_202603L) | (C++26) | [P3886R0](https://wg21.link/P3886R0) | 
| `__cpp_lib_result_of_sfinae` | [std::result\_of](https://en.cppreference.com/cpp/types/result_of) and [SFINAE](https://en.cppreference.com/cpp/language/sfinae) | [`201210L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_result_of_sfinae_201210L) | (C++14) | [N3462](https://wg21.link/N3462) | 
| `__cpp_lib_robust_nonmodifying_seq_ops` | Making non-modifying sequence operations more robust (two-range overloads for [std::mismatch](https://en.cppreference.com/cpp/algorithm/mismatch), [std::equal](https://en.cppreference.com/cpp/algorithm/equal) and [std::is\_permutation](https://en.cppreference.com/cpp/algorithm/is_permutation)) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_robust_nonmodifying_seq_ops_201304L) | (C++14) | [N3671](https://wg21.link/N3671) | 
| `__cpp_lib_sample` | [std::sample](https://en.cppreference.com/cpp/algorithm/sample) | [`201603L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_sample_201603L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) | 
| `__cpp_lib_saturation_arithmetic` | [Saturation arithmetic](<https://en.cppreference.com/cpp/numeric#Saturation_arithmetic_(since_C++26)>) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_saturation_arithmetic_202311L) | (C++26) | [P0543R3](https://wg21.link/P0543R3) | 
|  | Renaming saturation arithmetic functions | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_saturation_arithmetic_202603L) | (C++26) | [P4052R0](https://wg21.link/P4052R0) | 
| `__cpp_lib_scoped_lock` | [`std::scoped_lock`](https://en.cppreference.com/cpp/thread/scoped_lock) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_scoped_lock_201703L) | (C++17) | [P0156R2](https://wg21.link/P0156R2) | 
| `__cpp_lib_semaphore` | [`std::counting_semaphore`](https://en.cppreference.com/cpp/thread/counting_semaphore), `std::binary_semaphore` | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_semaphore_201907L) | (C++20) | [P1135R6](https://wg21.link/P1135R6) | 
| `__cpp_lib_senders` | std::execution: Sender-receiver model of execution control | [`202406L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_senders_202406L) | (C++26) | [P2300R10](https://wg21.link/P2300R10) | 
|  | std::execution: More extensions | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_senders_202506L) |  | [P3388R3](https://wg21.link/P3388R3) [P3396R1](https://wg21.link/P3396R1) [P3433R1](https://wg21.link/P3433R1) [P3481R5](https://wg21.link/P3481R5) [P3570R2](https://wg21.link/P3570R2) [P3682R0](https://wg21.link/P3682R0) [P3887R1](https://wg21.link/P3887R1) | 
| `__cpp_lib_shared_mutex` | [std::shared\_mutex](https://en.cppreference.com/cpp/thread/shared_mutex) (untimed) | [`201505L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_shared_mutex_201505L) | (C++17) | [N4508](https://wg21.link/N4508) | 
| `__cpp_lib_shared_ptr_arrays` | [std::shared\_ptr\<T\[\]>](https://en.cppreference.com/cpp/memory/shared_ptr) | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_shared_ptr_arrays_201611L) | (C++17) | [P0497R0](https://wg21.link/P0497R0) | 
|  | Array support of [std::make\_shared](https://en.cppreference.com/cpp/memory/shared_ptr/make_shared) | [`201707L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_shared_ptr_arrays_201707L) | (C++20) | [P0674R1](https://wg21.link/P0674R1) | 
| `__cpp_lib_shared_ptr_weak_type` | [`shared_ptr::weak_type`](https://en.cppreference.com/cpp/memory/shared_ptr) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_shared_ptr_weak_type_201606L) | (C++17) | [P0163R0](https://wg21.link/P0163R0) | 
| `__cpp_lib_shared_timed_mutex` | [std::shared\_timed\_mutex](https://en.cppreference.com/cpp/thread/shared_timed_mutex) | [`201402L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_shared_timed_mutex_201402L) | (C++14) | [N3891](https://wg21.link/N3891) | 
| `__cpp_lib_shift` | [`std::shift_left`](https://en.cppreference.com/cpp/algorithm/shift) and [`std::shift_right`](https://en.cppreference.com/cpp/algorithm/shift) | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_shift_201806L) | (C++20) | [P0769R2](https://wg21.link/P0769R2) | 
|  | std::ranges::shift\_left and std::ranges::shift\_right | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_shift_202202L) | (C++23) | [P2440R1](https://wg21.link/P2440R1) | 
| `__cpp_lib_simd` | [`<simd>`](https://en.cppreference.com/cpp/header/simd): [Data-parallel types](https://en.cppreference.com/cpp/numeric/simd) | [`202411L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_simd_202411L) | (C++26) | [P1928R15](https://wg21.link/P1928R15) | 
|  | std::simd::iota | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_simd_202606L) | (C++29) | [P3319R6](https://wg21.link/P3319R6) | 
| `__cpp_lib_simd_bitops` | [`<simd>`](https://en.cppreference.com/cpp/header/simd): bit permutations, std::simd::shl and std::simd::shr | [`202607L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_simd_bitops_202607L) | (C++29) | [P3772R2](https://wg21.link/P3772R2) [P3793R2](https://wg21.link/P3793R2) | 
| `__cpp_lib_simd_complex` | Interleaved [std::complex](https://en.cppreference.com/cpp/numeric/complex) values support in std::simd | [`202502L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_simd_complex_202502L) | (C++26) | [P2663R7](https://wg21.link/P2663R7) | 
| `__cpp_lib_simd_permutations` | SIMD permutation operations | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_simd_permutations_202506L) | (C++26) | [P2664R11](https://wg21.link/P2664R11) | 
| `__cpp_lib_smart_ptr_for_overwrite` | Smart pointer creation with default initialization ( [std::allocate\_shared\_for\_overwrite](https://en.cppreference.com/cpp/memory/shared_ptr/allocate_shared), [std::make\_shared\_for\_overwrite](https://en.cppreference.com/cpp/memory/shared_ptr/make_shared), [std::make\_unique\_for\_overwrite](https://en.cppreference.com/cpp/memory/unique_ptr/make_unique)) | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_smart_ptr_for_overwrite_202002L) | (C++20) | [P1020R1](https://wg21.link/P1020R1) [P1973R1](https://wg21.link/P1973R1) | 
| `__cpp_lib_smart_ptr_owner_equality` | Enabling the use of [std::weak\_ptr](https://en.cppreference.com/cpp/memory/weak_ptr) as keys in [unordered associative containers](https://en.cppreference.com/cpp/container#Unordered_associative_containers) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_smart_ptr_owner_equality_202306L) | (C++26) | [P1901R2](https://wg21.link/P1901R2) | 
| `__cpp_lib_source_location` | Source-code information capture ( [std::source\_location](https://en.cppreference.com/cpp/utility/source_location)) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_source_location_201907L) | (C++20) | [P1208R6](https://wg21.link/P1208R6) | 
| `__cpp_lib_span` | [`std::span`](https://en.cppreference.com/cpp/container/span) | [`202002L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_span_202002L) | (C++20) | [P0122R7](https://wg21.link/P0122R7) [LWG3274](https://wg21.link/LWG3274) [P1024R3](https://wg21.link/P1024R3) [P1976R2](https://wg21.link/P1976R2) | 
|  | Making parts of std::span freestanding | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_span_202311L) | (C++26) | [P2821R5](https://wg21.link/P2821R5) [P2833R2](https://wg21.link/P2833R2) | 
| `__cpp_lib_spanstream` | [`std::spanbuf`](https://en.cppreference.com/cpp/io/basic_spanbuf), [`std::spanstream`](https://en.cppreference.com/cpp/io/basic_spanstream) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_spanstream_202106L) | (C++23) | [P0448R4](https://wg21.link/P0448R4) | 
| `__cpp_lib_ssize` | [`std::ssize`](https://en.cppreference.com/cpp/iterator/size) and unsigned [`std::span::size`](https://en.cppreference.com/cpp/container/span/size) | [`201902L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_ssize_201902L) | (C++20) | [P1227R2](https://wg21.link/P1227R2) | 
| `__cpp_lib_sstream_from_string_view` | Interfacing [std::stringstream](https://en.cppreference.com/cpp/io/basic_stringstream)s with [std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_sstream_from_string_view_202306L) | (C++26) | [P2495R3](https://wg21.link/P2495R3) | 
| `__cpp_lib_stacktrace` | [Stacktrace library](https://en.cppreference.com/cpp/error#Stacktrace) | [`202011L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_stacktrace_202011L) | (C++23) | [P0881R7](https://wg21.link/P0881R7) | 
| `__cpp_lib_start_lifetime` | std::start\_lifetime | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_start_lifetime_202603L) | (C++26) | [P3726R2](https://wg21.link/P3726R2) | 
| `__cpp_lib_start_lifetime_as` | Explicit lifetime management (std::start\_lifetime\_as) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_start_lifetime_as_202207L) | (C++23) | [P2590R2](https://wg21.link/P2590R2) | 
| `__cpp_lib_starts_ends_with` | String prefix and suffix checking ( `starts_with()` and `ends_with()` for [std::string](https://en.cppreference.com/cpp/string/basic_string) and [std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view)) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_starts_ends_with_201711L) | (C++20) | [P0457R2](https://wg21.link/P0457R2) | 
| `__cpp_lib_stdatomic_h` | Compatibility header [`<stdatomic.h>`](https://en.cppreference.com/cpp/header/stdatomic.h) for C atomic operations | [`202011L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_stdatomic_h_202011L) | (C++23) | [P0943R6](https://wg21.link/P0943R6) | 
| `__cpp_lib_stdbit_h` | Compatibility header [`<stdbit.h>`](https://en.cppreference.com/cpp/header/stdbit.h) for C bitwise operations | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_stdbit_h_202603L) | (C++26) | [P3370R1](https://wg21.link/P3370R1) | 
| `__cpp_lib_stdckdint_h` | Compatibility header [`<stdckdint.h>`](https://en.cppreference.com/cpp/header/stdckdint.h) for C checked integer operations | [`202603L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_stdckdint_h_202603L) | (C++26) | [P3370R1](https://wg21.link/P3370R1) | 
| `__cpp_lib_string_contains` | `contains()` for [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string) and [std::basic\_string\_view](https://en.cppreference.com/cpp/string/basic_string_view) | [`202011L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_string_contains_202011L) | (C++23) | [P1679R3](https://wg21.link/P1679R3) | 
| `__cpp_lib_string_resize_and_overwrite` | std::basic\_string::resize\_and\_overwrite | [`202110L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_string_resize_and_overwrite_202110L) | (C++23) | [P1072R10](https://wg21.link/P1072R10) | 
| `__cpp_lib_string_subview` | std::string::subview() and std::string\_view::subview() | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_string_subview_202506L) | (C++26) | [P3044R2](https://wg21.link/P3044R2) | 
| `__cpp_lib_string_udls` | [User-defined literals for string types](https://en.cppreference.com/cpp/string/basic_string/operator%22%22s) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_string_udls_201304L) | (C++14) | [N3642](https://wg21.link/N3642) | 
| `__cpp_lib_string_view` | [std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view) | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_string_view_201606L) | (C++17) | [P0220R1](https://wg21.link/P0220R1) [P0254R2](https://wg21.link/P0254R2) | 
|  | [ConstexprIterator](https://en.cppreference.com/cpp/named_req/ConstexprIterator) | [`201803L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_string_view_201803L) | (C++20) | [P0858R0](https://wg21.link/P0858R0) [LWG3257](https://wg21.link/LWG3257) | 
|  | [Concatenation](https://en.cppreference.com/cpp/string/basic_string/operator%2B) of [std::string](https://en.cppreference.com/cpp/string/basic_string)s and [std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view)s | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_string_view_202403L) | (C++26) | [P2591R5](https://wg21.link/P2591R5) | 
| `__cpp_lib_submdspan` | std::submdspan | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_submdspan_202306L) | (C++26) | [P2630R4](https://wg21.link/P2630R4) | 
|  | Padded mdspan layouts | [`202403L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_submdspan_202403L) |  | [P2642R6](https://wg21.link/P2642R6) | 
| `__cpp_lib_syncbuf` | Synchronized buffered ostream (std::syncbuf, std::osyncstream) and manipulators | [`201803L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_syncbuf_201803L) | (C++20) | [P0053R7](https://wg21.link/P0053R7) [P0753R2](https://wg21.link/P0753R2) | 
| `__cpp_lib_task` | Coroutine task types | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_task_202506L) | (C++26) | [P3552R3](https://wg21.link/P3552R3) [P3980R1](https://wg21.link/P3980R1) [P3927R2](https://wg21.link/P3927R2) [P3941R4](https://wg21.link/P3941R4) [P4151R1](https://wg21.link/P4151R1) | 
| `__cpp_lib_text_encoding` | std::text\_encoding | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_text_encoding_202306L) | (C++26) | [P1885R12](https://wg21.link/P1885R12) | 
| `__cpp_lib_thread_attributes` | Thread attributes | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_thread_attributes_202606L) | (C++29) | [P2019R9](https://wg21.link/P2019R9) | 
| `__cpp_lib_three_way_comparison` | [Three-way comparison](https://en.cppreference.com/cpp/language/operator_comparison#Three-way_comparison) (library support); adding three-way comparison to the library | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_three_way_comparison_201907L) | (C++20) | [P0768R1](https://wg21.link/P0768R1) [P1614R2](https://wg21.link/P1614R2) | 
| `__cpp_lib_to_address` | Utility to convert a pointer to a raw pointer (std::to\_address) | [`201711L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_to_address_201711L) | (C++20) | [P0653R2](https://wg21.link/P0653R2) | 
| `__cpp_lib_to_array` | [`std::to_array`](https://en.cppreference.com/cpp/container/array/to_array) | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_to_array_201907L) | (C++20) | [P0325R4](https://wg21.link/P0325R4) | 
| `__cpp_lib_to_chars` | Elementary string conversions ( [`std::to_chars`](https://en.cppreference.com/cpp/utility/to_chars), [`std::from_chars`](https://en.cppreference.com/cpp/utility/from_chars)) | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_to_chars_201611L) | (C++17) | [P0067R5](https://wg21.link/P0067R5) [P0682R1](https://wg21.link/P0682R1) [LWG3137](https://wg21.link/LWG3137) | 
|  | Testing for success or failure of [`<charconv>`](https://en.cppreference.com/cpp/header/charconv) functions | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_to_chars_202306L) | (C++26) | [P2497R0](https://wg21.link/P2497R0) | 
|  | Fixing the default floating-point representation in std::to\_chars | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_to_chars_202606L) | (C++29) (DR17) | [P3505R4](https://wg21.link/P3505R4) | 
| `__cpp_lib_to_string` | Redefining [std::to\_string](https://en.cppreference.com/cpp/string/basic_string/to_string) in terms of [std::format](https://en.cppreference.com/cpp/utility/format/format) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_to_string_202306L) | (C++26) | [P2587R3](https://wg21.link/P2587R3) | 
| `__cpp_lib_to_underlying` | [`std::to_underlying`](https://en.cppreference.com/cpp/utility/to_underlying) | [`202102L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_to_underlying_202102L) | (C++23) | [P1682R3](https://wg21.link/P1682R3) | 
| `__cpp_lib_transformation_trait_aliases` | Alias templates for [transformation traits](https://en.cppreference.com/cpp/meta#Type_transformations) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_transformation_trait_aliases_201304L) | (C++14) | [N3655](https://wg21.link/N3655) | 
| `__cpp_lib_transparent_operators` | Transparent operator functors (std::less\<> et al) | [`201210L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_transparent_operators_201210L) | (C++14) | [N3421](https://wg21.link/N3421) | 
|  | Transparent [std::owner\_less](https://en.cppreference.com/cpp/memory/owner_less) ([`std::owner_less<void>`](https://en.cppreference.com/cpp/memory/owner_less_void)) | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_transparent_operators_201510L) | (C++17) | [P0074R0](https://wg21.link/P0074R0) | 
| `__cpp_lib_tuple_element_t` | [`std::tuple_element_t`](https://en.cppreference.com/cpp/utility/tuple_element#Helper_types) | [`201402L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_tuple_element_t_201402L) | (C++14) | [N3887](https://wg21.link/N3887) | 
| `__cpp_lib_tuple_like` | Compatibility between [std::tuple](https://en.cppreference.com/cpp/utility/tuple) and tuple-like objects ([std::pair](https://en.cppreference.com/cpp/utility/pair), [std::array](https://en.cppreference.com/cpp/container/array), std::subrange) | [`202207L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_tuple_like_202207L) | (C++23) | [P2165R4](https://wg21.link/P2165R4) | 
|  | Add tuple protocol to [std::complex](https://en.cppreference.com/cpp/numeric/complex) | [`202311L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_tuple_like_202311L) | (C++26) | [P2819R2](https://wg21.link/P2819R2) | 
| `__cpp_lib_tuples_by_type` | [Addressing tuples by type](https://en.cppreference.com/cpp/utility/tuple/get) | [`201304L`](https://en.cppreference.com/cpp/compiler_support/14#cpp_lib_tuples_by_type_201304L) | (C++14) | [N3670](https://wg21.link/N3670) | 
| `__cpp_lib_type_identity` | std::type\_identity | [`201806L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_type_identity_201806L) | (C++20) | [P0887R1](https://wg21.link/P0887R1) | 
| `__cpp_lib_type_order` | Standardized constexpr type ordering | [`202506L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_type_order_202506L) | (C++26) | [P2830R10](https://wg21.link/P2830R10) [P3778R0](https://wg21.link/P3778R0) [P4140R0](https://wg21.link/P4140R0) | 
| `__cpp_lib_type_trait_variable_templates` | Type traits variable templates ( [std::is\_void\_v](https://en.cppreference.com/cpp/types/is_void), etc) | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_type_trait_variable_templates_201510L) | (C++17) | [P0006R0](https://wg21.link/P0006R0) | 
| `__cpp_lib_uncaught_exceptions` | [`std::uncaught_exceptions`](https://en.cppreference.com/cpp/error/uncaught_exception) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_uncaught_exceptions_201411L) | (C++17) | [N4259](https://wg21.link/N4259) | 
| `__cpp_lib_unordered_map_try_emplace` | [std::unordered\_map::try\_emplace](https://en.cppreference.com/cpp/container/unordered_map/try_emplace), [std::unordered\_map::insert\_or\_assign](https://en.cppreference.com/cpp/container/unordered_map/insert_or_assign) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_unordered_map_try_emplace_201411L) | (C++17) | [N4279](https://wg21.link/N4279) | 
| `__cpp_lib_unreachable` | std::unreachable | [`202202L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_unreachable_202202L) | (C++23) | [P0627R6](https://wg21.link/P0627R6) | 
| `__cpp_lib_unwrap_ref` | [std::unwrap\_ref\_decay](https://en.cppreference.com/cpp/utility/functional/unwrap_reference) and [std::unwrap\_reference](https://en.cppreference.com/cpp/utility/functional/unwrap_reference) | [`201811L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_unwrap_ref_201811L) | (C++20) | [P0318R1](https://wg21.link/P0318R1) [LWG3348](https://wg21.link/LWG3348) | 
| `__cpp_lib_valarray` | Resolving inconsistencies in `begin`/`end` for [std::valarray](https://en.cppreference.com/cpp/numeric/valarray) | [`202511L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_valarray_202511L) | (C++26) (DR11) | [P3016R6](https://wg21.link/P3016R6) | 
| `__cpp_lib_variant` | [std::variant](https://en.cppreference.com/cpp/utility/variant): A type-safe union for C++17 | [`201606L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_variant_201606L) | (C++17) | [P0088R3](https://wg21.link/P0088R3) [P0393R3](https://wg21.link/P0393R3) [P0032R3](https://wg21.link/P0032R3) | 
|  | [`std::visit`](https://en.cppreference.com/cpp/utility/variant/visit2) for classes derived from [std::variant](https://en.cppreference.com/cpp/utility/variant) | [`202102L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_variant_202102L) | (C++23) (DR17) | [P2162R2](https://wg21.link/P2162R2) | 
|  | Fully constexpr [std::variant](https://en.cppreference.com/cpp/utility/variant) | [`202106L`](https://en.cppreference.com/cpp/compiler_support/23#cpp_lib_variant_202106L) | (C++23) (DR20) | [P2231R1](https://wg21.link/P2231R1) | 
|  | Member [`visit`](https://en.cppreference.com/cpp/utility/variant/visit) | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_variant_202306L) | (C++26) | [P2637R3](https://wg21.link/P2637R3) | 
| `__cpp_lib_view_interface` | view\_interface::at() | [`202606L`](https://en.cppreference.com/cpp/compiler_support/29#cpp_lib_view_interface_202606L) | (C++29) | [P3052R2](https://wg21.link/P3052R2) | 
| `__cpp_lib_void_t` | [std::void\_t](https://en.cppreference.com/cpp/types/void_t) | [`201411L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_void_t_201411L) | (C++17) | [N3911](https://wg21.link/N3911) | 
| Total number of macros: 294 |  |  |  |  | 

### Example

#### Normal usage

```
#ifdef __has_include                           // Check if __has_include is present
#  if __has_include(<optional>)                // Check for a standard library
#    include <optional>
#  elif __has_include(<experimental/optional>) // Check for an experimental version
#    include <experimental/optional>
#  elif __has_include(<boost/optional.hpp>)    // Try with an external library
#    include <boost/optional.hpp>
#  else                                        // Not found at all
#     error "Missing <optional>"
#  endif
#endif
#ifdef __has_cpp_attribute                      // Check if __has_cpp_attribute is present
#  if __has_cpp_attribute(deprecated)           // Check for an attribute
#    define DEPRECATED(msg) [[deprecated(msg)]]
#  endif
#endif
#ifndef DEPRECATED
#    define DEPRECATED(msg)
#endif
DEPRECATED("foo() has been deprecated") void foo();
#if __cpp_constexpr >= 201304                // Check for a specific version of a feature
#  define CONSTEXPR constexpr
#else
#  define CONSTEXPR inline
#endif
CONSTEXPR int bar(unsigned i)
{
#if __cpp_binary_literals                    // Check for the presence of a feature
    unsigned mask1 = 0b11000000;
    unsigned mask2 = 0b00000111;
#else
    unsigned mask1 = 0xC0;
    unsigned mask2 = 0x07;
#endif
    if (i & mask1)
        return 1;
    if (i & mask2)
        return 2;
    return 0;
}
int main() {}
```
#### Compiler Features Dump

The following (C++11 compatible) program dumps C++ compiler features and attributes.
Note that the use of `__has_cpp_attribute()` is not [conformant](https://en.cppreference.com#Attributes) and depends on the gcc/clang implementation.

```
static constexpr struct change_these_options_to_select_what_will_be_printed
{
    constexpr static int longest_macro_name { 50 };
    constexpr static bool titles               = 1;
    constexpr static bool counters             = 1;
    constexpr static bool attributes           = 1;
    constexpr static bool standard_values      = 1;
    constexpr static bool compiler_specific    = 1;
    constexpr static bool core_features        = 1;
    constexpr static bool lib_features         = 1;
    constexpr static bool supported_features   = 1;
    constexpr static bool unsupported_features = 1;
    constexpr static bool sort_by_date         = 0;
    constexpr static bool separate_year_month  = 1;
    constexpr static bool separated_revisions  = 1;
    constexpr static bool latest_revisions     = 1;
    constexpr static bool cxx98                = 0;
    constexpr static bool cxx11                = 1;
    constexpr static bool cxx14                = 1;
    constexpr static bool cxx17                = 1;
    constexpr static bool cxx20                = 1;
    constexpr static bool cxx23                = 1;
    constexpr static bool cxx26                = 1;
    constexpr static bool cxx29                = 1;
    constexpr static bool cxx32                = 0;
} print;
#if __cplusplus < 201100
#  error "C++11 or better is required"
#endif
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>
#ifdef __has_include
# if __has_include(<version>)
#   include <version>
# endif
#endif
// Expect a string that starts with 6-decimal-digits or with '_' (if unsupported)
#define COMPILER_VALUE_INT(n) #n [0] == '_' or #n [0] == '0' ? 0 : \
    (#n[5] - '0') + (#n[4] - '0') * 10 + (#n[3] - '0') * 100 + \
    (#n[2] - '0') * 1000 + (#n[1] - '0') * 10000 + (#n[0] - '0') * 100000
#define COMPILER_FEATURE_ENTRY(expect, name) { #name, COMPILER_VALUE_INT(name), expect },
#if defined(__has_cpp_attribute) && defined(__GNUG__)
# define COMPILER_ATTRIBUTE(expect, name) { #name, __has_cpp_attribute(name), expect },
#else
# define COMPILER_ATTRIBUTE(expect, name) { #name, COMPILER_VALUE_INT(name), expect },
#endif
#define COMPILER_SPECIFIC_STRING(value) #value
#define COMPILER_SPECIFIC_ENTRY(name) { #name, COMPILER_SPECIFIC_STRING(name) },
class CompilerFeature
{
    char const* name_; long data_; long std_;
public:
    constexpr CompilerFeature(char const* name, long data, long std)
        : name_(name), data_(data), std_(std) {}
    constexpr CompilerFeature(CompilerFeature const&) = default;
    CompilerFeature& operator=(CompilerFeature const&) = default;
    bool operator<(CompilerFeature const& rhs) const
        { return std::strcmp(name_, rhs.name_) < 0; }
    bool operator==(CompilerFeature const& rhs) const
        { return std::strcmp(name_, rhs.name_) == 0; }
    constexpr bool supported() const { return data_ >= std_; }
    constexpr bool maybe() const { return data_ > 0; }
    constexpr char const* name() const { return name_; }
    constexpr long std() const { return std_; }
    constexpr long data() const { return data_; }
    void data(long x) { data_ = x; }
};
static /*constexpr*/ std::pair<const char*, const char*> compiler[] = {
    COMPILER_SPECIFIC_ENTRY(__cplusplus) //< not compiler specific, but useful :)
    COMPILER_SPECIFIC_ENTRY(__clang_major__)
    COMPILER_SPECIFIC_ENTRY(__clang_minor__)
    COMPILER_SPECIFIC_ENTRY(__clang_patchlevel__)
    COMPILER_SPECIFIC_ENTRY(__GNUG__)
    COMPILER_SPECIFIC_ENTRY(__GNUC_MINOR__)
    COMPILER_SPECIFIC_ENTRY(__GNUC_PATCHLEVEL__)
    // Add your favorite compiler specific macros. Undefined ones will not be printed.
};
static constexpr CompilerFeature cxx98_core[] = {
    COMPILER_FEATURE_ENTRY(199711L, __cpp_exceptions)
    COMPILER_FEATURE_ENTRY(199711L, __cpp_rtti)
};
static constexpr CompilerFeature cxx11_core[] = {
    COMPILER_FEATURE_ENTRY(200704L, __cpp_alias_templates)
    COMPILER_FEATURE_ENTRY(200809L, __cpp_attributes)
    COMPILER_FEATURE_ENTRY(200704L, __cpp_constexpr)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_constexpr_in_decltype)
    COMPILER_FEATURE_ENTRY(200707L, __cpp_decltype)
    COMPILER_FEATURE_ENTRY(200604L, __cpp_delegating_constructors)
    COMPILER_FEATURE_ENTRY(201511L, __cpp_inheriting_constructors)
    COMPILER_FEATURE_ENTRY(200806L, __cpp_initializer_lists)
    COMPILER_FEATURE_ENTRY(200907L, __cpp_lambdas)
    COMPILER_FEATURE_ENTRY(200809L, __cpp_nsdmi)
    COMPILER_FEATURE_ENTRY(200907L, __cpp_range_based_for)
    COMPILER_FEATURE_ENTRY(200710L, __cpp_raw_strings)
    COMPILER_FEATURE_ENTRY(200710L, __cpp_ref_qualifiers)
    COMPILER_FEATURE_ENTRY(200610L, __cpp_rvalue_references)
    COMPILER_FEATURE_ENTRY(200410L, __cpp_static_assert)
    COMPILER_FEATURE_ENTRY(200806L, __cpp_threadsafe_static_init)
    COMPILER_FEATURE_ENTRY(200704L, __cpp_unicode_characters)
    COMPILER_FEATURE_ENTRY(200710L, __cpp_unicode_literals)
    COMPILER_FEATURE_ENTRY(200809L, __cpp_user_defined_literals)
    COMPILER_FEATURE_ENTRY(200704L, __cpp_variadic_templates)
};
static constexpr CompilerFeature cxx14_core[] = {
    COMPILER_FEATURE_ENTRY(201304L, __cpp_aggregate_nsdmi)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_binary_literals)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_constexpr)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_decltype_auto)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_generic_lambdas)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_init_captures)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_return_type_deduction)
    COMPILER_FEATURE_ENTRY(201309L, __cpp_sized_deallocation)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_variable_templates)
};
static constexpr CompilerFeature cxx14_lib[] = {
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_chrono_udls)
    COMPILER_FEATURE_ENTRY(201309L, __cpp_lib_complex_udls)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_exchange_function)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_generic_associative_lookup)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_integer_sequence)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_integral_constant_callable)
    COMPILER_FEATURE_ENTRY(201402L, __cpp_lib_is_final)
    COMPILER_FEATURE_ENTRY(201309L, __cpp_lib_is_null_pointer)
    COMPILER_FEATURE_ENTRY(201402L, __cpp_lib_make_reverse_iterator)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_make_unique)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_null_iterators)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_quoted_string_io)
    COMPILER_FEATURE_ENTRY(201210L, __cpp_lib_result_of_sfinae)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_robust_nonmodifying_seq_ops)
    COMPILER_FEATURE_ENTRY(201402L, __cpp_lib_shared_timed_mutex)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_string_udls)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_transformation_trait_aliases)
    COMPILER_FEATURE_ENTRY(201210L, __cpp_lib_transparent_operators)
    COMPILER_FEATURE_ENTRY(201402L, __cpp_lib_tuple_element_t)
    COMPILER_FEATURE_ENTRY(201304L, __cpp_lib_tuples_by_type)
};
static constexpr CompilerFeature cxx17_core[] = {
    COMPILER_FEATURE_ENTRY(201603L, __cpp_aggregate_bases)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_aligned_new)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_capture_star_this)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_constexpr)
    COMPILER_FEATURE_ENTRY(201703L, __cpp_deduction_guides)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_enumerator_attributes)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_fold_expressions)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_guaranteed_copy_elision)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_hex_float)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_if_constexpr)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_inline_variables)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_namespace_attributes)
    COMPILER_FEATURE_ENTRY(201510L, __cpp_noexcept_function_type)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_nontype_template_args)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_nontype_template_parameter_auto)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_range_based_for)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_static_assert)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_structured_bindings)
    COMPILER_FEATURE_ENTRY(201611L, __cpp_template_template_args)
    COMPILER_FEATURE_ENTRY(201611L, __cpp_variadic_using)
};
static constexpr CompilerFeature cxx17_lib[] = {
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_addressof_constexpr)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_allocator_traits_is_always_equal)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_any)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_apply)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_array_constexpr)
    COMPILER_FEATURE_ENTRY(201510L, __cpp_lib_as_const)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_atomic_is_always_lock_free)
    COMPILER_FEATURE_ENTRY(201505L, __cpp_lib_bool_constant)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_boyer_moore_searcher)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_byte)
    COMPILER_FEATURE_ENTRY(201611L, __cpp_lib_chrono)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_clamp)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_enable_shared_from_this)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_execution)
    COMPILER_FEATURE_ENTRY(201703L, __cpp_lib_filesystem)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_gcd_lcm)
    COMPILER_FEATURE_ENTRY(201703L, __cpp_lib_hardware_interference_size)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_has_unique_object_representations)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_hypot)
    COMPILER_FEATURE_ENTRY(201505L, __cpp_lib_incomplete_container_elements)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_invoke)
    COMPILER_FEATURE_ENTRY(201703L, __cpp_lib_is_aggregate)
    COMPILER_FEATURE_ENTRY(201703L, __cpp_lib_is_invocable)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_is_swappable)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_launder)
    COMPILER_FEATURE_ENTRY(201510L, __cpp_lib_logical_traits)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_make_from_tuple)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_map_try_emplace)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_math_special_functions)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_memory_resource)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_node_extract)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_nonmember_container_access)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_not_fn)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_optional)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_parallel_algorithm)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_raw_memory_algorithms)
    COMPILER_FEATURE_ENTRY(201603L, __cpp_lib_sample)
    COMPILER_FEATURE_ENTRY(201703L, __cpp_lib_scoped_lock)
    COMPILER_FEATURE_ENTRY(201505L, __cpp_lib_shared_mutex)
    COMPILER_FEATURE_ENTRY(201611L, __cpp_lib_shared_ptr_arrays)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_shared_ptr_weak_type)
    COMPILER_FEATURE_ENTRY(201606L, __cpp_lib_string_view)
    COMPILER_FEATURE_ENTRY(201611L, __cpp_lib_to_chars)
    COMPILER_FEATURE_ENTRY(201510L, __cpp_lib_transparent_operators)
    COMPILER_FEATURE_ENTRY(201510L, __cpp_lib_type_trait_variable_templates)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_uncaught_exceptions)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_unordered_map_try_emplace)
    COMPILER_FEATURE_ENTRY(202102L, __cpp_lib_variant)
    COMPILER_FEATURE_ENTRY(201411L, __cpp_lib_void_t)
};
static constexpr CompilerFeature cxx20_core[] = {
    COMPILER_FEATURE_ENTRY(201902L, __cpp_aggregate_paren_init)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_char8_t)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_concepts)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_conditional_explicit)
    COMPILER_FEATURE_ENTRY(202211L, __cpp_consteval)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_constexpr)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_constexpr_dynamic_alloc)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_constinit)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_deduction_guides)
    COMPILER_FEATURE_ENTRY(201707L, __cpp_designated_initializers)
    COMPILER_FEATURE_ENTRY(201707L, __cpp_generic_lambdas)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_impl_coroutine)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_impl_destroying_delete)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_impl_three_way_comparison)
    COMPILER_FEATURE_ENTRY(201803L, __cpp_init_captures)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_modules)
    COMPILER_FEATURE_ENTRY(201911L, __cpp_nontype_template_args)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_using_enum)
};
static constexpr CompilerFeature cxx20_lib[] = {
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_array_constexpr)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_assume_aligned)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_atomic_flag_test)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_lib_atomic_float)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_atomic_lock_free_type_aliases)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_atomic_ref)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_lib_atomic_shared_ptr)
    COMPILER_FEATURE_ENTRY(201911L, __cpp_lib_atomic_value_initialization)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_atomic_wait)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_barrier)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_bind_front)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_bit_cast)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_bitops)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_lib_bounded_array_traits)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_char8_t)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_chrono)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_lib_concepts)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_constexpr_algorithms)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_lib_constexpr_complex)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_constexpr_dynamic_alloc)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_constexpr_functional)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_constexpr_iterator)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_constexpr_memory)
    COMPILER_FEATURE_ENTRY(201911L, __cpp_lib_constexpr_numeric)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_constexpr_string)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_constexpr_string_view)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_constexpr_tuple)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_constexpr_utility)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_constexpr_vector)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_lib_coroutine)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_destroying_delete)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_endian)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_lib_erase_if)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_lib_execution)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_format)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_generic_unordered_lookup)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_lib_int_pow2)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_lib_integer_comparison_functions)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_lib_interpolate)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_is_constant_evaluated)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_is_layout_compatible)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_is_nothrow_convertible)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_is_pointer_interconvertible)
    COMPILER_FEATURE_ENTRY(201911L, __cpp_lib_jthread)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_latch)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_list_remove_return_type)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_math_constants)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_optional)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_lib_polymorphic_allocator)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_ranges)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_lib_remove_cvref)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_semaphore)
    COMPILER_FEATURE_ENTRY(201707L, __cpp_lib_shared_ptr_arrays)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_shift)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_lib_smart_ptr_for_overwrite)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_source_location)
    COMPILER_FEATURE_ENTRY(202002L, __cpp_lib_span)
    COMPILER_FEATURE_ENTRY(201902L, __cpp_lib_ssize)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_lib_starts_ends_with)
    COMPILER_FEATURE_ENTRY(201803L, __cpp_lib_string_view)
    COMPILER_FEATURE_ENTRY(201803L, __cpp_lib_syncbuf)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_three_way_comparison)
    COMPILER_FEATURE_ENTRY(201711L, __cpp_lib_to_address)
    COMPILER_FEATURE_ENTRY(201907L, __cpp_lib_to_array)
    COMPILER_FEATURE_ENTRY(201806L, __cpp_lib_type_identity)
    COMPILER_FEATURE_ENTRY(201811L, __cpp_lib_unwrap_ref)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_variant)
};
static constexpr CompilerFeature cxx23_core[] = {
    COMPILER_FEATURE_ENTRY(202110L, __cpp_auto_cast)
    COMPILER_FEATURE_ENTRY(202211L, __cpp_constexpr)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_explicit_this_parameter)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_if_consteval)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_implicit_move)
    COMPILER_FEATURE_ENTRY(202211L, __cpp_multidimensional_subscript)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_named_character_escapes)
    COMPILER_FEATURE_ENTRY(202211L, __cpp_range_based_for)
    COMPILER_FEATURE_ENTRY(202011L, __cpp_size_t_suffix)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_static_call_operator)
};
static constexpr CompilerFeature cxx23_lib[] = {
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_adaptor_iterator_pair_constructor)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_algorithm_iterator_requirements)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_allocate_at_least)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_associative_heterogeneous_erasure)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_barrier)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_bind_back)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_byteswap)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_common_reference)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_common_reference_wrapper)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_concepts)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_constexpr_bitset)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_constexpr_charconv)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_constexpr_cmath)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_constexpr_memory)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_constexpr_typeinfo)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_containers_ranges)
    COMPILER_FEATURE_ENTRY(202211L, __cpp_lib_expected)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_flat_map)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_flat_set)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_format)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_format_ranges)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_formatters)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_forward_like)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_generator)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_invoke_r)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ios_noreplace)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_is_implicit_lifetime)
    COMPILER_FEATURE_ENTRY(202011L, __cpp_lib_is_scoped_enum)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_mdspan)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_modules)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_move_iterator_concept)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_move_only_function)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_optional)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_out_ptr)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_print)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_ranges)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_as_const)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_as_rvalue)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_cartesian_product)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_ranges_chunk)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_ranges_chunk_by)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_contains)
    COMPILER_FEATURE_ENTRY(202302L, __cpp_lib_ranges_enumerate)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_find_last)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_fold)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_ranges_iota)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_ranges_join_with)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_repeat)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_ranges_slide)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_ranges_starts_ends_with)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_ranges_stride)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_ranges_to_container)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_ranges_zip)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_reference_from_temporary)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_shift)
    COMPILER_FEATURE_ENTRY(202106L, __cpp_lib_spanstream)
    COMPILER_FEATURE_ENTRY(202011L, __cpp_lib_stacktrace)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_start_lifetime_as)
    COMPILER_FEATURE_ENTRY(202011L, __cpp_lib_stdatomic_h)
    COMPILER_FEATURE_ENTRY(202011L, __cpp_lib_string_contains)
    COMPILER_FEATURE_ENTRY(202110L, __cpp_lib_string_resize_and_overwrite)
    COMPILER_FEATURE_ENTRY(202102L, __cpp_lib_to_underlying)
    COMPILER_FEATURE_ENTRY(202207L, __cpp_lib_tuple_like)
    COMPILER_FEATURE_ENTRY(202202L, __cpp_lib_unreachable)
};
static constexpr CompilerFeature cxx26_core[] = {
    COMPILER_FEATURE_ENTRY(202406L, __cpp_constexpr)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_constexpr_exceptions)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_constexpr_virtual_inheritance)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_contracts)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_deleted_function)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_expansion_statements)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_fold_expressions)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_impl_reflection)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_pack_indexing)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_placeholder_variables)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_pp_embed)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_static_assert)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_structured_bindings)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_template_parameters)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_trivial_union)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_variadic_friend)
};
static constexpr CompilerFeature cxx26_lib[] = {
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_algorithm_default_value_type)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_lib_aligned_accessor)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_apply)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_associative_heterogeneous_insertion)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_atomic_min_max)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_atomic_reductions)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_atomic_ref)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_bind_back)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_bind_front)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_bitset)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_chrono)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_constant_wrapper)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_constexpr_algorithms)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_lib_constexpr_atomic)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_constexpr_cmath)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_constexpr_complex)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_deque)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_exceptions)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_flat_map)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_flat_set)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_constexpr_format)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_forward_list)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_inplace_vector)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_list)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_map)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_constexpr_memory)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_lib_constexpr_new)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_queue)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_set)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_stack)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_unordered_map)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_constexpr_unordered_set)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_lib_constrained_equality)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_contracts)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_copyable_function)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_counting_scope)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_lib_debugging)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_define_static)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_exception_ptr_cast)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_flat_map)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_flat_set)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_format)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_format_path)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_format_uchar)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_freestanding_algorithm)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_freestanding_array)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_char_traits)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_charconv)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_cstdlib)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_freestanding_cstring)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_cwchar)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_errc)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_freestanding_execution)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_freestanding_expected)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_feature_test_macros)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_functional)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_iterator)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_freestanding_mdspan)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_freestanding_memory)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_freestanding_numeric)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_operator_new)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_freestanding_optional)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_freestanding_random)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_ranges)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_ratio)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_freestanding_string_view)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_tuple)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_freestanding_utility)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_freestanding_variant)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_fstream_native_handle)
    COMPILER_FEATURE_ENTRY(202604L, __cpp_lib_function_ref)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_hazard_pointer)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_hive)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_indirect)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_initializer_list)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_inplace_vector)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_integer_sequence)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_is_structural)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_lib_is_sufficiently_aligned)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_lib_is_virtual_base_of)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_is_within_lifetime)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_linalg)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_lib_mdspan)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_not_fn)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_observable_checkpoint)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_optional)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_lib_optional_range_support)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_out_ptr)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_parallel_algorithm)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_parallel_scheduler)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_lib_philox_engine)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_polymorphic)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_lib_print)
    COMPILER_FEATURE_ENTRY(202406L, __cpp_lib_ranges)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_ranges_as_const)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_ranges_as_input)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_lib_ranges_cache_latest)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_lib_ranges_concat)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_ranges_filter)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_lib_ranges_generate_random)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_ranges_indices)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_ranges_reserve_hint)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_ratio)
    COMPILER_FEATURE_ENTRY(202411L, __cpp_lib_raw_memory_algorithms)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_rcu)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_lib_reference_wrapper)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_reflection)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_replaceable_contract_violation_handler)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_saturation_arithmetic)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_senders)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_simd)
    COMPILER_FEATURE_ENTRY(202502L, __cpp_lib_simd_complex)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_simd_permutations)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_smart_ptr_owner_equality)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_span)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_sstream_from_string_view)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_start_lifetime)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_stdbit_h)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_stdckdint_h)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_string_subview)
    COMPILER_FEATURE_ENTRY(202403L, __cpp_lib_string_view)
    COMPILER_FEATURE_ENTRY(202603L, __cpp_lib_submdspan)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_task)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_text_encoding)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_to_chars)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_to_string)
    COMPILER_FEATURE_ENTRY(202311L, __cpp_lib_tuple_like)
    COMPILER_FEATURE_ENTRY(202506L, __cpp_lib_type_order)
    COMPILER_FEATURE_ENTRY(202511L, __cpp_lib_valarray)
    COMPILER_FEATURE_ENTRY(202306L, __cpp_lib_variant)
};
static constexpr CompilerFeature cxx29_core[] = {
    //< Continue to Populate
    COMPILER_FEATURE_ENTRY(202606L, __cpp_concepts)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_consteval)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_contracts)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_designated_initializers)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_impl_coroutine)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_pack_indexing)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_pp_embed)
};
static constexpr CompilerFeature cxx29_lib[] = {
    //< Continue to Populate
    COMPILER_FEATURE_ENTRY(202607L, __cpp_lib_bitops)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_constant_wrapper)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_expected)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_hazard_pointer)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_map_lookup)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_mdspan_copy)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_pointer_tag_pair)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_simd)
    COMPILER_FEATURE_ENTRY(202607L, __cpp_lib_simd_bitops)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_thread_attributes)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_to_chars)
    COMPILER_FEATURE_ENTRY(202606L, __cpp_lib_view_interface)
};
static constexpr CompilerFeature cxx32_core[] = {
    //< Continue to Populate
    COMPILER_FEATURE_ENTRY(202906L, __cpp_core_TODO)
};
static constexpr CompilerFeature cxx32_lib[] = {
    //< Continue to Populate
    COMPILER_FEATURE_ENTRY(202906L, __cpp_lib_TODO)
};
static constexpr CompilerFeature attributes[] = {
    COMPILER_ATTRIBUTE(202207L, assume)
    COMPILER_ATTRIBUTE(200809L, carries_dependency)
    COMPILER_ATTRIBUTE(201309L, deprecated)
    COMPILER_ATTRIBUTE(201603L, fallthrough)
    COMPILER_ATTRIBUTE(202403L, indeterminate)
    COMPILER_ATTRIBUTE(201803L, likely)
    COMPILER_ATTRIBUTE(201603L, maybe_unused)
    COMPILER_ATTRIBUTE(201803L, no_unique_address)
    COMPILER_ATTRIBUTE(201907L, nodiscard)
    COMPILER_ATTRIBUTE(200809L, noreturn)
    COMPILER_ATTRIBUTE(201803L, unlikely)
};
inline void show_compiler_specific_info()
{
    std::printf("Compiler specific macros:\n");
    for (auto co : compiler)
        if (std::strcmp(co.first, co.second))
            std::printf("%*s %s\n", -print.longest_macro_name, co.first, co.second);
}
inline void print_compiler_feature(const CompilerFeature& x)
{
    if (not ((print.supported_features and x.maybe()) or
            (print.unsupported_features and not x.maybe())))
        return;
    auto print_year_month = [](long n)
    {
        return std::printf("%ld%s%02ld",
            n / 100, print.separate_year_month ? "-" : "", n % 100);
    };
    std::printf("%*s ", -print.longest_macro_name, x.name());
    x.maybe() ? print_year_month(x.data()) :
                    std::printf("------%s", print.separate_year_month ? "-" : "");
    if (print.standard_values)
        std::printf("  %c  ", (x.supported() ? (x.data() > x.std() ? '>' : '=') : '<')),
            print_year_month(x.std());
    std::puts("");
}
template<class Container>
inline void show(char const* const title, Container const& co)
{
    if (print.titles)
    {
        std::printf("%-s (", title);
        if (print.counters)
        {
            std::printf("%zd/", std::count_if(std::begin(co), std::end(co),
                [](CompilerFeature x)
                {
                    return x.supported();
                }));
        }
        std::printf("%td)\n", std::distance(std::begin(co), std::end(co)));
    }
    if (print.sort_by_date)
    {
        std::vector<CompilerFeature> v(std::begin(co), std::end(co));
        std::stable_sort(v.begin(), v.end(),
            [](CompilerFeature const& lhs, CompilerFeature const& rhs)
            {
                return lhs.data() < rhs.data();
            });
        std::for_each(v.cbegin(), v.cend(), print_compiler_feature);
    }
    else
        std::for_each(std::begin(co), std::end(co), print_compiler_feature);
    std::puts("");
}
#define CXX(R) print.cxx##R ? R :
#define CORE(R) if (print.cxx##R) std::for_each( \
    std::begin(cxx##R##_core), std::end(cxx##R##_core), add);
#define LIB(R) if (print.cxx##R) std::for_each( \
    std::begin(cxx##R##_lib), std::end(cxx##R##_lib), add);
#define PCORE(R) if (print.cxx##R and print.core_features) \
    show("C++"#R " CORE", cxx##R##_core);
#define PLIB(R) if (print.cxx##R and print.lib_features ) \
    show("C++"#R " LIB" , cxx##R##_lib);
inline void show_latest()
{
    auto latest_rev = []() -> int
    {
        return CXX(32) CXX(29) CXX(26) CXX(23) CXX(20) CXX(17) CXX(14) CXX(11) 98;
    };
    std::vector<CompilerFeature> latest;
    auto add = [&latest](CompilerFeature x)
    {
        auto i = std::lower_bound(latest.begin(), latest.end(), x);
        if (i == latest.end() or not (*i == x))
            latest.insert(i, x);
        else if (i->data() < x.data())
            i->data(x.data());
    };
    char text[64];
    latest.reserve(1024); // max macros
    if (print.core_features)
    {   // preserve reverse revision insertion order!
        CORE(32) CORE(29) CORE(26) CORE(23) CORE(20) CORE(17) CORE(14) CORE(11) CORE(98)
        std::snprintf(text, sizeof text, "ALL CORE MACROS UP TO C++%02i", latest_rev());
        show(text, latest);
    }
    latest.clear();
    if (print.lib_features)
    {   // preserve reverse revision insertion order!
        LIB(32) LIB(29) LIB(26) LIB(23) LIB(20) LIB(17) LIB(14)
        std::snprintf(text, sizeof text, "ALL LIB MACROS UP TO C++%02i", latest_rev());
        show(text, latest);
    }
}
int main()
{
    if (print.separated_revisions)
    {
        PCORE(98) PCORE(11) PCORE(14) PLIB(14) PCORE(17) PLIB(17) PCORE(20) PLIB(20)
        PCORE(23) PLIB(23) PCORE(26) PLIB(26) PCORE(29) PLIB(29) PCORE(32) PLIB(32)
    }
    if (print.latest_revisions) show_latest();
    if (print.attributes) show("ATTRIBUTES", attributes);
    if (print.compiler_specific) show_compiler_specific_info();
}
```
Possible output:

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [P2552R3](https://wg21.link/P2552R3) | C++20 | `__has_cpp_attribute` must expand to a non-zero value for standard attributes | can expand to `0` | 

### See also

| [**Library feature-test macros**](https://en.cppreference.com/cpp/utility/feature_test) (C++20) | defined in the header [`<version>`](https://en.cppreference.com/cpp/header/version) | 
| **[Predefined Macro Symbols](https://en.cppreference.com/cpp/preprocessor/replace#Predefined_macros)** |  | 
| **[Macro Symbol Index](https://en.cppreference.com/cpp/symbol_index/macro)** |  | 

### External links

| 1. | [The official document on Feature-Test Recommendations](https://isocpp.org/std/standing-documents/sd-6-sg10-feature-test-recommendations) | 
| 2. | [Source code to dump compiler features](https://github.com/makelinux/examples/blob/develop/cpp/features.cpp) |