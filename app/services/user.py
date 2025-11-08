from app.models.user import User
from fastapi import HTTPException

#Base de données simulée
users = [
    User(id=1, first_name="John", last_name="Doe", email="", password=""),
    User(id=2, first_name="Jane", last_name="Doe", email="", password=""),
]

#Read all user
def get_users():
    return users

#Read one user
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

#create user
def create_user(user: User):
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User already exists")
    users.append(user)
    return user

#update user
def update_user(id: int, user: User):
    for index, u in enumerate(users):
        if u.id == id:
            users[index] = user
            return user
        raise HTTPException(status_code=404, detail="User not found")

#delete user
def delete_user(id: int):
    for index, u in enumerate(users):
        if u.id == id:
            del users[index]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")