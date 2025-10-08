"""Validation for Profile Setting Service"""

from pydantic import BaseModel, EmailStr, constr, conint

pattern_str = r"[a-z]"

class Bank_user(BaseModel):
    banking_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    pin: conint(gt=1000, lt=9999)
    card: conint(gt=10000000000000000, lt=9999999999999999)
    balance: conint(gt=0)