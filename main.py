from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.routers.auth import authRouter
from app.routers.user import userRouter

@asynccontextmanager
async def lifespan(app : FastAPI):
     # instialize DB at Start
     create_tables()
     yield # sepration point 

app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter , tags=['auth'] , prefix='/auth' )
app.include_router(router=userRouter , tags=['user'] , prefix='/user' )
# /auth/login
# /auth/signup
# /user/me (protected)
@app.get("/health")
def health_check():
    return {"status" : 'running'}