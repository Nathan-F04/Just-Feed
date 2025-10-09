"""Banking python file"""

# app/main.py
from fastapi import FastAPI, HTTPException, status
from .schemas import Bank_user

app = FastAPI()
bank_details: list[Bank_user] = []

@app.get("/api/banking")
def get_all_bank_accounts():
    return bank_details

@app.get("/api/banking/{banking_id}")
def get_bank_account_details(banking_id: int):
    for u in bank_details:
        if u.banking_id == banking_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="bank account not found")

@app.post("/api/banking", status_code=status.HTTP_201_CREATED)
def add_bank_account(bank_account: Bank_user):
    if any(u.banking_id == bank_account.banking_id for u in bank_details):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="bank_id already exists")
    bank_details.append(bank_account)
    return bank_account

@app.put("/api/banking/{banking_id}", status_code=status.HTTP_200_OK)
def edit_bank_account_details(banking_id: int, bank_account: Bank_user):
    for u in bank_details:
        if u.banking_id == banking_id:
            if banking_id == bank_account.banking_id:
                bank_details[bank_details.index(u)] = bank_account
                return bank_account
            else:
                return {"message" : "Can't update user_id value"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.delete("/api/delete/banking/{banking_id}", status_code=204)
def delete_bank_account(banking_id: int):
    for u in bank_details:
        if u.banking_id == banking_id:
            bank_details.remove(u)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
