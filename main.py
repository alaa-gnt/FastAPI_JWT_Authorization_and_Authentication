from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables

@asynccontextmanager
async def lifespan(app : FastAPI):
     # instialize DB at Start
     create_tables()
     yield # sepration point 

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status" : 'running'}