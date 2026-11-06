---
id: "pandas_022"
technology: "pandas"
category: "ML & Data"
title: "Table Visualization — pandas 3.1.0 documentation"
doc_order: 22
source_url: "https://pandas.pydata.org/docs/user_guide/style.html"
language: "en"
retrieved_at: "2026-11-03 17:57:37"
content_hash: "6de24112e0eafd069ec5f3ccbd87fa2f736e84781938d95d57f473a91923813b"
---

# Table Visualization — pandas 3.1.0 documentation

Source: https://pandas.pydata.org/docs/user_guide/style.html

---

# Table Visualization[#](https://pandas.pydata.org#Table-Visualization)

This section demonstrates visualization of tabular data using the [Styler](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.html) class. For information on visualization with charting please see [Chart Visualization](https://pandas.pydata.org/visualization.html). This document is written as a Jupyter Notebook, and can be viewed or downloaded [here](https://nbviewer.org/github/pandas-dev/pandas/blob/main/doc/source/user_guide/style.ipynb).

## Styler Object and Customising the Display[#](https://pandas.pydata.org#Styler-Object-and-Customising-the-Display)

Styling and output display customisation should be performed **after** the data in a DataFrame has been processed. The Styler is **not** dynamically updated if further changes to the DataFrame are made. The `DataFrame.style` attribute is a property that returns a [Styler](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.html) object. It has a `_repr_html_` method defined on it so it is rendered automatically in Jupyter Notebook.

The Styler, which can be used for large data but is primarily designed for small data, currently has the ability to output to these formats:

- HTML
- LaTeX
- String (and CSV by extension)
- Excel
- (JSON is not currently available)

The first three of these have display customisation methods designed to format and customise the output. These include:

- Formatting values, the index and columns headers, using [.format()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.format.html) and [.format\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.format_index.html),
- Renaming the index or column header labels, using [.relabel\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
- Hiding certain columns, the index and/or column headers, or index names, using [.hide()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.hide.html)
- Concatenating similar DataFrames, using [.concat()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.concat.html)

## Formatting the Display[#](https://pandas.pydata.org#Formatting-the-Display)

### Formatting Values[#](https://pandas.pydata.org#Formatting-Values)

The [Styler](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.html) distinguishes the *display* value from the *actual* value, in both data values and index or columns headers. To control the display value, the text is printed in each cell as a string, and we can use the [.format()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.format.html) and [.format\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.format_index.html) methods to manipulate this according to a [format spec
string](https://docs.python.org/3/library/string.html#format-specification-mini-language) or a callable that takes a single value and returns a string. It is possible to define this for the whole table, or index, or for individual columns, or MultiIndex levels. We can also overwrite index names.

Additionally, the format function has a **precision** argument to specifically help format floats, as well as **decimal** and **thousands** separators to support other locales, an **na\_rep** argument to display missing data, and an **escape** and **hyperlinks** arguments to help displaying safe-HTML or safe-LaTeX. The default formatter is configured to adopt pandas’ global options such as `styler.format.precision` option, controllable using `with pd.option_context('format.precision', 2):`

```
import pandas as pd
import numpy as np
df = pd.DataFrame(
    {"strings": ["Adam", "Mike"], "ints": [1, 3], "floats": [1.123, 1000.23]}
)
df.style.format(precision=3, thousands=".", decimal=",").format_index(
    str.upper, axis=1
).relabel_index(["row 1", "row 2"], axis=0)
```
|  | STRINGS | INTS | FLOATS | 
|---|---|---|---|
| row 1 | Adam | 1 | 1,123 | 
| row 2 | Mike | 3 | 1.000,230 | 

Using Styler to manipulate the display is a useful feature because maintaining the indexing and data values for other purposes gives greater control. You do not have to overwrite your DataFrame to display it how you like. Here is a more comprehensive example of using the formatting functions whilst still relying on the underlying data for indexing and calculations.

```
weather_df = pd.DataFrame(
    np.random.default_rng().random((10, 2)) * 5,
    index=pd.date_range(start="2021-01-01", periods=10),
    columns=["Tokyo", "Beijing"],
)
def rain_condition(v):
    if v < 1.75:
        return "Dry"
    elif v < 2.75:
        return "Rain"
    return "Heavy Rain"
def make_pretty(styler):
    styler.set_caption("Weather Conditions")
    styler.format(rain_condition)
    styler.format_index(lambda v: v.strftime("%A"))
    styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
    return styler
weather_df
```
|  | Tokyo | Beijing | 
|---|---|---|
| 2021-01-01 | 4.033111 | 3.556714 | 
| 2021-01-02 | 3.394422 | 4.036322 | 
| 2021-01-03 | 3.751606 | 3.553571 | 
| 2021-01-04 | 1.839333 | 0.957087 | 
| 2021-01-05 | 3.079616 | 1.469691 | 
| 2021-01-06 | 3.130261 | 3.908887 | 
| 2021-01-07 | 0.024447 | 0.632783 | 
| 2021-01-08 | 0.134889 | 2.914216 | 
| 2021-01-09 | 2.651961 | 0.675605 | 
| 2021-01-10 | 4.208827 | 2.859148 | 

```
weather_df.loc["2021-01-04":"2021-01-08"].style.pipe(make_pretty)
```
| Weather Conditions |  |  | 
|---|---|---|
|  | Tokyo | Beijing | 
|---|---|---|
| Monday | Rain | Dry | 
| Tuesday | Heavy Rain | Dry | 
| Wednesday | Heavy Rain | Heavy Rain | 
| Thursday | Dry | Dry | 
| Friday | Dry | Heavy Rain | 

### Hiding Data[#](https://pandas.pydata.org#Hiding-Data)

The index and column headers can be completely hidden, as well subselecting rows or columns that one wishes to exclude. Both these options are performed using the same methods.

The index can be hidden from rendering by calling [.hide()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.hide.html) without any arguments, which might be useful if your index is integer based. Similarly column headers can be hidden by calling [.hide(axis=”columns”)](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.hide.html) without any further arguments.

Specific rows or columns can be hidden from rendering by calling the same [.hide()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.hide.html) method and passing in a row/column label, a list-like or a slice of row/column labels to for the `subset` argument.

Hiding does not change the integer arrangement of CSS classes, e.g. hiding the first two columns of a DataFrame means the column class indexing will still start at `col2`, since `col0` and `col1` are simply ignored.

```
df = pd.DataFrame(np.random.default_rng().standard_normal((5, 5)))
df.style.hide(subset=[0, 2, 4], axis=0).hide(subset=[0, 2, 4], axis=1)
```
|  | 1 | 3 | 
|---|---|---|
| 1 | -0.966782 | 1.848126 | 
| 3 | 1.046144 | -0.232372 | 

To invert the function to a **show** functionality it is best practice to compose a list of hidden items.

```
show = [0, 2, 4]
df.style.hide([row for row in df.index if row not in show], axis=0).hide(
    [col for col in df.columns if col not in show], axis=1
)
```
|  | 0 | 2 | 4 | 
|---|---|---|---|
| 0 | 1.437440 | -0.123694 | 1.185940 | 
| 2 | -0.320181 | -0.391897 | -0.611419 | 
| 4 | -1.047904 | 1.006907 | -0.180358 | 

### Concatenating DataFrame Outputs[#](https://pandas.pydata.org#Concatenating-DataFrame-Outputs)

Two or more Stylers can be concatenated together provided they share the same columns. This is very useful for showing summary statistics for a DataFrame, and is often used in combination with DataFrame.agg.

Since the objects concatenated are Stylers they can independently be styled as will be shown below and their concatenation preserves those styles.

```
summary_styler = (
    df.agg(["sum", "mean"]).style.format(precision=3).relabel_index(["Sum", "Average"])
)
df.style.format(precision=1).concat(summary_styler)
```
|  | 0 | 1 | 2 | 3 | 4 | 
|---|---|---|---|---|---|
| 0 | 1.4 | 1.4 | -0.1 | -0.9 | 1.2 | 
| 1 | 1.6 | -1.0 | -1.5 | 1.8 | 1.1 | 
| 2 | -0.3 | -0.5 | -0.4 | -1.7 | -0.6 | 
| 3 | -0.4 | 1.0 | -0.2 | -0.2 | -2.2 | 
| 4 | -1.0 | 0.3 | 1.0 | -0.7 | -0.2 | 
| Sum | 1.286 | 1.296 | -1.261 | -1.617 | -0.756 | 
| Average | 0.257 | 0.259 | -0.252 | -0.323 | -0.151 | 

## Styler Object and HTML[#](https://pandas.pydata.org#Styler-Object-and-HTML)

The [Styler](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.html) was originally constructed to support the wide array of HTML formatting options. Its HTML output creates an HTML `<table>` and leverages CSS styling language to manipulate many parameters including colors, fonts, borders, background, etc. See [here](https://www.w3schools.com/html/html_tables.asp) for more information on styling HTML tables. This allows a lot of flexibility out of the box, and even enables web developers to
integrate DataFrames into their existing user interface designs.

Below we demonstrate the default output, which looks very similar to the standard DataFrame HTML representation. But the HTML here has already attached some CSS classes to each cell, even if we haven’t yet created any styles. We can view these by calling the [.to\_html()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.to_html.html) method, which returns the raw HTML as string, which is useful for further processing or adding to a file - read on in [More about CSS and
HTML](https://pandas.pydata.org#More-About-CSS-and-HTML). This section will also provide a walkthrough for how to convert this default output to represent a DataFrame output that is more communicative. For example how we can build `s`:

```
idx = pd.Index(["Tumour (Positive)", "Non-Tumour (Negative)"], name="Actual Label:")
cols = pd.MultiIndex.from_product(
    [["Decision Tree", "Regression", "Random"], ["Tumour", "Non-Tumour"]],
    names=["Model:", "Predicted:"],
)
df = pd.DataFrame(
    [[38.0, 2.0, 18.0, 22.0, 21, np.nan], [19, 439, 6, 452, 226, 232]],
    index=idx,
    columns=cols,
)
df.style
```
| Model: | Decision Tree |  | Regression |  | Random |  | 
|---|---|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  |  |  | 
| Tumour (Positive) | 38.000000 | 2.000000 | 18.000000 | 22.000000 | 21 | nan | 
| Non-Tumour (Negative) | 19.000000 | 439.000000 | 6.000000 | 452.000000 | 226 | 232.000000 | 

```
s
```
| Confusion matrix for multiple cancer prediction models. |  |  |  |  | 
|---|---|---|---|---|
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

The first step we have taken is the create the Styler object from the DataFrame and then select the range of interest by hiding unwanted columns with [.hide()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.hide.html).

```
s = df.style.format("{:.0f}").hide(
    [("Random", "Tumour"), ("Random", "Non-Tumour")], axis="columns"
)
s
```
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

## Methods to Add Styles[#](https://pandas.pydata.org#Methods-to-Add-Styles)

There are **3 primary methods of adding custom CSS styles** to [Styler](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.html):

- Using [.set\_table\_styles()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_table_styles.html) to control broader areas of the table with specified internal CSS. Although table styles allow the flexibility to add CSS selectors and properties controlling all individual parts of the table, they are unwieldy for individual cell specifications. Also, note that table styles cannot be exported to Excel.
- Using [.set\_td\_classes()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_td_classes.html) to directly link either external CSS classes to your data cells or link the internal CSS classes created by [.set\_table\_styles()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_table_styles.html). See [here](https://pandas.pydata.org#Setting-Classes-and-Linking-to-External-CSS). These cannot be used on column header rows or indexes, and also won’t export to Excel.
- Using the [.apply()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.apply.html) and [.map()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.map.html) functions to add direct internal CSS to specific data cells. See [here](https://pandas.pydata.org#Styler-Functions). As of v1.4.0 there are also methods that work directly on column header rows or indexes: [.apply\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.apply_index.html) and [.map\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.map_index.html). Note that only these methods add styles that will export to Excel. These methods work in a similar way to [DataFrame.apply()](https://pandas.pydata.org/reference/api/pandas.DataFrame.apply.html) and [DataFrame.map()](https://pandas.pydata.org/reference/api/pandas.DataFrame.map.html).

## Table Styles[#](https://pandas.pydata.org#Table-Styles)

Table styles are flexible enough to control all individual parts of the table, including column headers and indexes. However, they can be unwieldy to type for individual data cells or for any kind of conditional formatting, so we recommend that table styles are used for broad styling, such as entire rows or columns at a time.

Table styles are also used to control features which can apply to the whole table at once such as creating a generic hover functionality. The `:hover` pseudo-selector, as well as other pseudo-selectors, can only be used this way.

To replicate the normal format of CSS selectors and properties (attribute value pairs), e.g.

the necessary format to pass styles to [.set\_table\_styles()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_table_styles.html) is as a list of dicts, each with a CSS-selector tag and CSS-properties. Properties can either be a list of 2-tuples, or a regular CSS-string, for example:

```
cell_hover = {  # for row hover use <tr> instead of <td>
    "selector": "td:hover",
    "props": [("background-color", "#ffffb3")],
}
index_names = {
    "selector": ".index_name",
    "props": "font-style: italic; color: darkgrey; font-weight:normal;",
}
headers = {
    "selector": "th:not(.index_name)",
    "props": "background-color: #000066; color: white;",
}
s.set_table_styles([cell_hover, index_names, headers])
```
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

Next we just add a couple more styling artifacts targeting specific parts of the table. Be careful here, since we are *chaining methods* we need to explicitly instruct the method **not to** `overwrite` the existing styles.

```
s.set_table_styles(
    [
        {"selector": "th.col_heading", "props": "text-align: center;"},
        {"selector": "th.col_heading.level0", "props": "font-size: 1.5em;"},
        {"selector": "td", "props": "text-align: center; font-weight: bold;"},
    ],
    overwrite=False,
)
```
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

As a convenience method (*since version 1.2.0*) we can also pass a **dict** to [.set\_table\_styles()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_table_styles.html) which contains row or column keys. Behind the scenes Styler just indexes the keys and adds relevant `.col<m>` or `.row<n>` classes as necessary to the given CSS selectors.

```
s.set_table_styles(
    {
        ("Regression", "Tumour"): [
            {"selector": "th", "props": "border-left: 1px solid white"},
            {"selector": "td", "props": "border-left: 1px solid #000066"},
        ]
    },
    overwrite=False,
    axis=0,
)
```
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

## Setting Classes and Linking to External CSS[#](https://pandas.pydata.org#Setting-Classes-and-Linking-to-External-CSS)

If you have designed a website then it is likely you will already have an external CSS file that controls the styling of table and cell objects within it. You may want to use these native files rather than duplicate all the CSS in python (and duplicate any maintenance work).

### Table Attributes[#](https://pandas.pydata.org#Table-Attributes)

It is very easy to add a `class` to the main `<table>` using [.set\_table\_attributes()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html). This method can also attach inline styles - read more in [CSS Hierarchies](https://pandas.pydata.org#CSS-Hierarchies).

```
out = s.set_table_attributes('class="my-table-cls"').to_html()
print(out[out.find("<table") :][:109])
```
```
<table id="T_xyz01" class="my-table-cls">
  <thead>
    <tr>
      <th class="index_name level0" >Model:</th>
```
### Data Cell CSS Classes[#](https://pandas.pydata.org#Data-Cell-CSS-Classes)

*New in version 1.2.0*

The [.set\_td\_classes()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_td_classes.html) method accepts a DataFrame with matching indices and columns to the underlying [Styler](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.html)’s DataFrame. That DataFrame will contain strings as css-classes to add to individual data cells: the `<td>` elements of the `<table>`. Rather than use external CSS we will create our classes internally and add them to table style. We will save adding the
borders until the [section on tooltips](https://pandas.pydata.org#Tooltips-and-Captions).

```
s.set_table_styles(
    [  # create internal CSS classes
        {"selector": ".true", "props": "background-color: #e6ffe6;"},
        {"selector": ".false", "props": "background-color: #ffe6e6;"},
    ],
    overwrite=False,
)
cell_color = pd.DataFrame(
    [["true ", "false ", "true ", "false "], ["false ", "true ", "false ", "true "]],
    index=df.index,
    columns=df.columns[:4],
)
s.set_td_classes(cell_color)
```
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

## Styler Functions[#](https://pandas.pydata.org#Styler-Functions)

### Acting on Data[#](https://pandas.pydata.org#Acting-on-Data)

We use the following methods to pass your style functions. Both of those methods take a function (and some other keyword arguments) and apply it to the DataFrame in a certain way, rendering CSS styles.

- [.map()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.map.html) (elementwise): accepts a function that takes a single value and returns a string with the CSS attribute-value pair.
- [.apply()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.apply.html) (column-/row-/table-wise): accepts a function that takes a Series or DataFrame and returns a Series, DataFrame, or numpy array with an identical shape where each element is a string with a CSS attribute-value pair. This method passes each column or row of your DataFrame one-at-a-time or the entire table at once, depending on the `axis` keyword argument. For columnwise use `axis=0`, rowwise use `axis=1`, and for the
entire table at once use `axis=None`.

This method is powerful for applying multiple, complex logic to data cells. We create a new DataFrame to demonstrate this.

```
df2 = pd.DataFrame(
    np.random.default_rng(0).standard_normal((10, 4)), columns=["A", "B", "C", "D"]
)
df2.style
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

For example we can build a function that colors text if it is negative, and chain this with a function that partially fades cells of negligible value. Since this looks at each element in turn we use `map`.

```
def style_negative(v, props=""):
    return props if v < 0 else None
s2 = df2.style.map(style_negative, props="color:red;").map(
    lambda v: "opacity: 20%;" if (v < 0.3) and (v > -0.3) else None
)
s2
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

We can also build a function that highlights the maximum value across rows, cols, and the DataFrame all at once. In this case we use `apply`. Below we highlight the maximum in a column.

```
def highlight_max(s, props=""):
    return np.where(s == np.nanmax(s.values), props, "")
s2.apply(highlight_max, props="color:white;background-color:darkblue", axis=0)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

We can use the same function across the different axes, highlighting here the DataFrame maximum in purple, and row maximums in pink.

```
s2.apply(highlight_max, props="color:white;background-color:pink;", axis=1).apply(
    highlight_max, props="color:white;background-color:purple", axis=None
)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

This last example shows how some styles have been overwritten by others. In general the most recent style applied is active but you can read more in the [section on CSS hierarchies](https://pandas.pydata.org#CSS-Hierarchies). You can also apply these styles to more granular parts of the DataFrame - read more in section on [subset slicing](https://pandas.pydata.org#Finer-Control-with-Slicing).

It is possible to replicate some of this functionality using just classes but it can be more cumbersome. See [item 3) of Optimization](https://pandas.pydata.org#Optimization)

*Debugging Tip*: If you’re having trouble writing your style function, try just passing it into `DataFrame.apply`. Internally, `Styler.apply` uses `DataFrame.apply` so the result should be the same, and with `DataFrame.apply` you will be able to inspect the CSS string output of your intended function in each cell.

### Acting on the Index and Column Headers[#](https://pandas.pydata.org#Acting-on-the-Index-and-Column-Headers)

Similar application is achieved for headers by using:

- [.map\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.map_index.html) (elementwise): accepts a function that takes a single value and returns a string with the CSS attribute-value pair.
- [.apply\_index()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.apply_index.html) (level-wise): accepts a function that takes a Series and returns a Series, or numpy array with an identical shape where each element is a string with a CSS attribute-value pair. This method passes each level of your Index one-at-a-time. To style the index use `axis=0` and to style the column headers use `axis=1`.

You can select a `level` of a `MultiIndex` but currently no similar `subset` application is available for these methods.

```
s2.map_index(lambda v: "color:pink;" if v > 4 else "color:darkblue;", axis=0)
s2.apply_index(
    lambda s: np.where(s.isin(["A", "B"]), "color:pink;", "color:darkblue;"), axis=1
)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

## Tooltips and Captions[#](https://pandas.pydata.org#Tooltips-and-Captions)

Table captions can be added with the [.set\_caption()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_caption.html) method. You can use table styles to control the CSS relevant to the caption.

```
s.set_caption(
    "Confusion matrix for multiple cancer prediction models."
).set_table_styles(
    [{"selector": "caption", "props": "caption-side: bottom; font-size:1.25em;"}],
    overwrite=False,
)
```
| Confusion matrix for multiple cancer prediction models. |  |  |  |  | 
|---|---|---|---|---|
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

Adding tooltips (*since version 1.3.0*) can be done using the [.set\_tooltips()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_tooltips.html) method in the same way you can add CSS classes to data cells by providing a string based DataFrame with intersecting indices and columns. You don’t have to specify a `css_class` name or any css `props` for the tooltips, since there are standard defaults, but the option is there if you want more visual control.

```
tt = pd.DataFrame(
    [
        [
            "This model has a very strong true positive rate",
            "This model's total number of false negatives is too high",
        ]
    ],
    index=["Tumour (Positive)"],
    columns=df.columns[[0, 3]],
)
s.set_tooltips(
    tt,
    props="visibility: hidden; position: absolute; z-index: 1; "
    "border: 1px solid #000066;"
    "background-color: white; color: #000066; font-size: 0.8em;"
    "transform: translate(0px, -24px); padding: 0.6em; "
    "border-radius: 0.5em;",
)
```
| Confusion matrix for multiple cancer prediction models. |  |  |  |  | 
|---|---|---|---|---|
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

The only thing left to do for our table is to add the highlighting borders to draw the audience attention to the tooltips. We will create internal CSS classes as before using table styles. **Setting classes always overwrites** so we need to make sure we add the previous classes.

```
s.set_table_styles(
    [  # create internal CSS classes
        {"selector": ".border-red", "props": "border: 2px dashed red;"},
        {"selector": ".border-green", "props": "border: 2px dashed green;"},
    ],
    overwrite=False,
)
cell_border = pd.DataFrame(
    [["border-green ", " ", " ", "border-red "], [" ", " ", " ", " "]],
    index=df.index,
    columns=df.columns[:4],
)
s.set_td_classes(cell_color + cell_border)
```
| Confusion matrix for multiple cancer prediction models. |  |  |  |  | 
|---|---|---|---|---|
| Model: | Decision Tree |  | Regression |  | 
|---|---|---|---|---|
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | 
| Actual Label: |  |  |  |  | 
| Tumour (Positive) | 38 | 2 | 18 | 22 | 
| Non-Tumour (Negative) | 19 | 439 | 6 | 452 | 

## Finer Control with Slicing[#](https://pandas.pydata.org#Finer-Control-with-Slicing)

The examples we have shown so far for the `Styler.apply` and `Styler.map` functions have not demonstrated the use of the `subset` argument. This is a useful argument which permits a lot of flexibility: it allows you to apply styles to specific rows or columns, without having to code that logic into your `style` function.

The value passed to `subset` behaves similar to slicing a DataFrame;

- A scalar is treated as a column label
- A list (or Series or NumPy array) is treated as multiple column labels
- A tuple is treated as `(row_indexer, column_indexer)`

Consider using `pd.IndexSlice` to construct the tuple for the last one. We will create a MultiIndexed DataFrame to demonstrate the functionality.

```
df3 = pd.DataFrame(
    np.random.default_rng().standard_normal((4, 4)),
    pd.MultiIndex.from_product([["A", "B"], ["r1", "r2"]]),
    columns=["c1", "c2", "c3", "c4"],
)
df3
```
|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

We will use subset to highlight the maximum in the third and fourth columns with red text. We will highlight the subset sliced region in yellow.

```
slice_ = ["c3", "c4"]
df3.style.apply(
    highlight_max, props="color:red;", axis=0, subset=slice_
).set_properties(**{"background-color": "#ffffb3"}, subset=slice_)
```
|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

If combined with the `IndexSlice` as suggested then it can index across both dimensions with greater flexibility.

```
idx = pd.IndexSlice
slice_ = idx[idx[:, "r1"], idx["c2":"c4"]]
df3.style.apply(
    highlight_max, props="color:red;", axis=0, subset=slice_
).set_properties(**{"background-color": "#ffffb3"}, subset=slice_)
```
|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

This also provides the flexibility to sub select rows when used with the `axis=1`.

```
slice_ = idx[idx[:, "r2"], :]
df3.style.apply(
    highlight_max, props="color:red;", axis=1, subset=slice_
).set_properties(**{"background-color": "#ffffb3"}, subset=slice_)
```
|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

There is also scope to provide **conditional filtering**.

Suppose we want to highlight the maximum across columns 2 and 4 only in the case that the sum of columns 1 and 3 is less than -2.0 *(essentially excluding rows* `(:,'r2')`*)*.

```
slice_ = idx[idx[(df3["c1"] + df3["c3"]) < -2.0], ["c2", "c4"]]
df3.style.apply(
    highlight_max, props="color:red;", axis=1, subset=slice_
).set_properties(**{"background-color": "#ffffb3"}, subset=slice_)
```
|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

Only label-based slicing is supported right now, not positional, and not callables.

If your style function uses a `subset` or `axis` keyword argument, consider wrapping your function in a `functools.partial`, partialing out that keyword.

```
my_func2 = functools.partial(my_func, subset=42)
```
## Optimization[#](https://pandas.pydata.org#Optimization)

Generally, for smaller tables and most cases, the rendered HTML does not need to be optimized, and we don’t really recommend it. There are two cases where it is worth considering:

- If you are rendering and styling a very large HTML table, certain browsers have performance issues.
- If you are using `Styler` to dynamically create part of online user interfaces and want to improve network performance.

Here we recommend the following steps to implement:

### 1. Remove UUID and cell\_ids[#](https://pandas.pydata.org#1.-Remove-UUID-and-cell_ids)

Ignore the `uuid` and set `cell_ids` to `False`. This will prevent unnecessary HTML.

This is sub-optimal:

```
df4 = pd.DataFrame([[1, 2], [3, 4]])
s4 = df4.style
```
This is better:

```
from pandas.io.formats.style import Styler
s4 = Styler(df4, uuid_len=0, cell_ids=False)
```
### 2. Use table styles[#](https://pandas.pydata.org#2.-Use-table-styles)

Use table styles where possible (e.g. for all cells or rows or columns at a time) since the CSS is nearly always more efficient than other formats.

This is sub-optimal:

```
props = 'font-family: "Times New Roman", Times, serif; color: #e83e8c; font-size:1.3em;'
df4.style.map(lambda x: props, subset=[1])
```
|  | 0 | 1 | 
|---|---|---|
| 0 | 1 | 2 | 
| 1 | 3 | 4 | 

This is better:

```
df4.style.set_table_styles([{"selector": "td.col1", "props": props}])
```
|  | 0 | 1 | 
|---|---|---|
| 0 | 1 | 2 | 
| 1 | 3 | 4 | 

### 3. Set classes instead of using Styler functions[#](https://pandas.pydata.org#3.-Set-classes-instead-of-using-Styler-functions)

For large DataFrames where the same style is applied to many cells it can be more efficient to declare the styles as classes and then apply those classes to data cells, rather than directly applying styles to cells. It is, however, probably still easier to use the Styler function api when you are not concerned about optimization.

This is sub-optimal:

```
df2.style.apply(
    highlight_max, props="color:white;background-color:darkblue;", axis=0
).apply(highlight_max, props="color:white;background-color:pink;", axis=1).apply(
    highlight_max, props="color:white;background-color:purple", axis=None
)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

This is better:

```
build = lambda x: pd.DataFrame(x, index=df2.index, columns=df2.columns)
cls1 = build(df2.apply(highlight_max, props="cls-1 ", axis=0))
cls2 = build(
    df2.apply(highlight_max, props="cls-2 ", axis=1, result_type="expand").values
)
cls3 = build(highlight_max(df2, props="cls-3 "))
df2.style.set_table_styles(
    [
        {"selector": ".cls-1", "props": "color:white;background-color:darkblue;"},
        {"selector": ".cls-2", "props": "color:white;background-color:pink;"},
        {"selector": ".cls-3", "props": "color:white;background-color:purple;"},
    ]
).set_td_classes(cls1 + cls2 + cls3)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | 0.640423 | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | 1.042513 | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

### 4. Don’t use tooltips[#](https://pandas.pydata.org#4.-Don't-use-tooltips)

Tooltips require `cell_ids` to work and they generate extra HTML elements for *every* data cell.

### 5. If every byte counts use string replacement[#](https://pandas.pydata.org#5.-If-every-byte-counts-use-string-replacement)

You can remove unnecessary HTML, or shorten the default class names by replacing the default css dict. You can read a little more about CSS [below](https://pandas.pydata.org#More-About-CSS-and-HTML).

```
my_css = {
    "row_heading": "",
    "col_heading": "",
    "index_name": "",
    "col": "c",
    "row": "r",
    "col_trim": "",
    "row_trim": "",
    "level": "l",
    "data": "",
    "blank": "",
}
html = Styler(df4, uuid_len=0, cell_ids=False)
html.set_table_styles(
    [
        {"selector": "td", "props": props},
        {"selector": ".c1", "props": "color:green;"},
        {"selector": ".l0", "props": "color:blue;"},
    ],
    css_class_names=my_css,
)
print(html.to_html())
```
```
<style type="text/css">
#T_ td {
  font-family: "Times New Roman", Times, serif;
  color: #e83e8c;
  font-size: 1.3em;
}
#T_ .c1 {
  color: green;
}
#T_ .l0 {
  color: blue;
}
</style>
<table id="T_">
  <thead>
    <tr>
      <th class=" l0" > </th>
      <th class=" l0 c0" >0</th>
      <th class=" l0 c1" >1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th class=" l0 r0" >0</th>
      <td class=" r0 c0" >1</td>
      <td class=" r0 c1" >2</td>
    </tr>
    <tr>
      <th class=" l0 r1" >1</th>
      <td class=" r1 c0" >3</td>
      <td class=" r1 c1" >4</td>
    </tr>
  </tbody>
</table>
```
```
html
```
|  | 0 | 1 | 
|---|---|---|
| 0 | 1 | 2 | 
| 1 | 3 | 4 | 

## Builtin Styles[#](https://pandas.pydata.org#Builtin-Styles)

Some styling functions are common enough that we’ve “built them in” to the `Styler`, so you don’t have to write them and apply them yourself. The current list of such functions is:

- [.highlight\_null](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.highlight_null.html): for use with identifying missing data.
- [.highlight\_min](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.highlight_min.html) and [.highlight\_max](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.highlight_max.html): for use with identifying extremities in data.
- [.highlight\_between](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.highlight_between.html) and [.highlight\_quantile](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html): for use with identifying classes within data.
- [.background\_gradient](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.background_gradient.html): a flexible method for highlighting cells based on their, or other, values on a numeric scale.
- [.text\_gradient](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.text_gradient.html): similar method for highlighting text based on their, or other, values on a numeric scale.
- [.bar](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.bar.html): to display mini-charts within cell backgrounds.

The individual documentation on each function often gives more examples of their arguments.

### Highlight Null[#](https://pandas.pydata.org#Highlight-Null)

```
df2.iloc[0, 2] = np.nan
df2.iloc[4, 3] = np.nan
df2.loc[:4].style.highlight_null(color="yellow")
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 

### Highlight Min or Max[#](https://pandas.pydata.org#Highlight-Min-or-Max)

```
df2.loc[:4].style.highlight_max(
    axis=1, props=("color:white; font-weight:bold; background-color:darkblue;")
)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 

### Highlight Between[#](https://pandas.pydata.org#Highlight-Between)

This method accepts ranges as float, or NumPy arrays or Series provided the indexes match.

```
left = pd.Series([1.0, 0.0, 1.0], index=["A", "B", "D"])
df2.loc[:4].style.highlight_between(
    left=left, right=1.5, axis=1, props="color:white; background-color:purple;"
)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 

### Highlight Quantile[#](https://pandas.pydata.org#Highlight-Quantile)

Useful for detecting the highest or lowest percentile values

```
df2.loc[:4].style.highlight_quantile(q_left=0.85, axis=None, color="yellow")
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 

### Background Gradient and Text Gradient[#](https://pandas.pydata.org#Background-Gradient-and-Text-Gradient)

You can create “heatmaps” with the `background_gradient` and `text_gradient` methods. These require matplotlib, and we’ll use [Seaborn](https://seaborn.pydata.org/) to get a nice colormap.

```
import seaborn as sns
cm = sns.light_palette("green", as_cmap=True)
df2.style.background_gradient(cmap=cm)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

```
df2.style.text_gradient(cmap=cm)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

[.background\_gradient](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.background_gradient.html) and [.text\_gradient](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.text_gradient.html) have a number of keyword arguments to customise the gradients and colors. See the documentation.

### Set properties[#](https://pandas.pydata.org#Set-properties)

Use `Styler.set_properties` when the style doesn’t actually depend on the values. This is just a simple wrapper for `.map` where the function returns the same properties for all cells.

```
df2.loc[:4].style.set_properties(
    **{"background-color": "black", "color": "lawngreen", "border-color": "white"}
)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 

### Bar charts[#](https://pandas.pydata.org#Bar-charts)

You can include “bar charts” in your DataFrame.

```
df2.style.bar(subset=["A", "B"], color="#d65f5f")
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.125730 | -0.132105 | nan | 0.104900 | 
| 1 | -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| 2 | -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| 3 | -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| 4 | -0.544259 | -0.316300 | 0.411631 | nan | 
| 5 | -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 6 | 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| 7 | -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| 8 | -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| 9 | -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

Additional keyword arguments give more control on centering and positioning, and you can pass a list of `[color_negative, color_positive]` to highlight lower and higher values or a matplotlib colormap.

To showcase an example here’s how you can change the above with the new `align` option, combined with setting `vmin` and `vmax` limits, the `width` of the figure, and underlying css `props` of cells, leaving space to display the text and the bars. We also use `text_gradient` to color the text the same as the bars using a matplotlib colormap (although in this case the visualization is probably better without this additional effect).

```
df2.style.format("{:.3f}", na_rep="").bar(
    align=0,
    vmin=-2.5,
    vmax=2.5,
    cmap="bwr",
    height=50,
    width=60,
    props="width: 120px; border-right: 1px solid black;",
).text_gradient(cmap="bwr", vmin=-2.5, vmax=2.5)
```
|  | A | B | C | D | 
|---|---|---|---|---|
| 0 | 0.126 | -0.132 |  | 0.105 | 
| 1 | -0.536 | 0.362 | 1.304 | 0.947 | 
| 2 | -0.704 | -1.265 | -0.623 | 0.041 | 
| 3 | -2.325 | -0.219 | -1.246 | -0.732 | 
| 4 | -0.544 | -0.316 | 0.412 |  | 
| 5 | -0.129 | 1.366 | -0.665 | 0.352 | 
| 6 | 0.903 | 0.094 | -0.743 | -0.922 | 
| 7 | -0.458 | 0.220 | -1.010 | -0.209 | 
| 8 | -0.159 | 0.541 | 0.215 | 0.355 | 
| 9 | -0.654 | -0.130 | 0.784 | 1.493 | 

The following example aims to give a highlight of the behavior of the new align options:

```
HTML(head)
```
| Align | All Negative | Both Neg and Pos | All Positive | Large Positive | 
|---|---|---|---|---|
| left |  |  |  |  | 
| right |  |  |  |  | 
| zero |  |  |  |  | 
| mid |  |  |  |  | 
| mean |  |  |  |  | 
| 99 |  |  |  |  | 

| -100 | 
| -60 | 
| -30 | 
| -20 | 

| -10 | 
| -5 | 
| 0 | 
| 90 | 

| 10 | 
| 20 | 
| 50 | 
| 100 | 

| 100 | 
| 103 | 
| 101 | 
| 102 | 

| -100 | 
| -60 | 
| -30 | 
| -20 | 

| -10 | 
| -5 | 
| 0 | 
| 90 | 

| 10 | 
| 20 | 
| 50 | 
| 100 | 

| 100 | 
| 103 | 
| 101 | 
| 102 | 

| -100 | 
| -60 | 
| -30 | 
| -20 | 

| -10 | 
| -5 | 
| 0 | 
| 90 | 

| 10 | 
| 20 | 
| 50 | 
| 100 | 

| 100 | 
| 103 | 
| 101 | 
| 102 | 

| -100 | 
| -60 | 
| -30 | 
| -20 | 

| -10 | 
| -5 | 
| 0 | 
| 90 | 

| 10 | 
| 20 | 
| 50 | 
| 100 | 

| 100 | 
| 103 | 
| 101 | 
| 102 | 

| -100 | 
| -60 | 
| -30 | 
| -20 | 

| -10 | 
| -5 | 
| 0 | 
| 90 | 

| 10 | 
| 20 | 
| 50 | 
| 100 | 

| 100 | 
| 103 | 
| 101 | 
| 102 | 

| -100 | 
| -60 | 
| -30 | 
| -20 | 

| -10 | 
| -5 | 
| 0 | 
| 90 | 

| 10 | 
| 20 | 
| 50 | 
| 100 | 

| 100 | 
| 103 | 
| 101 | 
| 102 | 

## Sharing styles[#](https://pandas.pydata.org#Sharing-styles)

Say you have a lovely style built up for a DataFrame, and now you want to apply the same style to a second DataFrame. Export the style with `df1.style.export`, and import it on the second DataFrame with `df1.style.set`

```
style1 = (
    df2.style.map(style_negative, props="color:red;")
    .map(lambda v: "opacity: 20%;" if (v < 0.3) and (v > -0.3) else None)
    .set_table_styles([{"selector": "th", "props": "color: blue;"}])
    .hide(axis="index")
)
style1
```
| A | B | C | D | 
|---|---|---|---|
| 0.125730 | -0.132105 | nan | 0.104900 | 
| -0.535669 | 0.361595 | 1.304000 | 0.947081 | 
| -0.703735 | -1.265421 | -0.623274 | 0.041326 | 
| -2.325031 | -0.218792 | -1.245911 | -0.732267 | 
| -0.544259 | -0.316300 | 0.411631 | nan | 
| -0.128535 | 1.366463 | -0.665195 | 0.351510 | 
| 0.903470 | 0.094012 | -0.743499 | -0.921725 | 
| -0.457726 | 0.220195 | -1.009618 | -0.209176 | 
| -0.159225 | 0.540846 | 0.214659 | 0.355373 | 
| -0.653829 | -0.129614 | 0.783975 | 1.493431 | 

```
style2 = df3.style
style2.use(style1.export())
style2
```
| c1 | c2 | c3 | c4 | 
|---|---|---|---|
| -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
| 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
| -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

Notice that you’re able to share the styles even though they’re data aware. The styles are re-evaluated on the new DataFrame they’ve been `use`d upon.

## Limitations[#](https://pandas.pydata.org#Limitations)

- DataFrame only (use `Series.to_frame().style`)
- The index and columns do not need to be unique, but certain styling functions can only work with unique indexes.
- No large repr, and construction performance isn’t great; although we have some [HTML optimizations](https://pandas.pydata.org#Optimization)
- You can only apply styles, you can’t insert new HTML entities, except via subclassing.

## Other Fun and Useful Stuff[#](https://pandas.pydata.org#Other-Fun-and-Useful-Stuff)

Here are a few interesting examples.

### Widgets[#](https://pandas.pydata.org#Widgets)

`Styler` interacts pretty well with widgets. If you’re viewing this online instead of running the notebook yourself, you’re missing out on interactively adjusting the color palette.

```
from ipywidgets import widgets
@widgets.interact
def f(h_neg=(0, 359, 1), h_pos=(0, 359), s=(0.0, 99.9), l_post=(0.0, 99.9)):
    return df2.style.background_gradient(
        cmap=sns.palettes.diverging_palette(
            h_neg=h_neg, h_pos=h_pos, s=s, l=l_post, as_cmap=True
        )
    )
```
### Magnify[#](https://pandas.pydata.org#Magnify)

```
def magnify():
    return [
        {"selector": "th", "props": [("font-size", "4pt")]},
        {"selector": "td", "props": [("padding", "0em 0em")]},
        {"selector": "th:hover", "props": [("font-size", "12pt")]},
        {
            "selector": "tr:hover td:hover",
            "props": [("max-width", "200px"), ("font-size", "12pt")],
        },
    ]
```
```
cmap = sns.diverging_palette(5, 250, as_cmap=True)
bigdf = pd.DataFrame(np.random.default_rng(25).standard_normal((20, 25))).cumsum()
bigdf.style.background_gradient(cmap, axis=1).set_properties(
    **{"max-width": "80px", "font-size": "1pt"}
).set_caption("Hover to magnify").format(precision=2).set_table_styles(magnify())
```
| Hover to magnify |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0.35 | -0.00 | -0.53 | -2.28 | 0.02 | 0.93 | 1.04 | -0.54 | 2.23 | 1.94 | -0.23 | -0.16 | 0.96 | -0.25 | 0.22 | 1.22 | 1.19 | -0.53 | -0.46 | -0.55 | -0.01 | 0.07 | -0.39 | 0.77 | 0.05 | 
| 1 | 0.37 | -1.97 | -1.92 | -2.97 | 0.38 | 0.06 | 2.60 | -0.39 | 2.49 | 2.06 | 0.26 | 0.77 | 0.41 | 1.31 | -0.55 | 1.74 | 0.98 | -0.70 | 0.21 | -0.35 | 1.59 | -0.43 | 0.13 | 1.36 | 2.16 | 
| 2 | 1.98 | -1.27 | -0.24 | -2.12 | -0.40 | 0.39 | 3.83 | -0.91 | 4.01 | 2.42 | -0.36 | 1.23 | -1.16 | 0.62 | -1.60 | 2.24 | -0.04 | -2.26 | 0.52 | -0.83 | 0.87 | -1.03 | 1.17 | 1.53 | 1.41 | 
| 3 | 4.78 | -0.78 | 1.67 | -1.07 | 0.96 | -0.48 | 3.26 | -0.27 | 3.93 | 2.50 | 0.72 | -1.07 | -1.49 | 2.16 | -2.07 | 2.28 | 0.34 | -1.94 | 0.83 | -1.76 | 1.20 | -1.63 | 2.75 | 0.90 | 1.67 | 
| 4 | 4.58 | 0.35 | 1.79 | -0.36 | 0.40 | -0.86 | 2.31 | -0.44 | 3.65 | 1.36 | -0.53 | -0.91 | -1.67 | 1.45 | -2.99 | 1.17 | 0.44 | -2.48 | 0.20 | -2.32 | 0.73 | -1.94 | 2.84 | -0.86 | 1.41 | 
| 5 | 3.38 | -0.02 | 3.04 | -2.28 | -0.89 | -1.38 | 0.01 | 1.95 | 3.01 | 2.98 | -0.62 | 0.27 | -0.86 | 1.15 | -2.49 | 0.51 | -0.04 | -0.99 | -0.67 | -3.24 | 3.28 | -2.33 | 3.14 | 0.78 | 0.92 | 
| 6 | 2.81 | 1.80 | 3.02 | -2.01 | -1.23 | -0.85 | -1.57 | 2.12 | 4.01 | 3.94 | -1.13 | 0.91 | 1.28 | 1.27 | -1.81 | 0.15 | -1.77 | -0.25 | -1.63 | -3.94 | 3.34 | -2.35 | 3.01 | 1.90 | 1.05 | 
| 7 | 2.85 | 0.72 | 3.92 | -3.29 | -3.49 | -1.67 | -0.87 | 2.46 | 5.28 | 4.34 | -0.76 | 1.24 | 0.64 | 0.81 | -2.27 | 0.34 | -2.71 | -0.67 | -1.35 | -4.01 | 3.06 | -2.55 | 1.78 | 0.54 | 0.25 | 
| 8 | 3.80 | 1.51 | 4.19 | -2.67 | -2.71 | -4.04 | -1.42 | 3.30 | 7.04 | 4.52 | 0.96 | 2.40 | 0.78 | -0.24 | -3.28 | 0.28 | -2.51 | -0.74 | -0.74 | -3.44 | 3.11 | -2.12 | 2.07 | -1.35 | -1.03 | 
| 9 | 4.11 | 2.27 | 4.29 | -2.97 | -2.50 | -3.58 | -1.25 | 1.32 | 7.36 | 5.25 | 1.08 | 4.60 | -0.64 | -2.05 | 0.09 | -0.72 | -4.96 | -1.31 | 0.09 | -4.16 | 2.68 | -1.37 | 4.02 | -0.59 | -0.72 | 
| 10 | 3.67 | 3.02 | 7.08 | -4.10 | -3.57 | -3.95 | -0.53 | 1.94 | 7.14 | 4.78 | 2.44 | 5.06 | 0.69 | -2.28 | 1.23 | -1.56 | -2.90 | -1.71 | -0.27 | -3.72 | 2.50 | -1.97 | 4.47 | -1.23 | 1.21 | 
| 11 | 2.98 | 3.85 | 6.33 | -5.84 | -5.90 | -3.91 | -1.94 | 2.08 | 6.33 | 4.70 | 2.41 | 6.84 | 0.50 | -3.68 | -1.10 | -0.67 | -2.80 | -0.28 | -1.88 | -3.91 | 1.67 | -1.48 | 4.15 | 0.17 | 0.79 | 
| 12 | 2.76 | 3.21 | 6.80 | -4.75 | -5.36 | -4.53 | -3.00 | 1.17 | 6.52 | 4.20 | 2.25 | 7.97 | 0.98 | -3.45 | -1.59 | -0.86 | -3.09 | -0.24 | -2.08 | -3.73 | 1.03 | -0.18 | 4.54 | 0.48 | 1.69 | 
| 13 | 1.69 | 2.02 | 5.31 | -5.51 | -4.79 | -4.34 | -1.42 | -0.24 | 6.96 | 2.92 | 0.97 | 6.70 | 2.18 | -3.38 | -0.33 | -0.77 | -2.39 | 0.42 | -1.53 | -3.59 | 1.98 | 0.01 | 4.61 | 0.52 | 1.11 | 
| 14 | 0.17 | 1.26 | 7.10 | -5.35 | -5.81 | -4.61 | -0.45 | 1.61 | 5.10 | 1.31 | -1.18 | 6.09 | 1.25 | -2.23 | 0.32 | -1.33 | -0.08 | -0.19 | -1.21 | -2.83 | 0.97 | 0.13 | 4.89 | 0.36 | 1.83 | 
| 15 | 0.01 | 0.61 | 7.94 | -5.85 | -5.35 | -5.10 | 0.14 | 1.76 | 3.89 | 1.72 | -1.61 | 7.86 | 0.71 | -1.38 | -1.95 | -1.84 | -1.88 | -0.14 | -2.02 | -1.45 | 1.68 | 1.62 | 3.97 | -1.88 | 1.80 | 
| 16 | 1.42 | 0.91 | 9.86 | -6.10 | -6.02 | -4.56 | 1.24 | 1.38 | 3.25 | 1.05 | 0.38 | 5.77 | 1.92 | -1.51 | -0.36 | -1.01 | -3.01 | 0.10 | -2.50 | -1.99 | 0.29 | 2.91 | 2.07 | -1.64 | 3.87 | 
| 17 | 1.94 | 2.55 | 10.78 | -4.77 | -6.87 | -4.38 | 1.74 | 1.63 | 2.34 | 0.06 | 0.41 | 6.21 | 2.20 | -3.13 | -0.88 | -1.57 | -2.59 | -0.76 | -2.38 | -3.21 | -0.11 | 3.62 | 2.91 | -2.87 | 3.98 | 
| 18 | 1.27 | 4.45 | 11.25 | -4.68 | -4.93 | -7.30 | 0.92 | 2.30 | 2.34 | 0.52 | -0.15 | 6.01 | 2.52 | -1.89 | 1.37 | -2.65 | -1.98 | -2.85 | -2.78 | -2.81 | -0.86 | 3.93 | 2.83 | -1.04 | 4.17 | 
| 19 | 0.72 | 2.89 | 10.94 | -3.85 | -2.50 | -7.04 | 0.77 | 2.27 | 2.83 | 1.63 | 0.94 | 6.26 | 3.07 | -1.99 | 2.65 | -4.04 | -0.91 | -2.69 | -2.70 | -2.49 | -0.86 | 3.16 | 2.88 | -0.85 | 4.54 | 

### Sticky Headers[#](https://pandas.pydata.org#Sticky-Headers)

If you display a large matrix or DataFrame in a notebook, but you want to always see the column and row headers you can use the [.set\_sticky](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.set_sticky.html) method which manipulates the table styles CSS.

```
bigdf = pd.DataFrame(np.random.default_rng().standard_normal((16, 100)))
bigdf.style.set_sticky(axis="index")
```
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | -1.249542 | 0.567548 | -1.909437 | 1.458344 | -0.197655 | 0.989967 | 1.393843 | -2.968313 | -0.968918 | -1.761310 | 1.004715 | 2.154103 | 1.694473 | -0.440707 | 1.686886 | 1.166068 | 0.579233 | 1.506640 | 0.718049 | -0.554386 | -1.185115 | 0.318499 | -0.402136 | -0.866084 | 0.116440 | -0.770831 | 0.040033 | -0.352075 | -0.739156 | 0.538159 | -0.844084 | -0.725811 | -0.798409 | 1.365312 | -0.812031 | 0.008799 | -0.703116 | -0.015020 | -0.557571 | 0.567813 | -0.519146 | 1.200826 | -0.441853 | -0.989711 | 0.261050 | 0.404365 | 0.151773 | -1.454652 | 1.290298 | 1.057414 | -0.333858 | -1.209276 | -0.824068 | 0.524764 | -1.078480 | -1.443013 | -0.797468 | -1.196842 | 0.186133 | -0.915151 | -0.688486 | -0.993827 | 0.114382 | -1.422103 | -1.736256 | 0.220262 | 0.526817 | -1.960811 | 0.961365 | -0.394427 | -1.595684 | -0.536234 | 0.347678 | -0.402072 | 1.799940 | 0.877252 | 0.611150 | 0.978408 | -0.289397 | -0.670142 | -0.436286 | 0.572855 | 0.930773 | 0.905516 | -0.553170 | -1.499645 | 1.300117 | 1.801568 | 0.388096 | 0.212038 | -0.719029 | -1.166183 | 2.505967 | 0.796141 | -2.803961 | -0.962644 | 0.321278 | 0.132450 | -1.412649 | -1.113265 | 
| 1 | -1.386477 | 0.343699 | -1.777764 | -2.030883 | -2.039394 | -0.128416 | 1.553098 | 0.252039 | -1.177918 | 1.050435 | -1.286146 | -1.545711 | 0.165126 | -0.805035 | -0.185919 | 0.240780 | -0.774301 | 0.151167 | -0.090344 | -0.382306 | -1.175794 | 0.670109 | -1.115134 | -1.687216 | -2.087633 | -1.033784 | 1.206429 | -0.075021 | -0.207420 | -1.623272 | -2.000145 | 0.556966 | 0.565009 | -0.096283 | -1.860224 | 1.743555 | 0.019123 | -0.770004 | 0.883886 | -0.130834 | -0.967490 | -0.924367 | 1.471164 | -0.233796 | -2.109890 | 0.380962 | 1.050677 | -0.674036 | -0.188536 | 0.273588 | 0.522984 | 0.940079 | -1.239884 | 0.064871 | 0.196937 | 1.052862 | 1.158287 | -1.292776 | 0.401833 | 0.025043 | -0.205262 | -0.153565 | 0.685339 | -1.020628 | -0.178922 | 1.499049 | 0.065570 | -0.990070 | -0.306153 | -0.446412 | -0.572315 | -0.415098 | -0.004955 | -1.098927 | -0.729612 | 1.209824 | -1.184541 | 1.991115 | -1.334682 | 0.631567 | 0.698615 | -1.284625 | 0.062116 | -1.102275 | 1.842233 | 0.103789 | 0.277604 | -0.862671 | 1.267912 | 0.679236 | 1.051641 | -0.689062 | -1.098211 | -0.481141 | 0.785287 | 0.550755 | -0.193038 | 1.206172 | -0.198587 | -1.301408 | 
| 2 | 0.797726 | 0.332493 | 0.156359 | 0.541164 | -0.130185 | 0.519269 | -0.094363 | -0.717014 | -1.915807 | -0.068074 | 1.913234 | -1.744420 | -0.709762 | -0.019352 | 0.353815 | -0.279344 | -0.804538 | 1.261841 | -0.462474 | -0.668915 | 1.738801 | 1.231813 | 0.948650 | -0.063552 | -0.748174 | 0.188053 | 0.819249 | 0.269694 | 1.328088 | 0.843363 | -0.281611 | 1.198336 | 0.238340 | -1.275175 | 0.360701 | 0.487321 | -1.494900 | -0.178627 | -0.633445 | 0.619047 | 0.105146 | -1.935095 | -0.781640 | -0.553514 | -0.304370 | 0.405786 | -0.246216 | -0.028615 | 0.182151 | 1.121132 | -1.185987 | 0.045238 | 0.851223 | 0.609628 | -0.346280 | -1.641365 | -2.645157 | 0.220398 | -1.195801 | -0.582228 | 0.960550 | 0.271946 | -0.747949 | 0.676832 | 0.268733 | -1.007901 | -0.785411 | -0.588994 | 0.471147 | 0.191162 | 1.343307 | -0.148078 | -0.769660 | -0.111852 | 0.101180 | -0.410467 | -0.151339 | 0.015735 | -0.233816 | 0.123209 | -0.732491 | -0.568736 | -0.871965 | 0.979355 | -1.690540 | -0.023238 | -0.722154 | -0.131529 | 0.776237 | 1.340735 | 0.304377 | -0.050628 | -1.792796 | -1.173447 | 2.119066 | 0.628281 | -1.069870 | 0.303223 | -0.081146 | -0.071162 | 
| 3 | -0.731988 | 0.362592 | 0.356363 | 1.351990 | -2.493069 | 2.302545 | 0.959011 | 0.412911 | -1.184261 | 1.584461 | -0.541656 | -1.504424 | -0.545613 | -2.024992 | -0.872900 | -2.273011 | 1.314306 | -0.026611 | -1.396559 | 0.275738 | 0.486888 | -0.679761 | -0.788042 | -0.341907 | -0.886905 | 0.876181 | 1.961002 | 0.056490 | 0.730247 | 0.867651 | 0.510434 | 1.621525 | -0.642243 | -0.579611 | -1.269745 | 1.537741 | 0.258812 | 1.896280 | 0.411411 | 0.023065 | -0.490354 | 0.134000 | 0.638802 | -0.845080 | 0.878381 | 1.812716 | 0.848001 | -0.912596 | 0.958782 | 1.204671 | 0.889057 | -0.481549 | -0.809575 | 3.113664 | 2.790555 | 0.790664 | -0.386375 | -0.958566 | 1.293568 | -0.242375 | -1.654247 | -0.517165 | -0.046716 | -2.017556 | 0.775479 | 0.290433 | -0.354921 | -0.551662 | 0.858737 | -0.720153 | 2.740839 | -1.242803 | -0.699635 | -1.118300 | -1.025630 | -0.584491 | -0.403746 | -0.148979 | 0.681991 | 0.617719 | 0.592520 | -0.376256 | -1.209913 | -0.973329 | -0.209426 | 0.623346 | -1.536506 | 0.573466 | -0.942691 | -0.439838 | -2.229326 | 1.180379 | 0.201228 | -1.045893 | 0.747619 | 1.161727 | 1.359439 | -0.056496 | -0.346755 | -0.686260 | 
| 4 | 0.797414 | 1.041336 | 0.200795 | 0.018358 | 0.795113 | -0.386274 | 0.427011 | -0.160934 | -1.966054 | -0.952876 | -1.138180 | -0.635081 | 1.523410 | -0.856518 | 0.684642 | -1.081286 | 0.228999 | -0.890409 | 0.500534 | -0.912965 | -0.658863 | 0.711759 | 0.476150 | 0.973722 | -1.576857 | -0.640923 | -0.398626 | 0.141123 | 0.156522 | -0.066611 | -1.749565 | -0.518997 | -0.439959 | 0.322202 | -1.054731 | 1.581706 | 0.112304 | 2.048272 | -0.543601 | -1.147761 | 0.545976 | 0.266249 | 0.470301 | -0.687722 | -0.632856 | -0.683362 | -1.291750 | 0.565963 | 0.399943 | 0.905395 | -0.192770 | 0.807798 | -0.387576 | -0.216277 | -0.046453 | 1.935200 | 1.183481 | 0.405696 | 1.873436 | 1.961536 | 1.008626 | 0.671273 | -2.855887 | 0.741276 | 0.074018 | 1.129584 | -0.886903 | -0.340590 | 0.215483 | 0.446204 | 0.439725 | 1.957116 | -0.445490 | 0.947790 | 0.635031 | 0.225685 | 1.523159 | 0.813343 | -0.060784 | -1.607853 | -0.352196 | -1.515608 | 0.044250 | -0.566870 | 0.565938 | 2.362594 | -1.048067 | 0.636425 | 1.208411 | -1.126668 | 1.103816 | -0.682065 | 0.293105 | 0.007222 | -1.748249 | -0.097906 | -1.006603 | 1.238084 | 0.032449 | -0.916133 | 
| 5 | 0.638091 | -1.263351 | -1.026522 | 0.213395 | 0.605262 | 0.668249 | -0.149394 | -1.339944 | 0.698683 | 1.199415 | -0.263830 | -0.051851 | -0.791915 | -0.044925 | 1.659059 | 1.492263 | 1.750472 | -1.727650 | 0.242873 | 1.231380 | 0.060159 | 1.386421 | -0.998404 | -0.008600 | 0.463815 | 0.212580 | 0.548790 | -0.836541 | -1.772024 | 2.637310 | -0.646087 | 0.014787 | -0.818144 | -0.661508 | 1.127787 | 0.407368 | 1.064530 | -0.271909 | 0.422858 | 0.573724 | -0.871016 | 0.174475 | -0.601939 | 1.320925 | 0.359677 | 0.692463 | -0.707375 | -0.105360 | -0.428715 | 1.272814 | -1.154052 | -0.758770 | -0.523536 | -0.750004 | -0.151967 | -0.936328 | -0.485521 | 1.630334 | 0.065307 | 1.263922 | 0.393902 | 0.800497 | -1.200119 | 0.921761 | 2.294416 | -0.322866 | 0.385961 | -1.698391 | 0.529921 | 0.538005 | -0.826206 | -0.966698 | 0.777591 | 1.603942 | 0.572657 | 0.882799 | 0.173200 | -0.004198 | -0.638427 | 1.958323 | -0.323694 | 1.894872 | -1.607778 | 0.603142 | 0.677462 | 0.462840 | 1.312929 | -0.029531 | -0.355775 | -1.424371 | 0.201973 | 0.078968 | 0.530699 | -0.351735 | -1.753653 | 1.437835 | -2.017140 | -1.894215 | 0.582887 | -1.908740 | 
| 6 | 0.615421 | -0.556665 | -0.828299 | 0.438880 | 1.320985 | 0.520077 | 0.254125 | -0.229425 | 1.235457 | 1.276169 | 0.558587 | 0.782341 | -0.732503 | -1.210421 | -0.034196 | 1.034804 | -0.122429 | -0.000241 | -1.530904 | -1.449231 | -0.009184 | 1.825607 | 1.285270 | 0.489378 | -2.364886 | -1.799813 | 1.830970 | -2.082466 | 0.383160 | -1.144195 | 0.082588 | 1.211101 | 0.390994 | -0.040749 | 0.808947 | 1.311611 | 0.453154 | 0.569982 | 0.646023 | -0.069526 | -1.006879 | -0.874861 | 2.546722 | 0.416755 | -0.140203 | -1.523114 | -3.374827 | -1.655652 | -0.424794 | 0.378496 | 1.908024 | 0.319300 | -1.535855 | -0.103569 | -0.000077 | -0.926792 | -1.578229 | -0.424063 | -0.805444 | 0.436176 | -1.217475 | -0.354085 | -0.315280 | -0.556084 | 0.468431 | 0.762999 | -0.581309 | -0.338872 | -1.891932 | 0.575485 | -0.993463 | -2.882135 | 0.893977 | 0.441540 | -0.245048 | -0.011467 | 1.743730 | -1.384662 | 1.036140 | -0.105277 | -0.846649 | -1.171898 | 1.043947 | -0.034855 | -0.023222 | 0.496117 | -0.813425 | 0.372879 | 1.117880 | 0.950857 | -1.947647 | 1.068407 | 0.153447 | 0.609296 | 0.106221 | 0.565740 | 0.779673 | -0.250506 | -0.255725 | -1.076758 | 
| 7 | 0.677673 | -0.983991 | -0.508196 | -0.223275 | -0.892658 | 0.049644 | 0.199172 | -1.285564 | 0.522279 | 0.556498 | 1.534189 | -0.589428 | 0.225771 | -0.413116 | 0.056281 | -0.687684 | -0.748417 | -1.063367 | -1.061866 | -0.621624 | -0.347029 | 0.418753 | -1.106199 | -0.011235 | -0.203031 | -0.749104 | 0.757819 | -1.678048 | 0.831730 | 0.317106 | -0.713187 | -1.296103 | 1.178605 | -1.766184 | 0.405308 | -0.282047 | -0.700566 | -0.216445 | 1.412939 | 1.277242 | -1.008928 | 0.814763 | 0.288451 | -0.541380 | -0.557220 | -0.211266 | 1.400355 | -0.302584 | -0.972397 | 0.473262 | -1.233860 | -1.398580 | -0.345065 | -0.230340 | -0.688938 | 0.486462 | 0.445978 | -0.131654 | -0.032604 | 1.096168 | -1.165757 | -0.755705 | 1.113990 | 0.252089 | -0.179101 | 1.889106 | 1.257870 | 0.043826 | 0.001889 | -1.019826 | -0.576884 | -1.086858 | 0.363399 | -0.138195 | -1.576783 | 0.621132 | -0.213443 | 1.236186 | -0.219811 | -1.990014 | 0.039207 | -0.549818 | 0.275171 | -0.200415 | 1.065812 | 1.472389 | 1.891503 | -1.376733 | 0.128155 | -0.478999 | -0.679482 | 0.369820 | -0.084990 | -0.741410 | -1.356090 | -0.992864 | -1.587088 | -0.081792 | -0.661331 | 0.857166 | 
| 8 | 0.103721 | -1.750882 | 0.454741 | 0.880516 | 0.022227 | 0.031036 | -1.479162 | 0.574677 | -1.171226 | -0.964487 | 0.042584 | 2.674862 | -0.829213 | 2.284442 | 0.529467 | -0.033147 | -1.372299 | -0.056735 | -0.483158 | 1.633496 | 0.407124 | -0.361379 | 0.876548 | -0.347282 | -0.193713 | -0.900805 | 0.851192 | 1.411834 | 0.549841 | 0.109058 | -0.723613 | -0.792426 | 1.250363 | -0.807820 | 0.069971 | -0.303110 | 0.207053 | 0.257658 | -1.898140 | -0.102084 | 0.111499 | 0.488816 | -1.412533 | -0.399015 | -0.044270 | -1.160856 | 1.110853 | 0.424903 | 0.094994 | 0.876240 | 0.371636 | 0.514959 | 0.716920 | -0.861331 | 0.410777 | -1.166119 | -0.425079 | 0.000568 | -0.556060 | 0.630109 | 0.265495 | 2.302520 | 0.488671 | 1.750115 | -1.168802 | -0.843555 | -1.356735 | -0.944888 | -0.805620 | 0.384120 | 1.782541 | -0.436819 | -0.987764 | -0.052830 | -0.778743 | -0.436386 | -0.979797 | 0.646287 | -0.247060 | 0.808295 | 0.357228 | 0.202857 | -0.413732 | 0.696503 | -1.814141 | -0.454738 | 1.032526 | 0.006814 | -1.198463 | 1.926113 | 0.463695 | -1.061729 | 0.940131 | 0.440455 | 0.834434 | -0.239375 | -1.193795 | 0.289589 | -1.919376 | 0.300618 | 
| 9 | 1.167028 | 0.801218 | -0.753100 | -1.444753 | 0.227993 | -1.038193 | 1.025010 | -0.579519 | 0.132131 | 1.254681 | 0.643115 | 0.769858 | 0.223719 | -1.016941 | 0.058445 | -0.974466 | -1.654139 | -1.303969 | 0.783598 | 1.121699 | 0.959242 | -0.975369 | 0.504326 | 1.044171 | 1.008731 | -2.296769 | 1.259882 | -0.251946 | 0.783393 | -1.309242 | -0.046419 | 0.193768 | -1.077143 | -1.652423 | -0.246300 | 1.272914 | -1.155368 | 0.019024 | -0.349040 | -0.851228 | -1.927419 | 0.614689 | 0.219010 | -2.101607 | -1.312230 | -0.037534 | -1.262569 | 2.046184 | 0.479554 | -0.253348 | -0.675235 | 1.976276 | -0.530426 | -0.660220 | 0.571842 | -0.045128 | -0.447864 | 1.502488 | -2.248540 | 0.461898 | -0.378596 | -0.052101 | 0.789870 | 0.109803 | 0.243981 | 1.643840 | -1.047127 | -0.838163 | 0.190855 | -1.005314 | 0.296393 | 1.147729 | -1.830598 | -0.816001 | 0.377070 | -0.575019 | -1.097977 | 0.410986 | 1.192989 | 1.102330 | 0.596597 | -0.453403 | -1.282656 | 2.132497 | 1.801097 | -1.326927 | -0.042096 | -1.214378 | -0.203234 | -0.321269 | -0.284141 | -0.134051 | -0.565122 | -0.835913 | 0.784693 | -0.070871 | -0.136708 | 0.893560 | -0.070201 | -1.093890 | 
| 10 | -2.072411 | -0.385812 | -0.535624 | 1.146529 | -1.328274 | -1.466910 | -0.343952 | 0.635520 | 1.916967 | -0.445547 | 0.513106 | 0.122684 | -2.012649 | 2.213130 | -0.876255 | -0.337970 | -0.691478 | -0.565034 | 1.128058 | -1.146403 | -1.343220 | -0.089720 | -1.842053 | -1.065449 | -1.937323 | 0.370771 | 0.498412 | -0.201642 | 0.325548 | 0.375321 | -0.422994 | -0.311858 | -0.270497 | -0.513538 | 0.209063 | -1.363838 | -0.452896 | 0.603445 | 1.180090 | -0.081360 | -0.731317 | 2.014934 | -0.332546 | 0.768859 | 1.202408 | 0.268089 | -0.334788 | -0.793848 | -0.022587 | -0.171461 | 1.900468 | -1.967115 | -1.293951 | 0.782726 | 0.145005 | -0.409100 | -0.813320 | -0.175022 | -0.171934 | -0.117674 | -0.259813 | -0.564975 | -0.037270 | -0.689533 | 1.427015 | 0.981466 | 0.572991 | 0.137788 | 0.026421 | 0.196064 | 1.208259 | 1.415522 | -0.892827 | -1.014016 | 0.166945 | -2.723871 | -0.750593 | 0.537742 | -0.040917 | 0.216384 | 1.206401 | 0.464926 | -0.730086 | 2.395573 | -0.459004 | 1.233121 | 0.198533 | 0.576266 | 1.031852 | 0.731763 | -0.019858 | 1.694699 | 0.021719 | -1.811736 | 0.047970 | 0.739044 | -1.452084 | -0.209275 | -1.642848 | 0.429650 | 
| 11 | 1.118249 | -0.174247 | 1.124966 | -0.721937 | -0.265553 | -0.520646 | -1.361829 | 0.565736 | -1.618938 | 0.308877 | -1.667273 | 1.161356 | 0.700031 | 0.967877 | 2.235055 | -0.537956 | 1.252550 | -0.643366 | -1.423460 | -0.271388 | -0.108833 | 1.615209 | 0.290848 | 1.290791 | -0.137172 | 1.127603 | 0.327152 | -0.988139 | 0.447378 | 0.616595 | 0.146788 | -0.389949 | 0.259622 | 0.419123 | 0.850294 | 1.519774 | -0.813029 | 1.292770 | -1.096248 | 0.520481 | -0.707953 | 1.064422 | -0.709130 | -2.010674 | -0.025539 | 1.983015 | -0.290004 | -0.888709 | 0.228862 | -0.329893 | 0.319327 | 0.025947 | -0.998704 | 1.277585 | 1.613820 | 0.524826 | -2.374740 | 3.569202 | -0.102998 | 0.634771 | -0.341868 | -0.578210 | -0.356209 | -1.042418 | 0.096909 | 0.186491 | -1.441296 | -0.434589 | 1.058764 | 1.039132 | -1.731982 | -0.093453 | -0.501065 | 2.070266 | 0.071090 | 0.216531 | -0.724696 | 1.936130 | 0.919238 | 1.222116 | 0.217523 | -0.489636 | -0.233529 | -0.014936 | 1.830587 | -1.292743 | 1.290005 | -0.817594 | -1.988278 | -2.197472 | -0.204582 | -1.251410 | 0.292923 | -0.075040 | -0.039473 | -0.453339 | 1.277491 | -0.452404 | 0.643447 | 0.142819 | 
| 12 | -0.351171 | 1.023940 | -1.511498 | 0.618944 | 0.179706 | -1.228064 | 0.649514 | -0.052935 | 0.546807 | -1.203840 | -0.131340 | -0.092921 | -0.909330 | -0.137975 | 1.637062 | -1.295018 | -0.264532 | 1.136117 | -0.716100 | -1.183280 | -0.471934 | 0.143074 | -0.014638 | 0.961549 | -0.321732 | -0.933943 | -0.841826 | -1.296579 | -0.442408 | 1.282533 | -1.601770 | -1.345018 | -0.662283 | 0.220842 | 0.388788 | 0.632474 | -1.347650 | 1.594317 | -0.617301 | -2.331357 | -2.511449 | -1.364538 | -0.799043 | -0.925109 | 0.632510 | -0.351499 | -2.661751 | -0.349751 | 0.773978 | 1.368351 | -0.268107 | -1.427781 | 0.685167 | -0.682513 | 0.276713 | -1.945579 | 0.645838 | -1.447977 | -0.628495 | -0.807960 | 0.011758 | -0.330518 | 0.419784 | 0.958082 | 1.586090 | 0.439872 | 1.340896 | 0.482043 | -0.006991 | -1.687864 | -1.017623 | -0.877199 | 0.740574 | -1.760090 | 0.659850 | -1.057235 | 0.536957 | 0.541132 | 3.194705 | 0.842192 | -0.282684 | -0.700363 | -0.395353 | -0.648448 | 1.684356 | -0.605384 | -0.729134 | 1.618759 | -0.086524 | 1.454520 | -0.045343 | -0.213119 | 0.320458 | 0.393286 | 0.263270 | -1.188044 | 0.045544 | -0.096079 | 1.379419 | 0.619566 | 
| 13 | -2.697761 | -0.216438 | 0.193286 | 1.100150 | -0.310430 | 0.019088 | -0.584535 | 0.719542 | -0.408461 | -0.647319 | -0.123209 | 0.002073 | -0.062305 | 1.309970 | 1.387754 | 1.288008 | 1.811905 | -1.065786 | -0.129579 | -0.024781 | -0.045186 | 0.854322 | 0.632747 | 0.582554 | -0.528291 | -0.509413 | -0.513704 | -3.074055 | -0.347337 | -0.049953 | -0.689384 | 0.237674 | 0.709307 | -0.181012 | 0.705539 | -0.471619 | -0.993367 | 1.037987 | -1.325141 | 0.545704 | 1.465180 | -0.987134 | 1.293419 | 1.133797 | -0.118827 | -2.039961 | -0.628638 | 0.551746 | -0.863957 | 0.954502 | -1.415083 | 0.253340 | 0.132188 | -0.892947 | -0.068687 | -0.311260 | -0.218912 | -1.371360 | 0.194940 | -2.114055 | 0.549188 | 1.226060 | 0.396822 | 0.427769 | -2.101510 | -0.332989 | -0.636885 | 0.364170 | -0.295028 | -2.414402 | -0.710915 | 0.951053 | 0.627281 | -1.456425 | -0.574606 | 0.341497 | 0.211243 | -1.100198 | 0.139133 | -1.922422 | -1.677048 | -0.109762 | 0.588005 | 1.388541 | -1.574352 | 3.018430 | 0.272214 | 0.119566 | 0.274605 | -1.003207 | 0.375928 | 0.520244 | -0.608685 | -0.891610 | 0.366384 | -1.100234 | 0.747745 | -0.301267 | -0.525439 | -0.418862 | 
| 14 | -0.122055 | 2.385162 | -0.889962 | -2.126945 | -0.868092 | 0.924390 | -0.072401 | 0.511622 | -1.186318 | 0.412805 | 0.049856 | 0.175842 | 0.021513 | -1.390033 | -0.715350 | 1.008352 | -0.405259 | -0.620009 | 0.935516 | 1.076372 | -0.951242 | -1.028077 | 1.287850 | 0.990782 | -0.928193 | -1.701400 | 0.933439 | -1.095484 | 0.703306 | 0.119863 | 0.680616 | -0.552189 | -1.773081 | -1.745979 | 1.016690 | -0.997333 | 0.347358 | -1.073921 | -1.250854 | -0.057358 | -1.987934 | 1.072044 | -0.396370 | -0.137720 | 1.255489 | 1.385366 | -0.662146 | -0.172926 | -0.114310 | 0.181880 | 2.509978 | -0.670348 | 0.046463 | -0.727387 | 0.650764 | -0.199858 | -1.275904 | -2.227526 | -0.346872 | 0.159554 | 1.228139 | -0.324135 | -0.185899 | 1.391892 | -0.303876 | 0.077019 | -0.221683 | 0.043599 | -0.229868 | -1.641672 | -0.246286 | 0.481877 | 0.318264 | -1.241771 | -0.513658 | 0.505226 | 0.137411 | 1.744722 | 0.284010 | -0.292033 | 1.186801 | -0.005072 | 2.514258 | -0.798792 | -1.713557 | -0.552754 | -0.160860 | -0.758267 | -0.579887 | 0.238086 | 0.457199 | 0.693525 | -0.461557 | -0.331175 | 0.895554 | 1.286008 | -1.996121 | 1.152437 | 0.604731 | 1.644384 | 
| 15 | 0.221145 | -1.173363 | 0.639189 | 0.952842 | 1.027615 | 1.095652 | -1.755546 | 1.805602 | 0.441859 | -0.348648 | -0.792012 | 0.973091 | 0.812662 | 0.402470 | -1.116643 | -0.749974 | 0.334878 | 0.038702 | 0.485698 | 0.356709 | 0.002965 | 0.233249 | -0.230521 | -3.210940 | 0.452658 | -1.311130 | 1.589915 | 1.743064 | 1.739856 | -0.464779 | -0.425398 | 2.501711 | -0.353845 | 0.071148 | 0.029837 | 0.273868 | 0.557694 | 0.035491 | -0.328312 | 1.093099 | -0.555101 | 0.416110 | 0.399903 | 0.660542 | 0.803015 | -0.318798 | 0.022345 | 0.157851 | 0.504515 | 0.428456 | -1.873753 | 0.622458 | -0.707877 | 0.380368 | -1.132078 | 1.936629 | 0.784655 | 0.886954 | -0.701823 | 0.259614 | 2.232133 | 0.232930 | -1.149868 | -0.751935 | 0.473409 | -0.604753 | -1.199894 | 0.300114 | 0.714157 | 0.665725 | 1.743132 | 0.497531 | 0.623560 | -1.022099 | 0.456591 | -1.664579 | 0.397944 | -0.962254 | -0.254085 | 0.809131 | 1.155931 | -2.477604 | 0.057874 | 0.888901 | 1.501404 | 1.272566 | 0.457429 | 1.241974 | -0.719311 | -1.331647 | 0.536821 | -0.782027 | 1.286608 | 0.859641 | -0.336375 | -0.313944 | -0.676993 | 0.130637 | 1.424001 | -0.292073 | 

It is also possible to stick MultiIndexes and even only specific levels.

```
bigdf.index = pd.MultiIndex.from_product([["A", "B"], [0, 1], [0, 1, 2, 3]])
bigdf.style.set_sticky(axis="index", pixel_size=18, levels=[1, 2])
```
|  |  |  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 0 | 0 | -1.249542 | 0.567548 | -1.909437 | 1.458344 | -0.197655 | 0.989967 | 1.393843 | -2.968313 | -0.968918 | -1.761310 | 1.004715 | 2.154103 | 1.694473 | -0.440707 | 1.686886 | 1.166068 | 0.579233 | 1.506640 | 0.718049 | -0.554386 | -1.185115 | 0.318499 | -0.402136 | -0.866084 | 0.116440 | -0.770831 | 0.040033 | -0.352075 | -0.739156 | 0.538159 | -0.844084 | -0.725811 | -0.798409 | 1.365312 | -0.812031 | 0.008799 | -0.703116 | -0.015020 | -0.557571 | 0.567813 | -0.519146 | 1.200826 | -0.441853 | -0.989711 | 0.261050 | 0.404365 | 0.151773 | -1.454652 | 1.290298 | 1.057414 | -0.333858 | -1.209276 | -0.824068 | 0.524764 | -1.078480 | -1.443013 | -0.797468 | -1.196842 | 0.186133 | -0.915151 | -0.688486 | -0.993827 | 0.114382 | -1.422103 | -1.736256 | 0.220262 | 0.526817 | -1.960811 | 0.961365 | -0.394427 | -1.595684 | -0.536234 | 0.347678 | -0.402072 | 1.799940 | 0.877252 | 0.611150 | 0.978408 | -0.289397 | -0.670142 | -0.436286 | 0.572855 | 0.930773 | 0.905516 | -0.553170 | -1.499645 | 1.300117 | 1.801568 | 0.388096 | 0.212038 | -0.719029 | -1.166183 | 2.505967 | 0.796141 | -2.803961 | -0.962644 | 0.321278 | 0.132450 | -1.412649 | -1.113265 | 
|  |  | 1 | -1.386477 | 0.343699 | -1.777764 | -2.030883 | -2.039394 | -0.128416 | 1.553098 | 0.252039 | -1.177918 | 1.050435 | -1.286146 | -1.545711 | 0.165126 | -0.805035 | -0.185919 | 0.240780 | -0.774301 | 0.151167 | -0.090344 | -0.382306 | -1.175794 | 0.670109 | -1.115134 | -1.687216 | -2.087633 | -1.033784 | 1.206429 | -0.075021 | -0.207420 | -1.623272 | -2.000145 | 0.556966 | 0.565009 | -0.096283 | -1.860224 | 1.743555 | 0.019123 | -0.770004 | 0.883886 | -0.130834 | -0.967490 | -0.924367 | 1.471164 | -0.233796 | -2.109890 | 0.380962 | 1.050677 | -0.674036 | -0.188536 | 0.273588 | 0.522984 | 0.940079 | -1.239884 | 0.064871 | 0.196937 | 1.052862 | 1.158287 | -1.292776 | 0.401833 | 0.025043 | -0.205262 | -0.153565 | 0.685339 | -1.020628 | -0.178922 | 1.499049 | 0.065570 | -0.990070 | -0.306153 | -0.446412 | -0.572315 | -0.415098 | -0.004955 | -1.098927 | -0.729612 | 1.209824 | -1.184541 | 1.991115 | -1.334682 | 0.631567 | 0.698615 | -1.284625 | 0.062116 | -1.102275 | 1.842233 | 0.103789 | 0.277604 | -0.862671 | 1.267912 | 0.679236 | 1.051641 | -0.689062 | -1.098211 | -0.481141 | 0.785287 | 0.550755 | -0.193038 | 1.206172 | -0.198587 | -1.301408 | 
|  |  | 2 | 0.797726 | 0.332493 | 0.156359 | 0.541164 | -0.130185 | 0.519269 | -0.094363 | -0.717014 | -1.915807 | -0.068074 | 1.913234 | -1.744420 | -0.709762 | -0.019352 | 0.353815 | -0.279344 | -0.804538 | 1.261841 | -0.462474 | -0.668915 | 1.738801 | 1.231813 | 0.948650 | -0.063552 | -0.748174 | 0.188053 | 0.819249 | 0.269694 | 1.328088 | 0.843363 | -0.281611 | 1.198336 | 0.238340 | -1.275175 | 0.360701 | 0.487321 | -1.494900 | -0.178627 | -0.633445 | 0.619047 | 0.105146 | -1.935095 | -0.781640 | -0.553514 | -0.304370 | 0.405786 | -0.246216 | -0.028615 | 0.182151 | 1.121132 | -1.185987 | 0.045238 | 0.851223 | 0.609628 | -0.346280 | -1.641365 | -2.645157 | 0.220398 | -1.195801 | -0.582228 | 0.960550 | 0.271946 | -0.747949 | 0.676832 | 0.268733 | -1.007901 | -0.785411 | -0.588994 | 0.471147 | 0.191162 | 1.343307 | -0.148078 | -0.769660 | -0.111852 | 0.101180 | -0.410467 | -0.151339 | 0.015735 | -0.233816 | 0.123209 | -0.732491 | -0.568736 | -0.871965 | 0.979355 | -1.690540 | -0.023238 | -0.722154 | -0.131529 | 0.776237 | 1.340735 | 0.304377 | -0.050628 | -1.792796 | -1.173447 | 2.119066 | 0.628281 | -1.069870 | 0.303223 | -0.081146 | -0.071162 | 
|  |  | 3 | -0.731988 | 0.362592 | 0.356363 | 1.351990 | -2.493069 | 2.302545 | 0.959011 | 0.412911 | -1.184261 | 1.584461 | -0.541656 | -1.504424 | -0.545613 | -2.024992 | -0.872900 | -2.273011 | 1.314306 | -0.026611 | -1.396559 | 0.275738 | 0.486888 | -0.679761 | -0.788042 | -0.341907 | -0.886905 | 0.876181 | 1.961002 | 0.056490 | 0.730247 | 0.867651 | 0.510434 | 1.621525 | -0.642243 | -0.579611 | -1.269745 | 1.537741 | 0.258812 | 1.896280 | 0.411411 | 0.023065 | -0.490354 | 0.134000 | 0.638802 | -0.845080 | 0.878381 | 1.812716 | 0.848001 | -0.912596 | 0.958782 | 1.204671 | 0.889057 | -0.481549 | -0.809575 | 3.113664 | 2.790555 | 0.790664 | -0.386375 | -0.958566 | 1.293568 | -0.242375 | -1.654247 | -0.517165 | -0.046716 | -2.017556 | 0.775479 | 0.290433 | -0.354921 | -0.551662 | 0.858737 | -0.720153 | 2.740839 | -1.242803 | -0.699635 | -1.118300 | -1.025630 | -0.584491 | -0.403746 | -0.148979 | 0.681991 | 0.617719 | 0.592520 | -0.376256 | -1.209913 | -0.973329 | -0.209426 | 0.623346 | -1.536506 | 0.573466 | -0.942691 | -0.439838 | -2.229326 | 1.180379 | 0.201228 | -1.045893 | 0.747619 | 1.161727 | 1.359439 | -0.056496 | -0.346755 | -0.686260 | 
|  | 1 | 0 | 0.797414 | 1.041336 | 0.200795 | 0.018358 | 0.795113 | -0.386274 | 0.427011 | -0.160934 | -1.966054 | -0.952876 | -1.138180 | -0.635081 | 1.523410 | -0.856518 | 0.684642 | -1.081286 | 0.228999 | -0.890409 | 0.500534 | -0.912965 | -0.658863 | 0.711759 | 0.476150 | 0.973722 | -1.576857 | -0.640923 | -0.398626 | 0.141123 | 0.156522 | -0.066611 | -1.749565 | -0.518997 | -0.439959 | 0.322202 | -1.054731 | 1.581706 | 0.112304 | 2.048272 | -0.543601 | -1.147761 | 0.545976 | 0.266249 | 0.470301 | -0.687722 | -0.632856 | -0.683362 | -1.291750 | 0.565963 | 0.399943 | 0.905395 | -0.192770 | 0.807798 | -0.387576 | -0.216277 | -0.046453 | 1.935200 | 1.183481 | 0.405696 | 1.873436 | 1.961536 | 1.008626 | 0.671273 | -2.855887 | 0.741276 | 0.074018 | 1.129584 | -0.886903 | -0.340590 | 0.215483 | 0.446204 | 0.439725 | 1.957116 | -0.445490 | 0.947790 | 0.635031 | 0.225685 | 1.523159 | 0.813343 | -0.060784 | -1.607853 | -0.352196 | -1.515608 | 0.044250 | -0.566870 | 0.565938 | 2.362594 | -1.048067 | 0.636425 | 1.208411 | -1.126668 | 1.103816 | -0.682065 | 0.293105 | 0.007222 | -1.748249 | -0.097906 | -1.006603 | 1.238084 | 0.032449 | -0.916133 | 
|  |  | 1 | 0.638091 | -1.263351 | -1.026522 | 0.213395 | 0.605262 | 0.668249 | -0.149394 | -1.339944 | 0.698683 | 1.199415 | -0.263830 | -0.051851 | -0.791915 | -0.044925 | 1.659059 | 1.492263 | 1.750472 | -1.727650 | 0.242873 | 1.231380 | 0.060159 | 1.386421 | -0.998404 | -0.008600 | 0.463815 | 0.212580 | 0.548790 | -0.836541 | -1.772024 | 2.637310 | -0.646087 | 0.014787 | -0.818144 | -0.661508 | 1.127787 | 0.407368 | 1.064530 | -0.271909 | 0.422858 | 0.573724 | -0.871016 | 0.174475 | -0.601939 | 1.320925 | 0.359677 | 0.692463 | -0.707375 | -0.105360 | -0.428715 | 1.272814 | -1.154052 | -0.758770 | -0.523536 | -0.750004 | -0.151967 | -0.936328 | -0.485521 | 1.630334 | 0.065307 | 1.263922 | 0.393902 | 0.800497 | -1.200119 | 0.921761 | 2.294416 | -0.322866 | 0.385961 | -1.698391 | 0.529921 | 0.538005 | -0.826206 | -0.966698 | 0.777591 | 1.603942 | 0.572657 | 0.882799 | 0.173200 | -0.004198 | -0.638427 | 1.958323 | -0.323694 | 1.894872 | -1.607778 | 0.603142 | 0.677462 | 0.462840 | 1.312929 | -0.029531 | -0.355775 | -1.424371 | 0.201973 | 0.078968 | 0.530699 | -0.351735 | -1.753653 | 1.437835 | -2.017140 | -1.894215 | 0.582887 | -1.908740 | 
|  |  | 2 | 0.615421 | -0.556665 | -0.828299 | 0.438880 | 1.320985 | 0.520077 | 0.254125 | -0.229425 | 1.235457 | 1.276169 | 0.558587 | 0.782341 | -0.732503 | -1.210421 | -0.034196 | 1.034804 | -0.122429 | -0.000241 | -1.530904 | -1.449231 | -0.009184 | 1.825607 | 1.285270 | 0.489378 | -2.364886 | -1.799813 | 1.830970 | -2.082466 | 0.383160 | -1.144195 | 0.082588 | 1.211101 | 0.390994 | -0.040749 | 0.808947 | 1.311611 | 0.453154 | 0.569982 | 0.646023 | -0.069526 | -1.006879 | -0.874861 | 2.546722 | 0.416755 | -0.140203 | -1.523114 | -3.374827 | -1.655652 | -0.424794 | 0.378496 | 1.908024 | 0.319300 | -1.535855 | -0.103569 | -0.000077 | -0.926792 | -1.578229 | -0.424063 | -0.805444 | 0.436176 | -1.217475 | -0.354085 | -0.315280 | -0.556084 | 0.468431 | 0.762999 | -0.581309 | -0.338872 | -1.891932 | 0.575485 | -0.993463 | -2.882135 | 0.893977 | 0.441540 | -0.245048 | -0.011467 | 1.743730 | -1.384662 | 1.036140 | -0.105277 | -0.846649 | -1.171898 | 1.043947 | -0.034855 | -0.023222 | 0.496117 | -0.813425 | 0.372879 | 1.117880 | 0.950857 | -1.947647 | 1.068407 | 0.153447 | 0.609296 | 0.106221 | 0.565740 | 0.779673 | -0.250506 | -0.255725 | -1.076758 | 
|  |  | 3 | 0.677673 | -0.983991 | -0.508196 | -0.223275 | -0.892658 | 0.049644 | 0.199172 | -1.285564 | 0.522279 | 0.556498 | 1.534189 | -0.589428 | 0.225771 | -0.413116 | 0.056281 | -0.687684 | -0.748417 | -1.063367 | -1.061866 | -0.621624 | -0.347029 | 0.418753 | -1.106199 | -0.011235 | -0.203031 | -0.749104 | 0.757819 | -1.678048 | 0.831730 | 0.317106 | -0.713187 | -1.296103 | 1.178605 | -1.766184 | 0.405308 | -0.282047 | -0.700566 | -0.216445 | 1.412939 | 1.277242 | -1.008928 | 0.814763 | 0.288451 | -0.541380 | -0.557220 | -0.211266 | 1.400355 | -0.302584 | -0.972397 | 0.473262 | -1.233860 | -1.398580 | -0.345065 | -0.230340 | -0.688938 | 0.486462 | 0.445978 | -0.131654 | -0.032604 | 1.096168 | -1.165757 | -0.755705 | 1.113990 | 0.252089 | -0.179101 | 1.889106 | 1.257870 | 0.043826 | 0.001889 | -1.019826 | -0.576884 | -1.086858 | 0.363399 | -0.138195 | -1.576783 | 0.621132 | -0.213443 | 1.236186 | -0.219811 | -1.990014 | 0.039207 | -0.549818 | 0.275171 | -0.200415 | 1.065812 | 1.472389 | 1.891503 | -1.376733 | 0.128155 | -0.478999 | -0.679482 | 0.369820 | -0.084990 | -0.741410 | -1.356090 | -0.992864 | -1.587088 | -0.081792 | -0.661331 | 0.857166 | 
| B | 0 | 0 | 0.103721 | -1.750882 | 0.454741 | 0.880516 | 0.022227 | 0.031036 | -1.479162 | 0.574677 | -1.171226 | -0.964487 | 0.042584 | 2.674862 | -0.829213 | 2.284442 | 0.529467 | -0.033147 | -1.372299 | -0.056735 | -0.483158 | 1.633496 | 0.407124 | -0.361379 | 0.876548 | -0.347282 | -0.193713 | -0.900805 | 0.851192 | 1.411834 | 0.549841 | 0.109058 | -0.723613 | -0.792426 | 1.250363 | -0.807820 | 0.069971 | -0.303110 | 0.207053 | 0.257658 | -1.898140 | -0.102084 | 0.111499 | 0.488816 | -1.412533 | -0.399015 | -0.044270 | -1.160856 | 1.110853 | 0.424903 | 0.094994 | 0.876240 | 0.371636 | 0.514959 | 0.716920 | -0.861331 | 0.410777 | -1.166119 | -0.425079 | 0.000568 | -0.556060 | 0.630109 | 0.265495 | 2.302520 | 0.488671 | 1.750115 | -1.168802 | -0.843555 | -1.356735 | -0.944888 | -0.805620 | 0.384120 | 1.782541 | -0.436819 | -0.987764 | -0.052830 | -0.778743 | -0.436386 | -0.979797 | 0.646287 | -0.247060 | 0.808295 | 0.357228 | 0.202857 | -0.413732 | 0.696503 | -1.814141 | -0.454738 | 1.032526 | 0.006814 | -1.198463 | 1.926113 | 0.463695 | -1.061729 | 0.940131 | 0.440455 | 0.834434 | -0.239375 | -1.193795 | 0.289589 | -1.919376 | 0.300618 | 
|  |  | 1 | 1.167028 | 0.801218 | -0.753100 | -1.444753 | 0.227993 | -1.038193 | 1.025010 | -0.579519 | 0.132131 | 1.254681 | 0.643115 | 0.769858 | 0.223719 | -1.016941 | 0.058445 | -0.974466 | -1.654139 | -1.303969 | 0.783598 | 1.121699 | 0.959242 | -0.975369 | 0.504326 | 1.044171 | 1.008731 | -2.296769 | 1.259882 | -0.251946 | 0.783393 | -1.309242 | -0.046419 | 0.193768 | -1.077143 | -1.652423 | -0.246300 | 1.272914 | -1.155368 | 0.019024 | -0.349040 | -0.851228 | -1.927419 | 0.614689 | 0.219010 | -2.101607 | -1.312230 | -0.037534 | -1.262569 | 2.046184 | 0.479554 | -0.253348 | -0.675235 | 1.976276 | -0.530426 | -0.660220 | 0.571842 | -0.045128 | -0.447864 | 1.502488 | -2.248540 | 0.461898 | -0.378596 | -0.052101 | 0.789870 | 0.109803 | 0.243981 | 1.643840 | -1.047127 | -0.838163 | 0.190855 | -1.005314 | 0.296393 | 1.147729 | -1.830598 | -0.816001 | 0.377070 | -0.575019 | -1.097977 | 0.410986 | 1.192989 | 1.102330 | 0.596597 | -0.453403 | -1.282656 | 2.132497 | 1.801097 | -1.326927 | -0.042096 | -1.214378 | -0.203234 | -0.321269 | -0.284141 | -0.134051 | -0.565122 | -0.835913 | 0.784693 | -0.070871 | -0.136708 | 0.893560 | -0.070201 | -1.093890 | 
|  |  | 2 | -2.072411 | -0.385812 | -0.535624 | 1.146529 | -1.328274 | -1.466910 | -0.343952 | 0.635520 | 1.916967 | -0.445547 | 0.513106 | 0.122684 | -2.012649 | 2.213130 | -0.876255 | -0.337970 | -0.691478 | -0.565034 | 1.128058 | -1.146403 | -1.343220 | -0.089720 | -1.842053 | -1.065449 | -1.937323 | 0.370771 | 0.498412 | -0.201642 | 0.325548 | 0.375321 | -0.422994 | -0.311858 | -0.270497 | -0.513538 | 0.209063 | -1.363838 | -0.452896 | 0.603445 | 1.180090 | -0.081360 | -0.731317 | 2.014934 | -0.332546 | 0.768859 | 1.202408 | 0.268089 | -0.334788 | -0.793848 | -0.022587 | -0.171461 | 1.900468 | -1.967115 | -1.293951 | 0.782726 | 0.145005 | -0.409100 | -0.813320 | -0.175022 | -0.171934 | -0.117674 | -0.259813 | -0.564975 | -0.037270 | -0.689533 | 1.427015 | 0.981466 | 0.572991 | 0.137788 | 0.026421 | 0.196064 | 1.208259 | 1.415522 | -0.892827 | -1.014016 | 0.166945 | -2.723871 | -0.750593 | 0.537742 | -0.040917 | 0.216384 | 1.206401 | 0.464926 | -0.730086 | 2.395573 | -0.459004 | 1.233121 | 0.198533 | 0.576266 | 1.031852 | 0.731763 | -0.019858 | 1.694699 | 0.021719 | -1.811736 | 0.047970 | 0.739044 | -1.452084 | -0.209275 | -1.642848 | 0.429650 | 
|  |  | 3 | 1.118249 | -0.174247 | 1.124966 | -0.721937 | -0.265553 | -0.520646 | -1.361829 | 0.565736 | -1.618938 | 0.308877 | -1.667273 | 1.161356 | 0.700031 | 0.967877 | 2.235055 | -0.537956 | 1.252550 | -0.643366 | -1.423460 | -0.271388 | -0.108833 | 1.615209 | 0.290848 | 1.290791 | -0.137172 | 1.127603 | 0.327152 | -0.988139 | 0.447378 | 0.616595 | 0.146788 | -0.389949 | 0.259622 | 0.419123 | 0.850294 | 1.519774 | -0.813029 | 1.292770 | -1.096248 | 0.520481 | -0.707953 | 1.064422 | -0.709130 | -2.010674 | -0.025539 | 1.983015 | -0.290004 | -0.888709 | 0.228862 | -0.329893 | 0.319327 | 0.025947 | -0.998704 | 1.277585 | 1.613820 | 0.524826 | -2.374740 | 3.569202 | -0.102998 | 0.634771 | -0.341868 | -0.578210 | -0.356209 | -1.042418 | 0.096909 | 0.186491 | -1.441296 | -0.434589 | 1.058764 | 1.039132 | -1.731982 | -0.093453 | -0.501065 | 2.070266 | 0.071090 | 0.216531 | -0.724696 | 1.936130 | 0.919238 | 1.222116 | 0.217523 | -0.489636 | -0.233529 | -0.014936 | 1.830587 | -1.292743 | 1.290005 | -0.817594 | -1.988278 | -2.197472 | -0.204582 | -1.251410 | 0.292923 | -0.075040 | -0.039473 | -0.453339 | 1.277491 | -0.452404 | 0.643447 | 0.142819 | 
|  | 1 | 0 | -0.351171 | 1.023940 | -1.511498 | 0.618944 | 0.179706 | -1.228064 | 0.649514 | -0.052935 | 0.546807 | -1.203840 | -0.131340 | -0.092921 | -0.909330 | -0.137975 | 1.637062 | -1.295018 | -0.264532 | 1.136117 | -0.716100 | -1.183280 | -0.471934 | 0.143074 | -0.014638 | 0.961549 | -0.321732 | -0.933943 | -0.841826 | -1.296579 | -0.442408 | 1.282533 | -1.601770 | -1.345018 | -0.662283 | 0.220842 | 0.388788 | 0.632474 | -1.347650 | 1.594317 | -0.617301 | -2.331357 | -2.511449 | -1.364538 | -0.799043 | -0.925109 | 0.632510 | -0.351499 | -2.661751 | -0.349751 | 0.773978 | 1.368351 | -0.268107 | -1.427781 | 0.685167 | -0.682513 | 0.276713 | -1.945579 | 0.645838 | -1.447977 | -0.628495 | -0.807960 | 0.011758 | -0.330518 | 0.419784 | 0.958082 | 1.586090 | 0.439872 | 1.340896 | 0.482043 | -0.006991 | -1.687864 | -1.017623 | -0.877199 | 0.740574 | -1.760090 | 0.659850 | -1.057235 | 0.536957 | 0.541132 | 3.194705 | 0.842192 | -0.282684 | -0.700363 | -0.395353 | -0.648448 | 1.684356 | -0.605384 | -0.729134 | 1.618759 | -0.086524 | 1.454520 | -0.045343 | -0.213119 | 0.320458 | 0.393286 | 0.263270 | -1.188044 | 0.045544 | -0.096079 | 1.379419 | 0.619566 | 
|  |  | 1 | -2.697761 | -0.216438 | 0.193286 | 1.100150 | -0.310430 | 0.019088 | -0.584535 | 0.719542 | -0.408461 | -0.647319 | -0.123209 | 0.002073 | -0.062305 | 1.309970 | 1.387754 | 1.288008 | 1.811905 | -1.065786 | -0.129579 | -0.024781 | -0.045186 | 0.854322 | 0.632747 | 0.582554 | -0.528291 | -0.509413 | -0.513704 | -3.074055 | -0.347337 | -0.049953 | -0.689384 | 0.237674 | 0.709307 | -0.181012 | 0.705539 | -0.471619 | -0.993367 | 1.037987 | -1.325141 | 0.545704 | 1.465180 | -0.987134 | 1.293419 | 1.133797 | -0.118827 | -2.039961 | -0.628638 | 0.551746 | -0.863957 | 0.954502 | -1.415083 | 0.253340 | 0.132188 | -0.892947 | -0.068687 | -0.311260 | -0.218912 | -1.371360 | 0.194940 | -2.114055 | 0.549188 | 1.226060 | 0.396822 | 0.427769 | -2.101510 | -0.332989 | -0.636885 | 0.364170 | -0.295028 | -2.414402 | -0.710915 | 0.951053 | 0.627281 | -1.456425 | -0.574606 | 0.341497 | 0.211243 | -1.100198 | 0.139133 | -1.922422 | -1.677048 | -0.109762 | 0.588005 | 1.388541 | -1.574352 | 3.018430 | 0.272214 | 0.119566 | 0.274605 | -1.003207 | 0.375928 | 0.520244 | -0.608685 | -0.891610 | 0.366384 | -1.100234 | 0.747745 | -0.301267 | -0.525439 | -0.418862 | 
|  |  | 2 | -0.122055 | 2.385162 | -0.889962 | -2.126945 | -0.868092 | 0.924390 | -0.072401 | 0.511622 | -1.186318 | 0.412805 | 0.049856 | 0.175842 | 0.021513 | -1.390033 | -0.715350 | 1.008352 | -0.405259 | -0.620009 | 0.935516 | 1.076372 | -0.951242 | -1.028077 | 1.287850 | 0.990782 | -0.928193 | -1.701400 | 0.933439 | -1.095484 | 0.703306 | 0.119863 | 0.680616 | -0.552189 | -1.773081 | -1.745979 | 1.016690 | -0.997333 | 0.347358 | -1.073921 | -1.250854 | -0.057358 | -1.987934 | 1.072044 | -0.396370 | -0.137720 | 1.255489 | 1.385366 | -0.662146 | -0.172926 | -0.114310 | 0.181880 | 2.509978 | -0.670348 | 0.046463 | -0.727387 | 0.650764 | -0.199858 | -1.275904 | -2.227526 | -0.346872 | 0.159554 | 1.228139 | -0.324135 | -0.185899 | 1.391892 | -0.303876 | 0.077019 | -0.221683 | 0.043599 | -0.229868 | -1.641672 | -0.246286 | 0.481877 | 0.318264 | -1.241771 | -0.513658 | 0.505226 | 0.137411 | 1.744722 | 0.284010 | -0.292033 | 1.186801 | -0.005072 | 2.514258 | -0.798792 | -1.713557 | -0.552754 | -0.160860 | -0.758267 | -0.579887 | 0.238086 | 0.457199 | 0.693525 | -0.461557 | -0.331175 | 0.895554 | 1.286008 | -1.996121 | 1.152437 | 0.604731 | 1.644384 | 
|  |  | 3 | 0.221145 | -1.173363 | 0.639189 | 0.952842 | 1.027615 | 1.095652 | -1.755546 | 1.805602 | 0.441859 | -0.348648 | -0.792012 | 0.973091 | 0.812662 | 0.402470 | -1.116643 | -0.749974 | 0.334878 | 0.038702 | 0.485698 | 0.356709 | 0.002965 | 0.233249 | -0.230521 | -3.210940 | 0.452658 | -1.311130 | 1.589915 | 1.743064 | 1.739856 | -0.464779 | -0.425398 | 2.501711 | -0.353845 | 0.071148 | 0.029837 | 0.273868 | 0.557694 | 0.035491 | -0.328312 | 1.093099 | -0.555101 | 0.416110 | 0.399903 | 0.660542 | 0.803015 | -0.318798 | 0.022345 | 0.157851 | 0.504515 | 0.428456 | -1.873753 | 0.622458 | -0.707877 | 0.380368 | -1.132078 | 1.936629 | 0.784655 | 0.886954 | -0.701823 | 0.259614 | 2.232133 | 0.232930 | -1.149868 | -0.751935 | 0.473409 | -0.604753 | -1.199894 | 0.300114 | 0.714157 | 0.665725 | 1.743132 | 0.497531 | 0.623560 | -1.022099 | 0.456591 | -1.664579 | 0.397944 | -0.962254 | -0.254085 | 0.809131 | 1.155931 | -2.477604 | 0.057874 | 0.888901 | 1.501404 | 1.272566 | 0.457429 | 1.241974 | -0.719311 | -1.331647 | 0.536821 | -0.782027 | 1.286608 | 0.859641 | -0.336375 | -0.313944 | -0.676993 | 0.130637 | 1.424001 | -0.292073 | 

### HTML Escaping[#](https://pandas.pydata.org#HTML-Escaping)

Suppose you have to display HTML within HTML, that can be a bit of pain when the renderer can’t distinguish. You can use the `escape` formatting option to handle this, and even use it within a formatter that contains HTML itself.

Note that if you’re using `Styler` on untrusted, user-provided input to serve HTML then you should escape the input to prevent security vulnerabilities. See the Jinja2 documentation for more.

```
df4 = pd.DataFrame([["<div></div>", '"&other"', "<span></span>"]])
df4.style
```
|  | 0 | 1 | 2 | 
|---|---|---|---|
| 0 |  | "&other" |  | 

```
df4.style.format(escape="html")
```
|  | 0 | 1 | 2 | 
|---|---|---|---|
| 0 | \<div>\</div> | "&other" | \<span>\</span> | 

```
df4.style.format(
    '<a href="https://pandas.pydata.org" target="_blank">{}</a>', escape="html"
)
```
## Export to Excel[#](https://pandas.pydata.org#Export-to-Excel)

Some support (*since version 0.20.0*) is available for exporting styled `DataFrames` to Excel worksheets using the `OpenPyXL` or `XlsxWriter` engines. CSS2.2 properties handled include:

- `background-color`
- `border-style` properties
- `border-width` properties
- `border-color` properties
- `color`
- `font-family`
- `font-style`
- `font-weight`
- `text-align`
- `text-decoration`
- `vertical-align`
- `white-space: nowrap`
- Shorthand and side-specific border properties are supported (e.g. `border-style` and `border-left-style`) as well as the `border` shorthands for all sides (`border: 1px solid green`) or specified sides (`border-left: 1px solid green`). Using a `border` shorthand will override any border properties set before it (See [CSS Working Group](https://drafts.csswg.org/css-backgrounds/#border-shorthands) for more details)
- Only CSS2 named colors and hex colors of the form `#rgb` or `#rrggbb` are currently supported.
- The following pseudo CSS properties are also available to set Excel specific style properties: 
  - `number-format`
  - `border-style` (for Excel-specific styles: “hair”, “mediumDashDot”, “dashDotDot”, “mediumDashDotDot”, “dashDot”, “slantDashDot”, or “mediumDashed”)

Table level styles, and data cell CSS-classes are not included in the export to Excel: individual cells must have their properties mapped by the `Styler.apply` and/or `Styler.map` methods.

```
df2.style.map(style_negative, props="color:red;").highlight_max(axis=0).to_excel(
    "styled.xlsx", engine="openpyxl"
)
```
A screenshot of the output:

## Export to LaTeX[#](https://pandas.pydata.org#Export-to-LaTeX)

There is support (*since version 1.3.0*) to export `Styler` to LaTeX. The documentation for the [.to\_latex](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.to_latex.html) method gives further detail and numerous examples.

## More About CSS and HTML[#](https://pandas.pydata.org#More-About-CSS-and-HTML)

Cascading Style Sheet (CSS) language, which is designed to influence how a browser renders HTML elements, has its own peculiarities. It never reports errors: it just silently ignores them and doesn’t render your objects how you intend so can sometimes be frustrating. Here is a very brief primer on how `Styler` creates HTML and interacts with CSS, with advice on common pitfalls to avoid.

### CSS Classes and Ids[#](https://pandas.pydata.org#CSS-Classes-and-Ids)

The precise structure of the CSS `class` attached to each cell is as follows.

- Cells with Index and Column names include `index_name` and `level<k>` where `k` is its level in a MultiIndex
- Index label cells include 
  - `row_heading`
  - `level<k>` where `k` is the level in a MultiIndex
  - `row<m>` where `m` is the numeric position of the row
- Column label cells include 
  - `col_heading`
  - `level<k>` where `k` is the level in a MultiIndex
  - `col<n>` where `n` is the numeric position of the column
- Data cells include 
  - `data`
  - `row<m>`, where `m` is the numeric position of the cell.
  - `col<n>`, where `n` is the numeric position of the cell.
- Blank cells include `blank`
- Trimmed cells include `col_trim` or `row_trim`

The structure of the `id` is `T_uuid_level<k>_row<m>_col<n>` where `level<k>` is used only on headings, and headings will only have either `row<m>` or `col<n>` whichever is needed. By default we’ve also prepended each row/column identifier with a UUID unique to each DataFrame so that the style from one doesn’t collide with the styling from another within the same notebook or page. You can read more about the use of UUIDs in [Optimization](https://pandas.pydata.org#Optimization).

We can see example of the HTML by calling the [.to\_html()](https://pandas.pydata.org/reference/api/pandas.io.formats.style.Styler.to_html.html) method.

```
print(
    pd.DataFrame(
        [[1, 2], [3, 4]], index=["i1", "i2"], columns=["c1", "c2"]
    ).style.to_html()
)
```
```
<style type="text/css">
</style>
<table id="T_d850e">
  <thead>
    <tr>
      <th class="blank level0" > </th>
      <th id="T_d850e_level0_col0" class="col_heading level0 col0" >c1</th>
      <th id="T_d850e_level0_col1" class="col_heading level0 col1" >c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d850e_level0_row0" class="row_heading level0 row0" >i1</th>
      <td id="T_d850e_row0_col0" class="data row0 col0" >1</td>
      <td id="T_d850e_row0_col1" class="data row0 col1" >2</td>
    </tr>
    <tr>
      <th id="T_d850e_level0_row1" class="row_heading level0 row1" >i2</th>
      <td id="T_d850e_row1_col0" class="data row1 col0" >3</td>
      <td id="T_d850e_row1_col1" class="data row1 col1" >4</td>
    </tr>
  </tbody>
</table>
```
### CSS Hierarchies[#](https://pandas.pydata.org#CSS-Hierarchies)

The examples have shown that when CSS styles overlap, the one that comes last in the HTML render, takes precedence. So the following yield different results:

```
df4 = pd.DataFrame([["text"]])
df4.style.map(lambda x: "color:green;").map(lambda x: "color:red;")
```
|  | 0 | 
|---|---|
| 0 | text | 

```
df4.style.map(lambda x: "color:red;").map(lambda x: "color:green;")
```
|  | 0 | 
|---|---|
| 0 | text | 

This is only true for CSS rules that are equivalent in hierarchy, or importance. You can read more about [CSS specificity here](https://www.w3schools.com/css/css_specificity.asp) but for our purposes it suffices to summarize the key points:

A CSS importance score for each HTML element is derived by starting at zero and adding:

- 1000 for an inline style attribute
- 100 for each ID
- 10 for each attribute, class or pseudo-class
- 1 for each element name or pseudo-element

Let’s use this to describe the action of the following configurations

```
df4.style.set_uuid("a_").set_table_styles(
    [{"selector": "td", "props": "color:red;"}]
).map(lambda x: "color:green;")
```
|  | 0 | 
|---|---|
| 0 | text | 

This text is red because the generated selector `#T_a_ td` is worth 101 (ID plus element), whereas `#T_a_row0_col0` is only worth 100 (ID), so is considered inferior even though in the HTML it comes after the previous.

```
df4.style.set_uuid("b_").set_table_styles(
    [
        {"selector": "td", "props": "color:red;"},
        {"selector": ".cls-1", "props": "color:blue;"},
    ]
).map(lambda x: "color:green;").set_td_classes(pd.DataFrame([["cls-1"]]))
```
|  | 0 | 
|---|---|
| 0 | text | 

In the above case the text is blue because the selector `#T_b_ .cls-1` is worth 110 (ID plus class), which takes precedence.

```
df4.style.set_uuid("c_").set_table_styles(
    [
        {"selector": "td", "props": "color:red;"},
        {"selector": ".cls-1", "props": "color:blue;"},
        {"selector": "td.data", "props": "color:yellow;"},
    ]
).map(lambda x: "color:green;").set_td_classes(pd.DataFrame([["cls-1"]]))
```
|  | 0 | 
|---|---|
| 0 | text | 

Now we have created another table style this time the selector `T_c_ td.data` (ID plus element plus class) gets bumped up to 111.

If your style fails to be applied, and its really frustrating, try the `!important` trump card.

```
df4.style.set_uuid("d_").set_table_styles(
    [
        {"selector": "td", "props": "color:red;"},
        {"selector": ".cls-1", "props": "color:blue;"},
        {"selector": "td.data", "props": "color:yellow;"},
    ]
).map(lambda x: "color:green !important;").set_td_classes(pd.DataFrame([["cls-1"]]))
```
|  | 0 | 
|---|---|
| 0 | text | 

Finally got that green text after all!

## Extensibility[#](https://pandas.pydata.org#Extensibility)

The core of pandas is, and will remain, its “high-performance, easy-to-use data structures”. With that in mind, we hope that `DataFrame.style` accomplishes two goals

- Provide an API that is pleasing to use interactively and is “good enough” for many tasks
- Provide the foundations for dedicated libraries to build on

If you build a great library on top of this, let us know and we’ll [link](https://pandas.pydata.org/community/ecosystem.html) to it.

### Subclassing[#](https://pandas.pydata.org#Subclassing)

If the default template doesn’t quite suit your needs, you can subclass Styler and extend or override the template. We’ll show an example of extending the default template to insert a custom header before each table.

```
from jinja2 import Environment, ChoiceLoader, FileSystemLoader
from IPython.display import HTML
from pandas.io.formats.style import Styler
```
We’ll use the following template:

```
with open("templates/myhtml.tpl") as f_html:
    print(f_html.read())
```
```
{% extends "html_table.tpl" %}
{% block table %}
<h1>{{ table_title|default("My Table") }}</h1>
{{ super() }}
{% endblock table %}
```
Now that we’ve created a template, we need to set up a subclass of `Styler` that knows about it.

```
class MyStyler(Styler):
    env = Environment(
        loader=ChoiceLoader(
            [
                FileSystemLoader("templates"),  # contains ours
                Styler.loader,  # the default
            ]
        )
    )
    template_html_table = env.get_template("myhtml.tpl")
```
Notice that we include the original loader in our environment’s loader. That’s because we extend the original template, so the Jinja environment needs to be able to find it.

Now we can use that custom styler. It’s `__init__` takes a DataFrame.

```
MyStyler(df3)
```
# My Table

|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

Our custom template accepts a `table_title` keyword. We can provide the value in the `.to_html` method.

```
HTML(MyStyler(df3).to_html(table_title="Extending Example"))
```
# Extending Example

|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

For convenience, we provide the `Styler.from_custom_template` method that does the same as the custom subclass.

```
EasyStyler = Styler.from_custom_template("templates", "myhtml.tpl")
HTML(EasyStyler(df3).to_html(table_title="Another Title"))
```
# Another Title

|  |  | c1 | c2 | c3 | c4 | 
|---|---|---|---|---|---|
| A | r1 | -1.036038 | -0.283096 | 0.543826 | 2.285762 | 
|  | r2 | 0.724792 | 0.163105 | 0.848006 | 0.039803 | 
| B | r1 | -1.910225 | 0.743117 | 0.067063 | -0.787786 | 
|  | r2 | -0.817487 | 0.996195 | 0.091432 | 0.855318 | 

#### Template Structure[#](https://pandas.pydata.org#Template-Structure)

Here’s the template structure for the both the style generation template and the table generation template:

Style template:

```
HTML(style_structure)
```
\<style type="text/css">

\</style>

Table template:

```
HTML(table_structure)
```
\<table ...>

\</table>

See the template in the [GitHub repo](https://github.com/pandas-dev/pandas) for more details.