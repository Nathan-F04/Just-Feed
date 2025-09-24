"""Module for the login service"""

from fastapi import FastAPI
from .schemas import Account

app = FastAPI()
accounts = list[Account]

@app.post("/account/create")
def create_account(account: Account):
    accounts.append(account)
