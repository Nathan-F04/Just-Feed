"""Banking python file"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .database import engine, SessionLocal
from .models import Base, BankUserDB
from .schemas import BankUserCreate, BankUserRead

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/banking", response_model=list[BankUserRead])
def get_all_bank_accounts(db: Session = Depends(get_db)):
    stmt = select(BankUserDB).order_by(BankUserDB.id)
    return list(db.execute(stmt).scalars())

@app.get("/api/banking/{banking_id}", response_model=BankUserRead)
def get_bank_account(banking_id: int, db: Session = Depends(get_db)):
    bank_user = db.get(BankUserDB, banking_id)
    if not bank_user:
        raise HTTPException(status_code=404, detail="bank account not found")
    return bank_user

@app.post("/api/banking", response_model=BankUserRead, status_code=status.HTTP_201_CREATED)
def add_bank_account(payload: BankUserCreate, db: Session = Depends(get_db)):
    bank_user = BankUserDB(**payload.model_dump())
    db.add(bank_user)
    try:
        db.commit()
        db.refresh(bank_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="bank_id already exists")
    return bank_user



@app.put("/api/banking/{banking_id}", response_model=BankUserRead, status_code=status.HTTP_200_OK)
def edit_bank_account_details(banking_id: int, bank_account: Bank_user):
    for u in bank_details:
        if u.banking_id == banking_id:
            if banking_id == bank_account.banking_id:
                bank_details[bank_details.index(u)] = bank_account
                return bank_account
            else:
                return {"message" : "Can't update user_id value"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.put("/api/banking/{banking_id}", response_model=BankUserRead, status_code=status.HTTP_200_OK)
def edit_bank_account_details(banking_id: int, payload: BankUserCreate, db: Session = Depends(get_db)):
    bank_user_changed = BankUserDB(**payload.model_dump())
    bank_user_original = get_bank_account(banking_id)
    # stmt = select(BankUserDB).where(BankUserDB.name == "patrick")
    # patrick = session.scalars(stmt).one()
    # patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
    # sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

    # db.commit()
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

