from fastapi import (
    HTTPException,
    status,
)
from .models import Blog
from sqlalchemy.orm import Session


class BlogRepository:

    @staticmethod
    def get_all(db: Session):
        blogs = db.query(Blog).all()
        if blogs:
            return blogs
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=[])

    @staticmethod
    def get_one(db: Session, blog_id: int):
        blog = db.query(Blog).filter_by(id=blog_id).first()
        if blog:
            return blog
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with th id {blog_id} Not Found")

    @staticmethod
    def create(db: Session, body):
        new_blog = Blog(title=body.title, body=body.body, user_id=1)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return {"data": new_blog,
                "message": "update was successfully", "code": 200}

    @staticmethod
    def update(db: Session, blog_id: int, body):
        post = db.query(Blog).filter_by(id=blog_id).first()
        if post:
            update_doc = {"title": body.title, "body": body.body}
            db.query(Blog).filter_by(id=blog_id).update(update_doc)
            db.commit()
            return \
                {"data": db.query(Blog).filter_by(id=blog_id).one(),
                 "message": "update was successfully", "code": 200}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with th id {blog_id} Not Found")

    @staticmethod
    def delete(db: Session, blog_id: int):
        post = db.query(Blog).filter_by(id=blog_id)
        if not post.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with th id {blog_id} Not Found")

        db.query(Blog).filter_by(id=blog_id).delete()
        db.commit()
        return {"message": "Delete was successfully", "code": 204}
