from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, conint


class Postbase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(Postbase):
    pass


class Userout(BaseModel):
    id : int
    email: EmailStr
    created_AT:datetime
    class Config:
        from_attributes:True

class Post(Postbase):
    id: int
    created_AT:datetime
    owner:Userout

    class Config:
        from_attributes=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class GetUser(BaseModel):
    email:EmailStr
    id:int

class UserLogin(BaseModel):
    email :EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)