from fastapi import APIRouter, Depends, status, HTTPException
from settings import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import User
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


# region router
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)
# endregion


# region db
def get_db_conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db_conn)]
# endregion


# region DTOs
class UserDTO(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str
# endregion


# region Utilities
SECRET_KEY = 'tcj1$f3k2z0%^6%0h=+g*%@2*u6+zu@m^j7dh-6*2lu44ka*p0'
ALGORITHM = 'HS256'
# hashing işlemi için bcrypt pakatini kuralım (pip install bcrypt)
# CryptContext için pip install passlib
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def create_access_token(username: str, user_id: int, user_role: str, expires_delta: timedelta):
    encode = {
        'sub': username,
        'id': user_id,
        'role': user_role,
    }

    expire = datetime.utcnow() + expires_delta

    encode.update({
        'exp': expire
    })

    # token base auth kullanılırken üreteceğimiz token jwt token olacak
    # bunun için pip install python-jose
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def authenticate_user(db: db_dependency, user_name: str, password: str):
    user = db.query(User).filter(User.user_name == user_name).first()

    if not User:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False

    return user


async def get_currnet_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate user.'
            )
        return {
            'username': username,
            'id': user_id,
            'role': user_role
        }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user.'
        )

# endregion


@router.post(path='/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_dto: UserDTO):
    try:
        user = User(
            email=user_dto.email,
            user_name=user_dto.username,
            first_name=user_dto.first_name,
            last_name=user_dto.last_name,
            hashed_password=pwd_context.hash(user_dto.password),
            is_active=True,
            role=user_dto.role
        )

        db.add(user)
        db.commit()

        return {
            'status_code':201,
            'transaction': 'Successful'
        }
    except Exception as err:
        return {
            'error': str(err)
        }


@router.post(path='/token')
async def get_access_token(db: db_dependency, from_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(db, from_data.username, from_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user'
        )
    else:
        token = create_access_token(user.user_name, user.id, user.role, timedelta(minutes=20))

    return {
        'access_token': token,
        'token_type': 'bearer'
    }



