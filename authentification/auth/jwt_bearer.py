

from typing import Optional
from typing_extensions import Annotated, Doc
from fastapi import Request,HTTPException 
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

from auth.jwt_handle import decodeJWT 


class jwtBearer(HTTPBearer):
    def __init__(self,auto_Error :bool = True): 
        super(jwtBearer,self).__init__(auto_error = auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer,self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403,detail="Incalid or Expired Toke,")
            return credentials.credentials  
        else:
            raise HTTPException(status_code=403,detail="Incalid or Expired Toke,")  
        

    def verify_jwt(self,jwttoken : str):
        isTokenValid : bool = False 
        payload = decodeJWT(jwttoken)
        if payload:
            isTokenValid = True 
        return isTokenValid

    