import pandas as pd
from io import BytesIO
from datetime import datetime

def sanitize_csv_data(file_contents: bytes) -> list:
    data = pd.read_csv(BytesIO(file_contents), delimiter=';', encoding='utf-8')
    sanitized_rows = []
    
    for _, row in data.iterrows():
        if pd.isnull(row['name']) or pd.isnull(row['price']) or pd.isnull(row['expiration']):
            continue

        expiration_str = str(row['expiration']).strip()
        expiration = None
        for date_format in ("%Y-%m-%d", "%m/%d/%Y"):
            try:
                expiration = datetime.strptime(expiration_str, date_format)
                expiration = expiration.strftime("%Y-%m-%d")  # Format it to "YYYY-MM-DD"
                break
            except ValueError:
                continue

        if expiration is None:
            continue

        sanitized_row = {
            "name": str(row['name']).strip().split(" #(")[0],
            "price": float(str(row['price']).replace("$", "").strip()),
            "expiration": expiration
        }
        sanitized_rows.append(sanitized_row)
    
    return sanitized_rows