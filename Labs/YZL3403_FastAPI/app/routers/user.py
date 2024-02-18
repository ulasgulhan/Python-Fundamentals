from fastapi import APIRouter, Depends, status, HTTPException
from settings import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from models import User
from pydantic import BaseModel, Field
from .auth import get_currnet_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/user',
    tags=['user']
)


def get_db_conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db_conn)]
user_dependency = Annotated[dict, Depends(get_currnet_user)]
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


class PasswordVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.get(path='/', status_code=status.HTTP_200_OK)
async def get_user(db: db_dependency):
    data = db.query(User).all()

    if data is not None:
        return data

    raise HTTPException(
        status_code=200,
        detail='User not found'
    )


@router.put(path='/password', status_code=status.HTTP_200_OK)
async def change_password(db: db_dependency, user: user_dependency, pwd_verification: PasswordVerification,):
    if user is None:
        raise HTTPException(
            status_code=401,
            detail='Authentication Faild'
        )

    user_model = db.query(User).filter(User.id == int(user.get('id'))).first()

    if not pwd_context.verify(pwd_verification.password, user_model.hashed_password):
        raise HTTPException(
            status_code=401,
            detail='Erron on password change'
        )

    user_model.hashed_password = pwd_context.hash(pwd_verification.new_password)

    db.add(user_model)
    db.commit()

    return {
        'status_code': 200,
        'transaction': 'Successful'
    }






