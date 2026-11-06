---
id: "pandas_007"
technology: "pandas"
category: "ML & Data"
title: "Indexing and selecting data — pandas 3.1.0 documentation"
doc_order: 7
source_url: "https://pandas.pydata.org/docs/user_guide/indexing.html"
language: "en"
retrieved_at: "2026-11-03 17:57:19"
content_hash: "b8029e93f709ae0c235c4c4f85ae2a806d9d6c9ecfd79cf1ce6f2ba446580ae8"
---

# Indexing and selecting data — pandas 3.1.0 documentation

Source: https://pandas.pydata.org/docs/user_guide/indexing.html

---

# Indexing and selecting data[#](https://pandas.pydata.org#indexing-and-selecting-data)

The axis labeling information in pandas objects serves many purposes:

- Identifies data (i.e. provides *metadata*) using known indicators,
important for analysis, visualization, and interactive console display.
- Enables automatic and explicit data alignment.
- Allows intuitive getting and setting of subsets of the data set.

In this section, we will focus on the final point: namely, how to slice, dice, and generally get and set subsets of pandas objects. The primary focus will be on Series and DataFrame as they have received more development attention in this area.

Note

The Python and NumPy indexing operators `[]` and attribute operator `.`
provide quick and easy access to pandas data structures across a wide range
of use cases. This makes interactive work intuitive, as there’s little new
to learn if you already know how to deal with Python dictionaries and NumPy
arrays. However, since the type of the data to be accessed isn’t known in
advance, directly using standard operators has some optimization limits. For
production code, we recommended that you take advantage of the optimized
pandas data access methods exposed in this chapter.

