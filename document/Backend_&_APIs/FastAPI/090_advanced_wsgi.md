---
id: "fastapi_090"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 90
source_url: "https://fastapi.tiangolo.com/advanced/wsgi"
language: "en"
retrieved_at: "2026-11-01 22:05:13"
content_hash: "7f36918006db641330df70d4c9df815943e06016500e22def027c276f9fbe8db"
---

# FastAPI

Source: https://fastapi.tiangolo.com/advanced/wsgi

---

# Including WSGI - Flask, Django, others[¶](https://fastapi.tiangolo.com#including-wsgi-flask-django-others)

You can mount WSGI applications as you saw with [Sub Applications - Mounts](https://fastapi.tiangolo.com/sub-applications/), [Behind a Proxy](https://fastapi.tiangolo.com/behind-a-proxy/).

For that, you can use the `WSGIMiddleware` and use it to wrap your WSGI application, for example, Flask, Django, etc.

## Using `WSGIMiddleware`[¶](https://fastapi.tiangolo.com#using-wsgimiddleware)

Note

This requires adding `a2wsgi` to your project, for example with `uv add a2wsgi`.

You need to import `WSGIMiddleware` from `a2wsgi`.

Then wrap the WSGI (e.g. Flask) app with the middleware.

And then mount that under a path.

```
from a2wsgi import WSGIMiddleware
from fastapi import FastAPI
from flask import Flask, request
from markupsafe import escape
flask_app = Flask(__name__)
@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"
app = FastAPI()
@app.get("/v2")
def read_main():
    return {"message": "Hello World"}
app.mount("/v1", WSGIMiddleware(flask_app))
```
Note

Previously, it was recommended to use `WSGIMiddleware` from `fastapi.middleware.wsgi`, but it is now deprecated.

It's advised to use the `a2wsgi` package instead. The usage remains the same.

Just ensure that you have the `a2wsgi` package installed and import `WSGIMiddleware` correctly from `a2wsgi`.

## Check it[¶](https://fastapi.tiangolo.com#check-it)

Now, every request under the path `/v1/` will be handled by the Flask application.

And the rest will be handled by **FastAPI**.

If you run it and go to [http://localhost:8000/v1/](http://localhost:8000/v1/) you will see the response from Flask:

```
Hello, World from Flask!
```
And if you go to [http://localhost:8000/v2](http://localhost:8000/v2) you will see the response from FastAPI:

```
{
    "message": "Hello World"
}
```