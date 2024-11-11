from sqlalchemy.orm import Session
from .models import Product
from .schemas import ProductCreate
from typing import List

def bulk_insert_products(db: Session, rows: List[dict], exchange_rates: dict) -> List[Product]:
    products = []
    for row in rows:
        product_data = transform_row(row, exchange_rates)
        if product_data:
            product = Product(**product_data.dict())
            db.add(product)
            products.append(product)
    db.commit()
    return products

def transform_row(row: dict, exchange_rates: dict) -> ProductCreate:
    price = row["price"]
    expiration = row["expiration"]
    currencies = {currency: round(price * exchange_rates[currency], 2) for currency in exchange_rates}
    
    return ProductCreate(
        name=row["name"],
        price=price,
        expiration=expiration,
        currencies=currencies,
    )