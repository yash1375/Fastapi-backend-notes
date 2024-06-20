from fastapi import APIRouter,Response,status,Depends
from ..Models.User import User,Login
from ..db.db import Connect_mongo
import bcrypt
import jwt  
from ..Dependencies.Dependencies import verify_token
from bson.objectid import ObjectId

from dotenv import load_dotenv
import os
load_dotenv()

secret = os.getenv("SECRET_NOTE")

router = APIRouter(prefix="/user")
@router.post('/createuser')
def createnotes(user:User,response:Response):
    data = Connect_mongo()["users"]
    email = data.find_one({"email": user.email},{"email": 1,"_id": False})
    if email != None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "email already exits"
    salt = bcrypt.gensalt()
    user.password = bcrypt.hashpw(user.password.encode('utf-8'),salt)
    data.insert_one(dict(user))
    response.status_code = status.HTTP_201_CREATED
    return "success"

@router.get('/login')
def login(login:Login,response:Response):
    data = Connect_mongo()["users"]
    data = data.find_one({"email": login.email},{"email": 1,"password": 1})
    if data == None or not bcrypt.checkpw(login.password.encode('utf-8'),data['password']):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return("wrong pass or email")
    login_token_json = {
        "id":str(data["_id"])
    }
    auth_token = jwt.encode(login_token_json,secret)
    response.status_code = status.HTTP_200_OK
    response.headers["auth_token"] = auth_token
    return {"auth_token":auth_token}

@router.get('/getuser')
def getuser(response:Response, id: dict = Depends(verify_token)):
    if(not id):
         return
    data = Connect_mongo()["users"]
    user = data.find_one(ObjectId(id["id"]),{"password":0,"_id":0})
    response.status_code = status.HTTP_200_OK
    print("succues")