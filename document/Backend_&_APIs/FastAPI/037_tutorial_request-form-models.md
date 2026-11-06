---
id: "fastapi_037"
technology: "FastAPI"
category: "Backend & APIs"
title: "FastAPI"
doc_order: 37
source_url: "https://fastapi.tiangolo.com/tutorial/request-form-models"
language: "en"
retrieved_at: "2026-11-01 22:03:59"
content_hash: "7e12407f20d09574047984cedddb27e240dc70da912034064962ce717b7638b2"
---

# FastAPI

Source: https://fastapi.tiangolo.com/tutorial/request-form-models

---

# Form Models[¶](https://fastapi.tiangolo.com#form-models)

You can use **Pydantic models** to declare **form fields** in FastAPI.

Note

To use forms, first install [`python-multipart`](https://github.com/Kludex/python-multipart).

Add it to your project:

```
$ uv add python-multipart
```
Note

This is supported since FastAPI version `0.113.0`. 🤓

## Pydantic Models for Forms[¶](https://fastapi.tiangolo.com#pydantic-models-for-forms)

You just need to declare a **Pydantic model** with the fields you want to receive as **form fields**, and then declare the parameter as `Form`:

```
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class FormData(BaseModel):
    username: str
    password: str
@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class FormData(BaseModel):
    username: str
    password: str
@app.post("/login/")
async def login(data: FormData = Form()):
    return data
```
**FastAPI** will **extract** the data for **each field** from the **form data** in the request and give you the Pydantic model you defined.

For [HTML checkboxes](https://fastapi.tiangolo.com/request-forms/#boolean-form-fields), declare boolean fields with a default of `False`.

## Check the Docs[¶](https://fastapi.tiangolo.com#check-the-docs)

You can verify it in the docs UI at `/docs`:

## Forbid Extra Form Fields[¶](https://fastapi.tiangolo.com#forbid-extra-form-fields)

In some special use cases (probably not very common), you might want to **restrict** the form fields to only those declared in the Pydantic model. And **forbid** any **extra** fields.

Note

This is supported since FastAPI version `0.114.0`. 🤓

You can use Pydantic's model configuration to `forbid` any `extra` fields:

```
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}
@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}
@app.post("/login/")
async def login(data: FormData = Form()):
    return data
```
If a client tries to send some extra data, they will receive an **error** response.

For example, if the client tries to send the form fields:

- `username`: `Rick`
- `password`: `Portal Gun`
- `extra`: `Mr. Poopybutthole`

They will receive an error response telling them that the field `extra` is not allowed:

```
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["body", "extra"],
            "msg": "Extra inputs are not permitted",
            "input": "Mr. Poopybutthole"
        }
    ]
}
```
## Combine Form Models[¶](https://fastapi.tiangolo.com#combine-form-models)

You can combine multiple form models with individual `Form` parameters.

```
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Profile(BaseModel):
    name: str
class Preferences(BaseModel):
    tags: list[str] = []
@app.post("/profiles/")
async def create_profile(
    profile: Annotated[Profile, Form()],
    preferences: Annotated[Preferences, Form()],
    token: Annotated[str, Form()],
):
    return {"profile": profile, "preferences": preferences, "token": token}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Profile(BaseModel):
    name: str
class Preferences(BaseModel):
    tags: list[str] = []
@app.post("/profiles/")
async def create_profile(
    profile: Profile = Form(),
    preferences: Preferences = Form(),
    token: str = Form(),
):
    return {"profile": profile, "preferences": preferences, "token": token}
```
The client sends `name`, `tags`, and `token` as form fields. Each model validates the form fields independently.

Each model's `extra` configuration applies to all form fields, including fields and files declared in other parameters or dependencies. With `extra="forbid"`, any field outside that model is rejected. With `extra="allow"`, those fields are included as model extras.

If multiple declarations use the same form field name, each validates that field's value. Use compatible types and constraints for shared fields so the OpenAPI schema can describe them consistently.

## Optional Form Models[¶](https://fastapi.tiangolo.com#optional-form-models)

Declare a form model with `| None` and a default of `None` to make the group optional.

```
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Profile(BaseModel):
    name: str
    age: int
@app.post("/profiles/")
async def create_profile(
    token: Annotated[str, Form()],
    profile: Annotated[Profile | None, Form()] = None,
):
    return {"token": token, "profile": profile}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Profile(BaseModel):
    name: str
    age: int
@app.post("/profiles/")
async def create_profile(
    token: str = Form(),
    profile: Profile | None = Form(default=None),
):
    return {"token": token, "profile": profile}
```
If neither `name` nor `age` is sent, `profile` is `None`. If either is sent, FastAPI validates the model and requires both fields. An empty submitted value also counts as supplying a field.

Using `| None` without a default still makes the parameter required.

Extra fields follow the model's `extra` configuration. Ignored extras do not make the model present.

An optional model containing only unchecked checkboxes is omitted. Send a value such as `enabled=false` to supply it explicitly.

## Optional Unions of Form Models[¶](https://fastapi.tiangolo.com#optional-unions-of-form-models)

You can also use an optional union of models.

```
from typing import Annotated, Literal
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Person(BaseModel):
    kind: Literal["person"]
    name: str
class Company(BaseModel):
    kind: Literal["company"]
    company_name: str
@app.post("/contacts/")
async def create_contact(
    contact: Annotated[Person | Company | None, Form(discriminator="kind")] = None,
):
    return contact
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from typing import Literal
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Person(BaseModel):
    kind: Literal["person"]
    name: str
class Company(BaseModel):
    kind: Literal["company"]
    company_name: str
@app.post("/contacts/")
async def create_contact(
    contact: Person | Company | None = Form(default=None, discriminator="kind"),
):
    return contact
```
If no form fields are sent, `contact` is `None`. Send `kind=person` with `name`, or `kind=company` with `company_name`. The discriminator selects which model to validate.

## Combine Unions of Form Models[¶](https://fastapi.tiangolo.com#combine-unions-of-form-models)

You can combine unions with other form models, individual `Form` parameters, and `File` parameters. Each union is validated independently.

```
from typing import Annotated, Literal
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Person(BaseModel):
    contact_type: Literal["person"]
    name: str
class Company(BaseModel):
    contact_type: Literal["company"]
    company_name: str
class Email(BaseModel):
    notification_type: Literal["email"]
    email: str
class SMS(BaseModel):
    notification_type: Literal["sms"]
    phone: str
@app.post("/contacts/")
async def create_contact(
    contact: Annotated[Person | Company, Form(discriminator="contact_type")],
    token: Annotated[str, Form()],
    notification: Annotated[
        Email | SMS | None, Form(discriminator="notification_type")
    ] = None,
):
    return {"contact": contact, "notification": notification, "token": token}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from typing import Literal
from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Person(BaseModel):
    contact_type: Literal["person"]
    name: str
class Company(BaseModel):
    contact_type: Literal["company"]
    company_name: str
class Email(BaseModel):
    notification_type: Literal["email"]
    email: str
class SMS(BaseModel):
    notification_type: Literal["sms"]
    phone: str
@app.post("/contacts/")
async def create_contact(
    contact: Person | Company = Form(discriminator="contact_type"),
    token: str = Form(),
    notification: Email | SMS | None = Form(
        default=None, discriminator="notification_type"
    ),
):
    return {"contact": contact, "notification": notification, "token": token}
```
Send all fields in the same form. For example, send `contact_type=person`, `name=Rick`, `notification_type=email`, `email=rick@example.com`, and `token=secret`.

Omit the notification fields to leave `notification` as `None`.

## Form Models and Files[¶](https://fastapi.tiangolo.com#form-models-and-files)

You can also combine a form model with [file parameters](https://fastapi.tiangolo.com/request-files/).

```
from typing import Annotated
from fastapi import FastAPI, Form, UploadFile
from pydantic import BaseModel
app = FastAPI()
class Profile(BaseModel):
    name: str
@app.post("/profiles/")
async def create_profile(profile: Annotated[Profile, Form()], avatar: UploadFile):
    return {"profile": profile, "filename": avatar.filename}
```
## 🤓 Other versions and variants

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
app = FastAPI()
class Profile(BaseModel):
    name: str
@app.post("/profiles/")
async def create_profile(profile: Profile = Form(), avatar: UploadFile = File()):
    return {"profile": profile, "filename": avatar.filename}
```
Here the client sends the `name` field and the `avatar` file using `multipart/form-data`.

## Summary[¶](https://fastapi.tiangolo.com#summary)

You can use Pydantic models to declare form fields in FastAPI. 😎