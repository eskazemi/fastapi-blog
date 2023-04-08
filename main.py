from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import api_router

app = FastAPI(
    title="Blog",
    version="1.0.0"
)
app.include_router(api_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

