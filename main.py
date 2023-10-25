from typing import Optional

from fastapi import FastAPI,Query
from fastapi.params import Body, Path
from enum import Enum

from models.items import Item

app = FastAPI()

#
# @app.get("/",description="This is the first endpoint of our api")
# async  def say_hello():
#     return {"Hello":"Everybody"}
#
# @app.put("/", description="No need parameters")
# async def say_hello_put():
#     return {"Put": "Methods"}
#
# @app.delete("/")
# async def delete_root():
#     return {"Delete":"Nothing to delete"}
#
# #Items
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         item_dict.update({"total_price": item.price + item.tax})
#     return item_dict
#
# @app.get("/items")
# async def read_item(q: Optional[str] = Query(None,min_length=2,max_length=10,title="Quantity",description="List length",alias="item_query")):
#     result = {"data": [{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},{"name": "rice"},]}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# ################### Post
# @app.post("/posts")
# async def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"message": "Posts created succeffully"}

#
# @app.put("/items/{item_id}")
# async def update_item(*,
#                       item_id: Optional[int] = Path(..., title="Id for item do you want change"),
#                       q:Optional[str] = None,
#                       item: Item = Body(...,description="All you want")
#                       ):
#     resultat = {"item_id": item_id}
#     if q:
#         resultat.update({"q":q})
#     if item:
#         resultat.update({"item": item})
#     return  resultat

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {
        "item_id": item_id,
        "item": item
    }
    return result