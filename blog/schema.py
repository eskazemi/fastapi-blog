from pydantic import (
    BaseModel,
    Field,
)
from user.schema import ShowUser
from typing import Optional


class CreateBlog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True



class UpdateBlog(BaseModel):
    title: Optional[str] = Field(default=None)
    body: Optional[str] = Field(default=None)

    class Config:
        orm_mode = True


class ShowBlog(CreateBlog):
    creator: ShowUser

    class Config:
        orm_mode = True
