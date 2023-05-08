from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import api_router
from db.session import engine
from db.base_class import Base

from config import get_setting


settings = get_setting()



def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.name, version=settings.project_version)
    create_tables()
    return app


app = start_application()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)