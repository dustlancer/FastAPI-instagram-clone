from fastapi import FastAPI
from db import models
from db.database import engine
from routers.user import router as user_router
from routers.post import router as post_router
from routers.comment import router as comment_router
from auth.authentication import router as auth_router

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)
app.include_router(auth_router)
app.include_router(comment_router) 

@app.get("/")
def root():
    return "hello world"


origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')