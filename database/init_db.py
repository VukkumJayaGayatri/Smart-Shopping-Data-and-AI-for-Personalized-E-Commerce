import sqlite3
import pandas as pd

# Load datasets
customers = pd.read_csv("data/customer_data_collection.csv")
products = pd.read_csv("data/product_recommendation_data.csv")

# Clean column names (replace spaces with underscores)
customers.columns = [col.replace(" ", "_") for col in customers.columns]
products.columns = [col.replace(" ", "_") for col in products.columns]

# Create DB
conn = sqlite3.connect("database/ecommerce.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    location TEXT,
    browsing_history TEXT,
    purchase_history TEXT,
    segment TEXT,
    avg_order_value REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    category TEXT,
    subcategory TEXT,
    price REAL,
    brand TEXT,
    avg_rating REAL,
    sentiment_score REAL,
    similar_products TEXT
)
""")

# Insert data
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)

conn.commit()
conn.close()