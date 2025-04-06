import sqlite3

class ProductAgent:
    def __init__(self):
        self.conn = sqlite3.connect("database/ecommerce.db")
    
    def get_products_by_category(self, category):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE category=?", (category,))
        return cursor.fetchall()