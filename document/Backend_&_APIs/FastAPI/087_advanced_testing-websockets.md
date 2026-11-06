---
id: "fastapi_087"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 87
source_url: "https://fastapi.tiangolo.com/advanced/testing-websockets"
language: "en"
retrieved_at: "2026-11-01 22:05:04"
content_hash: "1d8210b350a285014483a5b0ee07d0a7f4b421b43feb8321f39e983c829de660"
---

# FastAPI

Source: https://fastapi.tiangolo.com/advanced/testing-websockets

---

# Testing WebSockets[¶](https://fastapi.tiangolo.com#testing-websockets)

You can use the same `TestClient` to test WebSockets.

For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:

```
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
app = FastAPI()
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()
def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}
```
Note

For more details, check Starlette's documentation for [testing WebSockets](https://starlette.dev/testclient/#testing-websocket-sessions).