import cv2
import numpy as np
from ultralytics import YOLO


def detect_objects(image_path, model_path="models/yolov8m.pt", selected_class=None):
    """
    Runs YOLO object detection on the given image and returns:
      - the original image with bounding boxes
      - the highlighted version (only detected objects visible, rest black)
      - a dictionary of object counts
    """

    # Load YOLO model
    model = YOLO(model_path)

    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Unable to read image: {image_path}")

    # Run YOLO detection
    results = model(image_path)
    detections = results[0].boxes

    # Create a blank black image (same size as original)
    highlighted = np.zeros_like(img)

    object_counts = {}
    for box in detections:
        cls = int(box.cls[0])
        class_name = model.names[cls]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Filter based on selected class
        if not selected_class or selected_class.lower() == class_name.lower():
            # Draw bounding box and label on original image
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

            # Copy detected region onto highlighted image
            highlighted[y1:y2, x1:x2] = img[y1:y2, x1:x2]

            # Count detected objects
            object_counts[class_name] = object_counts.get(class_name, 0) + 1

    total_count = sum(object_counts.values())

    return img, highlighted, object_counts, total_count
