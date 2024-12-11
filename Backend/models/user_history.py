from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserHistory(Base):
    __tablename__ = "user_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
