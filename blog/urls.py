from fastapi import APIRouter

blog_router = APIRouter()

_tag_base = ["Blog"]


@blog_router.get('', tags=_tag_base)
def get_all():
    pass


@blog_router.get('/{post_id}', tags=_tag_base)
def get_one(blog_id: str):
    pass


@blog_router.post('', tags=_tag_base)
def create():
    pass


@blog_router.delete('/{blog_id}', tags=_tag_base)
def delete(blog_id: str):
    pass


@blog_router.put('/{blog_id}', tags=_tag_base)
def update(blog_id: str):
    pass

