"""Module for the Profile setting service"""

from fastapi import FastAPI, HTTPException, status
from .schemas import Setting

app = FastAPI()
settings: list[Setting] = []

@app.put("/api/users/", status_code=status.HTTP_201_CREATED)
def update_account(setting: Setting):
    """Test put method for altering an account"""
    for a in settings:
        if a.account_id == account_id:
            settings[settings.index(a)] = setting
            return setting
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
