from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
print(settings.path)

# models.Base.metadata.create_all(bind=engine)  --> this is the line responsible for sqlalchemy to generates all tables when server is in running

app = FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/")
def log():
    return "world welcomes you"



