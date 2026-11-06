---
id: "numpy_001"
technology: "NumPy"
category: "ML & Data"
title: "NumPy"
doc_order: 1
source_url: "https://numpy.org"
language: "en"
retrieved_at: "2026-11-01 22:36:54"
content_hash: "4e27dd0faf554595e4da8b960000ec3ce24f58c89ce14d771f2bd7d351444499"
---

# NumPy

Source: https://numpy.org

---

```
"""
To try the examples in the browser:
1. Type code in the input cell and press
   Shift + Enter to execute
2. Or copy paste the code, and click on
   the "Run" button in the toolbar
"""
# The standard way to import NumPy:
import numpy as np
# Create a 2-D array, set every second element in
# some rows and find max per row:
x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
x
# array([[  0,   1,   2,   3,   4],
#        [-99,   6, -99,   8, -99],
#        [-99,  11, -99,  13, -99]])
x.max(axis=1)
# array([ 4,  8, 13])
# Generate normally distributed random numbers:
rng = np.random.default_rng()
samples = rng.normal(size=2500)
samples
```
Nearly every scientist working in Python draws on the power of NumPy.

NumPy brings the computational power of languages like C and Fortran to Python, a language much easier to learn and use. With this power comes simplicity: a solution in NumPy is often clear and elegant.

NumPy's API is the starting point when libraries are written to exploit innovative hardware, create specialized array types, or add capabilities beyond what NumPy provides.

|  | Array Library | Capabilities & Application areas | 
|  | [Dask](https://dask.org/) | Distributed arrays and advanced parallelism for analytics, enabling performance at scale. | 
|  | [CuPy](https://cupy.dev) | NumPy-compatible array library for GPU-accelerated computing with Python. | 
|  | [JAX](https://docs.jax.dev) | Composable transformations of NumPy programs: differentiate, vectorize, just-in-time compilation to GPU/TPU. | 
|  | [Xarray](https://xarray.pydata.org/en/stable/index.html) | Labeled, indexed multi-dimensional arrays for advanced analytics and visualization. | 
|  | [Sparse](https://sparse.pydata.org/en/latest/) | NumPy-compatible sparse array library that integrates with Dask and SciPy's sparse linear algebra. | 
|  | [PyTorch](https://pytorch.org/) | Deep learning framework that accelerates the path from research prototyping to production deployment. | 
|  | [TensorFlow](https://www.tensorflow.org) | An end-to-end platform for machine learning to easily build and deploy ML powered applications. | 
|  | [Arrow](https://arrow.apache.org/) | A cross-language development platform for columnar in-memory data and analytics. | 
|  | [xtensor](https://github.com/xtensor-stack/xtensor-python) | Multi-dimensional arrays with broadcasting and lazy computing for numerical analysis. | 
|  | [Awkward Array](https://awkward-array.org/) | Manipulate JSON-like data with NumPy-like idioms. | 
|  | [uarray](https://uarray.org/en/latest/) | Python backend system that decouples API from implementation; unumpy provides a NumPy API. | 
|  | [tensorly](http://tensorly.org/stable/home.html) | Tensor learning, algebra and backends to seamlessly use NumPy, PyTorch, TensorFlow or CuPy. | 
|  | [Blosc2](https://www.blosc.org/python-blosc2/) | Accelerated computation for in-memory, on-disk, or remote compressed arrays. | 

NumPy lies at the core of a rich ecosystem of data science libraries. A typical exploratory data science workflow might look like:

NumPy forms the basis of powerful machine learning libraries like [scikit-learn](https://scikit-learn.org) and [SciPy](https://scipy.org). As machine learning grows, so does the list of libraries built on NumPy. [TensorFlow’s](https://www.tensorflow.org) deep learning capabilities have broad applications — among them speech and image recognition, text-based applications, time-series analysis, and video detection. [PyTorch](https://pytorch.org), another deep learning library, is popular among researchers in computer vision and natural language processing.

Statistical techniques called [ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html) such as binning, bagging, stacking, and boosting are among the ML algorithms implemented by tools such as [XGBoost](https://xgboost.readthedocs.io/), [LightGBM](https://lightgbm.readthedocs.io/en/latest/), and [CatBoost](https://catboost.ai) — one of the fastest inference engines. [Yellowbrick](https://www.scikit-yb.org/en/latest/) and [Eli5](https://eli5.readthedocs.io/en/latest/) offer machine learning visualizations.

NumPy is an essential component in the burgeoning [Python visualization landscape](https://pyviz.org/overviews/index.html), which includes [Matplotlib](https://matplotlib.org), [Seaborn](https://seaborn.pydata.org), [Plotly](https://plot.ly), [Altair](https://altair-viz.github.io), [Bokeh](https://docs.bokeh.org/en/latest/), [Holoviz](https://holoviz.org), [Vispy](http://vispy.org), [Napari](https://napari.org/), and [PyVista](https://pyvista.org), to name a few.

NumPy’s accelerated processing of large arrays allows researchers to visualize datasets far larger than native Python could handle.