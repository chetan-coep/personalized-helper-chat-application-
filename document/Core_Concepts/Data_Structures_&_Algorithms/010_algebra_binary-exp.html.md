---
id: "data_structures_&_algorithms_010"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Binary Exponentiation - Algorithms for Competitive Programming"
doc_order: 10
source_url: "https://cp-algorithms.com/algebra/binary-exp.html"
language: "en"
retrieved_at: "2026-11-03 18:00:12"
content_hash: "bde399035c42195aee99b70b60096c5337c5aed1e08147f38ee290d6dd679319"
---

# Binary Exponentiation - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/binary-exp.html

---

# Binary Exponentiation[¶](https://cp-algorithms.com#binary-exponentiation)

Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to calculate $a^n$, where $n$ is a non-negative integer, using only $O(\log n)$ multiplications (instead of $O(n)$ multiplications required by the naive approach).

It also has important applications in many tasks unrelated to arithmetic, since it
can be used with any operations that have the property of **associativity**:

Most obviously this applies to modular multiplication, to multiplication of matrices and to other problems which we will discuss below.

## Algorithm[¶](https://cp-algorithms.com#algorithm)

Raising $a$ to the power of $n$ is expressed naively as multiplication by $a$ done $n - 1$ times: $a^{n} = a \cdot a \cdot \ldots \cdot a$. However, this approach is not practical for large $a$ or $n$.

$a^{b+c} = a^b \cdot a^c$ and $a^{2b} = a^b \cdot a^b = (a^b)^2$.

The idea of binary exponentiation is, that we split the work using the binary representation of the exponent.

Let's write $n$ in base 2, for example:

Since the number $n$ has exactly $\lfloor \log\_2 n \rfloor + 1$ digits in base 2, we only need to perform $O(\log n)$ multiplications, if we know the powers $a^1, a^2, a^4, a^8, \dots, a^{2^{\lfloor \log\_2 n \rfloor}}$.

So we only need to know a fast way to compute those. Luckily this is very easy, since an element in the sequence is just the square of the previous element.

So to get the final answer for $3^{13}$, we only need to multiply three of them (skipping $3^2$ because the corresponding bit in $n$ is not set): $3^{13} = 6561 \cdot 81 \cdot 3 = 1594323$

The final complexity of this algorithm is $O(\log n)$: we have to compute $\log n$ powers of $a$, and then have to do at most $\log n$ multiplications to get the final answer from them.

The following recursive approach expresses the same idea:

## Implementation[¶](https://cp-algorithms.com#implementation)

First the recursive approach, which is a direct translation of the recursive formula:

```
long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
}
```
The second approach accomplishes the same task without recursion. It computes all the powers in a loop, and multiplies the ones with the corresponding set bit in $n$. Although the complexity of both approaches is identical, this approach will be faster in practice since we don't have the overhead of the recursive calls.

```
long long binpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}
```
## Applications[¶](https://cp-algorithms.com#applications)

### Effective computation of large exponents modulo a number[¶](https://cp-algorithms.com#effective-computation-of-large-exponents-modulo-a-number)

