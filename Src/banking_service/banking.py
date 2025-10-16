"""Banking python file"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from .bankingdb import engine, SessionLocal
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
def edit_bank_account_details(banking_id: int, payload: BankUserCreate, db: Session = Depends(get_db)):
    bank_user_changed = BankUserDB(**payload.model_dump())
    try:
        stmt = update(bank_user_changed).where(bank_user_changed.id == banking_id)
        db.commit()
        db.refresh(bank_user_changed)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="cannot edit bank details")
    except:
        HTTPException(status_code=404, detail="bank_id not found")
    return bank_user_changed

@app.delete("/api/banking/", response_model=BankUserRead, status_code=status.HTTP_200_OK)
def delete_bank_account_details(payload: BankUserCreate, db: Session = Depends(get_db)):
        bank_user_changed = BankUserDB(**payload.model_dump())
        db.delete(bank_user_changed)
        try:
            db.commit()
            db.refresh(bank_user_changed)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="cannot edit bank details")
        return bank_user_changed
