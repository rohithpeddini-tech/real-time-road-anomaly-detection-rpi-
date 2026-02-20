Real-Time Road Anomaly Detection using Raspberry Pi

📌 Project Overview

Road damage such as potholes, cracks, and unexpected obstacles is a major contributor to traffic accidents, vehicle damage, and inefficient infrastructure maintenance. This project proposes an edge-AI based monitoring system that detects road anomalies from dashcam footage in near real time. The system is designed for deployment on low-power devices like the , enabling on-device processing without dependency on cloud connectivity.

---

🎯 Objectives

- Detect potholes, cracks, and obstacles from road footage
- Enable near real-time processing on edge hardware
- Log detection frames for maintenance analysis
- Demonstrate a scalable smart-city monitoring solution

---

⚙️ Methodology

The system processes road footage frame-by-frame using computer vision and a lightweight YOLO-based object detection model. Each frame is resized and passed through the model to identify potential anomalies. Detected regions are highlighted with bounding boxes and stored for review.

The architecture follows an edge-computing approach where inference occurs locally, reducing latency and bandwidth usage while improving responsiveness.

---

🧰 Hardware & Software

Target Hardware

- Raspberry Pi (deployment platform)
- Camera module / dashcam input
- MicroSD storage

Software Stack

- Python
- OpenCV
- YOLOv8 lightweight detection model
- NumPy

---

📊 Results

The system successfully identifies irregular road surfaces and obstacles from test footage. Annotated frames are stored automatically for inspection. When deployed on optimized edge hardware, the model can achieve near real-time performance suitable for practical monitoring applications.

---

🚀 Applications

- Smart city road maintenance systems
- Driver safety and hazard alerts
- Infrastructure condition monitoring
- Autonomous navigation support

---

🔮 Future Scope

Future enhancements include model training on India-specific road datasets, integration with municipal dashboards, GPS-based anomaly mapping, and automated maintenance alerts.

---

📎 Repository Structure

- "src/" → detection code
- "models/" → model information
- "sample_input/" → test footage
- "output/" → detection results
- "docs/" → methodology & hardware notes
- "results/" → performance summary

---

👨‍💻 Author

Student Project – Electronics & Communication Engineering
Edge AI and Computer Vision Application
