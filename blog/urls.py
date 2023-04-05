from typing import List
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from blog.models import Blog
from sqlalchemy.orm import Session
from database import get_db
from blog.schema import (
    CreateBlog,
    UpdateBlog,
    ShowBlog
)

blog_router = APIRouter()

_tag_base = ["Blog"]


@blog_router.get('', tags=_tag_base, response_model=List[ShowBlog])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    if blogs:
        return blogs
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[])


@blog_router.get('/{post_id}', tags=_tag_base, response_model=ShowBlog)
def get_one(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter_by(id=blog_id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with th id {blog_id} Not Found")


@blog_router.post('', tags=_tag_base)
def create(request: CreateBlog, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": new_blog,
            "message": "update was successfully", "code": 200}


@blog_router.delete('/{blog_id}', tags=_tag_base)
def delete(blog_id: int, db: Session = Depends(get_db)):
    post = db.query(Blog).filter_by(id=blog_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with th id {blog_id} Not Found")

    db.query(Blog).filter_by(id=blog_id).delete()
    db.commit()
    return {"message": "Delete was successfully", "code": 204}


@blog_router.put('/{blog_id}', tags=_tag_base)
def update(request: UpdateBlog, blog_id: int, db: Session = Depends(get_db)):
    post = db.query(Blog).filter_by(id=blog_id).first()
    if post:
        update_doc = {"title": request.title, "body": request.body}
        db.query(Blog).filter_by(id=blog_id).update(update_doc)
        db.commit()
        return \
            {"data": db.query(Blog).filter_by(id=blog_id).one(),
             "message": "update was successfully", "code": 200}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with th id {blog_id} Not Found")
