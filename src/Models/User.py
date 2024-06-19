from pydantic import BaseModel,Field,EmailStr
import time

class User(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=5)
    email: EmailStr 
    date : str = Field(default=time.asctime())
class Login(BaseModel):
    email : EmailStr
    password: str