See the [MultiIndex / Advanced Indexing](https://pandas.pydata.org/advanced.html#advanced) for `MultiIndex` and more advanced indexing documentation.

See the [cookbook](https://pandas.pydata.org/cookbook.html#cookbook-selection) for some advanced strategies.

## Different choices for indexing[#](https://pandas.pydata.org#different-choices-for-indexing)

Object selection has had a number of user-requested additions in order to support more explicit location based indexing. pandas now supports three types of multi-axis indexing.

- `.loc` is primarily label based, but may also be used with a boolean array. `.loc` will raise `KeyError` when the items are not found. Allowed inputs are:
  - A single label, e.g. `5` or `'a'` (Note that `5` is interpreted as a *label* of the index. This use is **not** an integer position along the
index.).
  - A list or array of labels `['a', 'b', 'c']`.
  - A slice object with labels `'a':'f'` (Note that contrary to usual Python
slices, **both** the start and the stop are included, when present in the
index! See [Slicing with labels](https://pandas.pydata.org#indexing-slicing-with-labels) and [Endpoints are inclusive](https://pandas.pydata.org/advanced.html#advanced-endpoints-are-inclusive).)
  - A boolean array (any `NA` values will be treated as `False`).
  - A `callable` function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above).
  - A tuple of row (and column) indices whose elements are one of the above inputs.
See more at [Selection by Label](https://pandas.pydata.org#indexing-label).
- `.iloc` is primarily integer position based (from `0` to `length-1` of the axis), but may also be used with a boolean
array. `.iloc` will raise `IndexError` if a requested
indexer is out-of-bounds, except *slice* indexers which allow
out-of-bounds indexing.  (this conforms with Python/NumPy *slice* semantics).  Allowed inputs are:
  - An integer e.g. `5`.
  - A list or array of integers `[4, 3, 0]`.
  - A slice object with ints `1:7`.
  - A boolean array (any `NA` values will be treated as `False`).
  - A `callable` function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above).
  - A tuple of row (and column) indices whose elements are one of the above inputs.
See more at [Selection by Position](https://pandas.pydata.org#indexing-integer), [Advanced Indexing](https://pandas.pydata.org/advanced.html#advanced) and [Advanced
Hierarchical](https://pandas.pydata.org/advanced.html#advanced-advanced-hierarchical).
- `.loc`, `.iloc`, and also `[]` indexing can accept a `callable` as indexer. See more at [Selection By Callable](https://pandas.pydata.org#indexing-callable).
Note Destructuring tuple keys into row (and column) indexes occurs
*before* callables are applied, so you cannot return a tuple from
a callable to index both rows and columns.

Getting values from an object with multi-axes selection uses the following
notation (using `.loc` as an example, but the following applies to `.iloc` as
well). Any of the axes accessors may be the null slice `:`. Axes left out of
the specification are assumed to be `:`, e.g. `p.loc['a']` is equivalent to
`p.loc['a', :]`.

```
In [1]: ser = pd.Series(range(5), index=list("abcde"))
In [2]: ser.loc[["a", "c", "e"]]
Out[2]: 
a    0
c    2
e    4
dtype: int64
In [3]: df = pd.DataFrame(np.arange(25).reshape(5, 5), index=list("abcde"), columns=list("abcde"))
In [4]: df.loc[["a", "c", "e"], ["b", "d"]]
Out[4]: 
    b   d
a   1   3
c  11  13
e  21  23
```
## Basics[#](https://pandas.pydata.org#basics)

As mentioned when introducing the data structures in the [last section](https://pandas.pydata.org/basics.html#basics), the primary function of indexing with `[]` (a.k.a. `__getitem__`
for those familiar with implementing class behavior in Python) is selecting out
lower-dimensional slices. The following table shows return type values when
indexing pandas objects with `[]`:

| Object Type | Selection | Return Value Type | 
|---|---|---|
| Series | `series[label]` | scalar value | 
| DataFrame | `frame[colname]` | `Series` corresponding to colname | 
| DataFrame | `frame[[colname]]` | `DataFrame` with columns corresponding to `[colname]` | 
| DataFrame | `frame[list_of_colnames]` | `DataFrame` with columns corresponding to `list_of_colnames` | 

The same principle applies to label-based selection with `.loc`: a
list-like of labels preserves the corresponding axis (so
`df.loc[:, ["A"]]` returns a `DataFrame`, even when the list contains a
single label), while a scalar label reduces the axis when labels on that
axis are unique (so `df.loc[:, "A"]` typically returns a `Series`; if
`"A"` is duplicated on the axis, a `DataFrame` is returned instead).
See [Selection by label](https://pandas.pydata.org#indexing-label) for details.

Here we construct a simple time series data set to use for illustrating the indexing functionality:

```
In [5]: dates = pd.date_range('1/1/2000', periods=8)
In [6]: df = pd.DataFrame(np.random.randn(8, 4),
   ...:                   index=dates, columns=['A', 'B', 'C', 'D'])
   ...: 
In [7]: df
Out[7]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885
```
Note

None of the indexing functionality is time series specific unless specifically stated.

Thus, as per above, we have the most basic indexing using `[]`:

```
In [8]: s = df['A']
In [9]: s[dates[5]]
Out[9]: np.float64(-0.6736897080883706)
```
You can pass a list of columns to `[]` to select columns in that order.
If a column is not contained in the DataFrame, an exception will be
raised. Multiple columns can also be set in this manner:

```
In [10]: df
Out[10]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885
In [11]: df[['B', 'A']] = df[['A', 'B']]
In [12]: df
Out[12]: 
                   A         B         C         D
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804
2000-01-04 -0.706771  0.721555 -1.039575  0.271860
2000-01-05  0.567020 -0.424972  0.276232 -1.087401
2000-01-06  0.113648 -0.673690 -1.478427  0.524988
2000-01-07  0.577046  0.404705 -1.715002 -1.039268
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885
```
You may find this useful for applying a transform (in-place) to a subset of the columns.

Warning

pandas aligns all AXES when setting `Series` and `DataFrame` from `.loc`.

This will **not** modify `df` because the column alignment is before value assignment.

```
In [13]: df[['A', 'B']]
Out[13]: 
                   A         B
2000-01-01 -0.282863  0.469112
2000-01-02 -0.173215  1.212112
2000-01-03 -2.104569 -0.861849
2000-01-04 -0.706771  0.721555
2000-01-05  0.567020 -0.424972
2000-01-06  0.113648 -0.673690
2000-01-07  0.577046  0.404705
2000-01-08 -1.157892 -0.370647
In [14]: df.loc[:, ['B', 'A']] = df[['A', 'B']]
In [15]: df[['A', 'B']]
Out[15]: 
                   A         B
2000-01-01 -0.282863  0.469112
2000-01-02 -0.173215  1.212112
2000-01-03 -2.104569 -0.861849
2000-01-04 -0.706771  0.721555
2000-01-05  0.567020 -0.424972
2000-01-06  0.113648 -0.673690
2000-01-07  0.577046  0.404705
2000-01-08 -1.157892 -0.370647
```
The correct way to swap column values is by using raw values:

```
In [16]: df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
In [17]: df[['A', 'B']]
Out[17]: 
                   A         B
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
2000-01-04  0.721555 -0.706771
2000-01-05 -0.424972  0.567020
2000-01-06 -0.673690  0.113648
2000-01-07  0.404705  0.577046
2000-01-08 -0.370647 -1.157892
```
However, pandas does not align AXES when setting `Series` and `DataFrame` from `.iloc`
because `.iloc` operates by position.

This will modify `df` because the column alignment is not done before value assignment.

```
In [18]: df[['A', 'B']]
Out[18]: 
                   A         B
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
2000-01-04  0.721555 -0.706771
2000-01-05 -0.424972  0.567020
2000-01-06 -0.673690  0.113648
2000-01-07  0.404705  0.577046
2000-01-08 -0.370647 -1.157892
In [19]: df.iloc[:, [1, 0]] = df[['A', 'B']]
In [20]: df[['A','B']]
Out[20]: 
                   A         B
2000-01-01 -0.282863  0.469112
2000-01-02 -0.173215  1.212112
2000-01-03 -2.104569 -0.861849
2000-01-04 -0.706771  0.721555
2000-01-05  0.567020 -0.424972
2000-01-06  0.113648 -0.673690
2000-01-07  0.577046  0.404705
2000-01-08 -1.157892 -0.370647
```
### Selecting columns with `select`[#](https://pandas.pydata.org#selecting-columns-with-select)

[`DataFrame.select()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.select.html#pandas.DataFrame.select) returns a DataFrame with the requested columns in the
given order, similar to passing a list of columns to `[]`. As a method, it
can be used within a chain of operations. Columns can be given as individual
arguments or as a single list:

```
In [21]: df.select('B', 'A')
Out[21]: 
                   B         A
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
2000-01-04  0.721555 -0.706771
2000-01-05 -0.424972  0.567020
2000-01-06 -0.673690  0.113648
2000-01-07  0.404705  0.577046
2000-01-08 -0.370647 -1.157892
In [22]: df.select(['B', 'A'])
Out[22]: 
                   B         A
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
2000-01-04  0.721555 -0.706771
2000-01-05 -0.424972  0.567020
2000-01-06 -0.673690  0.113648
2000-01-07  0.404705  0.577046
2000-01-08 -0.370647 -1.157892
```
In addition to existing columns, computed columns can be included via
[`pandas.col()`](https://pandas.pydata.org/reference/api/pandas.col.html#pandas.col) expressions or callables. A positional expression keeps the
name of the underlying column, while a keyword argument names the resulting
column. Later arguments can refer to columns computed earlier in the same call:

```
In [23]: df.select('A', pd.col('B') * 2, C=pd.col('A') + pd.col('B'), D=pd.col('C') > 0)
Out[23]: 
                   A         B         C      D
2000-01-01 -0.282863  0.938225  0.655361   True
2000-01-02 -0.173215  2.424224  2.251009   True
2000-01-03 -2.104569 -1.723698 -3.828267  False
2000-01-04 -0.706771  1.443110  0.736339   True
2000-01-05  0.567020 -0.849945 -0.282924  False
2000-01-06  0.113648 -1.347379 -1.233731  False
2000-01-07  0.577046  0.809410  1.386456   True
2000-01-08 -1.157892 -0.741294 -1.899186  False
```
A computed column with the same name as an existing column replaces it for later arguments. It does not replace a column that was already selected, so the result can contain duplicate column labels:

```
In [24]: df.select('A', A=pd.col('A') * 2, E=pd.col('A'))
Out[24]: 
                   A         A         E
2000-01-01 -0.282863 -0.565727 -0.565727
2000-01-02 -0.173215 -0.346429 -0.346429
2000-01-03 -2.104569 -4.209138 -4.209138
2000-01-04 -0.706771 -1.413542 -1.413542
2000-01-05  0.567020  1.134041  1.134041
2000-01-06  0.113648  0.227297  0.227297
2000-01-07  0.577046  1.154092  1.154092
2000-01-08 -1.157892 -2.315785 -2.315785
```
## Attribute access[#](https://pandas.pydata.org#attribute-access)

`Series` or  column on a `DataFrame` directly
as an attribute:

```
In [25]: sa = pd.Series([1, 2, 3], index=list('abc'))
In [26]: dfa = df.copy()
```
```
In [27]: sa.b
Out[27]: np.int64(2)
In [28]: dfa.A
Out[28]: 
2000-01-01   -0.282863
2000-01-02   -0.173215
2000-01-03   -2.104569
2000-01-04   -0.706771
2000-01-05    0.567020
2000-01-06    0.113648
2000-01-07    0.577046
2000-01-08   -1.157892
Freq: D, Name: A, dtype: float64
```
```
In [29]: sa.a = 5
In [30]: sa
Out[30]: 
a    5
b    2
c    3
dtype: int64
In [31]: dfa.A = list(range(len(dfa.index)))  # ok if A already exists
In [32]: dfa
Out[32]: 
            A         B         C         D
2000-01-01  0  0.469112 -1.509059 -1.135632
2000-01-02  1  1.212112  0.119209 -1.044236
2000-01-03  2 -0.861849 -0.494929  1.071804
2000-01-04  3  0.721555 -1.039575  0.271860
2000-01-05  4 -0.424972  0.276232 -1.087401
2000-01-06  5 -0.673690 -1.478427  0.524988
2000-01-07  6  0.404705 -1.715002 -1.039268
2000-01-08  7 -0.370647 -1.344312  0.844885
In [33]: dfa['A'] = list(range(len(dfa.index)))  # use this form to create a new column
In [34]: dfa
Out[34]: 
            A         B         C         D
2000-01-01  0  0.469112 -1.509059 -1.135632
2000-01-02  1  1.212112  0.119209 -1.044236
2000-01-03  2 -0.861849 -0.494929  1.071804
2000-01-04  3  0.721555 -1.039575  0.271860
2000-01-05  4 -0.424972  0.276232 -1.087401
2000-01-06  5 -0.673690 -1.478427  0.524988
2000-01-07  6  0.404705 -1.715002 -1.039268
2000-01-08  7 -0.370647 -1.344312  0.844885
```
Warning

- You can use this access only if the index element is a valid Python identifier, e.g. `s.1` is not allowed.
See [here for an explanation of valid identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).
- The attribute will not be available if it conflicts with an existing method name, e.g. `s.min` is not allowed, but `s['min']` is possible.
- Similarly, the attribute will not be available if it conflicts with any of the following list: `index`, `major_axis`, `minor_axis`, `items`.
- In any of these cases, standard indexing will still work, e.g. `s['1']`, `s['min']`, and `s['index']` will
access the corresponding element or column.

If you are using the IPython environment, you may also use tab-completion to see these accessible attributes.

You can also assign a `dict` to a row of a `DataFrame`:

```
In [35]: x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
In [36]: x.iloc[1] = {'x': 9, 'y': 99}
In [37]: x
Out[37]: 
   x   y
0  1   3
1  9  99
2  3   5
```
You can use attribute access to modify an existing element of a Series or column of a DataFrame, but be careful;
if you try to use attribute access to create a new column, it creates a new attribute rather than a
new column and will this raise a `UserWarning`:

```
In [38]: df_new = pd.DataFrame({'one': [1., 2., 3.]})
In [39]: df_new.two = [4, 5, 6]
In [40]: df_new
Out[40]: 
   one
0  1.0
1  2.0
2  3.0
```
## Slicing ranges[#](https://pandas.pydata.org#slicing-ranges)

The most robust and consistent way of slicing ranges along arbitrary axes is
described in the [Selection by Position](https://pandas.pydata.org#indexing-integer) section
detailing the `.iloc` method. For now, we explain the semantics of slicing using the `[]` operator.

With Series, the syntax works exactly as with an ndarray, returning a slice of the values and the corresponding labels:

```
In [41]: s[:5]
Out[41]: 
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
Freq: D, Name: A, dtype: float64
In [42]: s[::2]
Out[42]: 
2000-01-01    0.469112
2000-01-03   -0.861849
2000-01-05   -0.424972
2000-01-07    0.404705
Freq: 2D, Name: A, dtype: float64
In [43]: s[::-1]
Out[43]: 
2000-01-08   -0.370647
2000-01-07    0.404705
2000-01-06   -0.673690
2000-01-05   -0.424972
2000-01-04    0.721555
2000-01-03   -0.861849
2000-01-02    1.212112
2000-01-01    0.469112
Freq: -1D, Name: A, dtype: float64
```
Note that setting works as well:

```
In [44]: s2 = s.copy()
In [45]: s2[:5] = 0
In [46]: s2
Out[46]: 
2000-01-01    0.000000
2000-01-02    0.000000
2000-01-03    0.000000
2000-01-04    0.000000
2000-01-05    0.000000
2000-01-06   -0.673690
2000-01-07    0.404705
2000-01-08   -0.370647
Freq: D, Name: A, dtype: float64
```
With DataFrame, slicing inside of `[]` **slices the rows**. This is provided
largely as a convenience since it is such a common operation.

```
In [47]: df[:3]
Out[47]: 
                   A         B         C         D
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804
In [48]: df[::-1]
Out[48]: 
                   A         B         C         D
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885
2000-01-07  0.577046  0.404705 -1.715002 -1.039268
2000-01-06  0.113648 -0.673690 -1.478427  0.524988
2000-01-05  0.567020 -0.424972  0.276232 -1.087401
2000-01-04 -0.706771  0.721555 -1.039575  0.271860
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632
```
## Selection by label[#](https://pandas.pydata.org#selection-by-label)

Warning

`.loc` is strict when you present slicers that are not compatible (or convertible) with the index type. For example
using integers in a `DatetimeIndex`. These will raise a `TypeError`.

In \[49\]: dfl = pd.DataFrame(np.random.randn(5, 4), ....: columns=list('ABCD'), ....: index=pd.date\_range('20130101', periods=5)) ....: In \[50\]: dfl Out\[50\]: A B C D 2013-01-01 1.075770 -0.109050 1.643563 -1.469388 2013-01-02 0.357021 -0.674600 -1.776904 -0.968914 2013-01-03 -1.294524 0.413738 0.276662 -0.472035 2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061 2013-01-05 0.895717 0.805244 -1.206412 2.565646 In \[51\]: dfl.loc\[2:3\] --------------------------------------------------------------------------- TypeError Traceback (most recent call last) Cell In\[51\], line 1 ----> 1 dfl.loc\[2:3\] File \~/work/pandas/pandas/pandas/core/indexing.py:1342, in \_LocationIndexer.\_\_getitem\_\_(self, key) 1340 maybe\_callable = com.apply\_if\_callable(key, self.obj) 1341 maybe\_callable = self.\_raise\_callable\_usage(key, maybe\_callable) -> 1342 return self.\_getitem\_axis(maybe\_callable, axis=axis) File \~/work/pandas/pandas/pandas/core/indexing.py:1914, in \_LocIndexer.\_getitem\_axis(self, key, axis) 1912 if isinstance(key, slice): 1913 self.\_validate\_key(key, axis) -> 1914 return self.\_get\_slice\_axis(key, axis=axis) 1915 elif com.is\_bool\_indexer(key): 1916 return self.\_getbool\_axis(key, axis=axis) File \~/work/pandas/pandas/pandas/core/indexing.py:1978, in \_LocIndexer.\_get\_slice\_axis(self, slice\_obj, axis) 1975 return obj.copy(deep=False) 1977 labels = obj.\_get\_axis(axis) -> 1978 indexer = labels.slice\_indexer(slice\_obj.start, slice\_obj.stop, slice\_obj.step) 1980 if isinstance(indexer, slice): 1981 return self.obj.\_slice(indexer, axis=axis) File \~/work/pandas/pandas/pandas/core/indexes/datetimes.py:2316, in DatetimeIndex.slice\_indexer(self, start, end, step) 2308 # GH#33146 if start and end are combinations of str and None and Index is not 2309 # monotonic, we can not use Index.slice\_indexer because it does not honor the 2310 # actual elements, is only searching for start and end 2311 if ( 2312 check\_str\_or\_none(start) 2313 or check\_str\_or\_none(end) 2314 or self.is\_monotonic\_increasing 2315 ): -> 2316 return Index.slice\_indexer(self, start, end, step) 2318 mask = np.array(True) 2319 in\_index = True File \~/work/pandas/pandas/pandas/core/indexes/base.py:7136, in Index.slice\_indexer(self, start, end, step) 7085 def slice\_indexer( 7086 self, 7087 start: Hashable | None = None, 7088 end: Hashable | None = None, 7089 step: int | None = None, 7090 ) -> slice: 7091 """ 7092 Compute the slice indexer for input labels and step. 7093 (...) 7134 slice(1, 3, None) 7135 """ -> 7136 start\_slice, end\_slice = self.slice\_locs(start, end, step=step) 7138 # return a slice 7139 if not is\_scalar(start\_slice): File \~/work/pandas/pandas/pandas/core/indexes/base.py:7413, in Index.slice\_locs(self, start, end, step) 7411 start\_slice = None 7412 if start is not None: -> 7413 start\_slice = self.get\_slice\_bound(start, "left") 7414 if start\_slice is None: 7415 start\_slice = 0 File \~/work/pandas/pandas/pandas/core/indexes/base.py:7299, in Index.get\_slice\_bound(self, label, side) 7295 original\_label = label 7297 # For datetime indices label may be a string that has to be converted 7298 # to datetime boundary according to its resolution. -> 7299 label = self.\_maybe\_cast\_slice\_bound(label, side) 7301 # we need to look up the label 7302 try: File \~/work/pandas/pandas/pandas/core/indexes/datetimes.py:2276, in DatetimeIndex.\_maybe\_cast\_slice\_bound(self, label, side) 2267 label = Timestamp(label).to\_pydatetime() 2268 warnings.warn( 2269 # GH#35830 deprecate last remaining inconsistent date treatment 2270 "Slicing with a datetime.date object is deprecated. " (...) 2273 stacklevel=find\_stack\_level(), 2274 ) -> 2276 label = super().\_maybe\_cast\_slice\_bound(label, side) 2277 self.\_data.\_assert\_tzawareness\_compat(label) 2278 return Timestamp(label) File \~/work/pandas/pandas/pandas/core/indexes/datetimelike.py:628, in DatetimeIndexOpsMixin.\_maybe\_cast\_slice\_bound(self, label, side) 626 return lower if side == "left" else upper 627 elif not isinstance(label, self.\_data.\_recognized\_scalars): --> 628 self.\_raise\_invalid\_indexer("slice", label) 630 return label File \~/work/pandas/pandas/pandas/core/indexes/base.py:4317, in Index.\_raise\_invalid\_indexer(self, form, key, reraise) 4315 if reraise is not lib.no\_default: 4316 raise TypeError(msg) from reraise -> 4317 raise TypeError(msg) TypeError: cannot do slice indexing on DatetimeIndex with these indexers \[2\] of type int

String likes in slicing *can* be convertible to the type of the index and lead to natural slicing.

```
In [52]: dfl.loc['20130102':'20130104']
Out[52]: 
                   A         B         C         D
2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2013-01-03 -1.294524  0.413738  0.276662 -0.472035
2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
```
pandas provides a suite of methods in order to have **purely label based indexing**. This is a strict inclusion based protocol.
Every label asked for must be in the index, or a `KeyError` will be raised.
When slicing, both the start bound **AND** the stop bound are *included*, if present in the index.
Integers are valid labels, but they refer to the label **and not the position**.

The `.loc` attribute is the primary access method. The following are valid inputs:

- A single label, e.g. `5` or `'a'` (Note that `5` is interpreted as a *label* of the index. This use is **not** an integer position along the index.).
- A list or array of labels `['a', 'b', 'c']`.
- A slice object with labels `'a':'f'`. Note that contrary to usual Python
slices, **both** the start and the stop are included, when present in the
index! See [Slicing with labels](https://pandas.pydata.org#indexing-slicing-with-labels).
- A boolean array.
- A `callable`, see [Selection By Callable](https://pandas.pydata.org#indexing-callable).

```
In [53]: s1 = pd.Series(np.random.randn(6), index=list('abcdef'))
In [54]: s1
Out[54]: 
a    1.431256
b    1.340309
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64
In [55]: s1.loc['c':]
Out[55]: 
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64
In [56]: s1.loc['b']
Out[56]: np.float64(1.3403088497993827)
```
Note that setting works as well:

```
In [57]: s1.loc['c':] = 0
In [58]: s1
Out[58]: 
a    1.431256
b    1.340309
c    0.000000
d    0.000000
e    0.000000
f    0.000000
dtype: float64
```
With a DataFrame:

```
In [59]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                    index=list('abcdef'),
   ....:                    columns=list('ABCD'))
   ....: 
In [60]: df1
Out[60]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
b  1.130127 -1.436737 -1.413681  1.607920
c  1.024180  0.569605  0.875906 -2.211372
d  0.974466 -2.006747 -0.410001 -0.078638
e  0.545952 -1.219217 -1.226825  0.769804
f -1.281247 -0.727707 -0.121306 -0.097883
In [61]: df1.loc[['a', 'b', 'd'], :]
Out[61]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
b  1.130127 -1.436737 -1.413681  1.607920
d  0.974466 -2.006747 -0.410001 -0.078638
```
Accessing via label slices:

```
In [62]: df1.loc['d':, 'A':'C']
Out[62]: 
          A         B         C
d  0.974466 -2.006747 -0.410001
e  0.545952 -1.219217 -1.226825
f -1.281247 -0.727707 -0.121306
```
For getting a cross section using a label (equivalent to `df.xs('a')`):

```
In [63]: df1.loc['a']
Out[63]: 
A    0.132003
B   -0.827317
C   -0.076467
D   -1.187678
Name: a, dtype: float64
```
For getting values with a boolean array:

```
In [64]: df1.loc['a'] > 0
Out[64]: 
A     True
B    False
C    False
D    False
Name: a, dtype: bool
In [65]: df1.loc[:, df1.loc['a'] > 0]
Out[65]: 
          A
a  0.132003
b  1.130127
c  1.024180
d  0.974466
e  0.545952
f -1.281247
```
NA values in a boolean array propagate as `False`:

```
In [66]: mask = pd.array([True, False, True, False, pd.NA, False], dtype="boolean")
In [67]: mask
Out[67]: 
<BooleanArray>
[True, False, True, False, <NA>, False]
Length: 6, dtype: boolean
In [68]: df1[mask]
Out[68]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
c  1.024180  0.569605  0.875906 -2.211372
```
For getting a value explicitly:

```
# this is also equivalent to ``df1.at['a','A']``
In [69]: df1.loc['a', 'A']
Out[69]: np.float64(0.13200317033032932)
```
### Slicing with labels[#](https://pandas.pydata.org#slicing-with-labels)

When using `.loc` with slices, if both the start and the stop labels are
present in the index, then elements *located* between the two (including them)
are returned:

```
In [70]: s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])
In [71]: s.loc[3:5]
Out[71]: 
3    b
2    c
5    d
dtype: str
```
If the index is sorted, and can be compared against start and stop labels,
then slicing will still work as expected, by selecting labels which *rank*
between the two:

```
In [72]: s.sort_index()
Out[72]: 
0    a
2    c
3    b
4    e
5    d
dtype: str
In [73]: s.sort_index().loc[1:6]
Out[73]: 
2    c
3    b
4    e
5    d
dtype: str
```
However, if at least one of the two is absent *and* the index is not sorted, an
error will be raised (since doing otherwise would be computationally expensive,
as well as potentially ambiguous for mixed type indexes). For instance, in the
above example, `s.loc[1:6]` would raise `KeyError`.

For the rationale behind this behavior, see
[Endpoints are inclusive](https://pandas.pydata.org/advanced.html#advanced-endpoints-are-inclusive).

```
In [74]: s = pd.Series(list('abcdef'), index=[0, 3, 2, 5, 4, 2])
In [75]: s.loc[3:5]
Out[75]: 
3    b
2    c
5    d
dtype: str
```
Also, if the index has duplicate labels *and* either the start or the stop label is duplicated,
an error will be raised. For instance, in the above example, `s.loc[2:5]` would raise a `KeyError`.

For more information about duplicate labels, see
[Duplicate Labels](https://pandas.pydata.org/duplicates.html#duplicates).

When using a slice with a step, such as `.loc[start:stop:step]`, note that
*start* and *stop* are interpreted as **labels**, while *step* is applied over
the **positional index** within that label range. This means a stepped slice
will behave differently than using the labels `range(start, stop, step)` when
the index is not contiguous integers.

For example, in a `Series` with a non-contiguous integer index:

```
In [76]: s = pd.Series(range(10), index=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
In [77]: s.loc[10:50:5]              # (10), then skip 5 positions → 35 only
Out[77]: 
10    2
35    7
dtype: int64
In [78]: s.loc[[10, 15, 20, 25]]     # explicit label selection
Out[78]: 
10    2
15    3
20    4
25    5
dtype: int64
```
The first applies *step* across **positional locations** between the start/stop
labels. The second selects each label directly.

Similarly, with a string-based index, the behavior is identical:

```
In [79]: s = pd.Series(range(10), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
In [80]: s.loc['b':'i':2]            # Start at 'b' (position 1), stop at 'i' (position 8), step 2 positions → 'b', 'd', 'f', 'h'
Out[80]: 
b    1
d    3
f    5
h    7
dtype: int64
In [81]: s.loc[['b', 'd', 'f', 'h']] # explicit label selection
Out[81]: 
b    1
d    3
f    5
h    7
dtype: int64
```
In both cases, *start* and *stop* determine the label boundaries (inclusive),
while *step* skips positions within that range, regardless of the index type.

## Selection by position[#](https://pandas.pydata.org#selection-by-position)

pandas provides a suite of methods in order to get **purely integer based indexing**. The semantics follow closely Python and NumPy slicing. These are `0-based` indexing. When slicing, the start bound is *included*, while the upper bound is *excluded*. Trying to use a non-integer, even a **valid** label will raise an `IndexError`.

The `.iloc` attribute is the primary access method. The following are valid inputs:

- An integer e.g. `5`.
- A list or array of integers `[4, 3, 0]`.
- A slice object with ints `1:7`.
- A boolean array.
- A `callable`, see [Selection By Callable](https://pandas.pydata.org#indexing-callable).
- A tuple of row (and column) indexes, whose elements are one of the above types.

```
In [82]: s1 = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))
In [83]: s1
Out[83]: 
0    0.695775
2    0.341734
4    0.959726
6   -1.110336
8   -0.619976
dtype: float64
In [84]: s1.iloc[:3]
Out[84]: 
0    0.695775
2    0.341734
4    0.959726
dtype: float64
In [85]: s1.iloc[3]
Out[85]: np.float64(-1.110336102891167)
```
Note that setting works as well:

```
In [86]: s1.iloc[:3] = 0
In [87]: s1
Out[87]: 
0    0.000000
2    0.000000
4    0.000000
6   -1.110336
8   -0.619976
dtype: float64
```
With a DataFrame:

```
In [88]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                    index=list(range(0, 12, 2)),
   ....:                    columns=list(range(0, 8, 2)))
   ....: 
In [89]: df1
Out[89]: 
           0         2         4         6
0   0.149748 -0.732339  0.687738  0.176444
2   0.403310 -0.154951  0.301624 -2.179861
4  -1.369849 -0.954208  1.462696 -1.743161
6  -0.826591 -0.345352  1.314232  0.690579
8   0.995761  2.396780  0.014871  3.357427
10 -0.317441 -1.236269  0.896171 -0.487602
```
Select via integer slicing:

```
In [90]: df1.iloc[:3]
Out[90]: 
          0         2         4         6
0  0.149748 -0.732339  0.687738  0.176444
2  0.403310 -0.154951  0.301624 -2.179861
4 -1.369849 -0.954208  1.462696 -1.743161
In [91]: df1.iloc[1:5, 2:4]
Out[91]: 
          4         6
2  0.301624 -2.179861
4  1.462696 -1.743161
6  1.314232  0.690579
8  0.014871  3.357427
```
Select via integer list:

```
In [92]: df1.iloc[[1, 3, 5], [1, 3]]
Out[92]: 
           2         6
2  -0.154951 -2.179861
6  -0.345352  0.690579
10 -1.236269 -0.487602
```
```
In [93]: df1.iloc[1:3, :]
Out[93]: 
          0         2         4         6
2  0.403310 -0.154951  0.301624 -2.179861
4 -1.369849 -0.954208  1.462696 -1.743161
```
```
In [94]: df1.iloc[:, 1:3]
Out[94]: 
           2         4
0  -0.732339  0.687738
2  -0.154951  0.301624
4  -0.954208  1.462696
6  -0.345352  1.314232
8   2.396780  0.014871
10 -1.236269  0.896171
```
```
# this is also equivalent to ``df1.iat[1,1]``
In [95]: df1.iloc[1, 1]
Out[95]: np.float64(-0.1549507744249032)
```
For getting a cross section using an integer position (equiv to `df.xs(1)`):

```
In [96]: df1.iloc[1]
Out[96]: 
0    0.403310
2   -0.154951
4    0.301624
6   -2.179861
Name: 2, dtype: float64
```
Out of range slice indexes are handled gracefully just as in Python/NumPy.

```
# these are allowed in Python/NumPy.
In [97]: x = list('abcdef')
In [98]: x
Out[98]: ['a', 'b', 'c', 'd', 'e', 'f']
In [99]: x[4:10]
Out[99]: ['e', 'f']
In [100]: x[8:10]
Out[100]: []
In [101]: s = pd.Series(x)
In [102]: s
Out[102]: 
0    a
1    b
2    c
3    d
4    e
5    f
dtype: str
In [103]: s.iloc[4:10]
Out[103]: 
4    e
5    f
dtype: str
In [104]: s.iloc[8:10]
Out[104]: Series([], dtype: str)
```
Note that using slices that go out of bounds can result in an empty axis (e.g. an empty DataFrame being returned).

```
In [105]: dfl = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))
In [106]: dfl
Out[106]: 
          A         B
0 -0.082240 -2.182937
1  0.380396  0.084844
2  0.432390  1.519970
3 -0.493662  0.600178
4  0.274230  0.132885
In [107]: dfl.iloc[:, 2:3]
Out[107]: 
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]
In [108]: dfl.iloc[:, 1:3]
Out[108]: 
          B
