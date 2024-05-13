from fastapi import FastAPI
from fastapi import Path
from fastapi import Body
from fastapi.encoders import jsonable_encoder

from typing import Annotated
import pprint

from models.item import Item

app = FastAPI()

# Update replacing with PUT
ITEMS = {
  "foo": {
    "name": "Foo",
    "price": 50.2
  },
  "bar": {
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
  },
  "baz": {
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
  }
}

@app.get("/items/{id}", response_model = Item, response_model_exclude_unset = True)
async def read_item(id: Annotated[str, Path()]) -> Item:
  return ITEMS[id]

"""
@app.put("/items/{id}", response_model = Item, response_model_exclude_unset = True)
async def update_item(
  id: Annotated[str, Path()],
  item: Annotated[Item, Body(embed = True)]
) -> Item:
  dict_item: dict[str, str] = jsonable_encoder(item)
  ITEMS[id] = dict_item
  return dict_item
"""

# Partial updates with PATCH
@app.put("/items/{id}", response_model = Item, response_model_exclude_unset = True)
async def update_item(
  id: Annotated[str, Path()],
  item: Annotated[Item, Body(embed = True)]
) -> Item:
  dict_stored_item = ITEMS[id]
  stored_item = Item(**dict_stored_item)

  dict_updating_item = item.model_dump(exclude_unset = True)
  updated_item = stored_item.model_copy(update = dict_updating_item)

  ITEMS[id] = jsonable_encoder(updated_item)
  return updated_item
