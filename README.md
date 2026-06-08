# 🗑️ Waste Detection using YOLOv8n + Flask (Real-Time + Webcam)

## 📌 Overview
This project is a real-time waste detection system using YOLOv8n (Ultralytics) and Flask web framework.

It detects waste objects from uploaded images and also supports real-time webcam-based detection using OpenCV when executed from command prompt.

## 🎯 Objective
- Detect waste objects in real-time  
- Support both image upload and webcam-based detection  
- Deploy a YOLOv8n model using Flask web application  

## 🧠 Model Used
- YOLOv8n (Ultralytics lightweight object detection model)  
- Custom trained model (`best.pt`)  

## 🛠️ Tech Stack
- Python  
- Flask  
- YOLOv8n (Ultralytics)  
- PyTorch  
- OpenCV  
- NumPy  
- Pillow  

## ⚙️ How It Works
- User uploads an image through the web interface OR uses webcam mode via command prompt  
- Flask or OpenCV captures input  
- YOLOv8n model processes the input in real-time  
- Detected waste objects are highlighted with bounding boxes  

## 🚀 How to Run

Install dependencies:
pip install -r requirements.txt

Run Flask application:
python app.py

Open in browser:
http://127.0.0.1:5000/

## 🎥 Webcam Mode (Command Prompt)
The system can also run in real-time webcam mode using OpenCV when executed from terminal.

## 📸 Output
Detected waste objects are shown with bounding boxes in real-time on images or webcam feed.

## 🔮 Future Improvements
- Improve dataset with more waste categories  
- Enhance real-time webcam performance  
- Deploy on cloud platforms (AWS / Render)  
- Improve UI design  

## 👩‍💻 Author
Sinchana S  
BCA, JSS Science and Technology University, Mysuru  

## ⭐ Note
This project demonstrates real-time object detection using YOLOv8n and Flask for practical AI deployment in waste management systems.
## ⭐ Note
This project demonstrates real-time YOLO-based object detection with both web and webcam-based deployment using Flask and OpenCV.
