from fastapi import (
    HTTPException,
    status,
)
from sqlalchemy.orm import Session
from user.models import User
from hashing import HashController


class UserRepository:

    @staticmethod
    def get_all(db: Session,):
        pass

    @staticmethod
    def get_one(db: Session, user_id: int):
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"USer with th id {user_id} Not Found")

    @staticmethod
    def create(db: Session, body):
        new_user = User(hashed_password=HashController.hashing(
            body.password), email=body.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "create was successfully", "code": 201,
                "data": new_user}

    @staticmethod
    def update(db: Session, user_id: int):
        pass
