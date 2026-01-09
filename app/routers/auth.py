from fastapi import APIRouter, Depends
from app.db.schema.user import UserInCreate, UserInLogin, UserWithToken
from app.service.userService import UserService
from app.core.database import get_db
from sqlalchemy.orm import Session

authRouter = APIRouter()

@authRouter.post("/login", response_model=UserWithToken)
def login(loginDetails: UserInLogin, db: Session = Depends(get_db)):
    """Authenticate user and return JWT token"""
    user_service = UserService(session=db)
    return user_service.authenticate_user(loginDetails.email, loginDetails.password)

@authRouter.post("/signup", response_model=UserWithToken)
def signUp(signUpDetails: UserInCreate, db: Session = Depends(get_db)):
    """Register new user and return JWT token"""
    user_service = UserService(session=db)
    return user_service.create_user(signUpDetails)