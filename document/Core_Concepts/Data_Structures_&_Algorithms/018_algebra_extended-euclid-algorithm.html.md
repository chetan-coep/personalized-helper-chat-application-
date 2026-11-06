---
id: "data_structures_&_algorithms_018"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Extended Euclidean Algorithm - Algorithms for Competitive Programming"
doc_order: 18
source_url: "https://cp-algorithms.com/algebra/extended-euclid-algorithm.html"
language: "en"
retrieved_at: "2026-11-03 18:00:19"
content_hash: "7e94225b48e3a6dfe36f81844004232dc5f0c6db36081375848af045e99a4073"
---

# Extended Euclidean Algorithm - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/extended-euclid-algorithm.html

---

# Extended Euclidean Algorithm[¶](https://cp-algorithms.com#extended-euclidean-algorithm)

While the [Euclidean algorithm](https://cp-algorithms.com/euclid-algorithm.html) calculates only the greatest common divisor (GCD) of two non-negative integers $a$ and $b$, the extended version also finds a way to represent GCD in terms of $a$ and $b$, i.e. coefficients $x$ and $y$ for which:

It's important to note that by [Bézout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity) we can always find such a representation. For instance, $\gcd(55, 80) = 5$, therefore we can represent $5$ as a linear combination with the terms $55$ and $80$: $55 \cdot 3 + 80 \cdot (-2) = 5$

A more general form of that problem is discussed in the article about [Linear Diophantine Equations](https://cp-algorithms.com/linear-diophantine-equation.html).
It will build upon this algorithm.

## Algorithm[¶](https://cp-algorithms.com#algorithm)

We will denote the GCD of $a$ and $b$ with $g$ in this section.

The changes to the original algorithm are very simple. If we recall the algorithm, we can see that the algorithm ends with $b = 0$ and $a = g$. For these parameters we can easily find coefficients, namely $g \cdot 1 + 0 \cdot 0 = g$.

Starting from these coefficients $(x, y) = (1, 0)$, we can go backwards up the recursive calls. All we need to do is to figure out how the coefficients $x$ and $y$ change during the transition from $(a, b)$ to $(b, a \bmod b)$.

Let us assume we found the coefficients $(x\_1, y\_1)$ for $(b, a \bmod b)$:

and we want to find the pair $(x, y)$ for $(a, b)$:

We can represent $a \bmod b$ as:

Substituting this expression in the coefficient equation of $(x\_1, y\_1)$ gives:

and after rearranging the terms:

We found the values of $x$ and $y$:

## Implementation[¶](https://cp-algorithms.com#implementation)

```
int gcd(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}
```
The recursive function above returns the GCD and the values of coefficients to `x` and `y` (which are passed by reference to the function).

This implementation of extended Euclidean algorithm produces correct results for negative integers as well.

## Iterative version[¶](https://cp-algorithms.com#iterative-version)

It's also possible to write the Extended Euclidean algorithm in an iterative way. Because it avoids recursion, the code will run a little bit faster than the recursive one.

```
int gcd(int a, int b, int& x, int& y) {
    x = 1, y = 0;
    int x1 = 0, y1 = 1, a1 = a, b1 = b;
    while (b1) {
        int q = a1 / b1;
        tie(x, x1) = make_tuple(x1, x - q * x1);
        tie(y, y1) = make_tuple(y1, y - q * y1);
        tie(a1, b1) = make_tuple(b1, a1 - q * b1);
    }
    return a1;
}
```
If you look closely at the variables `a1` and `b1`, you can notice that they take exactly the same values as in the iterative version of the normal [Euclidean algorithm](https://cp-algorithms.com/euclid-algorithm.html#implementation). So the algorithm will at least compute the correct GCD.

To see why the algorithm computes the correct coefficients, consider that the following invariants hold at any given time (before the while loop begins and at the end of each iteration):

Let the values at the end of an iteration be denoted by a prime ($'$), and assume $q = \frac{a\_1}{b\_1}$. From the [Euclidean algorithm](https://cp-algorithms.com/euclid-algorithm.html), we have:

For the first invariant to hold, the following should be true:

Similarly for the second invariant, the following should hold:

By comparing the coefficients of $a$ and $b$, the update equations for each variable can be derived, ensuring that the invariants are maintained throughout the algorithm.

At the end we know that $a\_1$ contains the GCD, so $x \cdot a + y \cdot b = g$. Which means that we have found the required coefficients.

You can even optimize the code more, and remove the variable $a\_1$ and $b\_1$ from the code, and just reuse $a$ and $b$. However if you do so, you lose the ability to argue about the invariants.