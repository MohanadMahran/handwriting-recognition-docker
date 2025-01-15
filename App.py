from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = 'handwriting_model.h5'

# Check if the model exists, and create it if not
if not os.path.exists(MODEL_PATH):
    from model import create_and_save_model
    create_and_save_model()

model = load_model(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']

    # Open and preprocess the image
    image = Image.open(file).convert('L')  # Convert to grayscale
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0  # Normalize
    image_array = image_array.reshape(1, 28, 28)

    # Predict the digit
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)

    return f"The predicted digit is: {predicted_digit}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)