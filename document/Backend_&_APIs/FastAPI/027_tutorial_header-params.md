---
id: "fastapi_027"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 27
source_url: "https://fastapi.tiangolo.com/tutorial/header-params"
language: "en"
retrieved_at: "2026-11-01 22:03:50"
content_hash: "c8d3ffee8ca450ea6f67e47734bee7f33100fe50ec5102d6524794d16a4b7e8d"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/header-params

---

# Header Parameters[¶](https://fastapi.tiangolo.com#header-parameters)

You can define Header parameters the same way you define `Query`, `Path` and `Cookie` parameters.

## Import `Header`[¶](https://fastapi.tiangolo.com#import-header)

First import `Header`:

```
from typing import Annotated
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
```
## Declare `Header` parameters[¶](https://fastapi.tiangolo.com#declare-header-parameters)

Then declare the header parameters using the same structure as with `Path`, `Query` and `Cookie`.

You can define the default value as well as all the extra validation or annotation parameters:

```
from typing import Annotated
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
```
Technical Details

`Header` is a "sister" class of `Path`, `Query` and `Cookie`. It also inherits from the same common `Param` class.

But remember that when you import `Query`, `Path`, `Header`, and others from `fastapi`, those are actually functions that return special classes.

Note

To declare headers, you need to use `Header`, because otherwise the parameters would be interpreted as query parameters.

## Automatic conversion[¶](https://fastapi.tiangolo.com#automatic-conversion)

`Header` has a little extra functionality on top of what `Path`, `Query` and `Cookie` provide.

Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (`-`).

But a variable like `user-agent` is invalid in Python.

So, by default, `Header` will convert the parameter names characters from underscore (`_`) to hyphen (`-`) to extract and document the headers.

Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake\_case").

So, you can use `user_agent` as you normally would in Python code, instead of needing to capitalize the first letters as `User_Agent` or something similar.

If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter `convert_underscores` of `Header` to `False`:

```
from typing import Annotated
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(
    strange_header: str | None = Header(default=None, convert_underscores=False),
):
    return {"strange_header": strange_header}
```
Warning

Before setting `convert_underscores` to `False`, bear in mind that some HTTP proxies and servers disallow the usage of headers with underscores.

## Duplicate headers[¶](https://fastapi.tiangolo.com#duplicate-headers)

It is possible to receive duplicate headers. That means, the same header with multiple values.

You can define those cases using a list in the type declaration.

You will receive all the values from the duplicate header as a Python `list`.

For example, to declare a header of `X-Token` that can appear more than once, you can write:

```
from typing import Annotated
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/items/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}
```
If you communicate with that *path operation* sending two HTTP headers like:

```
X-Token: foo
X-Token: bar
```
The response would be like:

```
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
```
## Recap[¶](https://fastapi.tiangolo.com#recap)

Declare headers with `Header`, using the same common pattern as `Query`, `Path` and `Cookie`.

And don't worry about underscores in your variables, **FastAPI** will take care of converting them.