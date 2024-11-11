from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from .database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    expiration = Column(DateTime)
    currencies = Column(JSON)