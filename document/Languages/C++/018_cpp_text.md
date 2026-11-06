---
id: "c++_018"
technology: "C++"
category: "Languages"
title: "Text processing library - cppreference.com"
doc_order: 18
source_url: "https://en.cppreference.com/cpp/text"
language: "en"
retrieved_at: "2026-11-03 17:56:14"
content_hash: "5cb95e84fa5878fc81d931ce706e9d5e2e63d91329cb7b05582ec2fef62da0a9"
---

# Text processing library - cppreference.com

Source: https://en.cppreference.com/cpp/text

---

# Text processing library

The text processing library includes components for dealing with text.

The headers [`<locale>`](https://en.cppreference.com/cpp/header/locale) and [`<clocale>`](https://en.cppreference.com/cpp/header/clocale) provide internationalization support for character classification and string collation, numeric, monetary, and date/time formatting and parsing, and message retrieval.


### [Regular expressions library](https://en.cppreference.com/cpp/regex) (since C++11)

The header [`<regex>`](https://en.cppreference.com/cpp/header/regex) provides a class that represents [regular expressions](https://en.wikipedia.org/wiki/Regular_expression), which are a kind of mini-language used to perform pattern matching within strings.


### [Formatting library](https://en.cppreference.com/cpp/utility/format) (since C++20)

The header [`<format>`](https://en.cppreference.com/cpp/header/format) provides facilities for type-safe and extensible string formatting that is an alternative to the `printf` family of functions, and intended to complement the existing C++ I/O streams library.

### Null-terminated sequence utilities

*Null-terminated character sequences* (NTCTS) are sequences of characters that are terminated by a null character (the value after [value-initialization](https://en.cppreference.com/cpp/language/value_initialization)).

The strings library provides functions to create, inspect, and modify such sequences:

- [null-terminated byte strings](https://en.cppreference.com/cpp/string/byte) (NTBS) helper functions (including support of [wide character types](https://en.cppreference.com/cpp/string/wide)),
- [null-terminated multibyte strings](https://en.cppreference.com/cpp/string/multibyte) (NTMBS) helper functions.


### Primitive numeric conversions (since C++17)

In addition to sophisticated locale-dependent parsers and formatters provided by the [C++ I/O](https://en.cppreference.com/cpp/io) library, the [C I/O](https://en.cppreference.com/cpp/io/c) library, [C++ string converters](https://en.cppreference.com/cpp/string/basic_string#Numeric_conversions), and [C string converters](https://en.cppreference.com/cpp/string/byte#Conversions_to_numeric_formats), the header [`<charconv>`](https://en.cppreference.com/cpp/header/charconv) provides light-weight, locale-independent, non-allocating, non-throwing parsers and formatters for arithmetic types.

|  | converts an integer or floating-point value to a character sequence (function) | 
|  | the return type of [`std::to_chars`](https://en.cppreference.com/cpp/utility/to_chars) (class) | 
|  | converts a character sequence to an integer or floating-point value (function) | 
|  | the return type of [`std::from_chars`](https://en.cppreference.com/cpp/utility/from_chars) (class) | 
|  | specifies formatting for std::to\_chars and std::from\_chars (enum) | 


### Text encoding identifications (since C++26)

|  | describes an interface for accessing the [IANA Character Sets registry](https://www.iana.org/assignments/character-sets/character-sets.xhtml) (class) |