import uvicorn 
from fastapi import Body, FastAPI,Depends
from auth.jwt_bearer import jwtBearer
from auth.jwt_handle import signJWT

from models.schema import PostSchema, UserLoginSchema, UserSchema 


posts = [
    {
        "id":1, 
        "titleb":"penguis", 
        "content": "Penguis are good"
    }, 
    {
        "id":2, 
        "titleb":"penguis", 
        "content": "Penguis are good"
    },
    {
        "id":3, 
        "titleb":"penguis", 
        "content": "Penguis are good"
    },
    {
        "id":4, 
        "titleb":"penguis", 
        "content": "Penguis are good"
    },
    {
        "id":5, 
        "titleb":"penguis", 
        "content": "Penguis are good"
    }
] 

users = []
app = FastAPI() 

#1-great hello 
@app.get("/",tags=["Great"])
async def great_all():
    return {"Great":"Hello word"} 


#2-get all post 
@app.get("/posts",tags=['posts'],dependencies=[Depends(jwtBearer())])
async def get_all_posts():
    return {"data":f'{posts}'} 

#3-get post by id 
@app.get('/posts/{post_id}',tags=['posts'],dependencies=[Depends(jwtBearer())])
async def get_post_by_id(post_id:int):
    if post_id > len(posts):
        return {"data":[]} 
    else:
        return {"data": posts[post_id-1]} 
    

#4-create a new post 
@app.post('/posts',tags=["posts"],dependencies=[Depends(jwtBearer())])
async def create_post(post:PostSchema):
    post.id =len(posts)+1 
    posts.append(post.dict())
    return {"info": "Post added sucessfully"} 


################################################ 
@app.post("/users/signUp",tags=["Users"])
async def create_user(user : UserSchema = Body(default = None)):
    users.append(user)
    return signJWT(user.email) 


def check_user(data : UserLoginSchema):
    for user in users :
        if user.email == data.email and user.password == data.password:
            return True 
    return False


#User login 
@app.post("/users/login",tags=["Users"])
async def user_login(user: UserLoginSchema = Body()):
    print(user)
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error":"This user does not exist"
        } 
    

@app.get("/users",tags=["Users"], dependencies= [Depends(jwtBearer())])
async def all_user():
    result = users 
    return {
        "data": result
    }