0 -2.182937
1  0.084844
2  1.519970
3  0.600178
4  0.132885
In [109]: dfl.iloc[4:6]
Out[109]: 
         A         B
4  0.27423  0.132885
```
A single indexer that is out of bounds will raise an `IndexError`.
A list of indexers where any element is out of bounds will raise an
`IndexError`.

```
In [110]: dfl.iloc[[4, 5, 6]]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
File ~/work/pandas/pandas/pandas/core/indexing.py:2394, in _iLocIndexer._get_list_axis(self, key, axis)
   2393 try:
-> 2394     return self.obj.take(key, axis=axis)
   2395 except IndexError as err:
   2396     # re-raise with different error message, e.g. test_getitem_ndarray_3d
File ~/work/pandas/pandas/pandas/core/generic.py:4139, in NDFrame.take(self, indices, axis, **kwargs)
   4137             return self.copy(deep=False)
   4138 
-> 4139         new_data = self._mgr.take(
   4140             indices,
File ~/work/pandas/pandas/pandas/core/internals/managers.py:1091, in BaseBlockManager.take(self, indexer, axis, verify)
   1090 n = self.shape[axis]
-> 1091 indexer = maybe_convert_indices(indexer, n, verify=verify)
   1093 new_labels = self.axes[axis].take(indexer)
File ~/work/pandas/pandas/pandas/core/indexers/utils.py:284, in maybe_convert_indices(indices, n, verify)
    283     if mask.any():
--> 284         raise IndexError("indices are out-of-bounds")
    285 return indices
IndexError: indices are out-of-bounds
The above exception was the direct cause of the following exception:
IndexError                                Traceback (most recent call last)
Cell In[110], line 1
----> 1 dfl.iloc[[4, 5, 6]]
File ~/work/pandas/pandas/pandas/core/indexing.py:1342, in _LocationIndexer.__getitem__(self, key)
   1340 maybe_callable = com.apply_if_callable(key, self.obj)
   1341 maybe_callable = self._raise_callable_usage(key, maybe_callable)
-> 1342 return self._getitem_axis(maybe_callable, axis=axis)
File ~/work/pandas/pandas/pandas/core/indexing.py:2423, in _iLocIndexer._getitem_axis(self, key, axis)
   2421 # a list of integers
   2422 elif is_list_like_indexer(key):
-> 2423     return self._get_list_axis(key, axis=axis)
   2425 # a single integer
   2426 else:
   2427     key = item_from_zerodim(key)
File ~/work/pandas/pandas/pandas/core/indexing.py:2397, in _iLocIndexer._get_list_axis(self, key, axis)
   2394     return self.obj.take(key, axis=axis)
   2395 except IndexError as err:
   2396     # re-raise with different error message, e.g. test_getitem_ndarray_3d
-> 2397     raise IndexError("positional indexers are out-of-bounds") from err
IndexError: positional indexers are out-of-bounds
```
```
In [111]: dfl.iloc[:, 4]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[111], line 1
----> 1 dfl.iloc[:, 4]
File ~/work/pandas/pandas/pandas/core/indexing.py:1335, in _LocationIndexer.__getitem__(self, key)
   1333     if self._is_scalar_access(key):
   1334         return self.obj._get_value(*key, takeable=self._takeable)
-> 1335     return self._getitem_tuple(key)
   1336 else:
   1337     # we by definition only have the 0th axis
   1338     axis = self.axis or 0
File ~/work/pandas/pandas/pandas/core/indexing.py:2370, in _iLocIndexer._getitem_tuple(self, tup)
   2369 def _getitem_tuple(self, tup: tuple):
-> 2370     tup = self._validate_tuple_indexer(tup)
   2371     with suppress(IndexingError):
   2372         return self._getitem_lowerdim(tup)
File ~/work/pandas/pandas/pandas/core/indexing.py:1124, in _LocationIndexer._validate_tuple_indexer(self, key)
   1122 for i, k in enumerate(key):
   1123     try:
-> 1124         self._validate_key(k, i)
   1125     except ValueError as err:
   1126         raise ValueError(
   1127             f"Location based indexing can only have [{self._valid_types}] types"
   1128         ) from err
File ~/work/pandas/pandas/pandas/core/indexing.py:2264, in _iLocIndexer._validate_key(self, key, axis)
   2262     return
   2263 elif is_integer(key):
-> 2264     self._validate_integer(key, axis)
   2265 elif isinstance(key, tuple):
   2266     # a tuple should already have been caught by this point
   2267     # so don't treat a tuple as a valid indexer
   2268     raise IndexingError("Too many indexers")
File ~/work/pandas/pandas/pandas/core/indexing.py:2365, in _iLocIndexer._validate_integer(self, key, axis)
   2363 len_axis = len(self.obj._get_axis(axis))
   2364 if key >= len_axis or key < -len_axis:
-> 2365     raise IndexError("single positional indexer is out-of-bounds")
IndexError: single positional indexer is out-of-bounds
```
## Selection by callable[#](https://pandas.pydata.org#selection-by-callable)

`.loc`, `.iloc`, and also `[]` indexing can accept a `callable` as indexer.
The `callable` must be a function with one argument (the calling Series or DataFrame) that returns valid output for indexing.

Note

For `.iloc` indexing, returning a tuple from the callable is
not supported, since tuple destructuring for row and column indexes
occurs *before* applying callables.

```
In [112]: df1 = pd.DataFrame(np.random.randn(6, 4),
   .....:                    index=list('abcdef'),
   .....:                    columns=list('ABCD'))
   .....: 
In [113]: df1
Out[113]: 
          A         B         C         D
a -0.023688  2.410179  1.450520  0.206053
b -0.251905 -2.213588  1.063327  1.266143
c  0.299368 -0.863838  0.408204 -1.048089
d -0.025747 -0.988387  0.094055  1.262731
e  1.289997  0.082423 -0.055758  0.536580
f -0.489682  0.369374 -0.034571 -2.484478
In [114]: df1.loc[lambda df: df['A'] > 0, :]
Out[114]: 
          A         B         C         D
c  0.299368 -0.863838  0.408204 -1.048089
e  1.289997  0.082423 -0.055758  0.536580
In [115]: df1.loc[:, lambda df: ['A', 'B']]
Out[115]: 
          A         B
a -0.023688  2.410179
b -0.251905 -2.213588
c  0.299368 -0.863838
d -0.025747 -0.988387
e  1.289997  0.082423
f -0.489682  0.369374
In [116]: df1.iloc[:, lambda df: [0, 1]]
Out[116]: 
          A         B
a -0.023688  2.410179
b -0.251905 -2.213588
c  0.299368 -0.863838
d -0.025747 -0.988387
e  1.289997  0.082423
f -0.489682  0.369374
In [117]: df1[lambda df: df.columns[0]]
Out[117]: 
a   -0.023688
b   -0.251905
c    0.299368
d   -0.025747
e    1.289997
f   -0.489682
Name: A, dtype: float64
```
You can use callable indexing in `Series`.

```
In [118]: df1['A'].loc[lambda s: s > 0]
Out[118]: 
c    0.299368
e    1.289997
Name: A, dtype: float64
```
Using these methods / indexers, you can chain data selection operations without using a temporary variable.

```
In [119]: bb = pd.read_csv('data/baseball.csv', index_col='id')
In [120]: (bb.groupby(['year', 'team']).sum(numeric_only=True)
   .....:    .loc[lambda df: df['r'] > 100])
   .....: 
Out[120]: 
           stint    g    ab    r    h  ...   ibb   hbp    sh    sf  gidp
year team                              ...                              
2007 CIN       6  379   745  101  203  ...  14.0   1.0   1.0  15.0  18.0
     DET       5  301  1062  162  283  ...   3.0  10.0   4.0   8.0  28.0
     HOU       4  311   926  109  218  ...   3.0   9.0  16.0   6.0  17.0
     LAN      11  413  1021  153  293  ...   8.0   9.0   3.0   8.0  29.0
     NYN      13  622  1854  240  509  ...  24.0  23.0  18.0  15.0  48.0
     SFN       5  482  1305  198  337  ...  51.0   8.0  16.0   6.0  41.0
     TEX       2  198   729  115  200  ...   4.0   5.0   2.0   8.0  16.0
     TOR       4  459  1408  187  378  ...  16.0  12.0   4.0  16.0  38.0
[8 rows x 18 columns]
```
## Combining positional and label-based indexing[#](https://pandas.pydata.org#combining-positional-and-label-based-indexing)

If you wish to get the 0th and the 2nd elements from the index in the ‘A’ column, you can do:

```
In [121]: dfd = pd.DataFrame({'A': [1, 2, 3],
   .....:                     'B': [4, 5, 6]},
   .....:                    index=list('abc'))
   .....: 
In [122]: dfd
Out[122]: 
   A  B
a  1  4
b  2  5
c  3  6
In [123]: dfd.loc[dfd.index[[0, 2]], 'A']
Out[123]: 
a    1
c    3
Name: A, dtype: int64
```
This can also be expressed using `.iloc`, by explicitly getting locations on the indexers, and using
*positional* indexing to select things.

```
In [124]: dfd.iloc[[0, 2], dfd.columns.get_loc('A')]
Out[124]: 
a    1
c    3
Name: A, dtype: int64
```
For getting *multiple* indexers, using `.get_indexer`:

```
In [125]: dfd.iloc[[0, 2], dfd.columns.get_indexer(['A', 'B'])]
Out[125]: 
   A  B
a  1  4
c  3  6
```
### Reindexing[#](https://pandas.pydata.org#reindexing)

The idiomatic way to achieve selecting potentially not-found elements is via `.reindex()`. See also the section on [reindexing](https://pandas.pydata.org/basics.html#basics-reindexing).

```
In [126]: s = pd.Series([1, 2, 3])
In [127]: s.reindex([1, 2, 3])
Out[127]: 
1    2.0
2    3.0
3    NaN
dtype: float64
```
Alternatively, if you want to select only *valid* keys, the following is idiomatic and efficient; it is guaranteed to preserve the dtype of the selection.

```
In [128]: labels = [1, 2, 3]
In [129]: s.loc[s.index.intersection(labels)]
Out[129]: 
1    2
2    3
dtype: int64
```
Having a duplicated index will raise for a `.reindex()`:

```
In [130]: s = pd.Series(np.arange(4), index=['a', 'a', 'b', 'c'])
In [131]: labels = ['c', 'd']
In [132]: s.reindex(labels)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[132], line 1
----> 1 s.reindex(labels)
File ~/work/pandas/pandas/pandas/core/series.py:6035, in Series.reindex(self, index, axis, method, copy, level, fill_value, limit, tolerance)
   6031         original index entry) unfilled.
   6032 
   6033         See the :ref:`user guide <basics.reindexing>` for more.
   6034         """
-> 6035         return super().reindex(
   6036             index=index,
   6037             method=method,
   6038             level=level,
File ~/work/pandas/pandas/pandas/core/generic.py:5544, in NDFrame.reindex(self, labels, index, columns, axis, method, copy, level, fill_value, limit, tolerance)
   5540         if self._needs_reindex_multi(axes, method, level):
   5541             return self._reindex_multi(axes, fill_value)
   5542 
   5543         # perform the reindex on the axes
-> 5544         return self._reindex_axes(
   5545             axes, level, limit, tolerance, method, fill_value
   5546         ).__finalize__(self, method="reindex")
File ~/work/pandas/pandas/pandas/core/generic.py:5566, in NDFrame._reindex_axes(self, axes, level, limit, tolerance, method, fill_value)
   5562             if labels is None:
   5563                 continue
   5564 
   5565             ax = self._get_axis(a)
-> 5566             new_index, indexer = ax.reindex(
   5567                 labels, level=level, limit=limit, tolerance=tolerance, method=method
   5568             )
   5569 
File ~/work/pandas/pandas/pandas/core/indexes/base.py:4450, in Index.reindex(self, target, method, level, limit, tolerance)
   4447     raise ValueError("cannot handle a non-unique multi-index!")
   4448 elif not self.is_unique:
   4449     # GH#42568
-> 4450     raise ValueError("cannot reindex on an axis with duplicate labels")
   4451 else:
   4452     indexer, _ = self.get_indexer_non_unique(target)
ValueError: cannot reindex on an axis with duplicate labels
```
Generally, you can intersect the desired labels with the current axis, and then reindex.

```
In [133]: s.loc[s.index.intersection(labels)].reindex(labels)
Out[133]: 
c    3.0
d    NaN
dtype: float64
```
However, this would *still* raise if your resulting index is duplicated.

```
In [134]: labels = ['a', 'd']
In [135]: s.loc[s.index.intersection(labels)].reindex(labels)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[135], line 1
----> 1 s.loc[s.index.intersection(labels)].reindex(labels)
File ~/work/pandas/pandas/pandas/core/series.py:6035, in Series.reindex(self, index, axis, method, copy, level, fill_value, limit, tolerance)
   6031         original index entry) unfilled.
   6032 
   6033         See the :ref:`user guide <basics.reindexing>` for more.
   6034         """
