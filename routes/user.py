from fastapi import APIRouter, Response, status
from confing.db import conn
from schemas.user import userEntity, usersEntiry
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()


@user.get('/users')
def find_all_user():
    return usersEntiry(conn.local.user.find())


@user.post('/users', tags=["users"])
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    info = conn.local.user.find_one({"_id": id})
    return userEntity(info)


@user.get('/user/{id}')
def find_user(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.put('/users/{user_id}')
def update_user(user_id: str, info: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": dict(info)})
    return userEntity(conn.local.user.find_one({"_id": ObjectId(user_id)}))


@user.delete('/users/{user_id}')
def delete_user(user_id: str):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(user_id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
