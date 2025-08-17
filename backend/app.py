from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import cv2
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')
CORS(app)

# Global variable to store the model
model = None

def load_model():
    """Load the trained model"""
    global model
    try:
        from tensorflow import keras
        model_path = 'nail_biter_model.h5'
        if os.path.exists(model_path):
            model = keras.models.load_model(model_path)
            print("Model loaded successfully")
        else:
            print("Model file not found. Please ensure nail_biter_model.h5 is in the backend directory.")
    except Exception as e:
        print(f"Error loading model: {e}")

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory(app.static_folder, filename)

@app.route('/api/predict', methods=['POST'])
def predict():
    """Predict nail biting from uploaded image"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read and preprocess image
        image_bytes = file.read()
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({'error': 'Invalid image format'}), 400
        
        # Resize image to model input size
        img_resized = cv2.resize(img, (224, 224))
        img_normalized = img_resized / 255.0
        img_batch = np.expand_dims(img_normalized, axis=0)
        
        # Make prediction
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        prediction = model.predict(img_batch)
        probability = float(prediction[0][0])
        
        # Determine result
        if probability > 0.5:
            result = "Biting detected"
            confidence = probability
        else:
            result = "No biting detected"
            confidence = 1 - probability
        
        return jsonify({
            'result': result,
            'confidence': round(confidence * 100, 2),
            'probability': round(probability * 100, 2)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})

if __name__ == '__main__':
    load_model()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
