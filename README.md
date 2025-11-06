# ✊🖐️✌️ Rock-Paper-Scissors App (AI gesture classifier)
- Rock-Paper-Scissor is a machine learning–powered web app that recognizes hand gestures in images, predicts whether they represent rock, paper, or scissors and lets user play against the machine.

- Originally built with a FastAPI backend for inference and fully Dockerized for local deployment, the project has since been streamlined and deployed on Hugging Face Spaces using Streamlit — simplifying hosting, reducing infrastructure overhead, and making the app instantly accessible online.


---
## 🚀 Features

🧠 Deep Learning Classification – EfficientNet-based model trained for robust gesture recognition
 
📸 Interactive Web Interface – Upload an image and play against the computer in real time

⚙️ Hugging Face Deployment – Zero-setup web access and continuous availability

🐳 Dockerized Environment – Reproducible local setup and flexible deployment


---
## 🧩 Repository Structure

• This project is organized with the following structure to match Hugging Face requirements:

```bash
    ├── rock-paper-scissor_app    /      
    │   ├── app.py                       # Frontend entry point                 
    │   ├── Dockerfile                   # Backend Dockerfile
    │   └── models/                      # Trained model
    │       └── best_model.keras
    │   ├── requirements.txt
    │   └── rock_paper_scissor/          # Core logic: model loading & utils
    │       └── model.pyr
    │       └── utils
    │           └── logging_utils.py
```

---
## 🧠 Technical Overview

### 📂 Dataset

- Based on an open [Kaggle dataset](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors) of hand gesture images for Rock, Paper, Scissors.

- Images were resized and augmented to improve generalization.


### 🤖 Model

- Built using Keras / TensorFlow with EfficientNet as the base.

- Trained to classify three gesture categories: rock, paper, scissors

- Achieved strong accuracy on validation images (99%).
  

### ⚙️ Backend

- Initially exposed to a REST API at /predict. But then deployed at Hugging Face (no need of API)

- Accepts an uploaded image (jpg/png) and returns the label (e.g. rock), and the confidence percentage.


### 💻 Frontend (Streamlit)

- Provides a simple interface to upload an image and view predictions.

- It displays: Uploaded image preview, predicted label and confidence and random machine choice of Rock, Paper or Scissors.

  
---
## 🖼️ Demo
[Try the App!](https://huggingface.co/spaces/radisando/rock-paper-scissor-app)

![portfolio](https://github.com/user-attachments/assets/7e010fd6-74b1-4926-a1e6-3f0c1e0d8f88)


