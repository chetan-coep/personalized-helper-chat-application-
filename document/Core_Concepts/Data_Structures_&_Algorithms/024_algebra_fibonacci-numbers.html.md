---
id: "data_structures_&_algorithms_024"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Fibonacci Numbers - Algorithms for Competitive Programming"
doc_order: 24
source_url: "https://cp-algorithms.com/algebra/fibonacci-numbers.html"
language: "en"
retrieved_at: "2026-11-03 18:00:25"
content_hash: "e21f5d925775021eb70a5384536fdc0fadfd3c1ae8583a854d890574d7d6d532"
---

# Fibonacci Numbers - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/fibonacci-numbers.html

---

# Fibonacci Numbers[¶](https://cp-algorithms.com#fibonacci-numbers)

The Fibonacci sequence is defined as follows:

The first elements of the sequence ([OEIS A000045](http://oeis.org/A000045)) are:

## Properties[¶](https://cp-algorithms.com#properties)

Fibonacci numbers possess a lot of interesting properties. Here are a few of them:

- Cassini's identity:

This can be proved by induction. A one-line proof by Knuth comes from taking the determinant of the 2x2 matrix form below.


- The "addition" rule:

- Applying the previous identity to the case $k = n$, we get:

- From this we can prove by induction that for any positive integer $k$, $F\_{nk}$ is multiple of $F\_n$.
- For $n \ge 3$, the inverse is also true: if $F\_m$ is multiple of $F\_n$, then $m$ is multiple of $n$.
- GCD identity:

- Fibonacci numbers are the worst possible inputs for Euclidean algorithm (see Lame's theorem in [Euclidean algorithm](https://cp-algorithms.com/euclid-algorithm.html))

## Fibonacci Coding[¶](https://cp-algorithms.com#fibonacci-coding)

We can use the sequence to encode positive integers into binary code words. According to Zeckendorf's theorem, any natural number $n$ can be uniquely represented as a sum of Fibonacci numbers:

such that $k\_1 \ge k\_2 + 2,\ k\_2 \ge k\_3 + 2,\ \ldots,\ k\_r \ge 2$ (i.e.: the representation cannot use two consecutive Fibonacci numbers).

It follows that any number can be uniquely encoded in the Fibonacci coding. And we can describe this representation with binary codes $d\_0 d\_1 d\_2 \dots d\_s 1$, where $d\_i$ is $1$ if $F\_{i+2}$ is used in the representation. The code will be appended by a $1$ to indicate the end of the code word. Notice that this is the only occurrence where two consecutive 1-bits appear.

The encoding of an integer $n$ can be done with a simple greedy algorithm:

1. Iterate through the Fibonacci numbers from the largest to the smallest until you find one less than or equal to $n$.
2. Suppose this number was $F\_i$. Subtract $F\_i$ from $n$ and put a $1$ in the $i-2$ position of the code word (indexing from 0 from the leftmost to the rightmost bit).
3. Repeat until there is no remainder.
4. Add a final $1$ to the codeword to indicate its end.

To decode a code word, first remove the final $1$. Then, if the $i$-th bit is set (indexing from 0 from the leftmost to the rightmost bit), sum $F\_{i+2}$ to the number.

## Formulas for the $n^{\text{th}}$ Fibonacci number[¶](https://cp-algorithms.com#formulas-for-the-ntextth-fibonacci-number)

### Closed-form expression[¶](https://cp-algorithms.com#closed-form-expression)

There is a formula known as "Binet's formula", even though it was already known by Moivre:

This formula is easy to prove by induction, but it can be deduced with the help of the concept of generating functions or by solving a functional equation.

You can immediately notice that the second term's absolute value is always less than $1$, and it also decreases very rapidly (exponentially). Hence the value of the first term alone is "almost" $F\_n$. This can be written strictly as:

where the square brackets denote rounding to the nearest integer.

As these two formulas would require very high accuracy when working with fractional numbers, they are of little use in practical calculations.

### Fibonacci in linear time[¶](https://cp-algorithms.com#fibonacci-in-linear-time)

The $n$-th Fibonacci number can be easily found in $O(n)$ by computing the numbers one by one up to $n$. However, there are also faster ways, as we will see.

We can start from an iterative approach using the formula $F\_n = F\_{n-1} + F\_{n-2}$. The implementation only needs to keep the two most recent values, starting from the base cases $F\_0$ and $F\_1$.

```
int fib(int n) {
    int a = 0;
    int b = 1;
    for (int i = 0; i < n; i++) {
        int tmp = a + b;
        a = b;
        b = tmp;
    }
    return a;
}
```
In this way, we obtain a linear solution with $O(n)$ time and $O(1)$ additional memory.

### Matrix form[¶](https://cp-algorithms.com#matrix-form)

To go from $(F\_n, F\_{n-1})$ to $(F\_{n+1}, F\_n)$, we can express the linear recurrence as a 2x2 matrix multiplication:

This lets us treat iterating the recurrence as repeated matrix multiplication, which has nice properties. In particular,

where $F\_1 = 1, F\_0 = 0$. In fact, since

we can use the matrix directly:

Thus, in order to find $F\_n$ in $O(\log  n)$ time, we must raise the matrix to n. (See [Binary exponentiation](https://cp-algorithms.com/binary-exp.html))

```
struct matrix {
    long long mat[2][2];
    matrix friend operator *(const matrix &a, const matrix &b){
        matrix c;
        for (int i = 0; i < 2; i++) {
          for (int j = 0; j < 2; j++) {
              c.mat[i][j] = 0;
              for (int k = 0; k < 2; k++) {
                  c.mat[i][j] += a.mat[i][k] * b.mat[k][j];
              }
          }
        }
        return c;
    }
};
matrix matpow(matrix base, long long n) {
    matrix ans{ {
      {1, 0},
      {0, 1}
    } };
    while (n) {
        if(n&1)
            ans = ans*base;
        base = base*base;
        n >>= 1;
    }
    return ans;
}
long long fib(int n) {
    matrix base{ {
      {1, 1},
      {1, 0}
    } };
    return matpow(base, n).mat[0][1];
}
```
### Fast Doubling Method[¶](https://cp-algorithms.com#fast-doubling-method)

By expanding the above matrix expression for $n = 2\cdot k$

we can find these simpler equations:

Thus using above two equations Fibonacci numbers can be calculated easily by the following code:

```
pair<int, int> fib (int n) {
    if (n == 0)
        return {0, 1};
    auto p = fib(n >> 1);
    int c = p.first * (2 * p.second - p.first);
    int d = p.first * p.first + p.second * p.second;
    if (n & 1)
        return {d, c + d};
    else
        return {c, d};
}
```
## Periodicity modulo p[¶](https://cp-algorithms.com#periodicity-modulo-p)

Consider the Fibonacci sequence modulo $p$. We will prove the sequence is periodic.

Let us prove this by contradiction. Consider the first $p^2 + 1$ pairs of Fibonacci numbers taken modulo $p$:

There can only be $p$ different remainders modulo $p$, and at most $p^2$ different pairs of remainders, so there are at least two identical pairs among them. This is sufficient to prove the sequence is periodic, as a Fibonacci number is only determined by its two predecessors. Hence if two pairs of consecutive numbers repeat, that would also mean the numbers after the pair will repeat in the same fashion.

We now choose two pairs of identical remainders with the smallest indices in the sequence. Let the pairs be $(F\_a,\ F\_{a + 1})$ and $(F\_b,\ F\_{b + 1})$. We will prove that $a = 0$. If this was false, there would be two previous pairs $(F\_{a-1},\ F\_a)$ and $(F\_{b-1},\ F\_b)$, which, by the property of Fibonacci numbers, would also be equal. However, this contradicts the fact that we had chosen pairs with the smallest indices, completing our proof that there is no pre-period (i.e the numbers are periodic starting from $F\_0$).