# 🎯 Object Detection & Counting

**Streamlit + YOLOv8** app for detecting and counting objects in uploaded images or live webcam feeds.  
It displays **two images side-by-side** — the original and a highlighted version where detected objects are visible and everything else is blacked out for clear focus.

---

## 📸 Features

✅ **Image Upload Mode** — Upload any image to detect and count objects.  
✅ **Webcam Mode** — Detect in real-time with smooth start/stop control.  
✅ **Highlight View** — Keeps detected objects visible while darkening the rest.  
✅ **Accurate Counting** — Displays live count of detected object classes.  
✅ **Clean UI** — Streamlit interface with instant feedback.  
✅ **Modular Codebase** — Easy to update or swap YOLO models.

---

## 🧠 How It Works

1. Load image or webcam frame.  
2. Pass it through **YOLOv8** for object detection.  
3. Draw bounding boxes and labels (black text for clarity).  
4. Create a **highlight mask** to show only detected regions.  
5. Display both views side-by-side in Streamlit.

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/Object-Detection-and-Object-Counting.git
cd Object-Detection-and-Object-Counting

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py




Object-Detection-and-Object-Counting/
│
├── app.py                # Streamlit main interface
├── detect_image.py       # Image detection logic (YOLOv8)
├── utils/
│   └── __init__.py
├── models/
│   └── yolov8m.pt        # YOLOv8 model weights
├── requirements.txt      # Dependencies
└── README.md             # Project documentation


💡 Example Use Cases

Realtime surveillance and people counting
Traffic object detection
Educational computer vision demos
YOLOv8 testing with a user-friendly interface



Thank You ❤️