**Problem:**
Compute $x^n \bmod m$.
This is a very common operation. For instance it is used in computing the [modular multiplicative inverse](https://cp-algorithms.com/module-inverse.html).

**Solution:**
Since we know that the modulo operator doesn't interfere with multiplications ($a \cdot b \equiv (a \bmod m) \cdot (b \bmod m) \pmod m$), we can directly use the same code, and just replace every multiplication with a modular multiplication:

```
long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
```
**Note:**
It's possible to speed this algorithm for large $b >> m$.
If $m$ is a positive number and $\gcd(x, m) = 1$, then  $x^n \equiv x^{n \bmod (m-1)} \pmod{m}$ for prime $m$, and $x^n \equiv x^{n \bmod{\phi(m)}} \pmod{m}$ for composite $m$.
This follows directly from Fermat's little theorem and Euler's theorem, see the article about [Modular Inverses](https://cp-algorithms.com/module-inverse.html#fermat-euler) for more details.

### Effective computation of Fibonacci numbers[¶](https://cp-algorithms.com#effective-computation-of-fibonacci-numbers)

**Problem:** Compute $n$-th Fibonacci number $F\_n$.

**Solution:** For more details, see the [Fibonacci Number article](https://cp-algorithms.com/fibonacci-numbers.html).
We will only go through an overview of the algorithm.
To compute the next Fibonacci number, only the two previous ones are needed, as $F\_n = F\_{n-1} + F\_{n-2}$.
We can build a $2 \times 2$ matrix that describes this transformation:
the transition from $F\_i$ and $F\_{i+1}$ to $F\_{i+1}$ and $F\_{i+2}$.
For example, applying this transformation to the pair $F\_0$ and $F\_1$ would change it into $F\_1$ and $F\_2$.
Therefore, we can raise this transformation matrix to the $n$-th power to find $F\_n$ in time complexity $O(\log n)$.

### Applying a permutation $k$ times[¶](https://cp-algorithms.com#applying-a-permutation-k-times)

**Problem:** You are given a sequence of length $n$. Apply to it a given permutation $k$ times.

**Solution:** Simply raise the permutation to $k$-th power using binary exponentiation, and then apply it to the sequence. This will give you a time complexity of $O(n \log k)$.

```
vector<int> applyPermutation(vector<int> sequence, vector<int> permutation) {
    vector<int> newSequence(sequence.size());
    for(int i = 0; i < sequence.size(); i++) {
        newSequence[i] = sequence[permutation[i]];
    }
    return newSequence;
}
vector<int> permute(vector<int> sequence, vector<int> permutation, long long k) {
    while (k > 0) {
        if (k & 1) {
            sequence = applyPermutation(sequence, permutation);
        }
        permutation = applyPermutation(permutation, permutation);
        k >>= 1;
    }
    return sequence;
}
```
**Note:** This task can be solved more efficiently in linear time by building the permutation graph and considering each cycle independently. You could then compute $k$ modulo the size of the cycle and find the final position for each number which is part of this cycle.

### Fast application of a set of geometric operations to a set of points[¶](https://cp-algorithms.com#fast-application-of-a-set-of-geometric-operations-to-a-set-of-points)

**Problem:** Given $n$ points $p\_i$, apply $m$ transformations to each of these points. Each transformation can be a shift, a scaling or a rotation around a given axis by a given angle. There is also a "loop" operation which applies a given list of transformations $k$ times ("loop" operations can be nested). You should apply all transformations faster than $O(n \cdot length)$, where $length$ is the total number of transformations to be applied (after unrolling "loop" operations).

**Solution:** Let's look at how the different types of transformations change the coordinates:

- Shift operation: adds a different constant to each of the coordinates.
- Scaling operation: multiplies each of the coordinates by a different constant.
- Rotation operation: the transformation is more complicated (we won't go in details here), but each of the new coordinates still can be represented as a linear combination of the old ones.

As you can see, each of the transformations can be represented as a linear operation on the coordinates. Thus, a transformation can be written as a $4 \times 4$ matrix of the form:

that, when multiplied by a vector with the old coordinates and a unit gives a new vector with the new coordinates and a unit:

(Why introduce a fictitious fourth coordinate, you ask? That is the beauty of [homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates), which find great application in computer graphics. Without this, it would not be possible to implement affine operations like the shift operation as a single matrix multiplication, as it requires us to *add* a constant to the coordinates. The affine transformation becomes a linear transformation in the higher dimension!)

Here are some examples of how transformations are represented in matrix form:

- Shift operation: shift $x$ coordinate by $5$, $y$ coordinate by $7$ and $z$ coordinate by $9$.

- Scaling operation: scale the $x$ coordinate by $10$ and the other two by $5$.

- Rotation operation: rotate $\theta$ degrees around the $x$ axis following the right-hand rule (counter-clockwise direction).

Now, once every transformation is described as a matrix, the sequence of transformations can be described as a product of these matrices, and a "loop" of $k$ repetitions can be described as the matrix raised to the power of $k$ (which can be calculated using binary exponentiation in $O(\log{k})$). This way, the matrix which represents all transformations can be calculated first in $O(m \log{k})$, and then it can be applied to each of the $n$ points in $O(n)$ for a total complexity of $O(n + m \log{k})$.

### Number of paths of length $k$ in a graph[¶](https://cp-algorithms.com#number-of-paths-of-length-k-in-a-graph)

**Problem:** Given a directed unweighted graph of $n$ vertices, find the number of paths of length $k$ from any vertex $u$ to any other vertex $v$.

**Solution:** This problem is considered in more detail in [a separate article](https://cp-algorithms.com/graph/fixed_length_paths.html). The algorithm consists of raising the adjacency matrix $M$ of the graph (a matrix where $m\_{ij} = 1$ if there is an edge from $i$ to $j$, or $0$ otherwise) to the $k$-th power. Now $m\_{ij}$ will be the number of paths of length $k$ from $i$ to $j$. The time complexity of this solution is $O(n^3 \log k)$.

**Note:** In that same article, another variation of this problem is considered: when the edges are weighted and it is required to find the minimum weight path containing exactly $k$ edges. As shown in that article, this problem is also solved by exponentiation of the adjacency matrix. The matrix would have the weight of the edge from $i$ to $j$, or $\infty$ if there is no such edge.
Instead of the usual operation of multiplying two matrices, a modified one should be used:
instead of multiplication, both values are added, and instead of a summation, a minimum is taken.
That is: $result\_{ij} = \min\limits\_{1\ \leq\ k\ \leq\ n}(a\_{ik} + b\_{kj})$.

### Variation of binary exponentiation: multiplying two numbers modulo $m$[¶](https://cp-algorithms.com#variation-of-binary-exponentiation-multiplying-two-numbers-modulo-m)

**Problem:** Multiply two numbers $a$ and $b$ modulo $m$. $a$ and $b$ fit in the built-in data types, but their product is too big to fit in a 64-bit integer. The idea is to compute $a \cdot b \pmod m$ without using bignum arithmetics.

**Solution:** We simply apply the binary construction algorithm described above, only performing additions instead of multiplications. In other words, we have "expanded" the multiplication of two numbers to $O (\log m)$ operations of addition and multiplication by two (which, in essence, is an addition).

**Note:** You can solve this task in a different way by using floating-point operations. First compute the expression $\frac{a \cdot b}{m}$ using floating-point numbers and cast it to an unsigned integer $q$. Subtract $q \cdot m$ from $a \cdot b$ using unsigned integer arithmetics and take it modulo $m$ to find the answer. This solution looks rather unreliable, but it is very fast, and very easy to implement. See [here](https://cs.stackexchange.com/questions/77016/modular-multiplication) for more information.