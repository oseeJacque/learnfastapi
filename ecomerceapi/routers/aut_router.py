from fastapi import Body, FastAPI, APIRouter,HTTPException,status
from models.models import user_pydanticIn,User
from utils.utils import get_hashed_password

authApp = APIRouter() 

@authApp.get("/Greet")
async def greet():
    return {
        "Hello": "World"
    } 
#User registration 
@authApp.post("/account/registration",tags=["Account"])
async def user_registration(user:user_pydanticIn):
    try:
        user_info = user.dict(exclude_unset = True) 
        user_info["password"] = get_hashed_password(user_info["password"]) 
        user_obj = await User.create(**user_info)
        new_user = await user_pydanticIn.from_tortoise_orm(user_obj) 
        return {
            "status": "ok", 
            "data": "Compte created successfully.Check your email to finish registration process"
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")

    
         

#toceyat643@undewp.com
