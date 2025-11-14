"""Validation schemas for Order Service"""

from typing import List, Optional, Annotated
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from annotated_types import Ge

# Type aliases
PositiveInt = Annotated[int, Ge(1)]
PositiveFloat = Annotated[float, Ge(0.01)]

# Cart Item schemas
class CartItemCreate(BaseModel):
    item_name: str = Field(min_length=1, max_length=100)
    price: PositiveFloat
    quantity: PositiveInt

class CartItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    item_name: str = Field(max_length=200)
    price: float
    quantity: int

class CartItemUpdate(BaseModel):
    quantity: PositiveInt

# Cart schemas
class CartRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    created_at: datetime
    items: List[CartItemRead] = []

# Order Item schemas
class OrderItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    item_name: str = Field(max_length=200)
    price: float
    quantity: int

# Order schemas
class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    total_amount: PositiveFloat
    status: str
    created_at: datetime
    items: List[OrderItemRead] = []

class OrderStatusUpdate(BaseModel):
    status: str = Field(pattern=r"^(pending|confirmed|preparing|ready|delivered|cancelled)$")