from flask import Flask, request, jsonify
import os
from model import load_model, predict

# Initialize Flask app
app = Flask(__name__)

# Make sure model is loaded
model_info = load_model()
print("Model loaded successfully!")

@app.route("/")
def home():
    """Home endpoint with API info"""
    return jsonify({
        "message": "Iris Species Prediction API",
        "endpoints": {
            "/predict": "POST request with 'features' array of 4 iris measurements"
        },
        "example_request": {
            "features": [5.1, 3.5, 1.4, 0.2]
        }
    })

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    """Prediction endpoint"""
    try:
        data = request.get_json()
        features = data.get("features", [])
        
        if len(features) != 4:
            return jsonify({"error": "Expected 4 features (sepal length, sepal width, petal length, petal width)"}), 400
            
        result = predict(features)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
