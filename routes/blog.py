from app import app
from models.blog import Blog


@app.get('/blog')
def get_all():
    pass


@app.get('/blog/{post_id}')
def get_one(blog_id: str):
    pass


@app.post('/blog')
def create(coding: Blog):
    pass


@app.delete("/blog/{post_id")
def delete(blog_id: str):
    pass


@app.put('/blog/{post_id}')
def update(blog_id: str, coding: Blog):
    pass
