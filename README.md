<<<<<<< HEAD
# ✊🖐️✌️ Rock-Paper-Scissor: An AI Hand Gesture Classifier

Rock-Paper-Scissor is a machine learning–powered app that recognizes hand gestures in images and predicts whether they represent rock, paper, or scissors.
It features a FastAPI backend for model inference and a Streamlit frontend for an intuitive web interface.
Everything is fully Dockerized for seamless deployment and local development.

## 🚀 Features

🧠 Deep Learning Classification — EfficientNet-based model trained to detect rock, paper, or scissors.

📸 Image Upload Interface — Upload any image directly from your browser.

⚙️ FastAPI REST API — Lightweight backend serving predictions through a /predict endpoint.

🌐 Streamlit Frontend — Clean and interactive UI for testing and visualization.

🐳 Dockerized Architecture — Easy to run locally or deploy anywhere using Docker.


## 🧩 Repository Structure

This project is organized into two components: a backend (FastAPI) and a frontend (Streamlit).

```bash
└── rock-paper-scissor-app/
    ├── rock-paper-scissor_backend/      # FastAPI backend
    │   ├── api/                         # API routes
    │   │   └── main.py    
    │   ├── models/                      # Trained model (.keras)
    │   ├── rock_paper_scissor/          # Core logic: model loading & utils
    │   ├── tests/                       # Unit tests for API
    │   ├── Dockerfile                   # Backend Dockerfile
    │   └── requirements.txt
    │
    └── rock-paper-scissor_frontend/     # Streamlit app
        ├── app.py                       # Frontend entry point
        ├── Dockerfile                   # Frontend Dockerfile
        └── requirements.txt
```

---
## 🧠 Technical Overview

### 📂 Dataset

- Based on an open dataset of hand gesture images for Rock, Paper, Scissors recognition.

- Images were resized and augmented to improve generalization.

- Dataset split into training, validation, and test sets.

### 🤖 Model

- Built using Keras / TensorFlow with EfficientNet as the base.

- Trained to classify three gesture categories: rock, paper, scissors

- Achieved strong accuracy on validation images (99%).

### ⚙️ Backend (FastAPI)

- Exposes a REST API at /predict.

- Accepts an uploaded image (jpg/png) and returns:

{
  "label": "rock",
  "confidence": 0.93,
  "probabilities": {"rock": 0.93, "paper": 0.04, "scissors": 0.03}
}

- Logs activity and handles errors gracefully (invalid file, empty upload, etc


### 💻 Frontend (Streamlit)

- Provides a simple interface to upload an image and view predictions.

- It displays:

    1. Uploaded image preview

    2. Predicted label and confidence

    3. Class probabilities


### 🐳 Dockerization

- Both backend and frontend can run independently or together via Docker Compose.

- Backend image runs FastAPI with Uvicorn on port 8000.

- Frontend image runs Streamlit on port 8501.

- Images communicate via local networking in Docker.


  
---
## ⚙️ How to Run Locally

### 🧩 1. Run the Backend (API)

```bash
cd rock-paper-scissor_backend
docker build -t rps-backend .
docker run -d -p 8000:8000 --name rps-api rps-backend
```

### 💡 2. Run the Frontend (Streamlit)

```bash
cd rock-paper-scissor_frontend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

- FastAPI backend → [http://localhost:8000]

- Streamlit frontend → [http://localhost:8501]

---
## 🖼️ Demo

Web Interface (Streamlit):

( tbd ... screenshot image here!)
=======
# ✊🖐️✌️ Rock-Paper-Scissor: An AI Hand Gesture Classifier

Rock-Paper-Scissor is a machine learning–powered app that recognizes hand gestures in images and predicts whether they represent rock, paper, or scissors.
It features a FastAPI backend for model inference and a Streamlit frontend for an intuitive web interface.
Everything is fully Dockerized for seamless deployment and local development.

# 🚀 Features

🧠 Deep Learning Classification — EfficientNet-based model trained to detect rock, paper, or scissors.

📸 Image Upload Interface — Upload any image directly from your browser.

⚙️ FastAPI REST API — Lightweight backend serving predictions through a /predict endpoint.

🌐 Streamlit Frontend — Clean and interactive UI for testing and visualization.

🐳 Dockerized Architecture — Easy to run locally or deploy anywhere using Docker.

# 🧩 Repository Structure

This project is organized into two components: a backend (FastAPI) and a frontend (Streamlit).

rock-paper-scissor-app/
├── rock-paper-scissor_backend/      # FastAPI backend
│   ├── api/                         # API routes
│   │   └── main.py
│   ├── models/                      # Trained model (.keras)
│   ├── rock_paper_scissor/          # Core logic: model loading & utils
│   ├── tests/                       # Unit tests for API
│   ├── Dockerfile                   # Backend Dockerfile
│   └── requirements.txt
│
└── rock-paper-scissor_frontend/     # Streamlit app
    ├── app.py                       # Frontend entry point
    ├── Dockerfile                   # Frontend Dockerfile
    └── requirements.txt

# 🧠 Technical Overview

## 📂 Dataset

- Based on an open dataset of hand gesture images for Rock, Paper, Scissors recognition.

- Images were resized and augmented to improve generalization.

- Dataset split into training, validation, and test sets.

## 🤖 Model

- Built using Keras / TensorFlow with EfficientNet as the base.

- Trained to classify three gesture categories: rock, paper, scissors

- Achieved strong accuracy on validation images (99%).

## ⚙️ Backend (FastAPI)

- Exposes a REST API at /predict.

- Accepts an uploaded image (jpg/png) and returns:

{
  "label": "rock",
  "confidence": 0.93,
  "probabilities": {"rock": 0.93, "paper": 0.04, "scissors": 0.03}
}

- Logs activity and handles errors gracefully (invalid file, empty upload, etc.).

## 💻 Frontend (Streamlit)

- Provides a simple interface to upload an image and view predictions.

- It displays:

(1) Uploaded image preview

(2) Predicted label and confidence

(3) Class probabilities

## 🐳 Dockerization

- Both backend and frontend can run independently or together via Docker Compose.

- Backend image runs FastAPI with Uvicorn on port 8000.

- Frontend image runs Streamlit on port 8501.

- Images communicate via local networking in Docker.

# ⚙️ How to Run Locally

### 🧩 1. Run the Backend (API)
cd rock-paper-scissor_backend
docker build -t rps-backend .
docker run -d -p 8000:8000 --name rps-api rps-backend


API available at: http://localhost:8000

### 💡 2. Run the Frontend (Streamlit)
cd rock-paper-scissor_frontend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py


Frontend available at: http://localhost:8501

### 🐳 3. (Optional) Run Both via Docker Compose

In the project root (rock-paper-scissor-app/):

docker compose up --build


This will start:

FastAPI backend → http://localhost:8000

Streamlit frontend → http://localhost:8501


# 🖼️ Demo

Web Interface (Streamlit):

( tbd ... screenshot image here!)
>>>>>>> 0155356 (Final app available)
