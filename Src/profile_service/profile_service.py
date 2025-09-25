"""Module for the Profile setting service"""

from fastapi import FastAPI, HTTPException, status
from .schemas import Account

app = FastAPI()
accounts: list[Account] = []

@app.put("/api/users/", status_code=status.HTTP_201_CREATED)
def update_account(account: Account):
    """Test put method for altering an account"""
    for a in accounts:
        if a.account_id == account.account_id:
            accounts[accounts.index(a)] = account
            return account
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
