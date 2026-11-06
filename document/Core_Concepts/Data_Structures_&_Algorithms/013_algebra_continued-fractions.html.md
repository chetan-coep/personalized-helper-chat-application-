---
id: "data_structures_&_algorithms_013"
technology: "Data Structures & Algorithms"
category: "Core Concepts"
title: "Continued fractions - Algorithms for Competitive Programming"
doc_order: 13
source_url: "https://cp-algorithms.com/algebra/continued-fractions.html"
language: "en"
retrieved_at: "2026-11-03 18:00:15"
content_hash: "a6a29fcedbce44f572dcd00b59d3865953d1b8991cff50807f33de35e5ba3106"
---

# Continued fractions - Algorithms for Competitive Programming

Source: https://cp-algorithms.com/algebra/continued-fractions.html

---

# Continued fractions[¶](https://cp-algorithms.com#continued-fractions)

**Continued fraction** is a representation of a real number as a specific convergent sequence of rational numbers. They are useful in competitive programming because they are easy to compute and can be efficiently used to find the best possible rational approximation of the underlying real number (among all numbers whose denominator doesn't exceed a given value).

Besides that, continued fractions are closely related to Euclidean algorithm which makes them useful in a bunch of number-theoretical problems.

## Continued fraction representation[¶](https://cp-algorithms.com#continued-fraction-representation)

Definition

Let $a\_0, a\_1, \dots, a\_k \in \mathbb Z$ and $a\_1, a\_2, \dots, a\_k \geq 1$. Then the expression

is called the **continued fraction representation** of the rational number $r$ and is denoted shortly as $r=\[a\_0;a\_1,a\_2,\dots,a\_k\]$.

## Example

Let $r = \frac{5}{3}$. There are two ways to represent it as a continued fraction:

It can be proven that any rational number can be represented as a continued fraction in exactly $2$ ways:

Moreover, the length $k$ of such continued fraction is estimated as $k = O(\log \min(p, q))$ for $r=\frac{p}{q}$.

The reasoning behind this will be clear once we delve into the details of the continued fraction construction.

Definition

Let $a\_0,a\_1,a\_2, \dots$ be an integer sequence such that $a\_1, a\_2, \dots \geq 1$. Let $r\_k = \[a\_0; a\_1, \dots, a\_k\]$. Then the expression

is called the **continued fraction representation** of the irrational number $r$ and is denoted shortly as $r = \[a\_0;a\_1,a\_2,\dots\]$.

Note that for $r=\[a\_0;a\_1,\dots\]$ and integer $k$, it holds that $r+k = \[a\_0+k; a\_1, \dots\]$.

Another important observation is that $\frac{1}{r}=\[0;a\_0, a\_1, \dots\]$ when $a\_0 > 0$ and $\frac{1}{r} = \[a\_1; a\_2, \dots\]$ when $a\_0 = 0$.

Definition

In the definition above, rational numbers $r\_0, r\_1, r\_2, \dots$ are called the **convergents** of $r$.

Correspondingly, individual $r\_k = \[a\_0; a\_1, \dots, a\_k\] = \frac{p\_k}{q\_k}$ is called the $k$-th **convergent** of $r$.

## Example

Consider $r = \[1; 1, 1, 1, \dots\]$. It can be proven by induction that $r\_k = \frac{F\_{k+2}}{F\_{k+1}}$, where $F\_k$ is the Fibonacci sequence defined as $F\_0 = 0$, $F\_1 = 1$ and $F\_{k} = F\_{k-1} + F\_{k-2}$. From the Binet's formula, it is known that

where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ is the golden ratio and $\psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\phi} \approx -0.618$. Thus,

Note that in this specific case, an alternative way to find $r$ would be to solve the equation

Definition

Let $r\_k = \[a\_0; a\_1, \dots, a\_{k-1}, a\_k\]$. The numbers $\[a\_0; a\_1, \dots, a\_{k-1}, t\]$ for $1 \leq t \leq a\_k$ are called **semiconvergents**.

We will typically refer to (semi)convergents that are greater than $r$ as **upper** (semi)convergents and to those that are less than $r$ as **lower** (semi)convergents.

Definition

