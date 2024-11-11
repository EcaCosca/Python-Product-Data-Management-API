# Product Data Management API

## Project Overview

Product Data Management API is an application that enables businesses to manage their product data efficiently. Users can upload CSV files containing product details, which are automatically processed and converted to various currencies based on current exchange rates. Additionally, the API provides endpoints to search and filter products by attributes such as name, price, and expiration date.

[Watch the project overview on Loom](#)

## Description

The Product Data Management API is a FastAPI-based backend solution designed for efficient product data processing and management. It allows users to upload CSV files, validates and sanitizes the data, converts prices to multiple currencies using real-time exchange rates, and provides endpoints to retrieve and search product data.

This project was built as a robust solution for managing and organizing product information, especially for businesses that handle large volumes of data and require dynamic currency conversions.

## Features

- **CSV Upload**: Upload a CSV file with product details for automatic processing.
- **Data Sanitization**: Ensures data accuracy by cleaning and validating each record.
- **Multi-Currency Support**: Converts product prices into different currencies based on the latest exchange rates.
- **Search and Filter Products**: Find products using filters like name, price range, and expiration date, and sort results by specific fields.

## User Stories

- **Upload CSV**: As a user, I can upload a CSV file with product information, which the system will validate and process.
- **Search Products**: As a user, I can search for products by name, price, or expiration date, and sort the results in ascending or descending order.

## Components

- **Database**: Stores product information with fields for name, price, expiration date, and currency values.
- **API Endpoints**: Provides RESTful endpoints to manage, search, and retrieve product data.

## Backend - API Documentation

### Models

**Product Model**

```sql
TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currencies JSONB,
    expiration DATE NOT NULL
);
```

### API Endpoints

| HTTP Method | URL                | Request Body       | Success Status | Error Status | Description                                               |
|-------------|--------------------|--------------------|----------------|--------------|-----------------------------------------------------------|
| POST        | /products/upload   | {file: csv}        | 200            | 400          | Uploads and processes a CSV file containing product data  |
| GET         | /products/search   | ?name&min_price&max_price&min_expiration&max_expiration&sort_by&order | 200 | 404 | Retrieves a list of products with optional filtering and sorting options |

## Development

### Setup

1. Clone the repository:
        ```sh
        git clone https://github.com/yourusername/product-data-management-api.git
        cd product-data-management-api
        ```

2. Create and activate a virtual environment:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Install dependencies:
        ```sh
        pip install -r requirements.txt
        ```

4. Configure environment variables:
        Create a `.env` file in the project root and add your database connection details and API keys. Example:
        ```env
        DATABASE_URL=your_postgres_database_url
        ```

5. Run database migrations:
        ```sh
        alembic upgrade head
        ```

6. Start the development server:
        ```sh
        uvicorn app.main:app --reload
        ```

## Usage

### Upload CSV

- **Endpoint**: `POST /products/upload`
- **Description**: Upload a CSV file containing product details.
- **Request**: Form data with a file field (`file`) containing the CSV file.

### Search Products

- **Endpoint**: `GET /products/search`
- **Query Parameters**:
        - `name`: Filter by product name.
        - `min_price` and `max_price`: Specify a price range.
        - `min_expiration` and `max_expiration`: Specify an expiration date range.
        - `sort_by`: Choose a field to sort by (name, expiration, or price).
        - `order`: Sorting order (asc or desc).
- **Example Request**:
        ```sh
        GET /products/search?name=Cheese&min_price=10&max_price=100&sort_by=price&order=desc
        ```

## Technologies

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database for storing product information.
- **Pandas**: Data manipulation and validation for CSV files.

## Links

### Key Technologies

- **FastAPI**
- **SQLAlchemy**
- **Pandas**
- **Neon for PostgreSQL**

