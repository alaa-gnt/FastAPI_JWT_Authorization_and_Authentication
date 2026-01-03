from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.routers.auth import authRouter

@asynccontextmanager
async def lifespan(app : FastAPI):
     # instialize DB at Start
     create_tables()
     yield # sepration point 

app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter , tags=['auth'] , prefix='/auth' )
# /auth/login
# /auth/signup
@app.get("/health")
def health_check():
    return {"status" : 'running'}