import os
print("Current working directory:", os.getcwd())
print("Template folder exists:", os.path.exists('templates'))
print("Recommendations template exists:", os.path.exists('templates/recommendations.html'))

from flask import Flask, render_template, request, redirect, url_for
from agents.customer_agent import CustomerAgent
from agents.recommendation_agent import RecommendationAgent

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/recommend/")
def recommend():
    customer_id = request.args.get('customer_id')
    if not customer_id:
        return redirect(url_for('home'))
    
    customer = CustomerAgent(customer_id).get_profile()
    if not customer:
        return "Customer not found", 404
    
    recommendations = RecommendationAgent().generate_recommendations(customer_id)
    return render_template('recommendations.html',
                        customer_id=customer_id,
                        age=customer[1],
                        gender=customer[2],
                        location=customer[3],
                        segment=customer[6],
                        recommendations=recommendations)

@app.route('/test')
def test():
    return render_template('recommendations.html', 
                         customer_id="TEST123",
                         age=25,
                         gender="Test",
                         location="Test",
                         segment="Test",
                         recommendations="Test recommendation")

if __name__ == "__main__":
    app.run(debug=False)