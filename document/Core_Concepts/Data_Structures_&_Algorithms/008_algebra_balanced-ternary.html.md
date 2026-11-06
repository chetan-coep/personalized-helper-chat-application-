---
id: "data_structures_&_algorithms_008"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Balanced Ternary - Algorithms for Competitive Programming"
doc_order: 8
source_url: "https://cp-algorithms.com/algebra/balanced-ternary.html"
language: "en"
retrieved_at: "2026-11-03 18:00:10"
content_hash: "24baa81733b4fc22e7361efcbd15962ea90a68491e15b54b96c652615461f18a"
---

# Balanced Ternary - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/balanced-ternary.html

---

# Balanced Ternary[¶](https://cp-algorithms.com#balanced-ternary)

This is a non-standard but still positional **numeral system**. Its feature is that digits can have one of the values `-1`, `0` and `1`.
Nevertheless, its base is still `3` (because there are three possible values). Since it is not convenient to write `-1` as a digit,
we'll use letter `Z` further for this purpose. If you think it is quite a strange system - look at the picture - here is one of the
computers utilizing it.

So here are few first numbers written in balanced ternary:

```
    0    0
    1    1
    2    1Z
    3    10
    4    11
    5    1ZZ
    6    1Z0
    7    1Z1
    8    10Z
    9    100
```
This system allows you to write negative values without leading minus sign: you can simply invert digits in any positive number.

```
    -1   Z
    -2   Z1
    -3   Z0
    -4   ZZ
    -5   Z11
```
Note that a negative number starts with `Z` and positive with `1`.

## Conversion algorithm[¶](https://cp-algorithms.com#conversion-algorithm)

It is easy to represent a given number in **balanced ternary** via temporary representing it in normal ternary number system. When value is
in standard ternary, its digits are either `0` or `1` or `2`. Iterating from the lowest digit we can safely skip any `0`s and `1`s,
however `2` should be turned into `Z` with adding `1` to the next digit. Digits `3` should be turned into `0` on the same terms -
such digits are not present in the number initially but they can be encountered after increasing some `2`s.

**Example 1:** Let us convert `64` to balanced ternary. At first we use normal ternary to rewrite the number:

Let us process it from the least significant (rightmost) digit:

- `1`, `0` and `1` are skipped as they are. (Because `0` and `1` are allowed in balanced ternary)
- `2` is turned into `Z` increasing the digit to its left, so we get `1Z101`.

The final result is `1Z101`.

Let us convert it back to the decimal system by adding the weighted positional values:

**Example 2:** Let us convert `237` to balanced ternary. At first we use normal ternary to rewrite the number:

Let us process it from the least significant (rightmost) digit:

- `0` and `1` are skipped as they are. (Because `0` and `1` are allowed in balanced ternary)
- `2` is turned into `Z` increasing the digit to its left, so we get `23Z10`.
- `3` is turned into `0` increasing the digit to its left, so we get `30Z10`.
- `3` is turned into `0` increasing the digit to its left (which is by default `0`), and so we get `100Z10`.

The final result is `100Z10`.

Let us convert it back to the decimal system by adding the weighted positional values: