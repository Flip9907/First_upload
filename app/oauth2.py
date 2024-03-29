from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import schema,database,models
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY=settings.secret_key
ALGORITHM =settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES =settings.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode=(data.copy())
    # a=str(to_encode)
    # print(a)
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str, credentials_Exception):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id =str(payload.get("user_id"))
        # print(id)
        if id is None:
            raise credentials_Exception
        token_data=schema.TokenData(id=id)
    except JWTError:
        raise credentials_Exception

    return token_data


def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_Exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail=f"could not validate credentials",
                                        headers={"WWW-Authenticate":"Bearer"})
    token=verify_access_token(token,credentials_Exception)
    user=db.query(models.Users).filter(models.Users.id==(token.id)).first()
    return user

# print(type(schema.TokenData(id="14")))