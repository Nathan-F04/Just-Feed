"""Module for the Profile setting service This file is a test fiel and will be replaced"""

from fastapi import FastAPI, HTTPException, status
from .schemas import Setting

app = FastAPI()
settings: list[Setting] = []

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def create_account(setting: Setting):
    """Addeds an account to the settings list"""
    if any(a.account_id == setting.account_id for a in settings):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    settings.append(setting)       
    return setting

@app.put("/api/users/{account_id}")
def update_account(setting: Setting, account_id: int):
    """Test put method for altering an account"""
    for a in settings:
        if a.account_id == account_id:
            settings[settings.index(a)] = setting
            return setting
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
