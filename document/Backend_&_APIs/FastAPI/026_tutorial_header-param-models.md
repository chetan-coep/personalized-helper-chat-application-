---
id: "fastapi_026"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 26
source_url: "https://fastapi.tiangolo.com/tutorial/header-param-models"
language: "en"
retrieved_at: "2026-11-01 22:03:53"
content_hash: "ccd2526e84b482be71dcf415155e2248001b95cd8f72a9e20e4c784b1b20cce7"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/header-param-models

---

# Header Parameter Models[¶](https://fastapi.tiangolo.com#header-parameter-models)

If you have a group of related **header parameters**, you can create a **Pydantic model** to declare them.

This would allow you to **re-use the model** in **multiple places** and also to declare validations and metadata for all the parameters at once. 😎

Note

This is supported since FastAPI version `0.115.0`. 🤓

## Header Parameters with a Pydantic Model[¶](https://fastapi.tiangolo.com#header-parameters-with-a-pydantic-model)

Declare the **header parameters** that you need in a **Pydantic model**, and then declare the parameter as `Header`:

```
from typing import Annotated
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
@app.get("/items/")
async def read_items(headers: CommonHeaders = Header()):
    return headers
```
**FastAPI** will **extract** the data for **each field** from the **headers** in the request and give you the Pydantic model you defined.

## Check the Docs[¶](https://fastapi.tiangolo.com#check-the-docs)

You can see the required headers in the docs UI at `/docs`:

## Forbid Extra Headers[¶](https://fastapi.tiangolo.com#forbid-extra-headers)

In some special use cases (probably not very common), you might want to **restrict** the headers that you want to receive.

You can use Pydantic's model configuration to `forbid` any `extra` fields:

```
from typing import Annotated
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
@app.get("/items/")
async def read_items(headers: CommonHeaders = Header()):
    return headers
```
If a client tries to send some **extra headers**, they will receive an **error** response.

For example, if the client tries to send a `tool` header with a value of `plumbus`, they will receive an **error** response telling them that the header parameter `tool` is not allowed:

```
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["header", "tool"],
            "msg": "Extra inputs are not permitted",
            "input": "plumbus",
        }
    ]
}
```
## Disable Convert Underscores[¶](https://fastapi.tiangolo.com#disable-convert-underscores)

The same way as with regular header parameters, when you have underscore characters in the parameter names, they are **automatically converted to hyphens**.

For example, if you have a header parameter `save_data` in the code, the expected HTTP header will be `save-data`, and it will show up like that in the docs.

If for some reason you need to disable this automatic conversion, you can do it as well for Pydantic models for header parameters.

```
from typing import Annotated
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
@app.get("/items/")
async def read_items(
    headers: Annotated[CommonHeaders, Header(convert_underscores=False)],
):
    return headers
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
@app.get("/items/")
async def read_items(headers: CommonHeaders = Header(convert_underscores=False)):
    return headers
```
Warning

Before setting `convert_underscores` to `False`, bear in mind that some HTTP proxies and servers disallow the usage of headers with underscores.

## Combine Parameter Models[¶](https://fastapi.tiangolo.com#combine-parameter-models)

You can combine multiple header parameter models with individual header parameters and dependencies. Each model is extracted and validated independently, as explained for [query parameter models](https://fastapi.tiangolo.com/query-param-models/#combine-parameter-models).

Each model's `extra` configuration applies to all header parameters, including those declared in other models or dependencies. With `extra="forbid"`, any header outside that model is rejected. With `extra="allow"`, those headers are included as model extras.

Each model uses its own `Header(convert_underscores=...)` setting, both when reading the request and when generating OpenAPI. Explicit field aliases remain literal header names.

## Optional Header Parameter Models[¶](https://fastapi.tiangolo.com#optional-header-parameter-models)

Declare a header parameter model with `| None` and a default of `None` to make the group optional.

```
from typing import Annotated
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class ClientHeaders(BaseModel):
    x_client_name: str
    x_client_version: str
@app.get("/items/")
async def read_items(client: Annotated[ClientHeaders | None, Header()] = None):
    return client
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Header
from pydantic import BaseModel
app = FastAPI()
class ClientHeaders(BaseModel):
    x_client_name: str
    x_client_version: str
@app.get("/items/")
async def read_items(client: ClientHeaders | None = Header(default=None)):
    return client
```
If neither `x-client-name` nor `x-client-version` is sent, `client` is `None`. If either is sent, FastAPI validates the model and requires both fields.

The same rules for defaults, extra fields, and OpenAPI apply as for [optional query parameter models](https://fastapi.tiangolo.com/query-param-models/#optional-query-parameter-models).

Headers such as `Host` also follow the model's `extra` configuration. With `extra="allow"`, they make the model present even if neither declared field is supplied.

## Summary[¶](https://fastapi.tiangolo.com#summary)

You can use **Pydantic models** to declare **headers** in **FastAPI**. 😎