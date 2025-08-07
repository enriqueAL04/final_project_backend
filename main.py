from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import users
from app.database import engine
from app.models import user, psychologist

user.Base.metadata.create_all(bind=engine)
psychologist.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI en Render!"}

app.include_router(users.router, prefix="/users", tags=["users"])
