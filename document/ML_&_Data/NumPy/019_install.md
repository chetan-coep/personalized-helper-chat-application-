---
id: "numpy_019"
technology: "NumPy"
category: "ML & Data"
title: "NumPy"
doc_order: 19
source_url: "https://numpy.org/install"
language: "en"
retrieved_at: "2026-11-01 22:37:17"
content_hash: "d65175668226d74cc20ffda08262dc8ae9379afac6395245a6e1e537683f6c96"
---

# NumPy

Source: https://numpy.org/install

---

This page assumes you are comfortable using a terminal and are familiar with package managers.
The only prerequisite for installing NumPy is Python itself. If you don’t have
Python yet and want the simplest way to get started, we recommend you use the
[Anaconda Distribution](https://www.anaconda.com/download) - it includes
Python, NumPy, and many other commonly used packages for scientific computing
and data science.

The recommended method of installing NumPy depends on your preferred workflow. Below, we break down the installation methods into the following categories:

Choose the method that best suits your needs. If you’re unsure, start with the **Environment-based** method using `conda` or `pip`.

Below are the different methods for **installing NumPy**. Click on the tabs to explore each method:

Recommended for new users who want a streamlined workflow.

**uv:** A modern Python package manager designed for speed and simplicity.

`uv pip install numpy`
**pixi:** A cross-platform package manager for Python and other languages.

`pixi add numpy`
The two main tools that install Python packages are `pip` and `conda`. Their functionality partially overlaps (e.g. both can install `numpy`), however, they can also work together. We’ll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can’t.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically “defaults” or “conda-forge”). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.

```
conda create -n my-env
conda activate my-env
conda install numpy
```
`pip install numpy`
**Tip:** Use a virtual environment for better dependency management

```
python -m venv my-env
source my-env/bin/activate  # macOS/Linux
my-env\Scripts\activate     # Windows
pip install numpy
```
Not recommended for most users, but available for convenience.

**macOS (Homebrew):**

`brew install numpy`
**Linux (APT):**

`sudo apt install python3-numpy`
**Windows (Chocolatey):**

`choco install numpy`
For advanced users and developers who want to customize or debug **NumPy**.

A word of warning: building Numpy from source can be a nontrivial exercise.
We recommend using binaries instead if those are available for your platform via one of the above methods.
For details on how to build from source, see [the building from source guide in the Numpy docs](https://numpy.org/devdocs/building/).

After installing NumPy, verify the installation by running the following in a Python shell or script:

```
import numpy as np
print(np.__version__)
```
This should print the installed version of NumPy without errors.

If your installation fails with the message below, see [Troubleshooting
ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!
Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```