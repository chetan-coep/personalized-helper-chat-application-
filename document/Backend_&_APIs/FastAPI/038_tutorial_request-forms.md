---
id: "fastapi_038"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 38
source_url: "https://fastapi.tiangolo.com/tutorial/request-forms"
language: "en"
retrieved_at: "2026-11-01 22:03:58"
content_hash: "879db85f6ebf0d15ca37e852379a9d552bd7c22d8f8953250c7884a35eef9ea6"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/request-forms

---

# Form Data[¶](https://fastapi.tiangolo.com#form-data)

When you need to receive form fields instead of JSON, you can use `Form`.

Note

To use forms, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```
## Import `Form`[¶](https://fastapi.tiangolo.com#import-form)

Import `Form` from `fastapi`:

```
from typing import Annotated
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```
## Define `Form` parameters[¶](https://fastapi.tiangolo.com#define-form-parameters)

Create form parameters the same way you would for `Body` or `Query`:

```
from typing import Annotated
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```
For example, in one of the ways the OAuth2 specification can be used (called "password flow") it is required to send a `username` and `password` as form fields.

The spec requires the fields to be exactly named `username` and `password`, and to be sent as form fields, not JSON.

With `Form` you can declare the same configurations as with `Body` (and `Query`, `Path`, `Cookie`), including validation, examples, an alias (e.g. `user-name` instead of `username`), etc.

Note

`Form` is a class that inherits directly from `Body`.

Tip

To declare form bodies, you need to use `Form` explicitly, because without it the parameters would be interpreted as query parameters or body (JSON) parameters.

## Boolean Form Fields[¶](https://fastapi.tiangolo.com#boolean-form-fields)

Browsers omit unchecked checkboxes when submitting HTML forms. Declare a boolean form parameter with a default of `False` to receive `False` when unchecked:

```
from typing import Annotated
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/preferences/")
async def update_preferences(subscribe: Annotated[bool, Form()] = False):
    return {"subscribe": subscribe}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/preferences/")
async def update_preferences(subscribe: bool = Form(default=False)):
    return {"subscribe": subscribe}
```
A checked checkbox sends its value, which defaults to `"on"`. **FastAPI** accepts `"on"` as `True`.

## About "Form Fields"[¶](https://fastapi.tiangolo.com#about-form-fields)

The way HTML forms (`<form></form>`) send the data to the server normally uses a "special" encoding for that data, it's different from JSON.

**FastAPI** will make sure to read that data from the right place instead of JSON.

Technical Details

Data from forms is normally encoded using the "media type" `application/x-www-form-urlencoded`.

But when the form includes files, it is encoded as `multipart/form-data`. You'll read about handling files in the next chapter.

You can use `Form(media_type="multipart/form-data")` to describe a multipart form in OpenAPI. Setting it on one parameter is enough when combining form parameters or models.

If you want to read more about these encodings and form fields, head to the [MDN web docs for `POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST).

Warning

You can declare multiple `Form` parameters in a *path operation*, but you can't also declare `Body` fields that you expect to receive as JSON, as the request will have the body encoded using `application/x-www-form-urlencoded` instead of `application/json`.

This is not a limitation of **FastAPI**, it's part of the HTTP protocol.

## Recap[¶](https://fastapi.tiangolo.com#recap)

Use `Form` to declare form data input parameters.