from fastapi import Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security.authHandler import AuthHandler

security = HTTPBearer()

class JWTBearer:
    """JWT Bearer token authentication dependency"""
    
    def __call__(self, credentials: HTTPAuthorizationCredentials = Security(security)):
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication scheme"
                )
            
            # Decode and verify token
            decoded_token = AuthHandler.decode_jwt(credentials.credentials)
            
            if not decoded_token:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid or expired token"
                )
            
            return decoded_token["user_id"]
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authorization code"
            )
