---
id: "fastapi_039"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 39
source_url: "https://fastapi.tiangolo.com/tutorial/request-forms-and-files"
language: "en"
retrieved_at: "2026-11-01 22:04:01"
content_hash: "604f476b3fad95922c1cb893272e7405db56a83aae0055d2f876910ee6a7a0fd"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/request-forms-and-files

---

# Request Forms and Files[¶](https://fastapi.tiangolo.com#request-forms-and-files)

You can define files and form fields at the same time using `File` and `Form`.

Note

To receive uploaded files and/or form data, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```
## Import `File` and `Form`[¶](https://fastapi.tiangolo.com#import-file-and-form)

```
from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile
app = FastAPI()
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, File, Form, UploadFile
app = FastAPI()
@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```
## Define `File` and `Form` parameters[¶](https://fastapi.tiangolo.com#define-file-and-form-parameters)

Create file and form parameters the same way you would for `Body` or `Query`:

```
from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile
app = FastAPI()
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, File, Form, UploadFile
app = FastAPI()
@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```
The files and form fields will be uploaded as form data and you will receive the files and form fields.

And you can declare some of the files as `bytes` and some as `UploadFile`.

Warning

You can declare multiple `File` and `Form` parameters in a *path operation*, but you can't also declare `Body` fields that you expect to receive as JSON, as the request will have the body encoded using `multipart/form-data` instead of `application/json`.

This is not a limitation of **FastAPI**, it's part of the HTTP protocol.

## Recap[¶](https://fastapi.tiangolo.com#recap)

Use `File` and `Form` together when you need to receive data and files in the same request.