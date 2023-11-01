from fastapi import Body, FastAPI, APIRouter,HTTPException,status,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.models import user_pydanticIn,User
from utils.utils import get_hashed_password, verify_token 


authApp = APIRouter() 
templates = Jinja2Templates(directory="templates")

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


@authApp.get("/account/verification", response_class = HTMLResponse, tags=["Account"])
async def email_verification(request:Request, token: str):
    user = await verify_token(token=token) 

    if user and not user.is_verified:
        user.is_verified = True 
        await user.save()
        return templates.TemplateResponse("verification.html",{"request":request,"username": user.username}) 
    
    raise HTTPException (
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid Token or expired token ", 
            headers= {"WWW.Authenticate": "Bearer"}
            ) 
    

    
         

#toceyat643@undewp.com
