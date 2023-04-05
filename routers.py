from fastapi import APIRouter
from blog.urls import blog_router
from user.urls import user_router
api_router = APIRouter()

api_router.include_router(blog_router, prefix="/blog")
api_router.include_router(user_router, prefix="/user")
