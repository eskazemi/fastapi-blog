from pydantic import (
    BaseModel,
    Field,
)
from typing import (
    Optional,
    List,
)


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


class UpdateUser(BaseModel):
    title: Optional[str] = Field(default=None)
    body: Optional[str] = Field(default=None)

    class Config:
        orm_mode = True
