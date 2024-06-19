from fastapi import FastAPI
from src.router.userroute import router
from src.router.noteroute import router as noteroute
app = FastAPI()


app.include_router(router)
app.include_router(noteroute)
@app.post("/")
async def create_item():
    return "helo"