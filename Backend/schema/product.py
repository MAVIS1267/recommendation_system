from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema cho bảng products
class ProductBase(BaseModel):
    name: str
    category: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    popularity: Optional[int] = 0

class Product(ProductBase):
    id: int
    popularity: int

    class Config:
        orm_mode = True
