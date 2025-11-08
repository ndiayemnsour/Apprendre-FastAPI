from fastapi import APIRouter
from typing import List
from app.models.user import User
from app.services.user import users

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/users", response_model=List[User])
def get_users():
    return users.get_users()

@router.get("/users/{id}", response_model=User)
def get_user(id: int):
    return users.get_user(id)

@router.post("/users", response_model=User)
def create_user(user: User):
    return users.create_user(user)

@router.put("/users/{id}", response_model=User)
def update_user(id: int, user: User):
    return users.update_user(id, user)

@router.delete("/users/{id}", response_model=User)
def delete_user(id: int):
    return users.delete_user(id)