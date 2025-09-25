"""Module for the Profile setting service"""

from fastapi import FastAPI, HTTPException, status
from .schemas import User

app = FastAPI()
users: list[User] = []
    
@app.put("/api/users/", status_code=status.HTTP_201_CREATED)
def update_user(user: User):
    for u in users:
        if(u.user_id == user.user_id):
            users[users.index(u)] = user 
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
