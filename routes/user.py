from fastapi import (
    APIRouter,
    Response,
)
from models.user import User
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

_tag_base = ["user"]


@user.get('/users')
def get_all():
    pass


@user.post('/users', tags=_tag_base)
def create_user(user: User):
    pass


@user.get('/user/{id}', tags=_tag_base)
def find_user(id: str):
    pass


@user.put('/users/{user_id}', tags=_tag_base)
def update_user(user_id: str, info: User):
    pass


@user.delete('/users/{user_id}', tags=_tag_base)
def delete_user(user_id: str):
    pass
