from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema cho bảng user_search_history
class UserSearchHistoryBase(BaseModel):
    user_id: int
    search_query: str
    product_id: Optional[int] = None

class UserSearchHistoryCreate(UserSearchHistoryBase):
    pass

class UserSearchHistory(UserSearchHistoryBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True