from pydantic import BaseModel

class Item(BaseModel):
  name: str | None = None
  description: str | None = None
  price: float | None = None
  tax: float = 10.5
  tags: list[str] = []
