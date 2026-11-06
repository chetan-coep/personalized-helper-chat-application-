---
id: "fastapi_083"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 83
source_url: "https://fastapi.tiangolo.com/advanced/sub-applications"
language: "en"
retrieved_at: "2026-11-01 22:04:57"
content_hash: "fcd477c2a5259ca4ad9b1f075720b77e10b5fc3a661fa77a146c8429df413243"
---

# FastAPI

Source: https://fastapi.tiangolo.com/advanced/sub-applications

---

# Sub Applications - Mounts[¶](https://fastapi.tiangolo.com#sub-applications-mounts)

If you need to have two independent FastAPI applications, with their own independent OpenAPI and their own docs UIs, you can have a main app and "mount" one (or more) sub-application(s).

## Mounting a **FastAPI** application[¶](https://fastapi.tiangolo.com#mounting-a-fastapi-application)

"Mounting" means adding a completely "independent" application in a specific path, that then takes care of handling everything under that path, with the *path operations* declared in that sub-application.

### Top-level application[¶](https://fastapi.tiangolo.com#top-level-application)

First, create the main, top-level, **FastAPI** application, and its *path operations*:

```
from fastapi import FastAPI
app = FastAPI()
@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}
subapi = FastAPI()
@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}
app.mount("/subapi", subapi)
```
### Sub-application[¶](https://fastapi.tiangolo.com#sub-application)

Then, create your sub-application, and its *path operations*.

This sub-application is just another standard FastAPI application, but this is the one that will be "mounted":

```
from fastapi import FastAPI
app = FastAPI()
@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}
subapi = FastAPI()
@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}
app.mount("/subapi", subapi)
```
### Mount the sub-application[¶](https://fastapi.tiangolo.com#mount-the-sub-application)

In your top-level application, `app`, mount the sub-application, `subapi`.

In this case, it will be mounted at the path `/subapi`:

```
from fastapi import FastAPI
app = FastAPI()
@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}
subapi = FastAPI()
@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}
app.mount("/subapi", subapi)
```
### Check the automatic API docs[¶](https://fastapi.tiangolo.com#check-the-automatic-api-docs)

Now, run the `fastapi` command:

```
$ uv run fastapi dev
<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
And open the docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You will see the automatic API docs for the main app, including only its own *path operations*:

And then, open the docs for the sub-application, at [http://127.0.0.1:8000/subapi/docs](http://127.0.0.1:8000/subapi/docs).

You will see the automatic API docs for the sub-application, including only its own *path operations*, all under the correct sub-path prefix `/subapi`:

If you try interacting with any of the two user interfaces, they will work correctly, because the browser will be able to talk to each specific app or sub-app.

### Technical Details: `root_path`[¶](https://fastapi.tiangolo.com#technical-details-root-path)

When you mount a sub-application as described above, FastAPI will take care of communicating the mount path for the sub-application using a mechanism from the ASGI specification called a `root_path`.

That way, the sub-application will know to use that path prefix for the docs UI.

And the sub-application could also have its own mounted sub-applications and everything would work correctly, because FastAPI handles all these `root_path`s automatically.

You will learn more about the `root_path` and how to use it explicitly in the section about [Behind a Proxy](https://fastapi.tiangolo.com/behind-a-proxy/).