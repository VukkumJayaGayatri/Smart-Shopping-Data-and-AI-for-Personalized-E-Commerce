import ollama
import sqlite3

class RecommendationAgent:
    def __init__(self):
        self.conn = sqlite3.connect("database/ecommerce.db")
    
    def generate_recommendations(self, customer_id):
        # Fetch customer data
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id=?", (customer_id,))
        customer = cursor.fetchone()
        
        # Use Ollama for personalized recs
        prompt = f"""
        Customer Profile: 
        - Age: {customer[1]}, Gender: {customer[2]}, Location: {customer[3]}
        - Browsing History: {customer[4]}
        - Purchase History: {customer[5]}
        
        Suggest 5 relevant products from the database.
        """
        
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response["message"]["content"]