-> 6035         return super().reindex(
   6036             index=index,
   6037             method=method,
   6038             level=level,
File ~/work/pandas/pandas/pandas/core/generic.py:5544, in NDFrame.reindex(self, labels, index, columns, axis, method, copy, level, fill_value, limit, tolerance)
   5540         if self._needs_reindex_multi(axes, method, level):
   5541             return self._reindex_multi(axes, fill_value)
   5542 
   5543         # perform the reindex on the axes
-> 5544         return self._reindex_axes(
   5545             axes, level, limit, tolerance, method, fill_value
   5546         ).__finalize__(self, method="reindex")
File ~/work/pandas/pandas/pandas/core/generic.py:5566, in NDFrame._reindex_axes(self, axes, level, limit, tolerance, method, fill_value)
   5562             if labels is None:
   5563                 continue
   5564 
   5565             ax = self._get_axis(a)
-> 5566             new_index, indexer = ax.reindex(
   5567                 labels, level=level, limit=limit, tolerance=tolerance, method=method
   5568             )
   5569 
File ~/work/pandas/pandas/pandas/core/indexes/base.py:4450, in Index.reindex(self, target, method, level, limit, tolerance)
   4447     raise ValueError("cannot handle a non-unique multi-index!")
   4448 elif not self.is_unique:
   4449     # GH#42568
-> 4450     raise ValueError("cannot reindex on an axis with duplicate labels")
   4451 else:
   4452     indexer, _ = self.get_indexer_non_unique(target)
ValueError: cannot reindex on an axis with duplicate labels
```
## Selecting random samples[#](https://pandas.pydata.org#selecting-random-samples)

A random selection of rows or columns from a Series or DataFrame with the [`sample()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.sample.html#pandas.DataFrame.sample) method. The method will sample rows by default, and accepts a specific number of rows/columns to return, or a fraction of rows.

```
In [136]: s = pd.Series([0, 1, 2, 3, 4, 5])
# When no arguments are passed, returns 1 row.
In [137]: s.sample()
Out[137]: 
4    4
dtype: int64
# One may specify either a number of rows:
In [138]: s.sample(n=3)
Out[138]: 
0    0
4    4
1    1
dtype: int64
# Or a fraction of the rows:
In [139]: s.sample(frac=0.5)
Out[139]: 
5    5
3    3
1    1
dtype: int64
```
By default, `sample` will return each row at most once, but one can also sample with replacement
using the `replace` option:

```
In [140]: s = pd.Series([0, 1, 2, 3, 4, 5])
# Without replacement (default):
In [141]: s.sample(n=6, replace=False)
Out[141]: 
0    0
1    1
5    5
3    3
2    2
4    4
dtype: int64
# With replacement:
In [142]: s.sample(n=6, replace=True)
Out[142]: 
0    0
4    4
3    3
2    2
4    4
4    4
dtype: int64
```
By default, each row has an equal probability of being selected, but if you want rows
to have different probabilities, you can pass the `sample` function sampling weights as
`weights`. These weights can be a list, a NumPy array, or a Series, but they must be of the same length as the object you are sampling. Missing values will be treated as a weight of zero, and inf values are not allowed. If weights do not sum to 1, they will be re-normalized by dividing all weights by the sum of the weights. For example:

```
In [143]: s = pd.Series([0, 1, 2, 3, 4, 5])
In [144]: example_weights = [0, 0, 0.2, 0.2, 0.2, 0.4]
In [145]: s.sample(n=2, weights=example_weights)
Out[145]: 
5    5
4    4
dtype: int64
# Weights will be re-normalized automatically
In [146]: example_weights2 = [0.5, 0, 0, 0, 0, 0]
In [147]: s.sample(n=1, weights=example_weights2)
Out[147]: 
0    0
dtype: int64
```
When applied to a DataFrame, you can use a column of the DataFrame as sampling weights (provided you are sampling rows and not columns) by simply passing the name of the column as a string.

```
In [148]: df2 = pd.DataFrame({'col1': [9, 8, 7, 6],
   .....:                     'weight_column': [0.5, 0.4, 0.1, 0]})
   .....: 
In [149]: df2.sample(n=2, weights='weight_column')
Out[149]: 
   col1  weight_column
0     9            0.5
1     8            0.4
```
`sample` also allows users to sample columns instead of rows using the `axis` argument.

```
In [150]: df3 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 3, 4]})
In [151]: df3.sample(n=1, axis=1)
Out[151]: 
   col2
0     2
1     3
2     4
```
Finally, one can also set a seed for `sample`’s random number generator using the `random_state` argument, which will accept either an integer (as a seed) or a NumPy RandomState object.

```
In [152]: df4 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 3, 4]})
# With a given seed, the sample will always draw the same rows.
In [153]: df4.sample(n=2, random_state=2)
Out[153]: 
   col1  col2
2     3     4
1     2     3
In [154]: df4.sample(n=2, random_state=2)
Out[154]: 
   col1  col2
2     3     4
1     2     3
```
## Setting with enlargement[#](https://pandas.pydata.org#setting-with-enlargement)

The `.loc/[]` operations can perform enlargement when setting a non-existent key for that axis.

In the `Series` case this is effectively an appending operation.

```
In [155]: se = pd.Series([1, 2, 3])
In [156]: se
Out[156]: 
0    1
1    2
2    3
dtype: int64
In [157]: se[5] = 5.
In [158]: se
Out[158]: 
0    1
1    2
2    3
5    5
dtype: int64
```
A `DataFrame` can be enlarged on either axis via `.loc`.

```
In [159]: dfi = pd.DataFrame(np.arange(6).reshape(3, 2),
   .....:                    columns=['A', 'B'])
   .....: 
In [160]: dfi
Out[160]: 
   A  B
0  0  1
1  2  3
2  4  5
In [161]: dfi.loc[:, 'C'] = dfi.loc[:, 'A']
In [162]: dfi
Out[162]: 
   A  B  C
0  0  1  0
1  2  3  2
2  4  5  4
```
This is like an `append` operation on the `DataFrame`.

```
In [163]: dfi.loc[3] = 5
In [164]: dfi
Out[164]: 
   A  B  C
0  0  1  0
1  2  3  2
2  4  5  4
3  5  5  5
```
## Fast scalar value getting and setting[#](https://pandas.pydata.org#fast-scalar-value-getting-and-setting)

Since indexing with `[]` must handle a lot of cases (single-label access,
slicing, boolean indexing, etc.), it has a bit of overhead in order to figure
out what you’re asking for. If you only want to access a scalar value, the
fastest way is to use the `at` and `iat` methods, which are implemented on
all of the data structures.

Similarly to `loc`, `at` provides **label** based scalar lookups, while, `iat` provides **integer** based lookups analogously to `iloc`

```
In [165]: s.iat[5]
Out[165]: np.int64(5)
In [166]: df.at[dates[5], 'A']
Out[166]: np.float64(0.1136484096888855)
In [167]: df.iat[3, 0]
Out[167]: np.float64(-0.7067711336300845)
```
You can also set using these same indexers.

```
In [168]: df.at[dates[5], 'A'] = 7
In [169]: df.iat[3, 0] = 7
```
`at` previously could enlarge the object in-place if the indexer was missing,
but this behavior is deprecated. Use `.loc` instead for setting values with
new keys:

```
In [170]: df.loc[dates[-1] + pd.Timedelta('1 day'), 0] = 7
In [171]: df
Out[171]: 
                   A         B         C         D    0
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632  NaN
2000-01-02 -0.173215  1.212112  0.119209 -1.044236  NaN
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804  NaN
2000-01-04  7.000000  0.721555 -1.039575  0.271860  NaN
2000-01-05  0.567020 -0.424972  0.276232 -1.087401  NaN
2000-01-06  7.000000 -0.673690 -1.478427  0.524988  NaN
2000-01-07  0.577046  0.404705 -1.715002 -1.039268  NaN
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885  NaN
2000-01-09       NaN       NaN       NaN       NaN  7.0
```
## Boolean indexing[#](https://pandas.pydata.org#boolean-indexing)

Another common operation is the use of boolean vectors to filter the data.
The operators are: `|` for `or`, `&` for `and`, and `~` for `not`.
These **must** be grouped by using parentheses, since by default Python will
evaluate an expression such as `df['A'] > 2 & df['B'] < 3` as
`df['A'] > (2 & df['B']) < 3`, while the desired evaluation order is
`(df['A'] > 2) & (df['B'] < 3)`.

Using a boolean vector to index a Series works exactly as in a NumPy ndarray:

```
In [172]: s = pd.Series(range(-3, 4))
In [173]: s
Out[173]: 
0   -3
1   -2
2   -1
3    0
4    1
5    2
6    3
dtype: int64
In [174]: s[s > 0]
Out[174]: 
4    1
5    2
6    3
dtype: int64
In [175]: s[(s < -1) | (s > 0.5)]
Out[175]: 
0   -3
1   -2
4    1
5    2
6    3
dtype: int64
In [176]: s[~(s < 0)]
Out[176]: 
3    0
4    1
5    2
6    3
dtype: int64
```
You may select rows from a DataFrame using a boolean vector the same length as the DataFrame’s index (for example, something derived from one of the columns of the DataFrame):

```
In [177]: df[df['A'] > 0]
Out[177]: 
                   A         B         C         D   0
2000-01-04  7.000000  0.721555 -1.039575  0.271860 NaN
2000-01-05  0.567020 -0.424972  0.276232 -1.087401 NaN
2000-01-06  7.000000 -0.673690 -1.478427  0.524988 NaN
2000-01-07  0.577046  0.404705 -1.715002 -1.039268 NaN
```
List comprehensions and the `map` method of Series can also be used to produce
more complex criteria:

```
In [178]: df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
   .....:                     'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
   .....:                     'c': np.random.randn(7)})
   .....: 
# only want 'two' or 'three'
In [179]: criterion = df2['a'].map(lambda x: x.startswith('t'))
In [180]: df2[criterion]
Out[180]: 
       a  b         c
2    two  y  2.543083
3  three  x  0.831311
4    two  y -0.816973
# equivalent but slower
In [181]: df2[[x.startswith('t') for x in df2['a']]]
Out[181]: 
       a  b         c
2    two  y  2.543083
3  three  x  0.831311
4    two  y -0.816973
# Multiple criteria
In [182]: df2[criterion & (df2['b'] == 'x')]
Out[182]: 
       a  b         c
3  three  x  0.831311
```
With the choice methods [Selection by Label](https://pandas.pydata.org#indexing-label), [Selection by Position](https://pandas.pydata.org#indexing-integer),
and [Advanced Indexing](https://pandas.pydata.org/advanced.html#advanced) you may select along more than one axis using boolean vectors combined with other indexing expressions.

```
In [183]: df2.loc[criterion & (df2['b'] == 'x'), 'b':'c']
Out[183]: 
   b         c
3  x  0.831311
```
Warning

While `loc` supports two kinds of boolean indexing, `iloc` only supports indexing with a
boolean array. If the indexer is a boolean `Series`, an error will be raised. For instance,
in the following example, `df.iloc[s.values, 1]` is ok. The boolean indexer is an array.
But `df.iloc[s, 1]` would raise `ValueError`.

```
In [184]: df = pd.DataFrame([[1, 2], [3, 4], [5, 6]],
   .....:                   index=list('abc'),
   .....:                   columns=['A', 'B'])
   .....: 
In [185]: s = (df['A'] > 2)
In [186]: s
Out[186]: 
a    False
b     True
c     True
Name: A, dtype: bool
In [187]: df.loc[s, 'B']
Out[187]: 
b    4
c    6
Name: B, dtype: int64
In [188]: df.iloc[s.values, 1]
Out[188]: 
b    4
c    6
Name: B, dtype: int64
```
### Filtering with `DataFrame.filter`[#](https://pandas.pydata.org#filtering-with-dataframe-filter)

Added in version 3.1.0.

[`DataFrame.filter()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter) and [`Series.filter()`](https://pandas.pydata.org/reference/api/pandas.Series.filter.html#pandas.Series.filter) also accept a boolean mask
through the `cond` keyword, keeping the rows where the mask is True. A
[`Series`](https://pandas.pydata.org/reference/api/pandas.Series.html#pandas.Series) mask is aligned on the index; any other array-like must have
the same length as the index.

```
In [189]: df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=list('abc'))
In [190]: df.filter(cond=df['A'] > 1)
Out[190]: 
   A  B
b  2  5
c  3  6
```
`cond` may also be a callable that returns a boolean mask, or an expression
created with [`pandas.col()`](https://pandas.pydata.org/reference/api/pandas.col.html#pandas.col). These two forms may be passed positionally,
which is convenient in a method chain where the intermediate object has no
name:

```
In [191]: df.filter(pd.col('A') > 1)
Out[191]: 
   A  B
b  2  5
c  3  6
In [192]: df.assign(C=pd.col('A') + pd.col('B')).filter(lambda df: df['C'] > 5)
Out[192]: 
   A  B  C
b  2  5  7
c  3  6  9
```
Pass `axis=1` to filter columns instead of rows:

```
In [193]: df.filter(cond=df.columns.str.startswith('A'), axis=1)
Out[193]: 
   A
a  1
b  2
c  3
```
Missing values in the mask are treated as False by default, matching
`df[mask]` for a mask with nullable boolean dtype. Pass `na=True` to keep
the corresponding rows instead, or `na="raise"` to raise an error:

```
In [194]: mask = pd.array([True, None, False], dtype="boolean")
In [195]: df.filter(cond=mask)
Out[195]: 
   A  B
a  1  4
In [196]: df.filter(cond=mask, na=True)
Out[196]: 
   A  B
a  1  4
b  2  5
```
## Indexing with isin[#](https://pandas.pydata.org#indexing-with-isin)

Consider the [`isin()`](https://pandas.pydata.org/reference/api/pandas.Series.isin.html#pandas.Series.isin) method of `Series`, which returns a boolean
vector that is true wherever the `Series` elements exist in the passed list.
This allows you to select rows where one or more columns have values you want:

```
In [197]: s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
In [198]: s
Out[198]: 
4    0
3    1
2    2
1    3
0    4
dtype: int64
In [199]: s.isin([2, 4, 6])
Out[199]: 
4    False
3    False
2     True
1    False
0     True
dtype: bool
In [200]: s[s.isin([2, 4, 6])]
Out[200]: 
2    2
0    4
dtype: int64
```
The same method is available for `Index` objects and is useful for the cases
when you don’t know which of the sought labels are in fact present:

```
In [201]: s[s.index.isin([2, 4, 6])]
Out[201]: 
4    0
2    2
dtype: int64
# compare it to the following
In [202]: s.reindex([2, 4, 6])
Out[202]: 
2    2.0
4    0.0
6    NaN
dtype: float64
```
In addition to that, `MultiIndex` allows selecting a separate level to use
in the membership check:

```
In [203]: s_mi = pd.Series(np.arange(6),
   .....:                  index=pd.MultiIndex.from_product([[0, 1], ['a', 'b', 'c']]))
   .....: 
In [204]: s_mi
Out[204]: 
0  a    0
   b    1
   c    2
1  a    3
   b    4
   c    5
dtype: int64
In [205]: s_mi.iloc[s_mi.index.isin([(1, 'a'), (2, 'b'), (0, 'c')])]
Out[205]: 
0  c    2
1  a    3
dtype: int64
In [206]: s_mi.iloc[s_mi.index.isin(['a', 'c', 'e'], level=1)]
Out[206]: 
0  a    0
   c    2
1  a    3
   c    5
dtype: int64
```
DataFrame also has an [`isin()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin) method.  When calling `isin`, pass a set of
values as either an array or dict.  If values is an array, `isin` returns
a DataFrame of booleans that is the same shape as the original DataFrame, with True
wherever the element is in the sequence of values.

```
In [207]: df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'],
   .....:                    'ids2': ['a', 'n', 'c', 'n']})
   .....: 
In [208]: values = ['a', 'b', 1, 3]
In [209]: df.isin(values)
Out[209]: 
    vals    ids   ids2
0   True   True   True
1  False   True  False
2   True  False  False
3  False  False  False
```
Oftentimes you’ll want to match certain values with certain columns.
Just make values a `dict` where the key is the column, and the value is
a list of items you want to check for.

```
In [210]: values = {'ids': ['a', 'b'], 'vals': [1, 3]}
In [211]: df.isin(values)
Out[211]: 
    vals    ids   ids2
0   True   True  False
1  False   True  False
2   True  False  False
3  False  False  False
```
To return the DataFrame of booleans where the values are *not* in the original DataFrame,
use the `~` operator:

```
In [212]: values = {'ids': ['a', 'b'], 'vals': [1, 3]}
In [213]: ~df.isin(values)
Out[213]: 
    vals    ids  ids2
0  False  False  True
1   True  False  True
2  False   True  True
3   True   True  True
```
Combine DataFrame’s `isin` with the `any()` and `all()` methods to
quickly select subsets of your data that meet a given criteria.
To select a row where each column meets its own criterion:

```
In [214]: values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}
In [215]: row_mask = df.isin(values).all(axis=1)
In [216]: df[row_mask]
Out[216]: 
   vals ids ids2
0     1   a    a
```
Selecting values from a Series with a boolean vector generally returns a
subset of the data. To guarantee that selection output has the same shape as
the original data, you can use the `where` method in `Series` and `DataFrame`.

To return only the selected rows:

```
In [217]: s[s > 0]
Out[217]: 
3    1
2    2
1    3
0    4
dtype: int64
```
To return a Series of the same shape as the original:

```
In [218]: s.where(s > 0)
Out[218]: 
4    NaN
3    1.0
2    2.0
1    3.0
0    4.0
dtype: float64
```
Selecting values from a DataFrame with a boolean criterion now also preserves
input data shape. `where` is used under the hood as the implementation.
The code below is equivalent to `df.where(df < 0)`.

```
In [219]: dates = pd.date_range('1/1/2000', periods=8)
In [220]: df = pd.DataFrame(np.random.randn(8, 4),
   .....:                   index=dates, columns=['A', 'B', 'C', 'D'])
   .....: 
In [221]: df[df < 0]
Out[221]: 
                   A         B         C         D
2000-01-01       NaN       NaN -0.250643 -1.350999
2000-01-02       NaN -0.026679       NaN       NaN
2000-01-03       NaN -1.112060       NaN -1.281223
2000-01-04       NaN       NaN -0.592066 -0.650567
2000-01-05 -0.374599       NaN -1.133167       NaN
2000-01-06 -1.254148       NaN       NaN       NaN
2000-01-07 -0.524443 -0.712053 -0.267772       NaN
2000-01-08 -0.076848       NaN -1.819296 -1.122503
```
In addition, `where` takes an optional `other` argument for replacement of
values where the condition is False, in the returned copy.

```
In [222]: df.where(df < 0, -df)
Out[222]: 
                   A         B         C         D
2000-01-01 -0.368085 -0.224661 -0.250643 -1.350999
2000-01-02 -0.142692 -0.026679 -1.345835 -0.938848
2000-01-03 -0.509624 -1.112060 -1.648517 -1.281223
2000-01-04 -0.553689 -0.359996 -0.592066 -0.650567
2000-01-05 -0.374599 -0.592071 -1.133167 -0.661259
2000-01-06 -1.254148 -0.627193 -0.411295 -1.282903
2000-01-07 -0.524443 -0.712053 -0.267772 -1.762567
2000-01-08 -0.076848 -2.431230 -1.819296 -1.122503
```
You may wish to set values based on some boolean criteria. This can be done intuitively like so:

```
In [223]: s2 = s.copy()
In [224]: s2[s2 < 0] = 0
In [225]: s2
Out[225]: 
4    0
3    1
2    2
1    3
0    4
dtype: int64
In [226]: df2 = df.copy()
In [227]: df2[df2 < 0] = 0
In [228]: df2
Out[228]: 
                   A         B         C         D
2000-01-01  0.368085  0.224661  0.000000  0.000000
2000-01-02  0.142692  0.000000  1.345835  0.938848
2000-01-03  0.509624  0.000000  1.648517  0.000000
2000-01-04  0.553689  0.359996  0.000000  0.000000
2000-01-05  0.000000  0.592071  0.000000  0.661259
2000-01-06  0.000000  0.627193  0.411295  1.282903
2000-01-07  0.000000  0.000000  0.000000  1.762567
2000-01-08  0.000000  2.431230  0.000000  0.000000
```
`where` returns a modified copy of the data.

Note

The signature for [`DataFrame.where()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where) differs from [`numpy.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where).
Roughly `df1.where(m, df2)` is equivalent to `np.where(m, df1, df2)`.

```
In [229]: df.where(df < 0, -df) == np.where(df < 0, df, -df)
Out[229]: 
               A     B     C     D
2000-01-01  True  True  True  True
2000-01-02  True  True  True  True
2000-01-03  True  True  True  True
2000-01-04  True  True  True  True
2000-01-05  True  True  True  True
2000-01-06  True  True  True  True
2000-01-07  True  True  True  True
2000-01-08  True  True  True  True
```
**Alignment**

Furthermore, `where` aligns the input boolean condition (ndarray or DataFrame),
such that partial selection with setting is possible. This is analogous to
partial setting via `.loc` (but on the contents rather than the axis labels).

```
In [230]: df2 = df.copy()
In [231]: df2[df2[1:4] > 0] = 3
In [232]: df2
Out[232]: 
                   A         B         C         D
2000-01-01  0.368085  0.224661 -0.250643 -1.350999
2000-01-02  3.000000 -0.026679  3.000000  3.000000
2000-01-03  3.000000 -1.112060  3.000000 -1.281223
2000-01-04  3.000000  3.000000 -0.592066 -0.650567
2000-01-05 -0.374599  0.592071 -1.133167  0.661259
2000-01-06 -1.254148  0.627193  0.411295  1.282903
2000-01-07 -0.524443 -0.712053 -0.267772  1.762567
2000-01-08 -0.076848  2.431230 -1.819296 -1.122503
```
Where can also accept `axis` and `level` parameters to align the input when
performing the `where`.

```
In [233]: df2 = df.copy()
In [234]: df2.where(df2 > 0, df2['A'], axis='index')
Out[234]: 
                   A         B         C         D
2000-01-01  0.368085  0.224661  0.368085  0.368085
2000-01-02  0.142692  0.142692  1.345835  0.938848
2000-01-03  0.509624  0.509624  1.648517  0.509624
2000-01-04  0.553689  0.359996  0.553689  0.553689
2000-01-05 -0.374599  0.592071 -0.374599  0.661259
2000-01-06 -1.254148  0.627193  0.411295  1.282903
2000-01-07 -0.524443 -0.524443 -0.524443  1.762567
2000-01-08 -0.076848  2.431230 -0.076848 -0.076848
```
This is equivalent to (but faster than) the following.

```
In [235]: df2 = df.copy()
In [236]: df.apply(lambda x, y: x.where(x > 0, y), y=df['A'])
Out[236]: 
                   A         B         C         D
2000-01-01  0.368085  0.224661  0.368085  0.368085
2000-01-02  0.142692  0.142692  1.345835  0.938848
2000-01-03  0.509624  0.509624  1.648517  0.509624
2000-01-04  0.553689  0.359996  0.553689  0.553689
2000-01-05 -0.374599  0.592071 -0.374599  0.661259
2000-01-06 -1.254148  0.627193  0.411295  1.282903
2000-01-07 -0.524443 -0.524443 -0.524443  1.762567
2000-01-08 -0.076848  2.431230 -0.076848 -0.076848
```
`where` can accept a callable as condition and `other` arguments. The function must
be with one argument (the calling Series or DataFrame) and that returns valid output
as condition and `other` argument.

```
In [237]: df3 = pd.DataFrame({'A': [1, 2, 3],
   .....:                     'B': [4, 5, 6],
   .....:                     'C': [7, 8, 9]})
   .....: 
In [238]: df3.where(lambda x: x > 4, lambda x: x + 10)
Out[238]: 
    A   B  C
0  11  14  7
1  12   5  8
2  13   6  9
```
### Mask[#](https://pandas.pydata.org#mask)

[`mask()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.mask.html#pandas.DataFrame.mask) is the inverse boolean operation of `where`.

```
In [239]: s.mask(s >= 0)
Out[239]: 
4   NaN
3   NaN
2   NaN
1   NaN
0   NaN
dtype: float64
In [240]: df.mask(df >= 0)
Out[240]: 
                   A         B         C         D
2000-01-01       NaN       NaN -0.250643 -1.350999
2000-01-02       NaN -0.026679       NaN       NaN
2000-01-03       NaN -1.112060       NaN -1.281223
2000-01-04       NaN       NaN -0.592066 -0.650567
2000-01-05 -0.374599       NaN -1.133167       NaN
2000-01-06 -1.254148       NaN       NaN       NaN
2000-01-07 -0.524443 -0.712053 -0.267772       NaN
2000-01-08 -0.076848       NaN -1.819296 -1.122503
```
## Setting with enlargement conditionally using `numpy()`[#](https://pandas.pydata.org#setting-with-enlargement-conditionally-using-numpy)

An alternative to [`where()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where) is to use [`numpy.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where).
Combined with setting a new column, you can use it to enlarge a DataFrame where the
values are determined conditionally.

Consider you have two choices to choose from in the following DataFrame. And you want to set a new column color to ‘green’ when the second column has ‘Z’. You can do the following:

```
In [241]: df = pd.DataFrame({'col1': list('ABBC'), 'col2': list('ZZXY')})
In [242]: df['color'] = np.where(df['col2'] == 'Z', 'green', 'red')
In [243]: df
Out[243]: 
  col1 col2  color
0    A    Z  green
1    B    Z  green
2    B    X    red
3    C    Y    red
```
If you have multiple conditions, you can use [`numpy.select()`](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy.select) to achieve that.  Say
corresponding to three conditions there are three choice of colors, with a fourth color
as a fallback, you can do the following.

```
In [244]: conditions = [
   .....:     (df['col2'] == 'Z') & (df['col1'] == 'A'),
   .....:     (df['col2'] == 'Z') & (df['col1'] == 'B'),
   .....:     (df['col1'] == 'B')
   .....: ]
   .....: 
In [245]: choices = ['yellow', 'blue', 'purple']
In [246]: df['color'] = np.select(conditions, choices, default='black')
In [247]: df
Out[247]: 
  col1 col2   color
0    A    Z  yellow
1    B    Z    blue
2    B    X  purple
3    C    Y   black
```
[`DataFrame`](https://pandas.pydata.org/reference/api/pandas.DataFrame.html#pandas.DataFrame) objects have a [`query()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query)
method that allows selection using an expression.

You can get the value of the frame where column `b` has values
between the values of columns `a` and `c`. For example:

```
In [248]: n = 10
In [249]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
In [250]: df
Out[250]: 
          a         b         c
0  0.977227  0.727376  0.630865
1  0.076462  0.474453  0.438921
2  0.118680  0.863670  0.138138
3  0.577363  0.686602  0.595307
4  0.564592  0.520630  0.913052
5  0.926075  0.616184  0.078718
6  0.854477  0.898725  0.076404
7  0.523211  0.591538  0.792342
8  0.216974  0.564056  0.397890
9  0.454131  0.915716  0.074315
# pure python
In [251]: df[(df['a'] < df['b']) & (df['b'] < df['c'])]
Out[251]: 
          a         b         c
7  0.523211  0.591538  0.792342
# query
In [252]: df.query('(a < b) & (b < c)')
Out[252]: 
          a         b         c
7  0.523211  0.591538  0.792342
```
Do the same thing but fall back on a named index if there is no column
with the name `a`.

```
In [253]: df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))
In [254]: df.index.name = 'a'
In [255]: df
Out[255]: 
   b  c
a      
0  0  0
1  3  1
2  3  4
3  0  4
4  0  1
5  3  4
6  4  3
7  1  4
8  0  3
9  0  1
In [256]: df.query('a < b and b < c')
Out[256]: 
   b  c
a      
2  3  4
```
If instead you don’t want to or cannot name your index, you can use the name
`index` in your query expression:

```
In [257]: df = pd.DataFrame(np.random.randint(n, size=(n, 2)), columns=list('bc'))
In [258]: df
Out[258]: 
   b  c
0  2  3
1  9  1
2  3  1
3  3  0
4  5  6
5  5  2
6  7  4
7  0  1
8  2  5
9  0  1
In [259]: df.query('index < b < c')
Out[259]: 
   b  c
0  2  3
4  5  6
```
Note

If the name of your index overlaps with a column name, the column name is given precedence. For example,

```
In [260]: df = pd.DataFrame({'a': np.random.randint(5, size=5)})
In [261]: df.index.name = 'a'
In [262]: df.query('a > 2')  # uses the column 'a', not the index
Out[262]: 
   a
a   
3  3
```
You can still use the index in a query expression by using the special identifier ‘index’:

```
In [263]: df.query('index > 2')
Out[263]: 
   a
a   
3  3
4  1
```
If for some reason you have a column named `index`, then you can refer to
the index as `ilevel_0` as well, but at this point you should consider
renaming your columns to something less ambiguous.

### [`MultiIndex`](https://pandas.pydata.org/reference/api/pandas.MultiIndex.html#pandas.MultiIndex) [`query()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query) Syntax[#](https://pandas.pydata.org#multiindex-query-syntax)

You can also use the levels of a `DataFrame` with a
[`MultiIndex`](https://pandas.pydata.org/reference/api/pandas.MultiIndex.html#pandas.MultiIndex) as if they were columns in the frame:

```
In [264]: n = 10
In [265]: colors = np.random.choice(['red', 'green'], size=n)
In [266]: foods = np.random.choice(['eggs', 'ham'], size=n)
In [267]: colors
Out[267]: 
array(['green', 'green', 'red', 'green', 'red', 'red', 'red', 'red',
       'green', 'green'], dtype='<U5')
In [268]: foods
Out[268]: 
array(['ham', 'ham', 'ham', 'ham', 'ham', 'ham', 'ham', 'eggs', 'eggs',
       'eggs'], dtype='<U4')
In [269]: index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])
In [270]: df = pd.DataFrame(np.random.randn(n, 2), index=index)
In [271]: df
Out[271]: 
                   0         1
color food                    
green ham  -1.087664 -0.883833
      ham  -1.554827 -0.118953
red   ham  -1.460084 -0.020351
green ham  -0.256125  0.358575
red   ham   1.112033 -0.200521
      ham  -0.508784 -0.327758
      ham   0.627056  0.067058
      eggs -1.376511  1.162330
green eggs -0.482120 -0.455309
      eggs -0.985682  1.383438
In [272]: df.query('color == "red"')
Out[272]: 
                   0         1
color food                    
red   ham  -1.460084 -0.020351
      ham   1.112033 -0.200521
      ham  -0.508784 -0.327758
      ham   0.627056  0.067058
      eggs -1.376511  1.162330
```
If the levels of the `MultiIndex` are unnamed, you can refer to them using
special names:

```
In [273]: df.index.names = [None, None]
In [274]: df
Out[274]: 
                   0         1
green ham  -1.087664 -0.883833
      ham  -1.554827 -0.118953
red   ham  -1.460084 -0.020351
green ham  -0.256125  0.358575
red   ham   1.112033 -0.200521
      ham  -0.508784 -0.327758
      ham   0.627056  0.067058
      eggs -1.376511  1.162330
green eggs -0.482120 -0.455309
      eggs -0.985682  1.383438
In [275]: df.query('ilevel_0 == "red"')
Out[275]: 
                 0         1
red ham  -1.460084 -0.020351
    ham   1.112033 -0.200521
    ham  -0.508784 -0.327758
    ham   0.627056  0.067058
    eggs -1.376511  1.162330
```
The convention is `ilevel_0`, which means “index level 0” for the 0th level
of the `index`.

A use case for [`query()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query) is when you have a collection of
[`DataFrame`](https://pandas.pydata.org/reference/api/pandas.DataFrame.html#pandas.DataFrame) objects that have a subset of column names (or index
levels/names) in common. You can pass the same query to both frames *without*
having to specify which frame you’re interested in querying

```
In [276]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
In [277]: df
Out[277]: 
          a         b         c
0  0.972314  0.789179  0.293847
1  0.374439  0.739133  0.221186
2  0.900625  0.534438  0.608763
3  0.166933  0.731582  0.965147
4  0.763981  0.372737  0.639792
5  0.702270  0.730804  0.134089
6  0.522758  0.311910  0.656542
7  0.258647  0.655096  0.654920
8  0.452594  0.454307  0.918260
9  0.581556  0.470410  0.417434
In [278]: df2 = pd.DataFrame(np.random.rand(n + 2, 3), columns=df.columns)
In [279]: df2
Out[279]: 
           a         b         c
0   0.552021  0.483125  0.807046
1   0.277950  0.213500  0.471524
2   0.501458  0.141708  0.763617
3   0.081639  0.906284  0.480101
4   0.472250  0.380061  0.822149
5   0.459151  0.851196  0.125791
6   0.857816  0.795472  0.527728
7   0.561164  0.945324  0.622249
8   0.511283  0.577675  0.989138
9   0.528050  0.627750  0.652326
10  0.393289  0.103627  0.056786
11  0.749255  0.505533  0.883673
In [280]: expr = '0.0 <= a <= c <= 0.5'
In [281]: map(lambda frame: frame.query(expr), [df, df2])
Out[281]: <map at 0x7fbcf869b490>
```
Full numpy-like syntax:

```
In [282]: df = pd.DataFrame(np.random.randint(n, size=(n, 3)), columns=list('abc'))
In [283]: df
Out[283]: 
   a  b  c
0  6  2  2
1  2  6  3
2  3  8  2
3  1  7  2
4  5  1  5
5  9  8  0
6  1  5  0
7  4  9  6
8  2  3  0
9  6  5  4
In [284]: df.query('(a < b) & (b < c)')
Out[284]: 
Empty DataFrame
Columns: [a, b, c]
Index: []
In [285]: df[(df['a'] < df['b']) & (df['b'] < df['c'])]
Out[285]: 
Empty DataFrame
Columns: [a, b, c]
Index: []
```
Slightly nicer by removing the parentheses (comparison operators bind tighter
than `&` and `|`):

```
In [286]: df.query('a < b & b < c')
Out[286]: 
Empty DataFrame
Columns: [a, b, c]
Index: []
```
Use English instead of symbols:

```
In [287]: df.query('a < b and b < c')
Out[287]: 
Empty DataFrame
Columns: [a, b, c]
Index: []
```
Pretty close to how you might write it on paper:

```
In [288]: df.query('a < b < c')
Out[288]: 
Empty DataFrame
Columns: [a, b, c]
Index: []
```
### The `in` and `not in` operators[#](https://pandas.pydata.org#the-in-and-not-in-operators)

[`query()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query) also supports special use of Python’s `in` and
`not in` comparison operators, providing a succinct syntax for calling the
`isin` method of a `Series` or `DataFrame`.

```
# get all rows where columns "a" and "b" have overlapping values
In [289]: df = pd.DataFrame({'a': list('aabbccddeeff'), 'b': list('aaaabbbbcccc'),
   .....:                    'c': np.random.randint(5, size=12),
   .....:                    'd': np.random.randint(9, size=12)})
   .....: 
In [290]: df
Out[290]: 
    a  b  c  d
0   a  a  2  3
1   a  a  0  0
2   b  a  1  6
3   b  a  2  2
4   c  b  1  7
5   c  b  2  7
6   d  b  3  6
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
10  f  c  3  3
11  f  c  1  3
In [291]: df.query('a in b')
Out[291]: 
   a  b  c  d
0  a  a  2  3
1  a  a  0  0
2  b  a  1  6
3  b  a  2  2
4  c  b  1  7
5  c  b  2  7
# How you'd do it in pure Python
In [292]: df[df['a'].isin(df['b'])]
Out[292]: 
   a  b  c  d
0  a  a  2  3
1  a  a  0  0
2  b  a  1  6
3  b  a  2  2
4  c  b  1  7
5  c  b  2  7
In [293]: df.query('a not in b')
Out[293]: 
    a  b  c  d
6   d  b  3  6
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
10  f  c  3  3
11  f  c  1  3
# pure Python
In [294]: df[~df['a'].isin(df['b'])]
Out[294]: 
    a  b  c  d
6   d  b  3  6
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
10  f  c  3  3
11  f  c  1  3
```
You can combine this with other expressions for very succinct queries:

```
# rows where cols a and b have overlapping values
# and col c's values are less than col d's
In [295]: df.query('a in b and c < d')
Out[295]: 
   a  b  c  d
0  a  a  2  3
2  b  a  1  6
4  c  b  1  7
5  c  b  2  7
# pure Python
In [296]: df[df['b'].isin(df['a']) & (df['c'] < df['d'])]
Out[296]: 
    a  b  c  d
0   a  a  2  3
2   b  a  1  6
4   c  b  1  7
5   c  b  2  7
6   d  b  3  6
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
11  f  c  1  3
```
Note

Note that `in` and `not in` are evaluated in Python, since `numexpr`
has no equivalent of this operation. However, **only the** `in`/`not in`
**expression itself** is evaluated in vanilla Python. For example, in the
expression

```
df.query('a in b + c + d')
```
`(b + c + d)` is evaluated by `numexpr` and *then* the `in`
operation is evaluated in plain Python. In general, any operations that can
be evaluated using `numexpr` will be.

### Special use of the `==` operator with `list` objects[#](https://pandas.pydata.org#special-use-of-the-operator-with-list-objects)

Comparing a `list` of values to a column using `==`/`!=` works similarly
to `in`/`not in`.

```
In [297]: df.query('b == ["a", "b", "c"]')
Out[297]: 
    a  b  c  d
0   a  a  2  3
1   a  a  0  0
2   b  a  1  6
3   b  a  2  2
4   c  b  1  7
5   c  b  2  7
6   d  b  3  6
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
10  f  c  3  3
11  f  c  1  3
# pure Python
In [298]: df[df['b'].isin(["a", "b", "c"])]
Out[298]: 
    a  b  c  d
0   a  a  2  3
1   a  a  0  0
2   b  a  1  6
3   b  a  2  2
4   c  b  1  7
5   c  b  2  7
6   d  b  3  6
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
10  f  c  3  3
11  f  c  1  3
In [299]: df.query('c == [1, 2]')
Out[299]: 
    a  b  c  d
0   a  a  2  3
2   b  a  1  6
3   b  a  2  2
4   c  b  1  7
5   c  b  2  7
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
11  f  c  1  3
In [300]: df.query('c != [1, 2]')
Out[300]: 
    a  b  c  d
1   a  a  0  0
6   d  b  3  6
10  f  c  3  3
# using in/not in
In [301]: df.query('[1, 2] in c')
Out[301]: 
    a  b  c  d
0   a  a  2  3
2   b  a  1  6
3   b  a  2  2
4   c  b  1  7
5   c  b  2  7
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
11  f  c  1  3
In [302]: df.query('[1, 2] not in c')
Out[302]: 
    a  b  c  d
1   a  a  0  0
6   d  b  3  6
10  f  c  3  3
# pure Python
In [303]: df[df['c'].isin([1, 2])]
Out[303]: 
    a  b  c  d
0   a  a  2  3
2   b  a  1  6
3   b  a  2  2
4   c  b  1  7
5   c  b  2  7
7   d  b  2  7
8   e  c  2  8
9   e  c  2  8
11  f  c  1  3
```
### Boolean operators[#](https://pandas.pydata.org#boolean-operators)

You can negate boolean expressions with the word `not` or the `~` operator.

```
In [304]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
In [305]: df['bools'] = np.random.rand(len(df)) > 0.5
In [306]: df.query('~bools')
Out[306]: 
          a         b         c  bools
4  0.580078  0.620439  0.434445  False
7  0.260776  0.290751  0.462080  False
9  0.165948  0.902260  0.825007  False
In [307]: df.query('not bools')
Out[307]: 
          a         b         c  bools
4  0.580078  0.620439  0.434445  False
7  0.260776  0.290751  0.462080  False
9  0.165948  0.902260  0.825007  False
In [308]: df.query('not bools') == df[~df['bools']]
Out[308]: 
      a     b     c  bools
4  True  True  True   True
7  True  True  True   True
9  True  True  True   True
```
Of course, expressions can be arbitrarily complex too:

```
# short query syntax
In [309]: shorter = df.query('a < b < c and (not bools) or bools > 2')
# equivalent in pure Python
In [310]: longer = df[(df['a'] < df['b'])
   .....:             & (df['b'] < df['c'])
   .....:             & (~df['bools'])
   .....:             | (df['bools'] > 2)]
   .....: 
In [311]: shorter
Out[311]: 
          a         b        c  bools
7  0.260776  0.290751  0.46208  False
In [312]: longer
Out[312]: 
          a         b        c  bools
7  0.260776  0.290751  0.46208  False
In [313]: shorter == longer
Out[313]: 
      a     b     c  bools
7  True  True  True   True
```
`DataFrame.query()` using `numexpr` is slightly faster than Python for
large frames.

You will only see the performance benefits of using the `numexpr` engine
with `DataFrame.query()` if your frame has more than approximately 100,000
rows.

This plot was created using a `DataFrame` with 3 columns each containing
floating point values generated using `numpy.random.randn()`.

```
In [314]: df = pd.DataFrame(np.random.randn(8, 4),
   .....:                   index=dates, columns=['A', 'B', 'C', 'D'])
   .....: 
In [315]: df2 = df.copy()
```
## Duplicate data[#](https://pandas.pydata.org#duplicate-data)

If you want to identify and remove duplicate rows in a DataFrame,  there are
two methods that will help: `duplicated` and `drop_duplicates`. Each
takes as an argument the columns to use to identify duplicated rows.

- `duplicated` returns a boolean vector whose length is the number of rows, and which indicates whether a row is duplicated.
- `drop_duplicates` removes duplicate rows.

By default, the first observed row of a duplicate set is considered unique, but
each method has a `keep` parameter to specify targets to be kept.

- `keep='first'` (default): mark / drop duplicates except for the first occurrence.
- `keep='last'`: mark / drop duplicates except for the last occurrence.
- `keep=False`: mark  / drop all duplicates.

```
In [316]: df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
   .....:                     'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
   .....:                     'c': np.random.randn(7)})
   .....: 
In [317]: df2
Out[317]: 
       a  b         c
0    one  x -1.467157
1    one  y  0.113937
2    two  x -1.428572
3    two  y  0.337109
4    two  x  0.052469
5  three  x -2.294560
6   four  x  2.148507
In [318]: df2.duplicated('a')
Out[318]: 
0    False
1     True
2    False
3     True
4     True
5    False
6    False
dtype: bool
In [319]: df2.duplicated('a', keep='last')
Out[319]: 
0     True
1    False
2     True
3     True
4    False
5    False
6    False
dtype: bool
In [320]: df2.duplicated('a', keep=False)
Out[320]: 
0     True
1     True
2     True
3     True
4     True
5    False
6    False
dtype: bool
In [321]: df2.drop_duplicates('a')
Out[321]: 
       a  b         c
0    one  x -1.467157
2    two  x -1.428572
5  three  x -2.294560
6   four  x  2.148507
In [322]: df2.drop_duplicates('a', keep='last')
Out[322]: 
       a  b         c
1    one  y  0.113937
4    two  x  0.052469
5  three  x -2.294560
6   four  x  2.148507
In [323]: df2.drop_duplicates('a', keep=False)
Out[323]: 
       a  b         c
5  three  x -2.294560
6   four  x  2.148507
```
Also, you can pass a list of columns to identify duplications.

```
In [324]: df2.duplicated(['a', 'b'])
Out[324]: 
0    False
1    False
2    False
3    False
4     True
5    False
6    False
dtype: bool
In [325]: df2.drop_duplicates(['a', 'b'])
Out[325]: 
       a  b         c
0    one  x -1.467157
1    one  y  0.113937
2    two  x -1.428572
3    two  y  0.337109
5  three  x -2.294560
6   four  x  2.148507
```
To drop duplicates by index value, use `Index.duplicated` then perform slicing.
The same set of options are available for the `keep` parameter.

```
In [326]: df3 = pd.DataFrame({'a': np.arange(6),
   .....:                     'b': np.random.randn(6)},
   .....:                    index=['a', 'a', 'b', 'c', 'b', 'a'])
   .....: 
In [327]: df3
Out[327]: 
   a         b
a  0 -0.293144
a  1 -1.596615
b  2  0.149716
c  3  0.173897
b  4 -0.049440
a  5  1.394590
In [328]: df3.index.duplicated()
Out[328]: array([False,  True, False, False,  True,  True])
In [329]: df3[~df3.index.duplicated()]
Out[329]: 
   a         b
a  0 -0.293144
b  2  0.149716
c  3  0.173897
In [330]: df3[~df3.index.duplicated(keep='last')]
Out[330]: 
   a         b
c  3  0.173897
b  4 -0.049440
a  5  1.394590
In [331]: df3[~df3.index.duplicated(keep=False)]
Out[331]: 
   a         b
c  3  0.173897
```
Each of Series or DataFrame have a `get` method which can return a
default value.

```
In [332]: s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
In [333]: s.get('a')  # equivalent to s['a']
Out[333]: np.int64(1)
In [334]: s.get('x', default=-1)
Out[334]: -1
```
## Looking up values by index/column labels[#](https://pandas.pydata.org#looking-up-values-by-index-column-labels)

Sometimes you want to extract a set of values given a sequence of row labels
and column labels, this can be achieved by `pandas.factorize`  and NumPy indexing.

For heterogeneous column types, we subset columns to avoid unnecessary NumPy conversions:

```
def pd_lookup_het(df, row_labels, col_labels):
   rows = df.index.get_indexer(row_labels)
   cols = df.columns.get_indexer(col_labels)
   sub = df.take(np.unique(cols), axis=1)
   sub = sub.take(np.unique(rows), axis=0)
   rows = sub.index.get_indexer(row_labels)
   values = sub.melt()["value"]
   cols = sub.columns.get_indexer(col_labels)
   flat_index = rows + cols * len(sub)
   result = values[flat_index]
   return result
```
For homogeneous column types, it is fastest to skip column subsetting and go directly to NumPy:

```
def pd_lookup_hom(df, row_labels, col_labels):
    rows = df.index.get_indexer(row_labels)
    df = df.loc[:, sorted(set(col_labels))]
    cols = df.columns.get_indexer(col_labels)
    result = df.to_numpy()[rows, cols]
    return result
```
Formerly this could be achieved with the dedicated `DataFrame.lookup` method
which was deprecated in version 1.2.0 and removed in version 2.0.0.

## Index objects[#](https://pandas.pydata.org#index-objects)

The pandas [`Index`](https://pandas.pydata.org/reference/api/pandas.Index.html#pandas.Index) class and its subclasses can be viewed as
implementing an *ordered multiset*. Duplicates are allowed.

[`Index`](https://pandas.pydata.org/reference/api/pandas.Index.html#pandas.Index) also provides the infrastructure necessary for
lookups, data alignment, and reindexing. The easiest way to create an
[`Index`](https://pandas.pydata.org/reference/api/pandas.Index.html#pandas.Index) directly is to pass a `list` or other sequence to
[`Index`](https://pandas.pydata.org/reference/api/pandas.Index.html#pandas.Index):

```
In [335]: index = pd.Index(['e', 'd', 'a', 'b'])
In [336]: index
Out[336]: Index(['e', 'd', 'a', 'b'], dtype='str')
In [337]: 'd' in index
Out[337]: True
```
or using numbers:

```
In [338]: index = pd.Index([1, 5, 12])
In [339]: index
Out[339]: Index([1, 5, 12], dtype='int64')
In [340]: 5 in index
Out[340]: True
```
If no dtype is given, `Index` tries to infer the dtype from the data.
It is also possible to give an explicit dtype when instantiating an [`Index`](https://pandas.pydata.org/reference/api/pandas.Index.html#pandas.Index):

```
In [341]: index = pd.Index(['e', 'd', 'a', 'b'], dtype="string")
In [342]: index
Out[342]: Index(['e', 'd', 'a', 'b'], dtype='string')
In [343]: index = pd.Index([1, 5, 12], dtype="int8")
In [344]: index
Out[344]: Index([1, 5, 12], dtype='int8')
In [345]: index = pd.Index([1, 5, 12], dtype="float32")
In [346]: index
Out[346]: Index([1.0, 5.0, 12.0], dtype='float32')
```
You can also pass a `name` to be stored in the index:

```
In [347]: index = pd.Index(['e', 'd', 'a', 'b'], name='something')
In [348]: index.name
Out[348]: 'something'
```
The name, if set, will be shown in the console display:

```
In [349]: index = pd.Index(list(range(5)), name='rows')
In [350]: columns = pd.Index(['A', 'B', 'C'], name='cols')
In [351]: df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)
In [352]: df
Out[352]: 
cols         A         B         C
rows                              
0     0.698035  0.631397  0.816412
1     0.709404 -1.193616 -0.263520
2    -0.878602  0.035458 -0.285808
3    -0.957431  2.243279 -1.124957
4    -1.994374  0.050270  0.512794
In [353]: df['A']
Out[353]: 
rows
0    0.698035
1    0.709404
2   -0.878602
3   -0.957431
4   -1.994374
Name: A, dtype: float64
```
### Setting metadata[#](https://pandas.pydata.org#setting-metadata)

Indexes are “mostly immutable”, but it is possible to set and change their
`name` attribute. You can use the `rename`, `set_names` to set these attributes
directly, and they default to returning a copy.

See [Advanced Indexing](https://pandas.pydata.org/advanced.html#advanced) for usage of MultiIndexes.

```
In [354]: ind = pd.Index([1, 2, 3])
In [355]: ind.rename("apple")
Out[355]: Index([1, 2, 3], dtype='int64', name='apple')
In [356]: ind
Out[356]: Index([1, 2, 3], dtype='int64')
In [357]: ind = ind.set_names(["apple"])
In [358]: ind.name = "bob"
In [359]: ind
Out[359]: Index([1, 2, 3], dtype='int64', name='bob')
```
`set_names`, `set_levels`, and `set_codes` also take an optional
`level` argument

```
In [360]: index = pd.MultiIndex.from_product([range(3), ['one', 'two']], names=['first', 'second'])
In [361]: index
Out[361]: 
MultiIndex([(0, 'one'),
            (0, 'two'),
            (1, 'one'),
            (1, 'two'),
            (2, 'one'),
            (2, 'two')],
           names=['first', 'second'])
In [362]: index.levels[1]
Out[362]: Index(['one', 'two'], dtype='str', name='second')
In [363]: index.set_levels(["a", "b"], level=1)
Out[363]: 
MultiIndex([(0, 'a'),
            (0, 'b'),
            (1, 'a'),
            (1, 'b'),
            (2, 'a'),
            (2, 'b')],
           names=['first', 'second'])
```
### Set operations on Index objects[#](https://pandas.pydata.org#set-operations-on-index-objects)

The two main operations are `union` and `intersection`.
Difference is provided via the `.difference()` method.

```
In [364]: a = pd.Index(['c', 'b', 'a'])
In [365]: b = pd.Index(['c', 'e', 'd'])
In [366]: a.difference(b)
Out[366]: Index(['a', 'b'], dtype='str')
```
Also available is the `symmetric_difference` operation, which returns elements
that appear in either `idx1` or `idx2`, but not in both. This is
equivalent to the Index created by `idx1.difference(idx2).union(idx2.difference(idx1))`,
with duplicates dropped.

```
In [367]: idx1 = pd.Index([1, 2, 3, 4])
In [368]: idx2 = pd.Index([2, 3, 4, 5])
In [369]: idx1.symmetric_difference(idx2)
Out[369]: Index([1, 5], dtype='int64')
```
Note

The resulting index from a set operation will be sorted in ascending order.

When performing [`Index.union()`](https://pandas.pydata.org/reference/api/pandas.Index.union.html#pandas.Index.union) between indexes with different dtypes, the indexes
must be cast to a common dtype. Typically, though not always, this is object dtype. The
exception is when performing a union between integer and float data. In this case, the
integer values are converted to float

```
In [370]: idx1 = pd.Index([0, 1, 2])
In [371]: idx2 = pd.Index([0.5, 1.5])
In [372]: idx1.union(idx2)
Out[372]: Index([0.0, 0.5, 1.0, 1.5, 2.0], dtype='float64')
```
### Missing values[#](https://pandas.pydata.org#missing-values)

Important

Even though `Index` can hold missing values (`NaN`), it should be avoided
if you do not want any unexpected results. For example, some operations
exclude missing values implicitly.

`Index.fillna` fills missing values with specified scalar value.

```
In [373]: idx1 = pd.Index([1, np.nan, 3, 4])
In [374]: idx1
Out[374]: Index([1.0, nan, 3.0, 4.0], dtype='float64')
In [375]: idx1.fillna(2)
Out[375]: Index([1.0, 2.0, 3.0, 4.0], dtype='float64')
In [376]: idx2 = pd.DatetimeIndex([pd.Timestamp('2011-01-01'),
   .....:                          pd.NaT,
   .....:                          pd.Timestamp('2011-01-03')])
   .....: 
In [377]: idx2
Out[377]: 
DatetimeIndex(['2011-01-01', 'NaT', '2011-01-03'], dtype='datetime64[us]',
              freq=None)
In [378]: idx2.fillna(pd.Timestamp('2011-01-02'))
Out[378]: 
DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'],
              dtype='datetime64[us]', freq=None)
```
## Set / reset index[#](https://pandas.pydata.org#set-reset-index)

Occasionally you will load or create a data set into a DataFrame and want to add an index after you’ve already done so. There are a couple of different ways.

### Set an index[#](https://pandas.pydata.org#set-an-index)

DataFrame has a [`set_index()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index) method which takes a column name
(for a regular `Index`) or a list of column names (for a `MultiIndex`).
To create a new, re-indexed DataFrame:

```
In [379]: data = pd.DataFrame({'a': ['bar', 'bar', 'foo', 'foo'],
   .....:                      'b': ['one', 'two', 'one', 'two'],
   .....:                      'c': ['z', 'y', 'x', 'w'],
   .....:                      'd': [1., 2., 3, 4]})
   .....: 
In [380]: data
Out[380]: 
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0
In [381]: indexed1 = data.set_index('c')
In [382]: indexed1
Out[382]: 
     a    b    d
c               
z  bar  one  1.0
y  bar  two  2.0
x  foo  one  3.0
w  foo  two  4.0
In [383]: indexed2 = data.set_index(['a', 'b'])
In [384]: indexed2
Out[384]: 
         c    d
a   b          
bar one  z  1.0
    two  y  2.0
foo one  x  3.0
    two  w  4.0
```
The `append` keyword option allow you to keep the existing index and append
the given columns to a MultiIndex:

```
In [385]: frame = data.set_index('c', drop=False)
In [386]: frame = frame.set_index(['a', 'b'], append=True)
In [387]: frame
Out[387]: 
           c    d
c a   b          
z bar one  z  1.0
y bar two  y  2.0
x foo one  x  3.0
w foo two  w  4.0
```
Other options in `set_index` allow you not drop the index columns.

```
In [388]: data.set_index('c', drop=False)
Out[388]: 
     a    b  c    d
c                  
z  bar  one  z  1.0
y  bar  two  y  2.0
x  foo  one  x  3.0
w  foo  two  w  4.0
```
### Reset the index[#](https://pandas.pydata.org#reset-the-index)

As a convenience, there is a new function on DataFrame called
[`reset_index()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index) which transfers the index values into the
DataFrame’s columns and sets a simple integer index.
This is the inverse operation of [`set_index()`](https://pandas.pydata.org/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index).

```
In [389]: data
Out[389]: 
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0
In [390]: data.reset_index()
Out[390]: 
   index    a    b  c    d
0      0  bar  one  z  1.0
1      1  bar  two  y  2.0
2      2  foo  one  x  3.0
3      3  foo  two  w  4.0
```
The output is more similar to a SQL table or a record array. The names for the
columns derived from the index are the ones stored in the `names` attribute.

You can use the `level` keyword to remove only a portion of the index:

```
In [391]: frame
Out[391]: 
           c    d
c a   b          
z bar one  z  1.0
y bar two  y  2.0
x foo one  x  3.0
w foo two  w  4.0
In [392]: frame.reset_index(level=1)
Out[392]: 
         a  c    d
c b               
z one  bar  z  1.0
y two  bar  y  2.0
x one  foo  x  3.0
w two  foo  w  4.0
```
`reset_index` takes an optional parameter `drop` which if true simply
discards the index, instead of putting index values in the DataFrame’s columns.

### Adding an ad hoc index[#](https://pandas.pydata.org#adding-an-ad-hoc-index)

You can assign a custom index to the `index` attribute:

```
In [393]: df_idx = pd.DataFrame(range(4))
In [394]: df_idx.index = pd.Index([10, 20, 30, 40], name="a")
In [395]: df_idx
Out[395]: 
    0
a    
10  0
20  1
30  2
40  3
```
### Why does assignment fail when using chained indexing?[#](https://pandas.pydata.org#why-does-assignment-fail-when-using-chained-indexing)

[Copy-on-Write](https://pandas.pydata.org/migration.html#copy-on-write) is the new default with pandas 3.0.
This means that chained indexing will never work.
See [this section](https://pandas.pydata.org/migration.html#copy-on-write-chained-assignment)
for more context.

## Series Assignment and Index Alignment[#](https://pandas.pydata.org#series-assignment-and-index-alignment)

When assigning a Series to a DataFrame column, pandas performs automatic alignment based on index labels. This is a fundamental behavior that can be surprising to new users who might expect positional assignment.

### Key Points:[#](https://pandas.pydata.org#key-points)

- Series values are matched to DataFrame rows by index label
- Position/order in the Series doesn’t matter
- Missing index labels result in NaN values
- This behavior is consistent across df\[col\] = series and df.loc\[:, col\] = series

You can think of this as reindexing the Series to the DataFrame index before
assignment (for example, `df[col] = series.reindex(df.index)`).

Examples: .. ipython:: python

import pandas as pd

\# Create a DataFrame df = pd.DataFrame({‘values’: \[1, 2, 3\]}, index=\[‘x’, ‘y’, ‘z’\])

\# Series with matching indices (different order) s1 = pd.Series(\[10, 20, 30\], index=\[‘z’, ‘x’, ‘y’\]) df\[‘aligned’\] = s1 # Aligns by index, not position print(df)

\# Series with partial index match s2 = pd.Series(\[100, 200\], index=\[‘x’, ‘z’\]) df\[‘partial’\] = s2 # Missing ‘y’ gets NaN print(df)

\# Series with non-matching indices s3 = pd.Series(\[1000, 2000\], index=\[‘a’, ‘b’\]) df\[‘nomatch’\] = s3 # All values become NaN print(df)

#Avoiding Confusion: #If you want positional assignment instead of index alignment: # reset the Series index to match DataFrame index df\[‘s1\_values’\] = s1.reindex(df.index)


## Column assignment vs. in-place setting[#](https://pandas.pydata.org#column-assignment-vs-in-place-setting)

While index alignment is consistent between `df[col] = value` and
`df.loc[:, col] = value` (see the previous section), the two forms differ in
how they treat the column’s existing dtype:

- `df[col] = value` **replaces** the column. The new column’s dtype is
inferred from `value`, regardless of what dtype the old column had.
- `df.loc[:, col] = value` (and `df.iloc[:, i] = value`) **sets the values
in place** in the existing column. The original dtype is preserved, and the
assignment will raise `TypeError` if `value` is not compatible with it.

This is most visible for `ExtensionDtype` columns
such as `category`, `Int64`, `boolean`, or `string`, where the
replacing form silently drops the extension dtype:

```
In [396]: df = pd.DataFrame({"a": pd.Categorical(["x", "y"], categories=["x", "y", "z"])})
In [397]: df["a"] = "z"          # replaces the column
In [398]: df.dtypes
Out[398]: 
a    str
dtype: object
In [399]: df = pd.DataFrame({"a": pd.Categorical(["x", "y"], categories=["x", "y", "z"])})
In [400]: df.loc[:, "a"] = "z"   # sets values in place
In [401]: df.dtypes
Out[401]: 
a    category
dtype: object
```
The same distinction applies to nullable numeric and boolean dtypes:

```
In [402]: df = pd.DataFrame({"a": pd.array([1, 2], dtype="Int64")})
In [403]: df["a"] = 5
In [404]: df.dtypes
Out[404]: 
a    int64
dtype: object
In [405]: df = pd.DataFrame({"a": pd.array([1, 2], dtype="Int64")})
In [406]: df.loc[:, "a"] = 5
In [407]: df.dtypes
Out[407]: 
a    Int64
dtype: object
```
Use `df.loc[:, col] = value` (or `.iloc`) when you want to update every
value of an existing column while keeping its dtype.