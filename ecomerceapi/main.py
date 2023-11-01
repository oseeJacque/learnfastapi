from fastapi import FastAPI
from routers.aut_router import authApp
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

app.include_router(authApp)

register_tortoise(
  app=app, 
  db_url = "sqlite://database.sqlite3", 
  modules= {"models": ["models.models"]}, 
  generate_schemas=True, 
  add_exception_handlers=True
 )