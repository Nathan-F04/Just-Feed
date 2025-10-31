"""Module for the login service"""

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .database import engine, SessionLocal
from .models import Base, AccountDB
from .schemas import (
    AccountCreate, AccountRead
)

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/login/sign-up", response_model=AccountRead, status_code=status.HTTP_201_CREATED)
def add_user(payload: AccountCreate, db: Session = Depends(get_db)):
    """Sign In method to create an account"""
    user = AccountDB(**payload.model_dump())
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="User already exists")
    return user
