from flask import Flask, jsonify, request
from classifier import get_prediction

app = Flask(__name__)

@app.route("/")

def index():
    return "Welcome To The Home Page"

@app.route("/predict", methods = ["POST"])

def predict():
    image = request.files.get("letter")
    prediction = get_prediction(image)
    
    return jsonify({
        "prediction": prediction
    }), 200

if __name__ == "__main__":
    app.run(debug = True)