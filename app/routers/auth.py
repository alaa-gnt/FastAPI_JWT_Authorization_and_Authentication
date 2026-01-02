from fastapi import APIRouter

authRouter = APIRouter()

@authRouter.post("./login")
def login():
    return{"data":"login"}

@authRouter.post("./Signup")
def signUp():
    return {"data":"signed up"}

