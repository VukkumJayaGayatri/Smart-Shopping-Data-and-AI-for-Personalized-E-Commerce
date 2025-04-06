from flask import Flask, request, jsonify
from agents.customer_agent import CustomerAgent
from agents.recommendation_agent import RecommendationAgent

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>E-Commerce Recommendation API</h1>
    <p>Try the recommendation endpoint: <a href='/recommend/C1000'>/recommend/C1000</a></p>
    """

@app.route("/recommend/<customer_id>", methods=["GET"])
def recommend(customer_id):
    print(f"Received request for customer: {customer_id}")  # Add this line
    try:
        customer = CustomerAgent(customer_id).get_profile()
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        
        recommendations = RecommendationAgent().generate_recommendations(customer_id)
        return jsonify({
            "customer_id": customer_id,
            "profile": {
                "age": customer[1],
                "gender": customer[2],
                "location": customer[3],
                "segment": customer[6]
            },
            "recommendations": recommendations
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/test")
def test():
    return "Server is working!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Changed port