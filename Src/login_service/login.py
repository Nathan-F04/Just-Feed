"""Module for the login service"""

from fastapi import FastAPI, HTTPException, status
from .schemas import Account

app = FastAPI()
accounts: list[Account] = []

@app.post("/account/create", status_code=status.HTTP_201_CREATED)
def create_account(account: Account):
    """Addeds an account to the accounts list"""
    if any(a.user_id == account.user_id for a in accounts):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    accounts.append(account)
    return account
