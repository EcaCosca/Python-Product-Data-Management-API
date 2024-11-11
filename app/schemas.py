from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    expiration: datetime
    currencies: Dict[str, float]

class ProductResponse(ProductCreate):
    id: int
    
    class Config:
        from_attributes = True