

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str 
    password: str
    age: int | None = None


class Login(BaseModel):
    email:str
    password:str

class AuthAPI:

    def post_register_user(self,user: User):
        return  user
        
    def post_login_user(self,login:Login):
	    return login
