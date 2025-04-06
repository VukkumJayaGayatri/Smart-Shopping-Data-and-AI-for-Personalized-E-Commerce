import sqlite3

class CustomerAgent:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.conn = sqlite3.connect("database/ecommerce.db")
    
    def get_profile(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id=?", (self.customer_id,))
        return cursor.fetchone()
    
    def update_preferences(self, new_interests):
        # (Optional) Update browsing history
        pass