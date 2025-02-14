from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the trained model
with open("xgboost_demand_forecasting.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Walmart Demand Forecasting API is Running!"

# Define API route for predictions
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    
    # Make predictions
    predictions = model.predict(df)
    
    return jsonify({"predictions": predictions.tolist()})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
