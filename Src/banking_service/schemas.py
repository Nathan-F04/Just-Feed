"""Validation for Profile Setting Service"""

from pydantic import BaseModel, EmailStr, constr, conint

pattern_str = r"[a-z]"

class Bank_user(BaseModel):
    banking_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    pin: conint(gt=1000, lt=9999)
    card: constr(min_length=16, max_length=16, pattern=r"\d{16}$")
    balance: conint(gt=0)

    #student_id: constr(min_length=8, max_length=8, pattern="^S\d{7}$")