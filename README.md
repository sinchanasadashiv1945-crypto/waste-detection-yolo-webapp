# 🗑️ Waste Detection using YOLO + Flask (Real-Time + Webcam)

## 📌 Overview
This project is a real-time waste detection system using YOLO (You Only Look Once) and Flask web framework.

It detects waste objects from images and also supports real-time webcam-based detection when run from command prompt.

## 🎯 Objective
- Detect waste objects in real-time  
- Support both image upload and webcam-based detection  
- Deploy YOLO model using Flask web application  

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
- User uploads an image via web interface OR runs webcam mode from command prompt  
- Flask or OpenCV captures input  
- YOLO model performs real-time object detection  
- Output is displayed with bounding boxes  

## 🚀 How to Run

Install dependencies:
pip install -r requirements.txt

Run Flask application:
python app.py

Open in browser:
http://127.0.0.1:5000/

## 🎥 Webcam Mode (Command Prompt)
Run detection using webcam:
python app.py (or your detection script if enabled)

Then system accesses webcam and performs real-time detection.

## 📸 Output
Detected waste objects are highlighted with bounding boxes in real-time.

## 🔮 Future Improvements
- Improve dataset with more waste categories  
- Optimize real-time webcam performance  
- Deploy on cloud platform  
- Improve UI design  

## 👩‍💻 Author
Sinchana S  
BCA, JSS Science and Technology University, Mysuru  

## ⭐ Note
This project demonstrates real-time YOLO-based object detection with both web and webcam-based deployment using Flask and OpenCV.
