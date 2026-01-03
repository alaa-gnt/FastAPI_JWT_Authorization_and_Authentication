from bcrypt import checkpw , hashpw , gensalt

class hashHelper(object):
    
    # declaring the next method as a static method wish means the method doesnt need self 
    # and can be called direcly on the class
    @staticmethod 
    def verfy_password(plain_password : str , hashed_password: str): # a function to check if the password is hashed or no
        if checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
        else:
            return False
        
    @staticmethod # the next method is static
    def get_password_hash(plain_password: str):
        return hashpw(
            plain_password.encode('utf-8'), # converts the plain text password into bytes wish is required by bcrypt
            gensalt() # each time the function is caleed the hash will be diffrente even if the password is the same
        ).decode('utf-8') # converting back to string 