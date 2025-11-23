from flask import Flask, render_template, request, jsonify
import os
import torch
from inference import load_model, predict_image
import base64
from PIL import Image
import io

app = Flask(__name__)

# Path to model weights
MODEL_PATH = "coatnet_aptos.pth"

# Load the model once at startup
model, device = load_model(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probabilities = None
    image_uploaded = False

    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", error="No file selected")

        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html", error="No file selected")

        image_bytes = file.read()
        pred_class, pred_label, probs = predict_image(model, device, image_bytes)
        prediction = f"Prediction: {pred_label} ({pred_class})"
        probabilities = [round(p, 4) for p in probs]
        image_uploaded = True

    return render_template("index.html", prediction=prediction,
                           probabilities=probabilities,
                           image_uploaded=image_uploaded)

# New API endpoint for JSON responses
@app.route("/api/predict", methods=["POST"])
def api_predict():
    if "file" not in request.files:
        return jsonify({"error": "No file selected"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        image_bytes = file.read()
        pred_class, pred_label, probs = predict_image(model, device, image_bytes)
        
        # Convert probabilities to float for JSON serialization
        probabilities = [float(round(p, 4)) for p in probs]
        
        return jsonify({
            "success": True,
            "prediction": {
                "class": pred_class,
                "label": pred_label
            },
            "probabilities": probabilities,
            "confidence": float(round(max(probs), 4))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)