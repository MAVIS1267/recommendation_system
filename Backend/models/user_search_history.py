from sqlalchemy import DateTime
from datetime import datetime

class UserSearchHistory(Base):
    __tablename__ = "user_search_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    search_query = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
