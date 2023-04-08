from pydantic import (
    BaseModel,
    Field,
)
from typing import Optional


class Creator(BaseModel):
    email: str

    class Config:
        orm_mode = True


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


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Creator

    class Config:
        orm_mode = True
