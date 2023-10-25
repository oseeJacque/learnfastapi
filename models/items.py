from pydantic import BaseModel
from typing import  Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "Avery nice Item",
                "price": 25.24,
                "tax": 1.59
            }
        }


