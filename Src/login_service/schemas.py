"""Validation for Login Service"""

from pydantic import BaseModel, EmailStr, constr

pattern_str = r"[a-z]"

class Account(BaseModel):
    """Json input vailidation for Accounts"""
    user_id: int
    name: constr(min_length=2, max_length=25)
    email: EmailStr
    password: constr(min_length=5, max_length=50, pattern=pattern_str)
