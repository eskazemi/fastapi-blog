from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uui

app = FastAPI()
posts = []


# post Model

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get('/')
def read_root():
    return {"welcome": "welcome to my REST AAPI"}


@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts')
def save_post(post: Post):
    post.id = str(uui())
    posts.append(post.dict())
    return posts[-1]


@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post Not Found')


@app.delete("/posts/{post_id")
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post Not Found')


@app.put('/posts/{post_id}')
def update_post(post_id: str, update_p: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = update_p.title
            posts[index]["content"] = update_p.content
            posts[index]["author"] = update_p.author

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not found")
