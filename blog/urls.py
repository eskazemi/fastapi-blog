from typing import List
from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session
from database import get_db
from blog.schema import (
    CreateBlog,
    UpdateBlog,
    ShowBlog
)
from user.schema import CreateUser
from authentication.oauth import get_current_user

from .repository import BlogRepository

blog_router = APIRouter(tags=["Blog"])


@blog_router.get('', response_model=List[ShowBlog])
def get_all(db: Session = Depends(get_db),
            get_current_user: CreateUser = Depends(get_current_user)):
    return BlogRepository.get_all(db)


@blog_router.get('/{post_id}', response_model=ShowBlog)
def get_one(blog_id: int, db: Session = Depends(get_db),
            get_current_user: CreateUser = Depends(get_current_user)
            ):
    return BlogRepository.get_one(db, blog_id)


@blog_router.post('', )
def create(body: CreateBlog, db: Session = Depends(get_db),
           get_current_user: CreateUser = Depends(get_current_user)
           ):
    return BlogRepository.create(db, body)


@blog_router.delete('/{blog_id}')
def delete(blog_id: int, db: Session = Depends(get_db),
           get_current_user: CreateUser = Depends(get_current_user)
           ):
    return BlogRepository.delete(db, blog_id)


@blog_router.put('/{blog_id}', )
def update(body: UpdateBlog, blog_id: int, db: Session = Depends(get_db),
           get_current_user: CreateUser = Depends(get_current_user)
           ):
    return BlogRepository.update(db, blog_id, body)
