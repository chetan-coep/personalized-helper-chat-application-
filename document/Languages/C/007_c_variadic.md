---
id: "c_007"
technology: "C"
category: "Languages"
title: "Variadic functions - cppreference.com"
doc_order: 7
source_url: "https://en.cppreference.com/c/variadic"
language: "en"
retrieved_at: "2026-11-03 17:55:13"
content_hash: "7e2b07cdbd7878c5eaf83fa91c39ba7fc336275d05d3677a0cd232c8fbdbd54c"
---

# Variadic functions - cppreference.com

Source: https://en.cppreference.com/c/variadic

---

# Variadic functions

Variadic functions are functions (e.g. [printf](https://en.cppreference.com/c/io/fprintf)) which take a variable number of arguments.

The declaration of a variadic function uses an ellipsis as the last parameter, e.g. `int printf(const char* format, ...);`. See [variadic arguments](https://en.cppreference.com/c/language/variadic) for additional detail on the syntax and automatic argument conversions.

Accessing the variadic arguments from the function body uses the following library facilities:

| Types |  | 
|  | holds the information needed by va\_start, va\_arg, va\_end, and va\_copy (typedef) | 
| Macros |  | 
|  | enables access to variadic function arguments (function macro) | 
|  | accesses the next variadic function argument (function macro) | 
|  | makes a copy of the variadic function arguments (function macro) | 
|  | ends traversal of the variadic function arguments (function macro) | 

### Example

Print values of different types.

```
#include <stdarg.h>
#include <stdio.h>
void simple_printf(const char* fmt, ...)
{
    va_list args;
    for (va_start(args, fmt); *fmt != '\0'; ++fmt)
    {
        switch(*fmt)
        {
            case 'd':
            {
                int i = va_arg(args, int);
                printf("%d\n", i);
                break;
            }
            case 'c':
            {
                // A 'char' variable will be promoted to 'int'
                // A character literal in C is already 'int' by itself
                int c = va_arg(args, int);
                printf("%c\n", c);
                break;
            }
            case 'f':
            {
                double d = va_arg(args, double);
                printf("%f\n", d);
                break;
            }
            default:
                puts("Unknown formatter!");
                goto END;
        }
    }
END:
    va_end(args);
}
int main(void)
{
    simple_printf("dcff", 3, 'a', 1.969, 42.5);
}
```
Output:

### References

- C23 standard (ISO/IEC 9899:2024):

  - 7.16 Variable arguments \<stdarg.h> (p: TBD)

- C17 standard (ISO/IEC 9899:2018):

  - 7.16 Variable arguments \<stdarg.h> (p: TBD)

- C11 standard (ISO/IEC 9899:2011):

  - 7.16 Variable arguments \<stdarg.h> (p: 269-272)

- C99 standard (ISO/IEC 9899:1999):

  - 7.15 Variable arguments \<stdarg.h> (p: 249-252)

- C89/C90 standard (ISO/IEC 9899:1990):

  - 4.8 VARIABLE ARGUMENTS \<stdarg.h>