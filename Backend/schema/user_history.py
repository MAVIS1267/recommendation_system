from pydantic import BaseModel
from typing import Optional

# Schema cho bảng user_history
class UserHistoryBase(BaseModel):
    user_id: int
    product_id: int

class UserHistoryCreate(UserHistoryBase):
    pass

class UserHistory(UserHistoryBase):
    id: int

    class Config:
        orm_mode = True