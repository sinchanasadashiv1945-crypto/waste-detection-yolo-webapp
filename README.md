# 🗑️ Waste Detection using YOLO + Flask

## 📌 Overview
This project is an AI-based waste detection system using YOLO (You Only Look Once) and Flask web framework.  
It detects waste objects from uploaded images and shows results with bounding boxes.

## 🎯 Objective
- Detect waste objects in images  
- Use a trained YOLO model for object detection  
- Deploy the model using a Flask web application  

## 🧠 Model Used
- YOLO (Ultralytics implementation)  
- Custom trained model (`best.pt`)  

## 🛠️ Tech Stack
- Python  
- Flask  
- YOLO (Ultralytics)  
- PyTorch  
- OpenCV  
- NumPy  
- Pillow  

## ⚙️ How It Works
- User uploads an image through the web interface  
- Flask sends image to YOLO model  
- Model detects waste objects  
- Output image with bounding boxes is displayed  

## 🚀 How to Run
Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open in browser:
http://127.0.0.1:5000/

## 📸 Output
Detected waste objects are shown with bounding boxes on the image.  
(Added sample screenshots in a screenshots folder)

## 🔮 Future Improvements
- Improve dataset with more waste categories  
- Enable real-time camera detection  
- Deploy on cloud platform  
- Improve UI design  

## 👩‍💻 Author
Sinchana S  
BCA, JSS Science and Technology University, Mysuru  

## ⭐ Note
This project is for educational and research purposes to demonstrate YOLO-based object detection with Flask deployment.
