"""Validation for Login Service"""

from pydantic import BaseModel, EmailStr, constr

class Account(BaseModel):
    """Json input vailidation for Accounts"""
    user_id: int
    name: constr(min_length=2, max_length=25)
    email: EmailStr
    password: constr(min_length=5, max_length=50, pattern = "[a-z]")
