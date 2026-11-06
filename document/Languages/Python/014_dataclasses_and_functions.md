---
id: "python_014"
technology: "Python"
category: "Languages"
title: "Python Data Classes: dataclass Decorator and default_factory"
doc_order: 14
source_url: "https://docs.python.org/3/library/dataclasses.html"
language: "en"
retrieved_at: "2026-11-03 20:58:00"
content_hash: "python_dataclasses_014"
---

# Python Data Classes (dataclasses)

Source: https://docs.python.org/3/library/dataclasses.html

---

## What is a Dataclass in Python

The `dataclasses` module provides a decorator and functions for automatically generating special methods such as `__init__()`, `__repr__()`, and `__eq__()` on user-defined classes. It eliminates repetitive boilerplate code when defining classes whose primary purpose is storing state.

## Using default_factory for Mutable Fields

In Python, mutable default arguments (such as empty lists `[]` or dictionaries `{}`) cannot be used directly as default values in a class definition because the default instance would be shared across all instances of the class.

To provide default mutable objects safely, use `field(default_factory=...)`:

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class UserProfile:
    username: str
    email: str
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
    is_active: bool = True

# Usage:
user1 = UserProfile(username="alex", email="alex@example.com")
user1.tags.append("developer")

user2 = UserProfile(username="sam", email="sam@example.com")
# user2.tags is an independent empty list, NOT shared with user1!
print(user1.tags)  # ['developer']
print(user2.tags)  # []
```

## Key Dataclass Parameters & Features

- `field(default_factory=Callable)`: A zero-argument callable that will be called when a default value is needed for this field.
- `@dataclass(frozen=True)`: Makes instances immutable and hashable (attributes cannot be assigned after initialization).
- `@dataclass(order=True)`: Automatically generates comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`).
- `asdict(instance)`: Converts a dataclass instance into a standard Python dictionary.
- `astuple(instance)`: Converts a dataclass instance into a tuple.

```python
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float

coord = Coordinate(10.5, 20.0)
print(asdict(coord))  # {'x': 10.5, 'y': 20.0}
```

