from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
import datetime

Base = declarative_base()

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String, index=True)
    date = Column(Date, index=True)
    amount = Column(Float)
    category = Column(String, index=True)

class ReceiptCreate(BaseModel):
    vendor: str
    date: datetime.date
    amount: float
    category: str = None
