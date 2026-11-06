---
id: "fastapi_086"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 86
source_url: "https://fastapi.tiangolo.com/advanced/testing-events"
language: "en"
retrieved_at: "2026-11-01 22:05:05"
content_hash: "c72220e89837f862a066c9814a4e383a08361a3b26297938229d6e5250ee0ab5"
---

# FastAPI

Source: https://fastapi.tiangolo.com/advanced/testing-events

---

# Testing Events: lifespan and startup - shutdown[¶](https://fastapi.tiangolo.com#testing-events-lifespan-and-startup-shutdown)

When you need `lifespan` to run in your tests, you can use the `TestClient` with a `with` statement:

```
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.testclient import TestClient
items = {}
@asynccontextmanager
async def lifespan(app: FastAPI):
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}
    yield
    # clean up items
    items.clear()
app = FastAPI(lifespan=lifespan)
@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]
def test_read_items():
    # Before the lifespan starts, "items" is still empty
    assert items == {}
    with TestClient(app) as client:
        # Inside the "with TestClient" block, the lifespan starts and items added
        assert items == {"foo": {"name": "Fighters"}, "bar": {"name": "Tenders"}}
        response = client.get("/items/foo")
        assert response.status_code == 200
        assert response.json() == {"name": "Fighters"}
        # After the requests is done, the items are still there
        assert items == {"foo": {"name": "Fighters"}, "bar": {"name": "Tenders"}}
    # The end of the "with TestClient" block simulates terminating the app, so
    # the lifespan ends and items are cleaned up
    assert items == {}
```
You can read more details about the ["Running lifespan in tests in the official Starlette documentation site."](https://starlette.dev/lifespan/#running-lifespan-in-tests)

For the deprecated `startup` and `shutdown` events, you can use the `TestClient` as follows:

```
from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()
items = {}
@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}
@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]
def test_read_items():
    with TestClient(app) as client:
        response = client.get("/items/foo")
        assert response.status_code == 200
        assert response.json() == {"name": "Fighters"}
```