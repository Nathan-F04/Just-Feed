"""Module for the login service"""

from fastapi import FastAPI
from .schemas import Account

app = FastAPI()
Accounts = list[Account]

@app.post("/account/create")
def create_account(account: Account):
    """Addeds an account to the accounts list"""
    Accounts.append(account)
    return Accounts
