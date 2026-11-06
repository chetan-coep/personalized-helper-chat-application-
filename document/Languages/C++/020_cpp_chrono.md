---
id: "c++_020"
technology: "C++"
category: "Languages"
title: "Date and time library - cppreference.com"
doc_order: 20
source_url: "https://en.cppreference.com/cpp/chrono"
language: "en"
retrieved_at: "2026-11-03 17:56:16"
content_hash: "7ef9590d828b31e6b0dee9f7f33f83ba0c8df62e3d7fa413bb56d8308102350f"
---

# Date and time library - cppreference.com

Source: https://en.cppreference.com/cpp/chrono

---

# Date and time library

C++ includes support for two types of time manipulation:

- The [chrono library](https://en.cppreference.com#chrono_library), a flexible collection of types that track time with varying degrees of precision (e.g., [std::chrono::time\_point](https://en.cppreference.com/cpp/chrono/time_point)).
- [C-style date and time library](https://en.cppreference.com#C-style_date_and_time_library) (e.g., [std::time](https://en.cppreference.com/cpp/chrono/c/time)).


### [Chrono library](https://en.cppreference.com/cpp/header/chrono) (since C++11)

The `chrono` library defines several main types as well as utility functions and common typedefs:

|  | (since C++20) | 

#### Clocks

A clock consists of a starting point (or epoch) and a tick rate. For example, a clock may have an epoch of January 1, 1970 and tick every second. C++ defines several clock types:

| Defined in  namespace `std::chrono` |  | 
|  | wall clock time from the system-wide realtime clock (class) | 
|  | monotonic clock that will never be adjusted (class) | 
|  | the clock with the shortest tick period available (class) | 
|  | determines if a type is a [Clock](https://en.cppreference.com/cpp/named_req/Clock) (class template) (variable template) | 
|  | [Clock](https://en.cppreference.com/cpp/named_req/Clock) for Coordinated Universal Time (UTC) (class) | 
|  | [Clock](https://en.cppreference.com/cpp/named_req/Clock) for International Atomic Time (TAI) (class) | 
|  | [Clock](https://en.cppreference.com/cpp/named_req/Clock) for GPS time (class) | 
|  | [Clock](https://en.cppreference.com/cpp/named_req/Clock) used for [file time](https://en.cppreference.com/cpp/filesystem/file_time_type) (typedef) | 
|  | pseudo-clock representing local time (class) | 

#### Time point

A time point is a duration of time that has passed since the epoch of a specific clock.

| Defined in  namespace `std::chrono` |  | 
|  | a point in time (class template) | 
|  | traits class defining how to convert time points of one clock to another (class template) | 
|  | convert time points of one clock to another (function template) | 

#### Duration

A duration consists of a span of time, defined as some number of ticks of some time unit. For example, "42 seconds" could be represented by a duration consisting of 42 ticks of a 1-second time unit.

| Defined in  namespace `std::chrono` |  | 
|  | a time interval (class template) | 


#### Time of day (since C++20)

`hh_mm_ss` splits a duration representing time elapsed since midnight into hours, minutes, seconds, and fractional seconds, as applicable. It is primarily a formatting tool.

| Defined in  namespace `std::chrono` |  | 
|  | represents a time of day (class template) | 
|  | translates between a 12h/24h format time of day (function) | 


#### Calendar (since C++20)

| Defined in  namespace `std::chrono` |  | 
|  | tag class indicating the *last* day or weekday in a month (class) (constant) | 
|  | represents a day of a month (class) | 
|  | represents a month of a year (class) | 
|  | represents a year in the Gregorian calendar (class) | 
|  | represents a day of the week in the Gregorian calendar (class) | 
|  | represents the n <sup>th</sup> [`weekday`](https://en.cppreference.com/cpp/chrono/weekday) of a month (class) | 
|  | represents the last [`weekday`](https://en.cppreference.com/cpp/chrono/weekday) of a month (class) | 
|  | represents a specific [`day`](https://en.cppreference.com/cpp/chrono/day) of a specific [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | represents the last day of a specific [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | represents the n <sup>th</sup> [`weekday`](https://en.cppreference.com/cpp/chrono/weekday) of a specific [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | represents the last [`weekday`](https://en.cppreference.com/cpp/chrono/weekday) of a specific [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | represents a specific [`month`](https://en.cppreference.com/cpp/chrono/month) of a specific [`year`](https://en.cppreference.com/cpp/chrono/year) (class) | 
|  | represents a specific [`year`](https://en.cppreference.com/cpp/chrono/year), [`month`](https://en.cppreference.com/cpp/chrono/month), and [`day`](https://en.cppreference.com/cpp/chrono/day) (class) | 
|  | represents the last day of a specific [`year`](https://en.cppreference.com/cpp/chrono/year) and [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | represents the n <sup>th</sup> [`weekday`](https://en.cppreference.com/cpp/chrono/weekday) of a specific [`year`](https://en.cppreference.com/cpp/chrono/year) and [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | represents the last [`weekday`](https://en.cppreference.com/cpp/chrono/weekday) of a specific [`year`](https://en.cppreference.com/cpp/chrono/year) and [`month`](https://en.cppreference.com/cpp/chrono/month) (class) | 
|  | conventional syntax for Gregorian calendar date creation (function) | 


#### Time zone (since C++20)

| Defined in  namespace `std::chrono` |  | 
|  | describes a copy of the [IANA time zone database](https://www.iana.org/time-zones) (class) | 
|  | represents a linked list of [`tzdb`](https://en.cppreference.com/cpp/chrono/tzdb) (class) | 
|  | accesses and controls the global time zone database information (function) | 
|  | locates a [`time_zone`](https://en.cppreference.com/cpp/chrono/time_zone) based on its name (function) | 
|  | returns the current [`time_zone`](https://en.cppreference.com/cpp/chrono/time_zone) (function) | 
|  | represents a time zone (class) | 
|  | represents information about a time zone at a particular time point (class) | 
|  | represents information about a local time to UNIX time conversion (class) | 
|  | selects how an ambiguous local time should be resolved (enum) | 
|  | traits class for time zone pointers used by [`zoned_time`](https://en.cppreference.com/cpp/chrono/zoned_time) (class template) | 
|  | represents a time zone and a time point (class) | 
|  | contains information about a leap second insertion (class) | 
|  | leap second insertion information (class) | 
|  | obtains leap second insertion information from a `utc_time` object (function template) | 
|  | represents an alternative name for a time zone (class) | 
|  | exception thrown to report that a local time is nonexistent (class) | 
|  | exception thrown to report that a local time is ambiguous (class) | 


#### Literals (since C++14)

| Defined in inline namespace `std::literals::chrono_literals` |  | 
|  | a std::chrono::year literal representing a particular year (function) | 
|  | a std::chrono::day literal representing a day of a month (function) | 
|  | a [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) literal representing hours (function) | 
|  | a [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) literal representing minutes (function) | 
|  | a [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) literal representing seconds (function) | 
|  | a [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) literal representing milliseconds (function) | 
|  | a [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) literal representing microseconds (function) | 
|  | a [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) literal representing nanoseconds (function) | 


#### Chrono I/O (since C++20)

| Defined in  namespace `std::chrono` |  | 
|  | parses a `chrono` object from a stream (function template) | 

### Notes

| [Feature-test](https://en.cppreference.com/cpp/utility/feature_test) macro | Value | Std | Feature | 
|---|---|---|---|
| [`__cpp_lib_chrono`](https://en.cppreference.com/cpp/feature_test#cpp_lib_chrono) | [`201510L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_chrono_201510L) | (C++17) | Rounding functions for [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) and [std::chrono::time\_point](https://en.cppreference.com/cpp/chrono/time_point) | 
|  | [`201611L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_chrono_201611L) | (C++17) | `constexpr` for all the member functions of [std::chrono::duration](https://en.cppreference.com/cpp/chrono/duration) and [std::chrono::time\_point](https://en.cppreference.com/cpp/chrono/time_point) | 
|  | [`201907L`](https://en.cppreference.com/cpp/compiler_support/20#cpp_lib_chrono_201907L) | (C++20) | [Calendars](https://en.cppreference.com#Calendar) and [Time zones](https://en.cppreference.com#Time_zone) | 
|  | [`202306L`](https://en.cppreference.com/cpp/compiler_support/26#cpp_lib_chrono_202306L) | (C++26) | [Hashing](https://en.cppreference.com/cpp/utility/hash) support for `std::chrono` value classes | 

Also provided are the C-style date and time functions, such as [std::time\_t](https://en.cppreference.com/cpp/chrono/c/time_t), [std::difftime](https://en.cppreference.com/cpp/chrono/c/difftime), and [CLOCKS\_PER\_SEC](https://en.cppreference.com/cpp/chrono/c/CLOCKS_PER_SEC).

### Example

```
#include <chrono>
#include <iostream>
 
long Fibonacci(unsigned n)
{
    return n < 2 ? n : Fibonacci(n - 1) + Fibonacci(n - 2);
}
 
int main()
{
    // Measures and displays an execution time of a function call.
    const auto start{std::chrono::steady_clock::now()};
    const auto fb{Fibonacci(42)};
    const auto finish{std::chrono::steady_clock::now()};
    const std::chrono::duration<double> elapsed_seconds{finish - start};
    
    std::cout << "Fibonacci(42): " << fb << "\nElapsed time: ";
//  std::cout << elapsed_seconds.count() << "s\n"; // Before C++20
    std::cout << elapsed_seconds << '\n'; // C++20's chrono::duration operator<<
    // Prints UTC and local time.
    const auto tp_utc{std::chrono::system_clock::now()};
    std::cout << "Current time 'UTC' is: " << tp_utc << "\n"
                 "Current time 'Local' is: "
              << std::chrono::current_zone()->to_local(tp_utc) << '\n';
}
```
Possible output: