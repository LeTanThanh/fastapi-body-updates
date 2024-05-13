from fastapi import FastAPI
from fastapi import Path
from fastapi import Body
from fastapi.encoders import jsonable_encoder

from typing import Annotated

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

@app.put("/items/{id}", response_model = Item, response_model_exclude_unset = True)
async def update_item(
  id: Annotated[str, Path()],
  item: Annotated[Item, Body(embed = True)]
) -> Item:
  dict_item: dict[str, str] = jsonable_encoder(item)
  ITEMS[id] = dict_item
  return dict_item
