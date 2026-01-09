from app.db.repository.userRepo import UserRepository
from app.db.schema.user import UserOutput , UserInCreate , UserWithToken
from app.core.security.authHandler import AuthHandler
from app.core.security.hashHelper import hashHelper
from sqlalchemy.orm import Session
from fastapi import HTTPException

class UserService:
    def __init__(self , session : Session):
        self.__userRespository = UserRepository(session=session)
    
    def create_user(self, user_data: UserInCreate) -> UserWithToken:
        """Create a new user with hashed password and return JWT token"""
        # Check if user already exists
        if self.__userRespository.user_exist_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Hash the password
        hashed_password = hashHelper.get_password_hash(user_data.password)
        
        # Create new user data with hashed password
        user_data_dict = user_data.model_dump()
        user_data_dict['password'] = hashed_password
        user_create = UserInCreate(**user_data_dict)
        
        # Save to database
        new_user = self.__userRespository.create_user(user_create)
        
        # Generate JWT token
        token = AuthHandler.sign_jwt(new_user.id)
        
        return UserWithToken(token=token)
    
    def authenticate_user(self, email: str, password: str) -> UserWithToken:
        """Authenticate user and return JWT token"""
        # Get user from database
        user = self.__userRespository.get_user_by_email(email)
        
        if not user:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        # Verify password
        if not hashHelper.verfy_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        # Generate JWT token
        token = AuthHandler.sign_jwt(user.id)
        
        return UserWithToken(token=token)
    
    def get_user_by_id(self, user_id: int) -> UserOutput:
        """Get user information by ID"""
        user = self.__userRespository.get_user_by_id(user_id)
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserOutput(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )