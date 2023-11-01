
from tortoise.contrib.fastapi import register_tortoise
from main import app


register_tortoise(
  app=app, 
  db_url = "sqlite://database.sqlite3", 
  modules= {"models": ["models"]}, 
  generate_schemas=True, 
  add_exception_handlers=True
 )