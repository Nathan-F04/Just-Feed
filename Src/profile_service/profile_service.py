# app/main.py
from fastapi import FastAPI, HTTPException, status
from .schemas import User

app = FastAPI()
users: list[User] = []
    
@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user
