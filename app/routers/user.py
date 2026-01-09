from fastapi import APIRouter, Depends
from app.db.schema.user import UserOutput
from app.service.userService import UserService
from app.core.database import get_db
from app.core.security.jwtBearer import JWTBearer
from sqlalchemy.orm import Session

userRouter = APIRouter()
jwt_bearer = JWTBearer()

@userRouter.get("/me", response_model=UserOutput)
def get_current_user(user_id: int = Depends(jwt_bearer), db: Session = Depends(get_db)):
    """Get current authenticated user information (protected route)"""
    user_service = UserService(session=db)
    return user_service.get_user_by_id(user_id)
