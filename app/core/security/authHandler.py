import jwt  # library for creating and verifiyin json web tokens (JWts)
from decouple import config # helps reading envirment variables
import time # to get the time

#reading from the .env file using the config function
JWT_SECRET = config("JWT_SECRET") 
JWT_ALGORITHM = config("JWT_ALGORITHM")

# a class to handeling authentification
class AuthHandler(object):

    @staticmethod # static method
    def sign_jwt(user_id : int ):
        # the content of the JWT 
        payload = { 
            "user_id": user_id , # user ID
            "expires": time.time() + 900 # experitation time wish is after 900s
        }

        # encoding the JWT content and storing it in one string in variable called token
        token = jwt.encode(payload , JWT_SECRET , algorithm=JWT_ALGORITHM) 
        return token
    
    # a static method to decode the already coded token
    @staticmethod
    def decode_jwt(token : str) -> dict: # taken a str and returing a python dict
        try:
            decoded_token = jwt.decode(token , JWT_SECRET , algorithms=[JWT_ALGORITHM])
            # decoding if the experision time is not up yet
            return decoded_token if decoded_token["expires"] >= time.time() else  None 
        except:
            print("enable to decode the token")