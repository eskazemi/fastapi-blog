from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from config import get_setting

settings = get_setting()

SQLALCHEMY_DATABASE_URL = f"postgresql://" \
                          f"{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_server}:{settings.postgres_port}/{settings.postgres_db}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()