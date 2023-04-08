from datetime import timedelta
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from authentication.jwt_config import (
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from hashing import HashController
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from user.models import User
from database import get_db

router = APIRouter(tags=["Authentication"])


@router.post('/login')
def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    elif not HashController.verify(user.hashed_password, body.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect Password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
