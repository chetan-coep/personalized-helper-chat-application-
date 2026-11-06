---
id: "pandas_004"
technology: "pandas"
category: "ML & Data"
title: "API reference — pandas 3.1.0 documentation"
doc_order: 4
source_url: "https://pandas.pydata.org/docs/reference/index.html"
language: "en"
retrieved_at: "2026-11-03 17:57:14"
content_hash: "678a63e591a7f8a0ec6a16350f70999fb4ba651daf3a4bd1da62015fe8559e62"
---

# API reference — pandas 3.1.0 documentation

Source: https://pandas.pydata.org/docs/reference/index.html

---

# API reference[#](https://pandas.pydata.org#api-reference)

This page gives an overview of all public pandas objects, functions and
methods. All classes and functions exposed in `pandas.*` namespace are public.

The following subpackages are public.

- `pandas.errors`: Custom exception and warnings classes that are raised by pandas.
- `pandas.plotting`: Plotting public API.
- `pandas.testing`: Functions that are useful for writing tests involving pandas objects.
- `pandas.api.extensions`: Functions and classes for extending pandas objects.
- `pandas.api.indexers`: Functions and classes for rolling window indexers.
- `pandas.api.interchange`: DataFrame interchange protocol.
- `pandas.api.types`: Datatype classes and functions.
- `pandas.api.typing`: Classes that may be necessary for type-hinting.
These are classes that are encountered as intermediate results but should not be instantiated
directly by users. These classes are not to be confused with classes from the [pandas-stubs](https://github.com/pandas-dev/pandas-stubs) package
which has classes in addition to those that occur in pandas for type-hinting.

In addition, public functions in `pandas.io`, `pandas.tseries`, `pandas.util` submodules
are explicitly mentioned in the documentation. Further APIs in these modules are not guaranteed
to be stable.

Warning

The `pandas.core`, `pandas.compat` top-level modules are PRIVATE. Stable functionality in such modules is not guaranteed.