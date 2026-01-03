from fastapi import APIRouter
from app.db.schema.user import UserInCreate, UserInLogin 

authRouter = APIRouter()

@authRouter.post("/login")
def login(loginDetailes : UserInLogin):
    return{"data":loginDetailes}

@authRouter.post("/Signup")
def signUp(signUpDetails : UserInCreate):
    return {"data":signUpDetails}

