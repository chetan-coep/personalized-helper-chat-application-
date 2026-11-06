---
id: "fastapi_050"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 50
source_url: "https://fastapi.tiangolo.com/tutorial/static-files"
language: "en"
retrieved_at: "2026-11-01 22:04:31"
content_hash: "e06f44aebd65200a9f999715934dde5450694c12d8909ca147e57ca9c31d8b14"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/static-files

---

# Static Files[¶](https://fastapi.tiangolo.com#static-files)

You can serve static files automatically from a directory using `StaticFiles`.

Tip

If you need to host a frontend, use `app.frontend()` instead, read about it in [Frontend](https://fastapi.tiangolo.com/frontend/).

`app.frontend()` uses `StaticFiles` underneath, with several additional advantages for frontends, like handling client-side routing.

## Use `StaticFiles`[¶](https://fastapi.tiangolo.com#use-staticfiles)

- Import `StaticFiles`.
- "Mount" a `StaticFiles()` instance in a specific path.

```
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
```
Technical Details

You could also use `from starlette.staticfiles import StaticFiles`.

**FastAPI** provides the same `starlette.staticfiles` as `fastapi.staticfiles` just as a convenience for you, the developer. But it actually comes directly from Starlette.

### What is "Mounting"[¶](https://fastapi.tiangolo.com#what-is-mounting)

"Mounting" means adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths.

This is different from using an `APIRouter` as a mounted application is completely independent. The OpenAPI and docs from your main application won't include anything from the mounted application, etc.

You can read more about this in the [Advanced User Guide](https://fastapi.tiangolo.com/advanced/).

## Details[¶](https://fastapi.tiangolo.com#details)

The first `"/static"` refers to the sub-path this "sub-application" will be "mounted" on. So, any path that starts with `"/static"` will be handled by it.

The `directory="static"` refers to the name of the directory that contains your static files.

The `name="static"` gives it a name that can be used internally by **FastAPI**.

All these parameters can be different than "`static`", adjust them to the needs and specific details of your own application.

## More info[¶](https://fastapi.tiangolo.com#more-info)

For more details and options check [Starlette's docs about Static Files](https://starlette.dev/staticfiles/).