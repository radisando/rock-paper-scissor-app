# ============================================================
# rock_paper_scissor/model.py
# Handles loading, preprocessing, and predicting with the model
# ============================================================
import os
import numpy as np
import json
from PIL import Image, ImageOps
import cv2  # for optional preprocessing or future use

import tensorflow as tf
from keras.models import load_model # Use direct keras imports
from keras.applications.efficientnet import preprocess_input

from rock_paper_scissor.utils.logging_utils import configure_logging

logger = configure_logging()


# ---- CONFIG ---
#MODEL_PATH = os.getenv("MODEL_PATH", "/home/rafael/code/rock-paper-scissor-app/rock-paper-scissor_backend/models/best_model.keras")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "..", "models", "best_model.keras"))
MODEL_PATH = os.path.abspath(MODEL_PATH)

IMG_SIZE = tuple(map(int, os.getenv("IMG_SIZE", "224,224").split(",")))
CLASS_NAMES = json.loads(os.getenv("CLASS_NAMES", '["paper","rock","scissors"]'))

# ---------- MODEL CACHE ----------
_model = None

def get_model():
    """
    Load and cache the trained model.
    """
    global _model
    print(f"🔍 Looking for model at: {MODEL_PATH}")
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"❌ Model not found at: {MODEL_PATH}")
        _model = load_model(MODEL_PATH, compile=False)
        print(f"✅ Model loaded from {MODEL_PATH}")

    return _model


def preprocess_image(pil_img: Image.Image) -> np.ndarray:
    """
    Preprocess a PIL image for prediction:
    - Convert to RGB
    - Resize to (128, 128)
    - Apply EfficientNet preprocessing
    - Add batch dimension
    """
    img = ImageOps.exif_transpose(pil_img).convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = np.array(img)
    arr = preprocess_input(arr)
    arr = np.expand_dims(arr, axis=0)  # (1,128,128,3)
    return arr


def predict_image(pil_img: Image.Image) -> dict:
    """
    Run prediction on a single PIL image.
    Returns a dictionary with label, confidence, and probabilities.
    """
    model = get_model()
    x = preprocess_image(pil_img)
    probs = model.predict(x, verbose=0)[0]
    idx = int(np.argmax(probs))
    return {
        "label": CLASS_NAMES[idx],
        "confidence": float(probs[idx]),
        "probabilities": {CLASS_NAMES[i]: float(p) for i, p in enumerate(probs)},
    }
