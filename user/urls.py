from fastapi import (
    APIRouter,
    Response,
)
from user.models import User
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

user_router = APIRouter()

_tag_base = ["user"]


@user_router.get('', tags=_tag_base)
def get_all():
    pass


@user_router.post('', tags=_tag_base)
def create_user():
    pass


@user_router.get('/{id}', tags=_tag_base)
def find_user(id: str):
    pass


@user_router.put('/{user_id}', tags=_tag_base)
def update_user(user_id: str):
    pass


@user_router.delete('/{user_id}', tags=_tag_base)
def delete_user(user_id: str):
    pass
