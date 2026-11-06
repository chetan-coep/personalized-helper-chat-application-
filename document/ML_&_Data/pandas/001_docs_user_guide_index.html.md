---
id: "pandas_001"
technology: "pandas"
category: "ML & Data"
title: "User Guide — pandas 3.1.0 documentation"
doc_order: 1
source_url: "https://pandas.pydata.org/docs/user_guide/index.html"
language: "en"
retrieved_at: "2026-11-03 17:57:12"
content_hash: "ec52162c2d4d0154c57b941746cc5213ef1f443a86349c269cf9e8dbadadcee1"
---

# User Guide — pandas 3.1.0 documentation

Source: https://pandas.pydata.org/docs/user_guide/index.html

---

# User Guide[#](https://pandas.pydata.org#user-guide)

The User Guide covers all of pandas by topic area. Each of the subsections introduces a topic (such as “working with missing data”), and discusses how pandas approaches the problem, with many examples throughout.

Users brand-new to pandas should start with [10 minutes to pandas](https://pandas.pydata.org/10min.html#min).

For a high level summary of the pandas fundamentals, see [Intro to data structures](https://pandas.pydata.org/dsintro.html#dsintro) and [Essential basic functionality](https://pandas.pydata.org/basics.html#basics).

Further information on any specific method can be obtained in the
[API reference](https://pandas.pydata.org/reference/index.html#api).

## How to read these guides[#](https://pandas.pydata.org#how-to-read-these-guides)

In these guides you will see input code inside code blocks such as:

```
import pandas as pd
pd.DataFrame({'A': [1, 2, 3]})
```
or:

```
In [1]: import pandas as pd
In [2]: pd.DataFrame({'A': [1, 2, 3]})
Out[2]: 
   A
0  1
1  2
2  3
```
The first block is a standard Python input, while in the second the `In [1]:`
indicates the input is inside a [notebook](https://jupyter.org). In Jupyter Notebooks the last line is printed and plots are shown inline.

For example:

```
In [3]: a = 1
In [4]: a
Out[4]: 1
```
is equivalent to:

```
a = 1
print(a)
```