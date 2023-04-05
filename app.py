from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="Blog",
    version="1.0.0"
)


app.include_router(user)




@app.get('/')
def read_root():
    return {"welcome": "welcome to my REST AAPI"}


