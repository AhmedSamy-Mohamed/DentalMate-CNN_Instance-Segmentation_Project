# 🦷 DentalMate

## Dental Condition Detection & Instance Segmentation

DentalMate is a Computer Vision project designed to detect and segment different dental conditions from real intraoral dental images.

The project uses **YOLO11s-Seg** for instance segmentation and provides an interactive **Streamlit web application** for real-time inference.

---

## 🚀 Live Demo

Try DentalMate online:

https://dentalmate-cnninstance-segmentationproject-vm8nzsonhu2dixazmjg.streamlit.app/

---

## 🎯 Project Objective

The goal of DentalMate is to build an AI-powered dental image analysis system capable of:

- Detecting dental conditions
- Localizing affected regions
- Performing instance segmentation
- Providing confidence scores for predictions
- Allowing users to test the trained model through a web interface

> **Note:** DentalMate is an educational/research prototype and is not intended to provide medical diagnosis.

---

## 🧠 Model

**Architecture:** YOLO11s-Seg

**Task:** Instance Segmentation

**Framework:** Ultralytics YOLO

**Training:** 100 epochs

**Parameters:** 10,069,912

**GFLOPs:** 32.9

---

## 🦷 Supported Classes

DentalMate supports 8 classes:

1. Caries - Filling
2. Caries - RCT
3. Tooth Decay - Crown
4. Abrasion - Filling
5. Fractured - Filling
6. Fractured Teeth - Crown
7. Multiple Tooth Loss - Implant
8. Single Tooth - Bridge

---

## 📊 Validation Results

### Object Detection

| Metric | Score |
|---|---:|
| Precision | 88.58% |
| Recall | 76.37% |
| mAP@50 | 83.73% |
| mAP@50-95 | 73.28% |

### Instance Segmentation

| Metric | Score |
|---|---:|
| Precision | 88.58% |
| Recall | 76.37% |
| mAP@50 | 83.94% |
| mAP@50-95 | 65.52% |

Validation was performed on **50 images containing 171 annotated instances**.

---

## 📈 Per-Class Performance

| Class | Box mAP@50-95 | Mask mAP@50-95 |
|---|---:|---:|
| Caries - Filling | 37.94% | 34.85% |
| Caries - RCT | 67.08% | 64.70% |
| Tooth Decay - Crown | 73.28% | 65.52% |
| Abrasion - Filling | 76.28% | 71.04% |
| Fractured - Filling | 83.85% | 80.67% |
| Fractured Teeth - Crown | 87.49% | 83.54% |
| Multiple Tooth Loss - Implant | 89.55% | 69.65% |
| Single Tooth - Bridge | 70.77% | 54.18% |

---

## 🖥️ Streamlit Application

The web application allows users to:

- Upload a dental image
- Select a confidence threshold
- Run DentalMate inference
- Visualize detected regions
- View predicted dental conditions
- View confidence scores

---

## 🛠️ Technologies

- Python
- YOLO11s-Seg
- Ultralytics
- PyTorch
- OpenCV
- Pillow
- Streamlit
- Git & GitHub

---

## 📂 Project Structure

```text
DentalMate-CNN_Instance-Segmentation_Project/
│
├── app.py
├── best.pt
├── requirements.txt
├── .gitignore
└── README.md 

⚙️ Installation

Clone the repository:

git clone https://github.com/AhmedSamy-Mohamed/DentalMate-CNN_Instance-Segmentation_Project.git

Navigate to the project:

cd DentalMate-CNN_Instance-Segmentation_Project

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
🧪 Example Workflow
Dental Image
     ↓
YOLO11s-Seg
     ↓
Object Detection
     +
Instance Segmentation
     ↓
Dental Condition
     +
Confidence Score
     ↓
Streamlit Visualization
⚠️ Disclaimer

DentalMate is an academic Computer Vision project developed for educational and research purposes.

The predictions should not be considered a medical diagnosis or a substitute for professional dental examination.

👨‍💻 Author

Ahmed Samy Mohamed Othman

Faculty of Engineering – Tanta University

Department of Mechatronics

⭐ Project Links

GitHub:

https://github.com/AhmedSamy-Mohamed/DentalMate-CNN_Instance-Segmentation_Project

Live Demo:

https://dentalmate-cnninstance-segmentationproject-vm8nzsonhu2dixazmjg.streamlit.app/