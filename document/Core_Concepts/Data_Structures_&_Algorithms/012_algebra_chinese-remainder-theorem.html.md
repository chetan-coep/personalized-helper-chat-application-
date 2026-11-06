---
id: "data_structures_&_algorithms_012"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Chinese Remainder Theorem - Algorithms for Competitive Programming"
doc_order: 12
source_url: "https://cp-algorithms.com/algebra/chinese-remainder-theorem.html"
language: "en"
retrieved_at: "2026-11-03 18:00:14"
content_hash: "3be594e01b7ff8c1df6f92c07763bc12a9c28144a81488f7efc21d1febc59407"
---

# Chinese Remainder Theorem - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/chinese-remainder-theorem.html

---

# Chinese Remainder Theorem[¶](https://cp-algorithms.com#chinese-remainder-theorem)

The Chinese Remainder Theorem (which will be referred to as CRT in the rest of this article) was discovered by Chinese mathematician Sun Zi.

## Formulation[¶](https://cp-algorithms.com#formulation)

Let $m = m\_1 \cdot m\_2 \cdots m\_k$, where $m\_i$ are pairwise coprime. In addition to $m\_i$, we are also given a system of congruences

where $a\_i$ are some given constants. The original form of CRT then states that the given system of congruences always has *one and exactly one* solution modulo $m$.

E.g. the system of congruences

has the solution $23$ modulo $105$, because $23 \bmod{3} = 2$, $23 \bmod{5} = 3$, and $23 \bmod{7} = 2$. We can write down every solution as $23 + 105\cdot k$ for $k \in \mathbb{Z}$.

### Corollary[¶](https://cp-algorithms.com#corollary)

A consequence of the CRT is that the equation

is equivalent to the system of equations

(As above, assume that $m = m\_1 m\_2 \cdots m\_k$ and $m\_i$ are pairwise coprime).

## Solution for Two Moduli[¶](https://cp-algorithms.com#solution-for-two-moduli)

Consider a system of two equations for coprime $m\_1, m\_2$:

