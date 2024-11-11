from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from .database import get_db, engine
from .models import Base
from .schemas import ProductResponse
from .crud import bulk_insert_products
from .utils.csv_utils import sanitize_csv_data
from .utils.currency_service import CurrencyService
from typing import List, Optional
from .models import Product

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/products/upload", response_model=List[ProductResponse])
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_contents = await file.read()
    rows = sanitize_csv_data(file_contents)
    if len(rows) > 100000:
        raise HTTPException(status_code=400, detail="CSV file has too many rows. Maximum allowed is 100000.")

    currency_service = CurrencyService()
    exchange_rates = currency_service.get_exchange_rates(['eur', 'cad', 'ars', 'cny', 'jpy'])

    products = bulk_insert_products(db, rows, exchange_rates)
    return products

@app.get("/products/search", response_model=List[ProductResponse])
def search_products(
    db: Session = Depends(get_db),
    name: Optional[str] = Query(None, description="Filter by product name"),
    min_price: Optional[float] = Query(None, description="Minimum price"),
    max_price: Optional[float] = Query(None, description="Maximum price"),
    min_expiration: Optional[str] = Query(None, description="Minimum expiration date (YYYY-MM-DD)"),
    max_expiration: Optional[str] = Query(None, description="Maximum expiration date (YYYY-MM-DD)"),
    sort_by: Optional[str] = Query("name", description="Sort by 'name', 'expiration', or 'price'"),
    order: Optional[str] = Query("asc", description="Order by 'asc' or 'desc'")
):
    query = db.query(Product)

    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if min_expiration:
        query = query.filter(Product.expiration >= min_expiration)
    if max_expiration:
        query = query.filter(Product.expiration <= max_expiration)

    sort_column = {
        "name": Product.name,
        "expiration": Product.expiration,
        "price": Product.price
    }.get(sort_by, Product.name)
    
    order_func = asc if order == "asc" else desc
    query = query.order_by(order_func(sort_column))

    products = query.all()
    
    return products