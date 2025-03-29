from pydantic import EmailStr, BaseModel

class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    username : str
    email : EmailStr