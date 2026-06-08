from flask import Flask, render_template, request
import os
from ultralytics import YOLO

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load YOLO model
model = YOLO("best.pt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    # save uploaded image
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(img_path)

    # run YOLO prediction
    results = model.predict(
        source=img_path,
        save=True,
        project="results",
        name="output",
        exist_ok=True,
        conf=0.1
    )

    return "Detection done! Check results/output folder"

if __name__ == '__main__':
    app.run(debug=True)