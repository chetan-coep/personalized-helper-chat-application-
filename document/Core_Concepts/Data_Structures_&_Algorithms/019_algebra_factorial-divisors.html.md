---
id: "data_structures_&_algorithms_019"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Finding Power of Factorial Divisor - Algorithms for Competitive Programming"
doc_order: 19
source_url: "https://cp-algorithms.com/algebra/factorial-divisors.html"
language: "en"
retrieved_at: "2026-11-03 18:00:20"
content_hash: "2a7d6f014f5e71ada18d9753cd7a05f1f6447c4eaee60b9469e897d5045761fd"
---

# Finding Power of Factorial Divisor - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/factorial-divisors.html

---

# Finding Power of Factorial Divisor[¶](https://cp-algorithms.com#finding-power-of-factorial-divisor)

You are given two numbers $n$ and $k$. Find the largest integer $x$ such that $k^x$ divides $n!$.

## Prime $k$[¶](https://cp-algorithms.com#prime-k)

Let's first consider the case of prime $k$. The explicit expression for factorial

Note that every $k$-th element of the product is divisible by $k$, i.e. adds $+1$ to the answer; the number of such elements is $\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor$.

Next, every $k^2$-th element is divisible by $k^2$, i.e. adds another $+1$ to the answer (the first power of $k$ has already been counted in the previous paragraph). The number of such elements is $\Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor$.

And so on, for every $i$ each $k^i$-th element adds another $+1$ to the answer, and there are $\Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor$ such elements.

The final answer is

This result is also known as [Legendre's formula](https://en.wikipedia.org/wiki/Legendre%27s_formula).
The sum is of course finite, since only approximately the first $\log\_k n$ elements are not zeros. Thus, the runtime of this algorithm is $O(\log\_k n)$.

### Implementation[¶](https://cp-algorithms.com#implementation)

```
int fact_pow (int n, int k) {
    int res = 0;
    while (n) {
        n /= k;
        res += n;
    }
    return res;
}
```
## Composite $k$[¶](https://cp-algorithms.com#composite-k)

The same idea can't be applied directly. Instead we can factor $k$, representing it as $k = k\_1^{p\_1} \cdot \ldots \cdot k\_m^{p\_m}$. For each $k\_i$, we find the number of times it is present in $n!$ using the algorithm described above - let's call this value $a\_i$. The answer for composite $k$ will be