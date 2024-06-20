from fastapi import FastAPI
from src.router.userroute import router
from src.router.noteroute import router as noteroute
from dotenv import load_dotenv
import os
load_dotenv(override=True)
if not os.getenv("SECRET_NOTE"):
    print("please EXPORT encrypt key as EXPORT SECRET_NOTE for jwt token")
    exit()
    
app = FastAPI()


app.include_router(router)
app.include_router(noteroute)
