"""Validation for Profile Setting Service"""

from pydantic import BaseModel, EmailStr, constr, conint

pattern_str = "\\d{16}$"

class Bank_user(BaseModel):
    banking_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    pin: conint(gt=1000, lt=9999)
    card: constr(min_length=16, max_length=16, pattern=pattern_str)
    balance: conint(gt=0)
