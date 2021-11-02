from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API With FastAPI AND MongoDb ",
    version="0.0.1"
)


app.include_router(user)


