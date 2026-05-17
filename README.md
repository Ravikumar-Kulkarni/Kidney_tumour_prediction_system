# Kidney_tumour_prediction_system

# Kidney Disease Prediction using CNN & VGG16

A Deep Learning based Kidney Disease Prediction System developed using TensorFlow/Keras and VGG16 architecture.  
This project uses a Convolutional Neural Network (CNN) with Transfer Learning to classify kidney disease from medical images.

The model is deployed using a Flask web application where users can upload kidney scan images and get real-time predictions.

---

# 📌 Project Overview

The main objective of this project is to build an intelligent kidney disease prediction system using Deep Learning and Computer Vision techniques.

The project uses:
- CNN (Convolutional Neural Network)
- VGG16 Transfer Learning
- Flask Deployment
- MLflow Experiment Tracking
- DagsHub Integration

---

# 🚀 Features

- CNN-based Image Classification
- VGG16 Transfer Learning
- Flask Web Application
- Real-Time Prediction
- Image Upload Functionality
- MLflow Experiment Tracking
- DagsHub Integration
- Deep Learning Pipeline
- User-Friendly Interface

---

# 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Flask
- HTML/CSS
- VGG16
- CNN
- MLflow
- DagsHub

---

# 🧠 Deep Learning Model

This project uses the **VGG16 Pretrained Model** for feature extraction and image classification.

### Model Workflow
1. Image Upload
2. Image Preprocessing
3. Feature Extraction using VGG16
4. CNN Classification
5. Prediction Output

---

# 📂 Project Structure

```bash
itv_kidney_prediction/
│
├── artifacts/
│   ├── model.h5
│
├── mlruns/
│
├── static/
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── src/
│   ├── pipeline/
│   ├── utils.py
│   └── predict.py
│
├── notebook/
│   └── kidney_prediction.ipynb
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🖼️ Dataset

The dataset contains kidney medical images used for classification.

### Image Classes
- Normal Kidney
- Kidney Disease

---

# ⚙️ Model Training

The VGG16 pretrained architecture is used with custom CNN layers for classification.

### Training Steps
- Image Preprocessing
- Data Augmentation
- Transfer Learning
- Fine-Tuning
- Model Evaluation
- Model Saving

---

# 📊 Model Architecture

- VGG16 Base Model
- Flatten Layer
- Dense Layers
- Dropout Layer
- Output Layer

---

# 📈 MLflow Experiment Tracking

This project uses **MLflow** to track:
- Model Parameters
- Accuracy Metrics
- Training Experiments
- Model Versions
- Loss Curves

MLflow helps monitor and compare multiple deep learning experiments efficiently.

---

# 🔗 DagsHub Integration

The project is integrated with **DagsHub** for:
- ML Experiment Tracking
- Remote MLflow Server
- Version Control
- Collaboration
- Model Management

DagsHub provides an organized platform for managing Machine Learning workflows and experiments.

---

# 🌐 Flask Web Application

The Flask application allows users to:
- Upload kidney images
- Predict disease status
- View prediction results instantly

---

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
```

---

## 2️⃣ Create Virtual Environment

```bash
conda create -p venv python=3.10 -y
```

Activate environment:

```bash
conda activate venv/
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run MLflow Tracking Server (Optional)

```bash
mlflow ui
```

MLflow UI will run at:

```bash
http://127.0.0.1:5000
```

---

## 5️⃣ Run Flask Application

```bash
python app.py
```

---

# 🖥️ Open Flask App in Browser

```bash
http://127.0.0.1:8000/
```

---

# 📈 Future Improvements

- Docker Deployment
- Cloud Deployment
- Better UI Design
- Mobile Application
- Multi-Class Kidney Disease Detection

---

# 📷 Output

The system predicts:
- Kidney Disease Detected
- Normal Kidney

with prediction confidence score.

---

# 🤝 Contribution

Contributions are welcome.  
Feel free to fork and improve this project.

---

# 📄 License

This project is developed for educational and learning purposes.

---

# 👨‍💻 Author

Ravikumar Kulkarni  
Data Science & Deep Learning Enthusiast
