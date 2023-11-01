from fastapi import HTTPException,status
from passlib.context import CryptContext 
from dotenv import dotenv_values
pwd_content = CryptContext(schemes=['bcrypt'], deprecated = 'auto') 
config_credential = dotenv_values(".env")
import jwt
from models.models import User





def get_hashed_password (password):
    return pwd_content.hash(password) 


async def verify_token(token: str):
    try:
        payload = jwt.decode(token, config_credential['SECRET'],algorithm=["HS256"])
        user = await User.get(id = payload.get("id")) 

    except: 
        raise HTTPException (
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid Token", 
            headers= {"WWW.Authenticate": "Bearer"}
            ) 
    return user