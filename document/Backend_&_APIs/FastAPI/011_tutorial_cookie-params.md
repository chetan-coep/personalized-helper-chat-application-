---
id: "fastapi_011"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 11
source_url: "https://fastapi.tiangolo.com/tutorial/cookie-params"
language: "en"
retrieved_at: "2026-11-01 22:03:49"
content_hash: "ae5e2dafaa169d9a9b79fd3e9db3addd9df2839004d3049d979c3b9c9720dc4c"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/cookie-params

---

# Cookie Parameters[¶](https://fastapi.tiangolo.com#cookie-parameters)

You can define Cookie parameters the same way you define `Query` and `Path` parameters.

## Import `Cookie`[¶](https://fastapi.tiangolo.com#import-cookie)

First import `Cookie`:

```
from typing import Annotated
from fastapi import Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
```
## Declare `Cookie` parameters[¶](https://fastapi.tiangolo.com#declare-cookie-parameters)

Then declare the cookie parameters using the same structure as with `Path` and `Query`.

You can define the default value as well as all the extra validation or annotation parameters:

```
from typing import Annotated
from fastapi import Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
```
Technical Details

`Cookie` is a "sister" class of `Path` and `Query`. It also inherits from the same common `Param` class.

But remember that when you import `Query`, `Path`, `Cookie` and others from `fastapi`, those are actually functions that return special classes.

Note

To declare cookies, you need to use `Cookie`, because otherwise the parameters would be interpreted as query parameters.

Note

Have in mind that, as **browsers handle cookies** in special ways and behind the scenes, they **don't** easily allow **JavaScript** to touch them.

If you go to the **API docs UI** at `/docs` you will be able to see the **documentation** for cookies for your *path operations*.

But even if you **fill the data** and click "Execute", because the docs UI works with **JavaScript**, the cookies won't be sent, and you will see an **error** message as if you didn't write any values.

## Recap[¶](https://fastapi.tiangolo.com#recap)

Declare cookies with `Cookie`, using the same common pattern as `Query` and `Path`.