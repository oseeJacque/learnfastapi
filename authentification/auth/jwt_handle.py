import time 
import jwt 
from decouple import config 

JWT_SECRET = config("secret") 
JWT_ALGORITHM = config("algorithm") 



# Function returns the generated Token (JWTs)
def token_response(token: str):
    return {
        "access token": token 
    } 

#Function used for signing th JWT string  
def signJWT(userID: str):
    payload = {
        "userID": userID, 
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token) 


#decodeur 
def decodeJWT(token: str):
    try:
        decod_token = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        return decod_token if decod_token['expires'] >= time.time() else None
    except:
        return {}