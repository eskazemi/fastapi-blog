from pydantic import BaseModel
from typing import List


class CreateUser(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    email: str
    blogs: List = []

    class Config:
        orm_mode = True

