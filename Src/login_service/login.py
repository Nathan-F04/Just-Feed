"""Module for the login service"""

from fastapi import FastAPI, HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from .database import engine, SessionLocal
from .models import Base, AccountDB
from .schemas import (
    AccountCreate, AccountLogin, AccountRead
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

@app.post("/api/login/sign-in")
def get_user_login(payload: AccountLogin, db: Session = Depends(get_db)):
    """Login checks if user exists in database and if passwords match"""
    payload_data = AccountDB(**payload.model_dump())
    stmt = select(AccountDB).where(AccountDB.email == payload_data.email)
    user = db.execute(stmt).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Incorrect Email")
    if payload_data.password == user.password:
        return "login Successful"
    raise HTTPException(status_code=400, detail="Incorrect Password")
