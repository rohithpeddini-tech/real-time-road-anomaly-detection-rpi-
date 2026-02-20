from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("sample_input/road.mp4")

frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, imgsz=320, conf=0.4)
    annotated = results[0].plot()

    cv2.imwrite(f"output/frame_{frame_id}.jpg", annotated)
    frame_id += 1

cap.release()
print("Processing complete")
