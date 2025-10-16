"""Validation for Profile Setting Service"""

# app/schemas.py
from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict

NameStr = Annotated[str, StringConstraints(min_length=2, max_length=50)]
Cardstr = Annotated[str, StringConstraints(pattern=r"\\d{16}$")]

class BankUserCreate(BaseModel):
    name: NameStr
    email: EmailStr
    pin: int = Field(gt=1000)
    card: Cardstr 
    balance: int = Field(gt=0)

class BankUserRead(BaseModel):
    id: int
    name: NameStr
    email: EmailStr
    pin: int = Field(gt=1000, lt=9999)
    card: Cardstr
    balance: int  = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)