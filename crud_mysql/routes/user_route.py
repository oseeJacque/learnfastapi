from fastapi import FastAPI, APIRouter
from sqlalchemy.exc import SQLAlchemyError

from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

#Get all users in data base 
@user.get("/users")
async def read_data():
    try:
        result = conn.execute(users.select()).fetchall()
        return {"users":f"{result}"}
    except SQLAlchemyError as e:
        return {"error":str(e)}


@user.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    try:
        result = conn.execute(users.select().where(users.c.id == user_id)).fetchall() 
        return {"data":f"{result}"} 
    except  SQLAlchemyError as e:
        return {"error":f"{str(e)}"}


@user.post("/users")
async def create_data(user: User):
    try :
        print(user)
        conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password))
        result = conn.execute(users.select()).fetchall()
        return {"message": f"{result}" }
    except SQLAlchemyError as e:
        return {"error":str(e)}


@user.put("/users/{user_id}")
async def update_data(user_id: int, user: User):
    conn.execute(users.update(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == user_id))
    return conn.execute(users.select()).fetchall()

@user.delete("/users/{user_id}")
async def delete_data(user_id:int):
    conn.execute(users.delete().where(users.c.id == user_id))
    return conn.execute(users.select()).fetchall()