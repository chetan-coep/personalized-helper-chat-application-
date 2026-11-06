---
id: "fastapi_076"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 76
source_url: "https://fastapi.tiangolo.com/advanced/response-headers"
language: "en"
retrieved_at: "2026-11-01 22:04:45"
content_hash: "5430d10dc1c4327f87764e7deae752613a5deb93e3a7e2482a361f76d348aa6d"
---

# FastAPI

Source: https://fastapi.tiangolo.com/advanced/response-headers

---

# Response Headers[¶](https://fastapi.tiangolo.com#response-headers)

## Use a `Response` parameter[¶](https://fastapi.tiangolo.com#use-a-response-parameter)

You can declare a parameter of type `Response` in your *path operation function* (as you can do for cookies).

And then you can set headers in that *temporary* response object.

```
from fastapi import FastAPI, Response
app = FastAPI()
@app.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}
```
And then you can return any object you need, as you normally would (a `dict`, a database model, etc).

And if you declared a `response_model`, it will still be used to filter and convert the object you returned.

**FastAPI** will use that *temporary* response to extract the headers (also cookies and status code), and will put them in the final response that contains the value you returned, filtered by any `response_model`.

You can also declare the `Response` parameter in dependencies, and set headers (and cookies) in them.

## Return a `Response` directly[¶](https://fastapi.tiangolo.com#return-a-response-directly)

You can also add headers when you return a `Response` directly.

Create a response as described in [Return a Response Directly](https://fastapi.tiangolo.com/response-directly/) and pass the headers as an additional parameter:

```
from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()
@app.get("/headers/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)
```
Technical Details

You could also use `from starlette.responses import Response` or `from starlette.responses import JSONResponse`.

**FastAPI** provides the same `starlette.responses` as `fastapi.responses` just as a convenience for you, the developer. But most of the available responses come directly from Starlette.

And as the `Response` can be used frequently to set headers and cookies, **FastAPI** also provides it at `fastapi.Response`.

## Custom Headers[¶](https://fastapi.tiangolo.com#custom-headers)

Keep in mind that custom proprietary headers can be added [using the `X-` prefix](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

But if you have custom headers that you want a client in a browser to be able to see, you need to add them to your CORS configurations (read more in [CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/)), using the parameter `expose_headers` documented in [Starlette's CORS docs](https://starlette.dev/middleware/#corsmiddleware).