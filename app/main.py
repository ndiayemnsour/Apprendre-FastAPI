from fastapi import FastAPI
from app.api.routes import users
app = FastAPI(title="Apprendre FASTAPI")

# Routes
app.include_router(users.router)
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans FASTAPI"}