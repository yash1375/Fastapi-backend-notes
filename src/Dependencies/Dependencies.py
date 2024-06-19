from typing import Annotated
from fastapi import Header,HTTPException
import jwt

secret = "ineedtochangethis@e43"
async def verify_token(auth_token: Annotated[str, Header()]):
    try:
        id = jwt.decode(auth_token,secret,algorithms="'HS256'")
        return id
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401,detail="wrong token")
