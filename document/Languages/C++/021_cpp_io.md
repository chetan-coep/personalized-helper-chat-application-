---
id: "c++_021"
technology: "C++"
category: "Languages"
title: "Input/output library - cppreference.com"
doc_order: 21
source_url: "https://en.cppreference.com/cpp/io"
language: "en"
retrieved_at: "2026-11-03 17:56:18"
content_hash: "4e73e70d38072addebe0d30498ecbfd6df126fb65105f30f3a98ee5dd4a0657b"
---

# Input/output library - cppreference.com

Source: https://en.cppreference.com/cpp/io

---

# Input/output library

C++ includes the following input/output libraries: an [OOP-style](https://en.wikipedia.org/wiki/Object-oriented_programming) [stream-based I/O](https://en.cppreference.com#Stream-based_I/O) library, [print-based family](https://en.cppreference.com#Print_functions) of functions[(since C++23)](https://en.cppreference.com/cpp/compiler_support/23#P2093R14), and the standard set of [C-style I/O](https://en.cppreference.com#C-style_I/O) functions.

### Stream-based I/O

The stream-based input/output library is organized around abstract input/output devices. These abstract devices allow the same code to handle input/output to files, memory streams, or custom adaptor devices that perform arbitrary operations (e.g. compression) on the fly.

Most of the classes are templated, so they can be adapted to any basic character type. Separate typedefs are provided for the most common basic character types (`char` and `wchar_t`). The classes are organized into the following hierarchy:

Inheritance diagram

| Abstraction |  | 
|  | manages formatting flags and input/output exceptions (class) | 
|  | manages an arbitrary stream buffer (class template) | 
|  | abstracts a raw device (class template) | 
|  | wraps a given abstract device ( [std::basic\_streambuf](https://en.cppreference.com/cpp/io/basic_streambuf)) and provides high-level output interface (class template) | 
|  | wraps a given abstract device ( [std::basic\_streambuf](https://en.cppreference.com/cpp/io/basic_streambuf)) and provides high-level input interface (class template) | 
|  | wraps a given abstract device ( [std::basic\_streambuf](https://en.cppreference.com/cpp/io/basic_streambuf)) and provides high-level input/output interface (class template) | 
| File I/O implementation |  | 
|  | implements raw file device (class template) | 
|  | implements high-level file stream input operations (class template) | 
|  | implements high-level file stream output operations (class template) | 
|  | implements high-level file stream input/output operations (class template) | 
| String I/O implementation |  | 
|  | implements raw string device (class template) | 
|  | implements high-level string stream input operations (class template) | 
|  | implements high-level string stream output operations (class template) | 
|  | implements high-level string stream input/output operations (class template) | 
| Array I/O implementations |  | 
|  | implements raw fixed character buffer device (class template) | 
|  | implements fixed character buffer input operations (class template) | 
|  | implements fixed character buffer output operations (class template) | 
|  | implements fixed character buffer input/output operations (class template) | 
|  | implements raw character array device (class) | 
|  | implements character array input operations (class) | 
|  | implements character array output operations (class) | 
|  | implements character array input/output operations (class) | 
| Synchronized output (since C++20) |  | 
|  | synchronized output device wrapper (class template) | 
|  | synchronized output stream wrapper (class template) | 

#### Typedefs

The following typedefs for common character types are provided in namespace `std`:

| Type | Definition | 
| std::ios | `std::basic_ios<char>` | 
| std::wios | `std::basic_ios<wchar_t>` | 
| [std::streambuf](https://en.cppreference.com/cpp/io/basic_streambuf) | `std::basic_streambuf<char>` | 
| [std::wstreambuf](https://en.cppreference.com/cpp/io/basic_streambuf) | `std::basic_streambuf<wchar_t>` | 
| [std::istream](https://en.cppreference.com/cpp/io/basic_istream) | `std::basic_istream<char>` | 
| [std::wistream](https://en.cppreference.com/cpp/io/basic_istream) | `std::basic_istream<wchar_t>` | 
| [std::iostream](https://en.cppreference.com/cpp/io/basic_iostream) | `std::basic_iostream<char>` | 
| [std::wiostream](https://en.cppreference.com/cpp/io/basic_iostream) | `std::basic_iostream<wchar_t>` | 
| [std::ostream](https://en.cppreference.com/cpp/io/basic_ostream) | `std::basic_ostream<char>` | 
| [std::wostream](https://en.cppreference.com/cpp/io/basic_ostream) | `std::basic_ostream<wchar_t>` | 
| [std::filebuf](https://en.cppreference.com/cpp/io/basic_filebuf) | `std::basic_filebuf<char>` | 
| [std::wfilebuf](https://en.cppreference.com/cpp/io/basic_filebuf) | `std::basic_filebuf<wchar_t>` | 
| [std::ifstream](https://en.cppreference.com/cpp/io/basic_ifstream) | `std::basic_ifstream<char>` | 
| [std::wifstream](https://en.cppreference.com/cpp/io/basic_ifstream) | `std::basic_ifstream<wchar_t>` | 
| [std::ofstream](https://en.cppreference.com/cpp/io/basic_ofstream) | `std::basic_ofstream<char>` | 
| [std::wofstream](https://en.cppreference.com/cpp/io/basic_ofstream) | `std::basic_ofstream<wchar_t>` | 
| [std::fstream](https://en.cppreference.com/cpp/io/basic_fstream) | `std::basic_fstream<char>` | 
| [std::wfstream](https://en.cppreference.com/cpp/io/basic_fstream) | `std::basic_fstream<wchar_t>` | 
| [std::stringbuf](https://en.cppreference.com/cpp/io/basic_stringbuf) | `std::basic_stringbuf<char>` | 
| [std::wstringbuf](https://en.cppreference.com/cpp/io/basic_stringbuf) | `std::basic_stringbuf<wchar_t>` | 
| [std::istringstream](https://en.cppreference.com/cpp/io/basic_istringstream) | `std::basic_istringstream<char>` | 
| [std::wistringstream](https://en.cppreference.com/cpp/io/basic_istringstream) | `std::basic_istringstream<wchar_t>` | 
| [std::ostringstream](https://en.cppreference.com/cpp/io/basic_ostringstream) | `std::basic_ostringstream<char>` | 
| [std::wostringstream](https://en.cppreference.com/cpp/io/basic_ostringstream) | `std::basic_ostringstream<wchar_t>` | 
| [std::stringstream](https://en.cppreference.com/cpp/io/basic_stringstream) | `std::basic_stringstream<char>` | 
| [std::wstringstream](https://en.cppreference.com/cpp/io/basic_stringstream) | `std::basic_stringstream<wchar_t>` | 
| std::spanbuf (C++23) | `std::basic_spanbuf<char>` | 
| std::wspanbuf (C++23) | `std::basic_spanbuf<wchar_t>` | 
| std::ispanstream (C++23) | `std::basic_ispanstream<char>` | 
| std::wispanstream (C++23) | `std::basic_ispanstream<wchar_t>` | 
| std::ospanstream (C++23) | `std::basic_ospanstream<char>` | 
| std::wospanstream (C++23) | `std::basic_ospanstream<wchar_t>` | 
| std::spanstream (C++23) | `std::basic_spanstream<char>` | 
| std::wspanstream (C++23) | `std::basic_spanstream<wchar_t>` | 
| std::syncbuf (C++20) | `std::basic_syncbuf<char>` | 
| std::wsyncbuf (C++20) | `std::basic_syncbuf<wchar_t>` | 
| std::osyncstream (C++20) | `std::basic_osyncstream<char>` | 
| std::wosyncstream (C++20) | `std::basic_osyncstream<wchar_t>` | 

#### Predefined standard stream objects

|  | reads from the standard C input stream [stdin](https://en.cppreference.com/cpp/io/c/std_streams) (global object) | 
|  | writes to the standard C output stream [stdout](https://en.cppreference.com/cpp/io/c/std_streams) (global object) | 
|  | writes to the standard C error stream [stderr](https://en.cppreference.com/cpp/io/c/std_streams), unbuffered (global object) | 
|  | writes to the standard C error stream [stderr](https://en.cppreference.com/cpp/io/c/std_streams) (global object) | 

The stream-based I/O library uses [I/O manipulators](https://en.cppreference.com/cpp/io/manip) (e.g. [std::boolalpha](https://en.cppreference.com/cpp/io/manip/boolalpha), [std::hex](https://en.cppreference.com/cpp/io/manip/hex), etc.) to control how streams behave.

#### Types

The following auxiliary types are defined:

|  | represents relative file/stream position (offset from fpos), sufficient to represent any file size (typedef) | 
|  | represents the number of characters transferred in an I/O operation or the size of an I/O buffer (typedef) | 
|  | represents absolute position in a stream or a file (class template) | 

The following typedef names for `std::fpos<std::mbstate_t>` are provided:

| Type | Definition | 
| `std::streampos` | `std::fpos<std::char_traits<char>::state_type>` | 
| `std::wstreampos` | `std::fpos<std::char_traits<wchar_t>::state_type>` | 
| `std::u8streampos` (C++20) | `std::fpos<std::char_traits<char8_t>::state_type>` | 
| `std::u16streampos` (C++11) | `std::fpos<std::char_traits<char16_t>::state_type>` | 
| `std::u32streampos` (C++11) | `std::fpos<std::char_traits<char32_t>::state_type>` | 


#### Error category interface (since C++11)

|  | the IO stream error codes (enum) | 
|  | identifies the iostream error category (function) | 


### Print functions [(since C++23)](https://en.cppreference.com/cpp/compiler_support/23#P2093R14)

The Unicode-aware print-family functions that perform formatted I/O on text that is already formatted. They bring all the performance benefits of [std::format](https://en.cppreference.com/cpp/utility/format/format), are locale-independent by default, reduce global state, avoid allocating a temporary [std::string](https://en.cppreference.com/cpp/string/basic_string) object and calling `operator<<`, and in general make formatting more efficient compared to [iostreams](https://en.cppreference.com#Stream-based_I/O) and [stdio](https://en.cppreference.com#C-style_I/O).

The following print-like functions are provided:

|  | prints to [stdout](https://en.cppreference.com/cpp/io/c/std_streams) or a file stream using [formatted](https://en.cppreference.com/cpp/utility/format) representation of the arguments (function template) | 
|  | same as std::print except that each print is terminated by additional new line (function template) | 
|  | prints to Unicode capable [stdout](https://en.cppreference.com/cpp/io/c/std_streams) or a file stream using [type-erased](https://en.cppreference.com/cpp/utility/format/basic_format_args) argument representation (function) | 
|  | prints to [stdout](https://en.cppreference.com/cpp/io/c/std_streams) or a file stream using [type-erased](https://en.cppreference.com/cpp/utility/format/basic_format_args) argument representation (function) | 
|  | outputs [formatted](https://en.cppreference.com/cpp/utility/format) representation of the arguments (function template) | 
|  | outputs [formatted](https://en.cppreference.com/cpp/utility/format) representation of the arguments with appended `'\n'` (function template) | 

C++ also includes the [input/output functions defined by C](https://en.cppreference.com/cpp/io/c), such as [std::fopen](https://en.cppreference.com/cpp/io/c/fopen), [std::getc](https://en.cppreference.com/cpp/io/c/fgetc), etc.

### See also

| [Filesystem library](https://en.cppreference.com/cpp/filesystem) [(since C++17)](https://en.cppreference.com/cpp/compiler_support/17#P0218R1) |  |