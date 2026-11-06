---
id: "data_structures_&_algorithms_016"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Number of divisors / sum of divisors - Algorithms for Competitive Programming"
doc_order: 16
source_url: "https://cp-algorithms.com/algebra/divisors.html"
language: "en"
retrieved_at: "2026-11-03 18:00:18"
content_hash: "6e771ae94c8ea17672a1d411f08919eefafc4e5f95a25683ccc58f8eed75e28e"
---

# Number of divisors / sum of divisors - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/divisors.html

---

# Number of divisors / sum of divisors[¶](https://cp-algorithms.com#number-of-divisors-sum-of-divisors)

In this article we discuss how to compute the number of divisors $d(n)$ and the sum of divisors $\sigma(n)$ of a given number $n$.

## Number of divisors[¶](https://cp-algorithms.com#number-of-divisors)

The prime factors of a divisor $d$, including their multiplicities, have to form a submultiset of the prime factors of $n$; e.g. $6 = 2 \cdot 3$ is a divisor of $60 = 2^2 \cdot 3 \cdot 5$. So we only need to count all different submultisets of the prime factorization of $n$.

A set with $x$ distinct elements has $2^x$ subsets. In our case, however, some prime factors may appear multiple times in the prime factorization of $n$, so we are choosing from a multiset rather than a set.

If a prime factor $p$ appears $e$ times in the prime factorization of $n$, then we can use the factor $p$ up to $e$ times in the submultiset. Which means we have $e+1$ choices.

Therefore if the prime factorization of $n$ is $p\_1^{e\_1} \cdot p\_2^{e\_2} \cdots p\_k^{e\_k}$, where $p\_i$ are distinct prime numbers, then the number of divisors is:

A way of thinking about it is the following:

- If there is only one distinct prime divisor $n = p\_1^{e\_1}$, then there are obviously $e\_1 + 1$ divisors ($1, p\_1, p\_1^2, \dots, p\_1^{e\_1}$).
- If there are two distinct prime divisors $n = p\_1^{e\_1} \cdot p\_2^{e\_2}$, then you can arrange all divisors in form of a tabular.

So the number of divisors is trivially $(e\_1 + 1) \cdot (e\_2 + 1)$.

- A similar argument can be made if there are more than two distinct prime factors.

```
long long numberOfDivisors(long long num) {
    long long total = 1;
    for (int i = 2; (long long)i * i <= num; i++) {
        if (num % i == 0) {
            int e = 0;
            do {
                e++;
                num /= i;
            } while (num % i == 0);
            total *= e + 1;
        }
    }
    if (num > 1) {
        total *= 2;
    }
    return total;
}
```
## Sum of divisors[¶](https://cp-algorithms.com#sum-of-divisors)

We can use the same argument of the previous section.

- If there is only one distinct prime divisor $n = p\_1^{e\_1}$, then the sum is:

- If there are two distinct prime divisors $n = p\_1^{e\_1} \cdot p\_2^{e\_2}$, then we can make the same table as before. The only difference is that now we want to compute the sum instead of counting the elements. It is easy to see, that the sum of each combination can be expressed as:

- In general, for $n = p\_1^{e\_1} \cdot p\_2^{e\_2} \cdots p\_k^{e\_k}$ we receive the formula:

```
long long SumOfDivisors(long long num) {
    long long total = 1;
    for (int i = 2; (long long)i * i <= num; i++) {
        if (num % i == 0) {
            int e = 0;
            do {
                e++;
                num /= i;
            } while (num % i == 0);
            long long sum = 0, pow = 1;
            do {
                sum += pow;
                pow *= i;
            } while (e-- > 0);
            total *= sum;
        }
    }
    if (num > 1) {
        total *= (1 + num);
    }
    return total;
}
```
## Multiplicative functions[¶](https://cp-algorithms.com#multiplicative-functions)

A multiplicative function is a function $f(x)$ which satisfies

if $a$ and $b$ are coprime.

Both $d(n)$ and $\sigma(n)$ are multiplicative functions.

Multiplicative functions have a huge variety of interesting properties, which can be very useful in number theory problems. For instance the Dirichlet convolution of two multiplicative functions is also multiplicative.