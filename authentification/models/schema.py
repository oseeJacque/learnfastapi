from pydantic import BaseModel,Field,EmailStr 

class PostSchema(BaseModel):
    id: int = Field(default=None) 
    title: str=Field(default=None) 
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title":"Some title about animals ", 
                "content": "Some content about animals"
            }
        } 


class UserSchema ( BaseModel):
    fullname : str =Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default= None)

    class config:
        the_shema = {
            "user_demo": {
                "fullname": "SOKE Osée", 
                "email" : "oseesoke@gmail.com",
                "password" : "azerty"
            }
        }

class UserLoginSchema ( BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default= None)

    class config:
        the_shema = {
            "user_demo": {
                "email" : "oseesoke@gmail.com",
                "password" : "azerty"
            }
        }