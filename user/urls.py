from fastapi import (
    APIRouter,
    Depends,
)
from user.schema import (
    CreateUser
)
from authentication.oauth import get_current_user
from sqlalchemy.orm import Session
from db.session import get_db
from .repository import UserRepository

user_router = APIRouter(tags=["user"])


@user_router.post('', status_code=201)
def create(body: CreateUser, db: Session = Depends(get_db)):
    return UserRepository.create(db, body)

#
# @user_router.get('/{id}', response_model=ShowUser)
# def get_one(user_id: int, db: Session = Depends(get_db),
#             get_current_user: CreateUser = Depends(get_current_user)
#             ):
#     return UserRepository.get_one(db, user_id)
#