We want to find a solution for $a \pmod{m\_1 m\_2}$. Using the [Extended Euclidean Algorithm](https://cp-algorithms.com/extended-euclid-algorithm.html) we can find Bézout coefficients $n\_1, n\_2$ such that

In fact $n\_1$ and $n\_2$ are just the [modular inverses](https://cp-algorithms.com/module-inverse.html) of $m\_1$ and $m\_2$ modulo $m\_2$ and $m\_1$.
We have $n\_1 m\_1 \equiv 1 \pmod{m\_2}$ so $n\_1 \equiv m\_1^{-1} \pmod{m\_2}$, and vice versa $n\_2 \equiv m\_2^{-1} \pmod{m\_1}$.

With those two coefficients we can define a solution:

It's easy to verify that this is indeed a solution by computing $a \bmod{m\_1}$ and $a \bmod{m\_2}$.

Notice, that the Chinese Remainder Theorem also guarantees, that only 1 solution exists modulo $m\_1 m\_2$. This is also easy to prove.

Lets assume that you have two different solutions $x$ and $y$. Because $x \equiv a\_i \pmod{m\_i}$ and $y \equiv a\_i \pmod{m\_i}$, it follows that $x − y \equiv 0 \pmod{m\_i}$ and therefore $x − y \equiv 0 \pmod{m\_1 m\_2}$ or equivalently $x \equiv y \pmod{m\_1 m\_2}$. So $x$ and $y$ are actually the same solution.

## Solution for General Case[¶](https://cp-algorithms.com#solution-for-general-case)

### Inductive Solution[¶](https://cp-algorithms.com#inductive-solution)

As $m\_1 m\_2$ is coprime to $m\_3$, we can inductively repeatedly apply the solution for two moduli for any number of moduli. First you compute $b\_2 := a \pmod{m\_1 m\_2}$ using the first two congruences, then you can compute $b\_3 := a \pmod{m\_1 m\_2 m\_3}$ using the congruences $a \equiv b\_2 \pmod{m\_1 m\_2}$ and $a \equiv a\_3 \pmod {m\_3}$, etc.

### Direct Construction[¶](https://cp-algorithms.com#direct-construction)

A direct construction similar to Lagrange interpolation is possible.

Let $M\_i := \prod\_{j \neq i} m\_j$, the product of all moduli but $m\_i$, and $N\_i$ the modular inverses $N\_i := M\_i^{-1} \bmod{m\_i}$. Then a solution to the system of congruences is:

We can check this is indeed a solution, by computing $a \bmod{m\_i}$ for all $i$. Because $M\_j$ is a multiple of $m\_i$ for $i \neq j$ we have

### Implementation[¶](https://cp-algorithms.com#implementation)

```
struct Congruence {
    long long a, m;
};
long long chinese_remainder_theorem(vector<Congruence> const& congruences) {
    long long M = 1;
    for (auto const& congruence : congruences) {
        M *= congruence.m;
    }
    long long solution = 0;
    for (auto const& congruence : congruences) {
        long long a_i = congruence.a;
        long long M_i = M / congruence.m;
        long long N_i = mod_inv(M_i, congruence.m);
        solution = (solution + a_i * M_i % M * N_i) % M;
    }
    return solution;
}
```
## Solution for not coprime moduli[¶](https://cp-algorithms.com#solution-for-not-coprime-moduli)

As mentioned, the algorithm above only works for coprime moduli $m\_1, m\_2, \dots m\_k$.

In the not coprime case, a system of congruences has exactly one solution modulo $\text{lcm}(m\_1, m\_2, \dots, m\_k)$, or has no solution at all.

E.g. in the following system, the first congruence implies that the solution is odd, and the second congruence implies that the solution is even. It's not possible that a number is both odd and even, therefore there is clearly no solution.

It is pretty simple to determine if a system has a solution. And if it has one, we can use the original algorithm to solve a slightly modified system of congruences.

A single congruence $a \equiv a\_i \pmod{m\_i}$ is equivalent to the system of congruences $a \equiv a\_i \pmod{p\_j^{n\_j}}$ where $p\_1^{n\_1} p\_2^{n\_2}\cdots p\_k^{n\_k}$ is the prime factorization of $m\_i$.

With this fact, we can modify the system of congruences into a system, that only has prime powers as moduli. E.g. the above system of congruences is equivalent to:

Because originally some moduli had common factors, we will get some congruences moduli based on the same prime, however possibly with different prime powers.

You can observe, that the congruence with the highest prime power modulus will be the strongest congruence of all congruences based on the same prime number. Either it will give a contradiction with some other congruence, or it will imply already all other congruences.

In our case, the first congruence $a \equiv 1 \pmod{4}$ implies $a \equiv 1 \pmod{2}$, and therefore contradicts the second congruence $a \equiv 0 \pmod{2}$. Therefore this system of congruences has no solution.

If there are no contradictions, then the system of equation has a solution. We can ignore all congruences except the ones with the highest prime power moduli. These moduli are now coprime, and therefore we can solve this one with the algorithm discussed in the sections above.

E.g. the following system has a solution modulo $\text{lcm}(10, 12) = 60$.

The system of congruence is equivalent to the system of congruences:

The only congruence with same prime modulo are $a \equiv 1 \pmod{4}$ and $a \equiv 1 \pmod{2}$. The first one already implies the second one, so we can ignore the second one, and solve the following system with coprime moduli instead:

It has the solution $53 \pmod{60}$, and indeed $53 \bmod{10} = 3$ and $53 \bmod{12} = 5$.

## Garner's Algorithm[¶](https://cp-algorithms.com#garners-algorithm)

Another consequence of the CRT is that we can represent big numbers using an array of small integers.

Instead of doing a lot of computations with very large numbers numbers, which might be expensive (think of doing divisions with 1000-digit numbers), you can pick a couple of coprime moduli and represent the large number as a system of congruences, and perform all operations on the system of equations. Any number $a$ less than $m\_1 m\_2 \cdots m\_k$ can be represented as an array $a\_1, \ldots, a\_k$, where $a \equiv a\_i \pmod{m\_i}$.

By using the above algorithm, you can again reconstruct the large number whenever you need it.

Alternatively you can represent the number in the **mixed radix** representation:

Garner's algorithm, which is discussed in the dedicated article [Garner's algorithm](https://cp-algorithms.com/garners-algorithm.html), computes the coefficients $x\_i$.
And with those coefficients you can restore the full number.