---
id: "c++_017"
technology: "C++"
category: "Languages"
title: "Strings library - cppreference.com"
doc_order: 17
source_url: "https://en.cppreference.com/cpp/string"
language: "en"
retrieved_at: "2026-11-03 17:56:13"
content_hash: "d8e4850c707bdab929e316570aa74b609b04f01d8abad3b72fef9efa68326e7f"
---

# Strings library - cppreference.com

Source: https://en.cppreference.com/cpp/string

---

# Strings library

### Characters

In the C++ standard library, a *character* is an object which, when treated sequentially, can represent text.

The term means not only objects of [character types](https://en.cppreference.com/cpp/language/type), but also any value that can be represented by a type that provides the definitions specified in the strings library and following libraries:

|  | (since C++11) | 

In the strings library and regular expressions library(since C++11), a character can be of only *char-like types*, i.e. those non-array types that satisfy the requirements of 
[PODType](https://en.cppreference.com/cpp/named_req/PODType)(until C++20)[TrivialType](https://en.cppreference.com/cpp/named_req/TrivialType) and [StandardLayoutType](https://en.cppreference.com/cpp/named_req/StandardLayoutType)(since C++20)(until C++26)[TriviallyCopyable](https://en.cppreference.com/cpp/named_req/TriviallyCopyable) and [StandardLayoutType](https://en.cppreference.com/cpp/named_req/StandardLayoutType)(since C++26).

| For any char-like type `T`, `std::is_trivially_default_constructible_v<T>` is `true`. | (since C++26) | 

Therefore, characters are also referred as *char-like objects* in the strings library and regular expressions library(since C++11).

Some standard library components accept *character container types*. They, too, are types used to represent individual characters. Such types are used for one of the template arguments of [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits) and the class templates which use [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits).

### Library components

The C++ strings library includes the following components:

#### Character traits

Many character-related class templates (such as [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string)) need a set of related types and functions to complete the definition of their semantics. These types and functions are provided as a set of member `typedef` names and functions in the template parameter `Traits` used by each such template. The classes which are able to complete those semantics are [CharTraits](https://en.cppreference.com/cpp/named_req/CharTraits).

The string library provides the class template [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits) that defines types and functions for [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string) and [std::basic\_string\_view](https://en.cppreference.com/cpp/string/basic_string_view)(since C++17).

The following specializations are defined, all of them satisfy the [CharTraits](https://en.cppreference.com/cpp/named_req/CharTraits) requirements:

| ``` template<> class char_traits<char>;  ```  |  |  | 
| ``` template<> class char_traits<wchar_t>;  ```  |  |  | 
| ``` template<> class char_traits<char8_t>;  ```  |  | (since C++20) | 
| ``` template<> class char_traits<char16_t>;  ```  |  | (since C++11) | 
| ``` template<> class char_traits<char32_t>;  ```  |  | (since C++11) | 

When a user-defined character container type for [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string) and [std::basic\_string\_view](https://en.cppreference.com/cpp/string/basic_string_view)(since C++17) is used, it is also necessary to provide a corresponding character trait class (which can be a specialization of [std::char\_traits](https://en.cppreference.com/cpp/string/char_traits)).


#### String classes ([std::string](https://en.cppreference.com/cpp/string/basic_string) etc.)

The class template [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string) generalizes how sequences of characters are manipulated and stored.  String creation, manipulation, and destruction are all handled by a convenient set of class methods and related functions.

Several specializations of [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string) are provided for commonly-used types:

| Type | Definition | 
| **std::string** | `std::basic_string<char>` | 
| **std::wstring** | `std::basic_string<wchar_t>` | 
| **std::u8string** (since C++20) | `std::basic_string<char8_t>` | 
| **std::u16string** (since C++11) | `std::basic_string<char16_t>` | 
| **std::u32string** (since C++11) | `std::basic_string<char32_t>` | 


#### String view classes ([std::string\_view](https://en.cppreference.com/cpp/string/basic_string_view) etc.) (since C++17)

The class template [std::basic\_string\_view](https://en.cppreference.com/cpp/string/basic_string_view) provides a lightweight object that offers read-only access to a string or a part of a string using an interface similar to the interface of [std::basic\_string](https://en.cppreference.com/cpp/string/basic_string).

Several specializations of [std::basic\_string\_view](https://en.cppreference.com/cpp/string/basic_string_view) are provided for commonly-used types:

| Type | Definition | 
| **std::string_view** | `std::basic_string_view<char>` | 
| **std::wstring_view** | `std::basic_string_view<wchar_t>` | 
| **std::u8string_view** (since C++20) | `std::basic_string_view<char8_t>` | 
| **std::u16string_view** | `std::basic_string_view<char16_t>` | 
| **std::u32string_view** | `std::basic_string_view<char32_t>` | 

### Relevant libraries

The [text processing library](https://en.cppreference.com/cpp/text) provides support for localizations, string conversions (e.g. [`std::toupper`](https://en.cppreference.com/cpp/locale/toupper)), character classification functions (e.g. [`std::isspace`](https://en.cppreference.com/cpp/locale/isspace)), and text encoding recognition ([`std::text_encoding`](https://en.cppreference.com/cpp/text/text_encoding)).

### Defect reports

The following behavior-changing defect reports were applied retroactively to previously published C++ standards.

| DR | Applied to | Behavior as published | Correct behavior | 
|---|---|---|---|
| [LWG 1170](https://cplusplus.github.io/LWG/issue1170) | C++98 | char-like types could be array types | prohibited |