Complementary to convergents, we define the **[complete quotients](https://en.wikipedia.org/wiki/Complete_quotient)** as $s\_k = \[a\_k; a\_{k+1}, a\_{k+2}, \dots\]$.

Correspondingly, we will call an individual $s\_k$ the $k$-th complete quotient of $r$.

From the definitions above, one can conclude that $s\_k \geq 1$ for $k \geq 1$.

Treating $\[a\_0; a\_1, \dots, a\_k\]$ as a formal algebraic expression and allowing arbitrary real numbers instead of $a\_i$, we obtain

In particular, $r = \[s\_0\] = s\_0$. On the other hand, we can express $s\_k$ as

meaning that we can compute $a\_k = \lfloor s\_k \rfloor$ and $s\_{k+1} = (s\_k - a\_k)^{-1}$ from $s\_k$.

The sequence $a\_0, a\_1, \dots$ is well-defined unless $s\_k=a\_k$ which only happens when $r$ is a rational number.

Thus the continued fraction representation is uniquely defined for any irrational number $r$.

### Implementation[¶](https://cp-algorithms.com#implementation)

In the code snippets we will mostly assume finite continued fractions.

From $s\_k$, the transition to $s\_{k+1}$ looks like

From this expression, the next complete quotient $s\_{k+1}$ is obtained as

For $s\_k=\frac{p}{q}$ it means that

Thus, the computation of a continued fraction representation for $r=\frac{p}{q}$ follows the steps of the Euclidean algorithm for $p$ and $q$.

From this also follows that $\gcd(p\_k, q\_k) = 1$ for $\frac{p\_k}{q\_k} = \[a\_0; a\_1, \dots, a\_k\]$. Hence, convergents are always irreducible.

```
auto fraction(int p, int q) {
    vector<int> a;
    while(q) {
        a.push_back(p / q);
        tie(p, q) = make_pair(q, p % q);
    }
    return a;
}
```
```
def fraction(p, q):
    a = []
    while q:
        a.append(p // q)
        p, q = q, p % q
    return a
```
## Key results[¶](https://cp-algorithms.com#key-results)

To provide some motivation for further study of continued fraction, we give some key facts now.

## Recurrence

For the convergents $r\_k = \frac{p\_k}{q\_k}$, the following recurrence stands, allowing their fast computation:

where $\frac{p\_{-1}}{q\_{-1}}=\frac{1}{0}$ and $\frac{p\_{-2}}{q\_{-2}}=\frac{0}{1}$.

## Deviations

The deviation of $r\_k = \frac{p\_k}{q\_k}$ from $r$ can be generally estimated as

Multiplying both sides with $q\_k$, we obtain alternate estimation:

From the recurrence above it follows that $q\_k$ grows at least as fast as Fibonacci numbers.

On the picture below you may see the visualization of how convergents $r\_k$ approach $r=\frac{1+\sqrt 5}{2}$:

$r=\frac{1+\sqrt 5}{2}$ is depicted by blue dotted line. Odd convergents approach it from above and even convergents approach it from below.

## Lattice hulls

Consider convex hulls of points above and below the line $y=rx$.

Odd convergents $(q\_k;p\_k)$ are the vertices of the upper hull, while the even convergents $(q\_k;p\_k)$ are the vertices of the bottom hull.

All integers vertices on the hulls are obtained as $(q;p)$ such that

for integer $0 \leq t \leq a\_k$. In other words, the set of lattice points on the hulls corresponds to the set of semiconvergents.

On the picture below, you may see the convergents and semiconvergents (intermediate gray points) of $r=\frac{9}{7}$.

## Best approximations

Let $\frac{p}{q}$ be the fraction to minimize $\left|r-\frac{p}{q}\right|$ subject to $q \leq x$ for some $x$.

Then $\frac{p}{q}$ is a semiconvergent of $r$.

The last fact allows to find the best rational approximations of $r$ by checking its semiconvergents.

Below you will find the further explanation and a bit of intuition and interpretation for these facts.

## Convergents[¶](https://cp-algorithms.com#convergents)

Let's take a closer look at the convergents that were defined earlier. For $r=\[a\_0, a\_1, a\_2, \dots\]$, its convergents are

Convergents are the core concept of continued fractions, so it is important to study their properties.

For the number $r$, its $k$-th convergent $r\_k = \frac{p\_k}{q\_k}$ can be computed as

where $P\_k(a\_0,\dots,a\_k)$ is [the continuant](<https://en.wikipedia.org/wiki/Continuant_(mathematics)>), a multivariate polynomial defined as

Thus, $r\_k$ is a weighted [mediant](<https://en.wikipedia.org/wiki/Mediant_(mathematics)>) of $r\_{k-1}$ and $r\_{k-2}$.

For consistency, two additional convergents $r\_{-1} = \frac{1}{0}$ and $r\_{-2} = \frac{0}{1}$ are defined.

## Detailed explanation

The numerator and the denominator of $r\_k$ can be seen as multivariate polynomials of $a\_0, a\_1, \dots, a\_k$:

From the definition of convergents,

From this follows $Q\_k(a\_0, \dots, a\_k) = P\_{k-1}(a\_1, \dots, a\_k)$. This yields the relation

Initially, $r\_0 = \frac{a\_0}{1}$ and $r\_1 = \frac{a\_0 a\_1 + 1}{a\_1}$, thus

For consistency, it is convenient to define $P\_{-1} = 1$ and $P\_{-2}=0$ and formally say that $r\_{-1} = \frac{1}{0}$ and $r\_{-2}=\frac{0}{1}$.

From numerical analysis, it is known that the determinant of an arbitrary tridiagonal matrix

can be computed recursively as $T\_k = a\_k T\_{k-1} - b\_{k-1} c\_{k-1} T\_{k-2}$. Comparing it to $P\_k$, we get a direct expression

This polynomial is also known as [the continuant](<https://en.wikipedia.org/wiki/Continuant_(mathematics)>) due to its close relation with continued fraction. The continuant won't change if the sequence on the main diagonal is reversed. This yields an alternative formula to compute it:

### Implementation[¶](https://cp-algorithms.com#implementation_1)

We will compute the convergents as a pair of sequences $p\_{-2}, p\_{-1}, p\_0, p\_1, \dots, p\_k$ and $q\_{-2}, q\_{-1}, q\_0, q\_1, \dots, q\_k$:

```
auto convergents(vector<int> a) {
    vector<int> p = {0, 1};
    vector<int> q = {1, 0};
    for(auto it: a) {
        p.push_back(p[p.size() - 1] * it + p[p.size() - 2]);
        q.push_back(q[q.size() - 1] * it + q[q.size() - 2]);
    }
    return make_pair(p, q);
}
```
```
def convergents(a):
    p = [0, 1]
    q = [1, 0]
    for it in a:
        p.append(p[-1]*it + p[-2])
        q.append(q[-1]*it + q[-2])
    return p, q
```
## Trees of continued fractions[¶](https://cp-algorithms.com#trees-of-continued-fractions)

There are two major ways to unite all possible continued fractions into useful tree structures.

### Stern-Brocot tree[¶](https://cp-algorithms.com#stern-brocot-tree)

[The Stern-Brocot tree](https://cp-algorithms.com/others/stern_brocot_tree_farey_sequences.html) is a binary search tree that contains all distinct positive rational numbers.

The tree generally looks as follows:

Fractions $\frac{0}{1}$ and $\frac{1}{0}$ are "virtually" kept on the left and right sides of the tree correspondingly.

Then the fraction in a node is a mediant $\frac{a+c}{b+d}$ of two fractions $\frac{a}{b}$ and $\frac{c}{d}$ above it.

The recurrence $\frac{p\_k}{q\_k}=\frac{a\_k p\_{k-1} + p\_{k-2}}{a\_k q\_{k-1} + q\_{k-2}}$ means that the continued fraction representation encodes the path to $\frac{p\_k}{q\_k}$ in the tree. To find $\[a\_0; a\_1, \dots, a\_{k}, 1\]$, one has to make $a\_0$ moves to the right, $a\_1$ moves to the left, $a\_2$ moves to the right and so on up to $a\_k$.

The parent of $\[a\_0; a\_1, \dots, a\_k,1\]$ then is the fraction obtained by taking one step back in the last used direction.

In other words, it is $\[a\_0; a\_1, \dots, a\_k-1,1\]$ when $a\_k > 1$ and $\[a\_0; a\_1, \dots, a\_{k-1}, 1\]$ when $a\_k = 1$.

Thus the children of $\[a\_0; a\_1, \dots, a\_k, 1\]$ are $\[a\_0; a\_1, \dots, a\_k+1, 1\]$ and $\[a\_0; a\_1, \dots, a\_k, 1, 1\]$.

Let's index the Stern-Brocot tree. The root vertex is assigned an index $1$. Then for a vertex $v$, the index of its left child is assigned by changing the leading bit of $v$ from $1$ to $10$ and for the right child, it's assigned by changing the leading bit from $1$ to $11$:

In this indexing, the continued fraction representation of a rational number specifies the [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) of its binary index.

For $\frac{5}{2} = \[2;2\] = \[2;1,1\]$, its index is $1011\_2$ and its run-length encoding, considering bits in the ascending order, is $\[2;1,1\]$.

Another example is $\frac{2}{5} = \[0;2,2\]=\[0;2,1,1\]$, which has index $1100\_2$ and its run-length encoding is, indeed, $\[0;2,2\]$.

It is worth noting that the Stern-Brocot tree is, in fact, a [treap](https://cp-algorithms.com/data_structures/treap.html). That is, it is a binary search tree by $\frac{p}{q}$, but it is a heap by both $p$ and $q$.

Comparing continued fractions

You're given $A=\[a\_0; a\_1, \dots, a\_n\]$ and $B=\[b\_0; b\_1, \dots, b\_m\]$. Which fraction is smaller?

## Solution

Assume for now that $A$ and $B$ are irrational and their continued fraction representations denote an infinite descent in the Stern-Brocot tree.

As we already mentioned, in this representation $a\_0$ denotes the number of right turns in the descent, $a\_1$ denotes the number of consequent left turns and so on. Therefore, when we compare $a\_k$ and $b\_k$, if $a\_k = b\_k$ we should just move on to comparing $a\_{k+1}$ and $b\_{k+1}$. Otherwise, if we're at right descents, we should check if $a\_k \< b\_k$ and if we're at left descents, we should check if $a\_k > b\_k$ to tell whether $A \< B$.

In other words, for irrational $A$ and $B$ it would be $A \< B$ if and only if $(a\_0, -a\_1, a\_2, -a\_3, \dots) \< (b\_0, -b\_1, b\_2, -b\_3, \dots)$ with lexicographical comparison.

Now, formally using $\infty$ as an element of continued fraction representation it is possible to emulate irrational numbers $A-\varepsilon$ and $A+\varepsilon$, that is, elements that are smaller (greater) than $A$, but greater (smaller) than any other real number. Specifically, for $A=\[a\_0; a\_1, \dots, a\_n\]$, one of these two elements can be emulated as $\[a\_0; a\_1, \dots, a\_n, \infty\]$ and the other can be emulated as $\[a\_0; a\_1, \dots, a\_n - 1, 1, \infty\]$.

Which one corresponds to $A-\varepsilon$ and which one to $A+\varepsilon$ can be determined by the parity of $n$ or by comparing them as irrational numbers.

```
# check if a < b assuming that a[-1] = b[-1] = infty and a != b
def less(a, b):
    a = [(-1)**i*a[i] for i in range(len(a))]
    b = [(-1)**i*b[i] for i in range(len(b))]
    return a < b
# [a0; a1, ..., ak] -> [a0, a1, ..., ak-1, 1]
def expand(a):
    if a: # empty a = inf
        a[-1] -= 1
        a.append(1)
    return a
# return a-eps, a+eps
def pm_eps(a):
    b = expand(a.copy())
    a.append(float('inf'))
    b.append(float('inf'))
    return (a, b) if less(a, b) else (b, a)
```
Best inner point

You're given $\frac{0}{1} \leq \frac{p\_0}{q\_0} \< \frac{p\_1}{q\_1} \leq \frac{1}{0}$. Find the rational number $\frac{p}{q}$ such that $(q; p)$ is lexicographically smallest and $\frac{p\_0}{q\_0} \< \frac{p}{q} \< \frac{p\_1}{q\_1}$.

## Solution

In terms of the Stern-Brocot tree it means that we need to find the LCA of $\frac{p\_0}{q\_0}$ and $\frac{p\_1}{q\_1}$. Due to the connection between Stern-Brocot tree and continued fraction, this LCA would roughly correspond to the largest common prefix of continued fraction representations for $\frac{p\_0}{q\_0}$ and $\frac{p\_1}{q\_1}$.

So, if $\frac{p\_0}{q\_0} = \[a\_0; a\_1, \dots, a\_{k-1}, a\_k, \dots\]$ and $\frac{p\_1}{q\_1} = \[a\_0; a\_1, \dots, a\_{k-1}, b\_k, \dots\]$ are irrational numbers, the LCA is $\[a\_0; a\_1, \dots, \min(a\_k, b\_k)+1\]$.

For rational $r\_0$ and $r\_1$, one of them could be the LCA itself which would require us to casework it. To simplify the solution for rational $r\_0$ and $r\_1$, it is possible to use continued fraction representation of $r\_0 + \varepsilon$ and $r\_1 - \varepsilon$ which was derived in the previous problem.

```
# finds lexicographically smallest (q, p)
# such that p0/q0 < p/q < p1/q1
def middle(p0, q0, p1, q1):
    a0 = pm_eps(fraction(p0, q0))[1]
    a1 = pm_eps(fraction(p1, q1))[0]
    a = []
    for i in range(min(len(a0), len(a1))):
        a.append(min(a0[i], a1[i]))
        if a0[i] != a1[i]:
            break
    a[-1] += 1
    p, q = convergents(a)
    return p[-1], q[-1]
```
You're given $N$ positive integer pairs $(C\_i, J\_i)$. You need to find a positive integer pair $(x, y)$ such that $C\_i x + J\_i y$ is a strictly increasing sequence.

Among such pairs, find the lexicographically minimum one.

## Solution

Rephrasing the statement, $A\_i x + B\_i y$ must be positive for all $i$, where $A\_i = C\_i - C\_{i-1}$ and $B\_i = J\_i - J\_{i-1}$.

Among such equations we have four significant groups for $A\_i x + B\_i y > 0$:

1. $A\_i, B\_i > 0$ can be ignored since we're looking for $x, y > 0$.
2. $A\_i, B\_i \leq 0$ would provide "IMPOSSIBLE" as an answer.
3. $A\_i > 0$, $B\_i \leq 0$. Such constraints are equivalent to $\frac{y}{x} \< \frac{A\_i}{-B\_i}$.
4. $A\_i \leq 0$, $B\_i > 0$. Such constraints are equivalent to $\frac{y}{x} > \frac{-A\_i}{B\_i}$.

Let $\frac{p\_0}{q\_0}$ be the largest $\frac{-A\_i}{B\_i}$ from the fourth group and $\frac{p\_1}{q\_1}$ be the smallest $\frac{A\_i}{-B\_i}$ from the third group.

The problem is now, given $\frac{p\_0}{q\_0} \< \frac{p\_1}{q\_1}$, find a fraction $\frac{p}{q}$ such that $(q;p)$ is lexicographically smallest and $\frac{p\_0}{q\_0} \< \frac{p}{q} \< \frac{p\_1}{q\_1}$.

```
    def solve():
    n = int(input())
    C = [0] * n
    J = [0] * n
    # p0/q0 < y/x < p1/q1
    p0, q0 = 0, 1
    p1, q1 = 1, 0
    fail = False
    for i in range(n):
        C[i], J[i] = map(int, input().split())
        if i > 0:
            A = C[i] - C[i-1]
            B = J[i] - J[i-1]
            if A <= 0 and B <= 0:
                fail = True
            elif B > 0 and A < 0: # y/x > (-A)/B if B > 0
                if (-A)*q0 > p0*B:
                    p0, q0 = -A, B
            elif B < 0 and A > 0: # y/x < A/(-B) if B < 0
                if A*q1 < p1*(-B):
                    p1, q1 = A, -B
    if p0*q1 >= p1*q0 or fail:
        return 'IMPOSSIBLE'
    p, q = middle(p0, q0, p1, q1)
    return str(q) + ' ' + str(p)
```
### Calkin-Wilf tree[¶](https://cp-algorithms.com#calkin-wilf-tree)

A somewhat simpler way to organize continued fractions in a binary tree is the [Calkin-Wilf tree](https://en.wikipedia.org/wiki/Calkin–Wilf_tree).

The tree generally looks like this:

In the root of the tree, the number $\frac{1}{1}$ is located. Then, for the vertex with a number $\frac{p}{q}$, its children are $\frac{p}{p+q}$ and $\frac{p+q}{q}$.

Unlike the Stern-Brocot tree, the Calkin-Wilf tree is not a binary *search* tree, so it can't be used to perform rational binary search.

In the Calkin-Wilf tree, the direct parent of a fraction $\frac{p}{q}$ is $\frac{p-q}{q}$ when $p>q$ and $\frac{p}{q-p}$ otherwise.

For the Stern-Brocot tree, we used the recurrence for convergents. To draw the connection between the continued fraction and the Calkin-Wilf tree, we should recall the recurrence for complete quotients. If $s\_k = \frac{p}{q}$, then $s\_{k+1} = \frac{q}{p \mod q} = \frac{q}{p-\lfloor p/q \rfloor \cdot q}$.

On the other hand, if we repeatedly go from $s\_k = \frac{p}{q}$ to its parent in the Calkin-Wilf tree when $p > q$, we will end up in $\frac{p \mod q}{q} = \frac{1}{s\_{k+1}}$. If we continue doing so, we will end up in $s\_{k+2}$, then $\frac{1}{s\_{k+3}}$ and so on. From this we can deduce that:

1. When $a\_0> 0$, the direct parent of $\[a\_0; a\_1, \dots, a\_k\]$ in the Calkin-Wilf tree is $\frac{p-q}{q}=\[a\_0 - 1; a\_1, \dots, a\_k\]$.
2. When $a\_0 = 0$ and $a\_1 > 1$, its direct parent is $\frac{p}{q-p} = \[0; a\_1 - 1, a\_2, \dots, a\_k\]$.
3. And when $a\_0 = 0$ and $a\_1 = 1$, its direct parent is $\frac{p}{q-p} = \[a\_2; a\_3, \dots, a\_k\]$.

Correspondingly, children of $\frac{p}{q} = \[a\_0; a\_1, \dots, a\_k\]$ are

1. $\frac{p+q}{q}=1+\frac{p}{q}$, which is $\[a\_0+1; a\_1, \dots, a\_k\]$,
2. $\frac{p}{p+q} = \frac{1}{1+\frac{q}{p}}$, which is $\[0, 1, a\_0, a\_1, \dots, a\_k\]$ for $a\_0 > 0$ and $\[0, a\_1+1, a\_2, \dots, a\_k\]$ for $a\_0=0$.

Noteworthy, if we enumerate vertices of the Calkin-Wilf tree in the breadth-first search order (that is, the root has a number $1$, and the children of the vertex $v$ have indices $2v$ and $2v+1$ correspondingly), the index of the rational number in the Calkin-Wilf tree would be the same as in the Stern-Brocot tree.

Thus, numbers on the same levels of the Stern-Brocot tree and the Calkin-Wilf tree are the same, but their ordering differs through the [bit-reversal permutation](https://en.wikipedia.org/wiki/Bit-reversal_permutation).

## Convergence[¶](https://cp-algorithms.com#convergence)

For the number $r$ and its $k$-th convergent $r\_k=\frac{p\_k}{q\_k}$ the following formula stands:

In particular, it means that

and

From this we can conclude that

The latter inequality is due to the fact that $r\_k$ and $r\_{k+1}$ are generally located on different sides of $r$, thus

## Detailed explanation

To estimate $|r-r\_k|$, we start by estimating the difference between adjacent convergents. By definition,

Replacing $p\_k$ and $q\_k$ in the numerator with their recurrences, we get

thus the numerator of $r\_k - r\_{k-1}$ is always the negated numerator of $r\_{k-1} - r\_{k-2}$. It, in turn, equals to $1$ for

thus

This yields an alternative representation of $r\_k$ as a partial sum of infinite series:

From the recurrent relation it follows that $q\_k$ monotonously increases at least as fast as Fibonacci numbers, thus

is always well-defined, as the underlying series always converge. Noteworthy, the residual series

has the same sign as $(-1)^k$ due to how fast $q\_i q\_{i-1}$ decreases. Hence even-indexed $r\_k$ approach $r$ from below while odd-indexed $r\_k$ approach it from above:

From this picture we can see that

thus the distance between $r$ and $r\_k$ is never larger than the distance between $r\_k$ and $r\_{k+1}$:

Extended Euclidean?

You're given $A, B, C \in \mathbb Z$. Find $x, y \in \mathbb Z$ such that $Ax + By = C$.

## Solution

Although this problem is typically solved with the [extended Euclidean algorithm](https://cp-algorithms.com/extended-euclid-algorithm.html), there is a simple and straightforward solution with continued fractions.

Let $\frac{A}{B}=\[a\_0; a\_1, \dots, a\_k\]$. It was proved above that $p\_k q\_{k-1} - p\_{k-1} q\_k = (-1)^{k-1}$. Substituting $p\_k$ and $q\_k$ with $A$ and $B$, we get

where $g = \gcd(A, B)$. If $C$ is divisible by $g$, then the solution is $x = (-1)^{k-1}\frac{C}{g} q\_{k-1}$ and $y = (-1)^{k}\frac{C}{g} p\_{k-1}$.

```
# return (x, y) such that Ax+By=C
# assumes that such (x, y) exists
def dio(A, B, C):
    p, q = convergents(fraction(A, B))
    C //= A // p[-1] # divide by gcd(A, B)
    t = (-1) if len(p) % 2 else 1
    return t*C*q[-2], -t*C*p[-2]
```
## Linear fractional transformations[¶](https://cp-algorithms.com#linear-fractional-transformations)

Another important concept for continued fractions are the so-called [linear fractional transformations](https://en.wikipedia.org/wiki/Linear_fractional_transformation).

Definition

A **linear fractional transformation** is a function $f : \mathbb R \to \mathbb R$ such that $f(x) = \frac{ax+b}{cx+d}$ for some $a,b,c,d \in \mathbb R$.

A composition $(L\_0 \circ L\_1)(x) = L\_0(L\_1(x))$ of linear fractional transforms $L\_0(x)=\frac{a\_0 x + b\_0}{c\_0 x + d\_0}$ and $L\_1(x)=\frac{a\_1 x + b\_1}{c\_1 x + d\_1}$ is itself a linear fractional transform:

Inverse of a linear fractional transform, is also a linear fractional transform:

You're given an array of positive integers $a\_1, \dots, a\_n$. You need to answer $m$ queries. Each query is to compute $\[a\_l; a\_{l+1}, \dots, a\_r\]$.

## Solution

We can solve this problem with the segment tree if we're able to concatenate continued fractions.

It's generally true that $\[a\_0; a\_1, \dots, a\_k, b\_0, b\_1, \dots, b\_k\] = \[a\_0; a\_1, \dots, a\_k, \[b\_1; b\_2, \dots, b\_k\]\]$.

Let's denote $L\_{k}(x) = \[a\_k; x\] = a\_k + \frac{1}{x} = \frac{a\_k\cdot x+1}{1\cdot x + 0}$. Note that $L\_k(\infty) = a\_k$. In this notion, it holds that

Thus, the problem boils down to the computation of

Composition of transforms is associative, so it's possible to compute in each node of a segment tree the composition of transforms in its subtree.

Linear fractional transformation of a continued fraction

Let $L(x) = \frac{ax+b}{cx+d}$. Compute the continued fraction representation $\[b\_0; b\_1, \dots, b\_m\]$ of $L(A)$ for $A=\[a\_0; a\_1, \dots, a\_n\]$.

*This allows to compute $A + \frac{p}{q} = \frac{qA + p}{q}$ and $A \cdot \frac{p}{q} = \frac{p A}{q}$ for any $\frac{p}{q}$.*

## Solution

As we noted above, $\[a\_0; a\_1, \dots, a\_k\] = (L\_{a\_0} \circ L\_{a\_1} \circ \dots \circ L\_{a\_k})(\infty)$, hence $L(\[a\_0; a\_1, \dots, a\_k\]) = (L \circ L\_{a\_0} \circ L\_{a\_1} \circ \dots L\_{a\_k})(\infty)$.

Hence, by consequentially adding $L\_{a\_0}$, $L\_{a\_1}$ and so on we would be able to compute

Since $L(x)$ is invertible, it is also monotonous in $x$. Therefore, for any $x \geq 0$ it holds that $L(\frac{p\_k x + p\_{k-1}}{q\_k x + q\_{k-1}})$ is between $L(\frac{p\_k}{q\_k}) = \frac{a\_k}{c\_k}$ and $L(\frac{p\_{k-1}}{q\_{k-1}}) = \frac{b\_k}{d\_k}$.

Moreover, for $x=\[a\_{k+1}; \dots, a\_n\]$ it is equal to $L(A)$. Hence, $b\_0 = \lfloor L(A) \rfloor$ is between $\lfloor L(\frac{p\_k}{q\_k}) \rfloor$ and $\lfloor L(\frac{p\_{k-1}}{q\_{k-1}}) \rfloor$. When they're equal, they're also equal to $b\_0$.

Note that $L(A) = (L\_{b\_0} \circ L\_{b\_1} \circ \dots \circ L\_{b\_m})(\infty)$. Knowing $b\_0$, we can compose $L\_{b\_0}^{-1}$ with the current transform and continue adding $L\_{a\_{k+1}}$, $L\_{a\_{k+2}}$ and so on, looking for new floors to agree, from which we would be able to deduce $b\_1$ and so on until we recover all values of $\[b\_0; b\_1, \dots, b\_m\]$.

Continued fraction arithmetics

Let $A=\[a\_0; a\_1, \dots, a\_n\]$ and $B=\[b\_0; b\_1, \dots, b\_m\]$. Compute the continued fraction representations of $A+B$ and $A \cdot B$.

## Solution

Idea here is similar to the previous problem, but instead of $L(x) = \frac{ax+b}{cx+d}$ you should consider bilinear fractional transform $L(x, y) = \frac{axy+bx+cy+d}{exy+fx+gy+h}$.

Rather than $L(x) \mapsto L(L\_{a\_k}(x))$ you would change your current transform as $L(x, y) \mapsto L(L\_{a\_k}(x), y)$ or $L(x, y) \mapsto L(x, L\_{b\_k}(y))$.

Then, you check if $\lfloor \frac{a}{e} \rfloor = \lfloor \frac{b}{f} \rfloor = \lfloor \frac{c}{g} \rfloor = \lfloor \frac{d}{h} \rfloor$ and if they all agree, you use this value as $c\_k$ in the resulting fraction and change the transform as

Definition

A continued fraction $x = \[a\_0; a\_1, \dots\]$ is said to be **periodic** if $x = \[a\_0; a\_1, \dots, a\_k, x\]$ for some $k$.

A continued fraction $x = \[a\_0; a\_1, \dots\]$ is said to be **eventually periodic** if $x = \[a\_0; a\_1, \dots, a\_k, y\]$, where $y$ is periodic.

For $x = \[1; 1, 1, \dots\]$ it holds that $x = 1 + \frac{1}{x}$, thus $x^2 = x + 1$. There is a generic connection between periodic continued fractions and quadratic equations. Consider the following equation:

On one hand, this equation means that the continued fraction representation of $x$ is periodic with the period $k+1$.

On the other hand, using the formula for convergents, this equation means that

That is, $x$ is a linear fractional transformation of itself. It follows from the equation that $x$ is a root of the second degree equation:

Similar reasoning stands for continued fractions that are eventually periodic, that is $x = \[a\_0; a\_1, \dots, a\_k, y\]$ for $y=\[b\_0; b\_1, \dots, b\_k, y\]$. Indeed, from first equation we derive that $x = L\_0(y)$ and from second equation that $y = L\_1(y)$, where $L\_0$ and $L\_1$ are linear fractional transformations. Therefore,

One can further prove (and it was first done by Lagrange) that for arbitrary quadratic equation $ax^2+bx+c=0$ with integer coefficients, its solution $x$ is an eventually periodic continued fraction.

Quadratic irrationality

Find the continued fraction of $\alpha = \frac{x+y\sqrt{n}}{z}$ where $x, y, z, n \in \mathbb Z$ and $n > 0$ is not a perfect square.

## Solution

For the $k$-th complete quotient $s\_k$ of the number it generally holds that

Therefore,

Multiplying the numerator and denominator by $(xq\_k - zp\_k) - q\_k y \sqrt n$, we'll get rid of $\sqrt n$ in the denominator, thus the complete quotients are of form

Let's find $s\_{k+1}$, assuming that $s\_k$ is known.

First of all, $a\_k = \lfloor s\_k \rfloor = \left\lfloor \frac{x\_k + y\_k \lfloor \sqrt n \rfloor}{z\_k} \right\rfloor$. Then,

Thus, if we denote $t\_k = x\_k - y\_k a\_k$, it will hold that

Nice thing about such representation is that if we reduce $x\_{k+1}, y\_{k+1}, z\_{k+1}$ by their greatest common divisor, the result would be unique. Therefore, we may use it to check whether the current state has already been repeated and also to check where was the previous index that had this state.

Below is the code to compute the continued fraction representation for $\alpha = \sqrt n$:

```
# compute the continued fraction of sqrt(n)
def sqrt(n):
    n0 = math.floor(math.sqrt(n))
    x, y, z = 1, 0, 1
    a = []
    def step(x, y, z):
        a.append((x * n0 + y) // z)
        t = y - a[-1]*z
        x, y, z = -z*x, z*t, t**2 - n*x**2
        g = math.gcd(x, math.gcd(y, z))
        return x // g, y // g, z // g
    used = dict()
    for i in range(n):
        used[x, y, z] = i
        x, y, z = step(x, y, z)
        if (x, y, z) in used:
            return a
```
Using the same `step` function but different initial $x$, $y$ and $z$ it is possible to compute it for arbitrary $\frac{x+y \sqrt{n}}{z}$.

You're given $x$ and $k$, $x$ is not a perfect square. Let $\sqrt x = \[a\_0; a\_1, \dots\]$, find $\frac{p\_k}{q\_k}=\[a\_0; a\_1, \dots, a\_k\]$ for $0 \leq k \leq 10^9$.

## Solution

After computing the period of $\sqrt x$, it is possible to compute $a\_k$ using binary exponentiation on the linear fractional transformation induced by the continued fraction representation. To find the resulting transformation, you compress the period of size $T$ into a single transformation and repeat it $\lfloor \frac{k-1}{T}\rfloor$ times, after which you manually combine it with the remaining transformations.

```
x, k = map(int, input().split())
mod = 10**9+7
# compose (A[0]*x + A[1]) / (A[2]*x + A[3]) and (B[0]*x + B[1]) / (B[2]*x + B[3])
def combine(A, B):
    return [t % mod for t in [A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3]]]
A = [1, 0, 0, 1] # (x + 0) / (0*x + 1) = x
a = sqrt(x)
T = len(a) - 1 # period of a
# apply ak + 1/x = (ak*x+1)/(1x+0) to (Ax + B) / (Cx + D)
for i in reversed(range(1, len(a))):
    A = combine([a[i], 1, 1, 0], A)
def bpow(A, n):
    return [1, 0, 0, 1] if not n else combine(A, bpow(A, n-1)) if n % 2 else bpow(combine(A, A), n // 2)
C = (0, 1, 0, 0) # = 1 / 0
while k % T:
    i = k % T
    C = combine([a[i], 1, 1, 0], C)
    k -= 1
C = combine(bpow(A, k // T), C)
C = combine([a[0], 1, 1, 0], C)
print(str(C[1]) + '/' + str(C[3]))
```
## Geometric interpretation[¶](https://cp-algorithms.com#geometric-interpretation)

Let $\vec r\_k = (q\_k;p\_k)$ for the convergent $r\_k = \frac{p\_k}{q\_k}$. Then, the following recurrence holds:

Let $\vec r = (1;r)$. Then, each vector $(x;y)$ corresponds to the number that is equal to its slope coefficient $\frac{y}{x}$.

With the notion of [pseudoscalar product](https://cp-algorithms.com/geometry/basic-geometry.html) $(x\_1;y\_1) \times (x\_2;y\_2) = x\_1 y\_2 - x\_2 y\_1$, it can be shown (see the explanation below) that

The last equation is due to the fact that $r\_{k-1}$ and $r\_{k-2}$ lie on the different sides of $r$, thus pseudoscalar products of $\vec r\_{k-1}$ and $\vec r\_{k-2}$ with $\vec r$ have distinct signs. With $a\_k = \lfloor s\_k \rfloor$ in mind, formula for $\vec r\_k$ now looks like

Note that $\vec r\_k \times r = (q;p) \times (1;r) = qr - p$, thus

## Explanation

As we have already noted, $a\_k = \lfloor s\_k \rfloor$, where $s\_k = \[a\_k; a\_{k+1}, a\_{k+2}, \dots\]$. On the other hand, from the convergent recurrence we derive that

In vector form, it rewrites as

meaning that $\vec r$ and $s\_k \vec r\_{k-1} + \vec r\_{k-2}$ are collinear (that is, have the same slope coefficient). Taking the [pseudoscalar product](https://cp-algorithms.com/geometry/basic-geometry.html) of both parts with $\vec r$, we get

which yields the final formula

Nose stretching algorithm

Each time you add $\vec r\_{k-1}$ to the vector $\vec p$, the value of $\vec p \times \vec r$ is increased by $\vec r\_{k-1} \times \vec r$.

Thus, $a\_k=\lfloor s\_k \rfloor$ is the maximum integer number of $\vec r\_{k-1}$ vectors that can be added to $\vec r\_{k-2}$ without changing the sign of the cross product with $\vec r$.

In other words, $a\_k$ is the maximum integer number of times you can add $\vec r\_{k-1}$ to $\vec r\_{k-2}$ without crossing the line defined by $\vec r$:

On the picture above, $\vec r\_2 = (4;3)$ is obtained by repeatedly adding $\vec r\_1 = (1;1)$ to $\vec r\_0 = (1;0)$.

When it is not possible to further add $\vec r\_1$ to $\vec r\_0$ without crossing the $y=rx$ line, we go to the other side and repeatedly add $\vec r\_2$ to $\vec r\_1$ to obtain $\vec r\_3 = (9;7)$.

This procedure generates exponentially longer vectors, that approach the line.

For this property, the procedure of generating consequent convergent vectors was dubbed the **nose stretching algorithm** by Boris Delaunay.

If we look on the triangle drawn on points $\vec r\_{k-2}$, $\vec r\_{k}$ and $\vec 0$ we will notice that its doubled area is

Combined with the [Pick's theorem](https://cp-algorithms.com/geometry/picks-theorem.html), it means that there are no lattice points strictly inside the triangle and the only lattice points on its border are $\vec 0$ and $\vec r\_{k-2} + t \cdot \vec r\_{k-1}$ for all integer $t$ such that $0 \leq t \leq a\_k$. When joined for all possible $k$ it means that there are no integer points in the space between polygons formed by even-indexed and odd-indexed convergent vectors.

This, in turn, means that $\vec r\_k$ with odd coefficients form a convex hull of lattice points with $x \geq 0$ above the line $y=rx$, while $\vec r\_k$ with even coefficients form a convex hull of lattice points with $x > 0$ below the line $y=rx$.

Definition

These polygons are also known as **Klein polygons**, named after Felix Klein who first suggested this geometric interpretation to the continued fractions.

## Problem examples[¶](https://cp-algorithms.com#problem-examples)

Now that the most important facts and concepts were introduced, it is time to delve into specific problem examples.

Convex hull under the line

Find the convex hull of lattice points $(x;y)$ such that $0 \leq x \leq N$ and $0 \leq y \leq rx$ for $r=\[a\_0;a\_1,\dots,a\_k\]=\frac{p\_k}{q\_k}$.

## Solution

If we were considering the unbounded set $0 \leq x$, the upper convex hull would be given by the line $y=rx$ itself.

However, with additional constraint $x \leq N$ we'd need to eventually deviate from the line to maintain proper convex hull.

Let $t = \lfloor \frac{N}{q\_k}\rfloor$, then first $t$ lattice points on the hull after $(0;0)$ are $\alpha \cdot (q\_k; p\_k)$ for integer $1 \leq \alpha \leq t$.

However $(t+1)(q\_k; p\_k)$ can't be next lattice point since $(t+1)q\_k$ is greater than $N$.

To get to the next lattice points in the hull, we should get to the point $(x;y)$ which diverges from $y=rx$ by the smallest margin, while maintaining $x \leq N$.

Let $(x; y)$ be the last current point in the convex hull. Then the next point $(x'; y')$ is such that $x' \leq N$ and $(x'; y') - (x; y) = (\Delta x; \Delta y)$ is as close to the line $y=rx$ as possible. In other words, $(\Delta x; \Delta y)$ maximizes $r \Delta x - \Delta y$ subject to $\Delta x \leq N - x$ and $\Delta y \leq r \Delta x$.

Points like that lie on the convex hull of lattice points below $y=rx$. In other words, $(\Delta x; \Delta y)$ must be a lower semiconvergent of $r$.

That being said, $(\Delta x; \Delta y)$ is of form $(q\_{i-1}; p\_{i-1}) + t \cdot (q\_i; p\_i)$ for some odd number $i$ and $0 \leq t \< a\_i$.

To find such $i$, we can traverse all possible $i$ starting from the largest one and use $t = \lfloor \frac{N-x-q\_{i-1}}{q\_i} \rfloor$ for $i$ such that $N-x-q\_{i-1} \geq 0$.

With $(\Delta x; \Delta y) = (q\_{i-1}; p\_{i-1}) + t \cdot (q\_i; p\_i)$, the condition $\Delta y \leq r \Delta x$ would be preserved by semiconvergent properties.

And $t \< a\_i$ would hold because we already exhausted semiconvergents obtained from $i+2$, hence $x + q\_{i-1} + a\_i q\_i = x+q\_{i+1}$ is greater than $N$.

Now that we may add $(\Delta x; \Delta y)$, to $(x;y)$ for $k = \lfloor \frac{N-x}{\Delta x} \rfloor$ times before we exceed $N$, after which we would try the next semiconvergent.

```
// returns [ah, ph, qh] such that points r[i]=(ph[i], qh[i]) constitute upper convex hull
// of lattice points on 0 <= x <= N and 0 <= y <= r * x, where r = [a0; a1, a2, ...]
// and there are ah[i]-1 integer points on the segment between r[i] and r[i+1]
auto hull(auto a, int N) {
    auto [p, q] = convergents(a);
    int t = N / q.back();
    vector ah = {t};
    vector ph = {0, t*p.back()};
    vector qh = {0, t*q.back()};
    for(int i = q.size() - 1; i >= 0; i--) {
        if(i % 2) {
            while(qh.back() + q[i - 1] <= N) {
                t = (N - qh.back() - q[i - 1]) / q[i];
                int dp = p[i - 1] + t * p[i];
                int dq = q[i - 1] + t * q[i];
                int k = (N - qh.back()) / dq;
                ah.push_back(k);
                ph.push_back(ph.back() + k * dp);
                qh.push_back(qh.back() + k * dq);
            }
        }
    }
    return make_tuple(ah, ph, qh);
}
```
```
# returns [ah, ph, qh] such that points r[i]=(ph[i], qh[i]) constitute upper convex hull
# of lattice points on 0 <= x <= N and 0 <= y <= r * x, where r = [a0; a1, a2, ...]
# and there are ah[i]-1 integer points on the segment between r[i] and r[i+1]
def hull(a, N):
    p, q = convergents(a)
    t = N // q[-1]
    ah = [t]
    ph = [0, t*p[-1]]
    qh = [0, t*q[-1]]
    for i in reversed(range(len(q))):
        if i % 2 == 1:
            while qh[-1] + q[i-1] <= N:
                t = (N - qh[-1] - q[i-1]) // q[i]
                dp = p[i-1] + t*p[i]
                dq = q[i-1] + t*q[i]
                k = (N - qh[-1]) // dq
                ah.append(k)
                ph.append(ph[-1] + k * dp)
                qh.append(qh[-1] + k * dq)
    return ah, ph, qh
```
You're given integer numbers $A$, $B$ and $N$. Find $x \geq 0$ and $y \geq 0$ such that $Ax + By \leq N$ and $Ax + By$ is the maximum possible.

## Solution

In this problem it holds that $1 \leq A, B, N \leq 2 \cdot 10^9$, so it can be solved in $O(\sqrt N)$. However, there is $O(\log N)$ solution with continued fractions.

For our convenience, we will invert the direction of $x$ by doing a substitution $x \mapsto \lfloor \frac{N}{A}\rfloor - x$, so that now we need to find the point $(x; y)$ such that $0 \leq x \leq \lfloor \frac{N}{A} \rfloor$, $By - Ax \leq N \;\bmod\; A$ and $By - Ax$ is the maximum possible. Optimal $y$ for each $x$ has a value of $\lfloor \frac{Ax + (N \bmod A)}{B} \rfloor$.

To treat it more generically, we will write a function that finds the best point on $0 \leq x \leq N$ and $y = \lfloor \frac{Ax+B}{C} \rfloor$.

Core solution idea in this problem essentially repeats the previous problem, but instead of using lower semiconvergents to diverge from line, you use upper semiconvergents to get closer to the line without crossing it and without violating $x \leq N$. Unfortunately, unlike the previous problem, you need to make sure that you don't cross the $y=\frac{Ax+B}{C}$ line while getting closer to it, so you should keep it in mind when calculating semiconvergent's coefficient $t$.

```
# (x, y) such that y = (A*x+B) // C,
# Cy - Ax is max and 0 <= x <= N.
def closest(A, B, C, N):
    # y <= (A*x + B)/C <=> diff(x, y) <= B
    def diff(x, y):
        return C*y-A*x
    a = fraction(A, C)
    p, q = convergents(a)
    ph = [B // C]
    qh = [0]
    for i in range(2, len(q) - 1):
        if i % 2 == 0:
            while diff(qh[-1] + q[i+1], ph[-1] + p[i+1]) <= B:
                t = 1 + (diff(qh[-1] + q[i-1], ph[-1] + p[i-1]) - B - 1) // abs(diff(q[i], p[i]))
                dp = p[i-1] + t*p[i]
                dq = q[i-1] + t*q[i]
                k = (N - qh[-1]) // dq
                if k == 0:
                    return qh[-1], ph[-1]
                if diff(dq, dp) != 0:
                    k = min(k, (B - diff(qh[-1], ph[-1])) // diff(dq, dp))
                qh.append(qh[-1] + k*dq)
                ph.append(ph[-1] + k*dp)
    return qh[-1], ph[-1]
def solve(A, B, N):
    x, y = closest(A, N % A, B, N // A)
    return N // A - x, y
```
Compute $\sum\limits\_{x=1}^N \lfloor ex \rfloor$, where $e = \[2; 1, 2, 1, 1, 4, 1, 1, 6, 1, \dots, 1, 2n, 1, \dots\]$ is the Euler's number and $N \leq 10^{4000}$.

## Solution

This sum is equal to the number of lattice point $(x;y)$ such that $1 \leq x \leq N$ and $1 \leq y \leq ex$.

After constructing the convex hull of the points below $y=ex$, this number can be computed using [Pick's theorem](https://cp-algorithms.com/geometry/picks-theorem.html):

```
// sum floor(k * x) for k in [1, N] and x = [a0; a1, a2, ...]
int sum_floor(auto a, int N) {
    N++;
    auto [ah, ph, qh] = hull(a, N);
    // The number of lattice points within a vertical right trapezoid
    // on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has
    // a+1 integer points on the segment (0; y1) - (dx; y2).
    auto picks = [](int y1, int y2, int dx, int a) {
        int b = y1 + y2 + a + dx;
        int A = (y1 + y2) * dx;
        return (A - b + 2) / 2 + b - (y2 + 1);
    };
    int ans = 0;
    for(size_t i = 1; i < qh.size(); i++) {
        ans += picks(ph[i - 1], ph[i], qh[i] - qh[i - 1], ah[i - 1]);
    }
    return ans - N;
}
```
```
# sum floor(k * x) for k in [1, N] and x = [a0; a1, a2, ...]
def sum_floor(a, N):
    N += 1
    ah, ph, qh = hull(a, N)
    # The number of lattice points within a vertical right trapezoid
    # on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has
    # a+1 integer points on the segment (0; y1) - (dx; y2).
    def picks(y1, y2, dx, a):
        b = y1 + y2 + a + dx
        A = (y1 + y2) * dx
        return (A - b + 2) // 2 + b - (y2 + 1)
    ans = 0
    for i in range(1, len(qh)):
        ans += picks(ph[i-1], ph[i], qh[i]-qh[i-1], ah[i-1])
    return ans - N
```
Given $p$, $q$ and $n$, compute $\sum\limits\_{i=1}^n \[p \cdot i \bmod q\]$.

## Solution

This problem reduces to the previous one if you note that $a \bmod b = a - \lfloor \frac{a}{b} \rfloor b$. With this fact, the sum reduces to

However, summing up $\lfloor rx \rfloor$ for $x$ from $1$ to $N$ is something that we're capable of from the previous problem.

```
void solve(int p, int q, int N) {
    cout << p * N * (N + 1) / 2 - q * sum_floor(fraction(p, q), N) << "\n";
}
```
```
def solve(p, q, N):
    return p * N * (N + 1) // 2 - q * sum_floor(fraction(p, q), N)
```
Given $N$, $M$, $A$ and $B$, compute $\sum\limits\_{i=0}^{N-1} \lfloor \frac{A \cdot i + B}{M} \rfloor$.

## Solution

This is the most technically troublesome problem so far.

It is possible to use the same approach and construct the full convex hull of points below the line $y = \frac{Ax+B}{M}$.

We already know how to solve it for $B = 0$. Moreover, we already know how to construct this convex hull up to the closest lattice point to this line on $\[0, N-1\]$ segment (this is done in the "Crime and Punishment" problem above.

Now we should note that once we reached the closest point to the line, we can just assume that the line in fact passes through the closest point, as there are no other lattice points on $\[0, N-1\]$ in between the actual line and the line moved slightly below to pass through the closest point.

That being said, to construct the full convex hull below the line $y=\frac{Ax+B}{M}$ on $\[0, N-1\]$, we can construct it up to the closest point to the line on $\[0, N-1\]$ and then continue as if the line passes through this point, reusing algorithm for constructing convex hull with $B=0$:

```
# hull of lattice (x, y) such that C*y <= A*x+B
def hull(A, B, C, N):
    def diff(x, y):
        return C*y-A*x
    a = fraction(A, C)
    p, q = convergents(a)
    ah = []
    ph = [B // C]
    qh = [0]
    def insert(dq, dp):
        k = (N - qh[-1]) // dq
        if diff(dq, dp) > 0:
            k = min(k, (B - diff(qh[-1], ph[-1])) // diff(dq, dp))
        ah.append(k)
        qh.append(qh[-1] + k*dq)
        ph.append(ph[-1] + k*dp)
    for i in range(1, len(q) - 1):
        if i % 2 == 0:
            while diff(qh[-1] + q[i+1], ph[-1] + p[i+1]) <= B:
                t = (B - diff(qh[-1] + q[i+1], ph[-1] + p[i+1])) // abs(diff(q[i], p[i]))
                dp = p[i+1] - t*p[i]
                dq = q[i+1] - t*q[i]
                if dq < 0 or qh[-1] + dq > N:
                    break
                insert(dq, dp)
    insert(q[-1], p[-1])
    for i in reversed(range(len(q))):
        if i % 2 == 1:
            while qh[-1] + q[i-1] <= N:
                t = (N - qh[-1] - q[i-1]) // q[i]
                dp = p[i-1] + t*p[i]
                dq = q[i-1] + t*q[i]
                insert(dq, dp)
    return ah, ph, qh
```
There is a rational number $\frac{p}{q}$ such that $1 \leq p, q \leq 10^9$. You may ask the value of $p q^{-1}$ modulo $m \sim 10^9$ for several prime numbers $m$. Recover $\frac{p}{q}$.

*Equivalent formulation:* Find $x$ that delivers the minimum of $Ax \;\bmod\; M$ for $1 \leq x \leq N$.

## Solution

Due to Chinese remainder theorem, asking the result modulo several prime numbers is the same as asking it modulo their product. Due to this, without loss of generality we'll assume that we know the remainder modulo sufficiently large number $m$.

There could be several possible solutions $(p, q)$ to $p \equiv qr \pmod m$ for a given remainder $r$. However, if $(p\_1, q\_1)$ and $(p\_2, q\_2)$ are both the solutions then it also holds that $p\_1 q\_2 \equiv p\_2 q\_1 \pmod m$. Assuming that $\frac{p\_1}{q\_1} \neq \frac{p\_2}{q\_2}$ it means that $|p\_1 q\_2 - p\_2 q\_1|$ is at least $m$.

In the statement we were told that $1 \leq p, q \leq 10^9$, so if both $p\_1, q\_1$ and $p\_2, q\_2$ are at most $10^9$, then the difference is at most $10^{18}$. For $m > 10^{18}$ it means that the solution $\frac{p}{q}$ with $1 \leq p, q \leq 10^9$ is unique, as a rational number.

So, the problem boils down, given $r$ modulo $m$, to finding any $q$ such that $1 \leq q \leq 10^9$ and $qr \;\bmod\; m \leq 10^9$.

This is effectively the same as finding $q$ that delivers the minimum possible $qr \bmod m$ for $1 \leq q \leq 10^9$.

For $qr = km + b$ it means that we need to find a pair $(q, m)$ such that $1 \leq q \leq 10^9$ and $qr - km \geq 0$ is the minimum possible.

Since $m$ is constant, we can divide by it and further restate it as find $q$ such that $1 \leq q \leq 10^9$ and $\frac{r}{m} q - k \geq 0$ is the minimum possible.

In terms of continued fractions it means that $\frac{k}{q}$ is the best diophantine approximation to $\frac{r}{m}$ and it is sufficient to only check lower semiconvergents of $\frac{r}{m}$.

```
# find Q that minimizes Q*r mod m for 1 <= k <= n < m 
def mod_min(r, n, m):
    a = fraction(r, m)
    p, q = convergents(a)
    for i in range(2, len(q)):
        if i % 2 == 1 and (i + 1 == len(q) or q[i+1] > n):
            t = (n - q[i-1]) // q[i]
            return q[i-1] + t*q[i]
```