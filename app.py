import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
import numpy as np
import os
import time

st.title("🧠 Object Detection & Counting (Image + Webcam)")
st.write("Upload an image or use webcam to detect and count objects.")

# Load YOLO model
model = YOLO("models/yolov8m.pt")

# Sidebar
option = st.sidebar.radio("Select Mode", ["📷 Upload Image", "🎥 Use Webcam"])
selected_class = st.sidebar.text_input(
    "Enter object name to detect (e.g., person, car) or leave blank for all:"
)

# --- IMAGE UPLOAD ---
if option == "📷 Upload Image":
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        tfile.write(uploaded_file.read())
        temp_path = tfile.name

        st.info("Processing uploaded image...")

        results = model(temp_path)
        img = cv2.imread(temp_path)
        detections = results[0].boxes

        mask = np.zeros_like(img, dtype=np.uint8)
        object_counts = {}

        for box in detections:
            cls = int(box.cls[0])
            class_name = model.names[cls]
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if not selected_class or selected_class.lower() == class_name.lower():
                count = object_counts.get(class_name, 0) + 1
                object_counts[class_name] = count

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 2)
                cv2.putText(img, f"{class_name} {count}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

                mask[y1:y2, x1:x2] = img[y1:y2, x1:x2]

        highlighted = mask
        combined = np.hstack((img, highlighted))
        total_count = sum(object_counts.values())

        st.image(cv2.cvtColor(combined, cv2.COLOR_BGR2RGB),
                 caption=f"Detected Objects (Total: {total_count})",
                 use_container_width=True)

        if selected_class:
            st.success(f"Detected {object_counts.get(selected_class, 0)} '{selected_class}' object(s).")
        else:
            st.success(f"Detected objects: {object_counts}")

        try:
            tfile.close()
            os.remove(temp_path)
        except:
            pass

# --- LIVE WEBCAM ---
elif option == "🎥 Use Webcam":
    st.info("Click the checkbox below to start or stop the webcam.")

    if "run_cam" not in st.session_state:
        st.session_state.run_cam = False

    toggle = st.checkbox("Start / Stop Webcam")

    if toggle:
        st.session_state.run_cam = not st.session_state.run_cam

    frame_window = st.empty()

    if st.session_state.run_cam:
        cap = cv2.VideoCapture(0)
        st.write("Webcam started. Uncheck the box to stop.")

        while st.session_state.run_cam:
            ret, frame = cap.read()
            if not ret:
                st.warning("No frame captured.")
                break

            results = model.predict(frame)
            detections = results[0].boxes
            mask = np.zeros_like(frame, dtype=np.uint8)
            object_counts = {}

            for box in detections:
                cls = int(box.cls[0])
                class_name = model.names[cls]
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if not selected_class or selected_class.lower() == class_name.lower():
                    count = object_counts.get(class_name, 0) + 1
                    object_counts[class_name] = count

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
                    cv2.putText(frame, f"{class_name} {count}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

                    mask[y1:y2, x1:x2] = frame[y1:y2, x1:x2]

            combined = np.hstack((frame, mask))
            frame_window.image(cv2.cvtColor(combined, cv2.COLOR_BGR2RGB),
                               use_container_width=True)

            if "detected_text" not in st.session_state:
              st.session_state.detected_text = st.empty()
            st.session_state.detected_text.write(f"Detected: {object_counts}")

            time.sleep(0.05)

            if not st.session_state.run_cam:
                break

        cap.release()
        cv2.destroyAllWindows()
        st.success("Webcam stopped successfully.")
